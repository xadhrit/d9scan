// port scanning through syn-flood protections
/*
 For ensure if a service exist on a port :
    if you receive any additional packets from the target after you've established a connection.
    1. Capture the packets
    2. Check if they are trasmitted with a TCP flag (CWR,ECE,URG, ACK, PSH, RST, SYN, FIN)
*/

package main

import (
	"fmt"
	"log"
	"net"
	"os"
  "strings"
  "time"

	"github.com/google/gopacket"
	"github.com/google/gopacket/pcap"
)

var (
	snaplen = int32(320)
	promise = true
	timeout = pcap.BlockForever
	filter  = "tcp[13] == 0x11 ot tcp[13] == 0x10 or tcp[13] == 0x18"
	/*
	   only looking for
	   * ACK && FIN : 0x11
	   * ACK: 0x10
	   * ACK and PSH 0x18
	*/
	devFound = false
	results  = make(map[string]int)
)

func capture(targetDev, target string) {
	handle, err := pcap.OpenLive(targetDev, snaplen, promise, timeout)

	if err != nil {
		log.Panicln(err)
	}

	defer handle.Close()

	if err := handle.SetBPFFilter(filter); err != nil {
		log.Panicln(err)
	}

	source := gopacket.NewPacketSource(handle, handle.LinkType())

	fmt.Println("Capturing packets")
	for packet := range source.Packets() {
		networkLayer := packet.NetworkLayer()
		if networkLayer == nil {
			continue
		}

		transportLayer := packet.TransportLayer()
		if transportLayer == nil {
			continue
		}

		sourceHost := networkLayer.NetworkFlow().Src().String()
		sourcePort := transportLayer.TransportFlow().Src().String()

		if sourceHost != target {
			continue
		}

		results[sourcePort] += 1
	}
}

func explode (portString string) ([]string , error){
     ret := make([]string, 0)

     ports := strings.Split(portString, ",")
     for _, port := range ports {
        port := strings.TrimSpace(port)
        ret = append(ret, port)
     }

     return ret, nil
}


func main() {
	if len(os.Args) != 4 {
		log.Fatalln("Usage: main.go <capture_targetDev><target_ip><port1,port2, port3>")
	}

	devices, err := pcap.FindAllDevs()

	if err != nil {
		log.Panicln(err)
	}

	targetDevice := os.Args[1]

  for _, device := range devices {
		if device.Name == targetDevice {
			devFound = true
		}
	}

	if !devFound {
		log.Panicf("Device named %s' does not exist\n ", targetDevice)
	}

	ip := os.Args[2]

	go capture(targetDevice, ip)

	time.Sleep(1 * time.Second)

	ports, err := explode(os.Args[3])

	if err != nil {
		log.Panicln(err)
	}

	for _, port := range ports {
		target := fmt.Sprintf("%s %s", ip, port)

		fmt.Println("Trying ", target)

		e, err := net.DialTimeout("tcp", target, 1000*time.Millisecond)

		if err != nil {
			continue
		}

		e.Close()
	}

	time.Sleep(2 * time.Second)

  for port, probability := range results {
		if probability >= 1 {
			fmt.Println("port %s open (probability: %d)\n", port, probability)
		}
	}
}

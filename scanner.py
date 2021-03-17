from socket import *

IP = input("Enter the IP address that you want to scan: ")
ports = range(1, 1001)

for port in ports:
	TCP_socket = socket(AF_INET, SOCK_STREAM)
	try:
		TCP_socket.settimeout(1)
		TCP_socket.connect((IP, port))
		print("[OPEN]: IP:", IP, "Port", port, "OPEN")
		TCP_socket.close()

	except:
		print("[CLOSED]: IP:", IP, "Port", port, "CLOSED")
		TCP_socket.close()
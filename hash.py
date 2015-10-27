import sys

f = open(sys.argv[1], 'r')

plaintext = ""
string = f.readline()
while(string != ""):
	plaintext += string
	string = f.readline()
f.close()

hash = ""
ciphertext= ""
while(len(ciphertext) > 24 or ciphertext == ""):
	ciphertext = ""
	for i in range(len(plaintext)/2):
		try:
			first = plaintext[i*2]
			second = plaintext[i*2+1]
			ciphertext += first ^ second
		except Exception:
			first = plaintext[i*2]
			ciphertext += first

	plaintext = ciphertext
	print(ciphertext)

print(ciphertext)

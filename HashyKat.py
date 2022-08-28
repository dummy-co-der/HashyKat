#!/usr/bin/python3
import hashlib
import time
from hashlib import md5
import sys
import os
from termcolor import colored


try:

	def banner():
		print(""" 
		        /\             /\\
                       |` \_,--="=--,_/ `|
                       \ ."  :'. .':  ". /
                      ==)  _ :  '  : _  (==
                        |>/O\   _   /O\<|
                        | \-"~` _ `~"-/ |   
                       >|`===. \_/ .===`|<
                 .-"-.   \==='  |  '===/   .-"-.
.---------------{'. '`}---\,  .-'-.  ,/---{.'. '}---------------.
 )              `"---"`     `~-===-~`     `"---"`              (
(           _   _           _           _  __     _             )
 )         | | | | __ _ ___| |__  _   _| |/ /__ _| |_          (
(          | |_| |/ _` / __| '_ \| | | | ' // _` | __|          )
 )         |  _  | (_| \__ \ | | | |_| | . \ (_| | |_          (
(          |_| |_|\__,_|___/_| |_|\__, |_|\_\__,_|\__|          )
 )                                |___/                        (
 (                                       ~ By Anuj Maheshwari  )    
'---------------------------------------------------------------' """)
		
	def for_md5():
		wordlis=input(" Enter the path of wordlist: ")


		with open(wordlis, "r", encoding='utf-8') as wordlist:
			hassh=input("Enter the hash: ")
			print('\n')
		
			for password in wordlist:
			# x is a variable storing the encrypting key of password
				password = password.replace("\n","")
				x = hashlib.md5(str(password).encode('utf-8')).hexdigest()
				if hassh == x:
				
					print(colored("			[*] Status:- Cracked: " + password,"green",attrs=['bold','reverse']))
					sys.exit(1)
				else:
				        continue
			print(colored("                 [*] Status:- Not Cracked. Hash not found! Use another wordlist.", "red",attrs=['bold','reverse']))	        	
				        
			sys.exit(1)


	def for_SHA1():
		wordlis=input(" Enter the path of wordlist: ")


		with open(wordlis, "r", encoding='utf-8') as wordlist:
			hassh=input("Enter the hash: ")
			print('\n')
		
			for password in wordlist:
			# x is a variable storing the encrypting key of password
				password = password.replace("\n","")
				x = hashlib.sha1(str(password).encode('utf-8')).hexdigest()
				if hassh == x:
				
					print(colored("			[*] Status:- Cracked: " + password,"green",attrs=['bold','reverse']))
					sys.exit(1)
				else:
				        continue
			print(colored("                 [*] Status:- Not Cracked. Hash not found! Use another wordlist.", "red",attrs=['bold','reverse']))	        	
				        
			sys.exit(1)


	def for_SHA224():
		wordlis=input(" Enter the path of wordlist: ")


		with open(wordlis, "r", encoding='utf-8') as wordlist:
			hassh=input("Enter the hash: ")
			print('\n')
		
			for password in wordlist:
			# x is a variable storing the encrypting key of password
				password = password.replace("\n","")
				x = hashlib.sha224(str(password).encode('utf-8')).hexdigest()
				if hassh == x:
				
					print(colored("			[*] Status:- Cracked: " + password,"green",attrs=['bold','reverse']))
					sys.exit(1)
				else:
				        continue
			print(colored("                 [*] Status:- Not Cracked. Hash not found! Use another wordlist.", "red",attrs=['bold','reverse']))	        	
				        
			sys.exit(1)


	def for_SHA256():
		wordlis=input("Enter the path of wordlist: ")


		with open(wordlis, "r", encoding='utf-8') as wordlist:
			hassh=input("Enter the hash: ")
			print('\n')
		
			for password in wordlist:
			# x is a variable storing the encrypting key of password
				password = password.replace("\n","")
				x = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
				if hassh == x:
				
					print(colored("			[*] Status:- Cracked: " + password,"green",attrs=['bold','reverse']))
					sys.exit(1)
				else:
				        continue
			print(colored("                 [*] Status:- Not Cracked. Hash not found! Use another wordlist.", "red",attrs=['bold','reverse']))	        	
				        
			sys.exit(1)


	def for_SHA384():
		wordlis=input("Enter the path of wordlist: ")


		with open(wordlis, "r", encoding='utf-8') as wordlist:
			hassh=input("Enter the hash: ")
			print('\n')
		
			for password in wordlist:
			# x is a variable storing the encrypting key of password
				password = password.replace("\n","")
				x = hashlib.sha384(str(password).encode('utf-8')).hexdigest()
				if hassh == x:
				
					print(colored("			[*] Status:- Cracked: " + password,"green",attrs=['bold','reverse']))
					sys.exit(1)
				else:
				        continue
			print(colored("                 [*] Status:- Not Cracked. Hash not found! Use another wordlist.", "red",attrs=['bold','reverse']))	        	
				        
			sys.exit(1)


	def for_SHA512():
		wordlis=input("Enter the path of wordlist: ")


		with open(wordlis, "r", encoding='utf-8') as wordlist:
			hassh=input("Enter the hash: ")
			print('\n')
		
			for password in wordlist:
			# x is a variable storing the encrypting key of password
				password = password.replace("\n","")
				x = hashlib.sha512(str(password).encode('utf-8')).hexdigest()
				if hassh == x:
				
					print(colored("			[*] Status:- Cracked: " + password,"green",attrs=['bold','reverse']))
					sys.exit(1)
				else:
				        continue
			print(colored("                 [*] Status:- Not Cracked. Hash not found! Use another wordlist.", "red",attrs=['bold','reverse']))	        	
				        
			sys.exit(1)
			

	def for_SHA3_224():
		wordlis=input("Enter the path of wordlist: ")


		with open(wordlis, "r", encoding='utf-8') as wordlist:
			hassh=input("Enter the hash: ")
			print('\n')
		
			for password in wordlist:
			# x is a variable storing the encrypting key of password
				password = password.replace("\n","")
				x = hashlib.sha3_224(str(password).encode('utf-8')).hexdigest()
				if hassh == x:
				
					print(colored("			[*] Status:- Cracked: " + password,"green",attrs=['bold','reverse']))
					sys.exit(1)
				else:
				        continue
			print(colored("                 [*] Status:- Not Cracked. Hash not found! Use another wordlist.", "red",attrs=['bold','reverse']))	        	
				        
			sys.exit(1)		


	def for_SHA3_256():
		wordlis=input("Enter the path of wordlist: ")


		with open(wordlis, "r", encoding='utf-8') as wordlist:
			hassh=input("Enter the hash: ")
			print('\n')
		
			for password in wordlist:
			# x is a variable storing the encrypting key of password
				password = password.replace("\n","")
				x = hashlib.sha3_256(str(password).encode('utf-8')).hexdigest()
				if hassh == x:
				
					print(colored("			[*] Status:- Cracked: " + password,"green",attrs=['bold','reverse']))
					sys.exit(1)
				else:
				        continue
			print(colored("                 [*] Status:- Not Cracked. Hash not found! Use another wordlist.", "red",attrs=['bold','reverse']))	        	
				        
			sys.exit(1)


	def for_SHA3_384():
		wordlis=input("Enter the path of wordlist: ")


		with open(wordlis, "r", encoding='utf-8') as wordlist:
			hassh=input("Enter the hash: ")
			print('\n')
		
			for password in wordlist:
			# x is a variable storing the encrypting key of password
				password = password.replace("\n","")
				x = hashlib.sha3_384(str(password).encode('utf-8')).hexdigest()
				if hassh == x:
				
					print(colored("			[*] Status:- Cracked: " + password,"green",attrs=['bold','reverse']))
					sys.exit(1)
				else:
				        continue
			print(colored("                 [*] Status:- Not Cracked. Hash not found! Use another wordlist.", "red",attrs=['bold','reverse']))	        	
				        
			sys.exit(1)	
					

	def for_SHA3_512():
		wordlis=input("Enter the path of wordlist: ")


		with open(wordlis, "r", encoding='utf-8') as wordlist:
			hassh=input("Enter the hash: ")
			print('\n')
		
			for password in wordlist:
			# x is a variable storing the encrypting key of password
				password = password.replace("\n","")
				x = hashlib.sha3_512(str(password).encode('utf-8')).hexdigest()
				if hassh == x:
				
					print(colored("			[*] Status:- Cracked: " + password,"green",attrs=['bold','reverse']))
					sys.exit(1)
				else:
				        continue
			print(colored("                 [*] Status:- Not Cracked. Hash not found! Use another wordlist.", "red",attrs=['bold','reverse']))	        	
				        
			sys.exit(1)		 


	if __name__ == "__main__":
		os.system('clear')
		banner()

		print(colored("[1] For md5","yellow",attrs=['bold']))
		print(colored("[2] For SHA1","yellow",attrs=['bold']))
		print(colored("[3] For SHA224","yellow",attrs=['bold']))
		print(colored("[4] For SHA256","yellow",attrs=['bold']))
		print(colored("[5] For SHA384","yellow",attrs=['bold']))
		print(colored("[6] For SHA512","yellow",attrs=['bold']))
		print(colored("[7] For SHA3_224","yellow",attrs=['bold']))
		print(colored("[8] For SHA3_256","yellow",attrs=['bold']))
		print(colored("[9] For SHA3_384","yellow",attrs=['bold']))
		print(colored("[10] For SHA3_512","yellow",attrs=['bold']))
	

		print('\n')

		select = int(input("Enter your choice: "))

		if select == 1:
			for_md5()
		if select == 2:
			for_SHA1()
		if select == 3:
			for_SHA224()
		if select == 4:
			for_SHA256()
		if select == 5:
			for_SHA384()
		if select == 6:
			for_SHA512()
		if select == 7:
			for_SHA3_224()
		if select == 8:
			for_SHA3_256()
		if select == 9:
			for_SHA3_384()
		if select == 10:
			for_SHA3_512()
		if select > 10:
			print("Not in scope")
			sys.exit(1)

except KeyboardInterrupt:
	print(colored("\n\n Stop By User!\n","red",attrs=['blink','bold','reverse']))

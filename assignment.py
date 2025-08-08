# a registration / login portal system


users_db = {"name":"samuel", "password":1234, "account":4000.0, "is_verified":True}


account = 0
verification_fee = 1500
print("""
   *---------------------------------------*
   |    Login and Registeration Portal     |
   |   ________________________________    |
   |   commands:                           |
   |   enter "login" to login              |
   |   enter "register" to register        |
   *---------------------------------------*

""")

command = input("enter a command to continue: ").lower().strip()

if command == "register":
	print("welcome to account creation menu")
	name = input("enter a name to create an account: ").capitalize()
	if name == users_db["name"]:
		print("username taken")
	else:
			
		password = input("enter a password to complete your account creation ")
		print("account creation success!")
		account_funding = float(input("how much do you want to deposit?: "))
		account += account_funding
		confirm = input("will you like to verify account?, a fee if 1500 will be incured(yes/no): ").lower()
		if confirm == "yes":
			if verification_fee > account:
				print("insufficient balance, verification terminated")
					
			else:	
				print("account verification success!")
				print("A verification fee of 1500 deducted from your balance")			
				user = {
					"name": name,
					"password": password,
					"account": account_funding
					}
				users_db.update(user)        
				users_db["account"] -= verification_fee     
				print(users_db)

		elif confirm == "no":
			print("verification skipped")
			user = {
				"name": name,
				"password": password,
				"account": account_funding
						        }
			user["is_verified"] = False
			users_db.update(user)
			print(users_db)
					
		else:
			print("invalid input")			
					 
			
elif command == "login":
	print("welcome to the login screen")
	name = input("enter your account username to access your account: ").lower()
	if name == users_db["name"]:
		password = int(input("enter your account password to login: "))
		if password == users_db["password"]:
			print("login success!")	
			confirm = input("would you like to verify your account?(yes/no): ")
			if confirm == "yes":
				if users_db["account"] < verification_fee:
					print("insufficient balance verification terminated")
							
				else:
					print("verification success!")
					users_db["account"] -= verification_fee
					print(users_db)
						
			elif confirm == "no":
				print("verification terminated")			 
		else:
			print("wrong password")
	else:
		print("user does not exist")
							
								
else:
	print("invalid input")		       





























































# not currently using user class
class User:
    def __init__(self):
        self.user = ""
        self.password = ""
        self.port = ""

user = input("Please type bitcoin.conf username: ")
password = input("Please type bitcoin.conf password: ")
testnet = input("Would you like to use the testnet port 18332 (Y/n): ")
if (testnet=="n"):
	port = input("Please type the port for your RPC server: ")
else:
	port = 18332

print(user, password, port)

# RETURN USER / PASSWORD / PORT TO MY PYTHON MODULE

import pexpect

#establishing the connection
ip_address = raw("What IP address do you want to connect to? \n")

username = "admin"
password = "cisco"
test1 = 0

#creating pexpect session
session = pexpect.spawn('telnet ' + ip_address, timeout = 10)
result = session.expect(['Username:', pexpect.TIMEOUT])


if result != 0:
    print("--- FAILURE CREATING SESSION FOR: ---", ip_address)
    exit()

session.expect("Username: ")
session.sendline(username + "\n")
test1 = 1


if test1 != 0:
	session.expect("Password: ")
	session.sendline(password + "\n")
	
if result != 0:
	print("--- FAILURE ENTERING PASSWORD: ---", password)
	exit()
	

print ("Success connecting to: ", ip_address)
session.readline ("Username")
print ("Username: ", username)
session.readline ("Password")
print ("Password: ", password)
print ("\n")


#Makes the session interactable
session.interact()

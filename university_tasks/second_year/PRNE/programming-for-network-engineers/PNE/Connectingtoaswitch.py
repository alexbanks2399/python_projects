import pexpect

#establishing the connection
ip_address = raw_input("What IP address do you want to connect to? \n")

username = "admin"
password = "cisco"

#creating pexpect session
session = pexpect.spawn('telnet ' + ip_address, timeout = 10)
result = session.expect(['Username:', pexpect.TIMEOUT])

# Session expecting password, enter it here
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT])

print"\nSuccessful connection to: ", ip_address
print "\nDone"

import pexpect
import time

password='PaloAlto123!'
promptfw = '> $'
promptos = '$ '

user = input('Enter your username: ')
passwd = input('Enter your password: ')
ip = input('Enter the fw ip/fqdn: ')

session = pexpect.spawn('ssh ' + user + '@' + ip)
session.expect('Password: ')
session.sendline(passwd)
session.expect(promptfw)
session.sendline('set cli scripting-mode on')
session.expect(promptfw)
session.sendline('set cli pager off')
session.expect(promptfw)

while True:

    session.sendline('show clock')
    session.expect(promptfw)
    output = '> '
    output += session.before.decode('utf-8')

    session.sendline('show session info')
    session.expect(promptfw)
    output += session.before.decode('utf-8')
    
    
    session.sendline('show system info')
    session.expect(promptfw)
    output += session.before.decode('utf-8')
    
    session.sendline('show session all')
    session.expect(promptfw)
    output += session.before.decode('utf-8')
    print()


    for line in output.split('\n'):
								if '@' not in line:
								    print(line)
    time.sleep(10)






    
            
        


import pexpect
import getpass
import time

def sanitize_output(feed):
    output = ''
    output += feed
    for line in output.split('\n'):
        if 'admin' not in line:
            print(line)

username = input('Please enter your corp username: ')
password = getpass.getpass(prompt = 'Please enter your corp Password: ')
fwid = input('Please provide the id of the Prisma Firewall: ')

promptfw = '> $'
promptos = '\$ $'

session = pexpect.spawn('ssh ' + username + '@dl1-jumpbox-01.cyr.pan.local')
session.expect('Password: ')
session.sendline(password)
session.expect('authentication:')
time.sleep(15)
session.sendline()
sanitize_output(session.before.decode('utf-8'))
session.expect(promptos)
session.sendline('dzdo gpcs_login.py -e prod1 -i ' + fwid)
sanitize_output(session.before.decode('utf-8'))
session.expect(promptfw)
session.sendline('set cli pager off')
session.expect(promptfw)
sanitize_output(session.before.decode('utf-8'))
session.sendline('set cli scripting-mode on')
session.expect(promptfw)
sanitize_output(session.before.decode('utf-8'))

while True:
    session.sendline('show clock')
    session.expect(promptfw)
    sanitize_output(session.before.decode('utf-8'))
    session.sendline('show running resource-monitor')
    session.expect(promptfw)
    sanitize_output(session.before.decode('utf-8'))
    session.sendline('show counter global filter delta yes')
    session.expect(promptfw)
    sanitize_output(session.before.decode('utf-8'))
    time.sleep(30)


        



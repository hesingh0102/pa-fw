import pexpect
import time
import datetime

passwd = 'admin'
prompt ='> $'




while True:
  #f=open("gc-logs.txt","a+")
  fw = pexpect.spawn('ssh admin@10.193.87.252') # Replace username with your userid
  # fw.expect('please acknowledge:\r\nDo you accept and acknowledge the statement above ? (yes/no) : ')
  # fw.sendline('yes')

  fw.expect('Password: ')
  fw.sendline(passwd)
  fw.expect(prompt)

  fw.sendline('set cli scripting-mode on')
  fw.expect(prompt)

  fw.sendline('set cli pager off')
  fw.expect(prompt)

  fw.sendline('show clock')
  fw.expect(prompt)
  output = '> '
  output += fw.before.decode('utf-8')



  fw.sendline('show running resource-monitor second last 5')
  fw.expect(prompt)
  output += fw.before.decode('utf-8')


  fw.sendline('show counter global filter delta yes')
  fw.expect(prompt)
  output += fw.before.decode('utf-8')


  fw.sendline('show session info')
  fw.expect(prompt)
  output += fw.before.decode('utf-8')


  fw.sendline('show session all filter count yes')
  fw.expect(prompt)
  output += fw.before.decode('utf-8')


  fw.sendline('debug dataplane pool statistics')
  fw.expect(prompt)
  output += fw.before.decode('utf-8')

  fw.sendline('show session packet-buffer-protection zones')
  fw.expect(prompt)
  output += fw.before.decode('utf-8')

  fw.sendline('show session packet-buffer-protection')
  fw.expect(prompt)
  output += fw.before.decode('utf-8')


  fw.sendline('show session meter')
  fw.expect(prompt)
  output += fw.before.decode('utf-8')

  fw.sendline('show clock')
  fw.expect(prompt)
  output += fw.before.decode('utf-8')

  fw.sendline('show counter global filter delta yes severity error')
  fw.expect(prompt)
  output += fw.before.decode('utf-8')

  
  fw.sendline('show running resource-monitor minute last 1')
  fw.expect(prompt)
  output += fw.before.decode('utf-8')


  fw.sendline('show counter rate ethernet1/1')#Ingress interface
  fw.expect(prompt)
  output += fw.before.decode('utf-8')


  fw.sendline('show counter rate ethernet1/2')#egress interface
  fw.expect(prompt)
  output += fw.before.decode('utf-8')


  fw.sendline('show running resource-monitor ingress-backlogs')
  fw.expect(prompt)
  output +='\n> '
  output += fw.before.decode('utf-8')

  for line in output.split('\n'):
    if 'admin' not in line:
      print(line)
      #f.write(line)
  #f.close()
  time.sleep(10)

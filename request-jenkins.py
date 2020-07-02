import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from requests.auth import HTTPBasicAuth

filew = open('sanitized-1.txt', 'w+')
ids = input('Please provide the job id of Jenkins: ')
jobname = input('Please eneter the exact name of the job - case sensitive: ')
url1 = 'https://sre-tools.pan.local:8443/job/'
url2 = '/consoleText'
url = url1 + jobname + '/' + ids + url2
print(url)
res = requests.get(url, auth = ('username', 'password'), verify=False)
print (res.status_code)
filew.write(res.text)
filew.close()

file = open('sanitized-1.txt', 'r')
for line in file:
    if ('\\r\\n\\t' in line):
        line = line.replace('\\r\\n\\t','\n')
    elif ('\\r\\n' in line):               
        line = line.replace('\\r\\n','\n')
    print(line)

file.close()




import requests

#Cpanel url for new website
hostname="tlj76e1ct6dh2fmvpfm3371e2.canarytokens.com"

user="admin"
password="Nto#@lk<JJ_(d.>"

try:
    
    session = requests.Session()
    
    #login as admin
    session.auth = (user, password)
    
    auth = session.post('https://' + hostname)
    response = session.get('https://' + hostname + '/cpanel/settings')
    
    if response.ok:
        print("Cpanel accessed as"+user)
    
except Exception as e:
    print(e)

import requests
import time
import urllib.request
import os

def login(username,password):
    payload = {
        'mode': '191',
        'username': username,
        'password': password,
        'a': '1661062428616'
    }

    while(1>0):
        with requests.Session() as s:
            p = s.post('http://172.16.68.6:8090/login.xml', data=payload)
            if(p.status_code==200):
                print("Connected!")
                time.sleep(1700)    #make it run again after 28.3 minutes 
            else:
                print("Error Response:"+p);



def logout(username):
    payload = {
        'mode': '193',
        'username': username,
        'a': '1661076221551'
    }

    with requests.Session() as s:
        p = s.post('http://172.16.68.6:8090/logout.xml', data=payload)
        print (p)

        # r = s.get('http://172.16.68.6:8090/')
        # print(r)



def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

def check_ping():
    hostname = "www."
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
    
    return pingstatus




session =login('21103016','178045HI')

# print(session)
# print(check_ping())




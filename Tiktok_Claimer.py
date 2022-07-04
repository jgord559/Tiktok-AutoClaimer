import requests
import os
from pystyle import *
from colorama import Fore
import json
from random import randint

uid = 'your uid'
sid = ''
user = input('User to claim?: ')


url = "https://api16-normal-c-useast1a.tiktokv.com/passport/login_name/update/?iid=7114694905583191810&device_id=7103265913999754757&ac=wifi&channel=googleplay&aid=1180&app_name=trill&version_code=240302&version_name=24.3.2&device_platform=android&ab_version=24.3.2&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=es&os_api=25&os_version=7.1.2&openudid=6d1bc771d91a26d2&manifest_version_code=240302&resolution=720*1280&dpi=239&update_version_code=240302&_rticket=1656719123822&current_region=NL&app_type=normal&sys_region=ES&mcc_mnc=20420&timezone_name=Europe%2FMadrid&residence=NL&ts=1656719121&timezone_offset=3600&build_number=24.3.2&region=ES&uoo=0&app_language=es&carrier_region=NL&locale=es&op_region=NL&ac2=wifi&host_abi=x86_64&cdid=fc486ba0-9c73-4837-93ef-023891876356&support_webview=1&okhttp_version=4.1.73.30-tiktok"
# change headers to your's only way it will work!
# dm me zt#7380 if you need help getting headers.
headers = {
"accept-encoding": "gzip",
"connection": "Keep-Alive",
"content-length": "61",
"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
"cookie": "passport_csrf_token=e4f49bcfa84940392c40433dce4d730b; passport_csrf_token_default=e4f49bcfa84940392c40433dce4d730b; tt_csrf_token=7rVNClmE-zC6dwd9GEy-YLm7PmqlGIzm3Keg; install_id=7114694905583191810; ttreq=1$0498a4ad824e614cbb3c02ee3ec82cfb59218085; d_ticket=a6ccb0e3d30322f4c517882b6b447e027559e; multi_sids=6978821847786292229%3A9344f25c038ea0aaa62ca6322d2892ed%7C7093848823089153030%3A85e55f37127fc0ebb21ef28559df2a07%7C6671934115891855365%3A0d824171b3b3b6a289e482b3d34ccf63%7C6749466465089848325%3Ab3c6dc25b25b5f22e022d7ff687eb7af%7C7114882393773573126%3A38a3cc6853b1ea71f39954b57766cfbb%7C7089763365870306310%3A7645f953d665cbff1687a97674819d2e%7C7092810600804303877%3Aca9b8af3bea077b002e0b2f42e461e28%7C7116518794030531630%3A97a082b4d7798f1daa06988e615887c4; cmpl_token=AgQQAPNSF-RP_bL8GoTrph0X-PJHhWKHv4fZYMb68A; odin_tt=aec331f3502742d734d47ff5adcedac37ea264487d413a489ca3f814c4160db04f3dca3a31815ec0f187039408c6b8a76ffbd994eebbc423258ba6b826be40c5c01c6d287b691e2594b2113b474a970a; sid_guard=97a082b4d7798f1daa06988e615887c4%7C1656944882%7C5184000%7CFri%2C+02-Sep-2022+14%3A28%3A02+GMT; uid_tt=4fa040e4be82cecf50793e0af589974030471e8b746416b424ed185bee526f7c; uid_tt_ss=4fa040e4be82cecf50793e0af589974030471e8b746416b424ed185bee526f7c; sid_tt=97a082b4d7798f1daa06988e615887c4; sessionid=97a082b4d7798f1daa06988e615887c4; sessionid_ss=97a082b4d7798f1daa06988e615887c4; store-idc=useast5; store-country-code=us; tt-target-idc=useast5; msToken=8IglX_fiDH5iHh1PwX1ZLHvxUvMdK06Yq7pSznPTHyR05omdmrhL8qYTKB2K1srWAXeMnstW1IPJ-He-FyPP4fnNHShUr4a0wyy6qknpUH8Eu_TALigAd3A=",
"host": "api16-normal-useast5.us.tiktokv.com",
"multi_login": "1",
"passport-sdk-version": "19",
"sdk-version": "2",
"user-agent": "com.ss.android.ugc.trill/240302 (Linux; U; Android 7.1.2; es_ES; SM-N975F; Build/N2G48H;tt-ok/3.10.0.2)",
"x-argus": "Vts10s5a4/Vzb+J/24i3WRDfpFUTpn0sjKl7KG7ih9j4LXI1Jg1w0g+Kdpqf+K3CrqdVCkuO2hln/Wyrn0EFdkDseyu+Nmo0iTS0vsuw4Aj2AE8aHMpfaOuL5PT4mtYapo6gNPCNSU9zDBTiXGL3SjZ3iIefCRdpFly/sHCLsQ1/ngP5vfFZ3u5J+OkDQ2Ffs/uvJK8CHHK3RbqbKTb2Q2xRls/8qWDPvqCC8GU+SNNHQxSveT+9JHnELikYl+PKnuf/+kCWjWGq7EI8ompbSiCH02X8WGNkK8hf2splJ+komYF5YO7LRmnAc3gpMdZ9Yr5xTX59DOJpkaG4yGI0yAyqsPMKCLbbKp1IBiQznU9YTA==",
"x-bd-client-key": "#iQ5puag+TdYbvVQ7Hd26DF4Vtj2si6Bdp3qzP5e9eynFljlgeC0S6dzrNr+uIhsMXmaBswLNc1twmQMa",
"x-bd-kmsv": "0",
"x-gorgon": "0404808040008fdae50bacd19828aa66ed9b3cb072cee893d63a",
"x-khronos": "1656950763",
"x-ladon": "lrStT5BMT38qLc+1PzpXYFa8hyE0zhOu4ChY3TY2iM0j83R8",
"x-ss-req-ticket": "1656950763387",
"x-ss-stub": "EAA69FB6AE353E42E1DB1F29A70B619C",
"x-tt-cmpl-token": "AgQQAPNSF-RP_bL8GoTrph0X-PJHhWKHv4dnYMb6kQ",
"x-tt-dm-status": "login=1;ct=1;rt=1",
"x-tt-multi-sids": "6978821847786292229%3A9344f25c038ea0aaa62ca6322d2892ed%7C7093848823089153030%3A85e55f37127fc0ebb21ef28559df2a07%7C6671934115891855365%3A0d824171b3b3b6a289e482b3d34ccf63%7C6749466465089848325%3Ab3c6dc25b25b5f22e022d7ff687eb7af%7C7114882393773573126%3A38a3cc6853b1ea71f39954b57766cfbb%7C7089763365870306310%3A7645f953d665cbff1687a97674819d2e%7C7092810600804303877%3Aca9b8af3bea077b002e0b2f42e461e28%7C7116518794030531630%3A97a082b4d7798f1daa06988e615887c4",
"x-tt-store-idc": "useast5",
"x-tt-store-region": "us",
"x-tt-store-region-src": "id",
"x-tt-token": "0497a082b4d7798f1daa06988e615887c40324deefe637798ec05e3ed60d597856bf55872c922687959c5f91cd16b862783b9cd40cf0af911462c40387a4cf721b6bcef7c956901b1ad1fc4722ced84c2b7419df564e073a48792e2973ff7bcf84206-1.0.1",
"x-vc-bdturing-sdk-version": "2.2.1.i18n",
}

def check():
    while True:
        deviceid = randint(1000000000000000000, 9999999999999999999)
        checkurl = (f"https://www.tiktok.com/api/user/detail/?aid=1988&app_name=tiktok_web&battery_info=1&browser_online=true&channel=tiktok_web&device_id={deviceid}&device_platform=web_pc&uniqueId={user}")
        checkhed = {
            'user-agent': 'fdsa',
            'cookie': f'sessionid={sid}',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}   
        checkreq = requests.get(checkurl, headers=checkhed)

        if '"statusCode":10202' in (checkreq.text):
            print("[+] " + "@" + user + " is available")
            tt()

        if '"statusCode":0' in (checkreq.text):
            print("[-] " + "@" + user + " is taken")

        if '"statusCode":10221' in (checkreq.text):
            print("[-] " + "@" + user + " is banned")
        


def tt():
        global check
        data = {"uid": f"{uid}", "login_name": f"{user}", "page_from": "0"}
        req = requests.post(url, headers=headers, data=data)
        loaded = json.loads(req.content)
        print(loaded['data'])
        print(f"")
        print(Fore.RESET)



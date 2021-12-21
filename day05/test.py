
import requests

url ="https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/84/37/448413784/448413784-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1638614292&gen=playurlv2&os=cosbv&oi=2064581296&trid=5777ee3cf8074157864eab1e56a01d75u&platform=pc&upsig=ee54e7895282759c8a63340cf267ea8b&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=25524&logo=80000000"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.41",
    "referer": "https://www.bilibili.com"
}
res = requests.get(url, headers=headers)
print(res)
with open('audio_test.mp4', 'wb') as f:
    f.write(res.content)
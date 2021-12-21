import requests
url = "https://kns.cnki.net/KNS8/Detail?sfield=fn&QueryID=0&CurRec=1&recid=&FileName=CGJS202107005&DbName=CJFDLAST2021&DbCode=CJFD&yx=&pr=&URLID="
# url = "https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLAST2021&filename=CGJS202107005&uniplatform=NZKPT&v=0PYOKEaVRLeHdtoVH-48iip9ZqwmNV2UddKpvL-suSvO1jZ938MVucIAqo5Eq_-n"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43",
    "Referer": "https://kns.cnki.net/kns8/defaultresult/index",

}

res = requests.get(url, headers=headers)
# print(res.text)


from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text, 'html.parser')
pdfDown = soup.find('a',attrs={"id":"pdfDown"})
href = pdfDown['href']
print(href)
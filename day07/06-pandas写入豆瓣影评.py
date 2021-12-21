"""
豆瓣影评

"""
import requests
from pandas import DataFrame
from bs4 import BeautifulSoup


url = "https://movie.douban.com/subject/34658290/comments"
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'
}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
# 找寻comments下面的div内容
commentItems = soup.find_all('div', attrs={"class": "comment-item"})
results = []
for i in commentItems:
    commentInfos = i.find('span', attrs={"class": "comment-info"}).find_all('span')
    # 评分标签
    star = commentInfos[1]['title'].strip()
    # 评分时间
    star_data = commentInfos[-1].text.strip()
    # 评论
    comment = i.find('span', attrs={"class": "short"}).text

    # content = [star, star_data, comment]
    # results.append(content)
    content_dict = {
        'star':star,
        'star_data':star_data,
        'comment':comment
    }
    results.append(content_dict)

print(results)
df = DataFrame(results)
df.to_csv('豆瓣影评.csv', index=False, encoding='utf-8-sig')
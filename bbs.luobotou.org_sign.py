# 需要提前执行：(报错请用pip3 install xxxxxx)
# pip install requests
# pip install bs4

#--------------------------------------
#此处修改成你的配置
url='https://bbs.luobotou.org/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1'
headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  "Accept-Language": "zh-CN,zh;q=0.9",
  "Accept-Encoding": "gzip, deflate, br",
  "Connection": "keep-alive",
  "Cookie" : "xxxx_1234_saltkey=xxxxxxxxxx; xxxx_1234_auth=xxxxxxxxxxxxxxxxxxx",
  "Host": "bbs.luobotou.org",
  "Referer": "https://bbs.luobotou.org/plugin.php?id=dsu_paulsign:sign"}
#以上请修改成自己的配置
#--------------------------------------

import re
import requests
from bs4 import BeautifulSoup
import html

#获取随机想说的话
mao = "http://api.maomao.tech/api/yiyan"
todaysay = requests.get(mao)
todaysay.encoding="UTF-8"
say=todaysay.text

#心情
form_data = {
    "formhash": "cb4f0a01",
    "qdxq": "kx",
    "todaysay": say,
}

#发送请求获取响应
r= requests.post(url, data=form_data, headers=headers)
r.encoding="UTF-8"
soup = BeautifulSoup(r.text, 'xml')
html_text = html.unescape(soup.text)
soup1 = BeautifulSoup(html_text, 'html.parser')

#寻找提示语句
div = soup1.find('div', class_='c')
text = div.get_text()

#输出
print(text)

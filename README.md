# discuz_sign
基于python的discuz! bbs签到脚本，有想添加的论坛欢迎提issues，大佬欢迎PR
## 教程：
### 本脚本适用于什么论坛？
滚动到论坛页面最下面，如果有<img width="115" alt="image" src="https://user-images.githubusercontent.com/109655023/209745903-7d6a9dac-3ad0-49b6-a9b0-e68e9dacdac8.png">则符合
### 获取cookie：
进入签到页面（理论上是https://你的论坛网址/plugin.php?id=dsu_paulsign:sign ）
按F12打开开发者工具，选择“网络”（英文是Network），点击“开始签到”
<img width="1292" alt="image" src="https://user-images.githubusercontent.com/109655023/209746232-64a0d0d8-87a0-439b-8314-7d746658288e.png">
请求网址即为“url”的值
再进入“应用”标签栏（英文是Applications）
<img width="626" alt="image" src="https://user-images.githubusercontent.com/109655023/209746556-138f45b9-e63c-4894-9475-90c6a3e4593b.png">
<\n> 找到“auth”与“saltkey”（前缀和我不一定一样）复制名称与值，粘贴到脚本"Cookie" :的位置

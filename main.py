# coding=utf-8
# python3 main.py
import sys
import json
import random
import os
import websocket
import requests
import platform
# 配置bot信息
bot_name = 'SprinkleBot'
password = 'tc101217'
channel = '公共聊天室'
# 提取系统信息
OS_info = platform.platform()
# 加入和发送函数
def join(bot_name, password, channel):
    ws.send(json.dumps({'cmd': 'join', 'nick': bot_name, 'password': password, "clientName": '[Sprinkle Chat](https://pntang.github.io/)', "clientKey": 'Z1ozsN2ZExhhUHt', 'channel': channel }))

def send(message):
    ws.send(json.dumps({'cmd': 'chat', 'text': message}))
# 爬取帮助文件
URL = 'https://sprinkle.eu.org/dx_xb/help.md'
res = requests.get(URL)
res.encoding = 'utf-8'
# 用户权限等级
level2 = '"level":2'
level4 = '"level":4'
level1 = '"level":1'
# 功能列表
emprs_list = ['( ﾟ∀。)', '(ノﾟ∀ﾟ)ノ', ' ﾟ∀ﾟ)σ', '(*ﾟーﾟ)', '( ﾟ∀ﾟ)', 'σ`∀´) ﾟ∀ﾟ)σ', '(((　ﾟдﾟ)))']

site_list = [
    'http://adarkroom.doublespeakgames.com/?lang=zh_cn',
    'https://www.sekai.co/trust/',
    'https://openarena.live/',
    'https://bruno-simon.com/',
    'https://sombras.app/?a=ZZffyi&b=Z33dhc',
    'https://favicon-pong.glitch.me/',
    'https://liferestart.syaro.io/view/',
    'https://win11.blueedge.me/',
    'https://dinoswords.gg/',
    'https://saythemoney.github.io/',
    'http://asciicker.com/',
    'https://m3o.xyz/',
    'https://rpgplayground.com/',
    'https://2020game.io/',
    'https://emojia.glitch.me/',
    'http://voxar.io/',
    'v1.windows93.net',
    'https://www.pcjs.org/',
    'https://win95.ajf.me/win95.html',
    'www.lemonjing.com',
    'www.shadiao.app',
    'https://multiuser-sketchpad-colors.glitch.me/',
    'http://league-of-heroes.herokuapp.com/',
    'https://appetize.io',
    'https://cmd.to/',
    'http://cursors.io/',
    ]
# 连接
ws = websocket.WebSocket()
ws.connect("wss://ws.crosst.chat:35197/")
join(bot_name, password, channel)
send('(｡･∀･)ﾉﾞ嗨')
# 循环判定
while 1 == 1:
    msg = str(ws.recv())
    print(msg)
    emprs = random.choice(emprs_list)
    site = random.choice(site_list)
    if '@SprinkleBot' in msg:
        send(res.text)
    elif '表情包' in msg and bot_name not in msg:
        send(emprs)
    elif '趣站' in msg and bot_name not in msg:
        send(site)
    elif '分享文件' in msg and bot_name not in msg and level1 not in msg:
        send("[点此上传文件](http://sprinkle.is-best.net/crosst/) 密码:crosst.chat 禁止上传非法内容")
    elif 'gitHub.com' in msg and bot_name not in msg and level1 not in msg:
        send('[使用Github镜像](https://hub.sprinkle.workers.dev)')
    elif '蛤' in msg and bot_name not in msg:
        send('σ`∀´) ﾟ∀ﾟ)σ')
    elif ' ﾟ∀ﾟ)σ' in msg and bot_name not in msg:
        send('σ`∀´) ﾟ∀ﾟ)σ')
    elif 'bot系统' in msg and '"trip":"bjvk1K"' in msg:
        send('/w Sprinkle ' + OS_info + '.')
    elif 'bot日志' in msg and '"trip":"bjvk1K"' in msg:
        send('开始保存日志')
        while 1 == 1:
            save_msg = str(ws.recv())
            print(save_msg)
            if 'bot停止' in save_msg and '"trip":"bjvk1K"' in msg:
                send('停止保存日志')
                break
            else:
                f = open("log.txt", "w")
                f.write('' +save_msg+ '\n')
                f.close()
    elif 'bot清空' in msg and '"trip":"bjvk1K"' in msg:
        clr = open('log.txt', 'w')
        clr.write('')
        clr.close()
        send('已清空日志')
    elif 'bot重启' in msg and '"trip":"bjvk1K"' in msg:
        ws.close()
        ws.connect("wss://ws.crosst.chat:35197/")
        join(bot_name, password, channel)
        send('我又来啦！')
    elif 'bot出去' in msg and '"trip":"bjvk1K"' in msg:
        ws.close()
        break
sys.exit(0)

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
password = '123456'
channel = 'your-channel'

bz = '''
### SprinkleBot 帮助
命令列表
| 表情包 | 趣站 | 涩图 | 蛤 |  ﾟ∀ﾟ)σ |
'''
# 加入和发送函数
def join(bot_name, password, channel):
    ws.send(json.dumps({'cmd': 'join', 'nick': bot_name, 'pass': password, 'channel': channel }))

def send(message):
    ws.send(json.dumps({'cmd': 'chat', 'text': message}))

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
ws.connect("wss://hack.chat/chat-ws")
join(bot_name, password, channel)
send('(｡･∀･)ﾉﾞ嗨')
# 循环判定
while 1 == 1:
    msg = str(ws.recv())
    print(msg)
    emprs = random.choice(emprs_list)
    site = random.choice(site_list)
    if 'onlineAdd' in msg:
        if '"nick":"Sprinkle"' in msg and '"trip":"EoZ5HO"' in msg:
            send('$$\color{red}主\color{orange}人\color{yellow}早\color{green}上\color{blue}好\color{purple}( ﾟ∀。)$$')
        else:
            send('偶哈哟，欢迎来到hackchat！(ノﾟ∀ﾟ)ノ')
            send('输入"帮助"来查看帮助内容')
    elif 'onlineRemove' in msg:
        send('拜拜(ノﾟ∀ﾟ)')
    elif '帮助' in msg and bot_name not in msg:
        send(bz)
    elif '涩图' in msg and bot_name not in msg:
        send('涩图一张，注意身体( ﾟ∀ﾟ) ![waifu](https://pic.sprinkle.workers.dev)')
    elif '表情包' in msg and bot_name not in msg:
        send(emprs)
    elif '趣站' in msg and bot_name not in msg:
        send(site)
    elif '蛤' in msg and bot_name not in msg:
        send('σ`∀´) ﾟ∀ﾟ)σ')
    elif ' ﾟ∀ﾟ)σ' in msg and bot_name not in msg:
        send('σ`∀´) ﾟ∀ﾟ)σ')
    elif 'bot出去' in msg and '"trip":"EoZ5HO"' in msg:
        ws.close()
        break
sys.exit(0)

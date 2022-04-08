# coding=utf-8
# python3 main.py
import sys
import json
import random
import os
import websocket
import platform
# 配置bot信息
bot_name = 'Sprink1e'
password = '123'
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

# 连接
ws = websocket.WebSocket()
ws.connect("wss://hack.chat/chat-ws")
join(bot_name, password, channel)
send('(｡･∀･)ﾉﾞHi!')
# 循环判定
while 1 == 1:
    msg = str(ws.recv())
    print(msg)
    if 'onlineAdd' in msg:
        if '"nick":"Sprinkle"' in msg and '"trip":"EoZ5HO"' in msg:
            send('$\color{red}主\color{orange}人\color{yellow}早\color{green}上\color{blue}好\color{purple}( ﾟ∀。)$')
        else:
            send('Hey yo!')
    elif '帮助' in msg and bot_name not in msg:
        send(bz)
    elif '涩图' in msg and bot_name not in msg:
        send('涩图一张，注意身体( ﾟ∀ﾟ) ![waifu](https://pic.sprinkle.workers.dev)')
    elif '蛤' in msg and bot_name not in msg:
        send('σ`∀´) ﾟ∀ﾟ)σ')
    elif ' ﾟ∀ﾟ)σ' in msg and bot_name not in msg:
        send('σ`∀´) ﾟ∀ﾟ)σ')
sys.exit(0)

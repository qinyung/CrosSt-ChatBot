# coding=utf-8
# python3 main.py

# ------------------------------配置bot信息------------------------------
bot_name = 'SprinkleBot'
password = ' '
channel = 'your-channel'
hello = False
roll = True
dev = False
# ------------------------------配置bot信息------------------------------

import os
import sys
import json
import time
import random
import websocket
from threading import Thread
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "The SprinkleBot is running..."


def run():
    app.run(host='0.0.0.0', port=8080)


t = Thread(target=run)
t.start()


# 加入和发送函数
def join(bot_name, password, channel):
    if dev == True:
        channel = 'dev'
        print(
            '----------------------已开启开发模式，请于?dev聊天室查看----------------------')
    ws.send(
        json.dumps({
            'cmd': 'join',
            'nick': bot_name,
            'pass': password,
            'channel': channel
        }))


def send(message):
    try:
        ws.send(json.dumps({'cmd': 'chat', 'text': message}))
    except:
        ws.close()
        ws.connect("wss://hack.chat/chat-ws")
        join(bot_name, password, channel)


# 功能列表
bot_ignore = ['"nick":"do_ob"', '"nick":"bo_od"', '>', bot_name]
bot_admin = ['EoZ5HO', 'eYFDHl']
bot_trust = ['EoZ5HO', 'eYFDHl']
py_ignore = ['import', 'while', 'for', 'from', 'input']
os_ignore = ['del', 'rm', 'python', '/', 'wget', 'git', 'apt']

bz = '''
| 指令 | 描述 | 指令 | 描述 |
| :---: | :---: | :---: | :---: |
| 表情包 | 发送一个表情包 | 虫合 | 嘲笑你(doge) |
| 趣站 | 发送一个好玩的网站 | 贴贴 | 你好恶心(吐)🤮 |
| 二次元图 | 发送涩涩的图片 | 传文件 | 使用分享站点传文件 |
| os | 运行Linux命令 | py | 运行python代码 |
| 手气 | 摇一个随机数 | haha | #@最高机密#@ |
'''

emprs_list = [
    '( ﾟ∀。)', '(ノﾟ∀ﾟ)ノ', ' ﾟ∀ﾟ)σ', '(*ﾟーﾟ)', '( ﾟ∀ﾟ)', 'σ`∀´) ﾟ∀ﾟ)σ',
    '(((　ﾟдﾟ)))'
]

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
    try:
        msg_json = json.loads(ws.recv())
        print(str(msg_json))
        if "cmd" in msg_json:
            cmd = msg_json["cmd"]
            if cmd == "chat":
                name = msg_json['nick']
                msg = msg_json['text']
                try:
                    trip = msg_json['trip']
                except:
                    trip = 'none'
                userid = msg_json['userid']
            elif cmd == 'onlineAdd':
                userhash = msg_json['hash']
                name = msg_json['nick']
                try:
                    trip = msg_json['trip']
                except:
                    trip = 'none'
                userid = msg_json['userid']
    except:
        pass
    if cmd == 'chat':
        ignore = any(word if word in msg_json else False
                     for word in bot_ignore)
        admin = any(word if word in trip else False for word in bot_admin)
        trust = any(word if word in trip else False for word in bot_trust)
        pyi = any(word if word in msg else False for word in py_ignore)
        osi = any(word if word in msg else False for word in os_ignore)
        if '@' + bot_name in msg:
            send('hi，我是SprinkleBot，输入"命令"来查看我的功能!')
        elif msg == '命令' and ignore == False:
            send(bz)
        elif msg == '二次元图' and ignore == False:
            send('涩图一张，注意身体( ﾟ∀ﾟ) ![waifu](https://pic.sprinkle.workers.dev)')
        elif msg == '表情包' and ignore == False:
            emprs = random.choice(emprs_list)
            send(emprs)
        elif msg == '趣站' and ignore == False:
            site = random.choice(site_list)
            send(site)
        elif msg == '手气' and ignore == False and roll == True:
            r = random.randint(0, 1001)
            send('摇出了' + str(r) + '')
        elif '蛤' in msg and ignore == False:
            send('σ`∀´) ﾟ∀ﾟ)σ')
        elif msg == '贴贴' and ignore == False:
            send('呕——(　ﾟдﾟ)')
        elif msg == '传文件' and ignore == False:
            send(
                '使用 [十字街分享站](http://sprinkle.is-best.net/crosst) 密码:crosst.chat'
            )
        elif 'os ' in msg and admin == True:
            command = msg[3: ]
            if osi == False and admin == True:
                runcmd = os.popen(command)
                output = runcmd.read()
                runcmd.close()
                send('```shell\n{}```'.format(output))
            elif osi == True:
                send('Error: unsupport command')
        elif 'py ' in msg and admin == True:
            command = msg[3: ]
            with open('botrun.py','w') as f:
                f.write(command)
                f.close()
            if pyi == False and admin == True:
                runcmd = os.popen('python3 botrun.py')
                output = runcmd.read()
                runcmd.close()
                send('```shell\n{}```'.format(output))
            elif pyi == True:
                send('Error: unsupport command')
        elif 'botcolor ' in msg and admin == True:
            color = msg[9: ]
            send('/color ' + color + '')
            send('变...变色了?!')
        elif 'bothello' in msg and admin == True:
            if hello == True:
                send('$HELLO设为False')
                hello = False
            elif hello == False:
                send('$HELLO设为True')
                hello = True
        elif 'botroll' in msg and admin == True:
            if roll == True:
                send('$ROLL设为False')
                roll = False
            elif roll == False:
                send('$ROLL设为True')
                roll = True
        elif 'bot休眠' in msg and admin == True:
            send('晚安')
            while 1 == 1:
                try:
                    msg1 = str(ws.recv())
                except:
                    ws.close()
                    ws = websocket.WebSocket()
                    ws.connect("wss://hack.chat/chat-ws")
                    join(bot_name, password, channel)
                if 'bot停止休眠' in msg1 and admin == True:
                    send('睡醒咯')
                    break
                elif '@SprinkleBot' in msg1 and ignore == False:
                    send('SprinkleBot在睡觉呢')
        elif 'bot出去' in msg and admin == True:
            ws.close()
            sys.exit(0)
    elif cmd == 'onlineAdd':
        if admin == True and hello == True:
            send(
                '$\color{red}主\color{orange}人\color{yellow}早\color{green}上\color{blue}好\color{purple}( ﾟ∀。)$'
            )
        elif hello == True:
            send('hi :D')
    else:
        pass

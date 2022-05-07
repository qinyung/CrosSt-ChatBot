# coding=utf-8
# python3 main.py

# ------------------------------配置bot信息------------------------------
bot_name = 'SprinkleBot'
password = ' '
channel = '公共聊天室'
hello = False
roll = False
dev = False

# ------------------------------配置bot信息------------------------------

import sys
import json
import time
import random
import websocket

# 加入和发送函数
def join(bot_name, password, channel):
    if dev == True:
        channel = 'dev'
        print('----------------------已开启开发模式，请于?dev聊天室查看----------------------')
    ws.send(json.dumps({'cmd': 'join', 'nick': bot_name, 'password': password, 'channel': channel }))

def send(message):
    try:
        ws.send(json.dumps({'cmd': 'chat', 'text': message}))
    except:
        ws.close()
        ws.connect("wss://ws.crosst.chat:35197")
        join(bot_name, password, channel)


# 功能列表
bot_ignore = ['"nick":"do_ob"', '"nick":"bo_od"', '"nick":"Anotia"', '>', bot_name]
bot_admin = ['"trip":"bjvk1K"', '"trip":"MTbR9U"', '"trip":"Z+zTvB"', '"trip":"w171pi"']


bz = '''
| 指令 | 描述 | 指令 | 描述 |
| :---: | :---: | :---: | :---: |
| 表情包 | 发送一个表情包 | 蛤 | 嘲笑你(doge) |
| 趣站 | 发送一个好玩的网站 | 呕 | 发送"贴贴"???🤮 |
| 涩图 | 发送涩涩的图片 | 传文件 | 使用分享站点传文件 |
| 手气 | 摇一个随机数 | haha | #@最高机密#@ |
'''

haha = '''
———————————————————————————————————————————
十字街炸弹 - 1.0 [Launch in 10s - 三秒后启动]
———————————————————————————————————————————
此举可能引起网站崩溃,请谨慎使用!!!
'''

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

color_list = ['#4EEE94', '#00BFFF', '#FFFF00', '#FF6A6A', '#fff', '#FF0000', '#FF1493', '#90EE90']

# 连接
ws = websocket.WebSocket()
ws.connect("wss://ws.crosst.chat:35197")
join(bot_name, password, channel)
send('(｡･∀･)ﾉﾞ嗨')
# 循环判定
while 1 == 1:
    try:
        msg = str(ws.recv())
    except:
        ws.close()
        ws = websocket.WebSocket()
        ws.connect("wss://ws.crosst.chat:35197")
        join(bot_name, password, channel)
    ignore = any(word if word in msg else False for word in bot_ignore)
    admin = any(word if word in msg else False for word in bot_admin)
    if 'onlineAdd' in msg:
        if admin == True:
            send('$\color{red}主\color{orange}人\color{yellow}早\color{green}上\color{blue}好\color{purple}( ﾟ∀。)$')
        elif hello == 'True':
            send('hi,欢迎来到十字街')
    elif '@SprinkleBot' in msg and ignore == False:
        send('hi，我是SprinkleBot，输入"帮助"来查看帮助内容!')
    elif '帮助' in msg and ignore == False:
        send(bz)
        send(admin_bz)
    elif '涩图' in msg and  ignore == False:
        send('涩图一张，注意身体( ﾟ∀ﾟ) ![waifu](https://pic.sprinkle.workers.dev)')
    elif '表情包' in msg and ignore == False:
        emprs = random.choice(emprs_list)
        send(emprs)
    elif '趣站' in msg and ignore == False:
        site = random.choice(site_list)
        send(site)
    elif '手气' in msg and ignore == False and roll == True:
        r = random.randint(0,11)
        send('摇出了' + str(r) + '')
    elif '蛤' in msg and ignore == False:
        send('σ`∀´) ﾟ∀ﾟ)σ')
    elif ' ﾟ∀ﾟ)σ' in msg and ignore == False:
        send('σ`∀´) ﾟ∀ﾟ)σ')
    elif '贴贴' in msg and ignore == False:
        send('呕——(　ﾟдﾟ)')
    elif 'bothaha' in msg and admin == True:
        send(haha)
        time.sleep(10)
        send('rickroll 你被骗了蛤蛤蛤，大傻瓜')
    elif 'bot变色' in msg and admin == True:
        color = random.choice(color_list)
        send('/color ' + color + '')
        send('艹艹艹艹艹巴啦啦小魔仙，变身!艹艹艹艹艹')
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
            msg1 = str(ws.recv())
            print(msg1)
            if 'bot停止休眠' in msg1 and admin == True:
                send('睡醒咯')
                break
            elif '@SprinkleBot' in msg1 and ignore == False:
                send('SprinkleBot在睡觉呢')
    elif 'bot出去' in msg and admin == True:
        ws.close()
        sys.exit(0)

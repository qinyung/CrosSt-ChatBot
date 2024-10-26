# coding=utf-8
# python3 main.py
import os
import sys
import json
from time import sleep
import random
import websocket
from threading import Thread
from flask import Flask
import requests
import urllib

# ------------------------------配置bot信息------------------------------
bot_name = 'Snowi'
password = os.getenv('BOT_PSWD')
cpassword = os.getenv('CROSST_PSWD')
channel = 'your-channel'
cchannel = '公共聊天室'

# ------------------------------配置bot信息------------------------------

# 新的页面，加入了查看日志的功能，和下方的flask网页选一个即可
# def main():
#    os.system('cd log')
#    os.system('python3 -m http.server 8080')





# 加入和发送函数
def join(bot_name, password, channel, server):
#    if dev == True:
#        channel = 'dev'
#        print(
#            '----------------------已开启开发模式，请于?dev聊天室查看----------------------')
#    c_name = os.getenv('C_NAME')
#    c_key = os.getenv('C_KEY')
    if server == 'crosst':
        ws.send(
            json.dumps({
                'cmd': 'join',
                'nick': bot_name,
                'password': password,
                "clientName": '[🎄识字街客户端](https://client.urcraft.repl.co)',
                # "clientKey": 'Z1ozsN2ZExhhUHt',
                'channel': channel,
            }))
    else:
        ws.send(
            json.dumps({
                'cmd': 'join',
                'nick': bot_name,
                'pass': password,
                'channel': channel
            }))


def send(message):
#    try:
    ws.send(json.dumps({'cmd': 'chat', 'text': message}))
#    except:
#        ws.close()
#        if server == 'crosst':
#            ws.connect("wss://ws.crosst.chat:35197/")
#        elif server == 'hc':
#            ws.conncect("wss://hack.chat/chat-ws")
#        join(bot_name, password, channel)

def chatapi(message):
    apiban = ['脱衣', '射', '操', '爽', '口交', '乱发网址', '正在维护', '未获取到相关信息', '大爷', '知道切糕不，一刀上海买房 两刀杨幂上床 三刀盖茨认娘 四刀铁定入常', '陪睡']
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(message))
    html = requests.get(url)
    getmsg2 = html.json()["content"].replace('你', '大小姐')
    getmsg1 = getmsg2.replace('菲菲', '雪羽桑')
    r = random.randint(0, 5)
    if r == 3:
        getmsg = str('呐~⭐' + getmsg1 + '')
    else:
        getmsg = getmsg1
    apignore = any(word if word in getmsg else False for word in apiban)
    if apignore == False:
        return getmsg
    else:
        return '(鞠躬)抱歉大小姐，雪羽酱没有听清'

# 功能列表
bot_ignore = ['"nick":"do_ob"', '"nick":"bo_od"', '>', '笑话', '收到私聊']
bot_admin = ['gDhuU3', 'sSv1j2', 'vnmh8c']
bot_trust = ['gDhuU3', 'sSv1j2', 'vnmh8c']
py_ignore = ['import', 'while', 'for', 'from', 'input']
os_ignore = ['del', 'rm', 'python', '/', 'apt']

bz = '''
| 功能 | 描述 | 功能 | 描述 |
| :---: | :---: | :---: | :---: |
| 反馈 | 反馈问题(beta) | 蛤 | 嘲笑你! |
| 睡觉 | 雪羽酱の晚安 | 早安问候 | 打招呼(beta) |
| 表情包 | 发送一个表情包 | 贴贴 | 和雪羽酱贴贴 |
__『Tips』__ 输入 “@Snowi 聊天内容” 可以和雪羽酱聊天喔⭐~
'''

emprs_list = [
    '( ﾟ∀。)', '(ノﾟ∀ﾟ)ノ', ' ﾟ∀ﾟ)σ', '(*ﾟーﾟ)', '( ﾟ∀ﾟ)', 'σ`∀´) ﾟ∀ﾟ)σ',
    '(　ﾟдﾟ)'
]

# 连接

def bot_main(server):
    global ws
    hello = False
    roll = True
    ws = websocket.WebSocket()

    if server == 'crosst':
        ws.connect("wss://ws.crosst.chat:35197/")
        join(bot_name, cpassword, cchannel, server)
    elif server == 'hc':
        ws.connect("wss://hack.chat/chat-ws")
        join(bot_name, password, channel, server)
    if server == 'hc':
        send('/color FFC1C1')
        send('(｡･∀･)ﾉﾞ嗨')



    # 监控网页
    app = Flask(__name__)
    @app.route("/")
    def main():
        return "The SprinkleBot is running..."
    def run():
        app.run(host='0.0.0.0', port=8080)
    t = Thread(target=run)
    t.start()



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
                    # userhash = msg_json['hash']
                    # name = msg_json['nick']
                    try:
                        trip = msg_json['trip']
                    except:
                        trip = 'none'
                    # userid = msg_json['userid']
        except:
            pass
        if cmd == 'warn':
            ws.close()
            break
        elif cmd == 'chat':
            ignore = any(word if word in str(msg_json) else False for word in bot_ignore)
            admin = any(word if word in trip else False for word in bot_admin)
            trust = any(word if word in trip else False for word in bot_trust)
            pyi = any(word if word in msg else False for word in py_ignore)
            osi = any(word if word in msg else False for word in os_ignore)
            if ignore == False:
                if msg == '功能':
                    send(bz)
                elif msg == '表情包':
                    emprs = random.choice(emprs_list)
                    send(emprs)
                elif msg == '手气' and roll == True:
                    r = random.randint(0, 1001)
                    send('摇出了' + str(r) + '')
                elif '蛤' in msg:
                    send('σ`∀´) ﾟ∀ﾟ)σ')
                elif msg == '贴贴':
                    send('『啊依系带哟』，大小姐什么时候和花見酱贴贴都可以哦')
                elif msg == '睡觉':
                    send('晚安哦，需要雪羽酱讲故事入眠可以找我哦')
                elif msg == '反馈':
                    send('抱歉给大小姐造成困扰，这里是[『雪羽酱の邮箱⭐』](mailto:mail@snowi.eu.org)')
                elif 'os ' in msg and trust == True:
                    command = msg[3: ]
                    if osi == False and trust == True:
                        runcmd = os.popen(command)
                        output = runcmd.read()
                        runcmd.close()
                        send('```shell\n{}```'.format(output))
                    elif osi == True:
                        send('Error: unsupport command')
                elif 'py ' in msg and trust == True:
                    command = msg[3: ]
                    with open('botrun.py','w') as f:
                        f.write(command)
                        f.close()
                    if pyi == False and trust == True:
                        runcmd = os.popen('python3 botrun.py')
                        output = runcmd.read()
                        runcmd.close()
                        send('```shell\n{}```'.format(output))
                    elif pyi == True:
                        send('Error: unsupport command')
                elif 'botcolor ' in msg and admin == True and server == 'hc':
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
                # elif '\ban ' in msg and admin == True:
                    # baninfo = msg[5: ]
                    # send('/ban ' + baninfo + '')
                # elif '\banip ' in msg and admin == True:
                    # baninfo = msg[7: ]
                    # send('/banip ' + baninfo + '')
                # elif r'\unban ' in msg and admin == True:
                    # baninfo = msg[7: ]
                    # send('/unban ' + baninfo + '')
                # elif r'\unbanip ' in msg and admin == True:
                    # baninfo = msg[9: ]
                    # send('/unbanip ' + baninfo + '')
                elif 'bot休眠' == msg and admin == True:
                    send('晚安')
                    while 1 == 1:
                        try:
                            msg1 = str(ws.recv())
                        except:
                            ws.close()
                            ws = websocket.WebSocket()
                            ws.connect("wss://ws.crosst.chat:35197/")
                            join(bot_name, password, channel)
                        if 'bot停止休眠' in msg1 and admin == True:
                            send('睡醒咯')
                            break
                        elif '@' + bot_name in msg1 and ignore == False:
                            send('我睡了:0')
                elif 'bot出去' == msg and admin == True:
                    ws.close()
                    sys.exit(0)
                else:
                    r = random.randint(0, 100)
                    if r == 5:
                        emprs = random.choice(emprs_list)
                        send(emprs)
                    elif r == 6:
                        try:
                            send(chatapi(str(msg)))
                        except:
                            pass
            elif '@' + bot_name in msg:
                if '>' not in msg and '@' + bot_name != msg:
                    try:
                        send(chatapi(str(msg[7: ])))
                    except:
                        send('(鞠躬)抱歉大小姐，雪羽酱没有听清')
                elif '>' not in msg and '@' + bot_name == msg:
                    send('啾，大小姐早安~唤醒我啦！我是QingYu的bot--Snowi！全名叫『花見雪羽』，偶哈哟秋梨膏！输入"功能"查看帮助内容')
            else:
                pass
        elif cmd == 'onlineAdd':
            admin = any(word if word in trip else False for word in bot_admin)
            if admin == True:
                send('呐，大小姐早安~『お早く○○ですね』今天也辛苦了!')
            elif admin == False and hello == True:
                send('hi :D')
# while 1 == 1:
#    bot_main('crosst')
#    sleep(10)
#    print('restart')
#crosst = Thread(target=bot_main('crosst'))
#crosst.start()
# hc = Thread(target=bot_main('hc'))
# hc.start()
# bot_main('hc')

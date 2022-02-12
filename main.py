# coding=utf-8
# python3 main.py
import sys
import json
import random
import os
import websocket
import requests

URL = 'https://spr233.eu.org/dx_xb/help.md'
res = requests.get(URL)
res.encoding = 'utf-8'

ws = websocket.WebSocket()
ws.connect("wss://ws.crosst.chat:35197/")
ws.send(json.dumps({'cmd': 'join', 'nick': 'dx_xb', 'password': '1234567', "clientName": '[Sprinkle Chat](https://pntang.github.io/)', "clientKey": 'Z1ozsN2ZExhhUHt', 'channel': '公共聊天室' }))
ws.send(json.dumps({'cmd': 'chat', 'text': '(｡･∀･)ﾉﾞ嗨'}))
while 1 == 1:
    msg = str(ws.recv())
    print(msg)
    emprs_list = ['( ﾟ∀。)', '(ノﾟ∀ﾟ)ノ', ' ﾟ∀ﾟ)σ', '(*ﾟーﾟ)', '( ﾟ∀ﾟ)', 'σ`∀´) ﾟ∀ﾟ)σ', '(((　ﾟдﾟ)))']
    emprs = random.choice(emprs_list)
    level2 = '"level":2'
    level4 = '"level":4'
    level1 = '"level":1'
    if '@dx_xb hi' in msg and level1 not in msg:
        ws.send(json.dumps({'cmd': 'chat', 'text': res.text}))
    elif '@dx_xb 表情包' in msg and level1 not in msg:
        ws.send(json.dumps({'cmd': 'chat', 'text': emprs}))
    elif '@dx_xb 帮助' in msg and level1 not in msg:
        ws.send(json.dumps({'cmd': 'chat', 'text': res.text}))
    elif '@dx_xb 上传' in msg and level1 not in msg:
        ws.send(json.dumps({'cmd': 'chat', 'text': '[点此上传文件](http://sprinkle.is-best.net/crosst/) 或 [使用pikpak](https://sprinklelive.github.io/pikpak) 禁止上传非法内容'}))
    elif '@dx_xb gitHub' in msg and level1 not in msg:
        ws.send(json.dumps({'cmd': 'chat', 'text': '[Github镜像](https://hub.sprinkle.workers.dev)'}))
    elif '@dx_xb test' in msg and '"trip":"bjvk1K"' in msg:
        ws.send(json.dumps({'cmd': 'chat', 'text': '/w Sprinkle ( ﾟ∀。)'}))
    elif '@dx_xb 重启' in msg and '"trip":"bjvk1K"' in msg:
        ws.close()
        ws.connect("wss://ws.crosst.chat:35197/")
        ws.send(json.dumps({'cmd': 'join', 'nick': 'dx_xb', 'password': '1234567', "clientName": '[Sprinkle Chat](https://pntang.github.io/)', "clientKey": 'Z1ozsN2ZExhhUHt', 'channel': '公共聊天室' }))
        ws.send(json.dumps({'cmd': 'chat', 'text': '我又来啦！'}))
    elif '@dx_xb 出去' in msg and '"trip":"bjvk1K"' in msg:
        ws.close()
        break
sys.exit(0)

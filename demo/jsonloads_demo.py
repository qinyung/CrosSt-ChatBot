# 循环判定
while 1 == 1:
    msg = json.loads(ws.recv())
    if "cmd" in msg:
        cmd = msg["cmd"]
        if cmd == "chat":
            name = msg['nick']
            text = msg['text']
            if 'Sprinkle' in name:
                send('aaa')

# 基于镜像基础
FROM python:3.6.5
# 创建代码文件夹工作目录 /code 
RUN mkdir /app
# 复制当前代码文件到容器中 /code 
COPY . /app
# 安装所需的包
RUN pip install -r /app/requirements.txt
RUN pip install websocket-client
# 指定cmd的工作目录 /code
WORKDIR /app
# 指定工作目录后执行当前目录下的脚本
CMD ["python3", "main.py"]

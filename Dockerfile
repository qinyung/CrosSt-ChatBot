# 基于镜像基础
FROM python:3.6.5
# 创建代码文件夹工作目录 /code 
RUN mkdir /code 
# 复制当前代码文件到容器中 /code 
COPY . /code 
# 安装所需的包
RUN pip install -r /code/requirements.txt
RUN pip install websocket-client
# 指定cmd的工作目录 /code
WORKDIR /code
CMD ["python", "/app/main.py"]

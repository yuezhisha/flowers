# 基础镜像
FROM python:3.11.9

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libmariadb-dev-compat libmariadb-dev\
    libgl1-mesa-glx \
    libglib2.0-0

# 复制依赖文件
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制代码
COPY . .

# 暴露端口
EXPOSE 8000

# 启动命令（在 docker-compose.yml 中覆盖）
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

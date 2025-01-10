# 如何使用此项目

- 安装docker(可选择linux版本和windows的docker-desktop)

```bash
# linux
yum -y install yum-utils
# 设置镜像仓库
wget -O /etc/yum.repos.d/Centos-7.repo http://mirrors.aliyun.com/repo/Centos-7.repo
wget -O /etc/yum.repos.d/epel-7.repo http://mirrors.aliyun.com/repo/epel-7.repo
wget -O /etc/yum.repos.d/docker-ce.repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
# 安装docker
yum install docker-ce -y
docker --version # 查看是否安装完成docker
docker-compose --version # 查看是否安装了docker-compose
# 安装docker-compose(如果没有则进行下面步骤)
curl -L "https://github.com/docker/compose/releases/download/v2.17.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
docker-compose --version # 再次测试是否安装了docker-compose
# windows
直接搜索docker-desktop进行安装即可
```

- 在本机上安装nvdia显卡驱动cuda版本按照自己的版本进行安装

这里给出官网链接: https://developer.nvidia.com/cuda-toolkit-archive

从github上拉取我上传的源码包

```bash
git clone https://github.com/yuezhisha/flowers.git
```

从阿里云镜像仓库拉取镜像

```bash
docker pull crpi-bhjs34yuuqd3hyux.cn-hangzhou.personal.cr.aliyuncs.com/registry_shiye/ai:latest
docker pull crpi-bhjs34yuuqd3hyux.cn-hangzhou.personal.cr.aliyuncs.com/registry_shiye/mqtt:latest
docker pull crpi-bhjs34yuuqd3hyux.cn-hangzhou.personal.cr.aliyuncs.com/registry_shiye/database:latest
```

使用docker-compose运行项目

```bash
docker-compose up --build
```




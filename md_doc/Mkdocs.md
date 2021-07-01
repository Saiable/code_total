[TOC]
基本配置命令
基本配置¶
my-project目录下，生成站点文件

mkdocs build -d web/site
#-d 是生成到哪个文件夹下
进入本地仓库目录

git add .
# 加入到暂存区

git commit -m up
# 提交到版本库

git push
# 上传
其他¶
//本地起服务
mkdocs serve --dev-addr=192.168.31.199:1666
//或者
mkdocs serve -a 127.0.0.1:9999
# Build state

[![Build Status](https://travis-ci.org/huntzhan/easy-fork.svg?branch=master)](https://travis-ci.org/huntzhan/easy-fork)

# 中文版文档(TODO: 替换成英文文档)

模块划分:

![easy-fork](https://cloud.githubusercontent.com/assets/5213906/11339417/6414958a-9234-11e5-8ef9-92a981357fb4.png)

功能模块简要概述:

1. CLI: 命令行界面, 逻辑挂载点
2. Create remote repo on gitlab by calling RESTful API of gitlab.
3. 将 Internet 上的 git repo clone 到本地.
4. 基于 (2), (3) 返回值, 配置 local git repo.
5. push local git repo to the remote of gitlab.
6. 文件操作模块, 包括读取配置, 更新 log 等.
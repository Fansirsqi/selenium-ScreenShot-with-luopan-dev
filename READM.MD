## 然后需要确定客户浏览器在你哪个浏览上登录着着?


## 打开对应浏览器所在位置

Chrome:
例如我的路径在这`C:\Program Files\Google\Chrome\Application`

Edge:
`C:\Program Files (x86)\Microsoft\Edge\Application`

如果你默认安装的那应该就是这，然后cmd cd到对应文件夹里


## 复制缓存目录

假装这是脚本路径`C:\Users\你的用户名\Desktop\selenium_auto_luopan_screenshot`

如果是Chrome浏览器,那就找到如下路径
`C:\Users\admin\AppData\Local\Google`

如果是Edge浏览器:
`C:\Users\admin\AppData\Local\Microsoft\Edge`

在以上文件夹中有个`User Data`文件夹,把这个文件夹直接复制到你的项目文件夹里面

现在你的项目文件夹结构应该是这样的
```
└─C:\Users\你的用户名\Desktop\selenium_auto_luopan_screenshot
  └─User Data...z这是文件夹,其他都是文件
  ├─idriver.py
  ├─auto_luopan_screenshot.py
  ├─README.MD
```

## 运行调试浏览器

Chrome执行这玩意:
`chrome.exe --remote-debugging-port=9527 --user-data-dir="C:\Users\你的用户名\Desktop\selenium_auto_luopan_screenshot\User Data"`
Edge执行这玩意:
`./msedge.exe --remote-debugging-port=9527 --user-data-dir="C:\Users\你的用户名\Desktop\selenium_auto_luopan_screenshot"`

以上所有的操作都是为了处理让selenium接管本地浏览器,现在不要关闭,尝试打开罗盘的url,看书是不是登录的状态(不会让你输验证码登录,就点一下啊那啥商家就行,前提是你需要把之前浏览器的状态保持登录,复制的那份文件夹..)

这里的端口号要和代码里的端口号一致

是否查看运行起来了
在cmd输入
`netstat -ano|findstr :952*`

```会检索端口号匹配的进程
PS C:\Users\BYSEVEN> netstat -ano|findstr :952*
  TCP    127.0.0.1:9527         0.0.0.0:0              LISTENING       13816
  TCP    127.0.0.1:9527         127.0.0.1:60499        ESTABLISHED     13816
  TCP    127.0.0.1:60499        127.0.0.1:9527         ESTABLISHED     9448
  TCP    127.0.0.1:60500        127.0.0.1:9527         TIME_WAIT       0
```

至此浏览器这边的配置好了

## python 配置

现在说下python这边

我是python 3.11版本,3.9,3.10应该都可以不影响

先执行换源换成清华源

`pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`

安装浏览器驱动

`pip install -r requirements.txt`

执行安装
`python install idriver.py`

运行脚本
运行前确保调试浏览打开罗盘首页即可
`python auto_luopan_screenshot.py`
## 然后需要确定客户浏览器在你哪个浏览上登录着着?

在已经登录的浏览安装扩展插件 `cookie-editor`

然后在luo盘主页,导出cookie

## 打开对应浏览器所在位置

Chrome:

例如我的路径在这`C:\Program Files\Google\Chrome\Application`

Edge:

`C:\Program Files (x86)\Microsoft\Edge\Application`

如果你默认安装的那应该就是这，然后cmd cd到对应文件夹里

## 运行调试浏览器

Chrome执行:
`chrome.exe --remote-debugging-port=9527 --user-data-dir="C:\Users\你的用户名\Desktop\selenium_auto_luopan_screenshot\User Data"`

Edge执行:
`./msedge.exe --remote-debugging-port=9527 --user-data-dir="C:\Users\你的用户名\Desktop\selenium_auto_luopan_screenshot

是否查看运行起来了

在cmd输入`netstat -ano|findstr :952*`

会检索端口号匹配的进程

```bash
PS C:\Users\BYSEVEN> netstat -ano|findstr :952*
  TCP    127.0.0.1:9527         0.0.0.0:0              LISTENING       13816
  TCP    127.0.0.1:9527         127.0.0.1:60499        ESTABLISHED     13816
  TCP    127.0.0.1:60499        127.0.0.1:9527         ESTABLISHED     9448
  TCP    127.0.0.1:60500        127.0.0.1:9527         TIME_WAIT       0
```

然后在新开的浏览器这边也安装浏览器扩展插件 cookie-editor

打开罗pan主页的url,会让你登录,这时候用cookie-editor导入 刚刚导出的cookie,再以商家身份进入,应该就可以了

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

选择安装适合自己的版本,报错请重新打开终端命令行运行安装,安装成功是如下返回信息样式

```
PS D:\pt> & C:/Path/Python/Python311/python.exe d:/pt/idriver.py
选择您的浏览器:
1. firefox
2. IE
3. Chromium
4. Chrome
5. Edge

:4

DevTools listening on ws://127.0.0.1:64515/devtools/browser/d6275d31-94d1-4eaf-96bc-a9c438585f2a
```

运行脚本

运行前确保调试浏览打开[罗pan首页](https://compass.jinritemai.com/shop)即可

`python auto_luopan_screenshot.py`

luo盘首页url: `https://compass.jinritemai.com/shop`
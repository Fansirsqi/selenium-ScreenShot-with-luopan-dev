from selenium import webdriver
from time import sleep


print('测试访问9527端口上运行的浏览器,打印标题')

if __name__ == '__main__':
    print('select - browser\n1.Chrome\n2.Edge')
    i =input(':')
    if i == '1':
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
        browser = webdriver.Chrome(options=chrome_options)
        sleep(1)
        print(browser.title)
    elif i=='2':
        from selenium.webdriver.edge.options import Options
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
        browser = webdriver.Edge(options=chrome_options)
        sleep(1)
        print(browser.title)
    else:
        print('暂时只写了这俩-退出')
        exit()
    exit()
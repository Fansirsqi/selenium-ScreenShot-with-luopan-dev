from selenium import webdriver

# for Edge
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# for Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# selenium 4  Chromium
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.core.utils import ChromeType

# firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# IE
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager


if __name__ == "__main__":
    print('选择您的浏览器:\n1. firefox\n2. IE\n3. Chromium\n4. Chrome\n5. Edge\n')
    select = input(':')
    if select == '1':
        driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif select == '2':
        driver_ie = webdriver.Ie(service=IEService(IEDriverManager().install()))
    elif select == '3':
        driver_Chromium = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    elif select == '4':
        driver_chrome = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
    elif select == '5':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        print('输入有误!,请您重新运行脚本选择安装')

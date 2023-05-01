'''
Author: FansirQ 2104898527@qq.com
Date: 2023-05-01 01:43:58
LastEditors: FansirQ 2104898527@qq.com
LastEditTime: 2023-05-01 13:31:49
FilePath: \pt\installedge.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from selenium import webdriver

#for Edge
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#for Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver_chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_edge = webdriver.Edge(EdgeChromiumDriverManager().install())
exit()
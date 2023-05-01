from datetime import datetime, timedelta, date

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as ECS
import re




def do_loger(context):
    current_now = datetime.now().strftime('%H:%M:%S')
    print(current_now+':'+context)
    with open(f'loger.log',mode='a+',encoding='utf-8')as log:
        log.writelines(current_now+' : '+context+'\n')

def set_time_list(star:str,end:str,ren:int):
    """生成任务列表时间节点

    Args:
        star (str): 开始时间 07:00
        
        end (str): 结束时间 19:30
        
        ren (int): 步长(分钟) 30
    Returns:[07:00...19:30]
    """
    start_time = datetime.strptime('07:00', '%H:%M')
    end_time = datetime.strptime('23:30', '%H:%M')
    time_list = []
    current_time = start_time
    while current_time <= end_time:
        time_list.append(current_time.strftime('%H:%M'))
        current_time += timedelta(minutes=30)
    return time_list

def is_living_today(living_time):
    """判断当前正在直播的是否是今天的"""
    # 定义正则表达式
    pattern = r"\d{4}/\d{2}/\d{2}"
    # 进行正则匹配
    match = re.search(pattern, living_time)
    # 获取匹配的年月日
    _stream = match.group()
    # 转换成日期对象
    stream_date = datetime.strptime(_stream, '%Y/%m/%d').date()
    # 获取当前年月
    current_date = datetime.now().date()
    print('当前年月日',current_date)
    print('开播时间',stream_date)
    # 比较日期
    if stream_date == current_date:
        print("直播还在进行中")
        return True
    else:
        print("昨日直播未结束")
        return False

def is_btn_see(driver,by_ways,_element):
    """检测按钮存在并点击

    Args:
        driver (_type_): _description_浏览器对象
        by_ways (_type_): _description_检测方法，id,css,xpath...
        _element (_type_): _description_,'传入的对象节点

    Returns:
        _type_: _description_
    """
    live_btn = WebDriverWait(driver, 60).until(ECS.visibility_of_element_located((by_ways, _element)))
    if live_btn.click():
        print(f'{live_btn} - find success ！')
        return True

def auto_wait_time(time_str):
    hour, minute = map(int, time_str.split(":"))
    if hour < 6:
        do_loger('等待5分钟')
        return sleep(300)
    elif hour == 6 and minute>35:
        do_loger('等待2分钟')
        return sleep(120)
    else:
        do_loger('等待1分钟')
        return sleep(60)


def start_task(driver,DebugModule=False):
    debug = DebugModule
    today = date.today()
    do_loger(f'DebugModule = {DebugModule}')
    task_time = set_time_list('07:00','23:30',30)
    err_wait_time = 10 #出错等待重启时间s
    count = 1
    err_count = 0
    while True:
        try:
            while True:
                current_time = datetime.now().strftime('%H:%M')
                current_now = datetime.now().strftime('%H:%M')#:%S
                handles = driver.window_handles
                # 在最外层循环 - 需要确保 - 句柄为1
                while len(handles) != 1:
                    handles = driver.window_handles
                    sleep(5)
                    for i in handles:
                        driver.switch_to.window(i)
                        sleep(1)
                        if driver.title != '直播列表-抖音电商罗盘':
                            driver.close()
                    # driver.switch_to.window(handles[1])
                    do_loger(f'剩余标签页面：{len(handles)}')
                #判断当前时间节点是否是任务节点
                if current_time in task_time or debug:
                    if len(handles) == 1:
                        driver.refresh()#刷新页面
                        do_loger('刷新主页-')
                        sleep(5)
                        if driver.title != '直播列表-抖音电商罗盘':
                            is_btn_see(driver,By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div/div[5]')
                            do_loger('点击主页直播导航栏按钮')
                            sleep(5)
                        #正在直播的账号数量
                        living_num = int(driver.find_element(By.XPATH,'//*[@id="compass-container"]/div[3]/div/div[2]/div[2]/div[1]/div[2]/div[1]/span[1]').text.replace("正在直播 (","").replace(")",""))
                        do_loger(f'当前直播账号数量 - {living_num}')
                        if living_num>0:
                            #直播间名称
                            living_nick_name = driver.find_element(By.XPATH,'//*[@id="compass-container"]/div[3]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/div[1]').text
                            #k开播时间
                            start_time = driver.find_element(By.XPATH,'//*[@id="compass-container"]/div[3]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]').text
                            if (living_nick_name=='巴黎欧莱雅' and is_living_today(start_time)):#判断是不是欧莱雅在播，以及是否今天在播
                                do_loger('='*20+f'当前执行第 {count} 次截图任务'+'='*20)
                                do_loger('尝试进入大屏')
                                #进入大屏页面
                                is_btn_see(driver,By.XPATH,'//*[@id="compass-container"]/div[3]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[2]/div[1]/button')
                                sleep(5)
                                do_loger('进入大屏成功')
                                handles = driver.window_handles
                                # print(handles)
                                sleep(5)
                                #切换窗口句柄
                                driver.switch_to.window(handles[1])

                                # 侧边点击数据按钮
                                is_btn_see(driver,By.XPATH,'//*[@id="scaleContainer"]/div[2]/a[1]/div')
                                do_loger('侧边点击数据按钮')
                                # 点击流量分析
                                is_btn_see(driver,By.XPATH,'//*[@id="fullpage"]/div/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div[2]')
                                do_loger('点击流量分析')
                                WebDriverWait(driver, 30).until(ECS.presence_of_element_located((By.XPATH,'//*[@id="fullpage"]/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div/canvas')))                         
                                sleep(5)
                                driver.save_screenshot(f'直播大屏_{current_now.replace(":","_")}.png')
                                do_loger('执行截屏-直播大屏')
                                sleep(1)

                                #进入千川大屏()
                                is_btn_see(driver,By.XPATH,'//*[@id="scaleContainer"]/div[2]/a[4]/div')
                                do_loger('点击千川导航栏')
                                is_btn_see(driver,By.CSS_SELECTOR,'.gotoButton--L25Cl')
                                do_loger('进入巨量千川')
                                sleep(5)
                                handles = driver.window_handles
                                # print(handles)
                                driver.switch_to.window(handles[2])

                                sleep(5)
                                do_loger('执行截屏-巨量千川')
                                driver.save_screenshot(f'巨量千川_{current_now.replace(":","_")}.png')
                                sleep(1)

                                driver.close()#关闭巨量千川
                                do_loger('关闭巨量千川标签页')
                                sleep(1)
                                
                                handles = driver.window_handles
                                #跳到大屏
                                driver.switch_to.window(handles[1])
                                driver.close()#关闭直播大屏
                                do_loger('关闭直播大屏标签页')
                                sleep(1)
                                
                                handles = driver.window_handles
                                # print(handles)
                                # 跳回窗口句柄1,主页
                                do_loger('回主页')
                                driver.switch_to.window(handles[0])
                                do_loger(f'检查当前标签页标题 {driver.title}')
                                
                                formatted_date = today.strftime('%Y-%m-%d')
                                css = f"[title='{formatted_date}']"
                                is_btn_see(driver,By.CSS_SELECTOR,css)
                                do_loger('点击直播日历中的今天')
                                # daily_info = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[3]/div/div[2]/div[2]/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]').text
                                # do_loger(f'在直播日历中找到 - {daily_info}')
                                # if daily_info == '巴黎欧莱雅':
                                try:
                                    # 尽量等待网页加载完成-这类是直播日历列表页面的排序字段
                                    px = WebDriverWait(driver,30).until(
                                        ECS.visibility_of_element_located((By.XPATH,'//*[@id="compass-container"]/div[3]/div/div[2]/div[2]/div[1]/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div[1]')))
                                except Exception as e:
                                    do_loger(e)
                                sleep(3)#防止获取元素过快
                                all_living_room_name = driver.find_elements(By.CSS_SELECTOR,'.name--hnn4p>.nickname--o3xex')
                                do_loger('遍历直播列表')
                                all_btn = driver.find_elements(By.CSS_SELECTOR,'[data-btm="d3764"]')
                                do_loger('遍历所有详情按钮')
                                for i,item in enumerate(all_living_room_name):
                                    if item.text == '巴黎欧莱雅':
                                        do_loger(f'选中 - {item.text}')
                                        
                                        sleep(1)
                                        do_loger('进入欧莱雅详情直播页面')
                                        all_btn[i].click()
                                        sleep(3)
                                    else:
                                        pass

                                handles = driver.window_handles
                                sleep(1)
                                driver.switch_to.window(handles[1])
                                
                                do_loger(f'进入成功判断- {driver.title}')
                                
                                do_loger('标签跳转')
                                # 下滑一定距离
                                driver.execute_script(script='window.scrollBy(0,150)')
                                do_loger('执行截屏-详情-流量转化')
                                driver.save_screenshot(f'详情_流量转化_{current_now.replace(":","_")}.png')
                                sleep(1)
                                # 点互动，
                                is_btn_see(driver,By.XPATH,'//*[@id="compass-container"]/div[3]/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[3]/div[2]')
                                sleep(3)
                                do_loger('执行截屏-详情-互动')
                                driver.save_screenshot(f'详情_互动_{current_now.replace(":","_")}.png')
                                sleep(1)
                                #点商品
                                is_btn_see(driver,By.XPATH,'//*[@id="compass-container"]/div[3]/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[3]/div[4]')
                                sleep(3)
                                do_loger('执行截屏-详情-商品')
                                driver.save_screenshot(f'详情_商品_{current_now.replace(":","_")}.png')
                                sleep(1)
                                #关闭详情
                                driver.close()
                                sleep(3)
                                handles = driver.window_handles
                                # print(handles)
                                # 跳回窗口句柄1
                                driver.switch_to.window(handles[0])
                                do_loger('='*20+f'第 {count} 次截图任务已完毕'+'='*20)
                                count+=1 

                            sleep(2)
                        else:
                            do_loger('当前没有账号在直播，等待一段时间后重新检测')
                            auto_wait_time(current_time)
                else:
                    #不是任务时间节点，执行等待
                    do_loger('不在时间节点-执行等待')
                    auto_wait_time(current_now)
            break
        except Exception as e:
            do_loger(f'抛出异常:\n{e}\n'+'='*20+'异常结束标记'+'='*20)
            do_loger('='*20+f'第 {count} 次截图任务失败'+'='*20)
            err_count+=1
            do_loger(f'预计等待{err_wait_time}秒重启任务')
            sleep(err_wait_time)
            do_loger(f'错误统计 - {err_count}')
            

            


if __name__ == '__main__':
    print('select - browser\n1.Chrome\n2.Edge')
    i =input(':')
    if i == '1':
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
        browser = webdriver.Chrome(options=chrome_options)
    elif i=='2':
        from selenium.webdriver.edge.options import Options
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
        browser = webdriver.Edge(options=chrome_options)
    else:
        print('暂时只写了这俩-退出')
        exit()
    sleep(1)
    browser.maximize_window()
    start_task(browser)
    
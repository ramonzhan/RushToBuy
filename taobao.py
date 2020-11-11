# -*- coding=utf-8 -*-
from selenium import webdriver
import datetime
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from io import BytesIO



def login(browser):
    # 打开淘宝登录页，并进行扫码登录
    # browser.get("https://www.taobao.com")
    # time.sleep(3)
    # if browser.find_element_by_link_text("亲，请登录"):
    #     browser.find_element_by_link_text("亲，请登录").click()
    #     print("请在15秒内完成扫码")
    #     time.sleep(15)
    #     browser.get("https://cart.taobao.com/cart.htm")
    # time.sleep(3)
    #
    # now = datetime.datetime.now()
    # print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
    # login
    wait = WebDriverWait(browser, 100, 0.1)
    # wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "登錄"))).click()
    print("click login has finished")

    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "请登录"))).click()
    browser.implicitly_wait(40)
    # browser.find_element_by_partial_link_text("釉白色").click()
    # browser.find_element_by_partial_link_text("8+256G").click()
    while EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "立即购买")):
        browser.find_element_by_partial_link_text("立即购买").click()
        if EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "提交订单")):
            print("购买成功")
            browser.find_element_by_partial_link_text("提交订单").click()
        print("买不到了")

    # wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "请登录"))).click()
    # wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "请登录"))).click()
    print("click message login has finished")
    # wait.until(EC.presence_of_element_located(()))



    # print(login_denglu)



# def buy(times, choose):
#     # 点击购物车里全选按钮
#     if choose == 2:
#         print("请手动勾选需要购买的商品")
#     while True:
#         now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
#         # 对比时间，时间到的话就点击结算
#         if now > times:
#             if choose == 1:
#                 while True:
#                     try:
#                         if browser.find_element_by_id("J_SelectAll2"):
#                             browser.find_element_by_id("J_SelectAll2").click()
#                             break
#                     except:
#                         print("找不到购买按钮")
#             # 点击结算按钮
#             while True:
#                 try:
#                     if browser.find_element_by_link_text("结 算"):
#                         browser.find_element_by_link_text("结 算").click()
#                         print("结算成功")
#                         break
#                 except:
#                     pass
#             while True:
#                 try:
#                     if browser.find_element_by_link_text('提交订单'):
#                         browser.find_element_by_link_text('提交订单').click()
#                         now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
#                         print("抢购成功时间：%s" % now1)
#                 except:
#                     print("再次尝试提交订单")
#             time.sleep(0.01)


if __name__ == "__main__":
    # times = input("请输入抢购时间，格式如(2018-09-06 11:20:00.000000):")
    # # 时间格式："2018-09-06 11:20:00.000000"
    # chrome_driver = r"C:\Users\ramon\Desktop\chromedriver.exe"
    #
    # # 方式一
    # # browser = webdriver.Chrome(executable_path=chrome_driver)
    #
    # # 方式二
    # options = webdriver.ChromeOptions()
    # options.binary_location = chrome_driver
    # browser = webdriver.Chrome(chrome_options=options)
    # print("browser has get")
    # # browser.maximize_window()
    # browser.get("https://www.cnblogs.com/lfri/p/10542797.html")
    # # login()
    # # choose = int(input("到时间自动勾选购物车请输入“1”，否则输入“2”："))
    # # buy(times, choose)

    ##### mate40 purchase
    option = webdriver.ChromeOptions()
    # option.add_argument('headless')  # 静默模式
    # option.binary_location = chrome_driver
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    ### 华为官网
    #driver.get("https://detail.tmall.com/item.htm?spm=a312a.7700824.w20166435-23246766915.6.105d7597htCaLX&id=630289014447&scene=taobao_shop")
    ### 测试官网购买
    driver.get("https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.30632a688gmjCw&id=600268789124&skuId=4193351784184&areaId=411500&user_id=1666576242&cat_id=2&is_b=1&rn=1178966d87fd258f93bd7c35c6689fc9")
    #driver.get("https://world.taobao.com/?scm=20140651.100.hk.1037445769_111588429818_taobao&gclid=CjwKCAiAkan9BRAqEiwAP9X6UXSzaQkpuqPTXIlfnx_B0jI7Hb2ubgn4L3rQsJmBWOcsfLNqGn8_pBoC4wwQAvD_BwE")
    # print(driver.title)
    print(driver.current_url)  #　打印当前地址
    login(browser=driver)



#显示等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep,ctime

# driver =webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://www.baidu.com/')
#将定位元素放在元组里进行传递，而非当成了两个变量进行传递
# element = WebDriverWait(driver,5,0.5).until(EC.visibility_of_element_located((By.ID,'kw')))
# element.send_keys('12')
# # sleep(2)
# driver.quit()

#通过is_displyed()方法实现显示等待
# driver =webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://www.baidu.com/')
# print(ctime())
# for i in range(10):
#     try:
#         element = driver.find_element(By.ID,'kw2')
#         if element.is_displayed():
#             break
#     except:
#         pass
#     sleep(1)
# else:
#     print("time out")
# print(ctime())
#
# driver.quit()


#隐式等待
# driver =webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get('http://www.baidu.com/')
#
# try:
#     print(ctime())
#     driver.find_element(By.ID,'kw').send_keys('12')
# except BaseException as msg:
#     print(msg)
# finally:
#     print(ctime())
# driver.quit()

#定位一组元素
driver =webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(10)
driver.get('http://www.baidu.com/')
driver.find_element(By.ID,'kw').send_keys('selenium')
driver.find_element(By.ID,'su').click()
sleep(2)
elements =driver.find_elements(By.XPATH,"//div[@class='toplist1-td_3zMd4 opr-toplist1-link_2YUtD']/a")

print(len(elements))

for i in elements:
    print(i.text)

driver.quit()


# driver.switch_to_frame()方法切换表单释放iframe，重新回到主页面上driver.switch_to.default_content()

# Selenium页面跳转后的元素定位-switch_to.window()使用
driver.switch_to.window(driver.window_handles[-1])#定位到最新打开窗口
driver.switch_to.window(driver.window_handles[-2])#定位到倒数第二打开窗口
driver.switch_to.window(driver.window_handles[0])#定位最开始页面

#弹框操作alert
alert = driver.switch_to_alert
alert.accept() #等同于单击“确认”或者“OK
alert.dismiss()#等同于单击“取消”或者“Cancel
alert.send_keys()#发送文本，针对有提交需求的prompt框
alert.text#获取alert文本的内容
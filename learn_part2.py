from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#
# class A():
#
#     def __init__(self,a,b):
#         self.a = int(a)
#         self.b = int(b)
#     def add(self):
#         return self.a+self.b
#
# count=A(4,5)
# print(count.add())
#
#
# class B(A):
#     def sub(self,a,b):
#         return a-b
# print(B(2,3).add())

# a='rt'
# try:
#     a ='rr'
#     print(a)
# except BaseException as msg:
#     print(msg)
# finally:
#     print("最后执行")


# def say_hello(name=None):
#     if name is None:
#         raise NameError('"name"can not')
#     else:
#         print("name is %r" %name)
# say_hello()

driver =webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,'form.fm>span>input.s_ipt' ).send_keys('123')
f
sleep(2)
driver.quit()
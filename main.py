#! /usr/bin/python3

from DrissionPage import ChromiumPage,ChromiumOptions
import time
# page = ChromiumPage()
co = ChromiumOptions().auto_port().headless()
page = ChromiumPage(co)
url = 'https://www.ablesci.com/site/login'


page.get(url)   

try:
    #todo
    page.ele('#LAY-user-login-email').input('xxxx@qq.com')
    page.ele('#LAY-user-login-password').input('xxxxxxxx')
    page.ele('登 录').click()
    sign_button = page.ele('今日打卡签到')
    
    if(sign_button):
        sign_button.click()
        # print('签到成功')
        # with open('/root/sign/message.txt','a+',encoding = 'utf-8') as f:
        with open('message.txt','a+',encoding = 'utf-8') as f:
            f.write("签到成功-"+str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"\n"))
        page.ele('关闭').click()
    else:
         with open('message.txt','a+',encoding = 'utf-8') as f:
            f.write("签到失败-"+str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"\n"))

except:
    # with open('/root/sign/message.txt','a+',encoding = 'utf-8') as f:
    with open('message.txt','a+',encoding = 'utf-8') as f:
        f.write("签到失败-"+str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"\n"))

page.ele('.user-avatar').hover()
time.sleep(2)
page.ele('退出').click()
page.quit()





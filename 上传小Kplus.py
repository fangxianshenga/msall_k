# -*- encoding=utf8 -*-
"""
time：2021/3/11

功能：
小K视频上传，
上传成功的会自动生成一个success.txt文件记录，然后可以根据txt文件进行下载
上传失败的会自动生成一个shibai.txt文件记录，等文件上传完后会根据此文件记录的名称再次上传一次
"""

import os
import time
import pywinauto
from selenium import webdriver
from pywinauto.keyboard import send_keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class upload(object):

    #上传地址
    path = r'C:\Users\v_fxfxfang\Desktop\video'

    def __init__(self):
        # self.rename_video()

        ##设置接管理管Chrome浏览器
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=chrome_options)
        #需要上传视频的路径
        # self.videopwd = r'C:\Users\v_fxfxfang\Desktop\video'
        self.videopwd = self.path
        self.videolist = os.listdir(self.videopwd)
        self.wait = WebDriverWait(self.driver, 1000)


    # 执行上传
    def uploadbtn(self, file):
        self.driver.refresh()
        # 定位上传按钮，添加本地文件
        try:
            self.driver.find_element_by_xpath('//div[@class="xk-user-upload m-b-20"]//i[@class="el-icon-upload el-icon--left"]').click()
            selement = self.driver.find_element_by_xpath('//div[@class="el-upload el-upload--text"]')
            time.sleep(2)

            if selement.is_enabled(): ##
                selement.click()

            # self.info(file)
            # 使用pywinauto来选择文件

            app = pywinauto.Desktop()
            # 选择文件上传的窗口
            dlg = app["打开"]

            # 选择文件地址输入框，点击激活
            dlg["Toolbar3"].click()
            # 键盘输入上传文件的路径

            # send_keys(r"D:\video")
            # 键盘输入回车，打开该路径

            send_keys("{VK_RETURN}")

            # 选中文件名输入框，输入文件名
            # dlg["文件名(&N):Edit"].type_keys("12.mp4")
            dlg["文件名(&N):Edit"].type_keys(file)
            # 点击打开
            try:
                for i in range(1,11):
                    dlg["打开(&O)"].click()
            except:
                ...

            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'editor-footer')))

            #点击上传
            time.sleep(20)
            try:
                self.wait.until(

                    EC.presence_of_element_located((By.CLASS_NAME,'editor-footer')))
                sele = self.driver.find_element_by_xpath('//div[@class="editor-footer"]/button[2]')

                for i in range(1,11):
                    sele.click()

            except:
                ...
            print('\n%s  视频上传成功' % file)
            with open('success.txt', 'a', encoding='utf-8') as tp:
                tp.write('\n%s  视频上传成功' % file)


            time.sleep(120)

        except:

            print('%s  视频上传失败' % file)
            with open('shibai.txt', 'a', encoding='utf-8') as tp:
                tp.write('\n%s' % file)
            print('\n%s  视频上传失败' % file)
        self.driver.refresh()

    #修改视频名字
    def rename_video(self):
        path = self.path
        filelist = os.listdir(path)
        print(filelist)
        count = 1

        for item in filelist:
            src = os.path.join(os.path.abspath(path), item)
            dst = os.path.join(os.path.abspath(path), '%d.mp4' % count)
            try:
                os.rename(src, dst)
                count += 1
            except:
                continue


if __name__ == '__main__':

    pq = upload()
    #先修改名字
    # pq.rename_video()

    #上传
    for video in pq.videolist:
        if 'mp4' in video:
            pq.uploadbtn(video)

    ##失败的再次运行
    shibai_path = os.path.dirname(os.path.abspath(__file__))
    shibai = os.path.join(shibai_path, 'shibai.txt')
    f = open(shibai, 'r',encoding='utf-8')
    for i in f:
        if 'mp4' in i:
            pq.uploadbtn(i)
    f.close()
    #上传失败再次上传一次


# coding=utf-8
from datetime import time

from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

def getSize():
    pass


class Login:

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.4'
    desired_caps['deviceName'] = '79KR8PU8SOLV79B6'
    desired_caps['appPackage'] = 'cn.zhimawu'
    desired_caps['appActivity'] = 'cn.zhimawu.SplashActivity'
    driver = webdriver.Remote( 'http://localhost:4723/wd/hub', desired_caps, keep_alive=True )
    driver.implicitly_wait(10000)

    def userlogin(self):
        self.driver.find_element_by_id("cn.zhimawu:id/login").click()
        self.driver.find_element_by_id("cn.zhimawu:id/editPhone").send_keys("15811055793")
        self.driver.find_element_by_id("cn.zhimawu:id/edit_pwd").set_text("1234qwer")
        self.driver.tap([(498, 942)], 1000)  # 模拟手指点击（最多五个手指），可设置按住时间长度（毫秒）
        self.driver.implicitly_wait(20000) #进入美甲类目
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageView").click()
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 1 / 2, y* 4/ 5, x / 2, y* 1/ 5, 10000)#下滑找到作品
        self.driver.tap([(172, 1499)], 1000)#进入作品详情
        self.driver.tap([(833, 1829)], 1000)#立即购买
        self.driver.implicitly_wait(20000)
        self.driver.tap([(833, 1829)], 1000)#提交订单
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout").click()#选择余额支付
        self.driver.find_element_by_id("cn.zhimawu:id/tv_go_pay").click()

if __name__ == '__main__':
    login = Login()
    login.userlogin()





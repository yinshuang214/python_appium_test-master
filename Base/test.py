
#coding=utf-8
import unittest

from appium import webdriver


class Login( unittest.TestCase ):

    def test_login(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = '79KR8PU8SOLV79B6'
        desired_caps['appPackage'] = 'cn.zhimawu.shouyiren'

        desired_caps['appActivity'] = 'cn.zhimawu.shouyiren.activity.login.LaunchActivity'
        #desired_caps['appActivity'] = 'cn.zhimawushouyiren.activity.login.LaunchActivity'
        self.driver = webdriver.Remote( 'http://localhost:4723/wd/hub', desired_caps )

        self.driver.implicitly_wait( 10000 )
        self.driver.find_element_by_id( "cn.zhimawu.shouyiren:id/edv_login_shortcut_phone" ).send_keys( "18310000001" )
        self.driver.find_element_by_id( "cn.zhimawu.shouyiren:id/tv_btn_login_shortcut_submit" ).click()
        self.driver.implicitly_wait( 10000 )
        self.driver.find_element_by_id( "cn.zhimawu.shouyiren:id/tv_btn_login_shortcut_submit" ).click()

if __name__ == '__main__':
    login=Login()
    login.test_login()
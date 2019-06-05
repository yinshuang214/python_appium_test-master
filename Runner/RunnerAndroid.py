# -*- coding: utf-8 -*-
import sys

from Base.BaseMailInfo import sendMail

sys.path.append( ".." )
from Base.BaseRunner import ParametrizedTestCase
import platform
from Base.BaseAndroidPhone import *
from Base.BaseAdb import *
from Base.BaseAppiumServer import AppiumServer
from multiprocessing import Pool
import unittest
from Base.BaseInit import init, mk_file, remove_file
from Base.BaseStatistics import countDate, writeExcel
from datetime import datetime
from Base.BaseApk import ApkInfo
import random
from Base import BaseInit
from Base.BaseLogcat import *
from TestCase.Android.UserClient.test_user_login import UserLogin

PATH = lambda p: os.path.abspath(
    os.path.join( os.path.dirname( __file__ ), p )
)


def kill_adb():
    # windows使用批处理文件将adb服务关闭
    if platform.system() == "Windows":
        # os.popen("taskkill /f /im adb.exe")
        os.system( PATH( "../Util/kill5037.bat" ) )
    # 其他系统则使用命令killall adb 命令
    else:
        os.popen( "killall adb" )
    # 重启adb命令
    os.system( "adb start-server" )


def runnerPool(getDevices):
    devices_Pool = []

    for i in range( 0, len( getDevices ) ):
        _pool = []
        _initApp = {}
        print( "=====runnerPool=========" )
        print( getDevices )
        _initApp["deviceName"] = getDevices[i]["devices"]
        _initApp["udid"] = getDevices[i]["devices"]
        _initApp["platformVersion"] = getAndroidPhoneInfo( devices=_initApp["deviceName"] )["release"]
        _initApp["platformName"] = "android"
        _initApp["port"] = getDevices[i]["port"]
        _initApp["automationName"] = "uiautomator2"
        _initApp["systemPort"] = getDevices[i]["systemPort"]
        _initApp["app"] = getDevices[i]["app"]
        apkInfo = ApkInfo( _initApp["app"] )
        _initApp["appPackage"] = apkInfo.getApkBaseInfo()[0]
        _initApp["appActivity"] = apkInfo.getApkActivity()
        _pool.append( _initApp )
        devices_Pool.append( _initApp )

    pool = Pool( len( devices_Pool ) )
    pool.map( runnerCaseApp, devices_Pool )
    pool.close()
    pool.join()


def runnerCaseApp(devices):
    starttime = datetime.now()
    suite = unittest.TestSuite()
    # 加入测试类
    suite.addTest( ParametrizedTestCase.parametrize( UserLogin, param=devices ) )
    # suite.addTest(ParametrizedTestCase.parametrize(GalleryTest, param=devices))
    unittest.TextTestRunner( verbosity=2 ).run( suite )
    # 结束时间
    endtime = datetime.now()
    # 统计用例执行总时间
    countDate( datetime.now().strftime( '%Y-%m-%d %H:%M:%S' ), str( (endtime - starttime).seconds ) + "秒" )


if __name__ == '__main__':

    # 首先关闭adb命令
    kill_adb()
    # 获取连接的设备信息
    devicess = AndroidDebugBridge().attached_devices()
    if len( devicess ) > 0:

        mk_file( 'android' )
        l_devices = []
        for dev in devicess:
            app = {}
            app["devices"] = dev
            init( dev )
            # 随机生成appium监听端口号
            app["port"] = str( random.randint( 4700, 4900 ) )
            # 随机生成appium(Android-only) 连接设备的端口号
            app["bport"] = str( random.randint( 4700, 4900 ) )
            app["systemPort"] = str( random.randint( 4700, 4900 ) )
            app["app"] = BaseInit.apkPath
            l_devices.append( app )

        # 命令行启用appium server
        appium_server = AppiumServer( l_devices )
        appium_server.start_server()

        # 从runner pool中获取设备和case信息，并执行测试用例验证结果
        runnerPool( l_devices )

        # 从Log中的devices.pickle/info.pickle/sum.pickle中读取数据写入Excel中形成报告
        writeExcel()

        # 发送邮件
        sendMail()

        appium_server.stop_server( l_devices )

        # 删除temp文件
        remove_file( PATH( "../yamls/temp.yaml" ) )

        # #log路径及解析
        # path = PATH("../Log/CrashInfo/Android/")
        # count = getCrashText().Count_crash(path)
        # print('crashlog解析完成，crash次数: %d' % count)
        # #中断logcat
        # # kill_adb()
    else:
        print( "没有可用的安卓设备" )

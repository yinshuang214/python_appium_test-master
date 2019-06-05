# -*- coding: utf-8 -*-

from Base.BaseElements import Element
from Base.BasePickle import *
from Base.BaseFile import *
from Base.BaseApk import *
from Base.BaseIpa import *

'''
初始化操作：
    1.指定被测应用的路径信息
    2.根据手机系统创建一系列文件夹
    3.删除一些日志文件
'''

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


apkPath = PATH("../app/Helijia_4.21.0_4210_debug.apk")  # 测试的安卓app路径
ipaPath = PATH("../app/iOS_NewDevelop_p_debug.ipa")  # 测试的iosapp路径

def mk_file(platform):
    destroy()
    mkdir_file(PATH("../Log/"+Element.INFO_FILE))
    mkdir_file(PATH("../Log/"+Element.SUM_FILE))
    mkdir_file(PATH("../Log/" + Element.DEVICES_FILE))
    data = read(PATH("../Log/"+Element.INFO_FILE))

    #判断执行用例的手机操作系统：android
    if platform == 'android':
        apkInfo = ApkInfo(apkPath).getApkBaseInfo()
        data["appName"] = ApkInfo(apkPath).getApkName()
        data["packageName"] = apkInfo[0]
        data["appVersion"] = apkInfo[2]

        data["sum"] = 0
        data["pass"] = 0
        data["fail"] = 0
        write(data=data, path=PATH("../Log/"+Element.SUM_FILE))
    # 判断执行用例的手机操作系统：ios
    elif platform == 'iOS':
        ipaInfo = getIpaInfo(ipaPath)
        data["appName"] = ipaInfo[0]
        data["packageName"] = ipaInfo[1]
        data["appVersion"] = ipaInfo[2]

        data["sum"] = 0
        data["pass"] = 0
        data["fail"] = 0
        write(data=data, path=PATH("../Log/" + Element.SUM_FILE))


def init(devices):
    # 每次都重新安装uiautomator2都两个应用
    os.popen("adb -s %s uninstall io.appium.uiautomator2.server.test" % devices)
    os.popen("adb -s %s uninstall io.appium.uiautomator2.server" % devices)
    os.popen("adb -s %s install -r %s" % (devices, PATH("../app/appium-uiautomator2-server-v0.1.9.apk")))
    os.popen("adb -s %s install -r %s" % (devices, PATH("../app/appium-uiautomator2-server-debug-androidTest.apk")))


def destroy():
    remove_file(PATH("../Log/"+Element.INFO_FILE))
    remove_file(PATH("../Log/"+Element.SUM_FILE))
    remove_file(PATH("../Log/"+Element.DEVICES_FILE))


if __name__ == '__main__':
    print(destroy())
    mkdir_file("android")
    # print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

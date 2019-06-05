import subprocess

import os

'''
获取ios下的硬件信息
'''

#获取ios设备信息
def getIosDevices():
    devices = []
    result = subprocess.Popen("ideviceinfo -k UniqueDeviceID", shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            devices.append(t[0])
    return devices


def getIosVersion(duid):
    command = "ideviceinfo -u %s -k ProductVersion" % duid
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]


def getIosProductName(duid):
    command = "ideviceinfo -u %s -k DeviceName" % duid
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]

def getIosProductType(duid):
    command = "ideviceinfo -u %s -k ProductType" % duid
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]

def getIosProductOs(duid):
    command = "ideviceinfo -u %s -k ProductName" % duid
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]

def getIosPhoneInfo(duid):
    name = getIosProductName(duid)
    release = getIosVersion(duid)
    type = getIosProductType(duid)
    result = {"release": release, "device": name, "duid": duid, "type": type}
    return result

#编译facebook的wda到真机
def buildWdaIos(duid):
    os.popen(
        "xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination id=" + duid + " test")


if __name__ == '__main__':
    dev_list = []
    devices = getIosDevices()
    for i in range(len(devices)):
        duid = getIosDevices()[i]
        dev = get_ios_PhoneInfo(duid)
        dev_list.append(dev)
    print(dev_list)



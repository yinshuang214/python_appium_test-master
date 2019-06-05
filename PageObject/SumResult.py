from Base.BaseAndroidPhone import getAndroidPhoneInfo
from Base.BaseIosPhone import getIosPhoneInfo
from Base.BaseStatistics import countSum, countInfo, countSumDevices

def statistics_result(**kwargs):
    countSum(kwargs["result"])

    print('Platform:', kwargs["platformName"])
    if kwargs["platformName"] == 'android':
        print('Device:', kwargs["devices"])
        get_phone = getAndroidPhoneInfo(kwargs["devices"])
        phone_name = get_phone["brand"] + "_" + get_phone["model"] + "_" + "android" + "_" + get_phone["release"]

        countInfo(result=kwargs["result"], testInfo=kwargs["testInfo"], caseName=kwargs["caseName"],
                  phoneName=phone_name,
                  driver=kwargs["driver"], logTest=kwargs["logTest"], devices=kwargs["devices"],
                  testCase=kwargs["testCase"],
                  testCheck=kwargs["testCheck"])
        countSumDevices(kwargs["devices"], kwargs["result"], phone_name=phone_name)
    elif kwargs["platformName"] == 'iOS':
        print('Device:', kwargs["devices"])
        get_phone = getIosPhoneInfo(kwargs["devices"])
        phone_name = get_phone["device"] + "_" + get_phone["release"] + "_" + "iOS" + "_" + get_phone["duid"]

        countInfo(result=kwargs["result"], testInfo=kwargs["testInfo"], caseName=kwargs["caseName"],
                  phoneName=phone_name,
                  driver=kwargs["driver"], logTest=kwargs["logTest"], devices=kwargs["devices"],
                  testCase=kwargs["testCase"],
                  testCheck=kwargs["testCheck"])
        countSumDevices(kwargs["devices"], kwargs["result"], phone_name=phone_name)


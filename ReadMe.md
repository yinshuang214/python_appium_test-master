## 简介
采用python3+appium，基于PageObject框架的UI自动化测试持续集成。
* unittest参数化
* PageObject分层管理
* 用例编写基于yaml配置多关键字驱动
* 自动生成excel测试报告
* 将Excel报告发送到邮件附件中
* 同时支持Android/iOS
* 支持多设备执行
* 支持Windows/Mac OS （iOS必须使用Mac OS）


## 目录结构

#### app
```
 待测apk/ipa 安装包路径
 uiautomator2等安装包路径
```

#### Base
 ```
Android 测试相关：
BaseAdb.py 封装常用的ADB命令
BaseAndroidPhone.py 使用ADB命令获取安卓设备信息
BaseApk.py 通过给定的apk文件获取package、version、activity等信息
BaseLog.py 通过logcat获取日志信息
BaseLogcat.py 分析logcat日志

iOS 测试相关：
BaseIosPhone.py 获取ios设备信息
BaseIpa.py  根据给定的ipa文件获取文件的version、appName等
BaseIosLog.py ios日志

数据处理相关：
BaseConfig.py 
BaseExcel.py
BaseFile.py
BasePickle.py
BaseYaml.py
BaseOperate.py
BaseReplace.py

测试执行相关：
BaseAppiumServer.py
BaseInit.py
BaseRunner.py
BaseElements.py

报告相关：
BaseStatisics.py
BaseError.py
BaseEmail.py
```
### Runner
```
RunnerAndroid.py 安卓测试用例主入口
RunnerIOS.py ios测试用例主入口
```
### Log-运行时自动生成
```
设备日志及持久化数据
操作日志，失败截图
crash解析结果
.pickle 记录case运行的中间数据，用来产生测试报告
```
### PageObject
```
操作的封装及测试结果统计
测试用例模块分级
```
### TestCase
```
Android、IOS 区分不同系统的app用例
UserClient、Merchant 区分用户端商户端用例
```
### 其他
```
../yamls  用例管理
../Util   批处理文件和公共方法
```


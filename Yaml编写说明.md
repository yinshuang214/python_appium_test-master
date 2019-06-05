####YAML测试用例编写说明
```angular2
testinfo: 表示用例介绍
    - id: 用例id
    - title: 用例标题
    - info: 前置条件
testcase: 用例的执行步骤
    - element_info: //XCUIElementTypeStaticText[@name="剪辑"] 元素
    -  find_type: id  元素类型
        - id
        - xpath
        - name
        - text
        - ids 需要增加index
        - index 和ids/xpaths/texts等配合 
        - class_name
        - ios_id
        - predicate

    - operate_type: click 操作
        - click 点击 
        - swipe_down 向下滑动
        - swipe_up 向上滑动
        - get_value 获取值
        - set_value 输入值
        - screen_tap 屏幕轻触tap
        - swipe_left 左滑
        - swipe_right 向右滑动
        - msg 传给set_value关键字（要向文本框输入的内容）
        - adb_tab 使用adb中的tab命令点击元素,元素必须可识别，应用于悬浮层场景
        - get_content_desc 无法切换到webview时，用此关键字
        - press_key_code 键盘触发事件，需要传code
        - code 传给press_key_code关键字
        - is_webview:1 为1表示切换到webview,为2表示切换到原生
        - 其他关键字 用于定制一些特殊业务
    - is_time: 3 自定义暂停3秒
    - info: 点击动态列表第一条数据 操作步骤介绍

- check: 检查点,支持多检查点
  - element_info: //XCUIElementTypeStaticText[@name="剪辑"]
  - find_type: ids
  - index: 0
  - operate_type:
    - contrary"  相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在
    - contrary_getval  检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
    - default_check  默认检查点，就是查找页面元素
    - compare 历史数据和实际数据对比
    - toast  toast检查
  - info: 查找是否存在历史记录

```
```
####YAML测试用例模板
testinfo:
    - id: test_start_001
      title: 登录测试
      info: 登录测试验证

testcase:
    - element_info: login
      is_time: 3
      find_type: id
      operate_type: click
      info: 点击开屏'登录'按钮

    - element_info: editPhone
      find_type: id
      operate_type: set_value
      msg: '18600105776'
      info: 输入手机号

    - element_info: edit_pwd
      is_time: 3
      find_type: id
      operate_type: set_value
      msg: '111111qq'
      info: 输入密码

    - element_info: btn_login
      find_type: id
      operate_type: click
      info: 点击登录按钮


check:
    - element_info: btn_login
      find_type: id
      check: default_check
      info: 验证填写手机控件存在

```
####YAML测试用例模板（用户端登录）

```angular2
testinfo:
    - id: test_login_001
      title: 登录测试
      info: 登录测试验证

testcase:
    - element_info: login
      is_time: 3
      find_type: id
      operate_type: click
      info: 点击开屏'登录'按钮

    - element_info: editPhone
      find_type: id
      operate_type: set_value
      msg: '18600105776'
      info: 输入手机号

    - element_info: edit_pwd
      is_time: 3
      find_type: id
      operate_type: set_value
      msg: '111111qq'
      info: 输入密码

    - element_info: btn_login
      find_type: id
      operate_type: click
      info: 点击登录按钮


check:
    - element_info: btn_login
      find_type: id
      check: default_check
      info: 验证填写手机控件存在

```
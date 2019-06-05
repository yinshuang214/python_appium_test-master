from Base.BaseSendMail import send_mail
import os

PATH = lambda p: os.path.abspath(
    os.path.join( os.path.dirname( __file__ ), p )
)


# 定义发送邮件的信息
def sendMailInfo():
    to_addr = ["houzi@helijia.com"]
    mail_host = "smtp.qq.com"
    mail_user = "974071737@qq.com"
    mail_pass = "zobxvejfugghbcib"
    port = "465"
    header_msg = "【质量保障】Appium自动化测试报告"
    attach = "Hi All,\n 自动化测试报告在附件中，请查收"
    report = PATH( "../Report/report.xlsx" )
    send_mail( to_addr=to_addr, mail_host=mail_host, mail_user=mail_user, port=port, mail_pass=mail_pass,
               header_msg=header_msg, report=report, attach=attach, report_name="Appium自动化测试报告.xls" )


# 发送邮件
def sendMail():
    sendMailInfo()

# 测试代码
if __name__ == "__main__":
    sendMailInfo()

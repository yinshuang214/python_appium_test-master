# -*- coding: utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
import os

PATH = lambda p: os.path.abspath(
    os.path.join( os.path.dirname( __file__ ), p )
)

#格式化邮件地址
def _format_addr(s):
    name, addr = parseaddr( s )
    return formataddr( (Header( name, 'utf-8' ).encode(), addr) )

#发送邮件
def send_mail(**kwargs):
    '''
    :param f: 附件路径
    :param to_addr:发给的人 []
    :return:
    '''
    from_addr = kwargs["mail_user"]
    password = kwargs["mail_pass"]
    smtp_server = kwargs["mail_host"]

    msg = MIMEMultipart()

    # msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
    msg['From'] = _format_addr( 'AutomationTeam <%s> ' %from_addr )
    msg['To'] = _format_addr( ' <%s>' % kwargs["to_addr"] )
    msg['Subject'] = Header( kwargs["header_msg"], 'utf-8' ).encode()
    msg.attach( MIMEText( kwargs["attach"], 'plain', 'utf-8' ) )

    if kwargs.get( "report", "0" ) != "0":
        part = MIMEApplication( open( kwargs["report"], 'rb' ).read() )
        part.add_header( 'Content-Disposition', 'attachment', filename=('gb2312', '', kwargs["report_name"]) )
        msg.attach( part )

    server = smtplib.SMTP_SSL( smtp_server, kwargs["port"] )
    server.set_debuglevel( 1 )
    server.login( from_addr, password )
    server.sendmail( from_addr, kwargs["to_addr"], msg.as_string() )
    server.quit()

#测试邮件发送
if __name__ == '__main__':
    to_addr = ["houzi@helijia.com"]
    mail_host = "smtp.qq.com"
    mail_user = "974071737@qq.com"
    mail_pass = "zobxvejfugghbcib"
    port = "465"
    header_msg = "lalalalal"
    attach = "Appium自动化测试"
    report = PATH( "../Base/report.xlsx" )
    send_mail( to_addr=to_addr, mail_host=mail_host, mail_user=mail_user, port=port, mail_pass=mail_pass,
               header_msg=header_msg, report=report, attach=attach, report_name="Appium自动化测试报告.xls" )

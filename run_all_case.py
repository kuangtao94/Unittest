"""
1.discover方法里面有三个参数：
-case_dir:这个是待执行用例的目录。
-pattern：这个是匹配脚本名称的规则，test*.py意思是匹配test开头的所有脚本。
-top_level_dir：这个是顶层目录的名称，一般默认等于None就行了。
2.discover加载到的用例是一个list集合，需要重新写入到一个list对象testcase里;
这样就可以用unittest里面的TextTestRunner这里类的run方法去执行。
"""

import unittest
import os,time
import HTMLTestRunner
from tomorrow import threads
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#unittest_test目录，下有case和report
cur_path = os.path.dirname(__file__)

def all_case(casename="case",rule="test*.py"):
    '''第一加载所有的测试用例'''
    case_path = os.path.join(cur_path,casename) #用例路径拼接
    #如果不存在case文件夹，自动创建
    if not os.path.exists(case_path):os.mkdir(case_path)
    discover = unittest.TestLoader().discover(
        casename,
        pattern=rule,
        top_level_dir=None
    )
    return discover

# def getNowtime():
#     return time.strftime("%Y-%M-%D %H-%M-%S",time.localtime(time.time()))

def report():
    """第二执行所有用例，并把结果写入HTML测试报告中"""
    # now = time.strftime("%Y-%M-%D %H-%M-%S")
    report_path = os.path.join(cur_path,"report") #report文件夹
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path,"result.html")  # html报告文件路径
    # file = os.path.join(os.path.dirname(__file__), "Report", "testReport.html")
    # print("report_path:%s"%report_abspath)
    with open(report_abspath, "wb") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=u'自动化测试报告,测试结果如下：',
            description=u'用例执行情况：')
        # 调用add_case函数返回值
        runner.run(all_case())
    return report_abspath

def send_mail():
    """第三发送测试报告"""
    # ----------1.跟发件相关的参数------

    smtpserver = "smtp.163.com"  # 发件服务器
    # smtpserver = "smtp.qq.com"
    port = 25  # 非SSL协议端口号
    # sender = "XXXX" # 账号
    sender = "自己163邮箱账号"
    psw = "自己的邮箱密码"
    # psw = "wmqtqbtnmyamhfjd" # 密码
    receiver = "xxxxx@qq.com" # 单个接收人也可以是 list
    # receiver = ["xxxxx@qq.com"]  # 多个收件人 list 对象

    # ----------2.编辑邮件的内容------
    # 读文件
    # file_path = "Result.html"
    # with open(file_path, "rb") as fp:
    #     mail_body = fp.read()
    with open(report(),"rb") as f:
        mail_body = f.read()
    msg = MIMEMultipart()
    msg["from"] = sender  # 发件人
    msg["to"] = receiver  # 收件人
    # msg["to"] = ";".join(receiver) # 多个收件人 list 转 str
    msg["subject"] = "我的主题报告-test"  # 主题

    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)

    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)

    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port) # QQ 邮箱
        smtp.login(sender, psw)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()


def main():
    send_mail()

if __name__ == '__main__':
    # runner = unittest_1.TextTestRunner()
    # runner.run(all_case())
    main()

    # report_abspath = os.path.join(report_path, "result.html")  # html报告文件路径
    # fp = open(report_abspath, "wb")
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u'自动化测试报告,测试结果如下：',
    #     description=u'用例执行情况：')
    # # 调用add_case函数返回值
    # runner.run(all_case())
    # fp.close()





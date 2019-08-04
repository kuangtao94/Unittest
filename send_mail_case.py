from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

base_file = os.path.abspath(r"report\result.html")


def is_result_pass():
    try:
        with open(base_file,"rb") as fp:
            file = fp.read()  # 读报告
        soup = BeautifulSoup(file,"html.parser")
        status = soup.find_all(class_="attribute")
        result = status[2].contents[-1]  # 获取报告结果
        if "Failure " in result or "Error" in result:
            print("测试过程有不通过的用例:%s"%result)
            return False
        else:
            return True
    except Exception as msg:
        print("测试过程中存在异常:%s"%str(msg))
        return False

if __name__ == '__main__':
    is_result_pass()

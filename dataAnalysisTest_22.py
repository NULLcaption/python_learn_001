"""
将自动化生成的数据通过邮件的形式发送个相关的人员
文件超过100M会出错
"""
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib

if __name__ == '__main__':
    fromaddr = 'xg.chen@chinaxpp.com'
    password = 'Zh19900331'
    toaddrs = ['ts.pan@chinaxpp.com', 'cxg1207@126.com']

    content = '2020年马上赢数据通过Python筛选出香飘飘和优乐美的所有数据'
    textApart = MIMEText(content)

    zipFile = 'F:\\test_data\\data3.csv'
    zipApart = MIMEApplication(open(zipFile, 'rb').read())
    zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

    m = MIMEMultipart()
    m.attach(textApart)
    m.attach(zipApart)
    m['Subject'] = '自动发送邮件机器人'

    try:
        server = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('send success')
        server.quit()
    except smtplib.SMTPException as e:
        print('send error:', e)  # 打印错误
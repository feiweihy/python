#!/usr/bin/python3

import smtplib
import com.jieyi.practice.EMailUtil as EMailUtil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


# 创建一个带附件的实例
message = MIMEMultipart('related')
message['From'] = Header("捷羿OA", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
subject = '2019年年会通知'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
content_txt = '各位同事：\n'
content_txt += '    “捷羿年会”即将拉开帷幕，诚挚邀请大家参加！附件为：行程安排、车辆安排、住宿安排！请带好身份证以及泳衣！年会期间！请大家一定要注意安全！遵守年会秩序！ \n'
content_txt += '--------------------------------------------------------------------------------\n'
content_txt += '张璐\n'
content_txt += '上海捷羿软件系统有限公司\n'
content_txt += '地址：上海市徐汇区桂箐路111号901\n'
content_txt += '电话：021-54279998\n'
content_txt += '传真：021-54279669\n'
content_txt += '手机：15800579445\n'


message.attach(MIMEText(content_txt, 'plain', 'utf-8'))

att1 = MIMEText(open('D:\\jieyiemail\\AnnualMeeting2019\\1-车辆统计.xlsx', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1.add_header('Content-Disposition', 'attachment',filename=('utf-8', '', r'1-车辆统计.xlsx'))

message.attach(att1)

att2 = MIMEText(open('D:\\jieyiemail\\AnnualMeeting2019\\2-年会行程安排.docx', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2.add_header('Content-Disposition', 'attachment',filename=('utf-8', '', r'2-年会行程安排.docx'))

message.attach(att2)

att3 = MIMEText(open('D:\\jieyiemail\\AnnualMeeting2019\\3-住宿安排.xlsx', 'rb').read(), 'base64', 'utf-8')
att3["Content-Type"] = 'application/octet-stream'
att3.add_header('Content-Disposition', 'attachment',filename=('utf-8', '', r'3-住宿安排.xlsx'))

message.attach(att3)

smtpObj = smtplib.SMTP()
smtpObj.connect(EMailUtil.mail_host, 25)  # 25 为 SMTP 端口号
smtpObj.login(EMailUtil.mail_user, EMailUtil.mail_pass)
for x in EMailUtil.receivers:
    try:
        smtpObj.sendmail(EMailUtil.sender, x, message.as_string())
        print("["+x+"]邮件发送成功")
    except smtplib.SMTPException:
        print("Error: ["+x+"]无法发送邮件")


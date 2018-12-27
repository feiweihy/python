#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.ym.163.com"  # 设置服务器
mail_user = "oa@jieyisoft.com"  # 用户名
mail_pass = "111111"  # 口令

sender = 'oa@jieyisoft.com'
receivers = ['529486618@qq.com','399935318@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receivers = ['894228236@qq.com',
             'fengwei@jieyisoft.com',
             'liukougen@jieyisoft.com',
             'wenshuanghua@jieyisoft.com',
             'gaozhongnan@jieyisoft.com',
             'yuxiaohui@jieyisoft.com',
             'xiangpingbo@jieyisoft.com',
             'liangdawei@jieyisoft.com',
             'sunsanrong@jieyisoft.com',
             'zhaoyan@jieyisoft.com',
             'zhangya@jieyisoft.com',
             'weiziyang@jieyisoft.com',
             'jiangyongqiang@jieyisoft.com',
             'hanxiaoming@jieyisoft.com',
             'chenchao@jieyisoft.com',
             'caodangfeng@jieyisoft.com',
             'dinghao@jieyisoft.com',
             'zhonghuizhi@jieyisoft.com',
             'zhangdawei@jieyisoft.com',
             'aijingjiao@jieyisoft.com',
             'huxiang@jieyisoft.com',
             'fengguoqiang@jieyisoft.com',
             'kanhonghua@jieyisoft.com',
             'jiangxufeng@jieyisoft.com',
             'zhoufuchun@jieyisoft.com',
             'linan@jieyisoft.com',
             'liuwenjie@jieyisoft.com',
             'lizhencheng@jieyisoft.com',
             'liang@jieyisoft.com',
             'mengxianning@jieyisoft.com',
             'liusheng@jieyisoft.com',
             'caokuan@jieyisoft.com',
             'xudong@jieyisoft.com',
             'minqiang@jieyisoft.com',
             'huyujun@jieyisoft.com',
             'jiangchao@jieyisoft.com',
             'liaochengtie@jieyisoft.com',
             'wanghao@jieyisoft.com',
             'yuyong@jieyisoft.com',
             'banyunfei@jieyisoft.com',
             'zoujun@jieyisoft.com',
             'jinghuan@jieyisoft.com',
             'lihao@jieyisoft.com',
             'liuwenhao@jieyisoft.com',
             'zhanglu@jieyisoft.com',
             'pengxiaomei@jieyisoft.com',
             'raoyou@jieyisoft.com',
             'wanlingling@jieyisoft.com',
             'fengyuping@jieyisoft.com',
             'huanglili@jieyisoft.com',
             'shitongshuo@jieyisoft.com',
             'liuchuandong@jieyisoft.com',
             'renzhiqiang@jieyisoft.com',
             'zhaolei@jieyisoft.com',
             'shuxiaomin@jieyisoft.com',
             'zhanglei@jieyisoft.com',
             'lizhi@jieyisoft.com',
             'mayue@jieyisoft.com',
             'yuandong@jieyisoft.com',
             'fanhao@jieyisoft.com',
             'xujun@jieyisoft.com',
             'lushiyu@jieyisoft.com',
             'luoming@jieyisoft.com',
             'chenhui@jieyisoft.com',
             'guofeng@jieyisoft.com',
             'songqiang@jieyisoft.com',
             'wangluhao@jieyisoft.com',
             'wangpan@jieyisoft.com',
             'liuquan@jieyisoft.com',
             'menxiaosai@jieyisoft.com',
             'xiongkun@jieyisoft.com',
             'xiechunyang@jieyisoft.com',
             'wujianlin@jieyisoft.com',
             'lizhiming@jieyisoft.com',
             'chenkang@jieyisoft.com',
             'linyinjie@jieyisoft.com',
             'luxiaoxiao@jieyisoft.com',
             'maochengye@jieyisoft.com',
             'jinxu@jieyisoft.com',
             'jiangpan@jieyisoft.com',
             'lifeng@jieyisoft.com',
             'wangpengfeng@jieyisoft.com',
             'tiandenghui@jieyisoft.com',
             'zhongbo@jieyisoft.com',
             'yangchenyu@jieyisoft.com',
             'zhangjiang@jieyisoft.com',
             'liuzhiyang@jieyisoft.com',
             'jiang_chao@jieyisoft.com',
             'wuhongzhao@jieyisoft.com',
             'zhenyi@jieyisoft.com',
             'liuxu@jieyisoft.com',
             'wangyoupeng@jieyisoft.com',
             'geqisheng@jieyisoft.com',
             'yangfeiyue@jieyisoft.com',
             'panjianyu@jieyisoft.com',
             'shuibo@jieyisoft.com',
             'yangxiaofeng@jieyisoft.com',
             'guoqing@jieyisoft.com',
             'quanli@jieyisoft.com',
             'cixu@jieyisoft.com']

# 创建一个带附件的实例
message = MIMEMultipart('related')
message['From'] = Header("捷羿OA", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
subject = '个人所得税专项附加扣除通知'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
content_txt = '各位同事：\n'
content_txt += '    十月份个税改革的红利刚进钱包，第二波红利又来啦！财政部、国家税务总局会同有关部门起草的《个人所得税专项附加扣除暂行办法》将于2019年1月1日起实施。\n'
content_txt += '\n'
content_txt += '       个人所得税专项附加扣除，是指个人所得税法规定的子女教育、住房贷款利息、住房租金、赡养老人、继续教育及大病医疗六项专项附加扣除。\n'
content_txt += '\n'
content_txt += '    附件是个人所得税系统APP安装注册指引以及2019新个人所得税专项附加扣除《暂行办法》解读，帮助大家理解“新个税法”（另：下载app后截图给我确认！专项扣除模块于2019年1月1日开放，请各位按照实际情况尽快填写！）\n'
content_txt += '--------------------------------------------------------------------------------\n'
content_txt += '张璐\n'
content_txt += '上海捷羿软件系统有限公司\n'
content_txt += '地址：上海市徐汇区桂箐路111号901\n'
content_txt += '电话：021-54279998\n'
content_txt += '传真：021-54279669\n'
content_txt += '手机：15800579445\n'


message.attach(MIMEText(content_txt, 'plain', 'utf-8'))

att1 = MIMEText(open('D:\\2019新个人所得税专项附加扣除《暂行办法》解读.pdf', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1.add_header('Content-Disposition', 'attachment',filename=('utf-8', '', r'1-2019新个人所得税专项附加扣除《暂行办法》解读.pdf'))

message.attach(att1)

# 构造附件2，传送当前目录下的 runoob.txt 文件
# MIMEMultipart(open('test.xlsx', 'rb').read())
att2 = MIMEText(open('D:\\个人所得税系统APP安装注册指引.docx', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2.add_header('Content-Disposition', 'attachment',filename=('utf-8', '', r'2-人所得税系统APP安装注册指引.docx'))
message.attach(att2)

smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
smtpObj.login(mail_user, mail_pass)
for x in receivers:
    try:
        smtpObj.sendmail(sender, x, message.as_string())
        print("["+x+"]邮件发送成功")
    except smtplib.SMTPException:
        print("Error: ["+x+"]无法发送邮件")


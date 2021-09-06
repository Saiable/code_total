"""
邮件发送,除非重大异常不用
"""
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
import time

# 接收服dao务器： pop.139.com
# 发送服务器： smtp.139.com
def sendEmail(biao_ti='睿企', nei_rong='睿企', file_name='', emil_receiver='zangzhenhua1996@163.com'):
    """
    发送邮件
    :param biao_ti:标题
    :param nei_rong:  内容
    :param file_name: 附件文件名
    :return:
    """
    try:
        email_sender = '318977674@qq.com'  # 这里是qq邮箱
        email_pwd = 'yfhyoyucukcvcbdi'  # 这里是授权码，不知道qq邮箱怎么获取授权码的同事可以百度一下
        # email_receiver = '624840539@qq.com'
        email_receiver = emil_receiver
        email_sever = SMTP_SSL('smtp.qq.com')  # 连接qq邮箱服务器
        email_sever.login(email_sender, email_pwd)  # 登录邮箱

        email_text = MIMEText(nei_rong, 'plain', 'utf-8')  # 邮件的内容，和内容的格式。这里是txt/plain，纯文本类型。
        email_liction = MIMEMultipart()  # 创建一个带附件的事例
        email_liction['Subject'] = Header(biao_ti, 'utf-8')  # 标题的内容和编码格式
        email_liction['From'] = email_sender
        email_liction['To'] = email_receiver
        email_liction['Date'] = time.ctime()
        if file_name:
            pass
        else:
            with open("无附件.txt", "w", encoding="utf-8") as f:
                f.write("无附件内容")
            file_name = "无附件.txt"

        email_file = MIMEApplication(
            open(file_name, 'rb').read())  # 第一个参数打开文件read()方法读出所有内容，刚好是字符串格式,第二个参数是希望的编码，这种方法比较简单
        email_file.add_header('Content-Disposition', 'attachment',
                              filename=file_name)  # 这里添加一个标题，Content-Disposition,attachment说明是一个附件，filename说明文件名．mail里有一个get_filename()的方法可以得到附件里的文件名。
        # filename不能随便命名，因为后缀名会影响到文本的格式。例如把"html"换成"txt"，最后加载到QQ邮件的附件就是‘temp.txt’。
        email_liction.attach(email_text)  # 把我们刚才写的邮件内容加进去
        email_liction.attach(email_file)  # 现在我们把编码好的附件也加进去
        try:
            email_sever.sendmail(email_sender, email_receiver,
                                 email_liction.as_string())  # 由于senemail要传String类型，所以要用.as_string()把内容组合成字符串
            print("发送成功")
        except Exception as e:
            print("发送失败")
        finally:
            email_sever.quit()
    except:
        pass


if __name__ == '__main__':
    sendEmail(biao_ti='222', nei_rong='222222', file_name='', emil_receiver='zangzhenhua1996@163.com')

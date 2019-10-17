import smtplib
from email.mime.text import MIMEText
from django.conf import settings
from apps.process.models import Intermediate,Process
from apps.permissions.models import User


mail_host = settings.MAIL_HOST
mail_user = settings.MAIL_USER
mail_pass = settings.MAIL_PASSWORD

mail_news = {}

def send_mail(to_list, sub, content):
    me = "LogServer"+"<"+mail_user+">"
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False

class Mail:
    def __init__(self,to_list,mail_host=mail_host,
                 mail_user=mail_user,mail_pass=mail_pass):

        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.to_list = to_list

    def send_mail(self,to_list, sub, content):
        me = "LogServer" + "<" + mail_user + ">"
        msg = MIMEText(content, _subtype='plain', _charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
            server = smtplib.SMTP()
            server.connect(self.mail_host)
            server.login(self.mail_user,self.mail_pass)
            server.sendmail(me, to_list, msg.as_string())
            server.close()
            return True
        except Exception as e:
            print(str(e))
            return False



class ProcessMail(Mail):

    def __init__(self,mail_host=mail_host,
                 mail_user=mail_user,mail_pass=mail_pass):

        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass



    def get_process_obj(self,process_obj):
        process_dict = {}
        process_dict['id'] = process_obj.id
        process_dict['title'] = process_obj.name
        process_dict['create_user'] = process_obj.create_user
        process_dict['create_time'] = process_obj.create_time
        process_dict['describe'] = process_obj.describe
        process_dict['user'] = process_obj.user
        return process_dict

    def auditing_notice(self,process_obj):
        title = '流程审核通知'
        content = '''
        审核流程表: %s
        流程申请人: %s
        创建时间: %s
        描述: %s
        查看详情: %s
        '''%(process_obj['title'],process_obj['create_user'],process_obj['create_time'],process_obj['describe'],process_obj['url'])
        self.send_mail(self.to_list,title,content)

    def auditing_success(self,process_obj):
        title = '恭喜您！流程审核通过了！'
        content = '''
        审核流程表: %s
        创建时间: %s
        描述: %s
        查看详情: %s
        ''' % (process_obj['title'],process_obj['create_user'], process_obj['describe'],process_obj['url'])
        self.send_mail(self.to_list,title,content)

    def auditing_failed(self,process_obj):
        title = '很遗憾！您的流程被拒绝了！'
        content = '''
        审核流程表: %s
        创建时间: %s
        描述: %s
        拒绝人: %s
        查看详情: %s
        '''% (process_obj['title'],process_obj['create_time'], process_obj['describe'], process_obj['user'],process_obj['url'])
        self.send_mail(self.to_list, title, content)

    def send_notice(self,id,host):
        intermediate_obj = Intermediate.objects.filter(id=id).all()
        for i in intermediate_obj:intermediate_obj = i
        user_process = User.objects.filter(id=intermediate_obj.user).all()
        self.to_list = [user_process.values('email')[0]['email']]
        url = host + '/process/audit/info/?audit=' + str(id)
        process_dict = self.get_process_obj(intermediate_obj)
        process_dict['url'] = url
        self.auditing_notice(process_dict)

    def send_failed(self,id,host):
        intermediate_obj = Intermediate.objects.filter(id=id).all()
        for i in intermediate_obj:intermediate_obj = i
        user_process = User.objects.filter(name=intermediate_obj.create_user).all()
        self.to_list = [user_process.values('email')[0]['email']]
        url = host + '/process/audit/info/?audit=' + str(id)
        process_dict = self.get_process_obj(intermediate_obj)
        process_dict['url'] = url
        process_dict['user'] = User.objects.filter(id=process_dict['user']).values('username')[0]['username']
        self.auditing_failed(process_dict)

    def send_success(self,id,host):
        intermediate_obj = Intermediate.objects.filter(id=id).all()
        for i in intermediate_obj: intermediate_obj = i
        user_process = User.objects.filter(name=intermediate_obj.create_user).all()
        self.to_list = [user_process.values('email')[0]['email']]
        url = host + '/process/audit/info/?audit=' + str(id)
        process_dict = self.get_process_obj(intermediate_obj)
        process_dict['url'] = url
        process_dict['user'] = User.objects.filter(id=process_dict['user']).values('username')[0]['username']
        self.auditing_success(process_dict)



if __name__ == '__main__':
    m = Mail(mailto_list)
    content = '1'
    send_mail(mailto_list,'测试',content)

from lib.page import PagerObj
from apps.process import models as process_models
from apps.permissions.models import User
from django.utils.safestring import mark_safe

class OptionProcess:

    def __init__(self,option_process,current_page,base_url,intermediate_obj, total_num=10):

        self.option_process = option_process
        self.current_page = current_page
        self.base_url = base_url
        if self.base_url.endswith('/'):
            self.base_url = base_url.rstrip('/')
        self.intermediate_obj = intermediate_obj
        self.total_num = total_num

    def process_page(self):
        if self.option_process == 'all':
            page = PagerObj(self.current_page, '{}/?option_process_select=all'.format(self.base_url),self.intermediate_obj, self.total_num)
            pager, process_list = page.pages()
            all = "selected"
            return {"process_list": process_list, 'pager': mark_safe(pager), 'all': all}
        elif self.option_process == 'audit':
            intermediate_obj = self.intermediate_obj.filter(status='0').all()
            page = PagerObj(self.current_page, '{}/?option_process_select=audit'.format(self.base_url),intermediate_obj, self.total_num)
            pager, process_list = page.pages()
            audit = 'selected'
            return {"process_list": process_list, 'pager': mark_safe(pager), 'audit': audit}
        elif self.option_process == 'success':
            intermediate_obj = self.intermediate_obj.filter(status='2').all()
            page = PagerObj(self.current_page, '{}/?option_process_select=success'.format(self.base_url), intermediate_obj, self.total_num)
            pager, process_list = page.pages()
            success = "selected"
            return {"process_list": process_list, 'pager': mark_safe(pager), 'success': success}
        elif self.option_process == 'failed':
            intermediate_obj = self.intermediate_obj.filter(status='1').all()
            page = PagerObj(self.current_page, '{}/?option_process_select=failed'.format(self.base_url), intermediate_obj, self.total_num)
            pager, process_list = page.pages()
            failed = "selected"
            return {"process_list": process_list, 'pager': mark_safe(pager), 'failed': failed}


class UserProcessObj:
    def __init__(self,id):
        self.id = id

    def get_process_obj(self):
        process_obj = process_models.Process.objects.filter(id=self.id)
        process_user_id = process_obj.values('process')[0]['process']
        for i in process_obj:
            process_obj = i
        user_list_obj = []
        process_user_id_list = process_user_id.split(',')
        for i in process_user_id_list:
            user_obj = User.objects.all().filter(id=i).all()
            for j in user_obj.values():
                user_list_obj.append(j)

        return process_obj,user_list_obj


def read_process(audit_user,process_id):
    intermediate_obj = process_models.Intermediate.objects.get(id=process_id)
    if int(intermediate_obj.user) == audit_user:
        if intermediate_obj.is_read == 0:
            process_models.Intermediate.objects.filter(id=process_id).update(is_read=1)

def set_read_process(audit_user,process_id):
    intermediate_obj = process_models.Intermediate.objects.get(id=process_id)
    if process_models.Intermediate.objects.get(id=process_id).is_read == 1:
        process_models.Intermediate.objects.filter(id=process_id).update(is_read=0)

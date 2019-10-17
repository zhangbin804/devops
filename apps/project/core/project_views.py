from apps.accounts.forms.forms import CreateProjectForm
from apps.project.models import *
from apps.accounts.core.accounts_auth import get_user_id
from apps.permissions.models import User
from lib.Git.GIT import GitApi
from lib.Ansiable.ansible_server_user import ansible_run
from lib.Ansiable.yaml.server_user_yaml import *
from apps.operational.create.password import random_str
from lib.Cmd.cmd import *
import time


def rsync_project(src,dst,exclude=None):
    if str(src).endswith('/'):
        src = src + '*'
    else:
        src = src + '/*'
    rsync_log = rsync(src=src,dst=dst,exclude=exclude)
    return rsync_log



def get_project_host(id):
    host = ''
    project_obj = Project.objects.get(id=id)
    group = project_obj.server_group.server_set.all()
    if group:
        for i in group:
            if host:
                host = host + ',' + i.ip
            else:
                host = i.ip
    return host


def is_flase(value):
    ret = None
    if value:
        ret = str(value)
    else:
        ret = ''
    return ret


def auth_git_url(project_id):
    git_url = ''
    project_obj = Project.objects.get(id=project_id)
    if project_obj.git_auth_way == 0:
        url_list = project_obj.git_url.split('//')
        git_user = is_flase(project_obj.git_user)
        git_password = is_flase(project_obj.git_password)
        if git_user and git_password:
            git_url = url_list[0] + '//' + git_user + ':' + "'" + git_password + "'@" + url_list[1]
        else:
            git_url = project_obj.git_url
    elif project_obj.git_auth_way == 1:
        git_url = project_obj.git_url
    return git_url


def exclude_file(id):
    project_obj = Project.objects.get(id=id)
    exclude = ' --exclude=.git '
    if project_obj.exclude_file:
        for i in str(project_obj.exclude_file).split(','):
            if i:
                exclude = exclude + ' ' + '--exclude=' + i
    return exclude


def clone_project_dict(project_id):
    update_project_dict = {}
    project_obj = Project.objects.get(id=project_id)
    update_project_dict['git_url'] = auth_git_url(project_id)
    TMP_DIR = '/tmp/'
    DIR_NAME = random_str(types="type5",randomlength=10)
    update_project_dict['src_dir'] = TMP_DIR + DIR_NAME
    update_project_dict['dst_dir'] = project_obj.deploy_dir.rstrip('/')
    update_project_dict['exclude'] = exclude_file(project_id)
    update_project_dict['host'] = get_project_host(project_id)
    update_project_dict['branch'] = project_obj.git_branch
    return update_project_dict


def local_clone_project(git_url,branch='master'):
    WORK_DIR = '/tmp/'
    dir_name = random_str(types='type5',randomlength=12)
    clone_dir = WORK_DIR + dir_name
    print(clone_dir,'clone_dir')
    home_dir = os.getcwd()
    git = GitApi()
    git.clone(clone_url=git_url,branch=branch,path=clone_dir)
    git.git_dir(clone_dir)
    current_tag = git.current_tag()
    current_commit_id = git.current_commit_id()
    print(current_tag)
    print(current_commit_id)
    os.chdir(home_dir)
    return current_tag,current_commit_id

def update_project_views(id,tag=None):
    project_dict = clone_project_dict(id)
    if tag:
        yaml = UPDATE_PROJECT_TAG_YAML.format(host=project_dict['host'],
                                          git_branch=project_dict['branch'],
                                          git_url=project_dict['git_url'],
                                          src_dir=project_dict['src_dir'],
                                          exclude=project_dict['exclude'],
                                          dst_dir=project_dict['dst_dir'],
                                          tag=tag,
                                          )
    else:
        yaml = UPDATE_PROJECT_YAML.format(host=project_dict['host'],
                                          git_branch=project_dict['branch'],
                                          git_url=project_dict['git_url'],
                                          src_dir=project_dict['src_dir'],
                                          exclude=project_dict['exclude'],
                                          dst_dir=project_dict['dst_dir']
                                          )
    if not project_dict['src_dir'].startswith('/tmp'):
        return False
    update_project_log = ansible_run(yaml)
    return update_project_log

def rollback_ansible_run(rollback_dict):
    yaml_modle = ROLLBAC_PROJECT_YAML.format(
        host=rollback_dict['host'],
        dst_dir=rollback_dict['dst_dir'],
        git_branch=rollback_dict['branch'] ,
        git_url=rollback_dict['git_url'],
        src_dir=rollback_dict['src_dir'],
        commit_id=rollback_dict['git_commit'],
        exclude=rollback_dict['exclude'],
    )
    if not rollback_dict['src_dir'].startswith('/tmp'):
        return False
    rollback_project_log = ansible_run(yaml_modle)
    return rollback_project_log


def get_git_information_log(id,request,text):
    project_log_dict = {}
    project_obj = Project.objects.get(id=id)
    git_url = auth_git_url(id)
    branch = project_obj.git_branch
    current_tag, current_commit_id = local_clone_project(git_url=git_url,branch=branch)
    project_log_dict['git_tag'] = current_tag.rstrip()
    project_log_dict['git_commit'] = current_commit_id.rstrip()
    project_log_dict['new_time'] = time.strftime('%Y-%m-%d %X')
    project_log_dict['operation_user'] = request.session.get('user')
    on_version_log_id = 0
    count_num = 0
    if project_obj.log:
        if project_obj.log.id:
            on_version_log_id = project_obj.log.id
        if  project_obj.log.count_num:
            count_num = project_obj.log.count_num + 1
    project_log_dict['on_version_log_id'] = on_version_log_id
    project_log_dict['count_num'] = count_num
    project_log_dict['text'] = text
    create_project_log = Log.objects.create(**project_log_dict)

    return create_project_log.id,project_log_dict





def create_project_dict(request,use='create'):
    project_dict = {}
    project_dict['title'] = request.POST.get('title')
    if use == 'create':
        project_dict['create_time'] = time.strftime('%Y-%m-%d %X')
    elif use == 'change':
        project_dict['change_time'] = time.strftime('%Y-%m-%d %X')
    project_dict['deploy_dir'] = request.POST.get('deploy_dir')
    project_dict['create_user_id'] = get_user_id(request.session['user'])
    project_dict['server_group_id'] = request.POST.get('server_group')
    project_dict['git_auth_way'] = request.POST.get('git_auth_way')
    project_dict['git_url'] = request.POST.get('git_url')
    project_dict['git_branch'] = request.POST.get('git_branch')
    project_dict['online_notice'] = request.POST.get('online_notice')
    project_dict['describe'] = request.POST.get('describe')
    git_user = request.POST.get('git_user')
    if git_user:
        project_dict['git_user'] = git_user
        project_dict['git_password'] = request.POST.get('git_passowrd')
    if request.POST.get('exclude_file'):
        project_dict['exclude_file'] = request.POST.get('exclude_file')
    if project_dict['online_notice'] == 'email':
        project_dict['email_notice_id'] = request.POST.get('email_notice')
    elif project_dict['online_notice'] == 'dingding':
        project_dict['dingding_notice'] = request.POST.get('dingding_notice')
    return project_dict

def send_project_content(project_obj,use='update'):
    title = ''
    use_title = ''
    if use == 'update':
        use_title = '更新'
        title = '项目更新'
    elif use == 'rollback':
        use_title = '回滚'
        title = '项目回滚'
    content = '''
    {use_title}项目: {name}
    注意 * (回滚时所显示的tag不准确,主要以commit_id为准)
    {use_title}tag: {tag}
    {use_title}commit_id: {commit_id}
    {use_title}操作人: {username}
    {use_title}时间: {new_time}
    '''.format(use_title=use_title,name=project_obj.title,
               tag=project_obj.log.git_tag,commit_id=project_obj.log.git_commit,
               username=project_obj.log.operation_user,new_time=project_obj.log.new_time)
    return title,content

def send_project_email(project_obj,use='update'):
    from lib.email import Mail
    print(project_obj.log,project_obj.log.git_commit)
    title,content = send_project_content(project_obj,use)
    to_list = []
    for i in project_obj.email_notice.user_set.all():
        to_list.append(i.email)
    m = Mail(to_list=to_list)
    m.send_mail(to_list,title,content)

def send_project_dingding(project_obj,use='update'):
    from lib.dingding import sendmessage
    dingding_webhook = project_obj.dingding_notice
    if not dingding_webhook :
        return None
    title,content = send_project_content(project_obj,use)
    sendmessage(content,dingding_webhook)

def send_project(project_obj,use='update'):
    if project_obj.online_notice == 'email':
        send_project_email(project_obj,use)
    elif project_obj.online_notice == 'dingding':
        send_project_dingding(project_obj,use)

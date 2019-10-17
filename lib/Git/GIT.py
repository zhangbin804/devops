import os
from lib.Cmd.cmd import *
from apps.operational.create.password import random_str




class GitApi(Shell):

    def clone(self, clone_url='', branch='master', path='/tmp/', clone_name=''):
        '''
        :param clone_url:  git仓库的地址
        :param branch:  分支名
        :param path:  指定clone的路径
        :param clone_name:  指定clone的名字（默认和仓库名一样）
        '''
        if clone_name == False:
            clone_name = clone_url.split('/')[-1].split('.')[-2]
        git_clone = 'git clone -b ' + branch + ' ' + clone_url + ' ' + path + clone_name
        return self.shell(git_clone)

    def git_dir(self,jobs_dir):
        '''
        :param dirname:  git的工作目录
        '''
        os.chdir(jobs_dir)

    def add(self, *args):
        return self.cmd('git add ' + self.str_all(args))

    def commit(self, *args):
        return self.cmd('git commit  -m  "{args}"'.format(args=self.__str_all(args)))

    def branch(self, parameter='', branch_name=''):
        '''
        :param parameter:  参数
        :param branch_name: 分支名
        '''
        return self.cmd(
            'git branch {parameter} {branch_name}'.format(parameter='-' + parameter, branch_name=branch_name))

    def checkout(self, *args):
        return self.cmd('git checkout ' + self.str_all(args))

    def tag(self, *args):
        return self.cmd('git tag ' + self.str_all(args))
    
    def current_tag(self):
        return self.cmd('git describe --tags --abbrev=0')
    
    def current_commit_id(self):
        return self.cmd('git rev-parse HEAD')

    def linux_get_origin_tag(self):
        return self.cmd("git ls-remote  --tags  -q|awk -F 'tags/'  '{print $NF}'|tail -10|tac")
    def log(self, *args):
        return self.cmd('git log ' + self.str_all(args))

    def deff(self, *args):
        return self.cmd('git diff' + self.str_all(args))

    def push(self, *args):
        return self.cmd('git push ' + self.str_all(args))

    def pull(self, *args):
        return self.cmd('git pull ' + self.str_all(args))

    def reset(self, commit_id):
        '''
        :param commit_id: 回退版本的id号
        '''
        return self.cmd('git reset --hard {commit_id}'.format(commit_id=commit_id))

    def status(self, *args):
        return self.cmd('git status ' + self.str_all(args))

    def fetch(self):
        return self.cmd('git fetch')

    def master_versions(self, num=1):
        '''
        :param num: master分支上最新提交的记录条数
        '''
        version_str = self.log('origin/master -n {num}'.format(num=num))
        master_version_list = version_str.strip().split('\n')
        master_version = master_version_list[-1].strip()
        return master_version

    def old_versions(self, num=1):
        version_str = self.log(' -n {num}'.format(num=num))
        old_version_list = version_str.strip().split('\n')
        old_version = old_version_list[-1].strip()
        return old_version

    def git_log_version_10(self, num=11):
        version_list_cmd = self.cmd('git  log --oneline -n {num}'.format(num=num))
        return version_list_cmd


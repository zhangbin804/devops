
UPDATE_PROJECT_YAML = '''
- hosts: {host}
  tasks:
  - name: with dir
    shell: mkdir -p {dst_dir} 
  - name: clone project
    shell: git clone -b {git_branch} {git_url} {src_dir}
  - name: rsync project
    shell: rsync -avz {src_dir}/*  {exclude}  {dst_dir}/
'''

UPDATE_PROJECT_TAG_YAML = '''
- hosts: {host}
  tasks:
  - name: with dir
    shell: mkdir {dst_dir} -p
  - name: clone project
    shell: git clone -b {git_branch} {git_url} {src_dir}
  - name: checkout tag 
    shell: cd {src_dir};git checkout {tag};cd -
  - name: rsync project
    shell: rsync -avz {src_dir}/*  {exclude}  {dst_dir}/
'''

ROLLBAC_PROJECT_YAML = '''
- hosts: {host}
  tasks:
  - name: with dir
    shell: mkdir {dst_dir} -p
  - name: clone project
    shell: git clone -b {git_branch} {git_url} {src_dir}
  - name: git rollback commit id
    shell: cd {src_dir} ;  git reset --hard {commit_id} ;cd -
  - name: rsync project
    shell: rsync -avz {src_dir}/*  {exclude}  {dst_dir}/
'''



ADD_SUERVER_USER_YAML = '''
- hosts: {host}
  tasks:
  - name: create ssh  user
    user: name={user} password={password} 
'''

ADD_SUERVER_USER_UID_YAML = '''
- hosts: {host}
  tasks:
  - name: create ssh  user
    user: name={user} password={password} uid={uid}
'''

ADD_SUERVER_USER_GID_YAML = '''
- hosts: {host}
  tasks:
  - name: create ssh  user
    user: name={user} password={password} gid={gid}
'''

ADD_SUERVER_USER_UGID_YAML = '''
- hosts: {host}
  tasks:
  - name: create ssh  user
    user: name={user} password={password} uid={uid} gid={gid}
'''

SUDO_YAML = '''
- hosts: {host}
  tasks:
  - name: sudo 
    lineinfile: dest=/etc/sudoers  state=present regexp=^{user} line={user}\t\tALL=(ALL)\tNOPASSWD:{sudo}
'''

REMOVE_SUDO_YAML = '''
- hosts: {host}
  tasks:
  - name: sudo 
    lineinfile: dest=/etc/sudoers  state=absent regexp=^{user} 
'''

REMOVE_SERVER_USER_YAML = '''
- hosts: {host}
  tasks:
  - name: remove ssh user
    user: name={user} state=absent  remove=yes
'''



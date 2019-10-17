import os

class Shell:
    def str_all(self,*args):
        file_all = ''
        for file in args[0]:
            file_all = file_all + file
        return file_all

    def shell(self,*args):
        os.system(self.str_all(args))
        return 1

    def cmd(self,*args):
        shell_cmd = os.popen(self.str_all(args)).read()
        return shell_cmd


def rsync(src,dst,exclude):
    cmd = Shell()
    exclude_file = '--exclude=.git '
    if src.endswith('/'):
        src = src.rstrip('/')
    if dst.endswith('/'):
        dst = src.rstrip('/')
    if exclude:
        for i in exclude:
            if i:
                i = '--exclude=%s'%(i)
                exclude_file = exclude_file + ' ' + i
    rsync_str = 'rsync -avz {src}/*   {exclude} {dst}/'.format(src=src,exclude=exclude_file,dst=dst)
    return cmd.cmd(rsync_str)





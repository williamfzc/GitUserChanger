TP_INFO = {
    'username': 'Feng Zhangchi',
    'email': '123456789@qq.com'
}

GITHUB_INFO = {
    'username': 'williamfzc',
    'email': '123456789@qq.com'
}


import os


COMMAND = 'git config --global'

def set_git(_input):
    _status = _input.lower()
    if _status == 'tp':
        os.system('{} user.name "{}"'.format(COMMAND, TP_INFO['username']))
        os.system('{} user.email "{}"'.format(COMMAND, TP_INFO['email']))
    else:
        os.system('{} user.name "{}"'.format(COMMAND, GITHUB_INFO['username']))
        os.system('{} user.email "{}"'.format(COMMAND, GITHUB_INFO['email']))

def get_git():
    print(os.popen(COMMAND+' user.name').readline().strip('\n'))
    print(os.popen(COMMAND+' user.email').readline().strip('\n'))


set_git('t')
get_git()


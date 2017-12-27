COMMAND = 'git config --global'

from git_conf import GIT_DICT, EASY_TK_URL
import os


def check_eniv(easy_tk_url):

    try:
        import easy_tk
    except:
        # check git eniv
        if os.system('git --version') != 0:
            raise (ImportError, 'Git may not be in your system path.')

        # check easy_tk
        if 'easy_tk' in os.listdir('.'):
            os.chdir('easy_tk')
            if '.git' in os.listdir('.'):
                _command = 'git pull --rebase'
            else:
                raise (ImportError, 'easy_tk doe not contains .git')
            os.system(_command)
            os.chdir('..')
        else:
            _command = 'git clone {}'.format(easy_tk_url)
            os.system(_command)


def set_git(user_choice):
    git_info = GIT_DICT[user_choice]
    os.system('{} user.name "{}"'.format(COMMAND, git_info['username']))
    os.system('{} user.email "{}"'.format(COMMAND, git_info['email']))


def get_cur_git(_result_dict):
    _username = os.popen(COMMAND+' user.name').readline().strip('\n')
    _password = os.popen(COMMAND+' user.email').readline().strip('\n')
    _old_str = 'Old git user is: \n{}\n{} \n\n'.format(_username, _password)
    _git_info = GIT_DICT[_result_dict[0][1]]
    _new_str = 'New git user is: \n{}\n{} \n'.format(
        _git_info['username'], _git_info['email'])
    return _old_str + _new_str


if __name__ == '__main__':

    check_eniv(EASY_TK_URL)

    try:
        from easy_tk.easy_tk.window_builder import WindowBuilder
    except ImportError:
        raise (ImportError, 'easy_tk meet some error. Try to download manually.')

    temp_dict = {
        'info': 'CHOOSE YOUR GIT USER',
        'widgets': {
            'git users list': {
                'type': 'choicelist',
                'level': 'must',
                'content': list(GIT_DICT.keys()),
            }
        },
        'after': get_cur_git
    }

    result = WindowBuilder(temp_dict).get()[0][1]
    set_git(result)



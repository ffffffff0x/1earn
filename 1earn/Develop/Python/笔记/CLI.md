# CLI

---

## 获取当前时间

```py
import datetime

def get_now():
    return datetime.datetime.now().strftime('%Y-%m-%d %X')
```

## 把 n 秒转为合适的时间单位

```py
def timer_unit(s):
    '''将 second 秒转为适合的单位
    '''

    if s <= 1:
        return f'{round(s, 1)}s'

    num, unit = [
        (i, u) for i, u in ((s / 60**i, u) for i, u in enumerate('smhd')) if i >= 1
    ][-1]

    return f'{round(num, 1)}{unit}'
```

## 上色

```py
from colorama import Fore, Style

def put_color(string, color, bold=False):
    '''
    give me some color to see :P
    '''

    if color == 'gray':
        COLOR = Style.DIM + Fore.WHITE
    else:
        COLOR = getattr(Fore, color.upper(), "WHITE")

    return f'{Style.BRIGHT if bold else ""}{COLOR}{str(string)}{Style.RESET_ALL}'
```

## 自定义 log

```py
import sys

class Logger:
    def __init__(self, filename, stdout=False, verb=2):
        self.stdout = stdout
        self.verbose = verb
        self.filename = filename

    def _log(self, log_content):
        if self.stdout:
            sys.stderr.write('\r'+log_content)
        else:
            with open(self.filename, 'a') as fp:
                fp.write(log_content)

    def log(self, event, level='INFO', return_str=False):
        '''记录日志

        @event: 具体事件
        @filename: 日志文件
        @level: 事件等级
        '''

        levels = {
            'DEBU': 'gray',
            'INFO': 'white',
            'WARN': 'yellow',
            'ERRO': 'red'
        }
        color = levels.get(level, 'white')

        clevel = put_color(level, color, True)
        log_time = put_color(get_now(), 'cyan', True)
        log_filename = put_color(self.filename.split('/')[-1], 'gray', True)

        cevent = put_color(event, color) if color != 'white' else event
        log_content = f'[{log_time}] [{clevel}] {cevent}'
        if self.verbose == 3:
            log_content = f'[{log_time}] [{clevel}] [{log_filename}] {cevent}'

        if not event.endswith('\n'):  # 保证结尾换行
            log_content += '\n'

        if self.verbose == 0:
            pass
        elif self.verbose == 1 and level == 'ERRO':
            self._log(log_content)
        elif self.verbose == 2 and level != 'DEBU':
            self._log(log_content)
        elif self.verbose == 3:
            self._log(log_content)

        if return_str:
            return '\r'+log_content.strip()
```

## 以 root 权限重启进程

```py
euid = os.geteuid()
if euid != 0:
    args = ['sudo', sys.executable] + sys.argv + [os.environ]  # type: ignore

    if os.system('sudo -n whoami 1>/dev/null 2>/dev/null') != 0:
        print('需要 root 权限，请输入 root 密码')

    os.execlpe('sudo', *args)
```

## 转为后台运行

```py
process = subprocess.Popen(
    f''' bash <<< '{sys.executable} {" ".join(sys.argv)} >> {Path.runtime_error_logfile} 2>&1 &'$'\\n''echo $!' ''',
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True,
)

try:
    pid = process.stdout.read().decode('utf-8').strip()
    if not pid.isdigit():
        raise RuntimeError(process.stderr.read().decode('utf-8'))

except KeyboardInterrupt:
    print(log(f'User canceled', 'WARN', return_str=True))

except subprocess.TimeoutExpired:
    print(log(f'后台运行失败: 命令行有误', 'ERRO', return_str=True))

except Exception as e:
    print(log(f'后台运行失败: {e}', 'ERRO', return_str=True))
    sys.exit(1)
else:
    print(log(f'后台运行中, pid: {pid}', 'INFO', return_str=True))

sys.exit(0)
```

用 subprocess.Popen 开个新的进程之后，自己退出，这样新的进程就是孤儿进程了，ppid 变成 1，远程的话断开 ssh 也没事。

---

## Source & Reference

- [Python 编写 CLI 的技巧分享](https://www.tr0y.wang/2020/11/24/Python-CLI-Trick/)

# Requests 小记

- [Requests: 让 HTTP 服务人类¶](https://2.python-requests.org//zh_CN/latest/)

`Requests 支持 Python 2.6—2.7以及3.3—3.7，而且能在 PyPy 下完美运行。`

```python
>>> import requests
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200

>>> r.headers['content-type']
'application/json; charset=utf8'

>>> r.encoding
'utf-8'

>>> r.text
u'{"type":"User"...'

>>> r.json()
{u'private_gists': 419, u'total_private_repos': 77, ...}
```











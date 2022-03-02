from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name

@app.route('/test')
def test_url_for:
    # 下面是一些调试用例(请在命令行窗口查看输出的URL)
    print(url_for('hello')) #输出:/
    #注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page',name='greyli'))

    print(url_for('user_page',name='peter'))

    print(url_for('test_url_for'))

    print(url_for('test_url_for',num=2))
    return 'Test page'
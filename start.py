#! python
# -*- coding: utf-8 -*-


from flask import Flask, request, redirect
# from urllib import request as frequest
# from multiprocessing import Process
import os

app = Flask(__name__)


# def down(url):
#     with frequest.urlopen(url) as f:
#         with open('123', 'wb') as wf:
#             wf.write(f.read())


def runDown(url):
    # print(123)
    # p = Process(target=down, args=(url,))
    # p.start()
    print('\n\n\n-----------------------------------')
    os.system('wget -P ../down/ ' + url + ' > ./log/down.log')


@app.route('/wg', methods=['POST'])
def downUrl():
    if request.method == 'POST':
        url = request.form.get('url')
        runDown(url)
    return 'Hello World! ' + url + '\n'


@app.route('/js')
def js():
    return redirect('http://wget.vlper.top/log/down.js')


@app.route('/')
def hello_world():
    return 'Hello World! \n'


def main_():
    app.run(port=8080)


if __name__ == '__main__':
    main_()

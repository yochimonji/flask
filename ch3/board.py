from flask import Flask, request, redirect
import os
app = Flask(__name__)

DATAFILE = './board-data.txt'

@app.route('/')
def index():
    msg = 'まだ書き込みはありません'
    
    if os.path.exists(DATAFILE):
        with open(DATAFILE, 'rt') as f:
            msg = f.read()

    return """
        <html><body>
            <h1>メッセージボード</h1>
            <div style="background-color:yellow; padding:3em;">
                {}
            </div>
            <h3>ボードの内容を更新</h3>
            <form action="/write" method="POST">
                <textarea name="msg" rows="6" cols="60"></textarea>
                <input type="submit" value="書込">
            </form>
        </body></html>
    """.format(msg)

@app.route('/write', methods=['POST'])
def write():
    if 'msg' in request.form:
        msg = str(request.form['msg'])
        with open(DATAFILE, 'wt') as f:
            f.write(msg)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, session, redirect
app = Flask(__name__)
app.secret_key = '9KStWezC'

@app.route('/')
def index():
    return """
        <html><body>
            <h1>ユーサー名を入力</h1>
            <form action="/setname" method="GET">
                名前：<input type="text" name="username">
                <input type="submit" value="開始">
            </form>
        </body></html>
    """

@app.route('/setname')
def setname():
    name = request.args.get('username')
    if not name:
        return redirect('/')
    session['name'] = name
    return redirect('/morning')

def getLinks():
    return """
        <ul>
            <li><a href="/morning">朝の挨拶</a></li>
            <li><a href="/hello">昼の挨拶</a></li>
            <li><a href="/night">夜の挨拶</a></li>
        </ul>
    """

@app.route('/morning')
def morning():
    if not ('name' in session):
        return redirect('/')
    return '<h1>{}さん、おはようございます！</h1>{}'.format(session['name'], getLinks())

@app.route('/hello')
def hello():
    if not ('name' in session):
        return redirect('/')
    return '<h1>{}さん、こんにちは！</h1>{}'.format(session['name'], getLinks())


@app.route('/night')
def night():
    if not ('name' in session):
        return redirect('/')
    return '<h1>{}さん、こんばんは！</h1>{}'.format(session['name'], getLinks())

if __name__ == '__main__':
    app.run(debug=True)
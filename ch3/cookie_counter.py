from flask import Flask, make_response, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    cnt_s = request.cookies.get('cnt')
    if cnt_s is None:
        cnt = 0
    else:
        cnt = int(cnt_s)
    cnt += 1
    response = make_response("""
        <h1>訪問回数： {}回</h1>
    """.format(cnt))
    # Cookieに保存
    max_age = 60 * 60 * 24 * 90
    expires = int(datetime.now().timestamp()) + max_age
    response.set_cookie('cnt', value=str(cnt),
            max_age=max_age,
            expires=expires)
    return response

if __name__ == '__main__':
    app.run(debug=True)
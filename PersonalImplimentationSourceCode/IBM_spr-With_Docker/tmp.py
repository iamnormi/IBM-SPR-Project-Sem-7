from flask import Flask
app=Flask(__name__)

@app.route('/flask')
def helloflask():
    return 'Hello Flask'

@app.route('/python')
def hellopython():
    return 'Hello python'

if __name__== '__main__':
    app.run(debug = True)


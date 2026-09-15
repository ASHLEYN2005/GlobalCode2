from flask import Flask, render_template , request

app = Flask(__name__)

@app.route('/')
def home():
    return {'okay': 'Hello, World!',
         'message': 'This is a simple Flask application.'}


@app.route('/whereami')
def where_am_i():
    return ['Ghana!']
@app.route('/card')
def card():
    return '<h1>Hello!</h1><p> <style My name is Ashleyn</p>'

@app.route('/color')
def color():
    return '<h1>Hello!</h1><p>My name is Ashleyn ,my favourate color is Blue</p>'


@app.route('/greet/<name>')
def greet(name):
    return render_template('main.html', user_name=name, names = ['ama' ,'kofi ', 'john'] ,is_admin=False )

# @app.route('/dan/<name>')
# def you(name):
#     return f'hello, {name} you are in Ghana!'

@app.route('/form', methods =['GET', 'POST'] )
def form():
    if request.method == 'GET':
        return "this is a get request"
    elif request.method == 'POST':
        return "this is a post request"
    else:
        return "this is not allowed"



if __name__ == '__main__':
    app.run(debug=True)

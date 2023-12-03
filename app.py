from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def home():
    return "You are in Home Page"
# Use of <converter: variable name> in the 
# route() decorator.
@app.route('/allow/<int:Number>')
def allow(Number):
    if Number < 25:
        return f'Hi! You Are Allowed with {Number}'
    else:
       return f'Hello! You are not allowed with {Number}'
if __name__ == '__main__':
    app.run()
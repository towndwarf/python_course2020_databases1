from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return """
     <html><body>
         <h2>Welcome to the Greeter</h2>
         <form action="/greet">
             What's your name? <input type='text' name='username'><br>
             What's your favorite food? <input type='text' name='favfood'><br>
             <input type='submit' value='Continue'>
         </form>
     </body></html>
     """


@app.route('/greet')
def greet():
    username = request.args.get('username', 'World')
    favfood = request.args['favfood']
    if favfood == '':
        msg = 'You did not tell me your favorite food.'
    else:
        msg = 'I like ' + favfood + ', too.'

    return f"""
     <html><body>
         <h2>Hello, {username}!</h2>
         {msg}
     </body></html>
     """


# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)

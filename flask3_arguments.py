from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args['name']
    stuff = request.args['other']

    return f"""
        <html><body>
            <h1>Hello, {name}!</h1>
            The time is {str(datetime.now())}. {stuff}
        </body></html>
        """


# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)

# ?name=python+flask&other=Submit
# http://localhost:5000/?name=Frank
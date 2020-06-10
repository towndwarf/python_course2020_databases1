from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def whatever():
    return """
        <html>
           <body>
            <h1>Hello, world!</h1>
            Click <a href="/time">here</a> for the time.
           </body>
        </html>
        """


@app.route('/time')
def whatever2():
    return f"""
        <html><body>
            The time is {str(datetime.now())}.
        </body></html>
        """


# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)

from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello():
 return f"""<html><body>
     <h1>Hello, world!</h1>
     The time is {str(datetime.now())}.</body></html>"""

# Launch the Flask dev server
app.run(host="localhost", debug=True)
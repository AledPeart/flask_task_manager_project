import os
from flask import Flask
if os.path.exists("env.py"):  #ensures that when we push to Heroku env is only imported if os can find an existing path 
    import env 


app = Flask(__name__) #creates an instance of Flask stored in the variable app


@app.route("/")


def hello():
    return "Hello world....again!"

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  #needs to be changed to false upon deplyment/submission
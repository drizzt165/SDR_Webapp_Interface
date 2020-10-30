from flask import Flask, request, render_template, redirect, url_for
#import zmq

#ctx = zmq.Context()
#sock = ctx.socket(zmq.PUB)
#sock.bind("tcp://*:9101")
app = Flask(__name__)

pastMsgs = ['Hello! Are you out there?'] #default msg for chat log

@app.route('/')
def home():
    return render_template('my-form.html',chatLog = ('<br/>'.join(pastMsgs)))

@app.route('/', methods=['POST'])
def my_form_post(prev_msg = None):
    name = request.form['name']
    message = request.form['message']
    location = request.form['location']

    allInfo = [name,message,location]
    stringInfo = ' | '.join(allInfo)
    print(allInfo)

    #sock.send_string(stringInfo)
    pastMsgs.append(message)
    return redirect(url_for("home",prev_msg = message))

if __name__ == "__main__":
    app.run()
    #sock.close()
    #ctx.term()

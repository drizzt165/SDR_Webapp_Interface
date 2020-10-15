from flask import Flask, request, render_template, redirect, url_for
#import zmq

#ctx = zmq.Context()
#sock = ctx.socket(zmq.PUB)
#sock.bind("tcp://*:9101")
app = Flask(__name__)

pastMsgs = ['Hello! Are you out there?']

@app.route('/')
def home():
    history = []
    return render_template('my-form.html',chatLog = ('<br/>'.join(pastMsgs)))

@app.route('/', methods=['POST'])
def my_form_post(prev_msg = None):
    text = request.form['text']
    processed_text = text #Change text if we desire
    #sock.send_string(processed_text)
    pastMsgs.append(processed_text)
    return redirect(url_for("home",prev_msg = processed_text))

if __name__ == "__main__":
    app.run(host = '0.0.0.0')
    #sock.close()
    #ctx.term()

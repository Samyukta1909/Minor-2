from flask import Flask,render_template,request,jsonify
# from subdomains import subdomain_thread_stop_event
from sensitiveFiles import hiddenFiles
from subdomains import subdomain
from endpoints import endpoint
from domain import WHOis
from records import record
import json
import json,threading
from threading import active_count
from flask_socketio import SocketIO
from news import headlines
from techstack import techStackFunc
import multiprocessing,time
from report import createreport
from flask import send_file
import requests
from test import testfunc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
stop_thread = threading.Event()


@app.route('/', methods=["GET","POST"])
def index():


    global hidFiles, subdoms, endpoints

    if request.form:

        target = request.form.get("urlvalue")
        print("Target: ",target)  

        # domainFile =WHOis(target)
        # recordFile,recordFile1=record(target)

        techStackFunc(target)

        # threading.Thread(target=headlines).start()
        # threading.Thread(target=hiddenFiles,args=(target,)).start()
        # threading.Thread(target=endpoint,args=(target,)).start()
        # threading.Thread(target=subdomain,args=(target,)).start()
        # testfunc()


        # return render_template('index.html', WHOis=domainFile,record=recordFile,name=recordFile1)
        return render_template('index.html')
        # return render_template('index.html',WHOis=domainFile,record=recordFile,name=recordFile1)

    else:
        threading.Thread(target=headlines).start()
        return render_template('index.html')
        # return render_template('index.html',Headlines=nhead)

@app.route('/contact',methods=["GET"])
def contact():
   return render_template('contact.html')

@app.route('/About',methods=["GET"])
def about():
   return render_template('about.html')
   
@socketio.on('message')
def establishConnect(msg):
    print("Connection: "+msg)
    # send(msg)

@app.route('/senstiveUrls',methods=['GET','POST'])
def senstiveUrls():
    # data = json.loads(request.data)['urls']
    data = json.loads(request.data)
    print(data)
    socketio.emit('sensitiveUrls',{'urls':data})
    return jsonify(result={"status": 200})

@app.route('/endpointUrls',methods=['GET','POST'])
def endpointUrls():
    data = json.loads(request.data)['urls']
    # print("DATA: ",data)
    socketio.emit('endpointUrls',{'urls':data})
    return jsonify(result={"status": 200})

@app.route('/subdomainUrls',methods=['GET','POST'])
def subdomainUrls():
     data = json.loads(request.data)['urls']
    #  print("Subdomain DATA: ",data)
     socketio.emit('subdomainUrls',{'urls':data})
     return jsonify(result={"status": 200})

@app.route('/news',methods=['GET','POST'])
def news():
    data = json.loads(request.data)['news']
    # print("News Data: ",data)
    socketio.emit('news',{'news':data})
    return jsonify(result={"status": 200})

@app.route('/Report',methods=['GET','POST'])
def report():
    createreport()
    path = "myreport/EagleEyeReport.pdf"
    return send_file(path, as_attachment=True)
   

@app.route('/techstackdata',methods=['GET','POST'])
def helpfunc():
    data = json.loads(request.data)
    print("Techstack Data: ",data)
    socketio.emit('techstackdata',{'techstack':data})
    return jsonify(result={"status": 200})



if __name__=="__main__":
    # app.run(debug=True)
    socketio.run(app,debug=True)

from flask import Flask,render_template,request,jsonify
from subdomains import subdomain_thread_stop_event
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
import multiprocessing,time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
stop_thread = threading.Event()

@app.route('/', methods=["GET","POST"])
def index():


    global hidFiles, subdoms, endpoints

    if request.form:

        target = request.form.get("urlvalue")
        # TEMPLATES_AUTO_RELOAD = True
        print("Target: ",target)

        subdomainThread = threading.Thread(target=subdomain,args=(target,))
        print(subdomainThread.is_alive())
        subdomain_thread_stop_event.set()
        time.sleep(5)
        subdomain_thread_stop_event.clear()
        print(subdomainThread.is_alive())

        subdomainThread.start()
        print(subdomainThread.is_alive())


        # domainFile =WHOis(target)
        # recordFile,recordFile1=record(target)

        # subdomainsProc = multiprocessing.Process(target=subdomain, args=(target,))
        # sensitiveFilesProc = multiprocessing.Process(target=hiddenFiles, args=(target,))
        # endPointsProc = multiprocessing.Process(target=endpoint, args=(target,))
        # newsProc = multiprocessing.Process(target=headlines)


        # print("Subdomain process status: ",subdomainsProc.is_alive())
        # if sensitiveFilesProc.is_alive() or endPointsProc.is_alive() or subdomainsProc.is_alive() or newsProc.is_alive():
        #     #     sensitiveFilesProc.terminate()   
        # #     endPointsProc.terminate()   
        #     subdomainsProc.kill()
        # #     newsProc.terminate()
        #     time.sleep(2)

        # print("Subdomain process status: ",subdomainsProc.is_alive())

        # sensitiveFilesProc.start()
        # endPointsProc.start()
        # subdomainsProc.start()
        # print("Subdomain process status: ",subdomainsProc.is_alive())
        # newsProc.start()

        # threading.Thread(target=hiddenFiles,args=(target,)).start()
        # threading.Thread(target=endpoint,args=(target,)).start()
        # threading.Thread(target=subdomain,args=(target,)).start()
        # threading.Thread(target=headlines).start()

        # return render_template('index.html', WHOis=domainFile,record=recordFile,name=recordFile1)
        return render_template('index.html')
        # return render_template('index.html',WHOis=domainFile,record=recordFile,name=recordFile1)

    else:
        threading.Thread(target=headlines).start()
        return render_template('index.html')
        # return render_template('index.html',Headlines=nhead)

@app.route('/Contact', methods=["GET","POST"])
def contact():
   return render_template('contact.html')
   
@socketio.on('message')
def establishConnect(msg):
    print("Connection: "+msg)
    # send(msg)

@app.route('/senstiveUrls',methods=['GET','POST'])
def senstiveUrls():
    data = json.loads(request.data)['urls']
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



if __name__=="__main__":
    # app.run(debug=True)
    socketio.run(app,debug=True)
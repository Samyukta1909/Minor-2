from flask import Flask,render_template,request,jsonify
from sensitiveFiles import hiddenFiles
from domain import WHOis
from records import record
import json
import json,threading
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/', methods=["GET","POST"])
def index():
    if request.form:
        # print(request.form.get("urlvalue"))
        target = request.form.get("urlvalue")
        
        domainFile =WHOis(target)
        recordFile,recordFile1=record(target)
        return render_template('index.html',WHOis=domainFile,record=recordFile,name=recordFile1)
    
        # hidFiles = hiddenFiles(target)
        # return render_template('index.html',hiddenFiles=hidFiles)

        print(target)
        # hidFiles = hiddenFiles(target)
        threading.Thread(target=hiddenFiles,args=(target,)).start()
        # return render_template('index.html',hiddenFiles=hidFiles)
        return render_template('index.html')
    else:
        return render_template('index.html')
    
    
    
        

@socketio.on('message')
def establishConnect(msg):
    print("Connection: "+msg)
    # send(msg)

@app.route('/senstiveUrls',methods=['GET','POST'])
def senstiveUrls():
    data = json.loads(request.data)['urls']
    socketio.emit('sensitiveUrls',{'urls':data})
    return jsonify(result={"status": 200})



if __name__=="__main__":
    # app.run(debug=True)
    socketio.run(app)
from flask import Flask,render_template,request
from sensitiveFiles import hiddenFiles
from subdomains import subdomain
from endpoints import endpoint
import json
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    global hidFiles, subdoms, endpoints
    if request.form:
        # print(request.form.get("urlvalue"))
        target = request.form.get("urlvalue")
        hidFiles = hiddenFiles(target)
        subdoms= subdomain(target)
        endpoints=endpoint(target)
        return render_template('index.html',hiddenFiles=hidFiles,subdomain=subdoms, endpoint=endpoints)
    else:
        return render_template('index.html')



if __name__=="__main__":
    app.run(debug=True)
from flask import Flask,render_template,request
from sensitiveFiles import hiddenFiles
import json
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    if request.form:
        # print(request.form.get("urlvalue"))
        target = request.form.get("urlvalue")
        print(target)
        hidFiles = hiddenFiles(target)
        return render_template('index.html',hiddenFiles=hidFiles)
    else:
        return render_template('index.html')



if __name__=="__main__":
    app.run(debug=True)
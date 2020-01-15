#importing libraries
from flask import Flask ,render_template,url_for,request,flash,redirect
from werkzeug.utils import secure_filename
from PIL import Image
import pytesseract
import os ,shutil
app = Flask(__name__)
app.secret_key="."
__author__="https://github.com/czyum"
app_path = os.path.dirname(os.path.abspath(__file__))
#Define functions for processing post requests on home route
@app.route("/",methods=["POST","GET"])  
#
def index():
    if request.method=="POST":
        route = os.path.join(app_path, 'static\images\\upload\\')
        #removing the previously uploaded images,comment it if those images are required
        shutil.rmtree(route)
        #print(route)

        if not os.path.isdir(route):
            os.mkdir(route)

        file=request.files["pic"]
       
        name = file.filename
       # print(name)
        destination = "".join([route, name])
        print(destination)
        file.save(destination)
        im=Image.open(file)
        pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        text=pytesseract.image_to_string(im)
        print(text)
        print(name)
        return render_template("output.html",name=str(name),text=text)

    return render_template("index.html")


  
if __name__=="__main__":
    app.run(debug=True) 
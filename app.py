from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import subprocess
import os
import magic

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload'
app.config['MAX_CONTENT_PATH'] = 2048
ALLOWED_EXTENSIONS = {'zip'}

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def check_format(filename):
   if( "zip" in magic.from_file(filename, mime=True)):
      return True
   else:
      os.remove(filename)
   return False

def get_metadata(filename):
   proc = subprocess.Popen(["./exiftool-12.23/exiftool", filename], stdout=subprocess.PIPE)
   (out, err) = proc.communicate()
   os.remove(filename)
   return out

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_zip():
   if request.method == 'POST':
      # check if the post request has the file part
      if 'file' not in request.files:
         print('No file part')
         return upload_file()
      file = request.files['file']
      if file.filename == '':
         print('No selected file')
         return redirect(request.url)
      if file and allowed_file(file.filename):
         filename = secure_filename(file.filename)
         path_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
         file.save(path_file)
         if(check_format(path_file) == False):
            return "Only ZIP format"
         return get_metadata(path_file)
         
      return "Only ZIP format"
   else:
      return "Not support GET method"
		
if __name__ == '__main__':
   app.run(debug = True)


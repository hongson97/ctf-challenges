from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import subprocess
import os
import magic

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload'
app.config['MAX_CONTENT_PATH'] = 2048
ALLOWED_EXTENSIONS = {'zip'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def check_format(filename):
   if( "zip" in magic.from_file(filename, mime=True)):
      return True
   else:
      os.remove(filename)
   return False

def format_stdout(out):
    str_output = str(out, 'UTF-8')
    arr_output = str_output.split("\n")
    return arr_output

def get_metadata(filename):
    proc = subprocess.Popen(["./exiftool-12.23/exiftool", filename], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
   # os.remove(filename)
    str_out = format_stdout(out)
    return str_out
    
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_zip():
   if request.method == 'POST':
      # check if the post request has the file part
      if 'file' not in request.files:
         data_error ="Error: Input zip file."
         render_template('upload.html',data = data_error)
      file = request.files['file']
      if file.filename == '':
         data_error = "Error: No selected file."
         render_template('upload.html',data = data_error)
         
      if file and allowed_file(file.filename):
         filename = secure_filename(file.filename)
         path_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
         file.save(path_file)
         
         if(os.path.exists(path_file) == True or check_format(path_file) == True):
            data_return = get_metadata(path_file)
            return render_template('upload.html', data=data_return)
         return render_template('upload.html',data = ["Error: File is invalid."])
                             
      return render_template('upload.html',data = ["Error: File is not supported."]);
   else:
      return render_template('upload.html')
		
if __name__ == '__main__':
   app.run(debug = True)

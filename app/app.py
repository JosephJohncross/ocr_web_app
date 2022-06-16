from flask import Flask, render_template, request
from ocr import extract
import config
import os 

app = Flask(__name__)
app.config["UPLOAD_PATH"] = config.UPLOAD_PATH

@app.route('/', methods=['GET','POST'])
def index():
      if request.method == 'GET':
            return render_template('index.html')
      elif request.method == 'POST':
            upload_data = request.files['upload']

            save_name = os.path.join(app.config["UPLOAD_PATH"], upload_data.filename)
            upload_data.save(save_name)

            extract_txt = extract(save_name)
            return render_template('extracted.html',extract_from_image=extract_txt)
      else:
            print('CRUD Operation not permitted')

if __name__ == '__main__':
      app.run(debug=True)
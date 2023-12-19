from flask import Flask, render_template, send_file
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import time
from transform_data import transform_data


# Creamos la aplicación
app = Flask(__name__)
# Tenemos que crear una llave para pder aceptar los forms
app.config['SECRET_KEY'] = 'supersecretkey'
# Le estamos diciendo a dónde va a subir los archivos
app.config['UPLOAD_FOLDER'] = 'static/files'

# Vamos a crear una clase para subir los archivos
class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

# Esto básicamente le dice que cuando el usuario elija algunas de esas direcciones
# Lo vamos a enviar a index.html
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    # Tenemos que agregar el campo para que se suba el archivo
    form = UploadFileForm()
    if form.validate_on_submit():
        global filename
        # First grab the file
        file = form.file.data 
        # Then save the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        filename = file.filename
        transform_data(filename)
        return waiting_and_processing()
    return render_template('index.html', form=form)

@app.route('/waiting_page')
def waiting_and_processing():
    return render_template('downloads.html')

@app.route('/downloads')
def downloads():
    return render_template('downloads.html')


@app.route('/return-file')
def return_file():
   name = filename.split('.')[0]
   return send_file(f'./static/transformed_files/{name}_transformed.csv')

if __name__ == '__main__':
    app.run()
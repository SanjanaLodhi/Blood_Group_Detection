from flask import Flask, render_template, request, redirect, session
import pymysql
import os
import uuid
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from flask import send_from_directory
# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'Vandana'

app.config['UPLOAD_FOLDER'] = 'uploads'

model = load_model('blood_group_model.h5')
# Connect to MySQL
conn = pymysql.connect(host='localhost', user='root', password='', database='blood_group')
cursor = conn.cursor()

class_labels = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

def model_predict(img_path):
    # Match image size used during training
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    print("Raw Predictions:", predictions)

    predicted_index = np.argmax(predictions)
    predicted_label = class_labels[predicted_index]
    print("Predicted Class:", predicted_label)

    return predicted_label

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor.execute("SELECT id, username FROM users WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()

        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect('/index')
        else:
            return "Invalid email or password"

    return render_template('login.html')


# Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        try:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                           (username, email, password))
            conn.commit()
            return redirect('/login')
        except:
            return "Error: Username or Email already exists."

    return render_template('signup.html')



@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file part"
        file = request.files['image']
        if file.filename == '':
            return "No selected file"
        if file:
            # Save with unique filename to prevent cache issues
            filename = f"{uuid.uuid4().hex}_{file.filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            result = model_predict(filepath)
            return render_template('index.html', prediction=result, image=filename)

    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)  # Enable Debug Mode

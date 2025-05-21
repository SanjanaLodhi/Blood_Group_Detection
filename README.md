# Blood Group Detection System


🔧 Features
Upload image of a blood sample

Predict blood group using a pre-trained CNN model

Clean user interface with Flask backend

Modular code (training, prediction, web app)

🧠 Model & Dataset
⚠️ Due to GitHub’s file size limitations, the pre-trained model (blood_group_model.h5) and the dataset used for training are not included in this repository.

Options:
Download Pre-trained Model & Dataset:

[Google Drive link to .h5 model file] (Insert link here)

[Google Drive link to dataset] (Insert link here)

Train the Model Yourself:

Use the provided train_model.py script (included in this repo).

Ensure your dataset is in the correct folder structure:
dataset/
├── A+/
├── A-/
├── B+/
├── B-/
├── AB+/
├── AB-/
├── O+/
└── O-/


🛠️ Installation
Clone the repo
git clone https://github.com/yourusername/blood_group.git
cd blood_group
Install dependencies
pip install -r requirements.txt
Run the application




python app.py
📂 Folder Structure

blood_group/
├── static/              # CSS, JS, images
├── templates/           # HTML templates
├── dataset/             # Not uploaded due to size
├── blood_group_model.h5 # Not uploaded due to size
├── app.py               # Flask application
├── train_model.py       # Script to train your own model
├── requirements.txt     # Python dependencies
└── README.md
👨‍💻 Tech Stack
Python

Flask

TensorFlow/Keras

OpenCV

NumPy & Pandas

📌 Notes
Model file must be placed in the project root directory as blood_group_model.h5 before running the Flask app.

If you face issues with large file size, consider using Git Large File Storage (LFS).


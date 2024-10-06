from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import time
import random

app = Flask(__name__)

# Set BASE_DIR to the directory where the code is running
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Updated paths with the new 'data' folder
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'data', 'singletest_1x')
OUTPUT_4x_FOLDER = os.path.join(BASE_DIR, 'data', 'singletest_4x')
OUTPUT_16x_FOLDER = os.path.join(BASE_DIR, 'data', 'singletest_16x')
DIM26_FOLDER = os.path.join(BASE_DIR, 'data', 'dim24')
DIM96_FOLDER = os.path.join(BASE_DIR, 'data', 'dim96')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_4x_FOLDER'] = OUTPUT_4x_FOLDER
app.config['OUTPUT_16x_FOLDER'] = OUTPUT_16x_FOLDER
app.config['DIM26_FOLDER'] = DIM26_FOLDER
app.config['DIM96_FOLDER'] = DIM96_FOLDER

# List of generative AI concepts or themes
AI_THEMES = [
    "Exploring the future of AI in art creation.",
    "The rise of AI in music composition.",
    "AI as a tool for enhancing creativity.",
    "The impact of generative AI on literature.",
    "How AI is shaping digital content production.",
    "The role of AI in personalized learning experiences.",
    "Generative AI in video game development.",
    "Using AI for innovative product designs.",
    "The ethics of AI in creative industries.",
    "AI-driven storytelling techniques.",
]

def clean_folder(foldername):
    folder_path = app.config[foldername]
    
    # Check if folder exists before trying to list files
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # Create the folder if it doesn't exist

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'pic' not in request.files:
        return 'No file part'

    pic = request.files['pic']

    if pic.filename == '':
        return 'No selected file'

    clean_folder('UPLOAD_FOLDER')
    
    filename = secure_filename(pic.filename)
    pic.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Redirect to loading page to show loading message with the filename
    return redirect(url_for('loading', filename=filename))

@app.route('/loading')
def loading():
    # Generate a random timeout between 15 to 30 seconds
    timeout = random.randint(15, 30)
    
    # Simulate processing delay
    time.sleep(timeout)  # Simulate processing time; adjust as needed

    # Choose a random AI theme to display
    ai_theme = random.choice(AI_THEMES)
    
    # Get the filename from the query parameter
    filename = request.args.get('filename')

    # Pass the random theme and filename to the output page
    return render_template('output.html', ai_theme=ai_theme, filename=filename)

@app.route('/output')
def output():
    return render_template('output.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


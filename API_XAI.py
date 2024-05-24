from flask import Flask, send_file
import os
import subprocess

app = Flask(__name__)

# Define the folder containing XAI result images
xai_result_folder = 'XAI_Result/'

# Function to run XAI.py script
def run_xai_script():
    subprocess.run(['python', 'XAI.py'])

@app.route('/')
def index():
    # Run the XAI.py script to generate images
    run_xai_script()

    # Fetch the list of image files in XAI_Result folder
    image_files = sorted(os.listdir(xai_result_folder))

    # Create HTML content with links to individual image pages
    html_content = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>XAI Results</title></head><body><h1>XAI Results</h1>'
    for image_file in image_files:
        html_content += f'<a href="/image/{image_file}">{image_file}</a><br>'
    html_content += '</body></html>'

    return html_content

@app.route('/image/<image_file_name>')
def image_page(image_file_name):
    # Get the path to the requested image file
    image_path = os.path.join(xai_result_folder, image_file_name)

    # Check if the file exists
    if os.path.exists(image_path):
        # Serve the image file
        return send_file(image_path, mimetype='image/png')  # Adjust mimetype as needed for your image type
    else:
        return 'Image not found'

if __name__ == '__main__':
    app.run(debug=True)

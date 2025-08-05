from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

FILE_NAME = 'activities.csv'

@app.route('/')
def index():
    # Create CSV file with headers if not exists
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Roll', 'Activity', 'Activity Type', 'Level'])

    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    roll = request.form['roll']
    activity = request.form['activity']
    activity_type = request.form['activity_type']
    level = request.form['level']

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, roll, activity, activity_type, level])

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

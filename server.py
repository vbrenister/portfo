from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


def write_to_csv(data):
    with open("database.csv", mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page>')
def work(page):
    return render_template(f'{page}.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.form.to_dict()
    write_to_csv(data)
    return redirect("thankyou")

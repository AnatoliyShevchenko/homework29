from flask import (Flask, render_template, request)
from persons import persons


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', persons=persons)

@app.route('/add', methods=['POST'])
def add():
    _added = {}
    key_name = ['name']
    key_ages = ['ages']
    key_info = ['info']
    name = request.form['name']
    age = request.form['age']
    about = request.form['about']
    name_value = list(name.split('/'))
    age_value = list(age.split('/'))
    info_value = list(about.split('/'))
    _added.update(list(zip(key_name, name_value)))
    _added.update(list(zip(key_ages, age_value)))
    _added.update(list(zip(key_info, info_value)))
    persons.append(_added)
    return render_template('search.html', name=name, age=age, about=about)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
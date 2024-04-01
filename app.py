from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bio.html', name='John Doe', birth_date='01/01/1990', education='Your Education')

@app.route('/project1')
def projects():
    projects_data = [
        {
            'title': 'практична 1',
            'technologies': 'Python',
            'repo_link': 'https://github.com/LabeUri/1lab_pyton.git'
        },
    ]
    return render_template('project1.html', projects=projects_data)

@app.route('/project2')
def projects2():
    projects_data = [
        {
            'title': 'практична 2',
            'technologies': 'Python',
            'repo_link': 'https://github.com/LabeUri/2pr_python.git'
        },
    ]
    
    return render_template('project1.html', projects=projects_data)

if __name__ == '__main__':
    app.run(debug=True)

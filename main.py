from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:root@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True) #primary key for blog entries
    title = db.Column(db.String(250)) #will go into title area
    body = db.Column(db.String(2048)) #will go into body area

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/blog', methods=['POST', 'GET'])
def blog():
    return render_template('/blog.html')


@app.route('/newpost', methods=['POST', 'GET'])
def new_post():
    return render_template('/newpost.html')


# class Task(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120))
#     completed = db.Column(db.Boolean)

#     def __init__(self, name):
#         self.name = name
#         self.completed = False


# @app.route('/', methods=['POST', 'GET'])
# def index():

#     if request.method == 'POST':
#         task_name = request.form['task']
#         new_task = Task(task_name)
#         db.session.add(new_task)
#         db.session.commit()

#     tasks = Task.query.filter_by(completed=False).all()
#     completed_tasks = Task.query.filter_by(completed=True).all()
#     return render_template('todos.html',title="Get It Done!", 
#         tasks=tasks, completed_tasks=completed_tasks)


# @app.route('/delete-task', methods=['POST'])
# def delete_task():

#     task_id = int(request.form['task-id'])
#     task = Task.query.get(task_id)
#     task.completed = True
#     db.session.add(task)
#     db.session.commit()

#     return redirect('/')


if __name__ == '__main__':
    app.run()
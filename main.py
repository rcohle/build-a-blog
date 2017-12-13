from flask import Flask, request, redirect, render_template,url_for
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

    blog_posts = Blog.query.all()
    return render_template('/blog.html', blog_posts=blog_posts)

@app.route('/post')
def post():
    id = request.args.get('id')
    post_id = Blog.query.get(id)
    return render_template('/post.html',post_id=post_id)


@app.route('/newpost', methods=['POST', 'GET'])
def new_post():

    error_title = 'Please enter a title for your blog post'
    error_body = 'Please enter content for your blog post'
    error_empty_title = ''
    error_empty_body = ''

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        if title == '':
            error_empty_title = error_title
        if body == '':
            error_empty_body = error_body

    if request.method == 'POST' and error_empty_body == '' and error_empty_title == '':
        db.session.add(Blog(title,body))
        db.session.commit()
        return redirect('/blog')

        #post_id = request.args.get('id','title','body')  #NEW
        #post_id2 = Blog.query.get(id)
        #return ('/post.html', post_id=post_id2)  #changed from redirect to blog
    else:
        return render_template('/newpost.html',error_empty_title=error_empty_title,error_empty_body=error_empty_body)

if __name__ == '__main__':
    app.run()
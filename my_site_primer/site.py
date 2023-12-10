from flask import Flask, render_template, url_for, request, redirect

from myDB import create_index, show_table, select_index, delete_index, update_index

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/posts/')
def posts():
    articles = show_table()
    return render_template('posts.html', articles=articles)


@app.route('/posts/<int:id>')
def post_detail(id):
    article = select_index(id)[0]
    return render_template('post-detail.html', article=article)


@app.route('/posts/<int:id>/delete')
def post_delete(id):
    delete_index(id)
    return redirect('/posts/')


@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def post_update(id):
    article = select_index(id)[0]
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        update_index(id, title, intro, text)
        return redirect('/posts/')
    return render_template('post-update.html', article=article)


@app.route('/create-article/', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        create_index(title, intro, text)
        return redirect('/posts/')
    else:
        return render_template('create_article.html')


app.run(debug=True)
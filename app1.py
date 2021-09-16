from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'name' : 'vishnu balaji',
        'alias' : 'pytorcher',
        'company' : 'facebook',
        'salary' : 50000
    },
    {
        'name' : 'harini',
        'alias' : 'natasha',
        'company' : 'google',
        'salary' : 70000
    }
]

@app.route('/')
def index():
    title = "Its just an index page"
    return render_template('index1.html', posts=posts, title=title)

@app.route('/about')
def about():
    title = "boom, looking for this?"
    return render_template('about.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)
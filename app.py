import json
from flask import Flask, request

app = Flask(__name__)

post1 = {
    "title" : "Good day",
    "content" : "I met a girl. She had blue eyes"
}
post2 = {
    "title" :"..",
    "content" : "nnn"
}

print(post1["title"])
print(post1["content"])
print (post2["title"])
print (post2["content"])
posts = [post1, post2]
@app.route('/')
def hello_world():
    return json.dumps(posts)

@app.route('/addpost',methods=["POST"])
def add_post():
    args = request.form
    title_value = args["title"]
    content_value = args["content"]
    new_post = {"title":title_value,
                "content":content_value}
    posts.append(new_post)
    print(title_value,content_value)
    return "ok"

if __name__ == '__main__':
    app.run()
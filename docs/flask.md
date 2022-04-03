# flask

## practice

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>hello world</p>"
```

## 参考
- https://flask.palletsprojects.com/en/2.1.x/quickstart/#a-minimal-application
# -*- coding: utf-8 -*-

# @Date    : 2018-10-26
# @Author  : Peng Shiyu

from flask import (
    Flask,
    render_template,
    request,
    jsonify,
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get")
def get():
    data = {}
    headers = dict(request.headers)
    data["headers"] = headers
    data["path"] = request.path
    data["base_url"] = request.base_url
    # data["user_agent"] = {
    #     "user_agent": request.user_agent.string,
    #     "browser": request.user_agent.browser,
    #     "language": request.user_agent.language,
    #     "platform": request.user_agent.platform,
    #     "version": request.user_agent.version,
    # }
    data["cookies"] = request.cookies
    data["url"] = request.url
    data["files"] = request.files
    data["json"] = request.json
    data["values"] = request.values
    data["args"] = request.args
    data["data"] = request.data
    data["form"] = request.form
    data["range"] = request.range
    data["script_root"] = request.script_root
    data["host"] = request.host
    data["endpoint"] = request.endpoint
    # data["accept_charsets"] = request.accept_charsets
    # data["accept_encodings"] = request.accept_encodings
    # data["accept_languages"] = request.accept_languages
    # data["accept_mimetypes"] = request.accept_mimetypes

    data["is_xhr"] = request.is_xhr

    data["x-forwarded-for"] = request.environ.get("HTTP_X_FORWARDED_FOR")
    data["X-Real-IP"] = request.environ.get("X-REAl-IP")
    data["remote_addr"] = request.remote_addr


    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

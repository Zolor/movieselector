# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask, render_template, request, redirect, url_for
from movieselector import movieselector
import requests

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        req = request.form
        print(req)
        #return redirect(url_for('relationships',ID=request.form.get('Galactic_ID')))
        return redirect(url_for('answer',imdb_answer=request.form.get('imdb_url')))
    else:
        return render_template('index.html')

@app.route('/answer', methods=["GET"])
def answer():
    if "This list is not public" in requests.get(request.args.get('imdb_answer')).text:
        return render_template('error.html')
    else:
        movie, imdb_link, imdb_poster = movieselector(request.args.get('imdb_answer'))
        return render_template('answer.html', movie = movie, imdb_link = imdb_link, imdb_poster = imdb_poster)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]

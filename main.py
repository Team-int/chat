from flask import redirect, url_for
from flask import Flask, render_template
from flask_socketio import SocketIO
import settings

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

@app.route('/')
def home():
	return redirect(url_for("web_index"))

@app.route('/web/<path>/')
def web_page(path):
	return render_template(path)

@app.route('/web/src/<path>/')
def web_src(path):
	return render_template('src/' + path)
	
@app.route('/web/')
def web_index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, host='copecone-server.duckdns.org', port=5000)

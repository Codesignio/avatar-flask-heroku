from flask import Flask, make_response, request
from avatar_generator import Avatar


app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/')
def hello():
    return 'You can generate avatars with the first letter. Try: /avatar?name=Pavel&size=128'

@app.route("/avatar")
def photo():
	try:
		initials = request.args.get('name');
		size = int(request.args.get('size'));
	except Exception:
		initials = "+";
		size = 128;
	avatar = Avatar.generate(size, initials, "PNG")
	headers = { 'Content-Type': 'image/png' }
	return make_response(avatar, 200, headers)
import pyrebase
import firebase_admin
from flask import *
#auth used for r/w e.g. creating users
from firebase_admin import credentials, auth
app = Flask(__name__)

cred = credentials.Certificate('fbAdminConfig.json')
firebase = firebase_admin.initialize_app(cred)
#used for read-only i.e. signing in
pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	unsuccessful = 'Please check your credentials'
	successful = 'Login successful'
	if request.method == 'POST':
		email = request.form['name']
		password = request.form['pass']
		try:
			userRef = pb.auth().sign_in_with_email_and_password(email, password)
			return redirect(url_for('dashboard',user=userRef))
		except Exception as ex:
			print(ex)
			return render_template('signin.html', us=unsuccessful)

	return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	unsuccessful = 'Please enter a valid email and password'
	successful = 'Signup successful'
	if request.method == 'POST':
		email = request.form['name']
		password = request.form['pass']
		try:
			auth.create_user(email=email, password=password)
			return render_template('signup.html', s=successful)
		except Exception as ex:
			print(ex)
			return render_template('signup.html', us=unsuccessful)

	return render_template('signup.html')

@app.route('/dashboard/<user>', methods=['GET', 'POST'])
def dashboard(user):
	#for refresh button
	if request.method == 'POST':
		pass
	#get user information
	name = user.identifier
	#pass in relevant info to load custom dashboard
	return render_template('dashboard.html', name=name)


if __name__ == '__main__':
	app.run()






# FlaskFirebaseAuth
A simple sign in, sign up, and custom dashboard for users built in Flask and Firebase


This is a template to bootstrap for your own applications. It implements a simple sign in, sign up, and custom dashboard for users with Firebase.

### Dependencies
```
- pyrebase
- firebase_admin
- flask
- python
```

### How to use
1. Clone this repo to your local computer
2. Set up a Firebase project and download the web application script configuration to a JSON file, named **fbconfig.json** (from settings icon -> Project Settings -> General (scroll to bottom).  
3. Export the AdminSDK private key to a JSON file, named **fbAdminConfig.json** (from settings icon -> Project Settings -> Service Accounts, generate new private key, make sure python is selected)
4. Run python app.py
5. Navigate to [address in terminal]/signup

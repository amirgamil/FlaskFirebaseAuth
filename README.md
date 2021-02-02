# FlaskFirebaseAuth
This is a template to bootstrap for your own applications. It implements a simple sign in, sign up, and custom dashboard for users with Firebase. I couldn't find one to clone when I was building this, so thought it might be useful to share

### Dependencies
```
- pyrebase
- firebase_admin
- flask
- python
```

### How to use
1. Clone this repo to your local computer
2. Set up a Firebase project (make sure you add a web application by clicking on the </> button
3. Download the web application script configuration to a JSON file, named **fbconfig.json** (from settings icon -> Project Settings -> General (scroll to bottom). 
4. Export the AdminSDK private key to a JSON file, named **fbAdminConfig.json** (from settings icon -> Project Settings -> Service Accounts, generate new private key, make sure python is selected)
5. Run python app.py
6. Navigate to [address in terminal]/signup

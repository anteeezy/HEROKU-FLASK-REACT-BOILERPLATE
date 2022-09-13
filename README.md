# HEROKU-FLASK-REACT-BOILERPLATE

A couple IMPORTANT notes. I found it hard to fully get setup with Flask and React so I hope to explain it down here. 

1. A Heroku Flask web app is as at heart a Python app. To get started, we need pipenv and the current copy of Python (heroku currently uses 3.10.7). We can pipenv install flask gunicorn flask-cors flask-restul. The barebones essentials is pipenv install flask gunicorn but I use cors and restful here. Using pipenv compared to other enviroments is that heroku will automatically look at your pipenv files your create and you do not need to make a requirments.txt later and it is easier to manage. 

2. Procfile. We create a Procfile in the root folder which is also connected to the python file which will run your flask app. Whatever you name your app is whatever we will use in our Procfile. I.E. web: gunicorn app:app or web: gunicorn <your file that runs your flask app>:<the name of your flask app>

3. runtime.txt. We can specify the specific python version, sometimes I've gotten errors when I did not specify but heroku will default to 3.10.7 or their newest update. All this file has is: python-3.10.7 and is found in the root folder along with your app.py and pip files. 

4. Changes to app.py (file that runes your app). You have to specify your static url path and static folder. Example from my boiler plate: app = Flask(__name__, static_url_path='', static_folder='frontend/build/'). The 'frontend/build/' is simply the folder of our react frontend and then the build file from npm run build, I will explain this later further.

5. Serve. You have to create a serve function which will actually link your flask to your react fronend via the 'index.html'found in build. You should look further into my file app.py for more context. 

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')
    
6. React frontend. You will store all of your react code in a folder called 'frontend'. You do not need to change package.json or really anything besides the links of requests. For example if you are calling 'http://localhost:5000/your_request' change this to your heroku link. -> 'https://receipterboxd.herokuapp.com/your_request'. 

7. MAKE SURE TO npm run build ! 

8. VERY IMPORTANT: MAKE SURE TO COMMENT /BUILD IN YOUR GIT IGNORE FILE. 

9. Assuming you already have heroku cli, run the series of commands: 
    heroku login
    heroku create your-app
    git add . 
    git commit -m 'first commit!' 
    git push heroku main
    
    Then go to your new deployed website! 
    
10. Hopefully you have no other errors. Make sure you are pipenv installing every library you are using and npm installing every react library in the specific frontend folder. 

11. NOTE ON DATABASES: This does not cover databases but a huge note is HEROKU DOES NOT USE SQLITE WHICH IS FLASK'S DEFAULT DATABASE! I suggest you use PostgreSQL. 

12. "no web processes running" was a commin error I was getting. This can simply be fixed by running heroku ps:scale web=1 after you push to main. 

13. If all else fails make sure you are checking the logs and make sure that your dynos are running and is being recognized! A good way is to use the heroku dashboard instead of cli. 

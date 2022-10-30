from django.shortcuts import render
from django.contrib import auth
from pyparsing import identbodychars
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyDShsoeNeZsQg2ZxdNp33v1QtrjSjalZPg",
    'authDomain': "health-care-web-212e0.firebaseapp.com",
    'databaseURL': "https://health-care-web-212e0-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "health-care-web-212e0",
    'storageBucket': "health-care-web-212e0.appspot.com",
    'messagingSenderId': "229559686647",
    'appId': "1:229559686647:web:a93fd4e466a9f2adb80af2",
    'measurementId': "G-WM3FSPBPDV",
    'serviceAccount': "C:\\Users\\ben_l\\OneDrive\\Desktop\\Uni Stuff\\Web Development\\health-care-web-212e0-firebase-adminsdk-nyf5g-9ba2dd4249.json"
    }

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
authenticate = firebase.auth()
database = firebase.database()


def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def findadoctor(request):
    return render(request, "findadoctor.html")
    
def specialities(request):
    return render(request, "specialities.html")

def healthcareblog(request):
    return render(request, "healthcareblog.html")

def ourservices(request):
    return render(request, "ourservices.html")


def postRegister(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phoneNum = request.POST.get('number')
    confirmPsw = request.POST.get('confirmPsw')
    gender = request.POST.get('gender')

    # Register user in firebase using email & password
    try:
        user = authenticate.create_user_with_email_and_password(email, confirmPsw)
    except:
        message = "Error Registering Account"
        return render(request, "register.html", {"msg": message})

    # Retrieve User Unique  ID after successfully registered user
    uid = user['localId']

    userData = {"name": name, "email": email, "phoneNum": phoneNum, "gender": gender}

    database.child("users").child(uid).child("details").set(userData)
    message = "Account Registered Succesfully"
    return render(request, "register.html", {"msg": message})


def postLogin(request):
    email = request.POST.get('email')
    password = request.POST.get('psw')

    try:
        user = authenticate.sign_in_with_email_and_password(email, password)
    except:
      message="Invalid Credentials. Please Try Again."
      return render(request, "register.html", {"msg": message})

    # Get user id and store as session id, request session while user login
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "index.html")

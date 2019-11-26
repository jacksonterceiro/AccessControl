import pyrebase

def getKey():

    firebaseConfig = {
    "apiKey": "AIzaSyDKhhF1VOIiQE41WOqqDeQNAl4EHpBUNmU",
    "authDomain": "acesscontrol-4d474.firebaseapp.com",
    "databaseURL": "https://acesscontrol-4d474.firebaseio.com",
    "projectId": "acesscontrol-4d474",
    "storageBucket": "acesscontrol-4d474.appspot.com",
    "messagingSenderId": "1010196558453",
    "appId": "1:1010196558453:web:084af14c1cad18bc"
    }

    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()

    value = db.child("reservations").get()

    return value.val()
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('C:/Users/Neverland/Desktop/flutter_trash/functions/capstone-dream-firebase-adminsdk-8gf2o-51de2b67b9.json')
firebase_admin.initialize_app(cred)

print('Firebase Admin SDK initialized successfully!')
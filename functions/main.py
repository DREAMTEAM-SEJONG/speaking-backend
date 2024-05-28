from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials, firestore as admin_firestore, initialize_app
import functions_framework
from datetime import datetime

# Firebase Admin SDK 초기화
json_path = 'capstone-dream-firebase-adminsdk-8gf2o-51de2b67b9.json'
cred = credentials.Certificate(json_path)
firebase_admin.initialize_app(cred)

# Firestore 클라이언트 초기화
db = admin_firestore.client()

def on_new_message(event, context):
    resource_string = context.resource
    
    data = event['value']['fields']

    # Document 경로에서 user_id와 room_id 추출
    resource_parts = resource_string.split('/')
    collection_name = resource_parts[5]
    user_id = resource_parts[6]
    room_id = resource_parts[8]
    # split_value = data['split']['integerValue']
    split_value = int(data.get('split', {}).get('integerValue', 0))
    
    # 이게 애플리케이션에서 보낸 사용자 발화
    comment = data['comment']['stringValue']
    
    # chat collection 데베에 데이터 추가된 경우
    if collection_name == "chat" and split_value == 1:
        print(f'New message added to chat/{user_id}/rooms/{room_id}/message with comment: {comment}')
        
        messages_collection = db.collection('chat').document(user_id).collection('rooms').document(room_id).collection('message')
        
        # 다른 함수 불러와서 결과 만들기
        result = comment

        # 이게 데이터 추가하는 코드
        messages_collection.add({
            'comment': result,
            'split': 2,
            'language': 1,
            'time': admin_firestore.SERVER_TIMESTAMP
        })
        print(f'Processed message added to chat/{user_id}/rooms/{room_id}/message with updated fields.')

    # lecture collection 데베에 데이터 추가된 경우
    elif collection_name == "lecture" and split_value == 1:
        print(f'New message added to lecture/{user_id}/rooms/{room_id}/message with comment: {comment}')
        
        messages_collection = db.collection('lecture').document(user_id).collection('rooms').document(room_id).collection('message')
        
        # 다른 함수 불러와서 결과 만들기
        result = comment

        # 이게 데이터 추가하는 코드
        messages_collection.add({
            'comment': result,
            'split': 2,
            'language': 1,
            'time': admin_firestore.SERVER_TIMESTAMP
        })
        print(f'Processed message added to lecture/{user_id}/rooms/{room_id}/message with updated fields.')


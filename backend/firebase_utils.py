# firebase_utils.py
from firebase_admin import messaging
from models import User, db

def send_firebase_notification(user_id, message):
    try:
        # Retrieve the FCM token for the user from the database
        user = User.query.get(user_id)
        if user and user.fcm_token:
            # Create a message to send via Firebase Cloud Messaging (FCM)
            firebase_message = messaging.Message(
                notification=messaging.Notification(
                    title="New Message",
                    body=message
                ),
                token=user.fcm_token  # Send the notification to the user's device
            )

            # Send the message using Firebase Cloud Messaging
            response = messaging.send(firebase_message)
            print(f"Successfully sent message: {response}")
        else:
            print(f"FCM token not found for user {user_id}. Cannot send notification.")
    except Exception as e:
        print(f"Error sending notification: {e}")

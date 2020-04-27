from firebase_admin import credentials
from firebase_admin import messaging
import firebase_admin
import sys

sys.path.append("lib")


cred = credentials.Certificate('/home/rajeev/PycharmProjects/firebase_messaging/DataSDK-2ffc438a9b47.json')
access_token_info = cred.get_access_token()

access_token = access_token_info.access_token
expiration_time = access_token_info.expiry
print(access_token,expiration_time)
default_app = firebase_admin.initialize_app(cred)


def send_to_topic():
    # [START send_to_topic]
    # The topic name can be optionally prefixed with "/topics/".
    topic = 'notify'

    # See documentation on defining a message payload.
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        topic=topic,
    )

    # Send a message to the devices subscribed to the provided topic.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)

    registration_tokens = [
        'chCK9jrYEQ8:APA91bEf0ZxbIsw0yCvHw1SrnitL1iDLV3eus-bXcfnuyDCSHlJwyh2saKLpEpHrJUDJT6ExcF0YIk0oA83Ps_IjlBk-MAxX3_74m6fQtHql1kP5Ks0lehn2xbdbA5TQ87aj6B0_R2kN',
        # ...
    ]

    # Unubscribe the devices corresponding to the registration tokens from the
    # topic.
    response = messaging.subscribe_to_topic(registration_tokens, topic)
    # See the TopicManagementResponse reference documentation
    # for the contents of response.
    print(response, 'tokens were subscribed successfully')
    # [END send_to_topic]

send_to_topic()

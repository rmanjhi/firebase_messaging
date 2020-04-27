from sleekxmpp.clientxmpp import ClientXMPP
import logging
import socket
import json
import uuid

logging.basicConfig(level=logging.DEBUG, format="%(levelname)7s %(module)12s:%(lineno)-4s %(message)s")

FCM_SERVER_URL = "fcm-xmpp.googleapis.com"
FCM_SERVER_PORT = 5235
FCM_SERVER_KEY = "AAAAK8rD2-8:APA91bGa17ZpU4G-_b1qv2F346N1GnbT8DXWgpvr0LmNSAJqpn22YQanDF6eszQvpdtLdSov-8iJt-sjhi1NvCIrfDThAP_blLaMXqn-LB5aJXdh6Hl6O4Y63Zr-7C0YCztVXN4wJJqk" # <- Your Server Key
FCM_SENDER_ID = "188085427183" # <- Your Sender ID
FCM_JID = FCM_SENDER_ID + "@gcm.googleapis.com"
FCM_SERVER_IP = socket.gethostbyname(FCM_SERVER_URL)
TOPIC = "config"

body = {
    "to": TOPIC,
    "message_id": uuid.uuid4().hex,
    "data": { "msg": "This is hello xmpp"}
}
message = "<message><gcm xmlns='google:mobile:data'>"+json.dumps(body)+"</gcm></message>"

class Client(ClientXMPP):
    def __init__(self):
        ClientXMPP.__init__(self, FCM_JID, FCM_SERVER_KEY, sasl_mech="PLAIN")
        self.add_event_handler("session_start", self.start)
        self.auto_reconnect = False
        self.connect((FCM_SERVER_IP, FCM_SERVER_PORT), use_tls = True,reattempt = True)
        print("Connected!!")
        self.process(block=True)
        print("Process Done!!")
    def start(self, event):
        self.send_raw(message)
        self.disconnect(wait=True)


Client()
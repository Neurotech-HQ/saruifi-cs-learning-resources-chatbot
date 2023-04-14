from fastapi import FastAPI, WebSocket, Request
from sarufi import Sarufi
from pydantic import BaseModel
import uvicorn
from urllib import parse
import os
import json
import logging
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ.get('SARUFI_CLIENT_ID')
client_secret = os.environ.get('SARUFI_CLIENT_SECRET')
account_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
account_sid = os.environ.get('TWILIO_SID')

logging.basicConfig(level=logging.DEBUG)
client=Client(account_sid, account_auth_token)
sarufi = Sarufi(client_id=client_id, client_secret=client_secret)

app = FastAPI()

def log_message(message, response):
    f = open("messageResponse.log", "a")
    f.write(f"\nMessage: {message} \n {response}")
    f.flush()

class Message(BaseModel):
    MessagingResponse: dict
    class Config():
        orm_mode = True

#websocket endpoint
@app.websocket("/ws/websocket_endpoint")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        message = await websocket.receive_text()
        print(message)
        bots = sarufi.bots()
        Nalah=bots[0]
        response = Nalah.respond(message, chat_id="QWERTY")
        # log_message(message, response)
        for content in response["message"]:
            await websocket.send_text(content)

# webhook endpoint
@app.post("/webhook_endpoint")
async def message_endpoint(request: Request):
    data = await request.body()
    # convert url and byte format to string
    parsed_data = parse.parse_qs(data.decode('utf-8'))
    json_data = json.dumps(parsed_data)
    # convert string to json
    message_dict = json.loads(json_data)
    # sarufi bots
    bots = sarufi.bots()
    Nalah=bots[0]
    # send message from request to Nalah(sarufi bot)
    response = Nalah.respond(message_dict["Body"][0])
    # get response and log with message
    log_message(message_dict["Body"], response["message"])
    # loop through list and send each item through twilio
    i = 0
    while i < len(response["message"]):
        message = client.messages.create(
                                    body=response["message"][i],
                                    from_=message_dict["To"],
                                    to= message_dict["From"])
        print(message.sid)
        i += 1

if __name__ == '__main__':
    uvicorn.run(app, debug=True)







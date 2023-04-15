# Nalah

A Computer Science resource chatbot built on [Sarufi](https://sarufi.io/). Sarufi is a low to no-code Conversational AI builder platform that will provides NLP infrastructure to create and deploy a chatbot.

The application uses a [**sarufi-python-sdk**](https://github.com/sarufi-io/sarufi-python-sdk)

Nalah, is integrated with whatsapp using **Twilio**.

## Installation

Set up the a virtual environment, e.g when using **python-virtualenv**

```bash
virtualenv venv
```

Install all the requirements from the **requirements.txt** file

```bash
pip install -r requirements.txt
```

Set up the required Environment variables in this case:

```bash
    SECRET_KEY = 'Some unique string'

    SARUFI_CLIENT_ID = 'Sarufi account client ID'

    SARUFI_CLIENT_SECRET = 'Sarufi account client secret'

    TWILIO_SID = 'Twilio Account SID'

    TWILIO_AUTH_TOKEN  = 'Twilio Account Authentication token'
 ```

 Using **uvicorn** as the server application **run**

 ```bash
 uvicorn main:app --reload
 ```

## Obtaining Sarufi credentials

Log in to your [sarufi](https://sarufi.io) account. Navigate to profile --> `Authorization`. There you will have you have the credentials to be used.

## Technologies used

- [Flask](https://flask.palletsprojects.com/)
- [Twilio](https://www.twilio.com/)
- [Sarufi](https://sarufi.io/)

## Screenshots

![screenshot](https://github.com/wekesa360/saruifi-cs-learning-resources-chatbot/blob/main/screenshots/Screenshot_1.png?raw=true)

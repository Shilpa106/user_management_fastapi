import time
import asyncio
from fastapi import FastAPI, BackgroundTasks, File, Form, UploadFile,status,HTTPException
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig


app = FastAPI()

conf = ConnectionConfig(
    MAIL_USERNAME="tu49085@gmail.com",
    MAIL_PASSWORD="Test@12345",
    MAIL_FROM="tu49085@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)


print("hey")
def usermail(event):
    print(event)
    email=event['email']
    password=event['password']
    print(type(event['email']))
    print(email)

    template =f" hey  {email} your successfully resgister and Password  {password} ,"

    message = MessageSchema(
        subject="please login",
        recipients=[email],
        # List of recipients, as many as you can pass
        body=template,
        subtype='html',

    )

    fm = FastMail(conf)
    time.sleep(5)
    mes= asyncio.run(fm.send_message(message))
    print(mes)
    return event


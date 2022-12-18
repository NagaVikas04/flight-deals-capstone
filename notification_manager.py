import smtplib

from twilio.rest import Client

TWILIO_ACCOUNT_SID = "Your TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR AUTH TOKEN"
TWILIO_TO_NUMBER = "YOUR NUMBER"
TWILIO_FROM_NUMBER = "YOUR TWILIO NUMBER"

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR GENERATED PASSWORD"

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            from_=TWILIO_FROM_NUMBER,
            body=message,
            to=TWILIO_TO_NUMBER
        )
        print(message.sid)

    def send_email(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight!\n\n{message}\n{google_flight_link}.encode('utf-8')"
                )
                print("mail sent successfully")


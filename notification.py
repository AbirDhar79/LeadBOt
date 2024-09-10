#Mailchimp was used to send notification as mail
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

def send_email_notification(posts):
    client = MailchimpMarketing.Client()
    client.set_config({
        "api_key": "0759901c5180fc3b4f9c6d37a3ce040e-us17",
        "server": "us17"
    })

    try:
        response = client.messages.send({
            "from_email": "professordhar69@gmail.com",
            "subject": "New Posts Notification",
            "text": "\n".join([f"{post['title']}: {post['url']}" for post in posts]),
            "to": [{"email": "abirdhar79@gmail.com"}]
        })
        print("Emails sent successfully:", response)
    except ApiClientError as error:
        print("Error sending emails:", error.text)

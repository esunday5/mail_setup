from flask_mail import Message
from mail import mail  # Import mail instance

def send_email(recipients, branch_name, request_type, content):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{request_type} Notification</title>
    </head>
    <body>
        <h2>New {request_type} for {branch_name}</h2>
        <p>{content}</p>
    </body>
    </html>
    """

    msg = Message(
        subject=f"{request_type} Notification",
        sender="emmanatesynergy@gmail.com",
        recipients=recipients
    )
    msg.body = f"You have a new {request_type} for {branch_name}."
    msg.html = html_content

    try:
        mail.send(msg)
        return {"message": f"Email sent successfully to: {', '.join(recipients)}"}, 200
    except Exception as e:
        return {"error": f"Failed to send email: {str(e)}"}, 500

import os
from flask import Flask, jsonify  # Import jsonify for JSON responses
from flask_mail import Mail, Message
import logging
from logging import StreamHandler

app = Flask(__name__)

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'emmanatesynergy@gmail.com'  # Your Gmail email
app.config['MAIL_PASSWORD'] = 'mrfl owrh pyoq hflx'  # App password if 2FA enabled
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_TIMEOUT'] = 10

mail = Mail(app)

@app.route("/")
def send_html_email():
    msg = Message(subject='You Have a New Request!',
            sender="emmanatesynergy@gmail.com",
            recipients=["henry.etim@ekondomfbank.com", "amanimeshiet@gmail.com"]
            )

    # HTML body content
    msg.html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Notification</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4; color: #333;">

    <!-- Email Container -->
    <div style="max-width: 600px; margin: auto; background-color: #ffffff; border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden;">

        <!-- Header Section -->
        <div style="background-color: #37a04e; padding: 20px; text-align: center;">
            <img src="https://ibank.mybankone.com/tenants/101/img/logo.png" alt="Logo" style="max-width: 150px;">
        </div>

        <!-- Warning Section -->
        <div style="padding: 20px; text-align: center;">
            <p style="font-size: 22px; font-weight: bold; color: #388e3c;">You have a new request for {Branch Name}!</p>
        </div>

        <!-- Subheading -->
        <p style="margin: 0 20px; font-size: 16px; text-align: center; color: #555;">From (staff name and position)</p>

        <!-- Email Body -->
        <div style="padding: 20px; text-align: center;">
            <p style="font-size: 14px; line-height: 1.6; color: #333;">{"Request Details"}</p>
            <p style="font-size: 14px; line-height: 1.6; color: #333;">{"Request Type"}</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam tempora perspiciatis molestias velit, recusandae, eligendi, aspernatur excepturi nam hic cumque nulla non saepe ducimus impedit soluta dolores maxime? Consequuntur, nam!</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam tempora perspiciatis molestias velit, recusandae, eligendi, aspernatur excepturi nam hic cumque nulla non saepe ducimus impedit soluta dolores maxime? Consequuntur, nam!</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam tempora perspiciatis molestias velit, recusandae, eligendi, aspernatur excepturi nam hic cumque nulla non saepe ducimus impedit soluta dolores maxime? Consequuntur, nam!</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam tempora perspiciatis molestias velit, recusandae, eligendi, aspernatur excepturi nam hic cumque nulla non saepe ducimus impedit soluta dolores maxime? Consequuntur, nam!</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam tempora perspiciatis molestias velit, recusandae, eligendi, aspernatur excepturi nam hic cumque nulla non saepe ducimus impedit soluta dolores maxime? Consequuntur, nam!</p>

            
            
            
            
            <div style="text-align: center; margin: 20px 0;">
                <a href="#" style="text-decoration: none; background-color: #337036; color: #ffffff; padding: 10px 20px; border-radius: 5px; font-size: 14px;">Click to review request</a>
            </div>
        </div>

        <!-- Spacer -->
        <div style="padding: 20px 0; text-align: center;">
            <hr style="border: 0; border-top: 1px solid #e0e0e0; margin: 0 20px;">
        </div>

        <!-- Footer -->
        <footer style="padding: 20px; text-align: center; font-size: 13px; color: #777; position: absolute-bottom;">
            <p style="margin: 0;">Copyright &copy; Ekondo Staff Portal 2024</p>
            <div style="margin: 10px 0;">
                <a href="https://www.facebook.com/ekondomfb/about" target="_blank" style="text-decoration: none; margin: 0 5px;">
                    <img src="https://via.placeholder.com/24?text=FB" alt="Facebook" style="width: 24px; height: 24px;">
                </a>
                <a href="https://x.com/ekondomfb" target="_blank" style="text-decoration: none; margin: 0 5px;">
                    <img src="https://via.placeholder.com/24?text=X" alt="Twitter" style="width: 24px; height: 24px;">
                </a>
                <a href="https://www.linkedin.com/in/ekondo-bank-40a666155" target="_blank" style="text-decoration: none; margin: 0 5px;">
                    <img src="https://via.placeholder.com/24?text=LI" alt="LinkedIn" style="width: 24px; height: 24px;">
                </a>
                <a href="https://www.instagram.com/ekondomfb" target="_blank" style="text-decoration: none; margin: 0 5px;">
                    <img src="https://via.placeholder.com/24?text=IG" alt="Instagram" style="width: 24px; height: 24px;">
                </a>
            </div>
        </footer>
    </div>

</body>
</html>
    """

    mail.send(msg)

    return "Email Sent Successfully!"

if __name__ == '__main__':
    app.run(debug=True)
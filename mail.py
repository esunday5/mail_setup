import os
from flask import Flask, jsonify, request  # Import jsonify for JSON responses
from flask_mail import Mail, Message
import logging
from logging import StreamHandler
from flask import Blueprint
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for the app
CORS(app, resources={r"/*": {"origins": "*"}})

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'emmanatesynergy@gmail.com'  # Your Gmail email
app.config['MAIL_PASSWORD'] = 'mrfl owrh pyoq hflx'  # App password if 2FA enabled
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_TIMEOUT'] = 10

mail = Mail(app)

# Register Petty Cash Advance Blueprint
from pettycashadvance import pettycashadvance_blueprint
from pettycashretirement import pettycashretirement_blueprint
from opexcapexretirement import opexcapexretirement_blueprint
from stationeryrequest import stationeryrequest_blueprint
app.register_blueprint(pettycashadvance_blueprint)
app.register_blueprint(pettycashretirement_blueprint)
app.register_blueprint(opexcapexretirement_blueprint)
app.register_blueprint(stationeryrequest_blueprint)

from notifications import (
    officer_blueprint,
    supervisor_blueprint,
    reviewer_blueprint,
    approver_blueprint,
    account_officer_blueprint,
)

app.register_blueprint(officer_blueprint)
app.register_blueprint(supervisor_blueprint)
app.register_blueprint(reviewer_blueprint)
app.register_blueprint(approver_blueprint)
app.register_blueprint(account_officer_blueprint)


def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_regex, email)


@app.route("/cashadvance", methods=["POST"])
def send_email():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data received"}, 400)

    branch_name = data.get("branch_name", "Unknown Branch")
    request_type = data.get("request_type", "Unknown Type")
    department = data.get("department", "Unknown Department")
    payee_name = data.get("payee_name", "Unknown Payee")
    payee_account = data.get("payee_account", "Unknown Account")
    invoice_amount = data.get("invoice_amount", "N/A")
    cash_advance = data.get("cash_advance", "N/A")
    narration = data.get("narration", "N/A")
    less_what = data.get("less_what", "N/A")
    amount = data.get("amount", "N/A")
    recipient_email = data.get("recipient_email")

    if not recipient_email:
        return jsonify({"error": "Recipient email is required"}, 400)

    if isinstance(recipient_email, str):
        recipient_emails = [recipient_email]
    elif isinstance(recipient_email, list):
        recipient_emails = recipient_email
    else:
        return jsonify({"error": "Invalid email format"}, 400)

    for email in recipient_emails:
        if not is_valid_email(email):
            return jsonify({"error": f"Invalid email: {email}"}, 400)

    # Define the HTML content with dynamic branch name
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Email Notification</title>
    </head>
    <body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4; color: #555;">
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden;">
            <div style="background-color: #37a04e; padding: 20px; text-align: center;">
                <img src="https://ibank.mybankone.com/tenants/101/img/logo.png" alt="Logo" style="max-width: 150px;">
            </div>
            <p style="font-size: 22px; font-weight: bold; color: #388e3c; text-align: center;">You have a new request for {branch_name}!</p>

            <div style="padding: 20px; font-size: 14px; text-align: center;">
                <p><strong>Request Type:</strong> {request_type}</p>
                <p><strong>Department:</strong> {department}</p>
                <p><strong>Payee Name:</strong> {payee_name}</p>
                <p><strong>Payee Account:</strong> {payee_account}</p>
                <p><strong>Invoice Amount:</strong> {invoice_amount}</p>
                <p><strong>Cash Advance:</strong> {cash_advance}</p>
                <p><strong>Narration:</strong> {narration}</p>
                <p><strong>Less What:</strong> {less_what}</p>
                <p><strong>Amount:</strong> {amount}</p>
                <p><strong>Recipient Email(s):</strong> {", ".join(recipient_email)}</p>
            </div>


                <div style="text-align: center; margin: 20px 0;">
                    <a href="#" style="text-decoration: none; background-color: #337036; color: #ffffff; padding: 10px 20px; border-radius: 5px; font-size: 14px;">Click to review request</a>
                </div>
            </div>
            <!-- Footer -->
            <footer style="padding: 20px; text-align: center; font-size: 13px; color: #777; position: absolute-bottom;">
                <p style="margin: 0;">Copyright &copy; Ekondo Staff Portal 2024</p>
            </footer>
        </div>
    </body>
    </html>
    """

 # Create the email
    msg = Message(
        subject="New Request Notification",
        sender="emmanatesynergy@gmail.com",
        recipients=recipient_emails,  # Changed to recipient_emails
    )
    msg.body = f"You have a new request for {branch_name}."  # Plain text fallback
    msg.html = html_content  # HTML content
    try:
        mail.send(msg)
        return {"message": "Email sent successfully!"}, 200
    except Exception as e:
        logging.error(f"Error sending email: {e}")  # Add logging
        return jsonify({"error": f"Failed to send email: {str(e)}"}, 500)


if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.DEBUG)  # Add logging
    print(app.url_map)
    app.run(debug=True)

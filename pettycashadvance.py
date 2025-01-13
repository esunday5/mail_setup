import os
from flask import Blueprint, request
from flask_mail import Message
from mail import mail  # Import mail from mail.py
from flask_cors import CORS

pettycashadvance_blueprint = Blueprint('pettycashadvance', __name__)

# Enable CORS for the app
CORS(pettycashadvance_blueprint, resources={r"/*": {"origins": "*"}})

# Petty Cash Advance route
@pettycashadvance_blueprint.route("/pettycashadvance", methods=["POST"])
def send_email():
    data = request.get_json()

    # Extracting required data
    branch_name = data.get("branch_name", "Unknown Branch")
    request_type = data.get("request_type", "Unknown Type")
    department = data.get("department", "Unknown Department")
    payee_name = data.get("payee_name", "Unknown Payee")
    payee_account = data.get("payee_account", "Unknown Account")
    total_amount = data.get("total_amount", "N/A")

    # Processing items and descriptions dynamically
    items_html = ""
    item_number = 1

    # Loop through items and descriptions
    while f"Item {item_number}" in data:
        item_name = data.get(f"Item {item_number}", "Unknown Item")
        description = data.get(f"Description {item_number}", "No description provided")
        items_html += f"""
        <p><strong>Item {item_number}:</strong> {item_name}<br>
        <strong>Description:</strong> {description}</p>
        """
        item_number += 1

    # Fallback if no items exist
    if not items_html:
        items_html = "<p>No items provided.</p>"

    # Email HTML content
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
                <p><strong>Items:</strong></p>
                {items_html}
                <p><strong>Total Amount:</strong> {total_amount}</p>
            </div>

            <div style="text-align: center; margin: 20px 0;">
                <a href="#" style="text-decoration: none; background-color: #337036; color: #ffffff; padding: 10px 20px; border-radius: 5px; font-size: 14px;">Click to review request</a>
            </div>
        </div>
        <footer style="padding: 20px; text-align: center; font-size: 13px; color: #777;">
            <p style="margin: 0;">Copyright &copy; Ekondo Staff Portal 2024</p>
        </footer>
    </body>
    </html>
    """

    # Create the email message
    msg = Message(
        subject="New Request Notification",
        sender="emmanatesynergy@gmail.com",
        recipients=["henry.etim@ekondomfbank.com", "amanimeshiet@gmail.com"]
    )
    msg.body = f"You have a new request for {branch_name}."  # Plain text fallback
    msg.html = html_content  # HTML content
    mail.send(msg)

    return {"message": "Email sent successfully!"}, 200

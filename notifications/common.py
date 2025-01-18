from flask_mail import Message
from mail import mail  # Import mail instance

def send_email(recipients, branch_name, request_type, department, payee_name, payee_account, description, invoice_amount, cash_advance, refund_reimbursement, less_what, total_amount, quantity, items):
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
                <p><strong>Description:</strong> {description}</p>
                <p><strong>Invoice Amount:</strong> {invoice_amount}</p>
                <p><strong>Cash Advance:</strong> {cash_advance}</p>
                <p><strong>Refund/Reimbursement:</strong> {refund_reimbursement}</p>
                <p><strong>Less What:</strong> {less_what}</p>
                <p><strong>Total Amount:</strong> {total_amount}</p>
                <p><strong>Quantity:</strong> {quantity}</p>
                <p><strong>Items:</strong> {', '.join(items) if isinstance(items, list) else items}</p>
            </div>

            <div style="text-align: center; margin: 20px 0;">
                <a href="#" style="text-decoration: none; background-color: #337036; color: #ffffff; padding: 10px 20px; border-radius: 5px; font-size: 14px;">Click to review request</a>
            </div>
        </div>
        <!-- Footer -->
        <footer style="padding: 20px; text-align: center; font-size: 13px; color: #777; position: absolute-bottom;">
            <p style="margin: 0;">Copyright &copy; Ekondo Staff Portal 2024</p>
        </footer>
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

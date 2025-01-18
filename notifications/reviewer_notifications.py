from flask import Blueprint, request, jsonify
from .common import send_email

reviewer_blueprint = Blueprint('reviewer', __name__)

@reviewer_blueprint.route("/notify/reviewer", methods=["POST"])
def notify_reviewer():
    data = request.get_json()
    branch_name = data.get("branch_name", "Unknown Branch")
    request_type = data.get("request_type", "Unknown Type")
    department = data.get("department", "Unknown Department")
    payee_name = data.get("payee_name", "Unknown Payee")
    payee_account = data.get("payee_account", "Unknown Account")
    description = data.get("description", "No description provided.")
    invoice_amount = data.get("invoice_amount", "N/A")
    cash_advance = data.get("cash_advance", "N/A")
    refund_reimbursement = data.get("refund_reimbursement", "N/A")
    less_what = data.get("less_what", "N/A")
    total_amount = data.get("total_amount", "N/A")
    quantity = data.get("quantity", "N/A")
    items = data.get("items", [])

    recipients = ["henry.etim@ekondomfbank.com"]  # Replace with reviewer email(s)

    return jsonify(send_email(recipients, branch_name, request_type, department, payee_name, payee_account, description, invoice_amount, cash_advance, refund_reimbursement, less_what, total_amount, quantity, items))

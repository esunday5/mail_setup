from flask import Blueprint, request, jsonify
from .common import send_email

supervisor_blueprint = Blueprint('supervisor', __name__)

@supervisor_blueprint.route("/notify/supervisor", methods=["POST"])
def notify_supervisor():
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

    recipients = ["ubong.wilson@ekondomfbank.com"]  # Replace with supervisor email(s)

    return jsonify(send_email(recipients, branch_name, request_type, department, payee_name, payee_account, description, invoice_amount, cash_advance, refund_reimbursement, less_what, total_amount, quantity, items))

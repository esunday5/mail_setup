from flask import Blueprint, request, jsonify
from .common import send_email

account_officer_blueprint = Blueprint('account_officer', __name__)

@account_officer_blueprint.route("/notify/account_officer", methods=["POST"])
def notify_account_officer():
    data = request.get_json()
    branch_name = data.get("branch_name", "Unknown Branch")
    request_type = data.get("request_type", "Unknown Type")
    content = data.get("content", "No content provided.")
    recipients = ["account_officer@example.com"]  # Replace with account officer email(s)

    return jsonify(send_email(recipients, branch_name, request_type, content))

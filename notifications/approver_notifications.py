from flask import Blueprint, request, jsonify
from .common import send_email

approver_blueprint = Blueprint('approver', __name__)

@approver_blueprint.route("/notify/approver", methods=["POST"])
def notify_approver():
    data = request.get_json()
    branch_name = data.get("branch_name", "Unknown Branch")
    request_type = data.get("request_type", "Unknown Type")
    content = data.get("content", "No content provided.")
    recipients = ["ekuere.akpan@ekondomfbank.com"]  # Replace with approver email(s)

    return jsonify(send_email(recipients, branch_name, request_type, content))

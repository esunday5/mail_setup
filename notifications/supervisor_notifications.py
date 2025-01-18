from flask import Blueprint, request, jsonify
from .common import send_email

supervisor_blueprint = Blueprint('supervisor', __name__)

@supervisor_blueprint.route("/notify/supervisor", methods=["POST"])
def notify_supervisor():
    data = request.get_json()
    branch_name = data.get("branch_name", "Unknown Branch")
    request_type = data.get("request_type", "Unknown Type")
    content = data.get("content", "No content provided.")
    recipients = ["supervisor@example.com"]  # Replace with supervisor email(s)

    return jsonify(send_email(recipients, branch_name, request_type, content))

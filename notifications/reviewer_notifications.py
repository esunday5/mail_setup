from flask import Blueprint, request, jsonify
from .common import send_email

reviewer_blueprint = Blueprint('reviewer', __name__)

@reviewer_blueprint.route("/notify/reviewer", methods=["POST"])
def notify_reviewer():
    data = request.get_json()
    branch_name = data.get("branch_name", "Unknown Branch")
    request_type = data.get("request_type", "Unknown Type")
    content = data.get("content", "No content provided.")
    recipients = ["reviewer@example.com"]  # Replace with reviewer email(s)

    return jsonify(send_email(recipients, branch_name, request_type, content))

from flask import Blueprint, request, jsonify
from .common import send_email

officer_blueprint = Blueprint('officer', __name__)

@officer_blueprint.route("/notify/officer", methods=["POST"])
def notify_officer():
    data = request.get_json()
    branch_name = data.get("branch_name", "Unknown Branch")
    request_type = data.get("request_type", "Unknown Type")
    content = data.get("content", "No content provided.")
    recipients = ["hyacinth.sunday@ekondomfbank.com"]  # Replace with officer email(s)

    return jsonify(send_email(recipients, branch_name, request_type, content))

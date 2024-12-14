from flask import Blueprint

# Create blueprints for different functionalities
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
message_bp = Blueprint('message', __name__, url_prefix='/api/messages')
meeting_bp = Blueprint('meeting', __name__, url_prefix='/api/meetings')

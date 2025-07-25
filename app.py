from flask import Flask, request, jsonify, send_file
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Gmail App Password Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'gopallohkna@gmail.com'        # ✅ your Gmail ID
app.config['MAIL_PASSWORD'] = 'oqea asyg dgru jzxd'     # ✅ your Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = 'gopallohkna@gmail.com'  # ✅ same as above

mail = Mail(app)

# Serve the HTML page
@app.route('/')
def serve_html():
    return send_file("webscraping.html")

# Receive POST request and send email
@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    query = data.get("query")

    if not name or not email or not query:
        return jsonify({"error": "Missing fields"}), 400

    try:
        msg = Message(
            subject=f"New Scraping Request from {name}",
            recipients=["gopallohkna@gmail.com"],  # ✅ The email to receive alerts
            body=f"""
You have a new request:

Name: {name}
Email: {email}
Query: {query}
"""
        )
        mail.send(msg)
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

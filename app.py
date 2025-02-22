from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

def get_top_output():
    """Fetches system top command output."""
    try:
        top_output = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True)
        return "<pre>" + top_output.stdout + "</pre>"
    except Exception as e:
        return f"Error fetching top output: {str(e)}"

@app.route('/htop')
def htop():
    name = "Your Full Name"  # Replace with your actual name
    username = os.getenv("USER", "Unknown User")  # Gets system username
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')

    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <h2>Top Output:</h2>
    {get_top_output()}
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


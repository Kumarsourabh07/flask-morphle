import os
import pytz
import subprocess
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Your full name
    full_name = "Kumar Sourabh"

    # Get system username
    system_username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Get 'top' command output
    top_output = subprocess.getoutput("top -b -n 1")

    # Format the response
    response = f"""
    <pre>
    Name: {full_name}
    User: {system_username}
    Server Time (IST): {server_time}

    TOP output:
    {top_output}
    </pre>
    """
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
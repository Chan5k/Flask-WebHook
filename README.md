# Flask Webhook

A simple Flask webhook application that receives JSON data, displays it on a webpage, and clears the data after refreshing the page.

## Requirements

- Python 3.6 or higher
- Flask 2.0.1 or higher

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Chan5k/flask-webhook.git

2. Change into the directory:

    ```bash
    cd flask-webhook

3. Install packages:
    
    ```bash
    pip install -r requirements.txt

# Usage

1. Start the app:

    ```bash
    python webhook.py

2. Send JSON data to the webhook using a tool like `curl`:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"key1": "value1", "key2": "value2"}' http://0.0.0.0:5000/webhook

3. View the received data by visiting `http://0.0.0.0:5000/display` in your browser. The data will be cleared upon refreshing the page.

# License
This project is licensed under the MIT License. See __LICENSE__ file for details.

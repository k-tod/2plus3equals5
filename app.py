import connexion
import logging
from flask import Flask, request, Response

# Initialize the Connexion application
app = connexion.App(__name__, specification_dir='./')
app.add_api('openapi.yaml')

# Get the underlying Flask app instance
flask_app = app.app

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a simple home page using Flask
@flask_app.route('/')
def home():
    return '''
    <h1>Simple Adding Calculator</h1>
    <form action="/add" method="get">
        <input type="number" name="a" required>
        <input type="number" name="b" required>
        <button type="submit">Add</button>
    </form>
    '''

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

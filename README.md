# E-COMMERCE-FLASK-WEBSITE
# Market Inventory Web App

This project is a Flask-based web application for managing a market inventory and user registrations. It incorporates SQLAlchemy for database management and WTForms for form validation.

## Features

- **User Registration**: Users can register for an account with a unique username, email address, and password. User credentials are securely stored in a SQLite database.
- **Market Inventory**: The application provides a market page where users can view items available for sale. Each item includes details such as name, price, barcode, and description.
- **User-Item Relationship**: Users are linked to the items they own through a one-to-many relationship. This allows users to manage their inventory and potentially buy or sell items in the future.
- **Responsive Design**: The web pages are designed to be responsive, ensuring a seamless user experience across various devices.

## Usage

To run the application locally:

1. Clone this repository.
2. Install the required dependencies listed in `requirements.txt`.
3. Run the Python script `app.py`.
4. Access the web application through a web browser at `http://localhost:5000`.

## Project Structure

- `app.py`: Main Python script containing Flask routes and database configurations.
- `forms.py`: Defines WTForms for user registration.
- `templates/`: Directory containing HTML templates for different pages.
- `market.db`: SQLite database file storing user and item data.

## Dependencies

- Flask
- Flask-SQLAlchemy
- WTForms

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.


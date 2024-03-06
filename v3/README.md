# Simple Email Service App

This Streamlit application simulates a simple email service. Users can send emails and check their inbox within the application.

## GitHub Repository

You can find the source code for this application in the [GitHub repository](https://github.com/SanjayB29/Simple_Email_Server_Replication.git).

## Structure

The application is divided into four parts:

- `main.py`: The entry point for the application. It provides navigation between sending emails and checking the inbox.
- `send.py`: Handles the functionality to send an email.
- `inbox.py`: Enables users to check their inbox and select an email to view.
- `view_mail.py`: Displays the content of a selected email.
- `__init__.py`: Initializes the application with the necessary setup, such as creating the Excel file to store emails.

## Setup

1. Clone this repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Run the app using `streamlit run main.py`.

## Dependencies

- Streamlit
- Pandas
- Openpyxl (for handling Excel files)

## How to Use

To start the application, execute:

```bash
streamlit run main.py
```

Choose whether to send an email or check your inbox. Follow the prompts to perform the desired action.

## License

This project is open-source and available under the MIT License.

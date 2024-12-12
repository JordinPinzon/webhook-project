# Webhook Flask Application

This is a simple Flask application that receives webhooks and responds with a confirmation message. It is designed to receive `POST` requests on the `/webhook` endpoint and process them.

## Requirements

Before running the application, make sure you have the following:

- Python 3.10 or higher
- Docker (if you want to run the app in a container)

## Installation and Running

### Option 1: Run Locally

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/JordinPinzon/webhook-project.git
    cd webhook-project
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3. Install dependencies from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python app.py
    ```

    The app will be available at `http://127.0.0.1:3000` (or `http://localhost:3000`).

5. To send a `POST` request to the `/webhook` endpoint, you can use `curl` or `Invoke-WebRequest` (on PowerShell):

    **Using `curl`**:
    ```bash
    curl -X POST http://localhost:3000/webhook -H "Content-Type: application/json" -d '{"event": "order_created", "order_id": 12345}'
    ```

    **Using PowerShell**:
    ```powershell
    Invoke-WebRequest -Uri http://localhost:3000/webhook -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"event": "order_created", "order_id": 12345}'
    ```

6. You should see a response like this if everything works correctly:

    ```json
    {
      "status": "Webhook received successfully"
    }
    ```

### Option 2: Run with Docker

If you prefer to run the app inside a Docker container, follow these steps:

1. Build the Docker image:

    ```bash
    docker build -t webhook-flask .
    ```

2. Run the container:

    ```bash
    docker run -p 3000:3000 webhook-flask
    ```

    The app will be available at `http://localhost:3000`.

3. Just like when running locally, you can send a `POST` request to the `/webhook` endpoint using `curl` or PowerShell as shown above.

## Important Files

- `app.py`: The main file of the Flask application.
- `requirements.txt`: Contains the dependencies needed to run the application.
- `Dockerfile`: Contains the instructions to build the Docker container.

## Contributing

If you wish to contribute to this project, please fork the repository, make your changes, and then open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

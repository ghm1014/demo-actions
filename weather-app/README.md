# Weather App

This is a simple web application that displays the current weather in Montreal using Flask and an external weather API.

## Project Structure

```
weather-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── templates
│   │   └── index.html
│   └── static
│       └── style.css
├── requirements.txt
├── Dockerfile
├── kubernetes
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd weather-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python app/main.py
   ```

5. **Access the application:**
   Open your web browser and go to `http://localhost:5000`.

## Usage

The application fetches the current weather data for Montreal and displays it on the main page. You can refresh the page to get the latest weather information.

## Docker

To build and run the application using Docker, use the following commands:

1. **Build the Docker image:**
   ```
   docker build -t weather-app .
   ```

2. **Run the Docker container:**
   ```
   docker run -p 5000:5000 weather-app
   ```

## Kubernetes

To deploy the application on a Kubernetes cluster, apply the configurations in the `kubernetes` directory:

1. **Deploy the application:**
   ```
   kubectl apply -f kubernetes/deployment.yaml
   ```

2. **Expose the service:**
   ```
   kubectl apply -f kubernetes/service.yaml
   ```

## License

This project is licensed under the MIT License.
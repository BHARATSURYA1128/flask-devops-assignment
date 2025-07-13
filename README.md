# Flask DevOps Assignment

This project demonstrates a complete DevOps workflow, encompassing containerization with Docker, CI/CD pipelines via GitHub Actions and CircleCI, and deployment to Kubernetes.

## Key Features & Benefits

*   **Dockerized Flask Application:**  Ensures consistency across different environments.
*   **CI/CD Pipeline:** Automated build, test, and deployment processes.
*   **Kubernetes Deployment:** Scalable and resilient deployment using Kubernetes.
*   **GitHub Actions Integration:** Automates workflow tasks directly within GitHub.
*   **CircleCI Integration:** Alternative CI/CD pipeline for enhanced flexibility.
*   **Simple Web Application:** Easily extendable for more complex features.

## Prerequisites & Dependencies

Before you begin, ensure you have the following installed:

*   **Python 3.6+:** The core language for the Flask application.
*   **Docker:**  For containerizing the application.  Download from [Docker Hub](https://www.docker.com/).
*   **kubectl:**  The Kubernetes command-line tool.  Install as per the [Kubernetes documentation](https://kubernetes.io/docs/tasks/tools/).
*   **Minikube (Optional):** For local Kubernetes development.  Get it from [Minikube's website](https://minikube.sigs.k8s.io/docs/start/).
*   **GitHub Account:** Required for GitHub Actions.
*   **CircleCI Account (Optional):**  Required for CircleCI integration.

## Installation & Setup Instructions

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/BHARATSURYA1128/flask-devops-assignment.git
    cd flask-devops-assignment
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage Examples

### Running the Application Locally

```bash
python app.py
```

Navigate to `http://0.0.0.0:5000` in your web browser to see the "Hello from Flask on Kubernetes via Docker Hub !" message.

### Building and Running the Docker Image

1.  **Build the Docker Image:**

    ```bash
    docker build -t flask-app .
    ```

2.  **Run the Docker Container:**

    ```bash
    docker run -p 5000:5000 flask-app
    ```

Access the application at `http://localhost:5000`.

### Deploying to Kubernetes (using Minikube)

1.  **Start Minikube:**

    ```bash
    minikube start
    ```

2.  **Apply the Kubernetes Deployment and Service:**

    ```bash
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    ```

3.  **Access the Service:**

    Find the service URL:

    ```bash
    minikube service flask-service --url
    ```

    Open the provided URL in your browser.

## Configuration Options

*   **Port:** The Flask application runs on port 5000 by default. You can change this in the `app.py` file.

*   **Environment Variables:**  You can use environment variables to configure the application further.  For example, you could set a `FLASK_ENV` variable for different environments.  These would be defined in your Kubernetes deployment YAML.

## Project Structure

```
├── .circleci               # CircleCI configuration files
│   └── config.yml         # CircleCI pipeline definition
├── .github                # GitHub Actions workflow directory
│   └── workflows          # Contains workflow files
│       └── main.yml      # GitHub Actions CI/CD workflow
├── Dockerfile             # Dockerfile for building the application image
├── README.md              # This README file
├── app.py                 # The main Flask application file
├── k8s                    # Kubernetes deployment files
│   ├── deployment.yaml   # Kubernetes deployment configuration
│   └── service.yaml      # Kubernetes service configuration
└── requirements.txt       # Python dependencies
```

## GitHub Actions Workflow

The `.github/workflows/main.yml` file defines the CI/CD pipeline that automates the build, test, and deployment of the application.  It is triggered on pushes to the `main` branch.

## CircleCI Configuration

The `.circleci/config.yml` file defines an alternative CI/CD pipeline using CircleCI.



## License Information

This project has no specified license. All rights are reserved by the owner.

## Acknowledgments

*   Flask - For providing the web framework.
*   Docker - For containerization technology.
*   Kubernetes - For container orchestration.
*   GitHub Actions and CircleCI - For CI/CD automation.

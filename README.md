\# 🚀 Flask DevOps Assignment -- DevOps CI/CD + Kubernetes

This project is a complete DevOps assignment implementation involving:

\- A Flask web application - Docker containerization - CI/CD using
GitHub Actions and CircleCI - Kubernetes deployment using Minikube -
Monitoring integration with Datadog

\> ✅ Goal: Demonstrate a full CI/CD pipeline and deployment workflow
from local dev to Kubernetes using free and open tools.

\-\--

\## 📁 Project Structure

\`\`\`bash better-flask-assignment/ ├── app.py \# Flask web app ├──
requirements.txt \# Python dependencies ├── Dockerfile \# Image build
instructions ├── .github/workflows/ \# GitHub Actions workflow ├──
.circleci/config.yml \# CircleCI pipeline └── k8s/ \# Kubernetes
manifests ├── deployment.yaml └── service.yaml 🔧


What I Built 🐍 Flask
Application A simple Flask server with basic routes, including a /crash
route intended for error tracking (planned for Bugsnag).

🐳 Docker & Docker Hub Created a Dockerfile to containerize the Flask
app

Built and pushed the image to Docker Hub

bash Copy Edit docker build -t \<your-username\>/better-flask-assignment
. docker push \<your-username\>/better-flask-assignment ⚙️ CI/CD
Pipeline GitHub Actions: Lint and test the Flask app on every push

CircleCI: Build the Docker image and push it to Docker Hub

Faced challenges with Docker version compatibility on CircleCI, resolved
by updating the executor and simplifying the config.

☸️ Kubernetes with Minikube Used Minikube for a local Kubernetes cluster

Wrote Deployment and Service manifests

Deployed the app with:

bash Copy Edit kubectl apply -f k8s/ kubectl get pods kubectl
port-forward svc/flask-app 5000:5000 Tested locally at:
http://localhost:5000

📊 Monitoring with Datadog Installed the Datadog Agent with Helm

Configured to Japan region (datadoghq.jp)

Verified node, pod, and cluster metrics in the Datadog dashboard

❌ What Didn\'t Work Intended to integrate Bugsnag for error tracking
using the /crash route

Couldn't complete Bugsnag setup due to time constraints

✅ What I Learned How to set up CI/CD workflows using GitHub Actions and
CircleCI

Troubleshooting Docker build failures in CI environments

Creating Kubernetes manifests and running local clusters with Minikube

How to configure and verify observability with Datadog

Real-world debugging of pipeline errors and container issues

🪛 Future Improvements Complete Bugsnag integration for Flask error
tracking

Replace Minikube with a managed Kubernetes provider (GKE, EKS)

Add Helm chart packaging for easier deployment

Configure Horizontal Pod Autoscaling

Enable full Datadog APM and logs

🙌 Thanks Thanks for reviewing this project! Please feel free to ask me
more about any step, error, or decision I made during this assignment.

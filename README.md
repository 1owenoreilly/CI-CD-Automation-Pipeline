# CI-CD-Automation-Pipeline

A Flask app with arithmetic endpoints (`/add`, `/multiply`), automated CI/CD pipeline using GitHub Actions, Docker deployment to Docker Hub, and Slack notifications.

## Setup
1. Clone the repo: `git clone https://github.com/1owenoreilly/CI-CD-Automation-Pipeline`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. Test endpoints: `curl "http://localhost:5000/add?a=2&b=3"`

## CI/CD Pipeline
- Triggers on push/pull requests to `main`.
- Runs tests (`pytest`), linting (`flake8`), builds/pushes Docker image to Docker Hub.
- Sends Slack notifications for build status.

## Endpoints
- `GET /add?a=<float>&b=<float>`: Returns sum of `a` and `b`.
- `GET /multiply?a=<float>&b=<float>`: Returns product of `a` and `b`.

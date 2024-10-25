Welcome to the Maintenance Log Repo!

This is the source to my little labor of love, an application in which users can track their maintenance tasks and spending!

Originally built on top of AWS Amplify's suite of technology and iac,
I wanted to further develop my skills by rebuilding the application from the ground up using my own RESTful API, hosting, CICD, ect
but still keep some key services that AWS provides like DynamoDB, ECS, Cognito, and CloudFormations.

Below is a roadmap for the implementation of this application:

## Phase 1: Planning & Setup

1. Project Goals:

- Build a README to explain project and this roadmap (if you're reading this, you're here!) DONE 10/24/24
- Define objectives: containerization, REST API, CI/CD, cloud deployment on ECS/EKS.
- Sketch architecture: React frontend, Python backend, AWS services for deployment.

2. Tech Stack:

- Frontend: React (JavaScript)
- Backend: Flask (Python) for REST APIs
- Database: DynamoDB (NoSQL)
- AWS Services: ECS, S3, API Gateway, CloudWatch
- Containerization: Docker
- CI/CD: GitHub Actions
- Infrastructure as Code (IaC): Terraform or CloudFormation

## Phase 2: Develop Core Application

1. Backend with REST APIs (Flask):

- Build CRUD REST API to manage vehicles and maintenance logs.

2. Frontend (React):

- Integrate frontend with backend API for vehicle management.

3. Database:

- Set up DynamoDB.

## Phase 3: Containerization

1. Dockerize the backend and frontend.
2. Use Docker Compose to manage multiple containers locally (backend, frontend, and database).
3. Test locally to ensure everything works as expected.

## Phase 4: CI/CD with GitHub Actions

1. Set up GitHub Actions for CI/CD pipeline:

- Automate testing, building, and pushing Docker images to AWS ECR.
- Deploy to ECS/Fargate for container orchestration.

## Phase 5: Cloud Deployment & Orchestration

1. Deploy backend and frontend containers to AWS ECS (or EKS).
2. Use API Gateway for handling REST API requests.
3. Set up CloudWatch for monitoring and logging.

## Phase 6: Infrastructure as Code (IaC)

1. Use Terraform or AWS CloudFormation to provision infrastructure as code.
2. Automate the creation of ECS clusters, API Gateway, and other AWS resources.

## Phase 7: Monitoring & Logging

1. Set up AWS CloudWatch for logging and monitoring services.
2. Set up alerts based on usage metrics to notify of any issues.

## Phase 8: Security & Optimization

1. Use AWS Cognito for secure authentication and authorization.
2. Optimize performance by implementing auto-scaling and caching.

## Phase 9: Go Live!

1. Lets host this, connect it to my domain and get it out onto the internet!

Wow thats quite the roadmap, some of this stuff I have played around with before, but others will be a new experience to me, so I am diving head first.
I may change some of this roadmap to fit the applications needs, but plan to use this readme as a log of my changes and development,
so ill be sure to note anything that didn't work out or was exchanged for a different piece of technology
Hopefully if you're reading this, the site is operational and it was all a success! (and is hosted on https://deserted-dunes.com) :)

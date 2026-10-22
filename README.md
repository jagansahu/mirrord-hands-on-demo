# mirrord Hands-On Demo
Playing around with MetalBear's mirrord using Python, Docker, and Kubernetes.

## Why I Built This
I wanted to understand the product from a developer's perspective. I built a small Payment Service and experimented with how mirrord changes the Kubernetes development workflow. 

## Tech Stack
- Python
- Docker
- Kubernetes (Kind)
- mirrord
- kubectl

## The Problem
In a traditional Kubernetes workflow, testing a code change often requires:

1. Building a Docker image
2. Loading or pushing the image
3. Deploying the updated application
4. Testing and debugging
5. Repeating for subsequent changes

mirrord helps developers test local code against Kubernetes environments without repeatedly deploying it.

## My Experiment

I built a simple Python Payment Service that calculates a total payment amount by adding a fee to a base amount.

Version 1 — Deployed in Kubernetes

Base amount: $100
Fee: $10
Total: $110

I then modified my local Python code, reducing the fee from $10 to $5, which changed the total from $110 to $105.

Version 2 — Running Locally

Base amount: $100
Fee: $5
Total: $105

What I Wanted to Test:

Normally, testing this change in Kubernetes would require rebuilding the Docker image and redeploying the updated Payment Service.

Instead, I wanted to see whether mirrord could let me test my modified local code against the existing Kubernetes environment without rebuilding or redeploying anything.

I tested two scenarios:

Mirror Mode: Could my local Payment Service process the same HTTP request as the Kubernetes service while the client still received the original $110 response?

Steal Mode: Could my local Payment Service take over the request and return the updated $105 response directly to the client?

The goal: Understand how mirrord helps developers test and debug code changes faster by eliminating repeated build-and-deploy cycles.

I explored two mirrord modes (Mirror Mode and Steal Mode):

### Mirror Mode
Both the deployed Kubernetes service and my local Python application receive the request.
The client receives the Kubernetes response ($110), while the local application calculates $105.

<img width="1146" height="118" alt="unknown" src="https://github.com/user-attachments/assets/e760fc9b-a917-42ff-ab82-9050832efdb8" />


### Steal Mode
mirrord redirects the request to my local Python application.
The client receives the local response ($105) without requiring a new Kubernetes deployment.

<img width="1146" height="118" alt="unknown" src="https://github.com/user-attachments/assets/c217ffd9-65db-4120-8fed-050d496da2f5" />


## Key Takeaways

**Mirror mode:** Debug local code using copies of Kubernetes traffic without changing the client's response.

**Steal mode:** Route matching Kubernetes requests to locally running code and return its response.

**Developer benefit:** Reduce the build-deploy-debug cycle and make development against Kubernetes environments easier.

## What I learned.

This experiment helped me understand the challenges engineering teams face when developing distributed applications. It also helped me understand the difference between mirror and steal mode (which is the main thing I wanted to understand as a developer).

Potential customer pain points include:

- Slow development cycles caused by repeated deployments
- Difficulty debugging microservices locally
- Complex Kubernetes development environments

## What I'd Explore Next

- Debugging with VS Code breakpoints
- Running multiple connected microservices
- Exploring mirrord for Teams


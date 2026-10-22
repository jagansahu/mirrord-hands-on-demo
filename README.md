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

- Base amount: $100
- Fee: $10
- Total: $110

I then modified my local Python code, reducing the fee from $10 to $5, which changed the total from $110 to $105.

Version 2 — Running Locally

- Base amount: $100
- Fee: $5
- Total: $105

## What I Wanted to Test

Normally, if I change my Payment Service code, I need to rebuild the Docker image and redeploy it to Kubernetes to test the updated version.

I wanted to see if **mirrord could let me test my updated code locally without rebuilding or redeploying anything.**

To test this, I changed the payment fee from $10 to $5 in my local Python code.

- **Kubernetes version (original):** $100 + $10 fee = **$110**
- **Local version (modified):** $100 + $5 fee = **$105**

I then tested two mirrord modes to see what would happen when I sent the same HTTP request.

### 1. Mirror Mode — Testing Without Changing the Client's Response

In mirror mode, mirrord sends a copy of the incoming request to my local Python application.

Both versions process the request:

- Kubernetes calculates $110.
- My local Python application calculates $105.
- **The client (`curl`) still receives $110**, because the original Kubernetes service handles the response.

<img width="1146" height="118" alt="unknown" src="https://github.com/user-attachments/assets/42f32531-5049-4ba9-aeb4-96cd315d8475" />


This showed me how developers can debug modified code locally without changing the response users receive.

### 2. Steal Mode — Testing My Updated Code as if It Were Deployed

In steal mode, mirrord redirects the incoming request to my local Python application instead of letting the Kubernetes version handle it.

- My local Python application calculates $105.
- **The client (`curl`) receives $105**, even though Kubernetes still has the original $110 version deployed.

<img width="1146" height="118" alt="unknown" src="https://github.com/user-attachments/assets/3ef30a06-f418-4be2-8518-28b2b6590bf9" />

This showed me how developers can test updated code against a Kubernetes environment without rebuilding or redeploying their application.

## Key Takeaway

**Mirror mode lets developers observe and debug changes. Steal mode lets developers test their changes as if they were deployed.**

Both can save developers time by reducing repeated Docker builds and Kubernetes deployments.

## What I learned.

This experiment helped me understand the challenges engineering teams face when developing distributed applications and how much time mirrord could potentially save me. It also helped me understand the difference between mirror and steal mode (which is the main thing I wanted to understand as a developer).

Potential customer pain points include:

- Slow development cycles caused by repeated deployments
- Difficulty debugging microservices locally
- Complex Kubernetes development environments

## What I'd Explore Next

- Debugging with VS Code breakpoints
- Running multiple connected microservices
- Exploring mirrord for Teams


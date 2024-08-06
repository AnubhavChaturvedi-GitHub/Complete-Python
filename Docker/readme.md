# Docker Overview

## Introduction to Docker
Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications.

## Containers vs Virtual Machines
### Containers
- **Lightweight:** Share the same OS kernel and only require the application and its dependencies.
- **Fast Start-up:** Containers can start almost instantly.
- **Resource Efficient:** Containers use fewer resources compared to VMs.

### Virtual Machines (VMs)
- **Heavyweight:** Each VM includes a full copy of an operating system, the application, necessary binaries, and libraries.
- **Slower Start-up:** VMs take longer to boot up.
- **Resource Intensive:** VMs require more resources due to the OS overhead.

## Docker Architecture
Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers.

### Components:
- **Docker Client:** The command-line interface users interact with.
- **Docker Daemon:** The background service running on the host that manages building, running, and distributing Docker containers.
- **Docker Registry:** Stores Docker images (e.g., Docker Hub).

## Installing Docker
Docker can be installed on various operating systems including Linux, Windows, and macOS. Detailed installation guides can be found on the [Docker official documentation](https://docs.docker.com/get-docker/).

### Basic Installation Steps (Linux):
```sh
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

sudo systemctl start docker
sudo systemctl enable docker
```

## Working with Docker Containers
### Basic Commands:
- **Run a Container:** `docker run -it --name my_container ubuntu`
- **List Containers:** `docker ps`
- **Stop a Container:** `docker stop my_container`
- **Remove a Container:** `docker rm my_container`

### Dockerfile:
A `Dockerfile` is a script containing a series of commands to form an image.
```Dockerfile
# Sample Dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip
COPY . /app
WORKDIR /app
CMD ["python3", "app.py"]
```

## Benefits of Containerization
- **Portability:** Consistent environments from development to production.
- **Scalability:** Easily scale applications horizontally.
- **Isolation:** Isolates applications from each other on the same hardware.

## Introduction to Swarm Mode and Microservices
### Swarm Mode:
Docker Swarm is Docker’s native clustering and orchestration tool. Swarm turns a pool of Docker hosts into a single, virtual Docker host.

### Microservices:
Microservices is an architectural style that structures an application as a collection of loosely coupled services. Each service is:
- **Highly Maintainable and Testable**
- **Independently Deployable**
- **Organized around Business Capabilities**

## Conclusion
Docker revolutionizes the way we develop, ship, and run applications. With the concepts of containers, Swarm mode, and microservices, Docker provides powerful tools to manage and scale applications efficiently.

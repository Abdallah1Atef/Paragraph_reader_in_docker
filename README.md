# Text Processing with Docker

## Overview
This project demonstrates containerization using Docker to create an isolated Python environment for text processing. It includes a Python script that reads a text file, removes stop words, and calculates word frequencies. The project serves as an educational tool to understand:

- Docker containerization and its components (Dockerfile, images, containers)
- Dependency management in isolated environments
- Batch text processing workflows

## Features
- **Dockerized Python Environment**: Pre-configured with all dependencies to ensure consistent execution across systems.
- **Text Processing Script**:
  - Reads a text file (`random_paragraphs.txt`)
  - Removes common English stop words using NLTK
  - Generates word frequency counts
  - Exports results to a CSV file (`word_counts.csv`)
- **Reproducible Builds**: Dockerfile specifies exact environment configuration

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/) (optional)

## Getting Started

## Project Structure
.
├── Dockerfile            # Docker configuration for Python environment
├── t2.py                 # Text processing script
├── requirements.txt      # Python dependencies (nltk)
├── random_paragraphs.txt # Input text file (mount into container)
└── README.md             # Documentation
### 1. Clone the Repository
```bash
git clone https://github.com/Abdallah1Atef/Text_Processing_with_Docker.git
cd text-processing-docker
```

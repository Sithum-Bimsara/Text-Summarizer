# Text Summarizer: Gradio-based AI Application

## Table of Contents
- [Introduction](#introduction)
- [What is Gradio?](#what-is-gradio)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Requirements](#requirements)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Text Summarizer is a lightweight Gradio-based application for summarizing text using Hugging Face's Transformers library. It leverages the `sshleifer/distilbart-cnn-12-6` model for summarization tasks.

This project demonstrates how to build an interactive user interface for AI applications using Gradio and deploy it on Hugging Face Spaces.

## What is Gradio?
Gradio is a Python library for building interactive user interfaces for machine learning models. It simplifies the process of creating web-based applications for AI models, allowing users to interact with models directly from their browsers. 

### Key Features of Gradio:
- Quick prototyping of ML applications.
- Shareable links for live demos.
- Supports various input and output types, including text, images, and audio.

## Project Structure
```
GenAIProject/ 
│
├── installation/
│    ├── requirements.txt             # Dependencies for the project
│
├── models/
│    ├── (Downloaded model files will be stored here)
│
├── text-summarization/
│    ├── textsummery.py               # Core application script
│                            
├── requirements.txt                  # List of dependencies
├── venv/                             # Virtual environment for the project
```

## Prerequisites
Before setting up the project, ensure the following tools are installed:
- Python 3.8+
- pip (Python package installer)
- Virtual environment tools (e.g., `venv` or `virtualenv`)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Sithum-Bimsara/Text-Summarizer.git
cd text-summarizer
```
### 2. Create a Virtual Environment
If you haven't already created a virtual environment (venv), follow these steps to set it up:

On Windows:
```bash
python -m venv venv
```
On macOS/Linux:
```bash
python3 -m venv venv
```
### 3. Activate the Virtual Environment

On Windows:
```bash
.\venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. First-Time Model Download
If running the application for the first time, download the model :
```python
text_summery = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", torch_dtype=torch.bfloat16)
```
Once downloaded, move the model files to the `models` directory and comment above codes sippets and uncomment folllowing code snippets.

Default download location(Windows): `C:\Users\<User>\.cache\huggingface\hub`

Update the `model_path` variable in the script to point to the `models` directory or cut and paste the model inside the model file and directly use the code at repo:
```python
model_path = "./models/sshleifer-distilbart-cnn-12-6"
text_summery = pipeline("summarization", model=model_path, torch_dtype=torch.bfloat16)
```

## Running the Application

### Local Deployment
Run the application locally:
```bash
python text-summarization/textsummery.py
```
Gradio will provide a local URL and a shareable link for accessing the app in your browser.

### Hugging Face Deployment
Deploy the app on Hugging Face Spaces:
1. Create a new Space on Hugging Face ([Hugging Face Spaces](https://huggingface.co/spaces)).
2. Upload all project files, including the model, to the Space.
3. Set `requirements.txt` to include:
   ```
   torch
   transformers
   gradio
   ```
4. Start the Space to see the live performance at:
   [Text Summarizer Live Demo](https://huggingface.co/spaces/Sithum-Bimsara/TextSummarizer)

## Requirements
- Python 3.8+
- `torch`
- `transformers`
- `gradio`

## Troubleshooting
- **Model Path Issues**: Ensure the model files are correctly placed in the `models` directory and the `model_path` variable points to it.
- **Gradio Link Not Working**: Check your firewall settings or ensure you have a stable internet connection.

## Contributing
Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

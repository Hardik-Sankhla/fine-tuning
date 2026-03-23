# Fine-Tuning Workflows and Recipes

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive repository containing reproducible examples, training scripts, data preprocessing pipelines, and documentation for fine-tuning open-source language models using Parameter-Efficient Fine-Tuning (PEFT) techniques like LoRA, QLoRA, and related methods.

## 🚀 Features

- **LoRA & QLoRA Fine-Tuning**: Efficient parameter-efficient fine-tuning for large language models
- **Nemotron-Style Models**: Specialized workflows for reasoning and instruction-tuned models
- **Reproducible Examples**: Ready-to-run scripts and notebooks for various fine-tuning scenarios
- **Data Preprocessing**: Tools for preparing datasets for instructional and non-instructional fine-tuning
- **Evaluation Scripts**: Comprehensive evaluation and inference pipelines
- **Modular Architecture**: Well-organized codebase with separate modules for training, data, and utilities

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Course Content](#course-content)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## 🛠 Installation

### Prerequisites
- Python 3.10 or higher
- GPU recommended for training (CUDA-compatible)

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd fine-tuning
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Quick Start

1. Configure your training parameters in `configs/train.yaml`
2. Run the training script:
   ```bash
   python scripts/train.py
   ```

## 📁 Project Structure

```
fine-tuning/
├── finetuning/         # Main Python package for fine-tuning
├── tools/              # Helper scripts and utilities
├── configs/            # YAML configuration files for experiments
├── notebooks/          # Interactive examples and demonstrations
├── tutorials/          # Course content and session materials
├── data/               # Dataset storage (gitignored)
├── models/             # Saved model checkpoints
├── experiments/        # Training runs, logs, and results
├── docs/               # Documentation and guides
└── tests/              # Unit and integration tests
```

## 💡 Usage

### Basic Fine-Tuning
1. Prepare your dataset in the `data/` directory
2. Modify configuration in `configs/train.yaml`
3. Execute training:
   ```bash
   python scripts/train.py
   ```

### Custom Training Scripts
Explore the `tools/` directory for specialized training workflows including:
- LoRA fine-tuning
- QLoRA for memory-efficient training
- Preference alignment with DPO
- Multimodal fine-tuning

### Experiments and Models
- Training runs and logs are stored in `experiments/`
- Fine-tuned models are saved in `models/`
- Use configurations from `configs/` to customize training

### Notebooks
Interactive Jupyter notebooks in the `notebooks/` directory provide:
- Step-by-step tutorials
- Visualization of training metrics
- Inference examples

## 📚 Course Content

This repository accompanies the comprehensive "5-Day Gen AI Intensive Course" covering advanced fine-tuning techniques. Below are the session directories:

- [01 Introduction & Course Syllabus](tutorials/01-Introduction-and-Course-Syllabus/README.md)
- [02 LLM Training Pipeline Overview](tutorials/02-LLM-Training-Pipeline-Overview/README.md)
- [03 Parameter Level Fine-Tuning: Full vs. Partial](tutorials/03-Parameter-Level-Fine-Tuning-Full-vs.-Partial/README.md)
- [04 Partial Fine-Tuning: Old School vs. Advanced Methods](tutorials/04-Partial-Fine-Tuning-Old-School-vs.-Advanced-Methods/README.md)
- [05 Parameter Efficient Fine-Tuning (PEFT): LoRa & QLoRa](tutorials/05-Parameter-Efficient-Fine-Tuning-PEFT-LoRa-and-QLoRa/README.md)
- [06 Advanced PEFT Techniques: DoRA, IA3, & BitFit](tutorials/06-Advanced-PEFT-Techniques-DoRA-IA3-and-BitFit/README.md)
- [07 Data Level Fine-Tuning: Instructional vs. Non-Instructional](tutorials/07-Data-Level-Fine-Tuning-Instructional-vs.-Non-Instructional/README.md)
- [08 Preference Based Learning: RLHF & DPO](tutorials/08-Preference-Based-Learning-RLHF-and-DPO/README.md)
- [09 Deep Dive: Unsupervised Pre-training (Self-Supervised Learning)](tutorials/09-Deep-Dive-Unsupervised-Pre-training-Self-Supervised-Learning/README.md)
- [10 Deep Dive: Non-Instructional Fine-Tuning & Domain Adaptation](tutorials/10-Deep-Dive-Non-Instructional-Fine-Tuning-and-Domain-Adaptation/README.md)
- [11 Data Preparation for Non-Instructional Fine-Tuning](tutorials/11-Data-Preparation-for-Non-Instructional-Fine-Tuning/README.md)
- [12 Deep Dive: Instructional Fine-Tuning & Chatbot Creation](tutorials/12-Deep-Dive-Instructional-Fine-Tuning-and-Chatbot-Creation/README.md)
- [13 Deep Dive: Preference Alignment with Human Feedback](tutorials/13-Deep-Dive-Preference-Alignment-with-Human-Feedback/README.md)
- [14 Family-wise LLM Breakdown: Llama, GPT, Gemini, & DeepSeek](tutorials/14-Family-wise-LLM-Breakdown-Llama-GPT-Gemini-and-DeepSeek/README.md)
- [15 Practical Setup: Essential Libraries & GPU Connection](tutorials/15-Practical-Setup-Essential-Libraries-and-GPU-Connection/README.md)
- [16 Working with Pre-built vs. Custom Data Sets](tutorials/16-Working-with-Pre-built-vs.-Custom-Data-Sets/README.md)
- [17 Model Selection, Tokenization, & Padding Explained](tutorials/17-Model-Selection-Tokenization-and-Padding-Explained/README.md)
- [18 Defining Training Arguments: Epochs, Learning Rate, & Batch Size](tutorials/18-Defining-Training-Arguments-Epochs-Learning-Rate-and-Batch-Size/README.md)
- [19 Executing Fine-Tuning with LoRa](tutorials/19-Executing-Fine-Tuning-with-LoRa/README.md)
- [20 Post-Training: Model Prediction & Inferencing](tutorials/20-Post-Training-Model-Prediction-and-Inferencing/README.md)
- [21 Part 2: Comprehensive Guide to Instructional Fine-Tuning](tutorials/21-Part-2-Comprehensive-Guide-to-Instructional-Fine-Tuning/README.md)
- [22 Loading & Unzipping Previous Training Checkpoints](tutorials/22-Loading-and-Unzipping-Previous-Training-Checkpoints/README.md)
- [23 Masking Labels for Improved Instructional Responses](tutorials/23-Masking-Labels-for-Improved-Instructional-Responses/README.md)
- [24 Part 3: Preference Alignment & DPO Training](tutorials/24-Part-3-Preference-Alignment-and-DPO-Training/README.md)
- [25 Preference Optimization Techniques: RLHF, RL AIF, & DPO](tutorials/25-Preference-Optimization-Techniques-RLHF-RL-AIF-and-DPO/README.md)
- [26 DPO Intuition: Understanding the Training Loss Formula](tutorials/26-DPO-Intuition-Understanding-the-Training-Loss-Formula/README.md)
- [27 Practical DPO Implementation & Avoiding LoRa Stacking](tutorials/27-Practical-DPO-Implementation-and-Avoiding-LoRa-Stacking/README.md)
- [28 Introduction to the Llama Factory Project](tutorials/28-Introduction-to-the-Llama-Factory-Project/README.md)
- [29 Setup & Setting up Llama Factory via GitHub](tutorials/29-Setup-and-Setting-up-Llama-Factory-via-GitHub/README.md)
- [30 Using Llama Factory Web UI: Selecting Models & Data](tutorials/30-Using-Llama-Factory-Web-UI-Selecting-Models-and-Data/README.md)
- [31 Training via CLI: Configuration via YAML Files](tutorials/31-Training-via-CLI-Configuration-via-YAML-Files/README.md)
- [32 Unsloth Framework: Achieving 2x Faster Training](tutorials/32-Unsloth-Framework-Achieving-2x-Faster-Training/README.md)
- [33 Inside Unsloth: Custom Kernels & Memory Efficiency](tutorials/33-Inside-Unsloth-Custom-Kernels-and-Memory-Efficiency/README.md)
- [34 Practical Walkthrough: Fine-Tuning with Unsloth](tutorials/34-Practical-Walkthrough-Fine-Tuning-with-Unsloth/README.md)
- [35 Enterprise Fine-Tuning via OpenAI API](tutorials/35-Enterprise-Fine-Tuning-via-OpenAI-API/README.md)
- [36 Preparing & Validating JSONL Data for OpenAI](tutorials/36-Preparing-and-Validating-JSONL-Data-for-OpenAI/README.md)
- [37 Creating and Monitoring OpenAI Fine-Tuning Jobs](tutorials/37-Creating-and-Monitoring-OpenAI-Fine-Tuning-Jobs/README.md)
- [38 Google Cloud Vertex AI: Fine-Tuning Gemini Models](tutorials/38-Google-Cloud-Vertex-AI-Fine-Tuning-Gemini-Models/README.md)
- [39 Data Management in Google Cloud Storage Buckets](tutorials/39-Data-Management-in-Google-Cloud-Storage-Buckets/README.md)
- [40 Embedding Fine-Tuning Masterclass](tutorials/40-Embedding-Fine-Tuning-Masterclass/README.md)
- [41 Multimodal AI: Image, Video, & Audio Modalities](tutorials/41-Multimodal-AI-Image-Video-and-Audio-Modalities/README.md)
- [42 Vision Transformer (ViT) Architecture Deep Dive](tutorials/42-Vision-Transformer-ViT-Architecture-Deep-Dive/README.md)
- [43 Keyword Search vs. Semantic Similarity](tutorials/43-Keyword-Search-vs.-Semantic-Similarity/README.md)
- [44 Step-by-Step: The Modern Text Embedding Process](tutorials/44-Step-by-Step-The-Modern-Text-Embedding-Process/README.md)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to get started.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Hardik Sankhla**
- Email: datascientist.hardiksankhla@gmail.com
- LinkedIn: [Your LinkedIn Profile]

---

⭐ If you find this repository helpful, please give it a star! 

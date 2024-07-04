# Speech Recognition System

This project aims to develop a Speech Recognition System using four different approaches:

1. Hidden Markov Model (HMM) Based Approach
2. Voice Command Driven Automation (VCDA)
3. Machine Learning Approach
4. Lexicon Based Approach

The goal is to create a user-friendly, secure, and efficient system for smart home automation using voice commands.

## Table of Contents

- [Introduction](#introduction)
- [Approaches](#approaches)
  - [HMM Based Approach](#hmm-based-approach)
  - [VCDA](#vcda)
  - [Machine Learning Approach](#machine-learning-approach)
  - [Lexicon Based Approach](#lexicon-based-approach)
- [Usage](#usage)
- [Dataset](#dataset)

## Introduction

In the era of smart living and smart devices, artificial intelligence (AI) and Internet-of-Things (IoT) technologies have revolutionized human-machine interactions. This project targets the integration of voice commands for controlling smart devices, enhancing human living standards, and bringing efficiency and convenience while addressing security issues.

The main objective of this project is to implement a voice recognition system adapted for smart home activities, making device integration seamless, secure, and user-friendly.

## Approaches

### HMM Based Approach

The Hidden Markov Model (HMM) approach involves the following components:

- **Signal Processing Module**: Uses Mel-Frequency Cestrum Coefficients (MFCC) to extract feature vectors from voice commands.
- **Acoustic Model**: Utilizes VQ-Codebooks based on training data to extract the exact voice through Context Dependent Triphone HMM.
- **Output Phase**: Translates the processed voice data into commands for executing tasks.

### VCDA

The Voice Command Driven Automation (VCDA) approach uses advanced voice processing techniques and Natural Language Processing (NLP) to control IoT devices through voice commands. This approach includes:

- **Voice Processing Client**: Recognizes and processes voice commands using NLP algorithms.
- **Hybrid and Companion Clients**: Enhance the voice control features for various smart home devices.

### Machine Learning Approach

The Machine Learning approach leverages adaptive machine learning models to enhance voice recognition and smart home control. Key components include:

- **Speech Recognition Platform**: Uses machine learning models for voice command processing.
- **IoT Framework**: Integrates various smart devices through an IoT network.
- **Machine Learning Models**: Train models to predict user behavior and control smart devices.

### Lexicon Based Approach

The Lexicon Based approach focuses on translating voice commands into text and extracting keywords to control smart home devices. Components include:

- **Audio Input Devices**: Capture voice commands.
- **Text Conversion and Tokenization**: Process voice commands into text and extract keywords.
- **Lexicon System**: Uses a predefined lexicon to control smart home appliances.


## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/speech-recognition-system.git
   cd speech-recognition-system

2. Install The necessary python libraries using pip command:
   ```bash
   pip install LIBRARY_NAME

3. Open All the .ipynb files using jupyter notebook


Dataset

The dataset used for training and testing the models is available at: https://drive.google.com/drive/folders/1ldTvTbjUIhiv6yWt2FK8uawGjlY3sw78?usp=sharing

---
title: AI LearnMate Generator
emoji: ⚡
colorFrom: red
colorTo: blue
sdk: gradio
sdk_version: 6.0.0
app_file: app.py
pinned: false
license: mit
short_description: Custom AI study guides, quizzes & summaries
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
# AI LearnMate Generator

**Live demo:** [Hugging Face Spaces](https://huggingface.co/spaces/mbalimadlala/AI-LearnMate-Generator)

## Overview

AI LearnMate Generator is a content generation tool built with Streamlit and hosted on Hugging Face Spaces. It helps users create educational or creative content using NLP models.

## Features

- Text generation using Hugging Face transformers  
- Customizable prompts and output length  
- Responsive Streamlit interface  
- Hosted on Hugging Face Spaces for easy access

## Tech Stack

- Python  
- Streamlit  
- Hugging Face Transformers  
- Hugging Face Spaces

## Setup

```bash
git clone https://github.com/mbalizzy/ai-learnmate-generator.git
cd ai-learnmate-generator
pip install -r requirements.txt
streamlit run app.py

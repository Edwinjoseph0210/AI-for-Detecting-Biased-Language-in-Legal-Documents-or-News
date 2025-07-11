# AI for Detecting Biased Language in Legal Documents or News

## Overview
This project is an AI-powered tool that detects and explains biased or manipulative language in legal documents, news articles, or government orders. It highlights emotionally charged, unfair, or politically skewed language and provides explanations and suggestions for neutrality.

## Features
- Accepts legal/news text input (copy-paste or file upload)
- Highlights emotionally charged, unfair, or politically skewed language using NLP
- Explains the type of bias (e.g., omission, exaggeration, stereotyping) using interpretable AI methods
- Provides neutrality suggestions or rewrites (optional)
- Uses HuggingFace Transformers (BERT, RoBERTa), spaCy for NER, LIME/SHAP for explainability
- Streamlit frontend for easy interaction

## Project Structure
```
├── app.py                # Streamlit frontend
├── bias_detector.py      # NLP model logic for bias detection
├── explain.py            # LIME/SHAP explainability logic
├── utils.py              # Helper functions (e.g., file reading)
├── requirements.txt      # Python dependencies
├── data/                 # Datasets for training/fine-tuning
├── models/               # Saved/fine-tuned models
└── README.md             # Project documentation
```

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```
2. (Optional) Place your fine-tuned model in the `models/` directory.
3. (Optional) Add your dataset to the `data/` directory.

## Usage
Run the Streamlit app:
```bash
streamlit run app.py
```

- Upload a `.txt` or `.docx` file, or paste your text.
- The app will highlight biased phrases and provide explanations and suggestions.

## Notes
- The current implementation uses placeholder logic for demo purposes. Replace with your fine-tuned model and real explainability methods for production use.
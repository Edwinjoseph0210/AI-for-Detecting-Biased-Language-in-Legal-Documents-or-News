import spacy
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Placeholder: Replace with your fine-tuned model
MODEL_NAME = "roberta-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

BIAS_LABELS = ["neutral", "exaggeration", "omission", "stereotyping", "emotionally_charged", "politically_skewed"]

# Dummy bias detection for demo
def detect_bias(text):
    doc = nlp(text)
    results = []
    for sent in doc.sents:
        # Placeholder: Replace with model inference
        if any(word in sent.text.lower() for word in ["clearly", "obviously", "never", "always"]):
            results.append({
                "phrase": sent.text,
                "bias_type": "exaggeration",
                "start": sent.start_char,
                "end": sent.end_char,
                "suggestion": sent.text.replace("clearly", "").replace("obviously", "")
            })
    return results

def highlight_text(text, bias_results):
    # Highlight biased phrases in HTML
    offset = 0
    for res in bias_results:
        start = res["start"] + offset
        end = res["end"] + offset
        phrase = text[start:end]
        highlight = f'<span style="background-color: #ffcccc" title="{res["bias_type"]}">{phrase}</span>'
        text = text[:start] + highlight + text[end:]
        offset += len(highlight) - len(phrase)
    return text 
# Placeholder for LIME/SHAP explainability

def explain_bias(result):
    # In a real implementation, use LIME/SHAP to explain model prediction
    if result["bias_type"] == "exaggeration":
        return "This phrase uses strong, absolute terms that may exaggerate the claim."
    elif result["bias_type"] == "omission":
        return "This phrase omits important context, which may mislead the reader."
    elif result["bias_type"] == "stereotyping":
        return "This phrase generalizes or stereotypes a group or individual."
    elif result["bias_type"] == "emotionally_charged":
        return "This phrase uses emotional language to influence opinion."
    elif result["bias_type"] == "politically_skewed":
        return "This phrase reflects a political bias."
    else:
        return "No significant bias detected." 
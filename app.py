import streamlit as st
from bias_detector import detect_bias, highlight_text
from explain import explain_bias

st.title("AI for Detecting Biased Language in Legal Documents or News")

uploaded_file = st.file_uploader("Upload a document", type=["txt", "docx"])
text_input = st.text_area("Or paste your text here:")

if uploaded_file:
    if uploaded_file.name.endswith(".txt"):
        text = uploaded_file.read().decode("utf-8")
    else:
        from utils import read_docx
        text = read_docx(uploaded_file)
elif text_input:
    text = text_input
else:
    text = ""

if text:
    bias_results = detect_bias(text)
    highlighted = highlight_text(text, bias_results)
    st.markdown(highlighted, unsafe_allow_html=True)
    for result in bias_results:
        explanation = explain_bias(result)
        st.write(f"**Phrase:** {result['phrase']}")
        st.write(f"**Bias Type:** {result['bias_type']}")
        st.write(f"**Explanation:** {explanation}")
        if 'suggestion' in result:
            st.write(f"**Neutral Suggestion:** {result['suggestion']}") 
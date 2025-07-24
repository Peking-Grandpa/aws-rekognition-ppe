import streamlit as st

# Page config
st.set_page_config(
    page_title="AI-powered PPE Detection",
    page_icon="🦺",
    layout="centered",
)

# --- Navigation Bar (fake) ---
st.markdown("""
<style>
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: sans-serif;
    background-color: #f9fafe;
    padding: 0.8rem 1rem;
    border-bottom: 1px solid #ddd;
}
.navbar-left, .navbar-right {
    display: flex;
    gap: 1.5rem;
    align-items: center;
}
.button {
    background-color: #007bff;
    color: white;
    padding: 0.4rem 1rem;
    border-radius: 8px;
    text-decoration: none;
}
</style>

<div class="navbar">
  <div class="navbar-left">
    <strong>🌀</strong>
    <a>Homepage</a>
    <a>About</a>
    <a>Technology</a>
  </div>
  <div class="navbar-right">
    <a href="#" class="button">Contact us →</a>
  </div>
</div>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("## Ensure workplace safety with *:blue[AI-powered]* PPE detection analysis.")
st.markdown("""
Leverage the power of AWS Rekognition to accurately detect Personal Protective Equipment,  
enhancing safety protocols and ensuring compliance in industrial environments.
""")

# --- Info Section ---
st.markdown("### Accurate & Reliable PPE Detection")
st.markdown("""
Our service utilizes advanced AWS Rekognition technology to  
provide precise and dependable analysis of PPE usage, critical for  
maintaining high safety standards.
""")

# Buttons
col1, col2 = st.columns([1, 1])
with col1:
    st.button("Test Now")
with col2:
    st.button("Learn More")
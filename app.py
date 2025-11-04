import streamlit as st
import g4f
from g4f.Provider import DeepInfra

# 🌾 Project Samarth — App Configuration
st.set_page_config(
    page_title="🌾 Project Samarth — AI Assistant for Agriculture Insights",
    page_icon="🌾",
    layout="centered"
).      
    
# 🌾 Title and Intro
st.title("🌾 Project Samarth — AI Assistant for Agriculture Insights")

st.markdown("""
Welcome to **Project Samarth**, your AI-powered agriculture companion.  
This assistant helps farmers, researchers, and policymakers with **data-driven insights** on:
- 🌦️ Rainfall & monsoon predictions  
- 🌱 Crop patterns & soil recommendations  
- 🌾 Weather impact on yield and irrigation  
- 📈 Climate and sustainability analysis  

Ask your question below and get actionable insights instantly.
""")

# 🧠 User Input
query = st.text_area(
    "💬 Ask a question:",
    placeholder="Example: Predict rainfall trend in Maharashtra for next season",
    height=120
)

# 🔮 Generate AI Insight
if st.button("🔍 Generate Insight"):
    if not query.strip():
        st.warning("⚠️ Please enter a valid question before submitting.")
    else:
        with st.spinner("🤔 Generating intelligent agricultural insights..."):
            try:
                # ✅ Using DeepInfra model
                response = g4f.ChatCompletion.create(
                    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
                    provider=DeepInfra,
                    messages=[{"role": "user", "content": query}],
                )

                # Convert generator to string if needed
                if hasattr(response, "__iter__") and not isinstance(response, str):
                    response = "".join(response)

                st.success("🌾 AI Insight:")
                st.write(response)

            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.info("Try again or switch to another provider if the issue persists.")

# 🌱 Footer. 
st.markdown("---")
st.caption("""
Developed under 🌾 **Project Samarth**  
Empowering Agriculture with AI | Powered by **g4f (Free LLM API)**
""")

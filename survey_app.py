
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Survey App", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f4f4f9;
            padding: 20px;
            border-radius: 10px;
        }
        .title {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            color: #2c3e50;
        }
        .logo {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100px;
        }
        @media (max-width: 600px) {
            .css-1d391kg {
                display: flex !important;
                flex-direction: row !important;
                align-items: center !important;
            }
            .css-1d391kg > div {
                width: auto !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Display logo

# Display logo and title side-by-side
st.image("top_header.png", use_container_width =True)  # You can also use use_column_width=True if you want full width
st.image("banner.png", use_container_width =True)

st.markdown('<div class="title">📋 Customer Survey Form</div>', unsafe_allow_html=True)

st.markdown("---")
st.subheader("Your Information")
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")

st.subheader("Survey Questions")
q1 = st.radio("1.നിങ്ങളുടെ ജോലിയിൽ നിങ്ങൾ സന്തോഷവാൻ ആണോ?", 
              ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"])
q2 = st.radio("2. നിങ്ങളുടെ ജോലിയും ഫാമിലി ലൈഫും തുല്യമായി മുന്നോട്ടു കൊണ്ട് പോകാൻ സാധിക്കുന്നുണ്ടോ ?", 
              ["Yes", "No", "Maybe"])
q3 = st.radio("3.നിങ്ങൾ സമൂഹത്തിൽ ഇടപെടുന്ന ആളാണോ ?", 
              ["Yes", "No", "Maybe"])
q4 = st.radio("4.നിങ്ങളുടെ വ്യക്തി ജീവിതത്തിൽ സന്തോഷം കണ്ടെത്താൻ സമയം നീക്കി വെക്കാറുണ്ടോ  ?", 
              ["Yes", "No", "Maybe"])
q5 = st.radio("5.നിങ്ങൾ സമൂഹത്തിൽ ഇടപെടുന്ന ആളാണോ ?", 
              ["Yes", "No", "Maybe"])
q6 = st.multiselect("6.ദൈനംദിന ജീവിതത്തിലെ ഒഴിവു സമയം നിങ്ങൾ എങ്ങിനെ ഉപയോഗപ്പെടുത്തുന്നു??", 
                    ["Social Media", "Reading", "Social Activities", "Nothing"])
q7 = st.text_area("7. Any suggestions or feedback?", height=100)

if st.button("✅ Submit Survey"):
    if not name or not email or not phone:
        st.warning("Please fill in all your personal information.")
    else:
        data = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Q1": q1,
            "Q2": q2,
            "Q3": ", ".join(q3),
            "Q4": q4,
            "Q5": q5,
            "Q6": q6,
            "Q7 Feedback": q7
        }
        df_new = pd.DataFrame([data])
        file_path = "survey_data.xlsx"
        if os.path.exists(file_path):
            df_existing = pd.read_excel(file_path)
            if email in df_existing["Email"].values:
                st.error("You have already submitted this survey.")
            else:
                df_combined = pd.concat([df_existing, df_new], ignore_index=True)
                df_combined.to_excel(file_path, index=False)
                st.success("🎉 Thank you for your feedback!")
        else:
            df_new.to_excel(file_path, index=False)
            st.success("🎉 Thank you for your feedback!")

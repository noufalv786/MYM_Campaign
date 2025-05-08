
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

st.markdown('<div class="title">📋 MYM Survey Form</div>', unsafe_allow_html=True)

st.markdown("---")
st.subheader("Your Information")
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
zones = ["", "Riyadh North", "Riyadh city", "Dammam", "Jubail"]
main_zone = st.selectbox("Choose your Zone", zones)
# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1
# Sub-zones for each main zone
sub_zone_map = {
    "Riyadh North": ["Malaz", "Sulai", "Aqeeq", "Mursalath", "Olaya", "Muhammdiya", "Roudha", "Qurthuba"],
    "Riyadh city": ["Batha", "Nasiriyah", "Shifa", "Manfouha"],
    "Dammam": ["Al Faisaliah", "Al Shati", "Al Mazrouiah"],
    "Jubail": ["Fanateer", "Huwailat", "Al Jalmudah"]
}

# Display sub-zone field only after a zone is selected
if main_zone and main_zone in sub_zone_map:
    sub_zone = st.selectbox(f"Select a sub-zone in {main_zone}", sub_zone_map[main_zone])
    st.success(f"You selected: {main_zone} > {sub_zone}")

# Store answers in session state
if "answers" not in st.session_state:
    st.session_state.answers = {}

st.subheader("Survey Questions")

# Step 1 Questions
if st.session_state.step == 1:
    st.header("ഭാഗം 1")
    st.session_state.answers["Q1"] = st.radio("1. സൗദിയിൽ നിങ്ങൾ കുടുംബത്തോടൊപ്പമാണോ താമസിക്കുന്നത്?", ["Yes", "No", "Maybe"])
    st.session_state.answers["Q2"] = st.radio("2. നിങ്ങളുടെ പ്രിയപ്പെട്ടവരുമായി ( നേരിൽ അല്ലെങ്കിൽ ഓൺലൈൻ വഴി) ദിവസവും എത്ര തവണ നിങ്ങൾ കമ്മ്യൂണിക്കേഷൻ നടത്താറുണ്ട് ?", ["Multiple Times", "One Time", "No"])
    st.session_state.answers["Q3"] = st.radio("3. ജോലി- കുടുംബ ജീവിതത്തിലെ സമതുലനത്തിൽ നിങ്ങൾ എത്രത്തോളം തൃപ്തരാണ് ?", ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"])
    st.session_state.answers["Q4"] = st.radio("4. നിങ്ങൾക്ക് ജോലി സ്ഥലത്ത് മതിയായ പരിഗണനയും ആദരവും ലഭിക്കുന്നുണ്ടോ?", ["No", "Yes", "Maybe"])
    st.session_state.answers["Q5"] = st.radio("5. പ്രവാസത്തിൽ നിങ്ങൾ ആത്മീയമായും മതപരമായും തൃപ്തരാണോ ?", ["Yes", "No", "Maybe"])

    if st.button("Next"):
        st.session_state.step = 2

# Step 2 Questions
elif st.session_state.step == 2:
    st.header("ഭാഗം 2")
    st.session_state.answers["Q6"] = st.radio("6. കേരളീയ പരമ്പരാഗത ആഘോഷരീതികളിൽ പങ്ക് കൊള്ളാൻ നിങ്ങൾക്ക് അവസരങ്ങൾ ലഭിക്കുന്നുണ്ടോ?", ["Yes", "No", "Maybe"])
    st.session_state.answers["Q7"] = st.radio("7. പ്രവാസലോകത്ത് നിങ്ങളുടെ ശാരീരിക ആരോഗ്യത്തിലും ആരോഗ്യപരിപാലനത്തിന് ലഭ്യമാകുന്ന സൗകര്യങ്ങളിലും നിങ്ങൾ തൃപ്തരാണോ?", ["Yes", "No", "Maybe"])
    st.session_state.answers["Q8"] = st.radio("8. നിങ്ങൾ ജോലി കഴിഞ്ഞുള്ള ഒഴിവ് സമയം വ്യായാമത്തിന് വേണ്ടി മാറ്റി വെക്കാറുണ്ടോ ?", ["Yes", "No", "Maybe"])
    st.session_state.answers["Q9"] = st.radio("9. നിങ്ങളുടെ വ്യക്തിഗത ലക്ഷ്യങ്ങളിലേക്കും സ്വപ്നങ്ങളിലേക്കും നടന്നടുക്കാൻ പ്രവാസ ജീവിതത്തിൽ കഴിയുന്നുണ്ടോ?", ["Yes", "No", "Maybe"])
    st.session_state.answers["Q10"] = st.radio("10. നിങ്ങൾ സമൂഹത്തിൽ ഇടപെടുന്ന ആളാണോ?", ["Yes", "No", "Maybe"])

    if st.button("✅ Submit Survey"):
        if not name or not email or not phone:
            st.warning("Please fill in all your personal information.")
        elif not main_zone or (main_zone in sub_zone_map and "sub_zone" not in locals()):
            st.warning("Please select a zone and sub-zone.")
        else:
            data = {
                "Name": name,
                "Email": email,
                "Phone": phone,
                "Zone": main_zone,
                "Sub-Zone": sub_zone if main_zone in sub_zone_map else "",
                **st.session_state.answers
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

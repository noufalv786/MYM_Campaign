import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configure Streamlit page
st.set_page_config(page_title="Survey App", layout="centered")

# Load Google Sheet
def get_google_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        st.secrets["google_credentials"], scope
    )
    client = gspread.authorize(credentials)
    sheet = client.open("MYM- Survey").sheet1  # 🔁 Replace with your Sheet name
    return sheet

# Custom CSS
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
    </style>
""", unsafe_allow_html=True)

# Banner and Title
st.image("top_header.png", use_container_width=True)
st.image("banner.png", use_container_width=True)
st.markdown('<div class="title">📋 MYM - Happiness Survey Form</div>', unsafe_allow_html=True)
st.markdown("---")

# Personal Information
st.subheader("Your Information")
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
zones = ["ALJOUF", "RIYADH NORTH", "RIYADH CITY", "DAMMAM", "JUBAIL", "ALHASA", "ALKHOBAR", "ALQASEEM", "HAIL", "HAFAL AL BATHIN"]
main_zone = st.selectbox("Choose your Zone", zones)

# Sub-zones
sub_zone_map = {
    "RIYADH NORTH": ["MURSALATH", "OLAYA", "AQEEQ", "MALAZ", "MUHAMMEDIYA", "ROUDHA", "SULAI", "QURTHUBA"],
    "RIYADH CITY": ["AZEEZIYA", "KHALIDIYA", "KHARJ", "MUZAHMIYAH","NEW SANAYYA","BADIYA","BATHA WEST","BATHA","SHIFA","SHUMESI"],
    "DAMMAM": ["TOYOTA", "AL BADIYA", "CITY","MADEENATHUL UMMAL","NINETY ONE","QATIF","RAHEEMA","AL RABIEA"],
    "JUBAIL": ["AL DANAH", "AL MIRQAB", "TOWN"],
    "ALHASA": ["HOFUF", "KHALIDIYYA", "MUBARAZ"],
    "ALKHOBAR": ["THUQBA CITY", "SHAMALIYA", "BAYONIYA"],
    "ALQASEEM": ["BURAIDA", "UNAIZA"],
    "HAIL": ["CITY", "NUGRA"],
}

if "step" not in st.session_state:
    st.session_state.step = 1
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "submitted" not in st.session_state:
    st.session_state.submitted = False
st.session_state.sub_zone = ""
if main_zone and main_zone in sub_zone_map:
    sub_zone = st.selectbox(f"Select a sub-zone in {main_zone}", sub_zone_map[main_zone])
    st.session_state.sub_zone = sub_zone
    st.success(f"You selected: {main_zone} > {sub_zone}")

# Thank You Page
if st.session_state.submitted:
    st.markdown("## 🎉 Thank You for particiapte in MYM-Survey!")
    st.markdown("""
        ---
        ### Your response has been recorded successfully.

        _You may now close this tab or return to the home page._
    """)
    if st.button("🔙 Go to Home"):
        st.session_state.step = 1
        st.session_state.submitted = False
        st.rerun()
    st.stop()

# Survey Questions
st.subheader("Survey Questions")

if st.session_state.step == 1:
    st.header("ഭാഗം 1")
    st.session_state.answers["FAMILY"] = st.radio("1. സൗദിയിൽ നിങ്ങൾ കുടുംബത്തോടൊപ്പമാണോ താമസിക്കുന്നത്?", ["Yes", "No", "Maybe"])
    st.session_state.answers["COMMUNICATION"] = st.radio("2.നിങ്ങളുടെ പ്രിയപ്പെട്ടവരുമായി ദിവസത്തിൽ എത്ര തവണ കമ്മ്യൂണിക്കേറ്റ് ചെയ്യുന്നു?", ["Multiple Times", "Often","One Time", "No"])
    st.session_state.answers["WORK/FAMILY BALANCE"] = st.radio("3.ജോലി-കുടുംബ സമതുലനം എത്രത്തോളം തൃപ്തമാണ് ?", ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"])
    st.session_state.answers["WORK-RESPECT"] = st.radio("4. നിങ്ങളുടെ ജോലി പരിസരം തൃപ്തമാണോ ?", ["No", "Yes", "Maybe"])
    st.session_state.answers["MORALIS ASPECT"] = st.radio("5. ആത്മീയ-മതപരമായി തൃപ്തമാണോ?", ["Yes", "No", "Often"])

    if st.button("Next"):
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.header("ഭാഗം 2")
    st.session_state.answers["KERALA FESTIVAL"] = st.radio("6. നാട്ടിലെ ആഘോഷങ്ങളിൽ ഭാഗവാക്കാറുണ്ടോ ?", ["Yes", "No", "Maybe"])
    st.session_state.answers["HEALTH"] = st.radio("7. ആരോഗൃപരമായി  തൃപ്തരാണോ?", ["Yes", "No", "Maybe"])
    st.session_state.answers["EXERCISE"] = st.radio("8. വ്യായാമത്തിന് സമയം മാറ്റിവെക്കാറുണ്ടോ?", ["Yes", "No", "Maybe"])
    st.session_state.answers["AIM/DREAM"] = st.radio("9. സ്വപ്നങ്ങൾ നേടിയെടുക്കാൻ ശ്രമിക്കാറുണ്ടോ ?", ["Yes", "No", "Maybe"])
    st.session_state.answers["AS A SOCIAL WORKER"] = st.radio("10. സമൂഹത്തിൽ പങ്കാളിയാകുന്നുണ്ടോ?", ["Yes", "No", "Maybe"])
    # New text area field for elaboration
    st.session_state.answers["COMMENT"] = st.text_area(
        "11.നിങ്ങളുടെ ക്ഷേമം മെച്ചപ്പെടുത്താൻ RSC പോലുള്ള  സംഘടനകൾക്ക് എന്താണ് ചെയ്യാൻ കഴിയുക?:",
        key="social_worker_comment"
    )

    if st.button("✅ Submit Survey"):
        if not name or not email or not phone:
            st.warning("Please fill in all your personal information.")
        elif not main_zone or (main_zone in sub_zone_map and "sub_zone" not in st.session_state):
            st.warning("Please select a zone and sub-zone.")
        else:
            with st.spinner("Submitting your response..."):
                try:
                    sheet = get_google_sheet()
                    existing_emails = sheet.col_values(2)  # Assuming Email is 2nd column
                    if email in existing_emails:
                        st.error("You have already submitted this survey.")
                    else:
                        row = [name, email, phone, main_zone, st.session_state.sub_zone] + list(st.session_state.answers.values())
                        sheet.append_row(row)
                        st.success("✅ Survey submitted successfully!")
                        st.session_state.submitted = True
                        st.rerun()
                except Exception as e:
                    st.error(f"An error occurred: {e}")


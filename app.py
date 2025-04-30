import streamlit as st
import re

# --- Custom Styles ---
st.markdown(
    """
    <style>
        /* Full app background with gradient */
        .stApp {
            background: linear-gradient(135deg, #74ebd5, #ACB6E5);  /* Bright blue-purple gradient */
            background-attachment: fixed;
        }

        /* Main content container */
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 10px;
            max-width: 800px;
            margin: auto;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }

        h1 {
            color: #333333;
            text-align: center;
        }

        .stButton>button {
            background-color: #6a11cb;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
        }

        .stButton>button:hover {
            background-color: #2575fc;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>AI Resume Screener</h1>", unsafe_allow_html=True)
st.markdown("<div class='main'>", unsafe_allow_html=True)

# --- Resume and JD Upload ---
resume_file = st.file_uploader("Upload Resume (.txt)", type=["txt"])
jd_file = st.file_uploader("Upload Job Description (.txt)", type=["txt"])

# --- Keyword Matching Function ---
def extract_keywords(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    words = text.split()
    return set(words)

# --- Main Logic ---
if resume_file and jd_file:
    resume_text = resume_file.read().decode("utf-8")
    jd_text = jd_file.read().decode("utf-8")

    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    matched_keywords = resume_keywords.intersection(jd_keywords)
    match_percentage = (len(matched_keywords) / len(jd_keywords)) * 100 if jd_keywords else 0

    st.subheader(f"Match Score: {match_percentage:.2f}%")

    if match_percentage > 70:
        st.success("✅ Strong Match – Your resume fits well!")
    elif match_percentage > 50:
        st.warning("⚠ Moderate Match – Add a few more keywords.")
    else:
        st.error("❌ Low Match – Resume needs improvement.")

    missing_keywords = jd_keywords - resume_keywords
    if missing_keywords:
        st.info(f"Missing Keywords: {', '.join(sorted(missing_keywords))}")

st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)

import streamlit as st

# Page config
st.set_page_config(
    page_title="치지직 VOD 다운로더",
    page_icon="📺",
    layout="wide"
)

# Pixel-perfect CSS matching the image exactly
st.markdown("""
<style>
    /* Global dark background */
    .stApp {
        background-color: #1a1a1a !important;
    }
    
    /* Hide Streamlit elements */
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    .stDecoration {display:none;}
    header {visibility: hidden;}
    
    /* Main container */
    .block-container {
        padding: 4rem 2rem !important;
        max-width: 800px !important;
        margin: 0 auto !important;
    }
    
    /* Title styling - centered like in image */
    .main-title {
        color: #00d97a;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin: 2rem 0 4rem 0;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .link-icon {
        margin-right: 12px;
        font-size: 2.2rem;
    }
    
    /* Input container - no visible borders */
    .input-section {
        max-width: 600px;
        margin: 0 auto;
        padding: 0;
    }
    
    /* VOD URL label styling */
    .stTextInput label {
        color: #888 !important;
        font-size: 14px !important;
        font-weight: 400 !important;
        margin-bottom: 8px !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Input field - exactly like image */
    .stTextInput > div > div > input {
        background-color: #2d2d2d !important;
        color: #ffffff !important;
        border: 1px solid #3a3a3a !important;
        border-radius: 8px !important;
        padding: 16px 18px !important;
        font-size: 16px !important;
        height: 56px !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #777 !important;
        font-style: italic;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #00d97a !important;
        box-shadow: 0 0 0 1px #00d97a !important;
        outline: none !important;
    }
    
    /* Button styling - matching image */
    .stLinkButton > a {
        background-color: #2d2d2d !important;
        color: #ffffff !important;
        border: 1px solid #3a3a3a !important;
        border-radius: 8px !important;
        padding: 16px 24px !important;
        text-decoration: none !important;
        font-weight: 500 !important;
        font-size: 16px !important;
        display: block !important;
        text-align: center !important;
        margin-top: 24px !important;
        height: 56px !important;
        line-height: 24px !important;
        transition: all 0.2s ease !important;
    }
    
    .stLinkButton > a:hover {
        background-color: #373737 !important;
        border-color: #4a4a4a !important;
    }
    
    /* Remove any extra spacing */
    .stTextInput > div {
        margin-bottom: 0 !important;
    }
    
    .stLinkButton {
        margin-top: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Centered title with icon - exactly like image
st.markdown("""
<div class="main-title">
    <span class="link-icon">🔗</span>
    치지직 VOD 다운로더
</div>
""", unsafe_allow_html=True)

# Input section - clean layout like image
st.markdown('<div class="input-section">', unsafe_allow_html=True)

# URL input field
url_input = st.text_input(
    "VOD URL", 
    placeholder="chzzk.naver.com/video/{number}",
    key="vod_url"
)

# Build URL for redirect
if url_input.strip():
    clean_url = url_input.strip()
    if not clean_url.startswith('http'):
        formatted_url = f"https://{clean_url}"
    else:
        formatted_url = clean_url
    download_url = f"https://chzzkdownloader.com?utm_source=streamlit&url={formatted_url}"
else:
    download_url = "https://chzzkdownloader.com?utm_source=streamlit"

# Button - smaller like original
st.link_button(
    "VOD 가져오기",
    download_url
)

st.markdown('</div>', unsafe_allow_html=True)

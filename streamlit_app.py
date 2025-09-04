import streamlit as st

# Page config
st.set_page_config(
    page_title="치지직 VOD 다운로더",
    page_icon="📺",
    layout="centered"
)

# CSS to exactly match the image
st.markdown("""
<style>
    .stApp {
        background-color: #1e1e1e;
    }
    
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    .stDecoration {display:none;}
    
    .main-title {
        color: #00ff88;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 2rem;
        display: flex;
        align-items: center;
    }
    
    .link-icon {
        margin-right: 10px;
    }
    
    /* Main container styling */
    .main-container {
        background-color: #2a2a2a;
        border: 1px solid #404040;
        border-radius: 12px;
        padding: 2rem;
        margin: 1rem 0;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 1px solid #555 !important;
        border-radius: 8px !important;
        padding: 15px !important;
        font-size: 16px !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #888 !important;
    }
    
    .stTextInput label {
        color: #ccc !important;
        font-size: 14px !important;
        margin-bottom: 8px !important;
    }
    
    /* Link button styling */
    .stLinkButton > a {
        background-color: #333 !important;
        color: #fff !important;
        border: 1px solid #555 !important;
        border-radius: 8px !important;
        padding: 12px 24px !important;
        text-decoration: none !important;
        font-weight: 500 !important;
        display: block !important;
        text-align: center !important;
        margin-top: 1rem !important;
    }
    
    .stLinkButton > a:hover {
        background-color: #444 !important;
        border-color: #666 !important;
    }
    
    .block-container {
        padding-top: 2rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<div class="main-title">
    <span class="link-icon">🔗</span>
    치지직 VOD 다운로더
</div>
""", unsafe_allow_html=True)

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# URL input
url_input = st.text_input(
    "VOD URL", 
    placeholder="chzzk.naver.com/video/{number}",
    key="url_input"
)

# Build redirect URL
if url_input:
    if not url_input.startswith('http'):
        clean_url = url_input
    else:
        clean_url = url_input
    download_url = f"https://chzzkdownloader.com?from=streamlit&url={clean_url}"
else:
    download_url = "https://chzzkdownloader.com?from=streamlit"

# Working redirect button
st.link_button(
    "VOD 가져오기",
    download_url,
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)

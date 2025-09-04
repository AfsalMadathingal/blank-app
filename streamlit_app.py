import streamlit as st

# Page config with dark theme
st.set_page_config(
    page_title="치지직 VOD 다운로더",
    page_icon="📺",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS to match the image exactly
st.markdown("""
<style>
    /* Global dark theme */
    .stApp {
        background-color: #0f0f0f !important;
    }
    
    /* Hide default Streamlit elements */
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    .stDecoration {display:none;}
    
    /* Title styling */
    .main-title {
        color: #00ff88;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: left;
        margin: 2rem 0 3rem 0;
        display: flex;
        align-items: center;
    }
    
    .link-icon {
        color: #00ff88;
        margin-right: 15px;
        font-size: 1.8rem;
    }
    
    /* Container styling to match image */
    .input-container {
        background-color: #1a1a1a;
        border: 1px solid #333;
        border-radius: 12px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    
    /* Input field styling */
    .stTextInput > div > div > input {
        background-color: #2a2a2a !important;
        color: #ffffff !important;
        border: 1px solid #404040 !important;
        border-radius: 8px !important;
        padding: 12px 16px !important;
        font-size: 16px !important;
        height: 48px !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #00ff88 !important;
        box-shadow: 0 0 0 1px #00ff88 !important;
        outline: none !important;
    }
    
    .stTextInput label {
        color: #cccccc !important;
        font-weight: 500 !important;
        font-size: 14px !important;
        margin-bottom: 8px !important;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #2a2a2a !important;
        color: #ffffff !important;
        border: 1px solid #404040 !important;
        border-radius: 8px !important;
        padding: 12px 24px !important;
        font-weight: 500 !important;
        font-size: 16px !important;
        height: 48px !important;
        margin-top: 16px !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton > button:hover {
        background-color: #333333 !important;
        border-color: #555555 !important;
    }
    
    .stButton > button:active {
        background-color: #1a1a1a !important;
    }
    
    /* Remove extra spacing */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 1rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Title with link icon
st.markdown("""
<div class="main-title">
    <span class="link-icon">🔗</span>
    치지직 VOD 다운로더
</div>
""", unsafe_allow_html=True)

# Create the main container
with st.container():
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    
    # URL input field
    url_input = st.text_input(
        "VOD URL", 
        placeholder="chzzk.naver.com/video/{number}",
        label_visibility="visible"
    )
    
    # Button
    if st.button("VOD 가져오기", use_container_width=True):
        if url_input:
            # Add https if not present
            if not url_input.startswith('http'):
                formatted_url = f"https://{url_input}"
            else:
                formatted_url = url_input
            
            download_url = f"https://chzzkdownloader.com?from=streamlit&url={formatted_url}"
            st.markdown(f'<meta http-equiv="refresh" content="0; url={download_url}">', unsafe_allow_html=True)
            st.success("리디렉트 중...")
        else:
            download_url = "https://chzzkdownloader.com?from=streamlit"
            st.markdown(f'<meta http-equiv="refresh" content="0; url={download_url}">', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

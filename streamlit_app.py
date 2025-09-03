import streamlit as st

# Page config
st.set_page_config(
    page_title="치지직 VOD 다운로더",
    page_icon="📺",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #ff6b6b;
        font-size: 3rem;
        margin-bottom: 2rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 3rem;
    }
    .download-button {
        display: flex;
        justify-content: center;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="main-header">📺 치지직 VOD 다운로더</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">좋아하는 치지직 스트림을 쉽게 다운로드하세요!</p>', unsafe_allow_html=True)

# Create columns for centering
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # URL input field
    url_input = st.text_input("Enter CHZZ VOD URL:", placeholder="https://chzzk.naver.com/...")
    
    # Direct link button with parameters
    if url_input:
        download_url = f"https://chzzkdownloader.com?from=streamlit&url={url_input}"
    else:
        download_url = "https://chzzkdownloader.com?from=streamlit"
    
    st.link_button(
        "🚀 Click Here to Download",
        download_url,
        use_container_width=True,
        type="primary"
    )

# Additional info
st.markdown("---")
st.markdown("""
### How to use:
1. Click the button above to visit the downloader
2. Paste your CHZZ VOD URL
3. Download your video!

*Safe, fast, and easy to use.*
""")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888;'>Made with ❤️ for CHZZ users</div>", 
    unsafe_allow_html=True
)

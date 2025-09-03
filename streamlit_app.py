import streamlit as st

# Page config
st.set_page_config(
    page_title="CHZZ VOD Downloader",
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
st.markdown('<h1 class="main-header">📺 CHZZ VOD Downloader</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Download your favorite CHZZ streams easily!</p>', unsafe_allow_html=True)

# Create columns for centering
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Direct link button
    st.link_button(
        "🚀 Click Here to Download",
        "https://chzzkdownloader.com",
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

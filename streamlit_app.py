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
        color: #4CAF50;
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
    url_input = st.text_input("치지직 VOD URL을 입력하세요:", placeholder="https://chzzk.naver.com/...")
    
    # Direct link button with parameters
    if url_input:
        download_url = f"https://chzzkdownloader.com?from=streamlit&url={url_input}"
    else:
        download_url = "https://chzzkdownloader.com?from=streamlit"
    
    st.link_button(
        "🚀 다운로드하러 가기",
        download_url,
        use_container_width=True,
        type="primary"
    )

# Additional info
st.markdown("---")
st.markdown("""
### 사용 방법:
1. 위의 버튼을 클릭하여 다운로더로 이동
2. 치지직 VOD URL을 붙여넣기
3. 비디오 다운로드!

*안전하고 빠르며 사용하기 쉽습니다.*
""")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888;'>치지직 유저들을 위해 ❤️ 로 제작</div>", 
    unsafe_allow_html=True
)# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888;'>Made with ❤️ for CHZZ users</div>", 
    unsafe_allow_html=True
)

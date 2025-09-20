import streamlit as st

# Page config with SEO optimization
st.set_page_config(
    page_title="치지직 VOD 다운로더 - 무료 CHZZK 비디오 다운로드 도구",
    page_icon="📺",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.chzzkdownloader.com/support',
        'Report a bug': "https://www.chzzkdownloader.com/report",
        'About': "# 치지직 VOD 다운로더\n가장 빠르고 안전한 CHZZK 비디오 다운로드 서비스"
    }
)

# SEO meta description
st.markdown("""
<meta name="description" content="무료 치지직 VOD 다운로더 - CHZZK 비디오를 빠르고 안전하게 다운로드하세요. 간단한 URL 입력으로 고품질 비디오 다운로드가 가능합니다.">
<meta name="keywords" content="치지직, CHZZK, VOD, 다운로더, 비디오 다운로드, 무료, 온라인 도구">
<meta name="author" content="CHZZK Save">
<meta property="og:title" content="치지직 VOD 다운로더 - 무료 CHZZK 비디오 다운로드">
<meta property="og:description" content="가장 빠르고 안전한 CHZZK 비디오 다운로드 서비스. 간단한 URL로 고품질 VOD를 무료로 다운로드하세요.">
<meta property="og:type" content="website">
<meta property="og:image" content="https://chzzkdownloader.com/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="치지직 VOD 다운로더">
<meta name="twitter:description" content="무료 CHZZK 비디오 다운로드 도구">
<meta name="robots" content="index, follow">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
""", unsafe_allow_html=True)

# Premium purchase button
st.markdown("""
<a href="https://www.paypal.com/ncp/payment/LM7VS22YPJVKJ" target="_blank" class="premium-button">
    <span class="premium-icon">⭐</span>
    프리미엄 구매
</a>
""", unsafe_allow_html=True)

# Modern CSS with improved UI and animations
st.markdown("""
<style>
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global dark background */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #0f0f0f 100%) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }
    
    /* Hide Streamlit elements */
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    .stDecoration {display:none;}
    header {visibility: hidden;}
    .stMainBlockContainer > div:first-child {padding-top: 2rem !important;}
    
    /* Main container */
    .block-container {
        padding: 3rem 2rem !important;
        max-width: 900px !important;
        margin: 0 auto !important;
    }
    
    /* Premium button styling */
    .premium-button {
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        background: linear-gradient(135deg, #ff6b6b, #ee5a24) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 24px !important;
        text-decoration: none !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        box-shadow: 0 4px 20px rgba(255, 107, 107, 0.3) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .premium-button:hover {
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.5) !important;
        text-decoration: none !important;
        color: white !important;
    }
    
    .premium-icon {
        font-size: 16px;
        animation: sparkle 2s ease-in-out infinite;
    }
    
    @keyframes sparkle {
        0%, 100% { transform: scale(1) rotate(0deg); }
        50% { transform: scale(1.2) rotate(180deg); }
    }
    
    /* Hero section styling */
    .hero-section {
        text-align: center;
        margin: 3rem 0 4rem 0;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.02);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    
    /* Title styling with gradient */
    .main-title {
        background: linear-gradient(135deg, #00d97a 0%, #00b866 50%, #00a653 100%);
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: clamp(2rem, 5vw, 3rem);
        font-weight: 700;
        text-align: center;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 16px;
        letter-spacing: -0.02em;
    }
    
    .link-icon {
        font-size: clamp(1.8rem, 4vw, 2.5rem);
        animation: bounce 2s ease-in-out infinite;
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-8px); }
        60% { transform: translateY(-4px); }
    }
    
    /* Subtitle with features */
    .subtitle {
        color: #888;
        font-size: 18px;
        margin: 1.5rem 0 2rem 0;
        line-height: 1.6;
    }
    
    .features {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 2rem 0;
        flex-wrap: wrap;
    }
    
    .feature {
        display: flex;
        align-items: center;
        gap: 8px;
        color: #00d97a;
        font-size: 14px;
        font-weight: 500;
    }
    
    /* Input container with glassmorphism */
    .input-section {
        max-width: 600px;
        margin: 0 auto;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    /* Input label styling */
    .stTextInput label {
        color: #bbb !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        margin-bottom: 12px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Modern input field */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.08) !important;
        color: #ffffff !important;
        border: 2px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        padding: 18px 20px !important;
        font-size: 16px !important;
        height: 60px !important;
        width: 100% !important;
        box-sizing: border-box !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #777 !important;
        font-style: normal;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #00d97a !important;
        box-shadow: 0 0 0 3px rgba(0, 217, 122, 0.1) !important;
        background: rgba(255, 255, 255, 0.12) !important;
        outline: none !important;
        transform: translateY(-2px) !important;
    }
    
    /* Modern button styling */
    .stLinkButton > a {
        background: linear-gradient(135deg, #00d97a 0%, #00b866 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 18px 32px !important;
        text-decoration: none !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        display: block !important;
        text-align: center !important;
        margin-top: 24px !important;
        height: 60px !important;
        line-height: 24px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 20px rgba(0, 217, 122, 0.3) !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .stLinkButton > a:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 30px rgba(0, 217, 122, 0.4) !important;
        background: linear-gradient(135deg, #00e085 0%, #00c970 100%) !important;
    }
    
    .stLinkButton > a::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .stLinkButton > a:hover::before {
        left: 100%;
    }
    
    /* Age-restricted download link styling */
    .age-restricted-link {
        color: rgba(255, 255, 255, 0.8) !important;
        font-size: 14px !important;
        text-decoration: none !important;
        transition: all 0.3s ease !important;
        font-weight: 400 !important;
        line-height: 1.5 !important;
    }
    
    .age-restricted-link:hover {
        color: #00d97a !important;
        text-decoration: underline !important;
    }
    
    /* Remove default spacing */
    .stTextInput > div {
        margin-bottom: 0 !important;
    }
    
    .stLinkButton {
        margin-top: 0 !important;
    }
    
    /* Trust indicators */
    .trust-section {
        text-align: center;
        margin-top: 3rem;
        padding: 2rem;
        color: #666;
    }
    
    .trust-indicators {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 1rem;
        flex-wrap: wrap;
    }
    
    .trust-item {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 14px;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .block-container {
            padding: 2rem 1rem !important;
        }
        
        .input-section {
            padding: 1.5rem;
        }
        
        .features {
            flex-direction: column;
            align-items: center;
            gap: 1rem;
        }
        
        .premium-button {
            top: 10px;
            right: 10px;
            padding: 10px 16px !important;
            font-size: 12px !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# SEO-optimized header with structured data
st.markdown("""
<div class="hero-section">
    <h1 class="main-title">
        <span class="link-icon">🔗</span>
        치지직 VOD 다운로더
    </h1>
    <div class="subtitle">
        CHZZK 비디오를 빠르고 안전하게 다운로드하세요
    </div>
    <div class="features">
        <div class="feature">
            <span>⚡</span>
            <span>초고속 다운로드</span>
        </div>
        <div class="feature">
            <span>🔒</span>
            <span>100% 안전</span>
        </div>
        <div class="feature">
            <span>💯</span>
            <span>무료 서비스</span>
        </div>
        <div class="feature">
            <span>📱</span>
            <span>모든 기기 지원</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Input section with modern design
st.markdown('<div class="input-section">', unsafe_allow_html=True)

# URL input field with better placeholder
url_input = st.text_input(
    "VOD URL", 
    placeholder="https://chzzk.naver.com/video/1234567890",
    key="vod_url",
    help="치지직 VOD 페이지의 전체 URL을 입력하세요"
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

# Modern download button
st.link_button(
    "🚀 VOD 다운로드 시작",
    download_url,
    use_container_width=True
)

# Age-restricted download link
st.markdown("""
<div style="text-align: center; margin-top: 16px;">
    <a href="https://www.paypal.com/ncp/payment/LM7VS22YPJVKJ" target="_blank" class="age-restricted-link">
        연령 제한 콘텐츠 다운로드가 필요하신가요? 프로 버전을 구매하세요!
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Trust section for SEO and user confidence
st.markdown("""
<div class="trust-section">
    <h3 style="color: #888; font-size: 16px; margin-bottom: 1rem;">신뢰할 수 있는 서비스</h3>
    <div class="trust-indicators">
        <div class="trust-item">
            <span>🛡️</span>
            <span>바이러스 없음</span>
        </div>
        <div class="trust-item">
            <span>🚫</span>
            <span>광고 없음</span>
        </div>
        <div class="trust-item">
            <span>📊</span>
            <span>개인정보 수집 안함</span>
        </div>
        <div class="trust-item">
            <span>💎</span>
            <span>원본 품질 보장</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# SEO-friendly text content for search engines
st.markdown("""
<div style="display: none;">
치지직 VOD 다운로더는 CHZZK(치지직) 플랫폼의 비디오 온 디맨드(VOD) 콘텐츠를 쉽고 빠르게 다운로드할 수 있는 무료 온라인 도구입니다. 
네이버의 게임 스트리밍 플랫폼인 치지직에서 제공되는 다양한 VOD 영상을 고품질로 저장할 수 있으며, 
별도의 소프트웨어 설치 없이 웹브라우저에서 바로 이용 가능합니다. 
안전하고 신뢰할 수 있는 다운로드 서비스로 개인정보 보호를 최우선으로 합니다.
</div>
""", unsafe_allow_html=True)

# Structured data for SEO
st.markdown("""
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "치지직 VOD 다운로더",
  "description": "CHZZK 비디오를 빠르고 안전하게 다운로드하는 무료 온라인 도구",
  "url": "https://chzzkdownloader.com",
  "applicationCategory": "Multimedia",
  "operatingSystem": "Any",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "KRW"
  },
  "featureList": [
    "초고속 다운로드",
    "100% 안전",
    "무료 서비스",
    "모든 기기 지원"
  ]
}
</script>
""", unsafe_allow_html=True)

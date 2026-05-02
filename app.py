import os
import streamlit as st
from dotenv import load_dotenv
from pathlib import Path


current_dir = Path(__file__).parent
env_path = current_dir / '.env'
load_dotenv(dotenv_path=env_path)

# Credentials extraction
API_KEY = os.getenv("WATSONX_API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")


st.set_page_config(
    page_title="QS-Nav | Quantum-Safe Navigator",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# IBM Carbon Design System Inspired Styling
st.markdown("""
    <style>
    /* IBM Color Palette */
    :root {
        --ibm-blue: #0f62fe;
        --ibm-blue-dark: #0043ce;
        --ibm-blue-light: #4589ff;
        --ibm-gray-10: #f4f4f4;
        --ibm-gray-20: #e0e0e0;
        --ibm-gray-50: #8d8d8d;
        --ibm-gray-90: #262626;
        --ibm-gray-100: #161616;
        --ibm-purple: #8a3ffc;
        --ibm-cyan: #1192e8;
        --ibm-teal: #009d9a;
    }
    
    /* Main Background with Gradient */
    .main {
        background: linear-gradient(135deg, #f4f4f4 0%, #e8eef5 100%);
    }
    
    /* Custom Header Styling */
    .custom-header {
        background: linear-gradient(135deg, var(--ibm-blue-dark) 0%, var(--ibm-blue) 50%, var(--ibm-purple) 100%);
        padding: 2rem 2rem 3rem 2rem;
        border-radius: 0 0 24px 24px;
        margin: -6rem -4rem 2rem -4rem;
        box-shadow: 0 8px 32px rgba(15, 98, 254, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .custom-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
        opacity: 0.4;
    }
    
    .header-content {
        position: relative;
        z-index: 1;
    }
    
    .main-title {
        color: white;
        font-size: 3rem;
        font-weight: 300;
        margin: 0;
        letter-spacing: -0.5px;
        text-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
    
    .main-subtitle {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.25rem;
        font-weight: 300;
        margin-top: 0.5rem;
        letter-spacing: 0.5px;
    }
    
    /* Enhanced Metrics */
    .stMetric {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: none;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
    }
    
    .stMetric:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(15, 98, 254, 0.15);
    }
    
    /* Card Styling */
    div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    }
    
    /* File Uploader Enhancement */
    .stFileUploader {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        border: 2px dashed var(--ibm-blue-light);
        transition: all 0.3s ease;
    }
    
    .stFileUploader:hover {
        border-color: var(--ibm-blue);
        background: #f8f9ff;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--ibm-gray-100) 0%, var(--ibm-gray-90) 100%);
        border-right: 1px solid var(--ibm-gray-50);
    }
    
    section[data-testid="stSidebar"] .stMarkdown {
        color: white;
    }
    
    /* Button Enhancements */
    .stButton > button {
        background: linear-gradient(135deg, var(--ibm-blue) 0%, var(--ibm-purple) 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(15, 98, 254, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(15, 98, 254, 0.4);
    }
    
    /* Alert Boxes */
    .stAlert {
        border-radius: 12px;
        border-left: 4px solid;
        animation: slideIn 0.5s ease;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Info Box Styling */
    .info-box {
        background: linear-gradient(135deg, #e8f4ff 0%, #f0f7ff 100%);
        border-left: 4px solid var(--ibm-blue);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(15, 98, 254, 0.1);
    }
    
    .success-box {
        background: linear-gradient(135deg, #e5f9f5 0%, #f0fdf9 100%);
        border-left: 4px solid var(--ibm-teal);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0, 157, 154, 0.1);
    }
    
    .warning-box {
        background: linear-gradient(135deg, #fff4e5 0%, #fffbf0 100%);
        border-left: 4px solid #ff832b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(255, 131, 43, 0.1);
    }
    
    /* Divider Enhancement */
    hr {
        margin: 2rem 0;
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--ibm-gray-20), transparent);
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: var(--ibm-blue) !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 4rem;
        color: var(--ibm-gray-50);
        font-size: 0.875rem;
        border-top: 1px solid var(--ibm-gray-20);
    }
    
    /* Badge Styling */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .badge-critical {
        background: #fff1f1;
        color: #da1e28;
    }
    
    .badge-warning {
        background: #fff4e5;
        color: #ff832b;
    }
    
    .badge-success {
        background: #e5f9f5;
        color: #009d9a;
    }
    
    /* Subheader Enhancement */
    .stSubheader {
        color: var(--ibm-gray-90);
        font-weight: 500;
        margin-bottom: 1rem;
    }
    
    /* Column Gap */
    div[data-testid="column"] {
        padding: 0 0.5rem;
    }
    
    /* Smooth Transitions */
    * {
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ERROR HANDLING & CONFIG CHECK
if not API_KEY or not PROJECT_ID:
    st.error("### ❌ Configuration Error")
    st.info(f"System searched at: **{env_path}**")
    st.warning("Please ensure your `.env` file contains **WATSONX_API_KEY** and **PROJECT_ID**.")
    st.stop()

# 4. CORE ENGINE (Watsonx Analysis Mockup) 
def analyze_quantum_risk(file_content):
    """
    Simulates sending data to Granite-3 via watsonx.ai.
    Reflecting your work on agentic workflows like 'Lucy' and 'Pivot'.
    """
    # Logic simulating identifying RSA/ECC vulnerabilities
    findings = {
        "score": 42,
        "vulnerabilities": [
            "⚠️ Detected Hardcoded RSA-2048 (Vulnerable to Shor's Algorithm)",
            "⚠️ Legacy ECC Curve P-256 in SSL configuration"
        ],
        "remediation": "Transition to **ML-KEM (Kyber)** for key encapsulation as per NIST standards."
    }
    return findings

# 5. MAIN APP INTERFACE
# Custom Header
st.markdown("""
    <div class="custom-header">
        <div class="header-content">
            <h1 class="main-title">🛡️ QS-Nav: Quantum-Safe Navigator</h1>
            <p class="main-subtitle">Automated Infrastructure Governance & Post-Quantum Cryptography Modernization</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Sidebar with Enhanced Branding
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    st.image("psyduck.png", width=100)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 📋 Project Details")
    st.markdown("---")
    
    st.markdown("""
        <div style='color: white; line-height: 1.8;'>
            <p><strong>👨‍💻 Developer</strong><br/>Janea Geresola</p>
            <p><strong>🎓 Status</strong><br/>Incoming Graduating Student (CPU)</p>
            <p><strong>🔐 Focus Area</strong><br/>Post-Quantum Cryptography (PQC)</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
        <div style='color: rgba(255,255,255,0.8); font-size: 0.85rem; line-height: 1.6;'>
            <p>🤖 <strong>Powered by IBM watsonx.ai</strong></p>
            <p>Leveraging <strong>IBM Bob</strong> and <strong>Granite-3</strong> models to bridge the quantum skills gap and secure infrastructure for the post-quantum era.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Technology Stack
    st.markdown("### 🛠️ Tech Stack")
    st.markdown("""
        <div style='display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem;'>
            <span class='badge badge-success'>IBM watsonx.ai</span>
            <span class='badge badge-success'>Granite-3</span>
            <span class='badge badge-success'>Streamlit</span>
            <span class='badge badge-success'>Python</span>
        </div>
    """, unsafe_allow_html=True)

# Main Content Area
st.markdown("<br>", unsafe_allow_html=True)

# Feature Highlights
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>🔍</div>
            <div style='font-weight: 600; color: #0f62fe;'>Smart Detection</div>
            <div style='font-size: 0.85rem; color: #8d8d8d; margin-top: 0.25rem;'>AI-powered vulnerability scanning</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>⚡</div>
            <div style='font-weight: 600; color: #0f62fe;'>Auto-Remediation</div>
            <div style='font-size: 0.85rem; color: #8d8d8d; margin-top: 0.25rem;'>NIST-approved PQC solutions</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>🚀</div>
            <div style='font-weight: 600; color: #0f62fe;'>Enterprise Ready</div>
            <div style='font-size: 0.85rem; color: #8d8d8d; margin-top: 0.25rem;'>Production-grade security</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>🛡️</div>
            <div style='font-weight: 600; color: #0f62fe;'>Quantum-Safe</div>
            <div style='font-size: 0.85rem; color: #8d8d8d; margin-top: 0.25rem;'>Future-proof encryption</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Dashboard Logic
st.markdown("### 📤 Upload Infrastructure Configuration")
uploaded_file = st.file_uploader(
    "Drop your Infrastructure-as-Code files here (YAML, Terraform, JSON)",
    type=['yaml', 'yml', 'tf', 'json'],
    help="Upload configuration files to analyze for quantum-vulnerable cryptographic implementations"
)

if uploaded_file:
    file_contents = uploaded_file.read().decode("utf-8")
    
    st.markdown(f"""
        <div class='info-box'>
            <strong>📄 File Uploaded:</strong> {uploaded_file.name} ({len(file_contents)} bytes)
        </div>
    """, unsafe_allow_html=True)
    
    with st.spinner("🔄 Granite-3 is analyzing your infrastructure for quantum vulnerabilities..."):
        # Placeholder for actual model interaction
        results = analyze_quantum_risk(file_contents)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Key Performance Indicators
    st.markdown("### 📊 Security Assessment Dashboard")
    m1, m2, m3 = st.columns(3)
    m1.metric("🎯 Quantum-Safe Score", f"{results['score']}/100", delta="-58", delta_color="inverse")
    m2.metric("⚠️ Cryptographic Flaws", len(results['vulnerabilities']), delta=f"+{len(results['vulnerabilities'])}", delta_color="inverse")
    m3.metric("🚨 Risk Level", "Critical", delta_color="off")

    st.markdown("<br>", unsafe_allow_html=True)

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("### 🔍 Vulnerability Analysis")
        st.markdown("<br>", unsafe_allow_html=True)
        for i, v in enumerate(results['vulnerabilities'], 1):
            st.markdown(f"""
                <div class='warning-box'>
                    <strong>Finding #{i}</strong><br/>
                    {v}
                </div>
            """, unsafe_allow_html=True)

    with col_right:
        st.markdown("### 🚀 Modernization Roadmap")
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class='success-box'>
                <strong>✅ Recommended Action</strong><br/>
                {results['remediation']}
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class='info-box'>
                <strong>💡 Why This Matters</strong><br/>
                Applying this change ensures <strong>Crypto-Agility</strong>, preventing 'Harvest Now, Decrypt Later' attacks where adversaries collect encrypted data today to decrypt it once quantum computers become available.
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Additional Resources
        with st.expander("📚 Learn More About Post-Quantum Cryptography"):
            st.markdown("""
                - **NIST PQC Standards**: ML-KEM (Kyber), ML-DSA (Dilithium), SLH-DSA (SPHINCS+)
                - **Timeline**: FIPS standards expected by 2024-2025
                - **Migration Strategy**: Hybrid approaches recommended during transition
                - **IBM Resources**: watsonx.ai for automated PQC migration planning
            """)

else:
    st.markdown("""
        <div class='info-box' style='text-align: center; padding: 3rem;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>📁</div>
            <h3 style='color: #0f62fe; margin-bottom: 1rem;'>Ready to Secure Your Infrastructure</h3>
            <p style='color: #8d8d8d; font-size: 1.1rem;'>Upload a configuration file to begin the quantum-safe audit</p>
            <p style='color: #8d8d8d; font-size: 0.9rem; margin-top: 1rem;'>Supported formats: YAML, Terraform (.tf), JSON</p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div class='footer'>
        <p><strong>QS-Nav: Quantum-Safe Navigator</strong></p>
        <p>Built with ❤️ using IBM watsonx.ai | Securing the Future of Cryptography</p>
        <p style='margin-top: 1rem; font-size: 0.75rem;'>
            © 2026 | Powered by IBM Granite-3 & IBM Bob |
            <a href='https://www.ibm.com/quantum' target='_blank' style='color: #0f62fe; text-decoration: none;'>Learn More About IBM Quantum</a>
        </p>
    </div>
""", unsafe_allow_html=True)
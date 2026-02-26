import streamlit as st
import os

# Page config
st.set_page_config(
    page_title="Resume Analyser — AI-Powered Resume Analysis",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

:root {
    --bg: #1a1a2e;
    --surface: #16213e;
    --surface2: #0f3460;
    --border: #1f4068;
    --accent: #e94560;
    --accent2: #f39c12;
    --accent3: #2ecc71;
    --text: #ecf0f1;
    --text-muted: #95a5a6;
    --glow: rgba(233,69,96,0.15);
}

* { 
    font-family: 'DM Sans', sans-serif;
}

html {
    scroll-behavior: smooth;
}

.stApp {
    background: var(--bg);
    color: var(--text);
}

/* Hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem; max-width: 1200px; }

/* Hero Section with Animations */
.hero {
    text-align: center;
    padding: 3rem 0 2rem;
    position: relative;
    animation: fadeInUp 0.8s ease-out;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: 3.8rem;
    font-weight: 800;
    line-height: 1.1;
    background: linear-gradient(135deg, #ecf0f1 30%, #e94560 70%, #f39c12 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1.5rem;
    white-space: nowrap;
    animation: fadeInUp 0.8s ease-out 0.2s backwards;
    text-align: center;
}

@media (max-width: 768px) {
    .hero h1 {
        font-size: 2.5rem;
        white-space: normal;
    }
}

@media (max-width: 480px) {
    .hero h1 {
        font-size: 2rem;
        white-space: normal;
    }
}

.hero-sub {
    color: var(--text-muted);
    font-size: 1.05rem;
    font-weight: 300;
    max-width: 650px;
    margin: 0 auto 2rem;
    line-height: 1.7;
    text-align: center;
    animation: fadeInUp 0.8s ease-out 0.4s backwards;
    display: block;
    padding: 0 1rem;
}

/* Cards with Smooth Animations */
.card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.8rem;
    margin-bottom: 1.2rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.card:hover { 
    border-color: var(--accent);
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(233, 69, 96, 0.15);
}

.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* Score ring */
.score-display {
    display: flex;
    align-items: center;
    gap: 2rem;
    padding: 1.5rem;
    background: linear-gradient(135deg, rgba(108,99,255,0.08), rgba(67,233,123,0.05));
    border: 1px solid rgba(108,99,255,0.2);
    border-radius: 16px;
    margin: 1rem 0;
}
.score-number {
    font-family: 'Syne', sans-serif;
    font-size: 4rem;
    font-weight: 800;
    line-height: 1;
}
.score-high { color: var(--accent3); }
.score-mid { color: #f7b731; }
.score-low { color: var(--accent2); }

/* Tags */
.tag {
    display: inline-block;
    padding: 0.3rem 0.8rem;
    border-radius: 100px;
    font-size: 0.8rem;
    font-weight: 500;
    margin: 0.2rem;
}
.tag-green { background: rgba(67,233,123,0.12); color: #43e97b; border: 1px solid rgba(67,233,123,0.2); }
.tag-red { background: rgba(255,101,132,0.12); color: #ff6584; border: 1px solid rgba(255,101,132,0.2); }
.tag-blue { background: rgba(108,99,255,0.12); color: #a09cff; border: 1px solid rgba(108,99,255,0.2); }
.tag-yellow { background: rgba(247,183,49,0.12); color: #f7b731; border: 1px solid rgba(247,183,49,0.2); }

/* Section Headers with Animation */
.section-header {
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: var(--text);
    margin: 2rem 0 1rem;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid var(--border);
    animation: fadeInLeft 0.6s ease-out;
}

@keyframes fadeInLeft {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

/* Streamlit Button Animations */
.stButton > button {
    background: linear-gradient(135deg, var(--accent), #c0392b) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    padding: 0.6rem 2rem !important;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1) !important;
    letter-spacing: 0.03em !important;
    position: relative !important;
    overflow: hidden !important;
    box-shadow: 0 4px 15px rgba(233, 69, 96, 0.2) !important;
}

.stButton > button::before {
    content: '' !important;
    position: absolute !important;
    top: 50% !important;
    left: 50% !important;
    width: 0 !important;
    height: 0 !important;
    border-radius: 50% !important;
    background: rgba(255, 255, 255, 0.1) !important;
    transform: translate(-50%, -50%) !important;
    transition: width 0.6s, height 0.6s !important;
}

.stButton > button:hover::before {
    width: 300px !important;
    height: 300px !important;
}

.stButton > button:hover {
    transform: translateY(-2px) scale(1.03) !important;
    box-shadow: 0 8px 30px rgba(233, 69, 96, 0.4) !important;
}

.stButton > button:active {
    transform: translateY(0) scale(0.98) !important;
}

.stButton > button:focus {
    outline: 2px solid var(--accent) !important;
    outline-offset: 3px !important;
    box-shadow: 0 0 0 4px rgba(233, 69, 96, 0.2) !important;
}

/* Download Button Special Animation */
.stDownloadButton > button {
    background: linear-gradient(135deg, #2ecc71, #27ae60) !important;
    animation: pulse 2s infinite !important;
}

@keyframes pulse {
    0%, 100% {
        box-shadow: 0 4px 15px rgba(46, 204, 113, 0.3);
    }
    50% {
        box-shadow: 0 4px 25px rgba(46, 204, 113, 0.5);
    }
}

.stDownloadButton > button:hover {
    background: linear-gradient(135deg, #27ae60, #229954) !important;
    animation: none !important;
}

/* Input Fields with Smooth Transitions */
.stTextArea textarea, .stTextInput input {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: #ecf0f1 !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stTextArea textarea::placeholder, .stTextInput input::placeholder {
    color: var(--text-muted) !important;
    opacity: 0.7 !important;
}
.stTextArea textarea:focus, .stTextInput input:focus {
    border-color: var(--accent) !important;
    color: #ecf0f1 !important;
}
/* File Uploader with Hover Effect */
.stFileUploader {
    background: var(--surface2) !important;
    border: 2px dashed var(--border) !important;
    border-radius: 16px !important;
    transition: all 0.3s ease !important;
}

.stFileUploader:hover {
    border-color: var(--accent) !important;
    background: rgba(233, 69, 96, 0.05) !important;
}
/* Tabs with Smooth Transitions */
.stTabs [data-baseweb="tab-list"] {
    background: var(--surface) !important;
    border-radius: 12px !important;
    padding: 0.3rem !important;
    border: 1px solid var(--border) !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    color: var(--text-muted) !important;
    border-radius: 8px !important;
    transition: all 0.3s ease !important;
}

.stTabs [data-baseweb="tab"]:hover {
    background: rgba(233, 69, 96, 0.1) !important;
    color: var(--accent) !important;
}

.stTabs [aria-selected="true"] {
    background: var(--accent) !important;
    color: white !important;
    transform: scale(1.02);
}
.stSelectbox select, [data-baseweb="select"] {
    background: var(--surface2) !important;
    border-color: var(--border) !important;
    color: #ecf0f1 !important;
}
.stSelectbox div[data-baseweb="select"] > div {
    color: #ecf0f1 !important;
}
[data-testid="stExpander"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
}
.stAlert {
    border-radius: 10px !important;
}
hr { border-color: var(--border) !important; }
</style>
""", unsafe_allow_html=True)

# ─── Imports ──────────────────────────────────────────────────────────────────
from ocr.pdf_text_extractor import extract_text_from_pdf
from ocr.image_ocr import extract_text_from_image
from ai.hybrid_client import HybridAIClient
from ai.prompts import (
    RESUME_CLEANUP_PROMPT,
    SKILL_EXTRACTION_PROMPT,
    RESUME_SCORING_PROMPT,
    JD_MATCHING_PROMPT,
    IMPROVEMENT_PROMPT,
    CAREER_ROADMAP_PROMPT,
)
from utils.file_handler import detect_file_type, extract_docx_text
from utils.pdf_generator import generate_roadmap_pdf
import json, re

# ─── Helpers ──────────────────────────────────────────────────────────────────
def parse_json_response(text: str) -> dict:
    """Extract JSON from Gemini response, handling markdown code blocks."""
    text = re.sub(r"```(?:json)?", "", text).strip().strip("`").strip()
    try:
        return json.loads(text)
    except Exception:
        return {"raw": text}

def score_color(score):
    if score >= 75: return "score-high"
    if score >= 50: return "score-mid"
    return "score-low"

def render_tags(items, css_class="tag-blue"):
    return " ".join([f'<span class="tag {css_class}">{item}</span>' for item in items])

# ─── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>Resume Analyser</h1>
    <p class="hero-sub">Upload your resume. Get deep AI analysis, JD matching, and a personalized career roadmap — in seconds.</p>
</div>
""", unsafe_allow_html=True)

# ─── API Keys (from environment only) ────────────────────────────────────────
groq_api_key = os.environ.get("GROQ_API_KEY", "")
gemini_api_key = os.environ.get("GEMINI_API_KEY", "")

# ─── Main Layout ──────────────────────────────────────────────────────────────
col_left, col_right = st.columns([1, 1.4], gap="large")

with col_left:
    st.markdown('<div class="section-header">📂 Upload Resume</div>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Drop your resume here",
        type=["pdf", "png", "jpg", "jpeg", "docx"],
        help="Supports text PDFs, scanned PDFs, images, and DOCX files"
    )

    st.markdown('<div class="section-header">🎯 Job Description (Optional)</div>', unsafe_allow_html=True)

    jd_tab1, jd_tab2 = st.tabs(["✏️ Paste JD", "📄 Upload JD PDF"])
    with jd_tab1:
        jd_text = st.text_area(
            "Paste the job description",
            height=180,
            placeholder="Paste the full job description here for ATS matching and gap analysis...",
            label_visibility="collapsed"
        )
    with jd_tab2:
        jd_file = st.file_uploader("Upload JD as PDF", type=["pdf"], key="jd_pdf")
        if jd_file:
            jd_text = extract_text_from_pdf(jd_file.read())
            st.success(f"✅ JD loaded ({len(jd_text.split())} words)")

    st.markdown('<div class="section-header">🗺️ Career Target</div>', unsafe_allow_html=True)
    target_role = st.text_input(
        "Target Role",
        placeholder="e.g. Senior Data Scientist, Full Stack Engineer...",
        label_visibility="collapsed"
    )

    analyze_btn = st.button("⚡ Analyze Resume", use_container_width=True, type="primary")

# ─── Results ──────────────────────────────────────────────────────────────────
with col_right:
    if analyze_btn:
        if not uploaded_file:
            st.error("⚠️ Please upload a resume first.")
        elif not groq_api_key and not gemini_api_key:
            st.error("⚠️ Please set GROQ_API_KEY or GEMINI_API_KEY environment variable.")
        else:
            # Use hybrid client (Groq for text, Gemini for OCR)
            ai_client = HybridAIClient(groq_api_key=groq_api_key, gemini_api_key=gemini_api_key)
            raw_bytes = uploaded_file.read()
            file_type = detect_file_type(uploaded_file.name)

            # ── Step 1: Extract text
            with st.spinner("🔍 Extracting resume content..."):
                if file_type == "docx":
                    raw_text = extract_docx_text(raw_bytes)
                elif file_type == "image":
                    raw_text = extract_text_from_image(raw_bytes)
                else:  # pdf
                    raw_text = extract_text_from_pdf(raw_bytes)
                    if len(raw_text.strip()) < 100:
                        # Likely scanned, fallback to image OCR
                        raw_text = extract_text_from_image(raw_bytes, is_pdf=True)

            # ── Step 2: AI Cleanup
            with st.spinner("🧠 Cleaning and structuring text..."):
                clean_text = ai_client.generate(
                    RESUME_CLEANUP_PROMPT.format(raw_text=raw_text)
                )

            # ── Step 3: Skills
            with st.spinner("🎯 Extracting skills..."):
                skills_raw = ai_client.generate(
                    SKILL_EXTRACTION_PROMPT.format(resume_text=clean_text)
                )
                skills_data = parse_json_response(skills_raw)

            # ── Step 4: Score
            with st.spinner("📊 Scoring resume..."):
                score_raw = ai_client.generate(
                    RESUME_SCORING_PROMPT.format(resume_text=clean_text)
                )
                score_data = parse_json_response(score_raw)

            # ── Step 5: Improvements
            with st.spinner("✍️ Generating improvement tips..."):
                improve_raw = ai_client.generate(
                    IMPROVEMENT_PROMPT.format(resume_text=clean_text)
                )
                improve_data = parse_json_response(improve_raw)

            # ── Step 6: JD Matching (if provided)
            jd_data = None
            if jd_text and jd_text.strip():
                with st.spinner("🔗 Matching against job description..."):
                    jd_raw = ai_client.generate(
                        JD_MATCHING_PROMPT.format(
                            resume_text=clean_text,
                            job_description=jd_text
                        )
                    )
                    jd_data = parse_json_response(jd_raw)

            # ── Step 7: Career Roadmap
            roadmap_data = None
            if target_role:
                with st.spinner(f"🗺️ Building roadmap for {target_role}..."):
                    roadmap_raw = ai_client.generate(
                        CAREER_ROADMAP_PROMPT.format(
                            resume_text=clean_text,
                            target_role=target_role
                        )
                    )
                    roadmap_data = parse_json_response(roadmap_raw)

            # ── RENDER RESULTS ─────────────────────────────────────────────

            # Resume Score
            score_val = score_data.get("overall_score", score_data.get("score", 0))
            try:
                score_val = int(score_val)
            except:
                score_val = 0
            color_cls = score_color(score_val)
            grade = "Excellent" if score_val >= 80 else "Good" if score_val >= 60 else "Needs Work"

            st.markdown(f"""
            <div class="score-display">
                <div>
                    <div class="score-number {color_cls}">{score_val}</div>
                    <div style="color: var(--text-muted); font-size: 0.85rem;">out of 100</div>
                </div>
                <div>
                    <div style="font-family: 'Syne', sans-serif; font-size: 1.4rem; font-weight: 700;">{grade}</div>
                    <div style="color: var(--text-muted); font-size: 0.9rem; margin-top: 0.3rem;">{score_data.get('summary', 'AI-powered resume analysis complete.')}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Results tabs
            tabs = ["🧠 Analysis", "⚡ Skills", "✍️ Improve"]
            if jd_data:
                tabs.append("🎯 JD Match")
            if roadmap_data:
                tabs.append("🗺️ Roadmap")

            result_tabs = st.tabs(tabs)
            tab_idx = 0

            # ── Analysis tab
            with result_tabs[tab_idx]:
                tab_idx += 1
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown('<div class="card-title">💪 Strengths</div>', unsafe_allow_html=True)
                    for s in score_data.get("strengths", []):
                        st.markdown(f"✅ {s}")
                    st.markdown("</div>", unsafe_allow_html=True)
                with col2:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown('<div class="card-title">⚠️ Weaknesses</div>', unsafe_allow_html=True)
                    for w in score_data.get("weaknesses", []):
                        st.markdown(f"🔸 {w}")
                    st.markdown("</div>", unsafe_allow_html=True)

                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown('<div class="card-title">📋 ATS Compatibility</div>', unsafe_allow_html=True)
                ats = score_data.get("ats_compatibility", {})
                if isinstance(ats, dict):
                    ats_score = ats.get("score", "N/A")
                    st.markdown(f"**ATS Score:** `{ats_score}`")
                    for tip in ats.get("tips", []):
                        st.markdown(f"→ {tip}")
                else:
                    st.markdown(str(ats))
                st.markdown("</div>", unsafe_allow_html=True)

                with st.expander("📄 Cleaned Resume Text"):
                    st.text(clean_text[:3000] + ("..." if len(clean_text) > 3000 else ""))

            # ── Skills tab
            with result_tabs[tab_idx]:
                tab_idx += 1
                tech = skills_data.get("technical_skills", [])
                soft = skills_data.get("soft_skills", [])
                tools = skills_data.get("tools_and_technologies", [])

                if tech:
                    st.markdown("**🔧 Technical Skills**")
                    st.markdown(render_tags(tech, "tag-blue"), unsafe_allow_html=True)
                if soft:
                    st.markdown("**🤝 Soft Skills**")
                    st.markdown(render_tags(soft, "tag-green"), unsafe_allow_html=True)
                if tools:
                    st.markdown("**🛠️ Tools & Technologies**")
                    st.markdown(render_tags(tools, "tag-yellow"), unsafe_allow_html=True)

                years = skills_data.get("years_of_experience", "")
                domain = skills_data.get("domain", "")
                if years or domain:
                    st.info(f"📅 **Experience:** {years} &nbsp;|&nbsp; **Domain:** {domain}")

            # ── Improve tab
            with result_tabs[tab_idx]:
                tab_idx += 1
                sections = improve_data.get("section_improvements", {})
                if isinstance(sections, dict):
                    for section, tips in sections.items():
                        with st.expander(f"📌 {section}"):
                            if isinstance(tips, list):
                                for tip in tips:
                                    st.markdown(f"• {tip}")
                            else:
                                st.markdown(str(tips))
                elif isinstance(sections, list):
                    for item in sections:
                        st.markdown(f"• {item}")

                bullets = improve_data.get("bullet_rewrites", [])
                if bullets:
                    st.markdown("**⚡ Suggested Bullet Rewrites**")
                    for b in bullets[:5]:
                        if isinstance(b, dict):
                            st.markdown(f"❌ *Before:* {b.get('before', '')}")
                            st.markdown(f"✅ *After:* {b.get('after', '')}")
                            st.divider()

                verbs = improve_data.get("action_verbs", [])
                if verbs:
                    st.markdown("**💥 Stronger Action Verbs**")
                    st.markdown(render_tags(verbs, "tag-blue"), unsafe_allow_html=True)

            # ── JD Match tab
            if jd_data:
                with result_tabs[tab_idx]:
                    tab_idx += 1
                    match_score = jd_data.get("match_score", 0)
                    try: match_score = int(match_score)
                    except: match_score = 0
                    color_cls2 = score_color(match_score)

                    st.markdown(f"""
                    <div class="score-display">
                        <div>
                            <div class="score-number {color_cls2}">{match_score}%</div>
                            <div style="color: var(--text-muted); font-size: 0.85rem;">JD Match</div>
                        </div>
                        <div style="color: var(--text-muted);">{jd_data.get('summary', '')}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    c1, c2 = st.columns(2)
                    with c1:
                        matching = jd_data.get("matching_keywords", [])
                        if matching:
                            st.markdown("**✅ Matching Keywords**")
                            st.markdown(render_tags(matching, "tag-green"), unsafe_allow_html=True)
                    with c2:
                        missing = jd_data.get("missing_skills", [])
                        if missing:
                            st.markdown("**❌ Missing Skills**")
                            st.markdown(render_tags(missing, "tag-red"), unsafe_allow_html=True)

                    weak = jd_data.get("weak_alignment", [])
                    if weak:
                        st.markdown("**⚠️ Weak Alignment Areas**")
                        for w in weak:
                            st.markdown(f"→ {w}")

                    ats_feedback = jd_data.get("ats_feedback", [])
                    if ats_feedback:
                        st.markdown("**🤖 ATS Optimization Tips**")
                        for tip in ats_feedback:
                            st.markdown(f"• {tip}")

            # ── Roadmap tab
            if roadmap_data:
                with result_tabs[tab_idx]:
                    current_level = roadmap_data.get("current_level", "Beginner")
                    st.info(f"**Current Level:** {current_level} → **Target:** {target_role}")

                    stages = roadmap_data.get("stages", [])
                    for stage in stages:
                        label = stage.get("level", "")
                        timeline = stage.get("timeline", "")
                        skills_list = stage.get("skills", [])
                        resources = stage.get("resources", [])

                        with st.expander(f"📍 {label}  —  ⏱️ {timeline}"):
                            if skills_list:
                                st.markdown("**Skills to acquire:**")
                                st.markdown(render_tags(skills_list, "tag-blue"), unsafe_allow_html=True)
                            if resources:
                                st.markdown("**📚 Learning Resources:**")
                                for r in resources:
                                    st.markdown(f"• {r}")

                    # PDF Download
                    pdf_bytes = generate_roadmap_pdf(target_role, roadmap_data)
                    st.download_button(
                        label="📥 Download Career Roadmap PDF",
                        data=pdf_bytes,
                        file_name=f"career_roadmap_{target_role.replace(' ', '_')}.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
    else:
        # Empty state
        st.markdown("""
        <div style="
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 400px;
            color: var(--text-muted);
            text-align: center;
            border: 2px dashed var(--border);
            border-radius: 20px;
            background: var(--surface);
        ">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🤖</div>
            <div style="font-family: 'Syne', sans-serif; font-size: 1.2rem; font-weight: 700; color: var(--text); margin-bottom: 0.5rem;">
                Your analysis will appear here
            </div>
            <div style="font-size: 0.9rem; max-width: 300px; line-height: 1.6;">
                Upload your resume and click <strong>Analyze Resume</strong> to get started.
            </div>
        </div>
        """, unsafe_allow_html=True)

# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; color: var(--text-muted); font-size: 0.8rem; margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border);">
    Built with Responsibility
</div>
""", unsafe_allow_html=True)

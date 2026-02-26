"""
Smart Prompt Architecture — one prompt per responsibility.
Each prompt returns clean, structured JSON for easy parsing.
"""

# ─── 1. Resume Cleanup ──────────────────────────────────────────────────────
RESUME_CLEANUP_PROMPT = """
You are a resume text cleaning specialist.

The following text was extracted from a resume via PDF parsing or OCR.
It may contain: broken lines, garbled characters, merged words, 
formatting artifacts, or OCR errors.

Your job:
1. Fix spelling and OCR errors
2. Reconstruct proper sentence structure
3. Restore section headings (EXPERIENCE, EDUCATION, SKILLS, etc.)
4. Remove duplicate text and artifacts
5. Preserve all real content — do NOT add or invent information

Return ONLY the cleaned resume text. No commentary.

--- RAW TEXT START ---
{raw_text}
--- RAW TEXT END ---
"""

# ─── 2. Skill Extraction ────────────────────────────────────────────────────
SKILL_EXTRACTION_PROMPT = """
You are a technical recruiter analyzing a resume for skills.

Analyze the resume below and extract:
1. Technical skills (programming languages, frameworks, databases, cloud, etc.)
2. Soft skills (communication, leadership, problem-solving, etc.)
3. Tools & technologies (specific software, platforms, IDEs, etc.)
4. Years of total experience (estimate if not explicit)
5. Primary domain/industry

Return ONLY valid JSON in this exact format:
{{
  "technical_skills": ["Python", "React", ...],
  "soft_skills": ["Team Leadership", ...],
  "tools_and_technologies": ["Git", "Docker", ...],
  "years_of_experience": "5 years",
  "domain": "Software Engineering / FinTech"
}}

--- RESUME ---
{resume_text}
"""

# ─── 3. Resume Scoring ──────────────────────────────────────────────────────
RESUME_SCORING_PROMPT = """
You are an expert resume evaluator and career coach.

Score the following resume on a scale of 0-100 based on:
- Clarity and formatting (20pts)
- Quantified achievements and impact (20pts)
- Skills relevance and depth (20pts)
- Professional summary quality (15pts)
- ATS compatibility (15pts)
- Overall presentation (10pts)

Return ONLY valid JSON in this exact format:
{{
  "overall_score": 78,
  "summary": "Strong technical resume with good project descriptions but lacks quantified metrics.",
  "strengths": [
    "Clear section structure",
    "Strong technical skill set",
    "Relevant project experience"
  ],
  "weaknesses": [
    "No measurable achievements (numbers/percentages)",
    "Summary section is generic",
    "Missing LinkedIn/GitHub links"
  ],
  "ats_compatibility": {{
    "score": "72/100",
    "tips": [
      "Use standard section headings",
      "Add more job-relevant keywords",
      "Avoid tables and graphics"
    ]
  }}
}}

--- RESUME ---
{resume_text}
"""

# ─── 4. JD Matching ──────────────────────────────────────────────────────────
JD_MATCHING_PROMPT = """
You are an ATS (Applicant Tracking System) and job matching expert.

Compare the resume against the job description and provide a detailed match analysis.

Return ONLY valid JSON in this exact format:
{{
  "match_score": 72,
  "summary": "Good alignment on technical skills but missing cloud and DevOps experience.",
  "matching_keywords": ["Python", "Machine Learning", "SQL", "Data Analysis"],
  "missing_skills": ["AWS", "Docker", "Kubernetes", "CI/CD"],
  "weak_alignment": [
    "Leadership experience mentioned but not detailed",
    "Communication skills not demonstrated with examples"
  ],
  "ats_feedback": [
    "Add 'cloud computing' keyword — appears 4x in JD",
    "Mirror the title 'Senior Data Scientist' in your summary",
    "Include 'A/B testing' which appears in required skills"
  ]
}}

--- RESUME ---
{resume_text}

--- JOB DESCRIPTION ---
{job_description}
"""

# ─── 5. Improvement Suggestions ─────────────────────────────────────────────
IMPROVEMENT_PROMPT = """
You are a professional resume writer and career coach.

Analyze the resume and provide actionable, specific improvement suggestions.

Return ONLY valid JSON in this exact format:
{{
  "section_improvements": {{
    "Professional Summary": [
      "Start with your years of experience and key expertise",
      "Add a specific achievement or differentiator"
    ],
    "Work Experience": [
      "Use STAR format: Situation, Task, Action, Result",
      "Add metrics to at least 3 bullet points per role"
    ],
    "Skills": [
      "Group skills by category (Languages, Frameworks, Tools)",
      "Remove generic soft skills from technical section"
    ],
    "Education": [
      "Add relevant coursework or GPA if above 3.5",
      "Include certifications with dates"
    ]
  }},
  "bullet_rewrites": [
    {{
      "before": "Worked on backend APIs",
      "after": "Engineered 12 RESTful APIs using Node.js, reducing response time by 40%"
    }},
    {{
      "before": "Helped improve team processes",
      "after": "Implemented Agile sprint ceremonies for 8-person team, boosting delivery velocity by 25%"
    }}
  ],
  "action_verbs": ["Engineered", "Architected", "Spearheaded", "Optimized", "Delivered", "Scaled", "Reduced", "Grew"],
  "quantification_tips": [
    "Add team sizes where you led or collaborated",
    "Include % improvement for any optimizations",
    "State budget or revenue impact where applicable"
  ]
}}

--- RESUME ---
{resume_text}
"""

# ─── 6. Career Roadmap ───────────────────────────────────────────────────────
CAREER_ROADMAP_PROMPT = """
You are a senior career advisor and skills development expert.

Based on the resume, create a personalized career roadmap to achieve the target role.
The roadmap should be realistic, specific, and achievable.

Return ONLY valid JSON in this exact format:
{{
  "current_level": "Mid-Level Developer",
  "target_role": "{target_role}",
  "gap_summary": "Strong Python foundation but needs cloud, ML ops, and leadership experience.",
  "stages": [
    {{
      "level": "Beginner",
      "timeline": "0-3 months",
      "skills": ["Docker basics", "AWS fundamentals", "SQL optimization"],
      "resources": [
        "AWS Cloud Practitioner — free on AWS Training portal",
        "Docker Getting Started — official docs",
        "Mode Analytics SQL Tutorial — free online"
      ],
      "milestones": ["Deploy a containerized app to AWS", "Complete AWS Cloud Practitioner cert"]
    }},
    {{
      "level": "Intermediate",
      "timeline": "3-9 months",
      "skills": ["Kubernetes", "MLflow", "Spark basics", "System Design"],
      "resources": [
        "Kubernetes The Hard Way — GitHub (free)",
        "MLflow documentation and tutorials",
        "Designing Data-Intensive Applications — book"
      ],
      "milestones": ["Build an end-to-end ML pipeline", "Lead a small project or feature"]
    }},
    {{
      "level": "Advanced",
      "timeline": "9-18 months",
      "skills": ["Distributed systems", "Team leadership", "Architecture design", "Stakeholder management"],
      "resources": [
        "Staff Engineer book by Will Larson",
        "System Design Interview — book + free resources",
        "Volunteer for tech lead role on a project"
      ],
      "milestones": ["Lead a cross-functional initiative", "Present technical decision to leadership", "Mentor junior engineers"]
    }}
  ]
}}

--- RESUME ---
{resume_text}

Target Role: {target_role}
"""

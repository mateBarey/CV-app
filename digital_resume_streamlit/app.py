from pathlib import Path
import base64
from plausible_patch import patch_plausible
patch_plausible()
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# --- BADGE CONFIG ---
BADGE_PAGE = "https://credentials.databricks.com/3177ab6f-1676-4b64-ba17-ef057a259eaf#acc.0jAGLJBc"
BADGE_IMG_BIG = "https://templates.images.credential.net/17165027227082916957584247676509.png"

# --- PATH SETTINGS ---
current_dir = Path(__file__).resolve().parent
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | George Cubas"
PAGE_ICON  = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

NAME        = "George Cubas"
DESCRIPTION = (
    "Engineer and Python Developer with more than 10 years of experience.\n"
    "Experienced in large scale million-dollar projects utilizing cross-functional team collaboration.\n"
    "Skilled in AI, ML Web development, Engineering Economics, with 4 years of experience in the Energy Sector"
)
EMAIL = "georgeraulc@email.com"

# Social links (no badge here)
SOCIAL_MEDIA = {
    "LinkedIn": {
        "url":  "https://www.linkedin.com/in/george-cubas-55113a29/",
        "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg"
    },
    "GitHub": {
        "url":  "https://github.com/mateBarey",
        "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"
    }
}

# Inject Plausible analytics
components.html(
    """
    <script defer data-domain="digital-resume-ms4l.onrender.com"
            src="https://plausible.io/js/script.js"></script>
    """,
    height=0,
)

# Load resume PDF and convert to base64 for download link
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    b64_pdf = base64.b64encode(PDFbyte).decode()

# Projects (simple links)
PROJECTS = {
    "🏆 Generative AI (RAG using Weaviate, Dspy)": 
        "https://github.com/mateBarey/Rag-GEN-AI",
    "🏆 Apache Spark Prediction Pipeline": 
        "https://github.com/mateBarey/Apache-Spark-IOT-Prediction-Pipeline",
    "🏆 Actor Critic Reinforcement Learning NN": 
        "https://github.com/mateBarey/Reinforcement-Learning",
}

# Traditional training & certifications (renders under Certifications section)
TRAINING_AND_CERT = {
    "🏆 IBM – AI Engineering Professional":
        '<a href="https://www.coursera.org/account/accomplishments/specialization/certificate/XJ95RYV4Z5TC" target="_blank">'
        'IBM – AI Engineering Professional</a>',
    "🏆 Google – Machine Learning":
        '<a href="https://www.coursera.org/account/accomplishments/specialization/certificate/P57BYGZPYANV" target="_blank">'
        'Google – Machine Learning</a>',
    "🏆 Google – Reinforcement Learning":
        '<a href="https://www.coursera.org/account/accomplishments/certificate/AGP9TE8AFPSC" target="_blank">'
        'Google – Reinforcement Learning</a>',
    "🏆 Databricks – Generative AI App Deployment & Monitoring":
        '<a href="https://www.linkedin.com/in/george-cubas-55113a29/overlay/1744050680291/single-media-viewer?type=DOCUMENT" target="_blank">'
        'Databricks – Generative AI App Deployment & Monitoring</a>'
}

# Load CSS and profile picture
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
profile_pic = Image.open(profile_pic_path)

# --- HERO SECTION ---
col1, col2 = st.columns(2)

# Profile image
with col1:
    st.image(profile_pic, width=230)

# Title, description, resume, badge, email, socials
with col2:
    # Name & description
    st.title(NAME)
    st.write(DESCRIPTION)

    # Resume Download
    st.markdown(
        f"""
        <div style='margin-top:10px;'>
          <a id="download-resume"
             href="data:application/octet-stream;base64,{b64_pdf}"  
             download="{resume_file.name}"
             style="font-size:17px; color:inherit; background-color:transparent;
                    border:1px solid currentColor; padding:8px 14px;
                    border-radius:8px; text-decoration:none;
                    display:inline-block; font-weight:500;
                    transition:all 0.2s ease-in-out;">
            📄 Download Resume
          </a>
          <script>
            const btn = document.getElementById("download-resume");
            if (btn && window.plausible) {{ btn.addEventListener("click", () => plausible("Download Resume")); }}
          </script>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Badge + Email
    st.markdown(
        f"""
        <style>
          .badge-link img {{ vertical-align:middle; margin-right:12px; }}
          .email-link {{ vertical-align:middle; color:inherit; text-decoration:none; font-size:16px; }}
          .email-link:hover {{ color:#1f77b4; }}
        </style>
        <div style="margin-top:1rem; display:flex; align-items:center;">
          <a class="badge-link" href="{BADGE_PAGE}" target="_blank">
            <img src="{BADGE_IMG_BIG}" alt="Gen AI Badge" width="60" />
          </a>
          <a class="email-link" href="mailto:{EMAIL}">📫 {EMAIL}</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Social icons
    cols = st.columns(len(SOCIAL_MEDIA))
    for idx, (platform, meta) in enumerate(SOCIAL_MEDIA.items()):
        cols[idx].markdown(
            f"""
            <a href="{meta['url']}" target="_blank" 
               onclick="window.plausible && plausible('Click {platform}')">
              <img src="{meta['icon']}" width="24" style="vertical-align:middle; margin-right:8px;" />
              {platform}
            </a>
            """,
            unsafe_allow_html=True
        )

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 6+ Years of experience extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and SQL
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills")
st.markdown(
    """
👩‍💻 Programming:
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="20">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/r/r-original.svg" width="20">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/ruby/ruby-plain.svg" width="20">
  &nbsp; Python, Rust, R, Ruby, SQL, Scikit-learn, Pandas, Polars
""",
    unsafe_allow_html=True
)
st.markdown(
    """
📊 Data Visualization:
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg" width="20" style="vertical-align:middle; margin-right:6px;">
  Dash, Streamlit, Plotly
""",
    unsafe_allow_html=True
)
st.markdown("""
🧠 Modeling: Logistic Regression, RL, Neural Nets, LLM, Xgboost, Natural Evolution
""")
st.markdown("""
🗄️ Databases:
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="20">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" width="20">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" width="20">
&nbsp; Postgres, MongoDB, MySQL, SqlServer
""", unsafe_allow_html=True)
st.markdown("""
🧱 Frameworks:
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="20">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="20">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="20">
&nbsp; FastAPI, Databricks, Django, Flask
""", unsafe_allow_html=True)
st.markdown("""
🔧 DevOps & Cloud:
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="20">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="20">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" width="20">
&nbsp; Git, Docker, GitHub Actions, Linux
""", unsafe_allow_html=True)
st.markdown("""
📚 Analytics:
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apache/apache-original.svg" width="20">
&nbsp; Databricks, Apache Spark
""", unsafe_allow_html=True)



# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Python Developer | EOG Resources**")
st.write("03/2024 - 09/2024")
st.write(
    """
- ► Developed and scaled Oil and Gas economic models, focusing on cost recovery and profit split for a new application using Polars.
- ► Optimized and adapted models by leveraging Polars' parallelized functions for enhanced performance.
- ► Created Depreciation, Depletion, and Amortization (DDA) functions to improve existing cash flow models.
- ► Implemented Net Present Value Index (NPVI) and Profitability Index (PVI) calculations using Polars for accurate cash flow analysis.
- ► Contributed to the debugging and enhancement of the Planning Economics Engine, resolving critical bugs and updating the codebase.
- ► Played a key role in evaluating new global assets by integrating updated income tax and tangible depreciation data for economic feasibility assessment.
- ► Designed and developed new FastAPI endpoints and stored procedures for advanced scenario sensitivity analysis.
"""
)
# --- JOB 1
st.write("🚧", "**Python Developer | Compbuss**")
st.write("08/2023 - Present")
st.write(
    """
- ► Design and build AI services including Image Learning and Classifiers using natural evolution and computer vision methods per OPENAI research paper and deploy using FASTAPI.
- ► Build RAG using dolphin llama model from Ollama and use Dspy with weaviate to build a rag system for the LLM so that n sources could be added and the model make inferences based on these sources
- ► Design, build, and maintain efficient, reusable, reliable code.
- ► Write and maintain code following engineering best practices using CI/CD KISS tools.
- ► Write unit and integration tests using test driven development methodologies.
"""
)

# --- JOB 1
st.write("🚧", "**Python Developer | University of Virginia**")
st.write("03/2022 - 12/2022")
st.write(
    """
- ► Generate programs for ETL process for Office of Sponsored Programs
- ► Utilize Pandas , nosql and sqlalchemy to streamline the ETL process for Awards, Proposals and agreements data for full end to end Project implementation using analysis, design, modeling and testing for server side scripts and applications.
- ► Build crawlers to verify the quality of the frontend data and see what percentage of data needs to be corrected
- ► Use Multiprocessing(bypassing GIL) and asyncio modules when applicable for parallelization/concurrent  performance in various scripts
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Python Developer | Kinstone Investment Properties**")
st.write("07/2019 - 03/2022")
st.write(
    """
- ► Model valuation and acquisition of new properties using Pandas, NumPy and Scikit-learn in Jupyter Notebook
- ► Utilize BeautifulSoup and Selenium to scrape Freddie Mac Multi Family Index information and Case Shiller Housing Price index information adjusted for real inflation. Construct Bridge API’s to schedule updated cost valuations for properties in certain areas of Houston using the Zillow API.
- ► Apply Monte Carlo Analysis using NumPy for building a real time and cost estimate for predicting a Levered and Unlevered IRR.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Python Engineer | Mass Action Engineering**")
st.write("01/2019 - 07/2019")
st.write(
    """
- ► Created Python scripts for processing all P & ID's and PFD's .
- ► Designed a process calculation utilizing NumPy, Pandas and Jupyter Notebook. The scripts were modularized to have each unit process within its own class using OOP principles.
- ► Worked with a tech team to effectively simulate the Free Radical Emulsion Polymerization of the monomer Vinylidene Fluoride.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Python Engineer | Occidental Petroleum**")
st.write("01/2019 - 07/2019")
st.write(
    """
- ► Planned various Field Development and Section Development plans in NM and TX areas.
- ► Built an Anti-Collision Risk Analysis Web application using Django Framework that calculated the risk between Planned Well Spreadsheet and Existing wells.
- ► Created a script that used a pretrained Neural network to extract Scanned Well File Data to a csv using a Linux shell script.
- ► Built scrapers using beautifulsoup4 and Selenium.
- ► Designed a drilling web application using Django and a machine learning algorithm that modeled drawdown for Production using Scikit-learn.
- ► Developed models using ArcGIS, Python, Arcpy , SQL, Excel
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects ")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Training and Certifications ")
st.write("---")
for project, link in TRAINING_AND_CERT.items():
    st.write(f"[{project}]({link})")

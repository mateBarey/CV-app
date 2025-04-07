from pathlib import Path
import base64
import streamlit.components.v1 as components
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).resolve().parent
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | George Cubas"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
NAME = "George Cubas"
DESCRIPTION = """
Engineer and Python Developer with more than 10 years of experience.
Experienced in large scale million-dollar projects utilizing cross-functional team collaboration.
Skilled in AI, ML Web development, Engineering Economics, with 4 years of experience in the Energy Sector
"""
EMAIL = "georgeraulc@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": {
        "url": "https://www.linkedin.com/in/george-cubas-55113a29/",
        "icon": "https://cdn-icons-png.flaticon.com/512/174/174857.png"
    },
    "GitHub": {
        "url": "https://github.com/mateBarey",
        "icon": "https://cdn-icons-png.flaticon.com/512/733/733553.png"
    }
}

# Inject Plausible <script> into head using components.html
components.html(
    """
    <script defer data-domain="digital-resume-ms4l.onrender.com" src="https://plausible.io/js/script.file-downloads.outbound-links.tagged-events.js"></script>
    <script>
    window.plausible = window.plausible || function() {
      (window.plausible.q = window.plausible.q || []).push(arguments)
    }
    </script>
    """,
    height=0,
)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    b64_pdf = base64.b64encode(PDFbyte).decode()
    
#remember to add a selenium crawler and beautifulsoup code
PROJECTS = {
    "🏆 DGenerative AI (RAG using Weaviate, Dspy) - A framework for integrating and retrieving information from multiple sources to enrich a LLM knowledge base and enhance its contextual accuracy": "https://github.com/mateBarey/Rag-GEN-AI",
    "🏆 Apache Spark Prediction Pipeline - use IOT data and spark to predict Pressure": "https://github.com/mateBarey/Apache-Spark-IOT-Prediction-Pipeline",
    "🏆 Actor Critic Reinforcement Learning NN - A reinforcement algorithm that uses an actor for finding the best policy and critic which enables finding the best probability associated with each action to take in order to solve the Cart Pole Problem ": "https://github.com/mateBarey/Reinforcement-Learning",

}

TRAINING_AND_CERT = {
    "🏆 IBM - AI Engineering Professional": "https://www.coursera.org/account/accomplishments/specialization/certificate/XJ95RYV4Z5TC",
    "🏆 Google - Machine Learning ": "https://www.coursera.org/account/accomplishments/specialization/certificate/P57BYGZPYANV",
    "🏆 Google - Reinforcement Learning ": "https://www.coursera.org/account/accomplishments/certificate/AGP9TE8AFPSC",
    "🏆 Databricks - Generative AI Application Deployment and Monitoring ": "https://www.linkedin.com/in/george-cubas-55113a29/overlay/1744050680291/single-media-viewer?type=DOCUMENT&profileId=ACoAAAXklY0Bqebj26kPZcGeVDc2Lwkgkw-Blmk&lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3B%2B6uqYaMwRTOebuqj%2BWU04g%3D%3D",

}




# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    components.html(f"""
    <style>
      .resume-button {{
        display: inline-block;
        background-color: #1f77b4;
        color: white;
        padding: 10px 16px;
        text-decoration: none;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 500;
        transition: background-color 0.3s;
      }}
      .resume-button:hover {{
        background-color: #145a86;
      }}
    </style>

    <a id="download-resume" class="resume-button" 
       href="data:application/octet-stream;base64,{b64_pdf}" 
       download="{resume_file.name}">
        📄 Download Resume
    </a>

    <script>
      const dl = document.getElementById("download-resume");
      dl.addEventListener("click", function() {{
        if (window.plausible) {{
          window.plausible("Download Resume");
        }}
      }});
    </script>
    """, height=80)
    st.markdown(f"<p style='margin-top: 12px;'>📫 {EMAIL}</p>", unsafe_allow_html=True)





# --- SOCIAL LINKS ---
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, meta) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].markdown(
        f"""
        <a href="{meta['url']}" target="_blank" onclick="window.plausible && window.plausible('Click GitHub')">
            <img src="{meta['icon']}" width="24" style="vertical-align: middle; margin-right: 8px;">
            {platform}
        </a>
        """,
        unsafe_allow_html=True
    )



# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 6+ Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and SQL
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.markdown("""
👩‍💻 Programming:
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg" width="20">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/r/r-original.svg" width="20">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/ruby/ruby-plain.svg" width="20">
 &nbsp; Python, Rust, R, Ruby, SQL, Scikit-learn, Pandas, Polars
""", unsafe_allow_html=True)
st.markdown("""
📊 Data Visualization:
<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2ZmZjtlbmFibGUtYmFja2dyb3VuZDphY2N1bXVsYXRlfTwvc3R5bGU+PC9kZWZzPjx0aXRsZT5wbG90bHk8L3RpdGxlPjxwYXRoIGQ9Ik0zNTMuMjc3LDI1NC42NTlhODMuNDU0LDgzLjQ1NCwwLDAsMS01OS4xNzUtMjQuNTM2Yy0zMy4wMDQsMC02MCwyNy45OTYtNjAsNjMsMCwuMTQyLDAsLjI4MywwLC40MjVjMCwzNS4wMDQsMjYuOTk2LDYzLDYwLDYzLDMyLjQ2MiwwLDYwLTI4LjAzMyw2MC02MywwLS4xNDIsMC0uMjgzLDAtLjQyNUM0MTMuMjc3LDI4Mi42NTUsMzg2LjI4LDI1NC42NTksMzUzLjI3NywyNTQuNjU5Wk0yNzcuMjczLDE2MC42NTlIMjA1LjI3Yy0zMy4wMDQsMC02MCwyNy45OTYtNjAsNjMsMCwuMTQyLDAsLjI4MywwLC40MjVjMCwzNS4wMDQsMjYuOTk2LDYzLDYwLDYzaDcxLjk5M2MzMi45OTMsMCw1OS45ODktMjcuOTk2LDU5LTMzLjAwMUMzMzguMjU3LDE4OC42NTUsMzEwLjI2LDYwLjY1OSwyNzcuMjczLDE2MC42NTlaTTIxMS4yNzMsNDAwLjY1OUgxNDMuMjdhNjMuMDAzLDYzLjAwMywwLDAsMS02MC02M2MwLS4xNDIsMC0uMjgzLDAtLjQyNUM4My4yNzcsMjY4LjY1NSwxMTAsMjQwLjY1OSwxNDMuMjcsMjQwLjY1OWg2OC4wMDNjMzIuOTkzLDAsNTkuOTg5LDI3Ljk5Niw1OSw2M3MtMjYuMDA3LDYzLTU5LDYzWiIgY2xhc3M9ImNscy0xIi8+PC9zdmc+" width="20" style="vertical-align: middle; margin-right: 6px;">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAMAAAC7IEhfAAABFVBMVEX///8AAAD7+/tVVVU/Pz/Hx8e2trZISEj4+Pj5+fnl5eWhobF5eXlHR0dvb2/s7OxLS0vV1dXQ0NDPz8/e3t7u7u5PT0+jo6PZ2dme3t6ZmZkxMTH19fXc3NzX19eCgoJ+fn7U1NRSUlKJiYnW1tZycnIuLi6FhYU9PT2oqKjY2NjPz8+hoaH29vbZ2dnY2NiampqSkpLExMSeHg6GAAABEklEQVQ4y+3R0Q7CMAxFURewRMB9BZXg//8X3GEtYJghM+R6Hc5sZZnuPIqO9zBvMFnQ+M57CPOSJ7GqgGzmn0DkPMT3qBTckPvSKx7YIQjRvmgRMOrEJhBZJ1whuQOEzEqcLWAhrH0CrcAgF7S3Q9AdLF1eUDnM+j1OZbLkYkX7rNm93Mu0pd/nPZK5Ykck8vZKJmdj7npq9yWqpIb0iIYQ0u0n+0wZoCnEkhFUwAAAABJRU5ErkJggg==" width="20" style="vertical-align:middle; margin-right:6px;">
&nbsp; Dash, Streamlit, Plotly
""", unsafe_allow_html=True)
st.markdown("""
🧠 Modeling: Logistic Regression, RL, Neural Nets, LLM, Xgboost, Natural Evoluation
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
st.write("🚧", "**Python Developer | University of Virginia**")
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
- ► Model valuation and acquisition of new properties using Pandas, NumPy and Sci-kitlearn in Jupyter Notebook
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
- ►Created Python scripts for processing all P & ID's and PFD's .
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
- ► Designed a drilling web application using Django and a machine learning algorithm that modeled drawdown for Production using Scikit-learn.
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

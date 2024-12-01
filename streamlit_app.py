import streamlit as st
import plotly.express as px
from PIL import Image
from utils.utils import social
import pandas as pd
st.set_page_config(layout="wide",page_title='Dogukan Dogru', page_icon=':green_book')


def professional_experience():

    #Deloitte Switzerland

    st.title("Data Scientist")
    st.header("Deloitte, Switzerland")
    st.subheader("April 2023 - Current")

    st.markdown("""
    - Developed and deployed an XGBoost-based payment prediction model, enabling proactive receivables management and automated early warning signals
    - Built scalable ML pipelines using Python and SQL, delivering MVP solutions within 3-4 day sprints
    - Stakeholder decisions are now driven by my custom Power BI solutions, integrating Azure PySpark for real-time analytics
    - Architected scalable data infrastructure that reduced model deployment time by 40% while maintaining robust data quality standards
    """)

    st.markdown("---")
    
    #Allianz Turkey

    st.title("Data Scientist")
    st.header("Allianz, Istanbul")
    st.subheader("June 2021 - April 2023")

    st.markdown("""
    - Automated Excel and SAS reports using Python and Apache Airflow, implementing enterprise-wide automation infrastructure
    - Developed Superset dashboards for C-level KPI tracking and designed predictive ML models for litigation outcomes
    - Created and deployed ML models achieving 10% litigation reduction and 5% increase in case win rates
    """)

    st.markdown("---")

    #Istanbul Economics Research and Consultancy    
    st.title("Data Analyst")
    st.header("Istanbul Economics Research, Istanbul")
    st.subheader("June 2020 - June 2021")

    st.markdown("""
    - Managed survey projects for major clients including Central Bank of Turkey and Harvard Business School
    - Designed and executed social media campaigns, analyzing public perception through survey data
    - Automated survey analysis processes using Python and R, while developing company's web presence
    """)

    st.markdown("---")

    #Politika Atlasi    
    st.title("Co-Founder")
    st.header("Politika Atlası, Istanbul")
    st.subheader("August 2017 - June 2020")

    st.markdown("""
    - politikaatlasi.com was an online newsletter startup which gathered interesting and important articles on many topics from well-known journal websites such as nytimes.com, ft.com and wired.com
    - As the founder/editor, I translated these articles into Turkish, after analyzing them
    - My main tasks were pitching content strategies, reviewing grammar and syntax error with quality standards and managing team of 4 personnel to deliver consistent, accurate and fascinating content
    """)

def skills():
    st.title('Skills & Expertise')
    
    skills_data = pd.DataFrame([
        # ML/AI
        {"name": "Skills", "parent": "", "proficiency": "", "category": "root"},
        {"name": "ML/AI", "parent": "Skills", "proficiency": "", "category": "ml"},
        {"name": "PyTorch", "parent": "ML/AI", "proficiency": "Advanced", "category": "ml"},
        {"name": "XGBoost", "parent": "ML/AI", "proficiency": "Expert", "category": "ml"},
        {"name": "LSTM", "parent": "ML/AI", "proficiency": "Advanced", "category": "ml"},
        {"name": "Classification Models", "parent": "ML/AI", "proficiency": "Expert", "category": "ml"},
        
        # Data Processing
        {"name": "Data Processing", "parent": "Skills", "proficiency": "", "category": "data"},
        {"name": "Python", "parent": "Data Processing", "proficiency": "Expert", "category": "data"},
        {"name": "R", "parent": "Data Processing", "proficiency": "Advanced", "category": "data"},
        {"name": "SQL", "parent": "Data Processing", "proficiency": "Expert", "category": "data"},
        {"name": "PySpark", "parent": "Data Processing", "proficiency": "Expert", "category": "data"},
        
        # Visualization
        {"name": "Visualization", "parent": "Skills", "proficiency": "", "category": "viz"},
        {"name": "Power BI", "parent": "Visualization", "proficiency": "Expert", "category": "viz"},
        {"name": "Superset", "parent": "Visualization", "proficiency": "Expert", "category": "viz"},
        {"name": "Tableau", "parent": "Visualization", "proficiency": "Advanced", "category": "viz"},
        
        # Cloud/Infrastructure
        {"name": "Cloud/Infrastructure", "parent": "Skills", "proficiency": "", "category": "cloud"},
        {"name": "Airflow", "parent": "Cloud/Infrastructure", "proficiency": "Expert", "category": "cloud"},
        {"name": "Azure", "parent": "Cloud/Infrastructure", "proficiency": "Advanced", "category": "cloud"},
        
        # Academic Knowledge
        {"name": "Academic Knowledge", "parent": "Skills", "proficiency": "", "category": "academic"},
        {"name": "Correspondence Analyses", "parent": "Academic Knowledge", "proficiency": "Advanced", "category": "academic"},
        {"name": "Fractal Market Theory", "parent": "Academic Knowledge", "proficiency": "Advanced", "category": "academic"},
        {"name": "Advanced Econometrics", "parent": "Academic Knowledge", "proficiency": "Expert", "category": "academic"},
        
        # Other
        {"name": "Other", "parent": "Skills", "proficiency": "", "category": "other"},
        {"name": "Wordpress", "parent": "Other", "proficiency": "Intermediate", "category": "other"},
        {"name": "Wix", "parent": "Other", "proficiency": "Intermediate", "category": "other"},
        {"name": "Figma", "parent": "Other", "proficiency": "Intermediate", "category": "other"},
        {"name": "Canva", "parent": "Other", "proficiency": "Advanced", "category": "other"},
        {"name": "Photoshop", "parent": "Other", "proficiency": "Intermediate", "category": "other"},
    ])
    
    unique_categories = sorted(list(set(skills_data['category'].values) - {'root'}))
    
    st.sidebar.header("Filter Skills")
    selected_categories = st.sidebar.multiselect(
        "Select Skill Categories",
        options=unique_categories,
        default=unique_categories
    )
    
    if selected_categories:
        filtered_data = skills_data[
            (skills_data['category'].isin(selected_categories)) | 
            (skills_data['category'] == 'root') |
            (skills_data['name'] == 'Skills')
        ]
    else:
        filtered_data = skills_data
    
    filtered_data['hover_text'] = filtered_data.apply(
        lambda x: f"Skill: {x['name']}<br>Proficiency: {x['proficiency']}" if x['proficiency'] else x['name'],
        axis=1
    )
    
    color_map = {
        'ml': '#FF6B6B',        # Red shade
        'data': '#4ECDC4',      # Teal shade
        'viz': '#45B7D1',       # Blue shade
        'cloud': '#96CEB4',     # Green shade
        'academic': '#FFEEAD',  # Yellow shade
        'other': '#D4A5A5',     # Pink shade
        'root': '#FFFFFF'       # White for root
    }
    
    filtered_data['colors'] = filtered_data['category'].map(color_map)
    
    fig = px.treemap(
        filtered_data,
        names='name',
        parents='parent',
        custom_data=['proficiency'],
        color='category',
        color_discrete_map=color_map,
        hover_data=['hover_text']
    )
    
    fig.update_traces(
        hovertemplate="<b>%{label}</b><br>%{customdata[0]}<extra></extra>",
        textfont=dict(size=16)
    )
    
    fig.update_layout(
        margin=dict(t=0, l=0, r=0, b=0),
        font=dict(
            family="monospace",
            size=16,
            color="#FFFFFF"
        ),
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("### Skill Categories")
    cols = st.columns(3)
    for i, (category, color) in enumerate(color_map.items()):
        if category != 'root':
            cols[i % 3].markdown(
                f'<div style="background-color: {color}; padding: 10px; border-radius: 5px; margin: 5px; color: black;">'
                f'{category.upper()}</div>',
                unsafe_allow_html=True
            )
    
    st.markdown("### Proficiency Levels")
    st.markdown("""
    - **Expert**: Deep knowledge and extensive practical experience
    - **Advanced**: Strong understanding with practical implementation experience
    - **Intermediate**: Working knowledge with some practical experience
    """)
    
    st.caption("💡 Tip: The treemap is interactive! Click to zoom in, click the center to zoom out, and hover for details.")
    st.caption("🔍 Use the sidebar to filter specific skill categories.")

def projects():
    col1, col2 = st.columns(2)

    with col1:
        whatsapp = Image.open("img/Whatsapp.png")
        st.image(whatsapp, width=550)

    with col2:
        st.markdown("""<h2> <a href="https://dogudogru-whatsapp-analyzer-streamlit-app-55duh2.streamlitapp.com/">Whatsapp Analyzer </a></h2>""", unsafe_allow_html=True)
        st.markdown("""
    - The aim of the project is to examine the underlying data of Whatsapp conversations in detail and present them to the user in a fun way
    - The target audience of the application we created is anyone who uses the messaging application Whatsapp and wants to examine their chat data
    - The project is planned to include sentiment analysis using machine learning models in the following stages
        """)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""<h2> <a href="https://dogudogru-tr-weighting-streamlit-app-o9sgc3.streamlitapp.com//">Turkey Report </a></h2>""", unsafe_allow_html=True)
        st.markdown("""
    - Weighting tool designed for the needs of Istanbul Economics Research (a consulting agency based in Istanbul) in pure Python
    - Before performing monthly survey data analysis, weighting is necessary to ensure that the sample distribution is similar to the population distribution and that the survey data becomes more meaningful.
    - This app assigns a weight to each person using gender, age group, education and political party preferences of participants in 2018
    - Tables and charts are prepared with the weights obtained. 
        """)        

    with col2:
        turkeyreport = Image.open("img/TurkeyReport.png")
        st.image(turkeyreport, width=550)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        zelzele = Image.open("img/Zelzele.png")
        st.image(zelzele, width=550)

    with col2:
        st.markdown("""<h2> <a href="https://dogudogru-zelzele-streamlit-app-wdr2va.streamlitapp.com/">Zelzele </a></h2>""", unsafe_allow_html=True)
        st.markdown("""
    - This app scrapes the last 500 recorded earthquake information from <a href="http://www.koeri.boun.edu.tr/scripts/lst2.asp">KOERI's website</a>, 
    - Converts text data into dataframe using Pandas dataframe manipulation techniques and uses st.cache function
    - The project is planned to include sentiment analysis using machine learning models in the following stages
    - Prepares map functions via Plotly Express
        """, unsafe_allow_html=True)        

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""<h2> <a href="https://github.com/dogudogru/Customer-Recomendation-Project">Customer Recommendation </a></h2>""", unsafe_allow_html=True)
        st.markdown("""
    - The aim of this project is to create a recommendation system with simple questions for customers who want to buy washing machines and dishwashers
    - Target audience is the customers who know the product they want to buy but do not have a grasp of the details about the product
    - For this reason, it is ensured that filtering and product recommendations can be made with simple questions, not boring with technical details
        """)        

    with col2:
        recommendation = Image.open("img/customer.png")
        st.image(recommendation, width=550)

def navigation():
    option = st.sidebar.selectbox('Navigation', ['Experience', 'Skills', 'Projects'])
    if option == 'Experience':
        professional_experience()
    elif option == 'Skills':
        skills()
    elif option == 'Projects':
        projects()
    


def main():

    st.sidebar.title('Dogukan Dogru \n Bogazici University \'20  \n B.A. Economics')
    navigation()

    social()


if __name__ == '__main__':
    main()
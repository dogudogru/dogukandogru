import streamlit as st
import plotly.express as px
from PIL import Image
from utils.utils import social
st.set_page_config(layout="wide",page_title='Dogukan Dogru', page_icon=':green_book')


def professional_experience():
    
    #Allianz Turkey

    st.title("Data Analyst")
    st.header("Allianz, Istanbul")
    st.subheader("June 2021 - Current")

    st.markdown("""
    - Developing and working on the integration of end-to-end software prototypes, including data engineering, machine learning and artificial intelligence algorithms, or custom algorithm development
    - Measuring and tracking impact of the developed solutions through business KPIs. Presenting result of analyses to business owners and share knowledge with team members
    - Investigate new data technologies and contribute to the continual development of the Big Data architecture
    """)

    st.markdown("---")

    #Istanbul Economics Research and Consultancy    
    st.title("Business Analyst")
    st.header("Istanbul Economics Research, Istanbul")
    st.subheader("June 2020 - June 2021")

    st.markdown("""
    - Devising and evaluating methods for collecting data and statistical analysis of the collected data
    - Organizing this information into statistical tables and reports
    - Conducting and tracking Facebook, LinkedIn, Twitter, Google Ads campaigns
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

    st.title('Skills')
    fig = px.treemap(
    names = ["Skills", 
            "LANGUAGES","Python", "R", "SQL", 
            "TOOLS", "Streamlit", "Airflow", "Superset", "Tableau", "SAS", "IBM SPSS",
            "ACADEMIC KNOWLEDGE", "Correspondence Analyses", "Fractal Market Theory", "Advanced Econometrics",
            "OTHER", "Wordpress", "Wix", "Figma", "Canva", "Photoshop"],

    parents = ["", 
            "Skills", "LANGUAGES", "LANGUAGES", "LANGUAGES", 
            "Skills", "TOOLS", "TOOLS", "TOOLS", "TOOLS", "TOOLS", "TOOLS",
            "Skills", "ACADEMIC KNOWLEDGE", "ACADEMIC KNOWLEDGE", "ACADEMIC KNOWLEDGE",
            "Skills", "OTHER", "OTHER", "OTHER", "OTHER", "OTHER"],
    
    
    )
    
    fig.update_layout(treemapcolorway= ["#7D7C99","#FFFFFF"],
                    margin = dict(t=0, l=0, r=0, b=0),
                    font=dict(
                    family="monospace",
                    size=20,
                    color="#FFFFFF"
    )
)
    st.plotly_chart(fig, use_container_width=True)
 
    st.caption("Did you know that the chart above is interactive?")    

def projects():
    col1, col2 = st.columns(2)

    with col1:
        whatsapp = Image.open('img\Whatsapp.png')
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
        turkeyreport = Image.open('img\TurkeyReport.png')
        st.image(turkeyreport, width=550)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        zelzele = Image.open('img\Zelzele.png')
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
        recommendation = Image.open('img\customer.png')
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
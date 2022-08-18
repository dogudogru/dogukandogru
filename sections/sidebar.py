import streamlit as st

class SideBar:

    def __init__(self, title, header, subheader) -> None:
        self.title = title
        self.header = header
        self.subheader = subheader
        self.interaction = False

        with st.sidebar:
            logo = Image.open("icons/dreamgames_logo.png")
            st.image(logo)
            st.title(self.title)
            st.header(self.header)
            st.subheader(self.subheader)

            st.write("---")

    def navigation():
        option = st.sidebar.selectbox('Navigation', ['Experience', 'Skills', 'Projects'])
        if option == 'Experience':
            professional_experience()
        elif option == 'Skills':
            skills()
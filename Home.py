import streamlit as st
st.set_page_config(layout="wide")
st.markdown("""

<style>
    @import url('https://fonts.googleapis.com/css?family=Comfortaa:wght@100&display=swap'); 

    html, body, h1,h2,h3,p{
        font-family: 'Comfortaa', sans-serif; 
        
    }
    div[data-baseweb="select"] > div {
    background-color: #62cbec;
            color:white;
            font-family: 'Comfortaa', sans-serif;
    }

    body{
        font-size: 18px;
    }

    [role=radiogroup]{
        gap: 1rem;
    }
    h1 {
        text-align: center
    }
    h2 {
        text-align: center
    }
    h3 {
        text-align: center
    }
    
    div[data-testid='stAppViewBlockContainer']{
        background-color: #62cbec10;
    }
            .center {
    display: block;
    margin-left: auto;
    margin-right: auto;
        width:200px;
}
</style>
""", unsafe_allow_html=True)
st.html("<img src='https://raw.githubusercontent.com/kaheetonaa/streamlit_quizz_template_euth/refs/heads/main/asset/logo.png' class='center'/>")
st.title('Welcome to euthmapper report')


import streamlit as st
import qrcode
import io
from PIL import Image

#st.set_page_config(layout="wide")
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
        font-size: 24px;
    }

    [role=radiogroup]{
        gap: 1rem;
    }
    h1 {
        text-align: center;
        color:#62cbec;
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


st.title('📋EUthMappers Humanitarian report and workshop cheatsheet')


def generate_qr_code(url, fill_color, bg_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=8,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=bg_color)
    img_buffer = io.BytesIO()
    img.save(img_buffer, format="PNG")
    img_bytes = img_buffer.getvalue()
    return st.image(img_bytes)
st.header('📉 The result of the workshop on 03/10/2024')
qr_img = generate_qr_code('google.com', '#62cbec', '#FFFFFF00')

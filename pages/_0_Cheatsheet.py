import streamlit as st
from PIL import Image
import qrcode
from datetime import datetime
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask
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


st.title('📋EUthMappers Humanitarian report and workshop cheatsheet')



def generate_qrcode(url):
    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=2
                        )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(image_factory=StyledPilImage, color_mask=HorizontalGradiantColorMask())

    current_ts = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    qrcode_path = generated_qrcodes_path + "qrcode_" + str(current_ts) + ".png"
    img.save(qrcode_path)
    return qrcode_path

qrcode_path = generate_qrcode('hello')
image = Image.open(qrcode_path)

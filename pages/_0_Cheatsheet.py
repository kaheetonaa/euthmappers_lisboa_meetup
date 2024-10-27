import streamlit as st
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask

st.title('📋EUthMappers Humanitarian report and workshop cheatsheet')

st.set_page_config(
    page_title="Cheatsheet",
    page_icon="📋",
    layout="centered",
    initial_sidebar_state="auto",
)

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

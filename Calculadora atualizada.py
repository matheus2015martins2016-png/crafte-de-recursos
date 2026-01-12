import streamlit as st
import streamlit as st
import streamlit as st
from PIL import Image

# Configurar o layout da página para largura total, se desejar
st.set_page_config(layout="centered")


# Carregar a imagem (substitua pelo caminho da sua imagem)
# Exemplo: imagem local
# image = Image.open('sua_imagem.png') 

# Exemplo: usando uma URL de imagem para fácil teste
image_url = 'https://framerusercontent.com/images/XnMIn7jevSfpw48QwPWnhNYqic.png' 

# Define as colunas: uma coluna vazia à esquerda, uma para a imagem (central), e uma vazia à direita.
# Os valores (1, 3, 1) determinam a proporção da largura. Ajuste conforme necessário.
col1, col2,col3 = st.columns([1, 3, 1])

with col2:
    # Use st.image dentro da coluna do meio
    st.image(image_url, width=800)

# Adicione mais conteúdo abaixo se necessário


st.title(  "Craft de Recursos – Legend of Ymir")

st.set_page_config(
    page_title="Craft de Recursos - Legend of Ymir",
    page_icon="logo.png",
    layout="centered"  # ou "wide"
)


col1, col2 = st.columns(2)

with col1:
    st.subheader("🔵 Recursos Raros")
    Raros_necessarios = st.number_input(
        "Recursos Raros necessários",
        min_value=0,
        step=1
    )

    Raros_atuais = st.number_input(
        "Recursos Raros que você tem",
        min_value=0,
        step=1
    )

with col2:
    st.subheader("📊 Resultado")

    if st.button("Calcular"):
        if Raros_atuais >= Raros_necessarios:
            st.success("Você já tem Recursos Azuis suficientes.")
        else:
            faltam = Raros_necessarios - Raros_atuais
            comuns = faltam * 100

            st.error(f"Recursos raros faltando: {faltam}")
            st.info(f"Recursos comuns necessários: {comuns}")


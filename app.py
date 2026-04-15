import streamlit as st
import pandas as pd
import re

def clean_data(df):
    # Lógica de limpieza: Eliminación de duplicados y filas vacías
    df = df.drop_duplicates().dropna(how='all')
    return df

st.set_page_config(page_title="DataCleaner Pro - Herramienta Gratuita", layout="centered")

st.title("Clean & Format Your Data 🛠️")
st.write("Sube tu archivo CSV o Excel y yo lo limpio por ti en segundos.")

uploaded_file = st.file_uploader("Elige un archivo", type=['csv', 'xlsx'])

if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    st.write("### Vista previa de tus datos originales:")
    st.dataframe(df.head())

    if st.button("Limpiar Datos Ahora"):
        cleaned_df = clean_data(df)
        st.success("¡Datos limpiados con éxito!")
        
        # Conversión para descarga
        csv = cleaned_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Descargar CSV Limpio",
            data=csv,
            file_name="data_limpia.csv",
            mime="text/csv",
        )

st.sidebar.info("Esta herramienta es gratuita. Considera apoyarnos viendo un anuncio o compartiéndola.")

st.sidebar.markdown('---')
st.sidebar.write("¿Te ahorré tiempo?")
st.sidebar.markdown("[☕ Invítame a un café](TU_LINK_AQUI)")

import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="DataCleaner Pro | Instant CSV & Excel Formatter",
    page_icon="🛠️",
    layout="centered"
)

# 2. Sidebar - Monetization & Info
st.sidebar.image("https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-1.svg", width=150)
st.sidebar.header("Support the Project")
st.sidebar.write("This tool is free and does not store your data. If it saved you time, consider supporting its maintenance:")

# BOTÓN DE DONACIÓN REAL
st.sidebar.markdown(
    f"""
    <a href="https://buymeacoffee.com/yojimbomrp" target="_blank">
        <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" 
        alt="Buy Me A Coffee" style="height: 50px !important;width: 180px !important;" >
    </a>
    """,
    unsafe_allow_html=True
)

st.sidebar.divider()
st.sidebar.info("🔒 **Privacy Note:** Your files are processed locally in memory and are never saved on our servers.")

# 3. Main Interface
st.title("DataCleaner Pro 🛠️")
st.subheader("Transform raw chaos into structured value")
st.write("Clean your datasets in seconds. Remove duplicates, drop empty rows, and format your files for Shopify, Amazon, or CRM usage.")

# 4. File Upload Logic
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=['csv', 'xlsx'])

if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.write("### 📄 Preview of Original Data:")
        st.dataframe(df.head(10))

        if st.button("🚀 Clean & Optimize Data"):
            # Cleaning logic
            initial_count = len(df)
            # Remove full empty rows and exact duplicates
            df_cleaned = df.drop_duplicates().dropna(how='all')
            final_count = len(df_cleaned)
            
            # --- NUEVA LÓGICA DE VALOR AÑADIDA ---
            rows_removed = initial_count - final_count
            # Estimamos que limpiar cada fila manual toma unos 2 segundos
            time_saved_seconds = rows_removed * 2 
            
            if rows_removed > 0:
                st.success(f"Done! We found and removed {rows_removed} redundant rows.")
                if time_saved_seconds > 60:
                    st.info(f"💡 You just saved approximately {time_saved_seconds // 60} minutes of boring manual work!")
                else:
                    st.info(f"💡 You just saved about {time_saved_seconds} seconds. Speed is power!")
            else:
                st.success("Your data is already clean! No duplicates found.")
                st.info("💡 Your dataset is in perfect shape for production.")
            # ---------------------------------------
            
            # Download button
            csv = df_cleaned.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Cleaned File",
                data=csv,
                file_name="cleaned_data_pro.csv",
                mime="text/csv",
            )
            
            st.balloons() # Pequeño efecto visual para mejorar la experiencia de usuario
            
    except Exception as e:
        st.error(f"Error: {e}. Please ensure the file is not corrupted and has a valid format.")

# 5. Footer / SEO Keywords
st.divider()
st.caption("Free Online CSV Cleaner | Excel Duplicate Remover | Data Formatting Tool")

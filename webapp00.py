import streamlit as st
import pandas as pd  # Certifique-se de importar pandas
from ACTlib01 import *

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQFwxxM13bxUC0dpyd0w0PxfZIrJ-hp4Px-R6rsTiG3c3n-89JApzA0jYJpU9vNfxeNCvtJ0Cg35KtO/pub?gid=556192647&single=true&output=csv"
db = Ler_GooglePlanilha(url)
db.fillna('', inplace=True)
Escrever(db)

# Adicionando título e cabeçalhos
st.title("MEU 1º WEB APP STREAMLIT")
st.header("Testando funcionalidades no Streamlit")
st.subheader("Sub Cabeçalho")
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

# Adicionando um slider
values = st.slider("Select a range of values", 0.0, 100.0, (5.0, 15.0))
st.write("Values:", values)

# Configurando a URL e a coluna de data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Carregando os dados
data_load_state = st.text('Carregando dados...')
data = load_data(1000)  # Carregando as primeiras 1000 linhas
data_load_state.text('Dados carregados!')

# Exibindo os dados
st.subheader('Dados carregados')
st.write(data)

# Opcional: você pode adicionar gráficos ou análises adicionais com os dados carregados

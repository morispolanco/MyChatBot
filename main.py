import streamlit as st
from googlesearch import search

def obtener_precio_mas_bajo(query, ubicacion="Guatemala"):
    precios = []

    # Realizar una búsqueda en Google con la consulta específica
    for j in search(query, num=5, stop=5, pause=2, tld="com", lang="en", country="GT"):
        precios.append(j)

    return precios

# Configuración de la página de Streamlit
st.title("Consulta de Precio Más Bajo en Guatemala")

# Obtener la consulta del usuario
query = st.text_input("Ingrese el nombre del producto:")

if query:
    # Obtener precios de Google
    precios = obtener_precio_mas_bajo(query)

    # Mostrar resultados
    st.subheader("Resultados de la búsqueda:")
    for precio in precios:
        st.write(precio)
else:
    st.warning("Ingrese el nombre del producto para realizar la búsqueda.")

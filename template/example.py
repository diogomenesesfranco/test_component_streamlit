import streamlit as st
from test_component import test_component

st.subheader("Componente com argumentos constantes")

# Crie uma instância do nosso componente com um argumento `name` constante e
# imprime seu valor de saída.
num_clicks = test_component("Usuário")
st.markdown("Você clicou %s vezes!" % int(num_clicks))

st.markdown("---")
st.subheader("Componente com argumentos variáveis")

# Crie uma segunda instância do nosso componente cujo argumento `name` irá variar
# baseado em um widget text_input.
#
# Usamos o argumento especial "key" para atribuir uma identidade fixa a esta
# instância do componente. Por padrão, quando os argumentos de um componente mudam,
# é considerada uma nova instância e será remontada no frontend
# e perderá seu estado atual. Neste caso, queremos variar o valor do componente
# argumento "nome" sem que ele seja recriado.
name_input = st.text_input("Digite seu nome", value="Usuário")
num_clicks = test_component(name_input, key="foo")
st.markdown("Você clicou %s vezes!" % int(num_clicks))

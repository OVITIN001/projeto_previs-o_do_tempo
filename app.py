import streamlit as st
from dados_api import previsao_temperatura

#cidades
Cidades = {
    "Xique-Xique" : [-10.824146291915795, -42.72700667066001],
    "Santos" : [-23.96202140298297, -46.32875160073251],
    "Coronel Fabriciano" : [-19.520287715130085, -42.62872359285969],
    "Joanésia" : [-19.175406224473747, -42.681088404458045],
    "Copacabana" : [-22.969718755119736, -43.187087212896905],
    "Cabo Frio" : [-22.88776083668657, -42.02570442607085],
    "Osaka" : [34.68742014251089, 135.52891732403603],
    "Paraisópolis" : [-23.61631084307922, -46.726910849043236]
}

#-------------------------------sidebar
st.sidebar.title("VT previsões")
st.sidebar.image("logo.png")

cidade = st.sidebar.selectbox("Escolha a cidade:", Cidades.keys())
latitude, longitude = Cidades[cidade]

#-----------------------------------BODY
st.title(f'Previsão do tempo em {cidade} para os próximos 7 dias')

st.markdown("----")

# Previsão de temperatura
dados, temperatura_media = previsao_temperatura(latitude, longitude)

for i, d in temperatura_media.iterrows():

    with st.container(border=True):
        st.subheader(d['dia_semana'])

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Data", f'{int(d['dia'])}/{int(d['mes'])}')

        with col2:
            st.metric("Temperatura média", f"{d['temperatura_media']:.2f}°")

        with col3:
            if d['temperatura_media'] < 10:
                temp = "cold.png"

            elif d['temperatura_media'] < 18:
                temp = "cool.png"

            elif d['temperatura_media'] < 25:
                temp = "comfort.png"

            else:
                temp = "warm.png"

            st.image(temp, width=40)

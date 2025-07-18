import streamlit as st
from paginas.auth_adm import auth_admin
from paginas.dashboard_principal import mostrar_relatorio_semanal
from paginas.sugestao_melhoria import sug_melhoria2


def main():
    st.set_page_config(
    page_title="Pagina de Login",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
    )

    pg_inicial = st.Page("paginas/dashboard_principal.py", title= "Pagina Inicial")
    sug_mlhr = st.Page("paginas/sugestao_melhoria.py", title= "Sugestão de Melhoria")

    authenticator =  auth_admin()
    authenticator.login()

    if st.session_state["authentication_status"] is False:
        st.error("Usuario/Senha invalido")

    elif st.session_state["authentication_status"] is None:
        st.warning("Por favor, Utilize se usuario e senha")

    elif st.session_state["authentication_status"] is True:
        logo = st.logo("Logo_Techstrat.png", size="large")
        pg = st.navigation(
        {
            "Visualizar": [pg_inicial, sug_mlhr],
            
        }
        )
        pg.run()


if __name__ == "__main__":
    main()

    




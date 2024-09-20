import streamlit as st

# darei o nome da mudança d estado de "navegacao"
if 'navegacao' not in st.session_state:
    st.session_state.navegacao = None
    
NAVEGACAO = [
    None,
    'Home',
    'Notificacoes',
    'Agendamentos',
    'Reservas',
    'Moradores',
    'Boletos',
    'Financeiro',
    'Malotes',
    'Prestadores',
    'Documentacao',
    'Seguro',
]

# funcao base para contruir a lógica do login
def login():
    st.header("Página de Login")
    navegacao = st.selectbox("Escolha a Página",NAVEGACAO)
    if st.button("Logar"):
        st.session_state.navegacao = navegacao
        st.rerun()

# Função Base para Construir a lógica do logout
def logout():
    st.session_state.navegacao = None
    st.rerun()

# atualização da navegacao
navegacao = st.session_state.navegacao

# Caso seja necessário insira o settings aqui

# logout
logout_pages = st.Page(logout,title='Sair')

# Seleção das Páginas:
home = st.Page(
    'pages/home.py',
    title='Home',
    default=(navegacao == 'Home')
)
notificacoes = st.Page(
    'pages/notif_mult.py',
    title='Notificações e Multas',
    default=(navegacao =='Notificacoes'),
)
agendamentos = st.Page(
    'pages/agendamentos.py',
    title='Agendamentos de mudança',
    default=(navegacao =='Agendamentos'),
)
reservas = st.Page(
    'pages/reservas.py',
    title='Reservas de Eventos',
    default=(navegacao =='Reservas'),
)
moradores = st.Page(
    'pages/historico_moradores.py',
    title='Histórico Moradores',
    default=(navegacao =='Moradores'),
)
boletos = st.Page(
    'pages/composicao_boletos.py',
    title='Composicao de Boletos',
    default=(navegacao =='Boletos'),
)
financeiro = st.Page(
    'pages/financeiro.py',
    title='Financeiro',
    default=(navegacao =='Financeiro'),
)
malotes = st.Page(
    'pages/malotes.py',
    title='Composição de Malotes',
    default=(navegacao =='Malotes'),
)
prestadores = st.Page(
    'pages/prestadores.py',
    title='Prestadores de Serviço',
    default=(navegacao =='Prestadores'),
)
documentacao = st.Page(
    'pages/documentacao.py',
    title='Documentação',
    default=(navegacao =='Documentacao'),
)
seguro = st.Page(
    'pages/seguro_edificacao.py',
    title='Seguro Edificação',
    default=(navegacao =='Seguro'),
)

# Sidebar
deslogar = [logout_pages]
opcoes = [home,notificacoes,agendamentos,reservas,moradores,boletos,financeiro,malotes,prestadores,documentacao,seguro]

# Titulo em todas as paginas
st.title('Unidade1')
dicionario = {}

# Lógica da Mudança
if st.session_state.navegacao in ['Home']:
    dicionario['Home'] =opcoes
if st.session_state.navegacao in ['Notificacoes']:
    dicionario['Notificacoes'] =opcoes
if st.session_state.navegacao in ['Agendamentos']:
    dicionario['Agendamentos'] =opcoes
if st.session_state.navegacao in ['Reservas']:
    dicionario['Reservas'] =opcoes
if st.session_state.navegacao in ['Moradores']:
    dicionario['Moradores'] =opcoes
if st.session_state.navegacao in ['Boletos']:
    dicionario['Boletos'] =opcoes
if st.session_state.navegacao in ['Financeiro']:
    dicionario['Financeiro'] =opcoes
if st.session_state.navegacao in ['Malotes']:
    dicionario['Malotes'] =opcoes
if st.session_state.navegacao in ['Prestadores']:
    dicionario['Prestadores'] =opcoes
if st.session_state.navegacao in ['Documentacao']:
    dicionario['Documentacao'] =opcoes
if st.session_state.navegacao in ['Seguro']:
    dicionario['Seguro'] =opcoes
if len(dicionario)>0:
    pg = st.navigation(
        {
            "logout":deslogar,
            "Unidade1": opcoes,
        }
    )
else:
    pg = st.navigation([st.Page(login)])

pg.run()
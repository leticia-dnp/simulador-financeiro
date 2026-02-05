import streamlit as st
import requests
import pandas as pd
import plotly.express as px 

st.set_page_config(page_title="Simulador Financeiro", page_icon="💰", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@700&display=swap');

    .stApp {
        background: linear-gradient(to bottom, #000000, #1a0029) !important;
        background-attachment: fixed !important;
    }
    header[data-testid="stHeader"] {
        background-color: rgba(18, 18, 18, 0.95);
    }
    h1, h2, h3 {
        font-family: 'Copperplate', serif !important;
        color: white !important;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.6);
    }
    p, label, .stMarkdown {
        font-family: 'Josefin Sans', sans-serif !important;
        font-weight: 700 !important;
        color: #f0f0f0 !important;
    }
    .stButton > button {
        font-family: 'Josefin Sans', sans-serif !important;
        font-weight: 700 !important;
        color: white !important;
        background: linear-gradient(145deg, #BB86FC, #6B256F) !important;
        border: none !important;
        border-radius: 15px !important;
        box-shadow: 0 5px 0 #1a0916, 0 10px 15px rgba(0,0,0,0.3) !important;
        transition: all 0.1s ease !important;
        transform: translateY(0);
    }
    .stButton > button:hover {
        box-shadow: 0 0 20px rgba(187, 134, 252, 0.4) !important;
        transform: scale(1.02) !important;
    }
    .stButton > button:active {
        transform: translateY(2px) !important;
        box-shadow: 0 2px 0 #1a0916, 0 4px 10px rgba(0,0,0,0.3) !important;
    }
    .metric-card {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        color: white;
        box-shadow: 10px 10px 20px rgba(0,0,0,0.5), -5px -5px 15px rgba(255,255,255,0.05);
        text-align: center;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .metric-value {
        font-size: 28px;
        font-weight: bold;
        margin: 10px 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .metric-label {
        font-size: 16px;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Estilização dos Inputs (Mês, Valor, Taxa, Juros) para igualar ao botão Simular */
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
        background: linear-gradient(#121212, #121212) padding-box, linear-gradient(45deg, #BB86FC, #E0B0FF) border-box !important;
        border: 2px solid transparent !important;
        border-radius: 15px !important;
        color: white !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3) !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }
    div[data-baseweb="select"] > div:hover, div[data-baseweb="input"] > div:hover {
        box-shadow: 0 0 15px rgba(187, 134, 252, 0.6) !important;
        transform: scale(1.02) !important;
    }
    div[data-baseweb="select"] span, div[data-baseweb="input"] input {
        color: white !important;
        font-weight: 700 !important;
        text-align: center !important;
        background-color: transparent !important;
    }
    div[data-baseweb="select"] svg {
        fill: white !important;
    }

    /* Remove os botões +/- dos inputs numéricos */
    [data-testid="stNumberInput"] button {
        display: none !important;
    }

    .title-container {
        position: relative;
        text-align: center;
        overflow: hidden;
        padding: 20px 0;
    }

    .title-container h1 {
        position: relative;
        z-index: 2;
    }

    .cifrao {
        position: fixed;
        bottom: -10vh;
        top: auto;
        color: #BB86FC;
        font-size: 20px;
        opacity: 0;
        animation: float-up 15s infinite linear;
        z-index: 0;
        user-select: none;
        pointer-events: none;
    }

    @keyframes float-up {
        0%   { transform: translateY(0) rotate(0deg); opacity: 0; }
        10%  { opacity: 0.2; }
        90%  { opacity: 0.2; }
        100% { transform: translateY(-120vh) rotate(360deg); opacity: 0; }
    }

    .cifrao:nth-of-type(1) { left: 15%; animation-delay: 0s; animation-duration: 15s; }
    .cifrao:nth-of-type(2) { left: 35%; animation-delay: -5s; animation-duration: 12s; font-size: 24px; }
    .cifrao:nth-of-type(3) { left: 55%; animation-delay: -2s; animation-duration: 18s; }
    .cifrao:nth-of-type(4) { left: 75%; animation-delay: -8s; animation-duration: 10s; font-size: 22px; }
    .cifrao:nth-of-type(5) { left: 90%; animation-delay: -12s; animation-duration: 14s; }
    .cifrao:nth-of-type(6) { left: 5%; animation-delay: -4s; animation-duration: 16s; color: #00E676; }
    .cifrao:nth-of-type(7) { left: 25%; animation-delay: -9s; animation-duration: 13s; color: #FF5252; }
    .cifrao:nth-of-type(8) { left: 45%; animation-delay: -6s; animation-duration: 19s; color: #00E676; }
    .cifrao:nth-of-type(9) { left: 65%; animation-delay: -11s; animation-duration: 11s; color: #FF5252; }
    .cifrao:nth-of-type(10) { left: 10%; animation-delay: -3s; animation-duration: 17s; color: #BB86FC; }
    .cifrao:nth-of-type(11) { left: 30%; animation-delay: -7s; animation-duration: 14s; color: #00E676; }
    .cifrao:nth-of-type(12) { left: 50%; animation-delay: -5s; animation-duration: 16s; color: #FF5252; }
    .cifrao:nth-of-type(13) { left: 70%; animation-delay: -10s; animation-duration: 12s; color: #BB86FC; }
    .cifrao:nth-of-type(14) { left: 85%; animation-delay: -2s; animation-duration: 18s; color: #00E676; }
    .cifrao:nth-of-type(15) { left: 95%; animation-delay: -8s; animation-duration: 15s; color: #FF5252; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-container">
    <h1>Simulador de Investimentos</h1>
    <span class="cifrao">$</span>
    <span class="cifrao">$</span>
    <span class="cifrao">$</span>
    <span class="cifrao">$</span>
    <span class="cifrao">$</span>
    <span class="cifrao">$</span>
    <span class="cifrao">$</span>
    <span class="cifrao">$</span>
    <span class="cifrao">$</span>
    <span class="cifrao">$</span>
    <span class="cifrao">$</span>
    <span class="cifrao">$</span>
    <span class="cifrao">$</span>
    <span class="cifrao">$</span>
    <span class="cifrao">$</span>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

meses_nomes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
               "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

c1, c2, c3, c4 = st.columns(4)
with c1:
    mes_inicio = st.selectbox("Mês de Início", meses_nomes)
with c2:
    valor = st.number_input("Valor Inicial (R$)", min_value=0.0, value=1000.0)
with c3:
    taxa = st.number_input("Taxa de Juros (% ao mês)", min_value=0.0, value=1.0)
with c4:
    meses = st.number_input("Prazo (meses)", min_value=1, value=12, step=1)

if st.button("Simular", type="primary", use_container_width=True):
    with st.spinner("Processando simulação..."):
        payload = {"valor": valor, "taxa": taxa, "meses": meses}
        try:
            response = requests.post("http://127.0.0.1:8000/simular", json=payload, timeout=10)
            if response.status_code == 200:
                data = response.json()
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                col_a, col_b, col_c = st.columns(3)
                metrics = [
                    ("Valor Inicial", f"R$ {data['valor_inicial']:,.2f}"),
                    ("Montante Final", f"R$ {data['montante_final']:,.2f}"),
                    ("Juros Totais", f"R$ {data['juros_totais']:,.2f}")
                ]
                
                for col, (label, value) in zip([col_a, col_b, col_c], metrics):
                    custom_style = ""
                    if label == "Valor Inicial":
                        custom_style = 'style="background: linear-gradient(145deg, #001F3F, #003366);"'
                    elif label == "Montante Final":
                        custom_style = 'style="background: linear-gradient(145deg, #003300, #004d00);"'
                    elif label == "Juros Totais":
                        custom_style = 'style="background: linear-gradient(145deg, #330000, #550000);"'

                    col.markdown(f"""
                        <div class="metric-card" {custom_style}>
                            <div class="metric-label">{label}</div>
                            <div class="metric-value">{value}</div>
                        </div>
                    """, unsafe_allow_html=True)

                start_index = meses_nomes.index(mes_inicio)
                valores_com_inicial = [data['valor_inicial']] + data['evolucao_mensal']
                indices = list(range(len(valores_com_inicial)))
                labels_meses = [meses_nomes[(start_index + i) % 12] for i in indices]
                
                principal_series = [data['valor_inicial']] * len(indices)
                juros_series = [data['valor_inicial'] * (1 + (data['taxa']/100) * i) for i in indices]

                df_chart = pd.DataFrame({
                    "Mês": indices,
                    "Nome do Mês": labels_meses,
                    "Montante": valores_com_inicial,
                    "Principal": principal_series,
                    "Juros": juros_series
                })
                
                col_graf1, col_graf2 = st.columns(2)

                with col_graf1:
                    y_cols = ["Montante", "Principal", "Juros"]
                    colors = ["#BB86FC", "#03DAC6", "#CF6679"]

                    fig = px.line(
                        df_chart, x="Mês", y=y_cols, 
                        title="Análise de Evolução",
                        labels={"value": "Valor", "Mês": "Mês", "variable": "Série"},
                        color_discrete_sequence=colors
                    )
                    
                    fig.update_traces(
                        line_shape='spline',
                        mode='lines+markers'
                    )
                    
                    fig.update_layout(
                        plot_bgcolor="rgba(0,0,0,0)",
                        paper_bgcolor="rgba(0,0,0,0)",
                        font=dict(color="white", family="Josefin Sans"),
                        hovermode="x unified"
                    )
                    fig.update_xaxes(tickmode='array', tickvals=indices, ticktext=labels_meses, showgrid=True, gridcolor='rgba(255,255,255,0.1)')
                    fig.update_yaxes(showticklabels=True, range=[data['valor_inicial'], None])
                    st.plotly_chart(fig, use_container_width=True)
                
                with col_graf2:
                    fig_pie = px.pie(
                        df_chart, values='Montante', names='Nome do Mês',
                        title='Distribuição Mensal',
                        hole=0.4,
                        color_discrete_sequence=px.colors.sequential.Turbo
                    )
                    fig_pie.update_traces(
                        textposition='inside', 
                        texttemplate='R$ %{value:,.0f}', 
                        hoverinfo='skip',
                        hovertemplate=None,
                        marker=dict(line=dict(color='#121212', width=2))
                    )
                    fig_pie.update_layout(
                        plot_bgcolor="rgba(0,0,0,0)",
                        paper_bgcolor="rgba(0,0,0,0)",
                        font=dict(color="white", family="Josefin Sans"),
                        separators=",."
                    )
                    st.plotly_chart(fig_pie, use_container_width=True)
                
            else:
                st.error("Erro ao conectar com a API.")
        except requests.exceptions.ConnectionError:
            st.error("⚠️ Erro de Conexão: O servidor backend não está rodando. Certifique-se de executar o arquivo 'backend.py' em um terminal separado.")
        except Exception as e:
            st.error(f"Erro: {e}")
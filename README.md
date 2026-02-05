# 💰 Simulador Financeiro – Juros Compostos com FastAPI & Streamlit

Projeto 2/2 – Bootcamp DIO + Bradesco: GenAI & Dados.

---

## Descrição Geral
Este projeto foi desenvolvido com o objetivo de aplicar conceitos de **engenharia de software**, **desenvolvimento web** e **visualização de dados** em um simulador interativo de investimentos.  
A aplicação combina **FastAPI** (backend) e **Streamlit** (frontend) para permitir que o usuário insira parâmetros financeiros e visualize a evolução de seus investimentos ao longo do tempo, com cálculos baseados em **juros compostos**.

---

## Estrutura do Projeto
- **Backend (FastAPI)**  
  - Arquivo principal: `backend.py`  
  - Endpoint: `POST /simular`  
  - Responsável por processar os cálculos financeiros e retornar os resultados.

- **Frontend (Streamlit)**  
  - Arquivo principal: `frontend/app.py`  
  - Interface gráfica moderna e responsiva para interação com o usuário.  
  - Inputs: Mês de Início, Valor Inicial, Taxa de Juros (% ao mês), Prazo (meses).  
  - Outputs: Cards estilizados com métricas e gráficos interativos (linha e pizza).  

- **Ambiente Virtual (venv)**  
  - Gerenciamento de dependências e bibliotecas necessárias (`fastapi`, `uvicorn`, `streamlit`, `pandas`, `plotly`).  

---

## Funcionalidades Principais
- Inserção de parâmetros financeiros via interface gráfica.  
- Cálculo automático de montante final, juros totais e evolução mensal.  
- Exibição de métricas em **cards estilizados**.  
- Visualização interativa com **gráficos Plotly** (linha e pizza).  
- Backend e frontend integrados via API REST.  

---

## ⚙️ Instalação e Execução

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/simulador-financeiro.git
cd simulador-financeiro
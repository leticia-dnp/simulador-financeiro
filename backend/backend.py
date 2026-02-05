from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Simulacao(BaseModel):
    valor: float
    taxa: float
    meses: int

@app.post("/simular")
def simular(simulacao: Simulacao):
    montante = simulacao.valor * ((1 + simulacao.taxa/100) ** simulacao.meses)
    juros = montante - simulacao.valor

    evolucao = []
    for m in range(1, simulacao.meses + 1):
        valor_mes = simulacao.valor * ((1 + simulacao.taxa/100) ** m)
        evolucao.append(valor_mes)

    return {
        "valor_inicial": simulacao.valor,
        "taxa": simulacao.taxa,
        "meses": simulacao.meses,
        "montante_final": round(montante, 2),
        "juros_totais": round(juros, 2),
        "evolucao_mensal": evolucao
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
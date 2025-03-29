from fastapi import APIRouter, HTTPException
import pandas as pd

router = APIRouter()

@router.get("/buscar-registros")
def getRegistros(buscaTextual: str = None):
    if not buscaTextual:
        raise HTTPException(status_code=400, detail="A palavra-chave é obrigatória para a busca.")

    registros = pd.read_csv("../../Teste 3/Relatorio_cadop.csv", sep=";", encoding="UTF-8")

    registros = registros.dropna()
    
    registrosEncontrados = registros[registros.apply(lambda row: row.astype(str).str.contains(buscaTextual, case=False).any(), axis=1)]
    
    if registrosEncontrados.empty:
        raise HTTPException(status_code=404, detail="Nenhum registro encontrado para a palavra-chave fornecida.")
    
    return registrosEncontrados.to_dict(orient="records")

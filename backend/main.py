"""
main.py — Servidor FastAPI para a Plataforma de Agentes Pedagógicos Inteligentes.

Rotas:
  GET  /api/health     — Health check
  GET  /api/practices  — Lista práticas pedagógicas
  POST /api/generate   — Gera sequência didática

Execute com: uvicorn main:app --reload --port 8000
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional

from agents import AGENTS
from services.ai_service import generate_with_ai
from services.template_service import generate_from_template

# ─── FastAPI App ──────────────────────────────────────────────
app = FastAPI(
    title="Agentes Pedagógicos Inteligentes",
    description="API para geração de sequências didáticas com IA",
    version="1.0.0",
)

# ─── CORS (permite frontend acessar) ─────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─── Modelos Pydantic ────────────────────────────────────────
class GenerateRequest(BaseModel):
    practice: str = Field(..., description="Chave da prática pedagógica (ex: 'abp', 'pbl')")
    tema: str = Field(..., description="Tema da aula")
    faixa_etaria: str = Field(..., description="Faixa etária dos alunos")
    tempo: str = Field(..., description="Tempo disponível para a aula")
    objetivos: Optional[str] = Field("", description="Objetivos específicos (opcional)")
    modelo: Optional[str] = Field("auto", description="Modelo de IA a usar: 'auto', 'gemini', 'groq', 'huggingface'")


class PracticeInfo(BaseModel):
    key: str
    name: str
    description: str


# ─── Rotas ───────────────────────────────────────────────────
@app.get("/api/health")
async def health_check():
    """Verifica se o servidor está funcionando."""
    return {"status": "ok", "message": "Servidor funcionando!"}


@app.get("/api/practices", response_model=list[PracticeInfo])
async def list_practices():
    """Lista todas as práticas pedagógicas disponíveis."""
    practices = []
    for key, agent_class in AGENTS.items():
        agent = agent_class()
        practices.append(PracticeInfo(
            key=key,
            name=agent.name,
            description=agent.description,
        ))
    return practices


@app.post("/api/generate")
async def generate_sequence(request: GenerateRequest):
    """
    Gera uma sequência didática baseada na prática pedagógica escolhida.
    Tenta usar IA primeiro, faz fallback para templates se necessário.
    """
    if request.practice not in AGENTS:
        raise HTTPException(
            status_code=400,
            detail=f"Prática '{request.practice}' não encontrada. "
                   f"Opções: {list(AGENTS.keys())}",
        )

    agent_class = AGENTS[request.practice]
    agent = agent_class()

    # Tenta gerar com IA usando o modelo selecionado
    prompt = agent.build_prompt(
        tema=request.tema,
        faixa_etaria=request.faixa_etaria,
        tempo=request.tempo,
        objetivos=request.objetivos or "",
    )

    modelo = request.modelo or "auto"
    result, provider_used = await generate_with_ai(prompt, modelo=modelo)

    # Fallback para template se IA falhar
    source = "ai"
    if result is None:
        result = generate_from_template(
            practice=request.practice,
            tema=request.tema,
            faixa_etaria=request.faixa_etaria,
            tempo=request.tempo,
            objetivos=request.objetivos or "",
        )
        source = "template"
        provider_used = "template"

    # Mapa de nomes amigáveis dos provedores
    provider_labels = {
        "gemini": "🤖 Google Gemini Flash",
        "groq": "⚡ Groq / Llama 3",
        "huggingface": "🧠 HuggingFace / Mistral",
        "template": "📋 Template Inteligente",
    }

    return {
        "success": True,
        "source": source,
        "provider": provider_used,
        "provider_label": provider_labels.get(provider_used, provider_used),
        "practice": agent.name,
        "sequence": result,
    }


# ─── Execução direta ────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

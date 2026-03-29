"""
ai_service.py — Roteador Multi-Provider de IA.
Despacha o prompt para o provedor de IA selecionado pelo usuário.
Modo "auto": tenta Gemini → Groq → HuggingFace.
"""
import os
from dotenv import load_dotenv

from .gemini_provider import generate_with_gemini
from .groq_provider import generate_with_groq
from .huggingface_provider import generate_with_huggingface

load_dotenv()

# ─── Mapeamento de provedores ────────────────────────────────
PROVIDERS = {
    "gemini": "Google Gemini Flash",
    "groq": "Groq / Llama 3",
    "huggingface": "HuggingFace / Mistral",
    "auto": "Automático",
}


async def generate_with_ai(prompt: str, modelo: str = "auto") -> tuple[dict | None, str]:
    """
    Roteador principal. Retorna (resultado, provider_usado).
    - Se modelo == "auto": tenta todos os providers em sequência.
    - Se modelo específico: tenta apenas aquele.
    """
    if modelo == "auto":
        return await _auto_generate(prompt)
    elif modelo == "gemini":
        result = await generate_with_gemini(prompt)
        return (result, "gemini") if result else (None, "gemini")
    elif modelo == "groq":
        result = await generate_with_groq(prompt)
        return (result, "groq") if result else (None, "groq")
    elif modelo == "huggingface":
        result = await generate_with_huggingface(prompt)
        return (result, "huggingface") if result else (None, "huggingface")
    else:
        # Modelo desconhecido → modo auto
        return await _auto_generate(prompt)


async def _auto_generate(prompt: str) -> tuple[dict | None, str]:
    """
    Modo automático: tenta os provedores em ordem de prioridade.
    Gemini (mais criativo) → Groq (mais rápido) → HuggingFace (legado).
    """
    # 1. Tentar Gemini
    print("[AI Router] Tentando Gemini...")
    result = await generate_with_gemini(prompt)
    if result:
        print("[AI Router] ✅ Gemini respondeu com sucesso!")
        return (result, "gemini")

    # 2. Tentar Groq
    print("[AI Router] Tentando Groq...")
    result = await generate_with_groq(prompt)
    if result:
        print("[AI Router] ✅ Groq respondeu com sucesso!")
        return (result, "groq")

    # 3. Tentar HuggingFace
    print("[AI Router] Tentando HuggingFace...")
    result = await generate_with_huggingface(prompt)
    if result:
        print("[AI Router] ✅ HuggingFace respondeu com sucesso!")
        return (result, "huggingface")

    # 4. Todos falharam
    print("[AI Router] ❌ Todos os provedores de IA falharam.")
    return (None, "none")

"""
ai_service.py — Roteador Multi-Provider de IA.
Despacha o prompt para o provedor de IA selecionado pelo usuário.
Modo "auto": tenta Gemini → Groq → HuggingFace → Template (fallback).
"""
import json
import os
import re
import httpx
from dotenv import load_dotenv

from services.gemini_provider import generate_with_gemini
from services.groq_provider import generate_with_groq

load_dotenv()

# ─── HuggingFace Config (legado, mantido) ────────────────────
HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")
AI_MODEL = os.getenv("AI_MODEL", "mistralai/Mixtral-8x7B-Instruct-v0.1")
HF_API_URL = f"https://api-inference.huggingface.co/models/{AI_MODEL}"

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
    - Se modelo específico: tenta apenas aquele, com fallback para template.
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
        result = await _generate_with_huggingface(prompt)
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
    result = await _generate_with_huggingface(prompt)
    if result:
        print("[AI Router] ✅ HuggingFace respondeu com sucesso!")
        return (result, "huggingface")

    # 4. Todos falharam
    print("[AI Router] ❌ Todos os provedores falharam. Usando template.")
    return (None, "none")


async def _generate_with_huggingface(prompt: str) -> dict | None:
    """
    Provider HuggingFace (Mistral). Código original mantido.
    """
    if not HF_API_KEY or HF_API_KEY == "hf_SEU_TOKEN_AQUI":
        print("[HuggingFace] Sem API Key configurada, usando fallback.")
        return None

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "inputs": f"<s>[INST] {prompt} [/INST]",
        "parameters": {
            "max_new_tokens": 3000,
            "temperature": 0.7,
            "top_p": 0.9,
            "return_full_text": False,
        },
    }

    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(HF_API_URL, json=payload, headers=headers)

            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    text = result[0].get("generated_text", "")
                    return _parse_response(text)
                return None
            else:
                print(f"[HuggingFace] Erro na API: {response.status_code} - {response.text[:200]}")
                return None

    except Exception as e:
        print(f"[HuggingFace] Exceção: {e}")
        return None


def _parse_response(text: str) -> dict | None:
    """Extrai JSON válido da resposta (usado pelo HuggingFace)."""
    json_match = re.search(r'\{[\s\S]*\}', text)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError:
            pass

    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        pass

    cleaned = text.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    if cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]

    try:
        return json.loads(cleaned.strip())
    except json.JSONDecodeError:
        print("[HuggingFace] Falha no parsing da resposta da IA.")
        return None

"""
groq_provider.py — Integração com a API do Groq (Llama 3.3 70B).
Tier gratuito: 30 requisições/minuto, 14.400/dia.
Docs: https://console.groq.com/docs/api-reference
"""
import json
import os
import re
import httpx
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = "llama-3.3-70b-versatile"
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


async def generate_with_groq(prompt: str) -> dict | None:
    """
    Envia prompt para a API do Groq e retorna JSON.
    Retorna None se falhar (para fallback).
    """
    if not GROQ_API_KEY:
        print("[Groq] Sem API Key configurada.")
        return None

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {
                "role": "system",
                "content": "Você é um especialista em pedagogia e educação. "
                           "Responda SEMPRE em JSON válido, sem texto adicional.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        "temperature": 0.7,
        "max_tokens": 4096,
        "top_p": 0.9,
        "response_format": {"type": "json_object"},
    }

    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(GROQ_URL, json=payload, headers=headers)

            if response.status_code == 200:
                result = response.json()
                choices = result.get("choices", [])
                if choices:
                    text = choices[0].get("message", {}).get("content", "")
                    return _parse_response(text)
                print("[Groq] Resposta vazia ou sem choices.")
                return None
            else:
                print(f"[Groq] Erro na API: {response.status_code} - {response.text[:300]}")
                return None

    except Exception as e:
        print(f"[Groq] Exceção: {e}")
        return None


def _parse_response(text: str) -> dict | None:
    """Extrai JSON válido da resposta do Groq."""
    # Estratégia 1: Parse direto (Groq com response_format retorna JSON limpo)
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        pass

    # Estratégia 2: Buscar bloco JSON com regex
    json_match = re.search(r'\{[\s\S]*\}', text)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError:
            pass

    # Estratégia 3: Limpar markdown
    cleaned = text.strip()
    for prefix in ["```json", "```"]:
        if cleaned.startswith(prefix):
            cleaned = cleaned[len(prefix):]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]

    try:
        return json.loads(cleaned.strip())
    except json.JSONDecodeError:
        print("[Groq] Falha no parsing da resposta.")
        return None

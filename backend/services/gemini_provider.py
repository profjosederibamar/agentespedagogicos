"""
gemini_provider.py — Integração com a API do Google Gemini (gemini-2.0-flash).
Tier gratuito: 15 requisições/minuto, 1.500/dia.
Docs: https://ai.google.dev/gemini-api/docs
"""
import json
import os
import httpx
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.0-flash"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"


async def generate_with_gemini(prompt: str) -> dict | None:
    """
    Envia prompt para a API do Google Gemini e retorna JSON.
    Retorna None se falhar (para fallback).
    """
    if not GEMINI_API_KEY:
        print("[Gemini] Sem API Key configurada.")
        return None

    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "topP": 0.9,
            "maxOutputTokens": 4096,
            "responseMimeType": "application/json",
        },
    }

    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                f"{GEMINI_URL}?key={GEMINI_API_KEY}",
                json=payload,
                headers=headers,
            )

            if response.status_code == 200:
                result = response.json()
                # Extrair texto da resposta do Gemini
                candidates = result.get("candidates", [])
                if candidates:
                    content = candidates[0].get("content", {})
                    parts = content.get("parts", [])
                    if parts:
                        text = parts[0].get("text", "")
                        return _parse_response(text)
                print("[Gemini] Resposta vazia ou sem candidatos.")
                return None
            else:
                print(f"[Gemini] Erro na API: {response.status_code} - {response.text[:300]}")
                return None

    except Exception as e:
        print(f"[Gemini] Exceção: {e}")
        return None


def _parse_response(text: str) -> dict | None:
    """Extrai JSON válido da resposta do Gemini."""
    import re

    # Estratégia 1: Parse direto (Gemini com responseMimeType retorna JSON limpo)
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
        print("[Gemini] Falha no parsing da resposta.")
        return None

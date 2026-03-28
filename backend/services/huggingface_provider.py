"""
huggingface_provider.py — Integração com a API do Hugging Face (Mistral/Mixtral).
Docs: https://huggingface.co/docs/api-inference/index
"""
import json
import os
import re
import httpx
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")
AI_MODEL = os.getenv("AI_MODEL", "mistralai/Mixtral-8x7B-Instruct-v0.1")
HF_API_URL = f"https://api-inference.huggingface.co/models/{AI_MODEL}"

async def generate_with_huggingface(prompt: str) -> dict | None:
    """
    Envia prompt para a API do Hugging Face e retorna JSON.
    Retorna None se falhar (para fallback).
    """
    if not HF_API_KEY or HF_API_KEY.startswith("hf_SEU_TOKEN"):
        print("[HuggingFace] Sem API Key válida configurada.")
        return None

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json",
    }

    # Formatando para Mistral (Instrução)
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
    """Extrai JSON válido da resposta do Hugging Face."""
    # Estratégia 1: Buscar bloco JSON com regex
    json_match = re.search(r'\{[\s\S]*\}', text)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError:
            pass

    # Estratégia 2: Parse direto
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        pass

    # Estratégia 3: Limpar markdown
    cleaned = text.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    elif cleaned.startswith("```"):
        cleaned = cleaned[3:]
    
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]

    try:
        return json.loads(cleaned.strip())
    except json.JSONDecodeError:
        print("[HuggingFace] Falha no parsing da resposta da IA.")
        return None

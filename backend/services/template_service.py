"""
template_service.py — Fallback com templates inteligentes.
Gera sequências didáticas completas usando os templates dos agentes,
sem depender de API externa.
"""
from agents import AGENTS


def generate_from_template(practice: str, tema: str, faixa_etaria: str, tempo: str, objetivos: str) -> dict:
    """
    Gera sequência didática usando o template do agente selecionado.
    Funciona 100% offline.
    """
    agent_class = AGENTS.get(practice)
    if not agent_class:
        raise ValueError(f"Prática pedagógica não encontrada: {practice}")

    agent = agent_class()
    template = agent.get_template(tema, faixa_etaria, tempo, objetivos)

    return template

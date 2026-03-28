"""
BaseAgent — Classe base para todos os agentes pedagógicos.
Cada agente herda desta classe e define seu system_prompt e templates específicos.
"""
from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """Classe base abstrata para agentes pedagógicos."""

    def __init__(self):
        self.name = self.get_name()
        self.description = self.get_description()
        self.system_prompt = self.get_system_prompt()

    @abstractmethod
    def get_name(self) -> str:
        """Retorna o nome da prática pedagógica."""
        pass

    @abstractmethod
    def get_description(self) -> str:
        """Retorna descrição curta da prática."""
        pass

    @abstractmethod
    def get_system_prompt(self) -> str:
        """Retorna o system prompt específico do agente para a IA."""
        pass

    @abstractmethod
    def get_template(self, tema: str, faixa_etaria: str, tempo: str, objetivos: str) -> dict:
        """Retorna um template de sequência didática (fallback sem IA)."""
        pass

    def build_prompt(self, tema: str, faixa_etaria: str, tempo: str, objetivos: str) -> str:
        """Constrói o prompt completo para enviar à IA."""
        obj_text = objetivos if objetivos else "Definidos pelo agente conforme o tema"

        return f"""{self.system_prompt}

DADOS DA SOLICITAÇÃO:
- Tema da aula: {tema}
- Faixa etária dos alunos: {faixa_etaria}
- Tempo disponível: {tempo}
- Objetivos específicos: {obj_text}

FORMATO DE RESPOSTA OBRIGATÓRIO (responda em JSON válido):
{{
    "titulo": "Título criativo da sequência didática",
    "problema_central": "Problema ou desafio central que guiará a aprendizagem",
    "objetivos_aprendizagem": ["objetivo 1", "objetivo 2", "objetivo 3", "objetivo 4"],
    "integracao_interdisciplinar": {{
        "descricao": "Como as disciplinas se conectam",
        "disciplinas": ["Disciplina 1: conexão", "Disciplina 2: conexão"]
    }},
    "passo_a_passo": [
        {{
            "aula": 1,
            "titulo": "Título da aula",
            "duracao": "tempo",
            "atividades": ["atividade 1", "atividade 2"],
            "recursos": ["recurso 1", "recurso 2"]
        }}
    ],
    "atividades_praticas": ["atividade 1", "atividade 2", "atividade 3"],
    "estrategias_engajamento": ["estratégia 1", "estratégia 2", "estratégia 3"],
    "avaliacao": {{
        "formativa": ["método 1", "método 2"],
        "somativa": ["método 1", "método 2"]
    }},
    "desenvolvimento_socioemocional": ["competência 1", "competência 2", "competência 3"],
    "adaptacao_hibrido": ["adaptação 1", "adaptação 2"],
    "uso_tecnologia": ["tecnologia 1", "tecnologia 2", "tecnologia 3"],
    "produto_final": "Descrição detalhada do produto final esperado"
}}

IMPORTANTE: Responda APENAS com o JSON, sem texto antes ou depois. O conteúdo deve ser em PORTUGUÊS BRASILEIRO, criativo, prático e aplicável em sala de aula real."""

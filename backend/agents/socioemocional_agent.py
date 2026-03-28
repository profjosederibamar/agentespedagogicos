"""Agente: Educação Socioemocional"""
from .base_agent import BaseAgent


class SocioemocionalAgent(BaseAgent):
    def get_name(self) -> str:
        return "Educação Socioemocional"

    def get_description(self) -> str:
        return "Integra competências socioemocionais ao conteúdo acadêmico de forma intencional."

    def get_system_prompt(self) -> str:
        return """Você é um agente especialista em EDUCAÇÃO SOCIOEMOCIONAL.
Crie sequências que integrem competências CASEL (autoconsciência, autogestão, consciência social, habilidades de relacionamento, tomada de decisão responsável) ao conteúdo. Inclua rodas de conversa, práticas de mindfulness, dinâmicas de autoconhecimento e reflexão emocional.
FOCO: O socioemocional não é 'extra', é o CENTRO da experiência de aprendizagem."""

    def get_template(self, tema: str, faixa_etaria: str, tempo: str, objetivos: str) -> dict:
        return {
            "titulo": f"Aprendizagem com Coração e Mente: '{tema}' e o Desenvolvimento Integral",
            "problema_central": f"Como aprender sobre '{tema}' pode nos ajudar a nos conhecer melhor, nos relacionar com respeito e tomar decisões éticas? O desafio é integrar o conteúdo acadêmico ao desenvolvimento emocional e social.",
            "objetivos_aprendizagem": [
                f"Aprender sobre '{tema}' conectando conteúdo a experiências emocionais",
                "Desenvolver autoconsciência: reconhecer emoções, valores e forças pessoais",
                "Praticar autogestão: regular emoções e definir metas de aprendizagem",
                "Exercitar consciência social: empatia e respeito à diversidade",
                "Tomar decisões responsáveis: ética, cuidado e pensamento consequencial"
            ],
            "integracao_interdisciplinar": {
                "descricao": "Competências socioemocionais permeiam todas as áreas do conhecimento.",
                "disciplinas": [
                    f"Disciplina principal: {tema} como veículo para reflexões socioemocionais",
                    "Língua Portuguesa: narrativas pessoais, diários e expressão de sentimentos",
                    "Artes: expressão emocional através de criação artística",
                    "Ciências Humanas: ética, cidadania e relações sociais",
                    "Educação Física: consciência corporal e cooperação"
                ]
            },
            "passo_a_passo": [
                {"aula": 1, "titulo": "Autoconsciência — Quem Sou Eu Diante do Tema", "duracao": tempo, "atividades": ["Momento mindfulness: respiração consciente e presença (3 min)", "Roda de conversa: 'O que sinto quando penso em...?'", f"Conexão pessoal com '{tema}': como isso afeta minha vida?", "Mapa de emoções: representação visual dos sentimentos sobre o tema", "Check-in emocional: como estou chegando? como quero sair?"], "recursos": ["Áudio de mindfulness", "Cartões de emoções", "Material para mapa visual", "Caderno de reflexões"]},
                {"aula": 2, "titulo": "Empatia — O Outro e o Tema", "duracao": tempo, "atividades": ["Aquecimento: jogo de espelho em duplas", "Dramatização: diferentes perspectivas sobre o tema", "Exercício de escuta ativa: ouvir sem julgar", "Produção: carta empática para alguém afetado pelo tema"], "recursos": ["Roteiros de dramatização", "Fichas de perspectivas", "Template de carta", "Material artístico"]},
                {"aula": 3, "titulo": "Colaboração e Gestão Emocional", "duracao": tempo, "atividades": ["Dinâmica de cooperação: desafio que exige trabalho em equipe", "Pausa reflexiva: como me senti durante o desafio?", "Estratégias de regulação emocional diante de frustrações", "Produção coletiva sobre o tema integrando aprendizados emocionais"], "recursos": ["Material para dinâmica", "Quadro de regulação emocional", "Material de produção", "Ficha de reflexão"]},
                {"aula": 4, "titulo": "Decisões Responsáveis e Expressão Final", "duracao": tempo, "atividades": ["Dilema ético relacionado ao tema: discussão em grupos", "Tomada de decisão responsável: análise de consequências", "Expressão artística final: representação da jornada socioemocional", "Roda de encerramento: 'Uma coisa que levo dessa experiência'", "Check-out emocional e celebração afetiva"], "recursos": ["Dilema ético impresso", "Quadro de consequências", "Material artístico variado", "Espaço organizado em roda"]}
            ],
            "atividades_praticas": [
                "Mapa de emoções: representação visual dos sentimentos sobre o tema",
                "Dramatização empática: vivenciar diferentes perspectivas",
                "Diário socioemocional: registro de emoções ao longo da sequência",
                "Carta empática para alguém afetado pelo tema estudado",
                "Criação artística que expressa a jornada emocional do aprendizado"
            ],
            "estrategias_engajamento": [
                "Ambiente seguro e acolhedor para expressão genuína",
                "Check-in/check-out emocional em toda aula",
                "Conexão pessoal com o conteúdo (storytelling)",
                "Variedade de formas de expressão (verbal, artística, corporal)",
                "Reconhecimento e validação de todas as emoções"
            ],
            "avaliacao": {
                "formativa": ["Observação sensível da participação e engajamento", "Diário socioemocional: evolução das reflexões", "Qualidade da escuta e interação nas rodas", "Check-ins emocionais como termômetro da turma"],
                "somativa": ["Produção artística expressiva sobre a jornada", "Reflexão escrita sobre crescimento socioemocional", "Portfólio de atividades socioemocionais", "Autoavaliação sobre competências CASEL desenvolvidas"]
            },
            "desenvolvimento_socioemocional": [
                "Autoconsciência: reconhecer emoções, valores e impacto pessoal",
                "Autogestão: regular emoções e manter foco diante de desafios",
                "Consciência social: praticar empatia e valorizar diversidade",
                "Habilidades de relacionamento: comunicar com respeito e cooperar",
                "Tomada de decisão responsável: considerar ética e consequências"
            ],
            "adaptacao_hibrido": [
                "Práticas de mindfulness guiadas por áudio/vídeo em casa",
                "Diário socioemocional digital (Google Docs privado)",
                "Rodas de conversa adaptadas para videochamada (câmeras ligadas)",
                "Exercícios de empatia e escuta ativa em duplas online",
                "Mural virtual de sentimentos e expressão (Padlet anônimo)"
            ],
            "uso_tecnologia": [
                "Headspace/Calm: apps de mindfulness para momentos de pausa",
                "Padlet anônimo para expressão segura de sentimentos",
                "Canva para criação de mapas de emoções visuais",
                "Flipgrid para reflexões em vídeo (ambiente seguro)",
                "Google Forms para check-ins emocionais digitais"
            ],
            "produto_final": f"PORTFÓLIO SOCIOEMOCIONAL sobre '{tema}': (1) diário de reflexões emocionais ao longo da sequência, (2) produção artística que expressa a jornada de aprendizagem emocional, (3) carta empática endereçada a alguém conectado ao tema, e (4) compromisso pessoal: 'O que vou fazer diferente a partir do que aprendi'."
        }

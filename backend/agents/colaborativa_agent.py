"""Agente: Aprendizagem Colaborativa"""
from .base_agent import BaseAgent


class ColaborativaAgent(BaseAgent):
    def get_name(self) -> str:
        return "Aprendizagem Colaborativa"

    def get_description(self) -> str:
        return "Aprendizagem centrada na interação e construção coletiva do conhecimento."

    def get_system_prompt(self) -> str:
        return """Você é um agente especialista em APRENDIZAGEM COLABORATIVA.
Crie sequências com trabalho em grupo estruturado, interdependência positiva, responsabilidade individual, técnicas como jigsaw, think-pair-share, world café e construção coletiva.
FOCO: Colaboração REAL com papéis definidos e interdependência positiva."""

    def get_template(self, tema: str, faixa_etaria: str, tempo: str, objetivos: str) -> dict:
        return {
            "titulo": f"Aprendendo Juntos: '{tema}' — Construção Coletiva do Conhecimento",
            "problema_central": f"Como podemos construir juntos um entendimento profundo sobre '{tema}' que nenhum de nós conseguiria sozinho? O desafio é usar a inteligência coletiva para explorar o tema de múltiplas perspectivas.",
            "objetivos_aprendizagem": [
                f"Construir coletivamente compreensão profunda sobre '{tema}'",
                "Desenvolver habilidades de comunicação e escuta ativa",
                "Trabalhar com interdependência positiva e responsabilidade individual",
                "Aprender a aprender com os outros, valorizando diferentes perspectivas",
                "Produzir conhecimento coletivo de qualidade superior ao individual"
            ],
            "integracao_interdisciplinar": {
                "descricao": "A colaboração enriquece quando cada membro traz expertise de áreas diferentes.",
                "disciplinas": [
                    f"Disciplina principal: {tema} explorado por diferentes ângulos",
                    "Língua Portuguesa: argumentação oral e escrita coletiva",
                    "Matemática: análise de dados e raciocínio lógico em grupo",
                    "Ciências Humanas: perspectivas sociais, históricas e éticas",
                    "Artes: expressão criativa coletiva e produção colaborativa"
                ]
            },
            "passo_a_passo": [
                {"aula": 1, "titulo": "Formação de Equipes e Jigsaw", "duracao": tempo, "atividades": ["Formação estratégica de equipes (4-5 alunos)", "Técnica Jigsaw: cada membro estuda parte diferente do tema", "Reunião de especialistas: membros de diferentes equipes com mesmo subtema", "Retorno às equipes: cada um ensina sua parte"], "recursos": ["Material dividido em partes", "Roteiro de especialista", "Fichas de síntese", "Timer"]},
                {"aula": 2, "titulo": "World Café — Debates Rotativos", "duracao": tempo, "atividades": ["Montagem de 4 mesas temáticas com perguntas provocadoras", "Rodadas de 8-10 min: grupos circulam pelas mesas", "Anfitriões ficam nas mesas e coletam contribuições", "Síntese coletiva: cada anfitrião apresenta o consolidado"], "recursos": ["Toalhas de mesa/papel kraft", "Canetas coloridas", "Perguntas provocadoras", "Timer para rotação"]},
                {"aula": 3, "titulo": "Produção Colaborativa", "duracao": tempo, "atividades": ["Think-Pair-Share: pensar individual → dupla → quarteto → grupo", "Construção coletiva de produto sobre o tema", "Papéis definidos: redator, designer, pesquisador, revisor", "Checkpoint: apresentação do progresso com feedback cruzado"], "recursos": ["Material de produção", "Template com papéis", "Checklist de qualidade", "Rubrica de feedback"]},
                {"aula": 4, "titulo": "Apresentação Coletiva e Metacognição", "duracao": tempo, "atividades": ["Apresentação dos trabalhos com participação de todos", "Feedback construtivo: 'stars and wishes' entre equipes", "Reflexão individual: 'O que aprendi com meus colegas?'", "Celebração das conquistas coletivas"], "recursos": ["Espaço de apresentação", "Fichas stars & wishes", "Diário de reflexão", "Certificados de equipe"]}
            ],
            "atividades_praticas": [
                "Jigsaw: cada um se torna especialista em um aspecto e ensina os outros",
                "World Café: debates rotativos com registro coletivo",
                "Think-Pair-Share: escalada de reflexão do individual ao coletivo",
                "Produção coletiva: texto, mural ou apresentação construída em conjunto",
                "Peer teaching: alunos ensinam e aprendem entre si"
            ],
            "estrategias_engajamento": [
                "Papéis rotativos para que todos experimentem diferentes funções",
                "Interdependência positiva: cada membro é essencial para o resultado",
                "Dinâmicas de aquecimento para criar confiança nas equipes",
                "Feedback entre pares construtivo e estruturado",
                "Celebração coletiva dos resultados do grupo"
            ],
            "avaliacao": {
                "formativa": ["Observação da qualidade das interações", "Fichas de contribuição individual", "Feedback entre pares estruturado", "Autoavaliação sobre colaboração"],
                "somativa": ["Produção coletiva final (qualidade e coesão)", "Avaliação individual sobre conteúdo aprendido", "Reflexão sobre contribuição pessoal ao grupo", "Portfólio de participação nas dinâmicas"]
            },
            "desenvolvimento_socioemocional": [
                "Empatia: ouvir e valorizar perspectivas diferentes",
                "Comunicação: expressar ideias com clareza e respeito",
                "Responsabilidade: cumprir sua parte para o bem do grupo",
                "Flexibilidade: adaptar-se às ideias e ritmos dos colegas",
                "Liderança compartilhada: todos podem liderar em momentos diferentes"
            ],
            "adaptacao_hibrido": [
                "Google Docs para escrita colaborativa em tempo real",
                "Breakout rooms para dinâmicas em pequenos grupos online",
                "Padlet/Jamboard para brainstorming virtual",
                "Fórum para discussões assíncronas entre aulas",
                "Vídeo-chamadas para reuniões de equipe remotas"
            ],
            "uso_tecnologia": [
                "Google Docs/Slides para produção colaborativa simultânea",
                "Miro/Jamboard para brainstorming e organização visual",
                "Padlet para murais colaborativos",
                "Flipgrid para compartilhamento de reflexões em vídeo",
                "Trello para gestão de tarefas do grupo"
            ],
            "produto_final": f"PRODUÇÃO COLETIVA sobre '{tema}': (1) material construído colaborativamente (texto, mural, apresentação multimídia), (2) síntese das perspectivas de todos os membros, (3) reflexão individual sobre aprendizados da colaboração, e (4) proposta de ação coletiva derivada do estudo."
        }

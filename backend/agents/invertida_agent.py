"""Agente: Sala de Aula Invertida"""
from .base_agent import BaseAgent


class InvertidaAgent(BaseAgent):
    def get_name(self) -> str:
        return "Sala de Aula Invertida"

    def get_description(self) -> str:
        return "Estudo prévio em casa, atividades práticas e aprofundamento em sala."

    def get_system_prompt(self) -> str:
        return """Você é um agente especialista em SALA DE AULA INVERTIDA (Flipped Classroom).
Crie sequências onde alunos estudam conteúdo em casa (vídeos, leituras) e usam o tempo de aula para práticas, discussões e aprofundamento com apoio do professor.
FOCO: Material de estudo prévio acessível e atividades presenciais ricas."""

    def get_template(self, tema: str, faixa_etaria: str, tempo: str, objetivos: str) -> dict:
        return {
            "titulo": f"Sala Invertida: '{tema}' — Estudar em Casa, Praticar na Escola",
            "problema_central": f"Como maximizar o tempo em sala para atividades profundas se os alunos já chegarem preparados sobre '{tema}'? O desafio é criar material de estudo prévio envolvente e atividades presenciais que aprofundem o aprendizado.",
            "objetivos_aprendizagem": [
                f"Construir conhecimento prévio sobre '{tema}' de forma autônoma",
                "Aprofundar compreensão através de atividades práticas em sala",
                "Desenvolver habilidades de estudo autônomo e autodisciplina",
                "Aplicar conceitos em situações práticas e desafiadoras",
                "Participar ativamente de discussões e debates em sala"
            ],
            "integracao_interdisciplinar": {
                "descricao": "A sala invertida permite explorar conexões interdisciplinares no tempo presencial.",
                "disciplinas": [
                    f"Disciplina principal: conteúdo teórico de {tema} no estudo prévio",
                    "Língua Portuguesa: leitura interpretativa e expressão oral nos debates",
                    "Matemática: aplicação prática e resolução de problemas em sala",
                    "Tecnologia: uso de plataformas digitais para estudo autônomo",
                    "Artes: criação de sínteses visuais e mapas mentais do conteúdo"
                ]
            },
            "passo_a_passo": [
                {"aula": 1, "titulo": "Estudo Prévio + Ativação em Sala", "duracao": tempo, "atividades": ["PRÉ-AULA (em casa): vídeo curto (5-8 min) + 3 perguntas norteadoras", "Ativação: quiz rápido para verificar estudo (5 min)", "Roda de dúvidas: esclarecimento dos pontos difíceis", "Aprofundamento: atividade prática aplicando o conceito"], "recursos": ["Vídeo-aula gravado", "Quiz (Kahoot/papel)", "Material de apoio impresso", "Roteiro de estudo"]},
                {"aula": 2, "titulo": "Estudo Prévio + Debate e Resolução", "duracao": tempo, "atividades": ["PRÉ-AULA: leitura guiada + anotações no caderno", "Think-Pair-Share: pensar, conversar, compartilhar", "Resolução de problemas em duplas com apoio do professor", "Mapa mental coletivo integrando descobertas"], "recursos": ["Texto-base para leitura", "Roteiro de anotações", "Problemas desafiadores", "Material para mapa mental"]},
                {"aula": 3, "titulo": "Estudo Prévio + Projeto Aplicado", "duracao": tempo, "atividades": ["PRÉ-AULA: podcast ou infográfico interativo", "Workshop prático: aplicar conceitos em projeto real", "Produção em equipe: criação de material sobre o tema", "Feedback do professor: mentoria individual/grupo"], "recursos": ["Podcast/infográfico", "Materiais para projeto", "Templates de produção", "Checklist de qualidade"]},
                {"aula": 4, "titulo": "Síntese e Avaliação Ativa", "duracao": tempo, "atividades": ["Revisão ativa: alunos ensinam uns aos outros (peer teaching)", "Desafio integrador: situação-problema que exige todo o conteúdo", "Autoavaliação: reflexão sobre aprendizado autônomo vs presencial", "Feedback coletivo e celebração dos aprendizados"], "recursos": ["Material de revisão", "Desafio integrador", "Ficha de autoavaliação", "Rubrica de avaliação"]}
            ],
            "atividades_praticas": [
                "Peer teaching: alunos ensinam conceitos uns aos outros",
                "Resolução de problemas desafiadores em duplas/trios",
                "Debate estruturado sobre aplicações do tema",
                "Criação de resumo visual (sketchnote) do conteúdo",
                "Workshop prático aplicando teoria estudada previamente"
            ],
            "estrategias_engajamento": [
                "Vídeos curtos e dinâmicos (máx. 8 min) para estudo prévio",
                "Quiz gamificado no início da aula para motivar estudo em casa",
                "Atividades práticas desafiadoras que só são possíveis com base teórica",
                "Reconhecimento de quem estudou: protagonismo nas discussões",
                "Variedade de formatos no estudo prévio (vídeo, texto, podcast, jogo)"
            ],
            "avaliacao": {
                "formativa": ["Quiz de entrada verificando estudo prévio", "Observação da participação nas atividades presenciais", "Anotações do estudo prévio como portfólio", "Feedback contínuo durante mentoria"],
                "somativa": ["Projeto aplicado demonstrando domínio dos conceitos", "Avaliação prática integradora", "Portfólio de estudo (anotações + produções)", "Autoavaliação estruturada sobre autonomia"]
            },
            "desenvolvimento_socioemocional": [
                "Autodisciplina: responsabilidade pelo estudo prévio",
                "Autonomia: aprender a aprender sem supervisão direta",
                "Protagonismo: preparação permite participação mais ativa",
                "Generosidade intelectual: ensinar colegas com dificuldade",
                "Metacognição: consciência sobre próprio processo de aprendizagem"
            ],
            "adaptacao_hibrido": [
                "Modelo naturalmente híbrido — estudo em casa + prática presencial",
                "Vídeo-aulas disponíveis para reassistir quantas vezes precisar",
                "Fórum de dúvidas sobre o material prévio",
                "Atividades presenciais podem ser adaptadas para videoconferência",
                "Padlet para compartilhamento de anotações e sínteses"
            ],
            "uso_tecnologia": [
                "Edpuzzle: vídeos interativos com perguntas embutidas",
                "Google Classroom: organização do material prévio e entregas",
                "Kahoot: quiz de verificação do estudo",
                "Anchor/Spotify: criação de podcasts educativos",
                "Canva: infográficos e sínteses visuais"
            ],
            "produto_final": f"PORTFÓLIO DE APRENDIZAGEM INVERTIDA sobre '{tema}': (1) caderno de anotações do estudo prévio, (2) produções criadas nas aulas presenciais, (3) material de ensino criado para peer teaching, e (4) reflexão sobre como a sala invertida potencializou seu aprendizado."
        }

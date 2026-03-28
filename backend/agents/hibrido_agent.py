"""Agente: Ensino Híbrido"""
from .base_agent import BaseAgent


class HibridoAgent(BaseAgent):
    def get_name(self) -> str:
        return "Ensino Híbrido"

    def get_description(self) -> str:
        return "Combina atividades presenciais e online de forma integrada e complementar."

    def get_system_prompt(self) -> str:
        return """Você é um agente pedagógico especialista em ENSINO HÍBRIDO.
Crie sequências que combinem presencial e online, usem modelos como rotação por estações, laboratório rotacional, sala invertida e flex. Inclua roteiros de estudo autônomo e atividades síncronas/assíncronas equilibradas.
FOCO: Integração real entre presencial e online, não apenas "dar aula com computador"."""

    def get_template(self, tema: str, faixa_etaria: str, tempo: str, objetivos: str) -> dict:
        return {
            "titulo": f"Aprendizagem Sem Fronteiras: '{tema}' — Conectando Presencial e Digital",
            "problema_central": f"Como integrar o melhor do presencial e do digital para criar uma experiência de aprendizagem sobre '{tema}' que seja personalizada, flexível e profunda?",
            "objetivos_aprendizagem": [
                f"Dominar conceitos de '{tema}' através de múltiplos canais e formatos",
                "Desenvolver autonomia e autogestão da aprendizagem",
                "Utilizar ferramentas digitais como extensão do espaço de aprendizagem",
                "Colaborar em ambientes tanto presenciais quanto virtuais",
                "Personalizar o percurso de aprendizagem conforme ritmo individual"
            ],
            "integracao_interdisciplinar": {
                "descricao": "O ensino híbrido permite integrar disciplinas em diferentes ambientes.",
                "disciplinas": [
                    f"Disciplina principal: conteúdo sobre {tema} em formato multimodal",
                    "Língua Portuguesa: produção textual digital e comunicação online",
                    "Matemática: análise de dados de progresso e estatísticas",
                    "Tecnologia: letramento digital e ferramentas colaborativas",
                    "Artes: produção multimídia e expressão visual digital"
                ]
            },
            "passo_a_passo": [
                {"aula": 1, "titulo": "Estação de Aprendizagem — Rotação", "duracao": tempo, "atividades": ["Estação 1: Vídeo/conteúdo interativo individual", "Estação 2: Discussão em grupo com professor", "Estação 3: Atividade prática mão-na-massa", "Estação 4: Quiz/exercícios online adaptativos", "Rotação de 10-12 min por estação"], "recursos": ["Computadores/tablets", "Material impresso", "Material prático", "QR codes das atividades"]},
                {"aula": 2, "titulo": "Laboratório Online + Mentoria Presencial", "duracao": tempo, "atividades": ["Atividade individual online: pesquisa e produção", "Mentoria presencial: professor atende grupos por nível", "Colaboração entre pares: alunos avançados ajudam colegas", "Checkpoint de progresso individual"], "recursos": ["Plataforma online", "Roteiro de estudo", "Ficha de acompanhamento", "Rubricas"]},
                {"aula": 3, "titulo": "Projeto Colaborativo Multimodal", "duracao": tempo, "atividades": ["Trabalho em grupo: produção de conteúdo sobre o tema", "Escolha do formato: vídeo, podcast, infográfico, apresentação", "Integração de pesquisa online com criação presencial", "Revisão entre pares usando rubrica compartilhada"], "recursos": ["Dispositivos de gravação", "Material de criação", "Templates de rubrica", "Internet"]},
                {"aula": 4, "titulo": "Apresentação e Avaliação Integrada", "duracao": tempo, "atividades": ["Galeria de aprendizagem: apresentação dos trabalhos", "Avaliação por pares com rubrica digital", "Quiz integrador online em tempo real", "Reflexão: roteiro de autoavaliação sobre o percurso"], "recursos": ["Projetor/TV", "Formulário digital", "Rubrica compartilhada", "Kahoot/Quizizz"]}
            ],
            "atividades_praticas": [
                "Rotação por estações com 4 ambientes diferentes de aprendizagem",
                "Produção de vídeo-aula onde alunos ensinam um conceito do tema",
                "Pesquisa online guiada com roteiro estruturado e curadoria",
                "Podcast educativo produzido em equipe sobre o tema",
                "Portfólio digital acumulativo de evidências de aprendizagem"
            ],
            "estrategias_engajamento": [
                "Personalização: alunos escolhem formato e ritmo de aprendizagem",
                "Rotação que quebra a monotonia e mantém energia alta",
                "Gamificação leve: XP por completar atividades online",
                "Feedback imediato em atividades digitais",
                "Produção autoral: alunos como criadores de conteúdo"
            ],
            "avaliacao": {
                "formativa": ["Dashboard de progresso online", "Observação nas atividades presenciais", "Quizzes formativos com feedback automático", "Reflexão semanal em diário digital"],
                "somativa": ["Projeto multimodal (vídeo, podcast ou infográfico)", "Quiz integrador presencial + online", "Portfólio digital de evidências", "Autoavaliação com rubrica estruturada"]
            },
            "desenvolvimento_socioemocional": [
                "Autonomia: autogestão do tempo e da aprendizagem online",
                "Disciplina digital: uso responsável e focado da tecnologia",
                "Colaboração: trabalhar com colegas presencial e remotamente",
                "Adaptabilidade: transitar entre diferentes formatos com flexibilidade",
                "Metacognição: refletir sobre como aprende melhor"
            ],
            "adaptacao_hibrido": [
                "Modelo já é híbrido por natureza — facilmente adaptável",
                "Atividades assíncronas com prazo flexível para estudo em casa",
                "Videoaulas gravadas como material de apoio permanente",
                "Fórum de dúvidas assíncrono para extensão das discussões",
                "Google Classroom como ambiente virtual de aprendizagem"
            ],
            "uso_tecnologia": [
                "Google Classroom/Teams como ambiente virtual central",
                "Edpuzzle para vídeos interativos com perguntas embutidas",
                "Kahoot/Quizizz para avaliações gamificadas",
                "Padlet para murais colaborativos entre aulas",
                "Loom/OBS para gravação de vídeo-aulas dos alunos"
            ],
            "produto_final": f"PORTFÓLIO HÍBRIDO sobre '{tema}': (1) produção multimodal da equipe (vídeo, podcast ou infográfico), (2) registro do percurso de aprendizagem em portfólio digital, (3) reflexão sobre como a integração presencial-digital potencializou o aprendizado, e (4) proposta de 'aula ideal' desenhada pelos alunos."
        }

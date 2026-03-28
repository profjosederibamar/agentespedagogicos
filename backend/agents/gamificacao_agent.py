"""Agente: Gamificação"""
from .base_agent import BaseAgent


class GamificacaoAgent(BaseAgent):
    def get_name(self) -> str:
        return "Gamificação"

    def get_description(self) -> str:
        return "Transforma o aprendizado em uma experiência de jogo com missões, pontos, conquistas e narrativa envolvente."

    def get_system_prompt(self) -> str:
        return """Você é um agente pedagógico especialista em GAMIFICAÇÃO EDUCACIONAL.

Seu papel é criar sequências didáticas que:
- Transformem a aprendizagem em uma JORNADA DE JOGO imersiva
- Usem mecânicas de jogos: missões, pontos, níveis, conquistas, rankings
- Criem uma NARRATIVA ENVOLVENTE que conecte todas as aulas
- Mantenham motivação alta através de desafios progressivos
- Equilibrem diversão e aprendizado profundo
- Incluam recompensas significativas (não apenas pontos vazios)
- Sejam inclusivas e permitam diferentes formas de sucesso

FOCO ESPECÍFICO: A narrativa deve ser IMERSIVA e os desafios devem escalar em complexidade."""

    def get_template(self, tema: str, faixa_etaria: str, tempo: str, objetivos: str) -> dict:
        return {
            "titulo": f"Quest Educacional: A Grande Aventura de '{tema}' — Missão Conhecimento",
            "problema_central": f"Aventureiros do conhecimento, uma grande missão aguarda vocês! O mundo de '{tema}' está em perigo e apenas equipes de heróis intelectuais podem salvá-lo. Cada equipe precisa completar missões, coletar conhecimento e enfrentar o Boss Final para restaurar a sabedoria perdida!",
            "objetivos_aprendizagem": [
                f"Dominar conceitos essenciais de '{tema}' através de desafios progressivos",
                "Desenvolver estratégia e pensamento tático para resolver problemas",
                "Colaborar em equipe para completar missões que exigem múltiplas habilidades",
                "Demonstrar aprendizado através de desafios práticos em diferentes níveis",
                "Refletir sobre o processo de aprendizagem através da jornada do herói"
            ],
            "integracao_interdisciplinar": {
                "descricao": "Cada missão integra diferentes disciplinas como habilidades especiais do personagem.",
                "disciplinas": [
                    f"Disciplina Principal: missões centrais sobre {tema}",
                    "Matemática: sistema de pontos, estatísticas, ranking e cálculos estratégicos",
                    "Língua Portuguesa: narrativa, diário do herói, comunicação nas missões",
                    "Artes: criação de avatares, brasões de equipe e mapas de missão",
                    "Educação Física: missões que envolvem movimento e dinâmicas corporais"
                ]
            },
            "passo_a_passo": [
                {
                    "aula": 1,
                    "titulo": "Fase 1 — Criação dos Heróis e Primeira Missão",
                    "duracao": tempo,
                    "atividades": [
                        "Introdução da narrativa épica: o mundo do conhecimento está em perigo!",
                        "Formação de guildas (equipes) e criação de identidade: nome, brasão, grito de guerra",
                        "Criação de avatares com classes (Pesquisador, Criador, Estrategista, Comunicador)",
                        "Missão Tutorial: desafio introdutório para ganhar primeiros XP e aprender as regras",
                        f"Desbloqueio do Mapa de '{tema}': revelação do que será explorado"
                    ],
                    "recursos": ["Carta de missão impressa", "Ficha de personagem", "Sistema de pontos (quadro)", "Materiais para brasão", "Mapa de aventura"]
                },
                {
                    "aula": 2,
                    "titulo": "Fase 2 — Missões de Exploração (Nível Intermediário)",
                    "duracao": tempo,
                    "atividades": [
                        "Desbloqueio de 3 missões paralelas (equipes escolhem a ordem)",
                        "Missão Conhecimento: quiz progressivo com dificuldade crescente (+XP)",
                        "Missão Criação: produzir algo que demonstre domínio de um conceito (+moedas)",
                        "Missão Cooperação: desafio que exige colaboração entre guildas (+bônus de aliança)",
                        "Power-up: recurso especial desbloqueado pela equipe com melhor desempenho coletivo"
                    ],
                    "recursos": ["Cartas de missão", "Material para atividades práticas", "Placar de XP", "Selos de conquista", "Timer/cronômetro"]
                },
                {
                    "aula": 3,
                    "titulo": "Fase 3 — Desafio Boss e Side Quests",
                    "duracao": tempo,
                    "atividades": [
                        "Side quests opcionais para ganhar XP bônus (atividades extras)",
                        "Preparação para o Boss Final: revisão estratégica em equipe",
                        "BOSS FIGHT: grande desafio que integra todo o conteúdo aprendido",
                        "O Boss pode ser: debate, prova prática, construção ou apresentação desafiadora",
                        "Reveal: cada equipe descobre quantos pontos conquistou no Boss"
                    ],
                    "recursos": ["Desafio Boss preparado", "Materiais conforme tipo de desafio", "Cronômetro", "Sistema de pontuação especial"]
                },
                {
                    "aula": 4,
                    "titulo": "Fase Final — Cerimônia de Premiação e Reflexão",
                    "duracao": tempo,
                    "atividades": [
                        "Contagem final de XP e revelação do ranking",
                        "Premiação por categorias: Melhor Guilda, Herói do Conhecimento, Mestre da Criatividade",
                        "Reflexão gamificada: 'Power-ups que levou para a vida real'",
                        "Diário do herói: registro escrito da jornada de aprendizagem",
                        "Easter egg final: revelação de conteúdo surpresa conectado ao tema",
                        "Celebração e entrega de certificados/conquistas"
                    ],
                    "recursos": ["Certificados de conquista", "Quadro de ranking final", "Selos e medalhas", "Material para reflexão"]
                }
            ],
            "atividades_praticas": [
                "Quiz Battle: equipes competem em rodadas de perguntas com dificuldade crescente",
                "Construção relâmpago: criar algo em tempo limitado usando materiais surpresa",
                "Enigma em cadeia: cada pista resolvida leva à próxima (escape room educacional)",
                "Desafio de comunicação: explicar um conceito sem usar certas palavras-chave",
                "Speed challenge: resolver o máximo de problemas em tempo cronometrado"
            ],
            "estrategias_engajamento": [
                "Narrativa contínua que prende a atenção e cria expectativa entre aulas",
                "Sistema de recompensas tangíveis e simbólicas (medalhas, privilégios, títulos)",
                "Escolhas que importam: decisões das equipes afetam o rumo da aventura",
                "Elementos surpresa: eventos aleatórios, power-ups e easter eggs",
                "Rankings visíveis mas com múltiplas categorias (todos podem vencer em algo)"
            ],
            "avaliacao": {
                "formativa": [
                    "Sistema de XP como indicador contínuo de aprendizagem",
                    "Observação do engajamento e colaboração durante as missões",
                    "Checkpoints: mini-avaliações disfarçadas de 'verificação de nível'",
                    "Diário do herói: reflexões sobre aprendizados a cada fase"
                ],
                "somativa": [
                    "Desempenho no Boss Fight (avaliação integradora)",
                    "Portfólio de conquistas: produção acumulada ao longo das missões",
                    "Apresentação final sobre os aprendizados do tema",
                    "Autoavaliação sobre crescimento ao longo da jornada"
                ]
            },
            "desenvolvimento_socioemocional": [
                "Resiliência: aprender com erros (perder XP) e tentar novamente",
                "Espírito esportivo: competir com ética e respeitar adversários",
                "Colaboração estratégica: combinar forças para superar desafios maiores",
                "Autogestão: administrar recursos e tempo durante as missões",
                "Celebração coletiva: reconhecer conquistas dos outros com genuína alegria"
            ],
            "adaptacao_hibrido": [
                "Missões assíncronas que podem ser completadas online em casa",
                "Plataforma de ranking online (planilha compartilhada ou Classcraft)",
                "Fórum de estratégia: equipes planejam próximos passos remotamente",
                "Quizzes online com feedback automático via Google Forms ou Kahoot",
                "Badges digitais enviados por e-mail ou grupo de WhatsApp da turma"
            ],
            "uso_tecnologia": [
                "Kahoot/Quizizz para quizzes gamificados em tempo real",
                "Classcraft ou ClassDojo para sistema de pontos e avatares",
                "Genially para criação de escape rooms virtuais",
                "Google Planilhas para ranking transparente e atualizado",
                "Canva para criação de certificados, badges e materiais visuais"
            ],
            "produto_final": f"Uma JORNADA GAMIFICADA COMPLETA sobre '{tema}', onde cada equipe terá: (1) portfólio de missões completadas com evidências de aprendizado, (2) artefatos criados durante as missões (respostas, criações, soluções), (3) diário do herói com reflexões sobre a jornada, e (4) apresentação final estilo 'speedrun' resumindo tudo que aprenderam em 5 minutos."
        }

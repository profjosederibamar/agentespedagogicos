"""Agente: Aprendizagem Baseada em Projetos (ABP)"""
from .base_agent import BaseAgent


class ABPAgent(BaseAgent):
    def get_name(self) -> str:
        return "Aprendizagem Baseada em Projetos (ABP)"

    def get_description(self) -> str:
        return "Gera sequências didáticas centradas em projetos reais, onde os alunos investigam, criam e apresentam soluções concretas."

    def get_system_prompt(self) -> str:
        return """Você é um agente pedagógico especialista em APRENDIZAGEM BASEADA EM PROJETOS (ABP).

Seu papel é criar sequências didáticas que:
- Partam de um PROJETO REAL e significativo para os alunos
- Envolvam investigação, planejamento, execução e apresentação
- Conectem múltiplas disciplinas através do projeto
- Desenvolvam habilidades do século XXI (colaboração, comunicação, pensamento crítico, criatividade)
- Resultem em um PRODUTO FINAL tangível e apresentável
- Incluam momentos de reflexão e autoavaliação
- Sejam viáveis para a realidade escolar brasileira

FOCO ESPECÍFICO: O projeto deve ter IMPACTO REAL na comunidade escolar ou local."""

    def get_template(self, tema: str, faixa_etaria: str, tempo: str, objetivos: str) -> dict:
        return {
            "titulo": f"Projeto Integrador: {tema} — Transformando Conhecimento em Ação",
            "problema_central": f"Como podemos utilizar o conhecimento sobre '{tema}' para criar um projeto que tenha impacto real na nossa comunidade escolar? Os alunos serão desafiados a investigar, planejar e executar um projeto completo que demonstre domínio do tema e gere benefício coletivo.",
            "objetivos_aprendizagem": [
                f"Compreender os conceitos fundamentais relacionados a '{tema}' por meio de investigação ativa",
                "Desenvolver habilidades de pesquisa, planejamento e gestão de projetos",
                "Trabalhar colaborativamente em equipe, distribuindo responsabilidades",
                "Criar um produto final tangível que demonstre aprendizado significativo",
                "Apresentar resultados de forma clara e persuasiva para diferentes públicos"
            ],
            "integracao_interdisciplinar": {
                "descricao": f"O projeto sobre '{tema}' integra naturalmente várias disciplinas, criando conexões significativas entre áreas do conhecimento.",
                "disciplinas": [
                    f"Língua Portuguesa: pesquisa, leitura, escrita de relatórios e apresentação oral sobre {tema}",
                    f"Matemática: coleta e análise de dados, gráficos e estatísticas relacionados ao projeto",
                    f"Ciências: investigação científica e experimentação conectada a {tema}",
                    "Artes: design visual, criação de materiais de divulgação e expressão artística",
                    "Geografia/História: contextualização social e histórica do tema"
                ]
            },
            "passo_a_passo": [
                {
                    "aula": 1,
                    "titulo": "Lançamento do Projeto — Provocação e Investigação Inicial",
                    "duracao": tempo,
                    "atividades": [
                        f"Dinâmica de sensibilização: apresentação de situação-problema real relacionada a '{tema}'",
                        "Brainstorming coletivo: 'O que sabemos? O que precisamos descobrir?'",
                        "Formação de equipes e definição de papéis (líder, pesquisador, designer, porta-voz)",
                        "Elaboração do mural de perguntas norteadoras da investigação"
                    ],
                    "recursos": ["Quadro/painel colaborativo", "Post-its", "Projetor/TV para vídeo motivacional", "Folhas A3 para mapa mental"]
                },
                {
                    "aula": 2,
                    "titulo": "Fase de Pesquisa e Planejamento",
                    "duracao": tempo,
                    "atividades": [
                        "Pesquisa orientada em fontes diversas (livros, internet, entrevistas)",
                        "Organização das informações em fichamentos e mapas conceituais",
                        "Elaboração do plano de projeto: objetivos, cronograma, recursos necessários",
                        "Checkpoint: cada equipe apresenta seu plano em 3 minutos"
                    ],
                    "recursos": ["Computadores/tablets", "Biblioteca", "Roteiro de pesquisa estruturado", "Template de plano de projeto"]
                },
                {
                    "aula": 3,
                    "titulo": "Mão na Massa — Execução do Projeto",
                    "duracao": tempo,
                    "atividades": [
                        "Execução das atividades planejadas por cada equipe",
                        "Criação do produto final (protótipo, maquete, campanha, material didático)",
                        "Registro do processo em diário de bordo/portfólio",
                        "Revisão entre pares: equipes avaliam o progresso umas das outras"
                    ],
                    "recursos": ["Materiais variados conforme o projeto", "Diário de bordo", "Câmera/celular para registro", "Rubrica de avaliação entre pares"]
                },
                {
                    "aula": 4,
                    "titulo": "Apresentação e Celebração",
                    "duracao": tempo,
                    "atividades": [
                        "Finalização e ensaio das apresentações",
                        "Feira de projetos: cada equipe apresenta seu produto final",
                        "Sessão de perguntas e feedback construtivo da turma e convidados",
                        "Reflexão individual escrita: 'O que aprendi? Como cresci?'",
                        "Celebração coletiva dos resultados alcançados"
                    ],
                    "recursos": ["Espaço para feira/exposição", "Projetor/TV", "Fichas de avaliação", "Certificados de participação"]
                }
            ],
            "atividades_praticas": [
                f"Investigação de campo: visita técnica ou entrevista com especialista sobre {tema}",
                "Construção de protótipo ou maquete representando a solução proposta",
                "Produção de infográfico ou vídeo curto explicando o projeto",
                "Campanha de conscientização na escola sobre os aprendizados do projeto",
                "Criação de portfólio digital documentando todo o processo"
            ],
            "estrategias_engajamento": [
                "Conexão com problemas reais da comunidade para gerar senso de propósito",
                "Autonomia das equipes na escolha do recorte e abordagem do projeto",
                "Checkpoints regulares com feedback construtivo e celebração de progressos",
                "Uso de tecnologia (vídeos, apps, redes sociais) para pesquisa e divulgação",
                "Convite a membros da comunidade para assistir às apresentações finais"
            ],
            "avaliacao": {
                "formativa": [
                    "Observação contínua da participação e colaboração em equipe",
                    "Diário de bordo com reflexões individuais sobre o processo",
                    "Checkpoints de progresso com rubricas claras",
                    "Autoavaliação e avaliação entre pares ao longo do projeto"
                ],
                "somativa": [
                    "Avaliação do produto final com rubrica criteriosa",
                    "Apresentação oral com critérios de clareza, domínio e criatividade",
                    "Portfólio completo do projeto (processo + produto)",
                    "Relatório final escrito com reflexão sobre aprendizados"
                ]
            },
            "desenvolvimento_socioemocional": [
                "Colaboração e trabalho em equipe: aprender a dividir tarefas e respeitar opiniões",
                "Resiliência e gestão de frustração: lidar com imprevistos durante o projeto",
                "Comunicação assertiva: apresentar ideias e receber feedback com maturidade",
                "Responsabilidade e compromisso: cumprir prazos e entregar sua parte",
                "Empatia: considerar diferentes perspectivas ao propor soluções"
            ],
            "adaptacao_hibrido": [
                "Pesquisa e planejamento podem ser realizados de forma assíncrona (em casa)",
                "Utilizar Google Docs/Padlet para colaboração online entre membros da equipe",
                "Gravação em vídeo das apresentações para compartilhamento com ausentes",
                "Fórum de discussão online para troca de ideias entre aulas presenciais",
                "Checkpoint virtual via videoconferência para equipes remotas"
            ],
            "uso_tecnologia": [
                "Google Docs/Slides para produção colaborativa de textos e apresentações",
                "Canva para design de infográficos e materiais visuais",
                "Padlet ou Miro para organização visual de ideias e brainstorming",
                "YouTube/TikTok para criação de vídeos curtos sobre o projeto",
                "Google Forms para coleta de dados e pesquisas de campo"
            ],
            "produto_final": f"Cada equipe produzirá um PROJETO COMPLETO sobre '{tema}', incluindo: (1) um produto tangível (protótipo, maquete, campanha, material didático ou solução prática), (2) uma apresentação oral de 10 minutos na feira de projetos, (3) um portfólio documentando todo o processo de investigação e criação, e (4) um infográfico ou vídeo curto para compartilhamento na comunidade escolar."
        }

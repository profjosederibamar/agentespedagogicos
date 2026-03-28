"""Agente: Aprendizagem Baseada em Problemas (PBL)"""
from .base_agent import BaseAgent


class PBLAgent(BaseAgent):
    def get_name(self) -> str:
        return "Aprendizagem Baseada em Problemas (PBL)"

    def get_description(self) -> str:
        return "Cria sequências onde alunos resolvem problemas complexos e autênticos, desenvolvendo raciocínio crítico e habilidades investigativas."

    def get_system_prompt(self) -> str:
        return """Você é um agente pedagógico especialista em APRENDIZAGEM BASEADA EM PROBLEMAS (PBL).

Seu papel é criar sequências didáticas que:
- Partam de um PROBLEMA REAL, complexo e autêntico
- Estimulem o raciocínio investigativo e o pensamento crítico
- Sigam o ciclo PBL: problema → hipóteses → pesquisa → solução → reflexão
- Promovam a autonomia do aluno na busca por respostas
- Integrem múltiplas disciplinas naturalmente através do problema
- Desenvolvam habilidades de análise, síntese e argumentação
- Sejam desafiadoras mas acessíveis para a faixa etária

FOCO ESPECÍFICO: O problema deve ser AUTÊNTICO e gerar curiosidade genuína nos alunos."""

    def get_template(self, tema: str, faixa_etaria: str, tempo: str, objetivos: str) -> dict:
        return {
            "titulo": f"Desafio Investigativo: Desvendando '{tema}' — Uma Jornada de Descobertas",
            "problema_central": f"Situação-problema autêntica: Imaginem que vocês são uma equipe de especialistas convidados para resolver um desafio real relacionado a '{tema}'. A comunidade precisa de respostas e soluções baseadas em evidências. Como vocês investigariam, analisariam e proporiam soluções viáveis?",
            "objetivos_aprendizagem": [
                f"Analisar criticamente o problema relacionado a '{tema}' a partir de múltiplas perspectivas",
                "Formular hipóteses fundamentadas e testáveis sobre o problema proposto",
                "Conduzir pesquisa orientada para validar ou refutar hipóteses",
                "Sintetizar informações de diferentes fontes para construir argumentação sólida",
                "Propor soluções criativas e viáveis baseadas em evidências"
            ],
            "integracao_interdisciplinar": {
                "descricao": f"O problema sobre '{tema}' exige conhecimentos de diversas áreas para ser compreendido e resolvido.",
                "disciplinas": [
                    f"Ciências: investigação científica e método experimental aplicado a {tema}",
                    "Matemática: análise de dados, probabilidade e raciocínio lógico",
                    "Língua Portuguesa: leitura interpretativa, argumentação escrita e debate oral",
                    "Ciências Humanas: contexto social, ético e histórico do problema",
                    "Tecnologia: pesquisa digital e ferramentas de análise de dados"
                ]
            },
            "passo_a_passo": [
                {
                    "aula": 1,
                    "titulo": "Apresentação do Problema — O Grande Desafio",
                    "duracao": tempo,
                    "atividades": [
                        f"Apresentação da situação-problema envolvente sobre '{tema}' (vídeo, notícia ou caso real)",
                        "Técnica KWL: O que SABEMOS? O que QUEREMOS saber? (a terceira coluna será preenchida depois)",
                        "Formulação de hipóteses iniciais em pequenos grupos",
                        "Socialização das hipóteses e definição das linhas de investigação"
                    ],
                    "recursos": ["Caso-problema impresso/projetado", "Quadro KWL", "Post-its para hipóteses", "Caderno de investigação"]
                },
                {
                    "aula": 2,
                    "titulo": "Investigação e Coleta de Evidências",
                    "duracao": tempo,
                    "atividades": [
                        "Pesquisa orientada em fontes diversas (livros, artigos, vídeos, dados)",
                        "Entrevistas com especialistas (professor de outra disciplina, profissional da área)",
                        "Organização das evidências: o que confirma/refuta nossas hipóteses?",
                        "Registro estruturado das descobertas no caderno de investigação"
                    ],
                    "recursos": ["Computadores/biblioteca", "Roteiro de pesquisa", "Ficha de registro de evidências", "Lista de fontes confiáveis"]
                },
                {
                    "aula": 3,
                    "titulo": "Análise e Construção da Solução",
                    "duracao": tempo,
                    "atividades": [
                        "Análise coletiva das evidências encontradas por cada grupo",
                        "Debate estruturado: confronto de hipóteses com as evidências",
                        "Elaboração da solução/resposta fundamentada ao problema",
                        "Preparação do relatório de descobertas (visual + escrito)"
                    ],
                    "recursos": ["Dados coletados", "Template de relatório", "Material para apresentação visual", "Rubrica de análise"]
                },
                {
                    "aula": 4,
                    "titulo": "Apresentação das Soluções e Metacognição",
                    "duracao": tempo,
                    "atividades": [
                        "Apresentação das soluções propostas por cada equipe (formato seminário)",
                        "Sessão de perguntas e contra-argumentação entre equipes",
                        "Preenchimento da coluna 'O que APRENDEMOS' do quadro KWL",
                        "Reflexão metacognitiva: 'Como meu pensamento mudou ao longo do processo?'",
                        "Avaliação individual e por pares"
                    ],
                    "recursos": ["Projetor/TV", "Fichas de avaliação por pares", "Quadro KWL atualizado", "Formulário de reflexão"]
                }
            ],
            "atividades_praticas": [
                "Laboratório de hipóteses: testagem prática de hipóteses formuladas pelos alunos",
                "Análise de caso real: estudo de situação similar resolvida por profissionais",
                "Debate argumentativo: defesa de posições com base em evidências coletadas",
                "Mapa de causa e efeito: visualização das relações entre variáveis do problema",
                "Simulação: representação do problema em escala reduzida para análise"
            ],
            "estrategias_engajamento": [
                "Problema apresentado como 'missão' com narrativa envolvente",
                "Quadro de progresso visual: equipes acompanham avanço da investigação",
                "Momentos 'eureka' planejados: descobertas que surpreendem e motivam",
                "Autonomia na escolha das estratégias de investigação",
                "Conexão explícita entre o problema e a vida real dos alunos"
            ],
            "avaliacao": {
                "formativa": [
                    "Caderno de investigação: registro contínuo do processo de pensamento",
                    "Observação da participação nos debates e discussões em grupo",
                    "Qualidade das hipóteses formuladas e revisadas ao longo do processo",
                    "Autoavaliação sobre o desenvolvimento do pensamento crítico"
                ],
                "somativa": [
                    "Relatório final de investigação (escrito + visual)",
                    "Apresentação oral da solução com argumentação fundamentada",
                    "Avaliação da qualidade das evidências e da lógica argumentativa",
                    "Reflexão metacognitiva escrita sobre o percurso de aprendizagem"
                ]
            },
            "desenvolvimento_socioemocional": [
                "Pensamento crítico: questionar premissas e buscar evidências antes de concluir",
                "Tolerância à ambiguidade: aprender a conviver com a incerteza durante a investigação",
                "Escuta ativa: considerar argumentos diferentes dos seus durante debates",
                "Persistência: manter o rigor investigativo mesmo com dificuldades",
                "Ética: compromisso com a verdade e honestidade intelectual"
            ],
            "adaptacao_hibrido": [
                "Fase de pesquisa pode ser realizada assincronamente em casa",
                "Fórum online para compartilhamento de evidências entre equipes",
                "Videoconferência para entrevistas com especialistas externos",
                "Padlet/Miro para organização colaborativa das evidências online",
                "Gravação das apresentações finais para estudo posterior"
            ],
            "uso_tecnologia": [
                "Google Scholar e bases de dados para pesquisa acadêmica simplificada",
                "Mentimeter para votação e enquetes durante debates",
                "Google Forms para coleta de dados primários",
                "Canva para criação de infográficos com resultados",
                "Ferramentas de mapa mental (MindMeister) para organizar ideias"
            ],
            "produto_final": f"Cada equipe entregará um DOSSIÊ DE INVESTIGAÇÃO sobre '{tema}' contendo: (1) relatório escrito com hipóteses, evidências e conclusões, (2) apresentação visual (infográfico ou slides) explicando a solução proposta, (3) reflexão metacognitiva individual sobre o processo de aprendizagem, e (4) proposta de ação concreta baseada nas descobertas."
        }

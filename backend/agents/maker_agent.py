"""Agente: Cultura Maker"""
from .base_agent import BaseAgent


class MakerAgent(BaseAgent):
    def get_name(self) -> str:
        return "Cultura Maker"

    def get_description(self) -> str:
        return "Aprender fazendo! Construção de projetos com materiais acessíveis e inventividade."

    def get_system_prompt(self) -> str:
        return """Você é um agente pedagógico especialista em CULTURA MAKER.
Seu papel é criar sequências didáticas que sigam o lema 'FAÇA VOCÊ MESMO', usem materiais ACESSÍVEIS e RECICLÁVEIS, estimulem INVENTIVIDADE, incluam prototipagem e iteração, valorizem o erro como aprendizado e resultem em artefatos funcionais.
FOCO: Materiais SIMPLES para criar coisas SURPREENDENTES."""

    def get_template(self, tema: str, faixa_etaria: str, tempo: str, objetivos: str) -> dict:
        return {
            "titulo": f"Oficina Maker: Inventando com '{tema}' — Do Lixo ao Luxo do Conhecimento",
            "problema_central": f"Como CONSTRUIR algo incrível com materiais simples que ajude a entender '{tema}'? Os alunos serão inventores, projetando e construindo protótipos que demonstrem conceitos de forma tangível.",
            "objetivos_aprendizagem": [
                f"Compreender conceitos de '{tema}' através da construção prática",
                "Desenvolver habilidades de prototipagem, teste e iteração",
                "Aplicar Design Thinking na resolução de problemas",
                "Usar materiais recicláveis de forma criativa e funcional",
                "Documentar o processo de criação como reflexão sobre o aprendizado"
            ],
            "integracao_interdisciplinar": {
                "descricao": "A Cultura Maker integra saberes através da construção prática.",
                "disciplinas": [
                    f"Ciências: princípios científicos aplicados na construção sobre {tema}",
                    "Matemática: medidas, proporções e geometria para construção",
                    "Artes: design, estética e criatividade nos protótipos",
                    "Tecnologia: pensamento computacional e lógica de funcionamento",
                    "Educação Ambiental: reuso e reciclagem de materiais"
                ]
            },
            "passo_a_passo": [
                {"aula": 1, "titulo": "Inspiração e Design Thinking", "duracao": tempo, "atividades": ["Provocação: desafio maker ligado ao tema", "Galeria de inspiração maker", "Ciclo de Design Thinking: Empatizar → Definir → Idear", "Brainstorming e esboço do protótipo"], "recursos": ["Cartões de desafio", "Exemplos maker", "Papel e post-its"]},
                {"aula": 2, "titulo": "Prototipagem v1.0", "duracao": tempo, "atividades": ["Planejamento: lista de materiais e etapas", "Construção do protótipo v1.0", "Teste inicial e feedback entre equipes", "Registro fotográfico do processo"], "recursos": ["Materiais recicláveis", "Cola quente, tesoura, fita", "Ferramentas básicas"]},
                {"aula": 3, "titulo": "Iteração v2.0", "duracao": tempo, "atividades": ["Análise do que funcionou/falhou", "Melhorias no design e funcionalidade", "Construção v2.0 aperfeiçoada", "Documentação técnica do projeto"], "recursos": ["Materiais adicionais", "Ficha de iteração", "Checklist de qualidade"]},
                {"aula": 4, "titulo": "Maker Faire — Mostra de Invenções", "duracao": tempo, "atividades": ["Montagem da exposição", "Demonstração ao vivo dos inventos", "Pitch de 3 min por equipe", "Votação e reflexão final"], "recursos": ["Espaço para exposição", "Fichas de votação", "Certificados"]}
            ],
            "atividades_praticas": [
                "Máquina de Rube Goldberg com materiais recicláveis",
                "Instrumentos de medição caseiros",
                "Protótipo para problema real da escola",
                "Circuitos simples com LED e bateria",
                "Jogos de tabuleiro 3D sobre o tema"
            ],
            "estrategias_engajamento": [
                "Liberdade criativa na abordagem do desafio",
                "Celebração do erro: 'Falhou bonito!'",
                "Kit misterioso de materiais surpresa",
                "Competição por categorias (criativo, funcional, bonito)",
                "Histórias de makers e inventores famosos"
            ],
            "avaliacao": {
                "formativa": ["Observação do processo de construção", "Registro fotográfico (portfólio)", "Ficha de iteração v1→v2", "Autoavaliação maker"],
                "somativa": ["Protótipo final: funcionalidade e criatividade", "Pitch do inventor", "Documentação técnica", "Reflexão sobre aprendizagem"]
            },
            "desenvolvimento_socioemocional": [
                "Resiliência e tolerância ao erro",
                "Criatividade sob restrição de recursos",
                "Orgulho do trabalho manual",
                "Colaboração prática em equipe",
                "Consciência sustentável"
            ],
            "adaptacao_hibrido": [
                "Desafios maker caseiros com materiais de casa",
                "Tutoriais em vídeo para técnicas de construção",
                "Galeria virtual de projetos",
                "Videoconferência para feedback entre equipes",
                "Canal para troca de dicas e materiais"
            ],
            "uso_tecnologia": [
                "Tinkercad para modelagem 3D",
                "Scratch/Arduino para projetos digitais",
                "Time-lapse do processo de construção",
                "Pinterest para inspiração maker",
                "Google Sites para portfólio digital"
            ],
            "produto_final": f"INVENÇÃO MAKER sobre '{tema}': protótipo funcional com materiais acessíveis, documentação técnica, vídeo time-lapse do processo e pitch apresentado na Maker Faire escolar."
        }

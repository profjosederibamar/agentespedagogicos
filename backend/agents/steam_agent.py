"""Agente: STEAM (Ciência, Tecnologia, Engenharia, Arte e Matemática)"""
from .base_agent import BaseAgent


class STEAMAgent(BaseAgent):
    def get_name(self) -> str:
        return "STEAM (Arte + Ciência)"

    def get_description(self) -> str:
        return "Integra Ciência, Tecnologia, Engenharia, Arte e Matemática em experiências criativas e experimentais."

    def get_system_prompt(self) -> str:
        return """Você é um agente pedagógico especialista em STEAM (Science, Technology, Engineering, Arts, Mathematics).

Seu papel é criar sequências didáticas que:
- INTEGREM genuinamente Ciência, Tecnologia, Engenharia, Arte e Matemática
- Valorizem a CRIATIVIDADE e a EXPRESSÃO ARTÍSTICA como formas de compreensão
- Proponham EXPERIMENTOS e CRIAÇÕES que conectem arte e ciência
- Estimulem o pensamento inventivo e a inovação
- Incluam atividades mão-na-massa (hands-on) com materiais acessíveis
- Resultem em produções que sejam ao mesmo tempo belas e funcionais

FOCO ESPECÍFICO: A ARTE deve ser protagonista junto com a ciência, não apenas decoração."""

    def get_template(self, tema: str, faixa_etaria: str, tempo: str, objetivos: str) -> dict:
        return {
            "titulo": f"Laboratório STEAM: Arte e Ciência em '{tema}' — Criar, Experimentar, Expressar",
            "problema_central": f"Como podemos usar a fusão entre arte e ciência para explorar '{tema}' de forma inovadora? Os alunos serão artistas-cientistas, criando obras e experimentos que revelem a beleza escondida nos conceitos e fenômenos relacionados ao tema.",
            "objetivos_aprendizagem": [
                f"Investigar os princípios científicos por trás de '{tema}' através de experimentação",
                "Expressar conceitos científicos através da linguagem artística",
                "Aplicar raciocínio matemático na criação de projetos criativos",
                "Utilizar pensamento de design e engenharia para resolver desafios",
                "Integrar tecnologia como ferramenta de criação e expressão"
            ],
            "integracao_interdisciplinar": {
                "descricao": "STEAM integra naturalmente todas as áreas do conhecimento em uma experiência holística.",
                "disciplinas": [
                    f"Ciências: experimentação e investigação dos fenômenos ligados a {tema}",
                    "Matemática: padrões, proporções, geometria e dados nas criações",
                    "Artes: expressão visual, musical ou corporal dos conceitos aprendidos",
                    "Tecnologia: ferramentas digitais para criação e documentação",
                    "Engenharia: design thinking e construção de protótipos funcionais"
                ]
            },
            "passo_a_passo": [
                {
                    "aula": 1,
                    "titulo": "Inspiração — Onde a Arte Encontra a Ciência",
                    "duracao": tempo,
                    "atividades": [
                        f"Galeria de inspiração: exemplos surpreendentes da conexão entre arte e '{tema}'",
                        "Experimento demonstrativo que revela a beleza do fenômeno científico",
                        "Exercício criativo 'Desenhe o que você imagina': representação artística livre do tema",
                        "Discussão coletiva: 'Onde vocês veem arte na ciência e ciência na arte?'"
                    ],
                    "recursos": ["Imagens inspiradoras", "Material para experimento demonstrativo", "Papel e materiais de desenho", "Projetor"]
                },
                {
                    "aula": 2,
                    "titulo": "Exploração — Laboratório de Experimentação Criativa",
                    "duracao": tempo,
                    "atividades": [
                        "Estações rotativas de experimentação (3-4 estações diferentes)",
                        "Cada estação conecta um conceito científico a uma técnica artística",
                        "Registro em caderno STEAM: observações científicas + esboços artísticos",
                        "Escolha do projeto final: qual experimento/criação cada equipe quer aprofundar?"
                    ],
                    "recursos": ["Materiais por estação", "Caderno STEAM", "Timer para rotação", "Checklist de experimentação"]
                },
                {
                    "aula": 3,
                    "titulo": "Criação — Artistas-Cientistas em Ação",
                    "duracao": tempo,
                    "atividades": [
                        "Desenvolvimento do projeto STEAM: criação artística + base científica",
                        "Aplicação de conceitos de design e engenharia na construção",
                        "Uso de matemática na proporção, escala e precisão das criações",
                        "Documentação: fotos e vídeos do processo + explicação científica"
                    ],
                    "recursos": ["Materiais diversos de arte e construção", "Ferramentas de medição", "Câmera/celular", "Materiais recicláveis"]
                },
                {
                    "aula": 4,
                    "titulo": "Exposição STEAM — Mostra de Arte e Ciência",
                    "duracao": tempo,
                    "atividades": [
                        "Montagem da exposição STEAM com obras e experimentos",
                        "Cada equipe apresenta sua criação, explicando a ciência por trás da arte",
                        "Interatividade: visitantes podem experimentar e interagir com as obras",
                        "Reflexão: 'Como essa experiência mudou minha forma de ver Arte e Ciência?'",
                        "Votação popular e celebração da criatividade"
                    ],
                    "recursos": ["Espaço para exposição", "Mesas e painéis", "Etiquetas explicativas", "Cédulas de votação"]
                }
            ],
            "atividades_praticas": [
                "Experimento artístico: cromatografia com flores e filtros de café (arte + química)",
                "Construção de instrumentos musicais com materiais recicláveis (música + física + engenharia)",
                "Criação de fractais e padrões geométricos na natureza (arte + matemática)",
                "Stop-motion explicativo: animação que ensina um conceito científico (arte + tecnologia)",
                "Bioarte: criação artística usando processos biológicos (arte + biologia)"
            ],
            "estrategias_engajamento": [
                "Estações rotativas que permitem experimentação livre e descoberta",
                "Conexão com artistas-cientistas famosos (Leonardo da Vinci, Ada Lovelace)",
                "Materiais sensoriais e experiências multissensoriais",
                "Liberdade criativa com suporte estruturado (escolhas dentro de parâmetros)",
                "Exposição final aberta à comunidade gerando orgulho e reconhecimento"
            ],
            "avaliacao": {
                "formativa": [
                    "Caderno STEAM: observações científicas integradas com esboços artísticos",
                    "Observação do processo criativo e experimentação",
                    "Feedback entre pares durante as estações rotativas",
                    "Autoavaliação do engajamento com ambos os lados (arte e ciência)"
                ],
                "somativa": [
                    "Obra/projeto STEAM final com componentes artísticos e científicos",
                    "Apresentação explicativa: 'A ciência por trás da minha arte'",
                    "Documentação visual do processo (portfólio fotográfico/vídeo)",
                    "Reflexão escrita sobre as conexões descobertas entre arte e ciência"
                ]
            },
            "desenvolvimento_socioemocional": [
                "Criatividade e expressão: liberdade para criar sem medo de errar",
                "Apreciação estética: sensibilidade para reconhecer beleza no mundo",
                "Curiosidade científica: maravilhamento diante dos fenômenos naturais",
                "Colaboração criativa: combinar diferentes talentos em um projeto único",
                "Autoconfiança: orgulho pelo que criou e capacidade de explicar"
            ],
            "adaptacao_hibrido": [
                "Experimentos caseiros com materiais simples como atividade assíncrona",
                "Galeria virtual de inspiração compartilhada em Padlet ou Google Slides",
                "Tutoriais em vídeo para técnicas artísticas e experimentos",
                "Exposição virtual: fotos e vídeos das criações em site ou rede social",
                "Desafios STEAM semanais para fazer em casa e compartilhar online"
            ],
            "uso_tecnologia": [
                "Tinkercad para modelagem 3D e design de protótipos",
                "Canva/Figma para design gráfico e composição visual",
                "Arduino/Micro:bit para projetos de arte interativa (se disponível)",
                "Aplicativos de câmera com filtros para documentação artística",
                "Scratch para criação de animações e arte digital interativa"
            ],
            "produto_final": f"Uma EXPOSIÇÃO STEAM sobre '{tema}' onde cada equipe apresenta uma criação que integra arte e ciência, incluindo: (1) uma obra artística-científica (escultura, instalação, performance ou arte digital), (2) um painel explicativo com a fundamentação científica e matemática, (3) um momento interativo onde visitantes experimentam o conceito, e (4) documentação visual em portfólio digital."
        }

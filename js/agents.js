/**
 * agents.js — Definições das 9 práticas pedagógicas
 * Metadados para renderização dos cards e identificação dos agentes.
 */

const PRACTICES = [
    {
        key: "abp",
        name: "Aprendizagem Baseada em Projetos",
        shortName: "ABP",
        icon: "assets/robots/robot_abp.png",
        description: "Projetos reais onde os alunos investigam, criam e apresentam soluções concretas para problemas autênticos.",
        gradient: "linear-gradient(135deg, #3b82f6, #1d4ed8)",
        color: "#3b82f6"
    },
    {
        key: "pbl",
        name: "Aprendizagem Baseada em Problemas",
        shortName: "PBL",
        icon: "assets/robots/robot_pbl.png",
        description: "Resolução de problemas complexos e autênticos que desenvolvem raciocínio crítico e habilidades investigativas.",
        gradient: "linear-gradient(135deg, #f43f5e, #be123c)",
        color: "#f43f5e"
    },
    {
        key: "steam",
        name: "STEAM (Arte + Ciência)",
        shortName: "STEAM",
        icon: "assets/robots/robot_steam.png",
        description: "Integração de Ciência, Tecnologia, Engenharia, Arte e Matemática em experiências criativas.",
        gradient: "linear-gradient(135deg, #8b5cf6, #6d28d9)",
        color: "#8b5cf6"
    },
    {
        key: "gamificacao",
        name: "Gamificação",
        shortName: "Gamificação",
        icon: "assets/robots/robot_gamificacao.png",
        description: "Aprendizado como jogo com missões, pontos, conquistas, rankings e narrativa envolvente.",
        gradient: "linear-gradient(135deg, #f59e0b, #d97706)",
        color: "#f59e0b"
    },
    {
        key: "maker",
        name: "Cultura Maker",
        shortName: "Maker",
        icon: "assets/robots/robot_maker.png",
        description: "Aprender fazendo! Construção de projetos com materiais acessíveis e muita inventividade.",
        gradient: "linear-gradient(135deg, #10b981, #059669)",
        color: "#10b981"
    },
    {
        key: "hibrido",
        name: "Ensino Híbrido",
        shortName: "Híbrido",
        icon: "assets/robots/robot_hibrido.png",
        description: "Combinação inteligente de atividades presencias e online, integradas e complementares.",
        gradient: "linear-gradient(135deg, #0ea5e9, #0284c7)",
        color: "#0ea5e9"
    },
    {
        key: "invertida",
        name: "Sala de Aula Invertida",
        shortName: "Invertida",
        icon: "assets/robots/robot_invertida.png",
        description: "Estudo prévio em casa e atividades práticas de aprofundamento em sala de aula.",
        gradient: "linear-gradient(135deg, #f97316, #ea580c)",
        color: "#f97316"
    },
    {
        key: "colaborativa",
        name: "Aprendizagem Colaborativa",
        shortName: "Colaborativa",
        icon: "assets/robots/robot_colaborativa.png",
        description: "Construção coletiva do conhecimento através de interação estruturada e cooperação.",
        gradient: "linear-gradient(135deg, #6366f1, #4338ca)",
        color: "#6366f1"
    },
    {
        key: "socioemocional",
        name: "Educação Socioemocional",
        shortName: "Socioemocional",
        icon: "assets/robots/robot_socioemocional.png",
        description: "Integração intencional de competências socioemocionais ao conteúdo acadêmico.",
        gradient: "linear-gradient(135deg, #ec4899, #db2777)",
        color: "#ec4899"
    }
];

/**
 * Retorna a prática pelo key
 */
function getPracticeByKey(key) {
    return PRACTICES.find(p => p.key === key) || null;
}

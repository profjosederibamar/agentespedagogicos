/**
 * history.js — Gerenciamento de histórico de sequências no localStorage
 */

const HISTORY_KEY = "agentes_pedagogicos_historico";

/**
 * Salva uma sequência no histórico.
 */
function saveToHistory(entry) {
    const history = getHistory();
    const item = {
        id: Date.now().toString(),
        createdAt: new Date().toISOString(),
        practice: entry.practice,
        practiceKey: entry.practiceKey,
        tema: entry.tema,
        faixaEtaria: entry.faixaEtaria,
        tempo: entry.tempo,
        source: entry.source,
        sequence: entry.sequence,
    };
    history.unshift(item);
    // Limita a 50 itens
    if (history.length > 50) history.pop();
    localStorage.setItem(HISTORY_KEY, JSON.stringify(history));
    return item;
}

/**
 * Retorna o histórico completo.
 */
function getHistory() {
    try {
        return JSON.parse(localStorage.getItem(HISTORY_KEY) || "[]");
    } catch {
        return [];
    }
}

/**
 * Retorna um item do histórico pelo ID.
 */
function getHistoryItem(id) {
    return getHistory().find(item => item.id === id) || null;
}

/**
 * Remove um item do histórico pelo ID.
 */
function removeFromHistory(id) {
    const history = getHistory().filter(item => item.id !== id);
    localStorage.setItem(HISTORY_KEY, JSON.stringify(history));
}

/**
 * Limpa todo o histórico.
 */
function clearHistory() {
    localStorage.removeItem(HISTORY_KEY);
}

/**
 * Formata data para exibição.
 */
function formatDate(isoString) {
    const d = new Date(isoString);
    return d.toLocaleDateString("pt-BR", {
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
    });
}

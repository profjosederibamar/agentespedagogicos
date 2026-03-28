/**
 * api.js — Comunicação com o backend FastAPI
 */

const API_CONFIG = {
    // Altere para a URL do seu backend em produção
    // Ex: "https://seu-backend.onrender.com"
    baseUrl: "http://localhost:8000",
};

/**
 * Envia dados para gerar sequência didática.
 * @param {Object} data - { practice, tema, faixa_etaria, tempo, objetivos }
 * @returns {Promise<Object>} Resposta do backend
 */
async function generateSequence(data) {
    const url = `${API_CONFIG.baseUrl}/api/generate`;

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            const err = await response.json().catch(() => ({}));
            throw new Error(err.detail || `Erro ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        if (error.message.includes("Failed to fetch") || error.message.includes("NetworkError")) {
            throw new Error(
                "Não foi possível conectar ao servidor. Verifique se o backend está rodando."
            );
        }
        throw error;
    }
}

/**
 * Verifica se o backend está acessível.
 * @returns {Promise<boolean>}
 */
async function checkBackendHealth() {
    try {
        const response = await fetch(`${API_CONFIG.baseUrl}/api/health`, {
            method: "GET",
            signal: AbortSignal.timeout(5000),
        });
        return response.ok;
    } catch {
        return false;
    }
}

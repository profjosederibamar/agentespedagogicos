/**
 * app.js — Lógica principal da aplicação SPA
 * Gerencia navegação, renderização e interações.
 */

// ─── Estado Global ──────────────────────────────────────────
let currentSection = "hero-section";
let selectedPractice = null;
let currentResult = null;
let isEditing = false;

// ─── Inicialização ──────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
    initNavigation();
    renderPracticesGrid();
    initFormHandler();
    initResultActions();
    initHistoryActions();
});

// ─── Navegação entre Seções ─────────────────────────────────
function showSection(sectionId) {
    document.querySelectorAll(".section").forEach(s => s.classList.remove("active"));
    const target = document.getElementById(sectionId);
    if (target) {
        target.classList.add("active");
        currentSection = sectionId;
        updateNavbarActive(sectionId);
        window.scrollTo({ top: 0, behavior: "smooth" });
    }
}

function updateNavbarActive(sectionId) {
    document.querySelectorAll(".nav-link").forEach(link => link.classList.remove("active"));
    
    if (sectionId === "hero-section") {
        document.getElementById("nav-home").classList.add("active");
    } else if (sectionId === "practices-section" || sectionId === "form-section" || sectionId === "loading-section") {
        document.getElementById("nav-practices").classList.add("active");
    } else if (sectionId === "history-section") {
        document.getElementById("nav-history").classList.add("active");
    }
}

function initNavigation() {
    // Navbar Logo
    document.getElementById("nav-logo").addEventListener("click", () => showSection("hero-section"));

    // Navbar Links
    document.getElementById("nav-home").addEventListener("click", () => showSection("hero-section"));
    document.getElementById("nav-practices").addEventListener("click", () => showSection("practices-section"));
    document.getElementById("nav-history").addEventListener("click", () => {
        renderHistoryList();
        showSection("history-section");
    });

    // Hero → Práticas
    document.getElementById("btn-start").addEventListener("click", () => {
        showSection("practices-section");
    });

    // Hero → Histórico
    document.getElementById("btn-history").addEventListener("click", () => {
        renderHistoryList();
        showSection("history-section");
    });

    // Botões voltar
    document.getElementById("btn-back-practices").addEventListener("click", () => {
        showSection("hero-section");
    });

    document.getElementById("btn-back-form").addEventListener("click", () => {
        showSection("practices-section");
    });

    document.getElementById("btn-back-result").addEventListener("click", () => {
        selectedPractice = null;
        currentResult = null;
        isEditing = false;
        showSection("hero-section");
    });

    document.getElementById("btn-back-history").addEventListener("click", () => {
        showSection("hero-section");
    });
}

// ─── Renderizar Grid de Práticas ────────────────────────────
function renderPracticesGrid() {
    const grid = document.getElementById("practices-grid");
    if (!grid) return;
    
    grid.innerHTML = PRACTICES.map((p, i) => `
        <div class="practice-card animate-in" 
             data-key="${p.key}" 
             style="--card-gradient: ${p.gradient}; animation-delay: ${i * 60}ms"
             id="practice-card-${p.key}">
            <img src="${p.icon}" alt="${p.name}" class="practice-card-icon">
            <h3 class="practice-card-title">${p.name}</h3>
            <p class="practice-card-desc">${p.description}</p>
        </div>
    `).join("");

    // Event listeners
    grid.querySelectorAll(".practice-card").forEach(card => {
        card.addEventListener("click", () => {
            const key = card.dataset.key;
            selectedPractice = getPracticeByKey(key);
            if (selectedPractice) {
                showFormSection();
            }
        });
    });
}

// ─── Formulário ─────────────────────────────────────────────
function showFormSection() {
    const badge = document.getElementById("selected-practice-badge");
    badge.innerHTML = `<img src="${selectedPractice.icon}" style="width:24px;height:24px;margin-right:8px;vertical-align:middle;"> ${selectedPractice.name}`;
    showSection("form-section");
}

function initFormHandler() {
    const form = document.getElementById("sequence-form");
    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        await handleGenerate();
    });
}

async function handleGenerate() {
    const tema = document.getElementById("tema").value.trim();
    const faixaEtaria = document.getElementById("faixa-etaria").value;
    const tempo = document.getElementById("tempo").value;
    const modelo = document.getElementById("modelo").value;
    const objetivos = document.getElementById("objetivos").value.trim();

    if (!tema || !faixaEtaria || !tempo) {
        showToast("Preencha todos os campos obrigatórios.", "error");
        return;
    }

    // Mostrar loading
    showSection("loading-section");
    animateLoading();

    const data = {
        practice: selectedPractice.key,
        tema: tema,
        faixa_etaria: faixaEtaria,
        tempo: tempo,
        objetivos: objetivos,
        modelo: modelo,
    };

    try {
        const response = await generateSequence(data);

        if (response.success) {
            currentResult = {
                practice: response.practice,
                practiceKey: selectedPractice.key,
                source: response.source,
                provider: response.provider || "",
                providerLabel: response.provider_label || "",
                sequence: response.sequence,
                tema: tema,
                faixaEtaria: faixaEtaria,
                tempo: tempo,
            };

            // Salvar no histórico
            saveToHistory(currentResult);

            // Renderizar resultado
            renderResult(currentResult);
            showSection("result-section");
            showToast("Sequência didática gerada com sucesso! ✨", "success");
        } else {
            throw new Error("Resposta inesperada do servidor");
        }
    } catch (error) {
        console.error("Erro ao gerar:", error);
        showSection("form-section");
        showToast(`Erro: ${error.message}`, "error");
    }
}

// ─── Loading Animation ─────────────────────────────────────
function animateLoading() {
    const messages = [
        "Analisando a prática pedagógica...",
        "Construindo objetivos de aprendizagem...",
        "Elaborando atividades criativas...",
        "Planejando aula a aula...",
        "Integrando disciplinas...",
        "Definindo estratégias de engajamento...",
        "Criando avaliações...",
        "Finalizando sua sequência didática...",
    ];

    const msgEl = document.getElementById("loading-message");
    const barEl = document.getElementById("loading-bar-fill");
    let step = 0;

    const interval = setInterval(() => {
        if (currentSection !== "loading-section" || step >= messages.length) {
            clearInterval(interval);
            return;
        }
        msgEl.textContent = messages[step];
        barEl.style.width = `${((step + 1) / messages.length) * 100}%`;
        step++;
    }, 1500);
}

// ─── Renderizar Resultado ───────────────────────────────────
function renderResult(data) {
    const container = document.getElementById("result-content");
    const s = data.sequence;
    const practice = getPracticeByKey(data.practiceKey);

    let html = "";

    // Título principal
    html += `
        <div class="result-title-card" style="background: ${practice ? practice.gradient : 'var(--gradient-primary)'}">
            <h1 class="result-main-title">${escapeHtml(s.titulo || 'Sequência Didática')}</h1>
            <p class="result-practice-label">
                <img src="${practice ? practice.icon : ''}" style="width:32px;height:32px;vertical-align:middle;margin-right:8px;"> 
                ${escapeHtml(data.practice)}
            </p>
            <span class="result-source-badge ${data.source}">
                ${data.source === 'ai' 
                    ? (data.providerLabel || '🤖 Gerado por IA')
                    : '📋 Gerado por Template Inteligente'}
            </span>
        </div>
    `;

    // Blocos de conteúdo
    const blocks = [
        { icon: "🎯", title: "Problema Central", key: "problema_central", type: "text" },
        { icon: "📋", title: "Objetivos de Aprendizagem", key: "objetivos_aprendizagem", type: "list" },
        { icon: "🔗", title: "Integração Interdisciplinar", key: "integracao_interdisciplinar", type: "interdisciplinar" },
        { icon: "📝", title: "Passo a Passo (Aula a Aula)", key: "passo_a_passo", type: "passos" },
        { icon: "🛠️", title: "Atividades Práticas", key: "atividades_praticas", type: "list" },
        { icon: "🚀", title: "Estratégias de Engajamento", key: "estrategias_engajamento", type: "list" },
        { icon: "📊", title: "Avaliação", key: "avaliacao", type: "avaliacao" },
        { icon: "❤️", title: "Desenvolvimento Socioemocional", key: "desenvolvimento_socioemocional", type: "list" },
        { icon: "💻", title: "Adaptação para Ensino Híbrido", key: "adaptacao_hibrido", type: "list" },
        { icon: "📱", title: "Uso de Tecnologia", key: "uso_tecnologia", type: "list" },
        { icon: "🏆", title: "Produto Final Esperado", key: "produto_final", type: "text" },
    ];

    blocks.forEach((block, idx) => {
        const value = s[block.key];
        if (!value) return;

        html += `<div class="result-block animate-in" style="animation-delay: ${idx * 80}ms">`;
        html += `<div class="result-block-header">`;
        html += `<span class="result-block-number">${idx + 1}</span>`;
        html += `<span class="result-block-icon">${block.icon}</span>`;
        html += `<h3 class="result-block-title">${block.title}</h3>`;
        html += `</div>`;

        switch (block.type) {
            case "text":
                html += `<p class="result-text" data-editable="${block.key}">${escapeHtml(value)}</p>`;
                break;

            case "list":
                if (Array.isArray(value)) {
                    html += `<ul class="result-list">`;
                    value.forEach(item => {
                        html += `<li data-editable="${block.key}">${escapeHtml(item)}</li>`;
                    });
                    html += `</ul>`;
                }
                break;

            case "interdisciplinar":
                if (value.descricao) {
                    html += `<p class="result-text" style="margin-bottom: var(--space-md)">${escapeHtml(value.descricao)}</p>`;
                }
                if (value.disciplinas && Array.isArray(value.disciplinas)) {
                    html += `<div style="display:flex; flex-wrap:wrap; gap:4px;">`;
                    value.disciplinas.forEach(d => {
                        html += `<span class="disciplina-tag">${escapeHtml(d)}</span>`;
                    });
                    html += `</div>`;
                }
                break;

            case "passos":
                if (Array.isArray(value)) {
                    value.forEach(aula => {
                        html += `<div class="aula-step">`;
                        html += `<div class="aula-step-header">`;
                        html += `<span class="aula-step-title">Aula ${aula.aula}: ${escapeHtml(aula.titulo)}</span>`;
                        html += `<span class="aula-step-duration">⏱️ ${escapeHtml(aula.duracao)}</span>`;
                        html += `</div>`;

                        if (aula.atividades && aula.atividades.length) {
                            html += `<h4>Atividades</h4>`;
                            html += `<ul class="result-list">`;
                            aula.atividades.forEach(a => {
                                html += `<li>${escapeHtml(a)}</li>`;
                            });
                            html += `</ul>`;
                        }

                        if (aula.recursos && aula.recursos.length) {
                            html += `<h4>Recursos</h4>`;
                            html += `<ul class="result-list">`;
                            aula.recursos.forEach(r => {
                                html += `<li>${escapeHtml(r)}</li>`;
                            });
                            html += `</ul>`;
                        }

                        html += `</div>`;
                    });
                }
                break;

            case "avaliacao":
                html += `<div class="avaliacao-grid">`;
                if (value.formativa && value.formativa.length) {
                    html += `<div class="avaliacao-col">`;
                    html += `<h4>📝 Formativa</h4>`;
                    html += `<ul class="result-list">`;
                    value.formativa.forEach(f => {
                        html += `<li>${escapeHtml(f)}</li>`;
                    });
                    html += `</ul></div>`;
                }
                if (value.somativa && value.somativa.length) {
                    html += `<div class="avaliacao-col">`;
                    html += `<h4>📊 Somativa</h4>`;
                    html += `<ul class="result-list">`;
                    value.somativa.forEach(s => {
                        html += `<li>${escapeHtml(s)}</li>`;
                    });
                    html += `</ul></div>`;
                }
                html += `</div>`;
                break;
        }

        html += `</div>`;
    });

    container.innerHTML = html;
}

// ─── Ações do Resultado ─────────────────────────────────────
function initResultActions() {
    // Download PDF
    document.getElementById("btn-download-pdf").addEventListener("click", () => {
        if (currentResult) {
            try {
                downloadPDF(currentResult.sequence, currentResult.practice);
                showToast("PDF baixado com sucesso! 📄", "success");
            } catch (e) {
                console.error("Erro ao gerar PDF:", e);
                showToast("Erro ao gerar PDF. Tente novamente.", "error");
            }
        }
    });

    // Toggle edição COMPLETA
    document.getElementById("btn-edit-toggle").addEventListener("click", () => {
        isEditing = !isEditing;
        const resultContent = document.getElementById("result-content");

        // Seleciona TODOS os elementos de texto editáveis
        const allEditables = resultContent.querySelectorAll(
            ".result-main-title, .result-text, .result-list li, " +
            ".disciplina-tag, .aula-step-title, .aula-step h4, " +
            ".avaliacao-col h4, .result-block-title, .result-practice-label"
        );

        allEditables.forEach(el => {
            el.contentEditable = isEditing ? "true" : "false";
        });

        // Adiciona/remove classe visual de edição no container
        resultContent.classList.toggle("editing-mode", isEditing);

        // Mostra/esconde banner de edição
        let banner = document.getElementById("editing-banner");
        if (isEditing) {
            if (!banner) {
                banner = document.createElement("div");
                banner.id = "editing-banner";
                banner.className = "editing-banner";
                banner.innerHTML = `
                    <span>✏️ <strong>Modo de Edição Ativo</strong> — Clique em qualquer texto para editar.</span>
                    <button class="btn btn-primary" id="btn-save-edit" style="padding: 0.5rem 1rem; font-size: 0.85rem;">
                        <span>✅</span> Salvar Alterações
                    </button>
                `;
                resultContent.parentElement.insertBefore(banner, resultContent);
                document.getElementById("btn-save-edit").addEventListener("click", () => {
                    document.getElementById("btn-edit-toggle").click();
                });
            }
            banner.style.display = "flex";
        } else {
            if (banner) banner.style.display = "none";
        }

        const btn = document.getElementById("btn-edit-toggle");
        btn.innerHTML = isEditing
            ? "<span>✅</span> Salvar"
            : "<span>✏️</span> Editar";
        btn.className = isEditing
            ? "btn btn-primary"
            : "btn btn-outline";

        showToast(
            isEditing
                ? "✏️ Modo de edição ativado! Clique em QUALQUER texto para editar."
                : "✅ Alterações salvas com sucesso!",
            isEditing ? "info" : "success"
        );
    });

    // Botão Regenerar (gerar novamente)
    document.getElementById("btn-regenerate")?.addEventListener("click", async () => {
        if (selectedPractice && currentResult) {
            showSection("loading-section");
            animateLoading();
            const data = {
                practice: selectedPractice.key,
                tema: currentResult.tema,
                faixa_etaria: currentResult.faixaEtaria,
                tempo: currentResult.tempo,
                objetivos: "",
            };
            try {
                const response = await generateSequence(data);
                if (response.success) {
                    currentResult = {
                        practice: response.practice,
                        practiceKey: selectedPractice.key,
                        source: response.source,
                        sequence: response.sequence,
                        tema: currentResult.tema,
                        faixaEtaria: currentResult.faixaEtaria,
                        tempo: currentResult.tempo,
                    };
                    saveToHistory(currentResult);
                    renderResult(currentResult);
                    showSection("result-section");
                    showToast("Nova sequência gerada! 🔄", "success");
                }
            } catch (error) {
                showSection("result-section");
                showToast(`Erro ao regenerar: ${error.message}`, "error");
            }
        }
    });
}

// ─── Histórico ──────────────────────────────────────────────
function initHistoryActions() {
    document.getElementById("btn-history-create")?.addEventListener("click", () => {
        showSection("practices-section");
    });
}

function renderHistoryList() {
    const history = getHistory();
    const listEl = document.getElementById("history-list");
    const emptyEl = document.getElementById("history-empty");

    if (history.length === 0) {
        listEl.style.display = "none";
        emptyEl.style.display = "block";
        return;
    }

    listEl.style.display = "flex";
    emptyEl.style.display = "none";

    listEl.innerHTML = history.map((item, i) => {
        const practice = getPracticeByKey(item.practiceKey);
        return `
            <div class="history-item animate-in" style="animation-delay: ${i * 50}ms" data-id="${item.id}">
                <div class="history-item-info">
                    <div class="history-item-title">
                        <img src="${practice ? practice.icon : ''}" style="width:20px;height:20px;vertical-align:middle;margin-right:8px;opacity:0.8;"> 
                        ${escapeHtml(item.sequence?.titulo || item.tema || 'Sequência')}
                    </div>
                    <div class="history-item-meta">
                        <span>📅 ${formatDate(item.createdAt)}</span>
                        <span>🎯 ${escapeHtml(item.practice || '')}</span>
                        <span>👥 ${escapeHtml(item.faixaEtaria || '')}</span>
                    </div>
                </div>
                <div class="history-item-actions">
                    <button class="btn btn-secondary btn-view-history" data-id="${item.id}">
                        <span>👁️</span> Ver
                    </button>
                    <button class="btn btn-danger btn-delete-history" data-id="${item.id}">
                        <span>🗑️</span>
                    </button>
                </div>
            </div>
        `;
    }).join("");

    // Event listeners
    listEl.querySelectorAll(".btn-view-history").forEach(btn => {
        btn.addEventListener("click", (e) => {
            e.stopPropagation();
            const id = btn.dataset.id;
            const item = getHistoryItem(id);
            if (item) {
                currentResult = {
                    practice: item.practice,
                    practiceKey: item.practiceKey,
                    source: item.source,
                    sequence: item.sequence,
                    tema: item.tema,
                    faixaEtaria: item.faixaEtaria,
                    tempo: item.tempo,
                };
                selectedPractice = getPracticeByKey(item.practiceKey);
                renderResult(currentResult);
                showSection("result-section");
            }
        });
    });

    listEl.querySelectorAll(".btn-delete-history").forEach(btn => {
        btn.addEventListener("click", (e) => {
            e.stopPropagation();
            const id = btn.dataset.id;
            removeFromHistory(id);
            renderHistoryList();
            showToast("Sequência removida do histórico.", "info");
        });
    });
}

// ─── Toast Notifications ────────────────────────────────────
function showToast(message, type = "info") {
    const container = document.getElementById("toast-container");
    const toast = document.createElement("div");
    toast.className = `toast ${type}`;
    toast.textContent = message;
    container.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = "0";
        toast.style.transform = "translateX(100px)";
        toast.style.transition = "all 0.3s ease";
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}

// ─── Utilitários ────────────────────────────────────────────
function escapeHtml(text) {
    if (!text) return "";
    const div = document.createElement("div");
    div.textContent = String(text);
    return div.innerHTML;
}

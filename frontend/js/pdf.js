/**
 * pdf.js — Geração de PDF formatado com jsPDF
 */

/**
 * Gera e baixa um PDF da sequência didática.
 * @param {Object} sequence - Dados da sequência
 * @param {string} practiceName - Nome da prática pedagógica
 */
function downloadPDF(sequence, practiceName) {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF({ unit: "mm", format: "a4" });

    const pageWidth = doc.internal.pageSize.getWidth();
    const margin = 20;
    const maxWidth = pageWidth - margin * 2;
    let y = 20;

    // Cores
    const primaryColor = [102, 126, 234]; // #667eea
    const textColor = [40, 40, 60];
    const mutedColor = [120, 120, 150];

    function checkPage(needed = 20) {
        if (y + needed > 270) {
            doc.addPage();
            y = 20;
        }
    }

    function addTitle(text, size = 16) {
        checkPage(20);
        doc.setFont("helvetica", "bold");
        doc.setFontSize(size);
        doc.setTextColor(...primaryColor);
        const lines = doc.splitTextToSize(text, maxWidth);
        doc.text(lines, margin, y);
        y += lines.length * (size * 0.45) + 4;
    }

    function addSubtitle(text) {
        checkPage(15);
        doc.setFont("helvetica", "bold");
        doc.setFontSize(11);
        doc.setTextColor(...primaryColor);
        doc.text(text, margin, y);
        y += 7;
    }

    function addText(text) {
        checkPage(10);
        doc.setFont("helvetica", "normal");
        doc.setFontSize(10);
        doc.setTextColor(...textColor);
        const lines = doc.splitTextToSize(text, maxWidth);
        lines.forEach(line => {
            checkPage(6);
            doc.text(line, margin, y);
            y += 5;
        });
        y += 3;
    }

    function addList(items) {
        items.forEach(item => {
            checkPage(8);
            doc.setFont("helvetica", "normal");
            doc.setFontSize(9.5);
            doc.setTextColor(...textColor);
            const lines = doc.splitTextToSize(`• ${item}`, maxWidth - 5);
            lines.forEach((line, i) => {
                checkPage(5);
                doc.text(line, margin + (i === 0 ? 0 : 3), y);
                y += 4.5;
            });
        });
        y += 3;
    }

    function addSeparator() {
        checkPage(8);
        doc.setDrawColor(200, 200, 220);
        doc.line(margin, y, pageWidth - margin, y);
        y += 6;
    }

    // ─── HEADER ────────────────────────────────────────
    doc.setFillColor(...primaryColor);
    doc.rect(0, 0, pageWidth, 35, "F");

    doc.setFont("helvetica", "bold");
    doc.setFontSize(18);
    doc.setTextColor(255, 255, 255);
    doc.text("Sequência Didática", margin, 15);

    doc.setFont("helvetica", "normal");
    doc.setFontSize(10);
    doc.setTextColor(220, 220, 255);
    doc.text(`Prática: ${practiceName}`, margin, 23);

    doc.setFontSize(8);
    doc.text(`Gerado em: ${new Date().toLocaleDateString("pt-BR")}`, margin, 30);

    y = 45;

    // ─── CONTEÚDO ────────────────────────────────────────
    const s = sequence;

    if (s.titulo) {
        addTitle(s.titulo, 14);
        addSeparator();
    }

    if (s.problema_central) {
        addSubtitle("🎯 Problema Central");
        addText(s.problema_central);
        addSeparator();
    }

    if (s.objetivos_aprendizagem && s.objetivos_aprendizagem.length) {
        addSubtitle("📋 Objetivos de Aprendizagem");
        addList(s.objetivos_aprendizagem);
        addSeparator();
    }

    if (s.integracao_interdisciplinar) {
        addSubtitle("🔗 Integração Interdisciplinar");
        if (s.integracao_interdisciplinar.descricao) {
            addText(s.integracao_interdisciplinar.descricao);
        }
        if (s.integracao_interdisciplinar.disciplinas) {
            addList(s.integracao_interdisciplinar.disciplinas);
        }
        addSeparator();
    }

    if (s.passo_a_passo && s.passo_a_passo.length) {
        addSubtitle("📝 Passo a Passo (Aula a Aula)");
        s.passo_a_passo.forEach(aula => {
            checkPage(20);
            doc.setFont("helvetica", "bold");
            doc.setFontSize(10);
            doc.setTextColor(...primaryColor);
            doc.text(`Aula ${aula.aula}: ${aula.titulo} (${aula.duracao})`, margin + 2, y);
            y += 6;

            if (aula.atividades && aula.atividades.length) {
                doc.setFont("helvetica", "italic");
                doc.setFontSize(9);
                doc.setTextColor(...mutedColor);
                doc.text("Atividades:", margin + 4, y);
                y += 5;
                addList(aula.atividades);
            }

            if (aula.recursos && aula.recursos.length) {
                doc.setFont("helvetica", "italic");
                doc.setFontSize(9);
                doc.setTextColor(...mutedColor);
                doc.text("Recursos:", margin + 4, y);
                y += 5;
                addList(aula.recursos);
            }
        });
        addSeparator();
    }

    if (s.atividades_praticas && s.atividades_praticas.length) {
        addSubtitle("🛠️ Atividades Práticas");
        addList(s.atividades_praticas);
        addSeparator();
    }

    if (s.estrategias_engajamento && s.estrategias_engajamento.length) {
        addSubtitle("🚀 Estratégias de Engajamento");
        addList(s.estrategias_engajamento);
        addSeparator();
    }

    if (s.avaliacao) {
        addSubtitle("📊 Avaliação");
        if (s.avaliacao.formativa && s.avaliacao.formativa.length) {
            doc.setFont("helvetica", "bold");
            doc.setFontSize(9.5);
            doc.setTextColor(...textColor);
            doc.text("Formativa:", margin + 2, y);
            y += 5;
            addList(s.avaliacao.formativa);
        }
        if (s.avaliacao.somativa && s.avaliacao.somativa.length) {
            doc.setFont("helvetica", "bold");
            doc.setFontSize(9.5);
            doc.setTextColor(...textColor);
            doc.text("Somativa:", margin + 2, y);
            y += 5;
            addList(s.avaliacao.somativa);
        }
        addSeparator();
    }

    if (s.desenvolvimento_socioemocional && s.desenvolvimento_socioemocional.length) {
        addSubtitle("❤️ Desenvolvimento Socioemocional");
        addList(s.desenvolvimento_socioemocional);
        addSeparator();
    }

    if (s.adaptacao_hibrido && s.adaptacao_hibrido.length) {
        addSubtitle("💻 Adaptação para Ensino Híbrido");
        addList(s.adaptacao_hibrido);
        addSeparator();
    }

    if (s.uso_tecnologia && s.uso_tecnologia.length) {
        addSubtitle("📱 Uso de Tecnologia");
        addList(s.uso_tecnologia);
        addSeparator();
    }

    if (s.produto_final) {
        addSubtitle("🏆 Produto Final Esperado");
        addText(s.produto_final);
    }

    // ─── RODAPÉ ────────────────────────────────────────
    const pageCount = doc.internal.getNumberOfPages();
    for (let i = 1; i <= pageCount; i++) {
        doc.setPage(i);
        doc.setFont("helvetica", "normal");
        doc.setFontSize(7);
        doc.setTextColor(150, 150, 170);
        doc.text(
            `Plataforma de Agentes Pedagógicos Inteligentes — Página ${i} de ${pageCount}`,
            pageWidth / 2, 290,
            { align: "center" }
        );
    }

    // ─── DOWNLOAD ────────────────────────────────────────
    const fileName = `sequencia-didatica-${s.titulo ? s.titulo.substring(0, 30).replace(/[^a-zA-Z0-9]/g, '-') : 'gerada'}.pdf`;
    doc.save(fileName);
}

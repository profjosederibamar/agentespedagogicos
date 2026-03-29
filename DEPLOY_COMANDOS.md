# 🚀 Guia de Deploy para o GitHub — Agentes Pedagógicos

Sempre que você fizer uma alteração no seu código e quiser que ela apareça no **GitHub Pages** (site) e no **Render** (servidor), siga estes 3 passos no terminal.

---

### 1️⃣ Verifique o que mudou
Antes de enviar, é bom ver quais arquivos foram alterados:
```powershell
git status
```

### 2️⃣ Prepare e Comente suas mudanças
Este comando "empacota" todas as suas alterações e coloca uma etiqueta (mensagem) nelas:
```powershell
git add -A
git commit -m "Descreva aqui o que você mudou (ex: ajuste no Gemini)"
```

### 3️⃣ Envie para o Mundo! 🌍
Este comando envia tudo para o GitHub. Assim que ele terminar, o Render começará a atualizar o servidor automaticamente.
```powershell
git push origin main
```

---

### 💡 Dicas de Ouro

*   **GitHub Pages**: Como o seu frontend está na **raiz** do repositório, o GitHub Pages atualiza quase instantaneamente após o `git push`.
*   **Render**: O Render demora cerca de 2 a 3 minutos para "instalar" a nova versão após o push. Você pode acompanhar o progresso na aba **Events** do painel do Render.
*   **Erro de Conexão?**: Se o comando `git push` pedir senha ou der erro de permissão, verifique se você está logado no VS Code com sua conta do GitHub.

---

### 🛠️ Comando "Tudo em Um" (Atalho)
Se você tem certeza das mudanças e quer fazer tudo de uma vez, pode copiar e colar esta linha única:
```powershell
git add -A; git commit -m "Atualização Geral"; git push origin main
```

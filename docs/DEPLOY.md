# 🚀 Tutorial de Deploy — Passo a Passo

Este guia explica como publicar a plataforma na internet **gratuitamente**.

---

## 📋 Visão Geral

| Componente | Serviço | Custo |
|-----------|---------|-------|
| Frontend | GitHub Pages | Gratuito |
| Backend | Render (ou HF Spaces) | Gratuito |

---

## 1️⃣ Deploy do Backend no Render

### Passo 1: Preparar o código

Certifique-se de que a pasta `backend/` está no seu repositório GitHub.

### Passo 2: Criar conta no Render

1. Acesse [render.com](https://render.com)
2. Clique em **"Get Started for Free"**
3. Faça login com sua conta GitHub

### Passo 3: Criar novo Web Service

1. No dashboard do Render, clique em **"New" → "Web Service"**
2. Conecte seu repositório GitHub
3. Configure:
   - **Name**: `agentes-pedagogicos-api`
   - **Region**: escolha a mais próxima (ex: Oregon)
   - **Branch**: `main`
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type**: **Free**

### Passo 4: Variáveis de ambiente

Na seção **"Environment"**, adicione:
- `GEMINI_API_KEY` = sua chave do Google AI Studio (recomendado)
- `GROQ_API_KEY` = sua chave do Groq Dashboard
- `HUGGINGFACE_API_KEY` = seu token do Hugging Face
- `ENVIRONMENT` = `production`

> 💡 **Dica**: Pegue suas chaves gratuitamente em:
> - **Gemini**: [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
> - **Groq**: [console.groq.com/keys](https://console.groq.com/keys)
> - **HuggingFace**: [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

### Passo 5: Deploy!

Clique em **"Create Web Service"**. O Render vai:
1. Clonar seu repositório
2. Instalar dependências
3. Iniciar o servidor

Sua API estará em: `https://agentes-pedagogicos-api.onrender.com`

> ⚠️ **Nota**: No plano gratuito, o servidor "dorme" após 15 min sem uso. A primeira requisição pode demorar ~30 segundos para "acordar".

---

## 2️⃣ Deploy do Frontend no GitHub Pages

### Passo 1: Atualizar URL do backend

Edite o arquivo `frontend/js/api.js` e atualize a URL:

```javascript
const API_CONFIG = {
    baseUrl: "https://agentes-pedagogicos-api.onrender.com",
};
```

### Passo 2: Configurar GitHub Pages

1. Vá ao seu repositório no GitHub
2. Clique em **Settings → Pages**
3. Em **Source**, selecione:
   - **Branch**: `main`
   - **Folder**: `/frontend` (se disponível, caso contrário `/root`)
4. Clique em **"Save"**

### Passo 3: Aguardar publicação

O GitHub vai gerar uma URL como:
`https://seu-usuario.github.io/Agentes-de-IA-Educacionais/`

> Se a pasta for `/root`, acesse: `https://seu-usuario.github.io/Agentes-de-IA-Educacionais/frontend/`

---

## 3️⃣ Alternativa: Backend no Hugging Face Spaces

### Passo 1: Criar conta

1. Acesse [huggingface.co](https://huggingface.co)
2. Crie uma conta gratuita

### Passo 2: Criar novo Space

1. Clique em **"New Space"**
2. Configure:
   - **Name**: `agentes-pedagogicos`
   - **SDK**: **Docker**
   - **Hardware**: **CPU basic (Free)**

### Passo 3: Upload dos arquivos

Faça upload de todos os arquivos da pasta `backend/`:
- `main.py`
- `requirements.txt`
- `Dockerfile`
- Pasta `agents/`
- Pasta `services/`

### Passo 4: Configurar secrets

Em **Settings → Variables and secrets**, adicione:
- `GEMINI_API_KEY` = sua chave Gemini
- `GROQ_API_KEY` = sua chave Groq
- `HUGGINGFACE_API_KEY` = seu token HuggingFace

A URL será: `https://seu-usuario-agentes-pedagogicos.hf.space`

---

## ✅ Checklist Final

- [ ] Backend está rodando (testar `/api/health`)
- [ ] Frontend atualizado com URL do backend
- [ ] Frontend publicado no GitHub Pages
- [ ] Testar o fluxo completo na versão publicada
- [ ] Pelo menos uma API Key configurada (Gemini, Groq ou HF)

---

## 🔧 Solução de Problemas

### "Não foi possível conectar ao servidor"
- Verifique se o backend está rodando
- No Render gratuito, aguarde ~30s para o servidor acordar
- Confirme que a URL no `api.js` está correta

### "CORS error"
- O backend já tem CORS configurado para aceitar qualquer origem
- Se persistir, verifique se a URL não tem `/` no final

### "Erro 500 do servidor"
- Verifique os logs no Render (Dashboard → Logs)
- Confirme que as dependências foram instaladas corretamente

---

## 🎉 Pronto!

Sua plataforma está no ar! Compartilhe o link com outros professores! 🚀

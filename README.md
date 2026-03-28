# 🧠 Plataforma de Agentes Pedagógicos Inteligentes

Uma aplicação web completa onde professores escolhem uma prática pedagógica inovadora e um agente de IA gera automaticamente uma **sequência didática excelente**, interdisciplinar e pronta para aplicar em sala de aula.

![Status](https://img.shields.io/badge/status-ativo-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

---

## ✨ Funcionalidades

- **9 Práticas Pedagógicas**: ABP, PBL, STEAM, Gamificação, Cultura Maker, Ensino Híbrido, Sala Invertida, Aprendizagem Colaborativa, Educação Socioemocional
- **Múltiplos Provedores de IA**: Escolha entre Google Gemini, Groq (Llama 3) ou HuggingFace
- **Roteamento Inteligente**: Sistema de fallback automático entre provedores e templates
- **12 Seções Completas**: Título, problema central, objetivos, passo a passo, avaliação e mais
- **Exportação em PDF**: Baixe a sequência em formato profissional
- **Histórico**: Acesse sequências geradas anteriormente
- **Edição Inline**: Edite o conteúdo diretamente na tela
- **Design Clean**: Interface moderna com tema claro, robôs 3D e animações suave

---

## 🏗️ Arquitetura

```
Frontend (HTML/CSS/JS)  ──→  Backend (FastAPI/Python)  ──→  Google Gemini (Principal)
     │                              │                      ├── Groq / Llama 3 (Backup)
     │                              ├── Multi-Provider AI  └── HuggingFace (Backup)
     │                              └── Templates Locais   ─── (Fallback Final)
     │
     ├── SPA com Tema Claro
     ├── Identidade Visual (Robôs 3D)
     └── Geração de PDF e Histórico
```

---

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.10+
- pip (gerenciador de pacotes Python)
- Navegador web moderno

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/Agentes-de-IA-Educacionais.git
cd Agentes-de-IA-Educacionais
```

### 2. Configure o Backend

```bash
cd backend

# Crie ambiente virtual (recomendado)
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale dependências
pip install -r requirements.txt

# Configure variáveis de ambiente
copy .env.example .env
# Edite o arquivo .env com sua API Key do Hugging Face (opcional)
```

### 3. Inicie o Backend

```bash
# Dentro da pasta backend/
uvicorn main:app --reload --port 8000
```

O servidor estará disponível em `http://localhost:8000`

### 4. Abra o Frontend

Abra o arquivo `frontend/index.html` diretamente no navegador.

Ou use um servidor local:

```bash
cd frontend
python -m http.server 3000
```

Acesse `http://localhost:3000`

---

## 🔑 Chaves de API (Recomendado)

O sistema funciona sem chaves (usando templates), mas para usar o poder total da IA, obtenha suas chaves gratuitas:

1. **Google Gemini (Principal)**: [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. **Groq (Velocidade)**: [console.groq.com/keys](https://console.groq.com/keys)
3. **HuggingFace**: [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

Adicione no arquivo `backend/.env`:
```
GEMINI_API_KEY=sua_chave_aqui
GROQ_API_KEY=sua_chave_aqui
HUGGINGFACE_API_KEY=sua_chave_aqui
```

---

## 📁 Estrutura de Pastas

```
├── frontend/
│   ├── index.html          # Página principal SPA
│   ├── css/styles.css      # Design system completo
│   ├── js/
│   │   ├── app.js          # Lógica principal
│   │   ├── agents.js       # Definições das práticas
│   │   ├── api.js          # Comunicação com backend
│   │   ├── pdf.js          # Geração de PDF
│   │   └── history.js      # Histórico (localStorage)
│   └── assets/favicon.svg
│
├── backend/
│   ├── main.py             # Servidor FastAPI
│   ├── agents/             # 9 agentes pedagógicos
│   ├── services/           # AI e Template services
│   ├── requirements.txt
│   └── Dockerfile
│
└── docs/DEPLOY.md          # Tutorial de deploy
```

---

## 🌐 Deploy

Veja o [Tutorial Completo de Deploy](docs/DEPLOY.md) para publicar:

- **Frontend**: GitHub Pages (gratuito)
- **Backend**: Render ou Hugging Face Spaces (gratuito)

---

## 📜 Licença

MIT License — use livremente para fins educacionais!

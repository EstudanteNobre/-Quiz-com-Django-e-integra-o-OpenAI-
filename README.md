# 🎯 InfoQuiz 2.0 - Quiz Inteligente com Django & OpenAI

O **InfoQuiz 2.0** é uma plataforma de aprendizado gamificada que utiliza Inteligência Artificial para gerar desafios personalizados. O projeto combina um sistema de quiz tradicional com a potência do GPT da OpenAI para criar perguntas dinâmicas e dicas de estudo em tempo real.

---

## 🚀 Funcionalidades Principais

### 1. Sistema de Quiz com IA (OpenAI)
- **Geração Dinâmica:** Perguntas criadas na hora via API da OpenAI.
- **Dicas de Estudo:** Sistema de revisão onde a IA gera uma dica personalizada para cada erro cometido.
- **Níveis de Dificuldade:** Algoritmo que organiza perguntas em Fácil, Médio e Difícil.

### 2. Gamificação e UX
- **Sistema de Pontuação:** Baseado na velocidade da resposta e nível de dificuldade.
- **Feedback Visual e Sonoro:** Cronômetro dinâmico, efeitos de acerto/erro e countdown.
- **Acessibilidade:** Painel com ajuste de fonte, alto contraste e suporte a leitores de tela.

### 3. Gestão de Usuários
- Dashboard completo com estatísticas de progresso e histórico.
- Ranking global e por temas técnicos (Python, Redes, Banco de Dados, etc.).
- Sistema de conquistas e títulos.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3.x / Django 5.2.8
- **Inteligência Artificial:** OpenAI API (GPT-4o-mini)
- **Segurança:** `python-dotenv` para gestão de variáveis de ambiente.
- **Frontend:** HTML5, CSS3 (Responsivo) e JavaScript para lógica de jogo.

---

## 🔧 Como Rodar o Projeto Localmente

1. **Clone o repositório:**
   git clone https://github.com/EstudanteNobre/-Quiz-com-Django-e-integra-o-OpenAI-.git

2. **Crie e ative seu ambiente virtual:**
   python -m venv .venv
   *(No Windows: .venv\Scripts\activate)*

3. **Instale as dependências:**
   pip install -r requirements.txt

4. **Configuração de Segurança (Variáveis de Ambiente):**
   - Renomeie o arquivo .env.example para .env.
   - Insira sua OPENAI_API_KEY e a SECRET_KEY do Django dentro do .env.

5. **Inicie o servidor:**
   python manage.py migrate
   python manage.py runserver

---

## 📄 Informações Adicionais
Projeto desenvolvido como parte do aprendizado em desenvolvimento web e integração de APIs de Inteligência Artificial.

Desenvolvido por **Gabriel Nobre** 🚀

import streamlit as st
from scraping.scraper import *


# MENU HORIZONTAL
st.markdown("""
    <style>
        .menu-bar {
            background-color: #2e7d32;
            padding: 10px;
            border-radius: 5px;
        }
        .menu-bar a {
            color: white;
            text-decoration: none;
            margin-right: 15px;
            font-weight: bold;
        }
        .menu-bar a:hover {
            text-decoration: underline;
        }
    </style>
    <div class="menu-bar">
        <a href="/?page=home">首页</a>
        <a href="/?page=news">新闻</a>
        <a href="/?page=photos">读图</a>
        <a href="/?page=economy">财经</a>
        <a href="/?page=education">教育</a>
        <a href="/?page=house">家居</a>
        <a href="/?page=health">健康</a>
        <a href="/?page=food">美食</a>
        <a href="/?page=fashion">时尚</a>
        <a href="/?page=travel">旅游</a>
        <a href="/?page=tv">影视</a>
        <a href="/?page=blog">博客</a>
        <a href="/?page=forum">群吧</a>
        <a href="/?page=discussion">论坛</a>
        <a href="/?page=radio">电台</a>
    </div>
""", unsafe_allow_html=True)

# Capturando a página clicada via query params
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0]

# Dicionário de conteúdos
page_texts = {
    "home": scraping(),
    "news": "这里是新闻页面 📰",
    "photos": "这里是读图页面 🖼️",
    "economy": "财经新闻页面 💰",
    "education": "教育专区 📚",
    "house": "家居生活 🏠",
    "health": "健康养生 💪",
    "food": "美食推荐 🍜",
    "fashion": "时尚潮流 👗",
    "travel": "旅游目的地 ✈️",
    "tv": "影视娱乐 🎬",
    "blog": "博客分享 ✏️",
    "forum": "群吧交流 💬",
    "discussion": "论坛讨论 🗣️",
    "radio": "电台节目 🎧"
}

# Exibir o conteúdo correspondente
st.title(page_texts.get(page, "页面不存在 ❌"))
#st.title(page_texts.get(page, print(scraping())))




# import streamlit as st

# # Definindo o menu de navegação com links
# st.markdown("""
#     <style>
#         .menu-bar {
#             background-color: #2e7d32;
#             padding: 10px;
#             border-radius: 5px;
#         }
#         .menu-bar a {
#             color: white;
#             text-decoration: none;
#             margin-right: 15px;
#             font-weight: bold;
#         }
#         .menu-bar a:hover {
#             text-decoration: underline;
#         }
#     </style>
#     <div class="menu-bar">
#         <a href="/?page=home">首页</a>
#         <a href="/?page=news">新闻</a>
#         <a href="/?page=photos">读图</a>
#         <a href="/?page=economy">财经</a>
#         <a href="/?page=education">教育</a>
#         <a href="/?page=house">家居</a>
#         <a href="/?page=health">健康</a>
#         <a href="/?page=food">美食</a>
#         <a href="/?page=fashion">时尚</a>
#         <a href="/?page=travel">旅游</a>
#         <a href="/?page=tv">影视</a>
#         <a href="/?page=blog">博客</a>
#         <a href="/?page=forum">群吧</a>
#         <a href="/?page=discussion">论坛</a>
#         <a href="/?page=radio">电台</a>
#     </div>
# """, unsafe_allow_html=True)

# # Capturando a página clicada via query params
# query_params = st.experimental_get_query_params()
# page = query_params.get("page", ["home"])[0]

# # Conteúdo de cada página
# if page == "home":
#     st.title("欢迎来到首页")
# elif page == "news":
#     st.title("新闻页面")
# elif page == "photos":
#     st.title("读图页面")
# elif page == "economy":
#     st.title("财经页面")
# elif page == "education":
#     st.title("教育页面")
# elif page == "house":
#     st.title("家居页面")
# elif page == "health":
#     st.title("健康页面")
# elif page == "food":
#     st.title("美食页面")
# elif page == "fashion":
#     st.title("时尚页面")
# elif page == "travel":
#     st.title("旅游页面")
# elif page == "tv":
#     st.title("影视页面")
# elif page == "blog":
#     st.title("博客页面")
# elif page == "forum":
#     st.title("群吧页面")
# elif page == "discussion":
#     st.title("论坛页面")
# elif page == "radio":
#     st.title("电台页面")

# import streamlit as st

# st.title("✅ Minha Lista de Tarefas")

# # Lista de tarefas
# tarefas = ["Comprar pão", "Ligar cliente", "Enviar relatório"]

# # Criando um dicionário para armazenar o estado de cada tarefa
# status_tarefas = {}

# # Exibir as checkboxes
# for tarefa in tarefas:
#     status_tarefas[tarefa] = st.checkbox(tarefa)

# # Mostrar as tarefas completas
# st.subheader("✔️ Tarefas Concluídas:")
# for tarefa, concluida in status_tarefas.items():
#     if concluida:
#         st.write(f"✅ {tarefa}")

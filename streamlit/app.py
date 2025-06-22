import streamlit as st

st.title("✅ Minha Lista de Tarefas")

# Lista de tarefas
tarefas = ["Comprar pão", "Ligar cliente", "Enviar relatório"]

# Criando um dicionário para armazenar o estado de cada tarefa
status_tarefas = {}

# Exibir as checkboxes
for tarefa in tarefas:
    status_tarefas[tarefa] = st.checkbox(tarefa)

# Mostrar as tarefas completas
st.subheader("✔️ Tarefas Concluídas:")
for tarefa, concluida in status_tarefas.items():
    if concluida:
        st.write(f"✅ {tarefa}")

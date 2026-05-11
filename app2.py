import requests
import streamlit as st

st.set_page_config(
    page_title="AI Studio Local",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

OLLAMA_URL = "http://localhost:11434/api/chat"
OLLAMA_MODELS = {
    "llama3.2 / 3b": "llama3.2:3b",
    "qwen2.5 / 3b": "qwen2.5:3b",
    "phi3 / mini": "phi3:mini",
    "gemma2 / 2b": "gemma2:2b",
}


def ask_ollama(model_id, messages, temperature, top_p, max_tokens):
    payload = {
        "model": model_id,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": temperature,
            "top_p": top_p,
            "num_predict": max_tokens,
        },
    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=180)
    response.raise_for_status()
    return response.json()["message"]["content"]


with st.sidebar:
    st.title("Configuracion local")
    model_label = st.selectbox("Modelo de Ollama", list(OLLAMA_MODELS.keys()))
    model_id = OLLAMA_MODELS[model_label]
    st.caption(f"Modelo activo: `{model_id}`")

    max_tokens = st.slider("Maximo de tokens", 64, 1024, 512, 64)
    temperature = st.slider("Temperatura", 0.1, 1.5, 0.7, 0.05)
    top_p = st.slider("Top-p", 0.1, 1.0, 0.95, 0.05)

    st.info("Esta version solo usa Ollama local. No necesita API key.")

st.title("AI Studio Local")
st.caption("Chat con modelos instalados en Ollama.")

if "local_chat_history" not in st.session_state:
    st.session_state.local_chat_history = []

for message in st.session_state.local_chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.local_chat_history:
    if st.button("Limpiar conversacion"):
        st.session_state.local_chat_history = []
        st.rerun()

user_input = st.chat_input("Escribe tu mensaje...")
if user_input:
    st.session_state.local_chat_history.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    messages = [
        {
            "role": "system",
            "content": "Responde de forma clara, breve y en el idioma del usuario.",
        },
        *st.session_state.local_chat_history,
    ]

    with st.chat_message("assistant"):
        with st.spinner("Consultando Ollama..."):
            try:
                answer = ask_ollama(model_id, messages, temperature, top_p, max_tokens)
                st.markdown(answer)
                st.session_state.local_chat_history.append(
                    {"role": "assistant", "content": answer}
                )
            except requests.exceptions.ConnectionError:
                st.error("No se pudo conectar con Ollama. Abre Ollama y revisa localhost:11434.")
            except requests.exceptions.HTTPError as exc:
                st.error(f"Ollama devolvio un error HTTP: {exc}")
            except Exception as exc:
                st.error(f"Error inesperado: {exc}")

import re
import requests
import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
# Configuración general de Streamlit: título de pestaña, icono y layout ancho.
st.set_page_config(
    page_title="AI Studio · Local + Remoto",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
# Estilos globales para darle a la app una apariencia oscura y consistente.
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@400;500&display=swap');
  :root {
    --bg:#0d0f14; --surface:#141720; --border:#252a38;
    --accent:#7c6af7; --accent2:#3ecfcf; --text:#e4e8f0;
    --muted:#6b7385; --danger:#f74b6a; --radius:12px;
  }
  html,body,[class*="css"]{font-family:'Syne',sans-serif;background-color:var(--bg)!important;color:var(--text)!important;}
  #MainMenu,footer,header{visibility:hidden;}
  [data-testid="stSidebar"]{background:var(--surface)!important;border-right:1px solid var(--border)!important;}
  [data-testid="stSidebar"] *{color:var(--text)!important;}
  .stTextInput>div>div>input,.stTextArea>div>div>textarea,.stSelectbox>div>div>div{
    background:var(--bg)!important;border:1px solid var(--border)!important;
    border-radius:var(--radius)!important;color:var(--text)!important;
    font-family:'DM Mono',monospace!important;}
  .stTextInput>div>div>input:focus,.stTextArea>div>div>textarea:focus{
    border-color:var(--accent)!important;box-shadow:0 0 0 3px rgba(124,106,247,.18)!important;}
  .stButton>button{
    background:linear-gradient(135deg,var(--accent),#9b59f5)!important;
    color:#fff!important;border:none!important;border-radius:var(--radius)!important;
    font-family:'Syne',sans-serif!important;font-weight:700!important;
    font-size:1rem!important;padding:.65rem 2.2rem!important;
    letter-spacing:.5px!important;transition:opacity .2s,transform .15s!important;}
  .stButton>button:hover{opacity:.88!important;transform:translateY(-1px)!important;}
  .answer-card{background:var(--surface);border:1px solid var(--accent);border-radius:var(--radius);
    padding:1.6rem 2rem;margin-top:1.5rem;box-shadow:0 0 28px rgba(124,106,247,.15);}
  .answer-card .label{font-size:.72rem;letter-spacing:2px;text-transform:uppercase;color:var(--accent2);margin-bottom:.5rem;}
  .answer-card .answer-text{font-size:1.2rem;font-weight:600;line-height:1.6;}
  .answer-card .meta{margin-top:.8rem;font-family:'DM Mono',monospace;font-size:.75rem;color:var(--muted);}
  .score-bar-wrap{margin-top:.3rem;display:flex;align-items:center;gap:.7rem;}
  .score-bar-bg{flex:1;height:6px;background:var(--border);border-radius:99px;overflow:hidden;}
  .score-bar-fill{height:100%;background:linear-gradient(90deg,var(--accent2),var(--accent));border-radius:99px;}
  .mode-badge{display:inline-block;padding:.2rem .8rem;border-radius:99px;font-size:.72rem;
    font-weight:700;letter-spacing:1px;text-transform:uppercase;margin-bottom:1rem;}
  .mode-qa{background:rgba(62,207,207,.15);color:var(--accent2);border:1px solid var(--accent2);}
  .mode-gen{background:rgba(124,106,247,.15);color:var(--accent);border:1px solid var(--accent);}
  .hero{padding:2rem 0 1rem;}
  .hero h1{font-size:2.8rem;font-weight:800;line-height:1.1;margin:0;
    background:linear-gradient(135deg,#fff 30%,var(--accent));
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;}
  .hero p{color:var(--muted);font-size:.95rem;margin-top:.5rem;}
  .instr-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1rem;}
  .instr-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1rem 1.2rem;}
  .instr-card .ic-icon{font-size:1.4rem;margin-bottom:.3rem;}
  .instr-card .ic-title{font-weight:700;font-size:.85rem;margin-bottom:.25rem;}
  .instr-card .ic-body{font-size:.78rem;color:var(--muted);line-height:1.5;}
  hr{border-color:var(--border)!important;}
  .tab-hint{font-size:.78rem;color:var(--muted);margin-bottom:1rem;}
</style>
""", unsafe_allow_html=True)

# ── Error handler ──────────────────────────────────────────────────────────────
def handle_error(e):
    """Muestra mensajes amigables según el tipo de error devuelto por cada proveedor."""
    err = str(e)
    if "401" in err or "authorization" in err.lower() or "token" in err.lower():
        st.error("🔐 **API key inválida o sin permisos.** Verifica la key del proveedor seleccionado.")
    elif "503" in err or "loading" in err.lower():
        st.warning("⏳ **Modelo cargando** (cold start). Espera unos segundos e intenta de nuevo.")
    elif "429" in err:
        st.warning("🚦 **Límite de requests alcanzado.** Espera un momento e intenta de nuevo.")
    elif "connection" in err.lower() or "timeout" in err.lower():
        st.error("🌐 **Error de conexión.** Revisa tu internet.")
    elif "terms of service" in err.lower() or "gated" in err.lower():
        st.error("🔒 **Modelo con acceso restringido.** Revisa los permisos de tu cuenta o selecciona otro modelo.")
    elif "model '" in err.lower() and "not found" in err.lower():
        st.error("❌ **Modelo no instalado en Ollama.** Instala el modelo seleccionado con `ollama pull <modelo>` o selecciona otro modelo instalado localmente.")
    elif "not supported by any provider" in err.lower() or "model not supported" in err.lower():
        st.error("❌ **Modelo no compatible con tu proveedor actual.** Prueba otro modelo o revisa si el modelo requiere un proveedor diferente.")
    else:
        st.error(f"❌ **Error inesperado:** {err}")


# Endpoint local de Ollama. Requiere que Ollama esté corriendo en la máquina.
OLLAMA_URL = "http://localhost:11434/api/chat"

# Modelos locales disponibles en tu instalación de Ollama.
OLLAMA_MODELS = {
    "🔥 llama3.2 / 3b": "llama3.2:3b",
    "🧩 qwen2.5 / 3b": "qwen2.5:3b",
    "💡 phi3 / mini": "phi3:mini",
    "🌌 gemma2 / 2b": "gemma2:2b",
}

# Endpoint remoto de Groq compatible con el formato de OpenAI Chat Completions.
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

# Modelos remotos disponibles vía Groq.
GROQ_MODELS = {
    "⚡ Groq / GPT-OSS 20B": "openai/gpt-oss-20b",
    "🧠 Groq / GPT-OSS 120B": "openai/gpt-oss-120b",
    "🦙 Groq / Llama 3.3 70B": "llama-3.3-70b-versatile",
    "🚀 Groq / Llama 3.1 8B Instant": "llama-3.1-8b-instant",
    "🧩 Groq / Compound Mini": "groq/compound-mini",
    "🔎 Groq / Qwen3 32B": "qwen/qwen3-32b",
}

# Router remoto oficial de Hugging Face para chat completions.
HF_URL = "https://router.huggingface.co/v1/chat/completions"

# Modelos de Hugging Face usando :fastest para que el router elija el proveedor más rápido.
HF_MODELS = {
    "🤗 HF / GPT-OSS 20B (fastest)": "openai/gpt-oss-20b:fastest",
    "🤗 HF / GPT-OSS 120B (fastest)": "openai/gpt-oss-120b:fastest",
    "🤗 HF / DeepSeek R1 (fastest)": "deepseek-ai/DeepSeek-R1:fastest",
    "🤗 HF / Qwen3 32B (fastest)": "Qwen/Qwen3-32B:fastest",
    "🤗 HF / Llama 3.1 8B (fastest)": "meta-llama/Llama-3.1-8B-Instruct:fastest",
}

def ollama_chat(model_id, messages, temperature=0.7, top_p=0.95, max_tokens=512):
    """Envía una conversación al servidor local de Ollama y devuelve solo el texto."""
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
    data = response.json()
    return data["message"]["content"]

def remote_chat(api_key, url, model_id, messages, temperature=0.7, top_p=0.95, max_tokens=512):
    """Llama proveedores remotos compatibles con OpenAI: Groq o Hugging Face."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model_id,
        "messages": messages,
        "temperature": temperature,
        "top_p": top_p,
    }

    # Groq usa max_completion_tokens; Hugging Face router espera max_tokens.
    token_limit_key = "max_tokens" if url == HF_URL else "max_completion_tokens"
    payload[token_limit_key] = max_tokens

    response = requests.post(url, headers=headers, json=payload, timeout=180)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]

def normalize_latex_markdown(text):
    """Convierte delimitadores LaTeX comunes a Markdown matemático renderizable."""
    if not text:
        return text

    normalized = text

    # Algunos modelos devuelven backslashes duplicados; esto limpia esos casos.
    normalized = re.sub(r"\\\\(?=[A-Za-z!,:;{}_^])", r"\\", normalized)
    normalized = re.sub(r"\\\\([\(\)\[\]])", r"\\\1", normalized)

    # Convierte bloques \[...\] a $$...$$.
    normalized = re.sub(
        r"\\\[(.+?)\\\]",
        lambda match: f"\n\n$$\n{match.group(1).strip()}\n$$\n\n",
        normalized,
        flags=re.DOTALL,
    )

    # Convierte expresiones en línea \(...\) a $...$.
    normalized = re.sub(
        r"\\\((.+?)\\\)",
        lambda match: f"${match.group(1).strip()}$",
        normalized,
        flags=re.DOTALL,
    )

    return normalized

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Configuración")
    st.markdown("---")

    # Primero se elige si se quiere ejecutar localmente o con un proveedor remoto.
    run_type = st.radio(
        "Tipo de ejecución",
        ["Remoto", "Local"],
        index=0,
    )

    # Local siempre significa Ollama; remoto permite escoger proveedor.
    if run_type == "Local":
        backend = "Ollama"
    else:
        backend = st.radio(
            "Proveedor remoto",
            ["Groq", "Hugging Face"],
            index=0,
        )

    groq_api_key = ""
    hf_api_key = ""

    # La API key solo se pide cuando el backend activo la necesita.
    if backend == "Groq":
        groq_api_key = st.text_input(
            "⚡ Groq API Key",
            type="password",
            placeholder="gsk_xxxxxxxxxxxxxxxxxxxx",
            help="console.groq.com → API Keys",
            key="groq_api_key",
        )
        if groq_api_key:
            st.success("✅ Groq key detectada")

    if backend == "Hugging Face":
        hf_api_key = st.text_input(
            "🤗 Hugging Face Token",
            type="password",
            placeholder="hf_xxxxxxxxxxxxxxxxxxxx",
            help="huggingface.co → Settings → Access Tokens. El token debe poder llamar Inference Providers.",
            key="hf_api_key",
        )
        if hf_api_key:
            st.success("✅ Hugging Face token detectado")

    # Resumen visible del backend que se usará para responder.
    st.markdown("---")
    st.markdown("#### Backend activo")
    st.caption(f"`{run_type}` → `{backend}`")

    if backend == "Ollama":
        st.success("💻 Ollama local seleccionado. No necesitas token.")
        st.caption("Asegurate de que Ollama esté corriendo en localhost:11434 y que el modelo esté instalado.")

    if backend == "Groq":
        st.success("⚡ Groq remoto seleccionado.")
        st.caption("Groq usa una API remota compatible con OpenAI.")

    if backend == "Hugging Face":
        st.success("🤗 Hugging Face remoto seleccionado.")
        st.caption("Usa el router oficial de Inference Providers con selección :fastest.")

    st.markdown("---")
    st.markdown("#### Modelo")

    # El listado de modelos cambia según el backend seleccionado.
    if backend == "Ollama":
        model_list = OLLAMA_MODELS
    elif backend == "Hugging Face":
        model_list = HF_MODELS
    else:
        model_list = GROQ_MODELS
    model_label = st.selectbox("Modelo", list(model_list.keys()), key=f"gen_model_{backend}", label_visibility="collapsed")
    model_id = model_list[model_label]
    st.caption(f"`{model_id}`")

    # Parámetros comunes para todos los proveedores.
    st.markdown("#### Parámetros")
    max_tokens  = st.slider("Máx. tokens a generar", 64, 1024, 512, 64, key="gen_tokens")
    temperature = st.slider("Temperatura", 0.1, 1.5, 0.7, 0.05,
                            help="Alto = creativo · Bajo = preciso", key="gen_temp")
    top_p       = st.slider("Top-p", 0.1, 1.0, 0.95, 0.05, key="gen_top_p")
    system_prompt = st.text_area(
        "System prompt (opcional)",
        value=(
            "Eres un asistente inteligente. Responde de forma clara, concisa y en el idioma del usuario. "
            "Si escribes formulas, usa Markdown matematico con $...$ para expresiones en linea "
            "y $$...$$ para ecuaciones centradas."
        ),
        height=140,
        key="gen_prompt",
    )

    st.markdown("---")
    st.caption("AI Studio · Local: Ollama · Remoto: Groq/HF")


# ── Hero ───────────────────────────────────────────────────────────────────────
# Encabezado principal de la app.
st.markdown("""
<div class="hero">
  <h1>🧠 AI Studio</h1>
  <p>Chat con modelos locales en Ollama y modelos remotos en Groq o Hugging Face.</p>
</div>
""", unsafe_allow_html=True)

# ── Main interface ─────────────────────────────────────────────────────────────────
st.markdown("## Chat Generativo")
st.markdown("Elige Local para Ollama o Remoto para Groq/Hugging Face desde la barra lateral.")

# Inicializa el historial de conversación una sola vez por sesión.
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Reimprime los mensajes anteriores cuando Streamlit recarga la página.
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(normalize_latex_markdown(msg["content"]))

# Botón para limpiar la conversación actual.
if st.session_state.chat_history:
    if st.button("🗑️ Limpiar conversación", key="gen_clear"):
        st.session_state.chat_history = []
        st.rerun()

user_input = st.chat_input("Escribe tu mensaje aquí…", key="gen_input")
if user_input:
    # Validaciones mínimas antes de llamar un proveedor remoto.
    if backend == "Groq" and not groq_api_key:
        st.error("⚡ Ingresa tu Groq API key en la barra lateral.")
        st.stop()
    if backend == "Hugging Face" and not hf_api_key:
        st.error("🤗 Ingresa tu Hugging Face token en la barra lateral.")
        st.stop()

    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("🤖 Generando respuesta…"):
            try:
                # Formato estándar de mensajes tipo OpenAI: system + historial completo.
                messages = [{"role": "system", "content": system_prompt}]
                for m in st.session_state.chat_history:
                    messages.append({"role": m["role"], "content": m["content"]})

                # Enruta la llamada al backend seleccionado.
                if backend == "Ollama":
                    reply = ollama_chat(
                        model_id,
                        messages=messages,
                        temperature=temperature,
                        top_p=top_p,
                        max_tokens=max_tokens,
                    )
                elif backend == "Groq":
                    reply = remote_chat(
                        groq_api_key,
                        GROQ_URL,
                        model_id,
                        messages=messages,
                        temperature=temperature,
                        top_p=top_p,
                        max_tokens=max_tokens,
                    )
                else:
                    reply = remote_chat(
                        hf_api_key,
                        HF_URL,
                        model_id,
                        messages=messages,
                        temperature=temperature,
                        top_p=top_p,
                        max_tokens=max_tokens,
                    )

                # Normaliza LaTeX antes de mostrarlo para que Streamlit renderice fórmulas.
                reply = normalize_latex_markdown(reply)
                st.markdown(reply)
                st.caption(f"🤖 `{model_id}` · temp={temperature} · top_p={top_p}")

                # Guarda la respuesta para mantener la conversación en la siguiente recarga.
                st.session_state.chat_history.append({"role": "assistant", "content": reply})

            except Exception as e:
                handle_error(e)

# ── Instrucciones ─────────────────────────────────────────────────────────────────
# Tarjetas informativas al final de la app.
st.markdown("---")
st.markdown("### 📖 Cómo usar AI Studio")
st.markdown("""
<div class="instr-grid">
  <div class="instr-card">
    <div class="ic-icon">💻</div>
    <div class="ic-title">1. Local</div>
    <div class="ic-body">Local usa Ollama y tus modelos instalados en la máquina, sin API key externa.</div>
  </div>
  <div class="instr-card">
    <div class="ic-icon">⚡</div>
    <div class="ic-title">2. Remoto</div>
    <div class="ic-body">Remoto permite usar Groq o Hugging Face con sus respectivas API keys.</div>
  </div>
  <div class="instr-card">
    <div class="ic-icon">🤗</div>
    <div class="ic-title">3. Hugging Face</div>
    <div class="ic-body">Hugging Face usa el router OpenAI-compatible de Inference Providers con modelos :fastest.</div>
  </div>
  <div class="instr-card">
    <div class="ic-icon">🎛️</div>
    <div class="ic-title">4. Parámetros</div>
    <div class="ic-body">Temperatura alta da respuestas más creativas; temperatura baja da respuestas más precisas y predecibles.</div>
  </div>
</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.caption("💡 Local = Ollama. Remoto = Groq o Hugging Face.")

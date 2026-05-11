# AI Studio: LLMs Locales y Remotos

<p align="center">
  <strong>Una pagina web en Streamlit para probar inteligencias artificiales gratis, locales y remotas.</strong>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img alt="Ollama" src="https://img.shields.io/badge/Ollama-Local-111111?style=for-the-badge">
  <img alt="Groq" src="https://img.shields.io/badge/Groq-Remoto-F55036?style=for-the-badge">
  <img alt="Hugging Face" src="https://img.shields.io/badge/Hugging%20Face-Remoto-FFD21E?style=for-the-badge">
</p>

---

## Vista General

**AI Studio** permite conversar con modelos de lenguaje desde una interfaz web sencilla. El proyecto compara dos formas de usar IA:

- **Local:** con Ollama, ejecutando modelos en tu propia computadora y sin API key.
- **Remota:** con Groq o Hugging Face, usando modelos en la nube mediante token/API key.

Tambien se incluye la presentacion del proyecto:

```text
Zero_Infrastructure_LLMs.pptx
```

## Que Incluye

```text
PresentacionLLM/
|-- app.py                         # App principal: Ollama + Groq + Hugging Face
|-- app2.py                        # App alternativa: solo Ollama local
|-- requirements.txt               # Dependencias de Python
|-- Zero_Infrastructure_LLMs.pptx   # Presentacion del proyecto
|-- files/                         # Carpeta opcional para material adicional
|-- files.zip                      # Material comprimido relacionado
|-- .gitignore                     # Archivos que no se suben al repositorio
`-- README.md                      # Guia de instalacion y uso
```

## Funciones

| Funcion | Descripcion |
| --- | --- |
| Chat local | Usa modelos instalados con Ollama en `localhost:11434`. |
| Chat remoto | Permite llamar APIs de Groq y Hugging Face. |
| Selector de modelo | Cambia de proveedor y modelo desde la barra lateral. |
| Parametros | Ajusta temperatura, top-p y maximo de tokens. |
| Historial | Mantiene la conversacion durante la sesion de Streamlit. |
| Markdown y formulas | Renderiza respuestas con Markdown y LaTeX cuando el modelo las genera. |

## Requisitos

Antes de instalar, revisa que tengas:

- Python 3.10 o superior.
- Git, si vas a clonar o subir el proyecto a GitHub.
- Ollama, si quieres usar IA local.
- Una API key de Groq, si quieres usar Groq.
- Un token de Hugging Face, si quieres usar Hugging Face Inference Providers.

## Instalacion Rapida

### 1. Clonar o Entrar al Proyecto

Si ya tienes la carpeta en tu PC:

```powershell
cd C:\Users\kenne\OneDrive\Documentos\progras\python\PresentacionLLM
```

Si lo descargas desde GitHub:

```bash
git clone https://github.com/TU_USUARIO/PresentacionLLM.git
cd PresentacionLLM
```

### 2. Crear Entorno Virtual

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la App Principal

```bash
python -m streamlit run app.py
```

Streamlit abrira la pagina en el navegador. Normalmente queda en:

```text
http://localhost:8501
```

## Uso Local con Ollama

Ollama permite usar modelos en tu computadora sin pagar una API externa.

1. Instala Ollama desde `https://ollama.com`.
2. Verifica que funcione:

```bash
ollama --version
```

3. Descarga al menos un modelo:

```bash
ollama pull llama3.2:3b
```

Modelos locales configurados en `app.py`:

```bash
ollama pull llama3.2:3b
ollama pull qwen2.5:3b
ollama pull phi3:mini
ollama pull gemma2:2b
```

4. Corre la app y selecciona en la barra lateral:

```text
Tipo de ejecucion: Local
Backend: Ollama
```

Tambien puedes abrir la version sencilla solo-local:

```bash
python -m streamlit run app2.py
```

## Uso Remoto con Groq

Groq ofrece inferencia rapida para modelos compatibles con una API tipo OpenAI.

1. Entra a `https://console.groq.com`.
2. Crea una API key.
3. Ejecuta la app:

```bash
python -m streamlit run app.py
```

4. En la barra lateral selecciona:

```text
Tipo de ejecucion: Remoto
Proveedor remoto: Groq
```

5. Pega tu API key en el campo seguro de la interfaz.

## Uso Remoto con Hugging Face

Hugging Face permite usar modelos mediante Inference Providers.

1. Entra a `https://huggingface.co/settings/tokens`.
2. Crea un token de acceso.
3. Asegurate de tener acceso a Inference Providers.
4. Ejecuta la app:

```bash
python -m streamlit run app.py
```

5. En la barra lateral selecciona:

```text
Tipo de ejecucion: Remoto
Proveedor remoto: Hugging Face
```

6. Pega tu token en el campo de la interfaz.

## Modelos Configurados

| Proveedor | Modelos |
| --- | --- |
| Ollama | `llama3.2:3b`, `qwen2.5:3b`, `phi3:mini`, `gemma2:2b` |
| Groq | `openai/gpt-oss-20b`, `openai/gpt-oss-120b`, `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `groq/compound-mini`, `qwen/qwen3-32b` |
| Hugging Face | `openai/gpt-oss-20b:fastest`, `openai/gpt-oss-120b:fastest`, `deepseek-ai/DeepSeek-R1:fastest`, `Qwen/Qwen3-32B:fastest`, `meta-llama/Llama-3.1-8B-Instruct:fastest` |

## Seguridad de Tokens

Nunca subas claves privadas al repositorio.

- No escribas API keys directamente en `app.py`.
- No subas archivos `.env`, `.key`, `.pem` ni `.streamlit/secrets.toml`.
- Pega las claves solo en la interfaz cuando ejecutes la app.
- Si compartes capturas, oculta tus tokens.

## Problemas Comunes

### Streamlit no abre

Instala dependencias otra vez y ejecuta:

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

### Ollama no responde

Revisa que Ollama este activo:

```bash
ollama list
```

Si falta el modelo:

```bash
ollama pull llama3.2:3b
```

### Error de API key

Verifica que:

- La key/token este bien copiada.
- El proveedor seleccionado sea correcto.
- Tu cuenta tenga permisos para el modelo.
- No haya espacios antes o despues del token.

## Preparar y Subir a GitHub

Inicializa Git:

```bash
git init
git add .
git commit -m "Primer commit de AI Studio"
git branch -M main
```

Crea un repositorio nuevo en GitHub y conecta la URL:

```bash
git remote add origin https://github.com/TU_USUARIO/PresentacionLLM.git
git push -u origin main
```

## Comandos Rapidos

```bash
python -m venv .venv
pip install -r requirements.txt
python -m streamlit run app.py
```

Para Ollama:

```bash
ollama pull llama3.2:3b
python -m streamlit run app2.py
```

## Creditos

Proyecto creado para presentar alternativas de uso de LLMs con baja infraestructura:

- Gratis o de bajo costo.
- Locales cuando se usa Ollama.
- Remotas cuando se usan Groq o Hugging Face.
- Faciles de probar desde una interfaz web.

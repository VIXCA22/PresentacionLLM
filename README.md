# AI Studio: LLMs Locales y Remotos

<p align="center">
  <strong>Aplicación web en Streamlit para probar modelos de IA locales y remotos desde una sola interfaz.</strong>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img alt="Ollama" src="https://img.shields.io/badge/Ollama-Local-111111?style=for-the-badge">
  <img alt="Groq" src="https://img.shields.io/badge/Groq-Remoto-F55036?style=for-the-badge">
  <img alt="Hugging Face" src="https://img.shields.io/badge/Hugging%20Face-Remoto-FFD21E?style=for-the-badge">
</p>

---

## Descripción

**AI Studio** es una aplicación web para conversar con modelos de lenguaje usando dos enfoques:

- **Ejecución local:** modelos instalados en la computadora mediante Ollama, sin API key.
- **Ejecución remota:** modelos disponibles mediante Groq o Hugging Face, usando una API key o token.

El objetivo del proyecto es mostrar cómo utilizar LLMs con baja infraestructura, combinando alternativas gratuitas, locales y remotas en una misma experiencia.

La presentación del proyecto está incluida en:

```text
Zero_Infrastructure_LLMs.pptx
```

## Características

| Característica | Descripción |
| --- | --- |
| Chat local | Usa modelos instalados con Ollama en `localhost:11434`. |
| Chat remoto | Permite llamar modelos desde Groq y Hugging Face. |
| Selector de proveedor | Cambia entre Local, Groq y Hugging Face desde la barra lateral. |
| Selector de modelo | Muestra modelos disponibles según el proveedor elegido. |
| Parámetros ajustables | Controla temperatura, top-p y máximo de tokens. |
| Historial de sesión | Conserva la conversación mientras la app está abierta. |
| Markdown y LaTeX | Renderiza texto enriquecido y fórmulas cuando el modelo las devuelve. |

## Estructura del Proyecto

```text
PresentacionLLM/
|-- app.py                         # Aplicación principal
|-- requirements.txt               # Dependencias de Python
|-- Zero_Infrastructure_LLMs.pptx   # Presentación del proyecto
|-- .gitignore                     # Exclusiones para Git
`-- README.md                      # Documentación
```

## Requisitos

Para ejecutar el proyecto necesitas:

- Python 3.10 o superior.
- `pip`, incluido normalmente con Python.
- Ollama, si quieres usar modelos locales.
- Una API key de Groq, si quieres usar Groq.
- Un token de Hugging Face, si quieres usar Hugging Face Inference Providers.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/PresentacionLLM.git
cd PresentacionLLM
```

Si ya tienes la carpeta en tu computadora, entra directamente al proyecto:

```powershell
cd C:\Users\kenne\OneDrive\Documentos\progras\python\PresentacionLLM
```

### 2. Crear y activar un entorno virtual

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

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python -m streamlit run app.py
```

Streamlit abrirá la aplicación en el navegador. Si no se abre automáticamente, entra a:

```text
http://localhost:8501
```

## Uso con Ollama Local

Ollama permite ejecutar modelos en tu computadora sin depender de una API externa.

1. Instala Ollama desde `https://ollama.com`.
2. Verifica la instalación:

```bash
ollama --version
```

3. Descarga al menos un modelo:

```bash
ollama pull llama3.2:3b
```

Modelos locales configurados en la app:

```bash
ollama pull llama3.2:3b
ollama pull qwen2.5:3b
ollama pull phi3:mini
ollama pull gemma2:2b
```

4. Ejecuta la app y selecciona:

```text
Tipo de ejecución: Local
Backend: Ollama
```

## Uso con Groq

Groq permite usar modelos remotos con una API compatible con el formato de chat completions.

1. Entra a `https://console.groq.com`.
2. Crea una API key.
3. Ejecuta la app:

```bash
python -m streamlit run app.py
```

4. En la barra lateral selecciona:

```text
Tipo de ejecución: Remoto
Proveedor remoto: Groq
```

5. Pega tu API key en el campo seguro de la interfaz.

## Uso con Hugging Face

Hugging Face permite usar modelos mediante Inference Providers.

1. Entra a `https://huggingface.co/settings/tokens`.
2. Crea un token de acceso.
3. Confirma que tu cuenta pueda usar Inference Providers.
4. Ejecuta la app:

```bash
python -m streamlit run app.py
```

5. En la barra lateral selecciona:

```text
Tipo de ejecución: Remoto
Proveedor remoto: Hugging Face
```

6. Pega tu token en el campo seguro de la interfaz.

## Modelos Configurados

| Proveedor | Modelos |
| --- | --- |
| Ollama | `llama3.2:3b`, `qwen2.5:3b`, `phi3:mini`, `gemma2:2b` |
| Groq | `openai/gpt-oss-20b`, `openai/gpt-oss-120b`, `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `groq/compound-mini`, `qwen/qwen3-32b` |
| Hugging Face | `openai/gpt-oss-20b:fastest`, `openai/gpt-oss-120b:fastest`, `deepseek-ai/DeepSeek-R1:fastest`, `Qwen/Qwen3-32B:fastest`, `meta-llama/Llama-3.1-8B-Instruct:fastest` |

## Seguridad

Este repositorio no necesita guardar claves privadas.

- No escribas API keys directamente en el código.
- No subas archivos `.env`, `.key`, `.pem` ni `.streamlit/secrets.toml`.
- Pega tus claves solo en la interfaz cuando ejecutes la app.
- Si compartes capturas de pantalla, oculta tus tokens.

## Solución de Problemas

### Streamlit no abre

Reinstala las dependencias y vuelve a ejecutar la app:

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

### Ollama no responde

Verifica que Ollama esté activo y que el modelo exista:

```bash
ollama list
ollama pull llama3.2:3b
```

### Error de API key o token

Revisa que:

- La clave esté bien copiada.
- El proveedor seleccionado sea correcto.
- Tu cuenta tenga permisos para usar el modelo.
- No haya espacios antes o después del token.

## Publicación en GitHub

Si el repositorio todavía no tiene remoto, crea un repositorio vacío en GitHub y conecta la URL:

```bash
git remote add origin https://github.com/TU_USUARIO/PresentacionLLM.git
git push -u origin main
```

Para subir cambios futuros:

```bash
git add .
git commit -m "Actualizar proyecto"
git push
```

## Comandos Rápidos

```bash
python -m venv .venv
pip install -r requirements.txt
python -m streamlit run app.py
```

Para preparar Ollama:

```bash
ollama pull llama3.2:3b
```

## Créditos

Proyecto desarrollado para presentar alternativas prácticas de uso de LLMs:

- Locales con Ollama.
- Remotas con Groq y Hugging Face.
- Accesibles desde una interfaz web con Streamlit.

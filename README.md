# AI Studio: Local and Remote LLMs

<p align="center">
  <strong>A Streamlit web app for testing local and remote AI models from one clean interface.</strong>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img alt="Ollama" src="https://img.shields.io/badge/Ollama-Local-111111?style=for-the-badge">
  <img alt="Groq" src="https://img.shields.io/badge/Groq-Remote-F55036?style=for-the-badge">
  <img alt="Hugging Face" src="https://img.shields.io/badge/Hugging%20Face-Remote-FFD21E?style=for-the-badge">
</p>

<p align="center">
  <a href="#english">English</a> | <a href="#español">Español</a>
</p>

---

## English

## Overview

**AI Studio** is a web application for chatting with large language models through two execution modes:

- **Local execution:** models installed on your own computer through Ollama, with no API key required.
- **Remote execution:** cloud-hosted models through Groq or Hugging Face, using an API key or access token.

The project demonstrates practical ways to use LLMs with low infrastructure requirements, combining free, local, and remote options in a single Streamlit experience.

The project presentation is included as:

```text
Zero_Infrastructure_LLMs.pptx
documento_base_llm_apis_IE0435.pdf
```

## Theoretical Background

This project is based on the connection between classical artificial intelligence concepts and modern large language models:

- **Artificial Intelligence:** computational systems that can recognize patterns, classify data, search for solutions, optimize decisions, or interact through natural language.
- **Machine Learning:** models learn from data instead of relying only on manually written rules.
- **Artificial Neural Networks:** models adjust internal weights to reduce error and improve predictions.
- **Deep Learning:** neural networks with multiple layers can represent more complex relationships and abstractions.
- **Transformers:** modern LLMs are mainly based on transformer architectures, where attention mechanisms help the model identify relevant parts of the input context.
- **Foundation Models:** large pre-trained models can be reused across many tasks without training them from scratch.
- **LLM APIs:** an API allows a program to send prompts, generation parameters, and authentication credentials to a provider and receive generated text back.

The practical focus is to compare low-cost or free options for accessing LLMs through APIs while keeping technical and ethical limitations visible: privacy, hallucinations, provider dependency, rate limits, and responsible use.

## Features

| Feature | Description |
| --- | --- |
| Local chat | Uses Ollama models running on `localhost:11434`. |
| Remote chat | Calls models through Groq and Hugging Face. |
| Provider selector | Switches between Local, Groq, and Hugging Face from the sidebar. |
| Model selector | Shows available models based on the selected provider. |
| Adjustable parameters | Controls temperature, top-p, and maximum tokens. |
| Session history | Keeps the conversation while the Streamlit session is active. |
| Markdown and LaTeX | Renders formatted text and formulas when returned by the model. |

## Project Structure

```text
PresentacionLLM/
|-- app.py                         # Main application
|-- requirements.txt               # Python dependencies
|-- Zero_Infrastructure_LLMs.pptx   # Project presentation
|-- documento_base_llm_apis_IE0435.pdf # Theoretical base document
|-- .gitattributes                 # Binary file handling for Git
|-- .gitignore                     # Git exclusions
`-- README.md                      # Documentation
```

## Requirements

- Python 3.10 or higher.
- `pip`, usually included with Python.
- Ollama, if you want to run local models.
- A Groq API key, if you want to use Groq.
- A Hugging Face token, if you want to use Hugging Face Inference Providers.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/VIXCA22/PresentacionLLM.git
cd PresentacionLLM
```

If the project is already on your computer, go directly to the folder:

```powershell
cd C:\Users\kenne\OneDrive\Documentos\progras\python\PresentacionLLM
```

### 2. Create and activate a virtual environment

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

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python -m streamlit run app.py
```

Streamlit will open the app in your browser. If it does not open automatically, visit:

```text
http://localhost:8501
```

## Using Local Ollama Models

Ollama lets you run models on your own computer without relying on an external API.

1. Install Ollama from `https://ollama.com`.
2. Verify the installation:

```bash
ollama --version
```

3. Pull at least one model:

```bash
ollama pull llama3.2:3b
```

Local models configured in the app:

```bash
ollama pull llama3.2:3b
ollama pull qwen2.5:3b
ollama pull phi3:mini
ollama pull gemma2:2b
```

4. Run the app and select:

```text
Execution type: Local
Backend: Ollama
```

## Using Groq

Groq provides remote model inference through an API compatible with chat completions.

1. Go to `https://console.groq.com`.
2. Create an API key.
3. Run the app:

```bash
python -m streamlit run app.py
```

4. In the sidebar, select:

```text
Execution type: Remote
Remote provider: Groq
```

5. Paste your API key into the secure input field.

## Using Hugging Face

Hugging Face provides model access through Inference Providers.

1. Go to `https://huggingface.co/settings/tokens`.
2. Create an access token.
3. Confirm that your account can use Inference Providers.
4. Run the app:

```bash
python -m streamlit run app.py
```

5. In the sidebar, select:

```text
Execution type: Remote
Remote provider: Hugging Face
```

6. Paste your token into the secure input field.

## Configured Models

| Provider | Models |
| --- | --- |
| Ollama | `llama3.2:3b`, `qwen2.5:3b`, `phi3:mini`, `gemma2:2b` |
| Groq | `openai/gpt-oss-20b`, `openai/gpt-oss-120b`, `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `groq/compound-mini`, `qwen/qwen3-32b` |
| Hugging Face | `openai/gpt-oss-20b:fastest`, `openai/gpt-oss-120b:fastest`, `deepseek-ai/DeepSeek-R1:fastest`, `Qwen/Qwen3-32B:fastest`, `meta-llama/Llama-3.1-8B-Instruct:fastest` |

## Security

This repository does not need to store private keys.

- Do not hard-code API keys in the source code.
- Do not commit `.env`, `.key`, `.pem`, or `.streamlit/secrets.toml` files.
- Paste keys only into the app interface while running locally.
- Hide tokens before sharing screenshots.

## Troubleshooting

### Streamlit does not open

Reinstall dependencies and run the app again:

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

### Ollama does not respond

Check that Ollama is running and that the model exists:

```bash
ollama list
ollama pull llama3.2:3b
```

### API key or token error

Check that:

- The key or token was copied correctly.
- The selected provider is correct.
- Your account has permission to use the selected model.
- There are no extra spaces before or after the token.

## Useful Commands

```bash
python -m venv .venv
pip install -r requirements.txt
python -m streamlit run app.py
```

Prepare Ollama:

```bash
ollama pull llama3.2:3b
```

## AI Tools Used

The project documentation and implementation were supported by generative AI tools. These tools were used as assistants for drafting, comparison, code review, organization of ideas, and documentation polishing. Final technical validation remains the author's responsibility.

| Tool | Use in the project |
| --- | --- |
| ChatGPT | README structuring, installation guidance, code cleanup, Git/GitHub workflow support, and bilingual documentation. |
| Claude | Conceptual review, explanation refinement, comparison of LLM/API alternatives, and wording support. |
| NotebookLM / LLM Notebook | Review and organization of source material, extraction of key ideas from documents, and support for theory synthesis. |

## References

- Coto Jiménez, M. (2026). *Introducción a los Modelos Clásicos de Inteligencia Artificial Aplicada a la Ingeniería Eléctrica*. Universidad de Costa Rica. Course document: `AI.pdf`.
- Universidad de Costa Rica, Escuela de Ingeniería Eléctrica. (2026). *Asignación: Presentación Individual, Tema 11: Opciones gratuitas o de bajo costo para acceder a LLMs a través de APIs*.
- Paddalwar, Y. *How to Access Free Open Source LLMs Like Llama 3 from Hugging Face Using Python API Step-by-Step*. Medium. https://medium.com/@yashpaddalwar/how-to-access-free-open-sourcellms-like-llama-3-from-hugging-face-using-python-api-step-by-step-5da80c98f4e3
- Vaswani, A., et al. (2017). *Attention Is All You Need*. https://arxiv.org/abs/1706.03762
- Hugging Face. *Inference Providers documentation*. https://huggingface.co/docs/inference-providers/en/index
- Groq. *GroqCloud and pricing information*. https://groq.com/groqcloud and https://groq.com/pricing
- Google AI for Developers. *Gemini API quickstart*. https://ai.google.dev/gemini-api/docs/quickstart
- Together AI. *Pricing*. https://www.together.ai/pricing
- Together AI Docs. *Serverless models*. https://docs.together.ai/docs/serverless-models
- Anthropic. *Claude*. https://www.anthropic.com/claude
- Google. *NotebookLM Help*. https://support.google.com/notebooklm/answer/16164461
- OpenAI. *What is ChatGPT?* https://help.openai.com/en/articles/6783457-what-is-chatgpt

---

## Español

## Descripción

**AI Studio** es una aplicación web para conversar con modelos de lenguaje usando dos enfoques:

- **Ejecución local:** modelos instalados en la computadora mediante Ollama, sin API key.
- **Ejecución remota:** modelos disponibles mediante Groq o Hugging Face, usando una API key o token.

El objetivo del proyecto es mostrar cómo utilizar LLMs con baja infraestructura, combinando alternativas gratuitas, locales y remotas en una misma experiencia.

La presentación del proyecto está incluida en:

```text
Zero_Infrastructure_LLMs.pptx
documento_base_llm_apis_IE0435.pdf
```

## Base Teórica

Este proyecto se apoya en la relación entre conceptos clásicos de inteligencia artificial y los modelos grandes de lenguaje modernos:

- **Inteligencia artificial:** sistemas computacionales capaces de reconocer patrones, clasificar datos, buscar soluciones, optimizar decisiones o interactuar mediante lenguaje natural.
- **Aprendizaje automático:** modelos que aprenden a partir de datos en lugar de depender solo de reglas escritas manualmente.
- **Redes neuronales artificiales:** modelos que ajustan pesos internos para reducir error y mejorar predicciones.
- **Deep learning:** redes con múltiples capas que permiten representar relaciones y abstracciones más complejas.
- **Transformers:** arquitectura dominante en LLMs modernos; usa mecanismos de atención para identificar partes relevantes del contexto.
- **Modelos fundacionales:** modelos grandes preentrenados que pueden reutilizarse en muchas tareas sin entrenarlos desde cero.
- **APIs de LLMs:** una API permite enviar prompts, parámetros de generación y credenciales a un proveedor para recibir texto generado por el modelo.

El enfoque práctico consiste en comparar opciones gratuitas o de bajo costo para acceder a LLMs mediante APIs, manteniendo visibles sus límites técnicos y éticos: privacidad, alucinaciones, dependencia del proveedor, límites de uso y responsabilidad en resultados técnicos.

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
|-- documento_base_llm_apis_IE0435.pdf # Documento base teórico
|-- .gitattributes                 # Manejo de archivos binarios en Git
|-- .gitignore                     # Exclusiones para Git
`-- README.md                      # Documentación
```

## Requisitos

- Python 3.10 o superior.
- `pip`, incluido normalmente con Python.
- Ollama, si quieres usar modelos locales.
- Una API key de Groq, si quieres usar Groq.
- Un token de Hugging Face, si quieres usar Hugging Face Inference Providers.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/VIXCA22/PresentacionLLM.git
cd PresentacionLLM
```

Si ya tienes la carpeta en tu computadora:

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

Si Streamlit no abre el navegador automáticamente, entra a:

```text
http://localhost:8501
```

## Uso con Ollama Local

Ollama permite ejecutar modelos en tu computadora sin depender de una API externa.

```bash
ollama --version
ollama pull llama3.2:3b
```

Modelos locales configurados en la app:

```bash
ollama pull llama3.2:3b
ollama pull qwen2.5:3b
ollama pull phi3:mini
ollama pull gemma2:2b
```

En la app selecciona:

```text
Tipo de ejecución: Local
Backend: Ollama
```

## Uso con Groq

1. Entra a `https://console.groq.com`.
2. Crea una API key.
3. Ejecuta la app.
4. Selecciona `Remoto` y luego `Groq`.
5. Pega tu API key en el campo seguro de la interfaz.

## Uso con Hugging Face

1. Entra a `https://huggingface.co/settings/tokens`.
2. Crea un token de acceso.
3. Confirma que tu cuenta pueda usar Inference Providers.
4. Ejecuta la app.
5. Selecciona `Remoto` y luego `Hugging Face`.
6. Pega tu token en el campo seguro de la interfaz.

## Seguridad

- No escribas API keys directamente en el código.
- No subas archivos `.env`, `.key`, `.pem` ni `.streamlit/secrets.toml`.
- Pega tus claves solo en la interfaz cuando ejecutes la app.
- Oculta tus tokens antes de compartir capturas de pantalla.

## Solución de Problemas

### Streamlit no abre

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

### Ollama no responde

```bash
ollama list
ollama pull llama3.2:3b
```

### Error de API key o token

Revisa que la clave esté bien copiada, que el proveedor seleccionado sea correcto y que tu cuenta tenga permisos para usar el modelo.

## Herramientas de IA Utilizadas

La documentación y la implementación del proyecto fueron apoyadas por herramientas de IA generativa. Estas herramientas se usaron como asistentes para redacción, comparación, revisión de código, organización de ideas y mejora de documentación. La validación técnica final sigue siendo responsabilidad del autor.

| Herramienta | Uso en el proyecto |
| --- | --- |
| ChatGPT | Estructura del README, guía de instalación, limpieza del código, flujo Git/GitHub y documentación bilingüe. |
| Claude | Revisión conceptual, mejora de explicaciones, comparación de alternativas LLM/API y apoyo de redacción. |
| NotebookLM / LLM Notebook | Revisión y organización de material fuente, extracción de ideas clave desde documentos y apoyo para sintetizar teoría. |

## Referencias

- Coto Jiménez, M. (2026). *Introducción a los Modelos Clásicos de Inteligencia Artificial Aplicada a la Ingeniería Eléctrica*. Universidad de Costa Rica. Documento del curso: `AI.pdf`.
- Universidad de Costa Rica, Escuela de Ingeniería Eléctrica. (2026). *Asignación: Presentación Individual, Tema 11: Opciones gratuitas o de bajo costo para acceder a LLMs a través de APIs*.
- Paddalwar, Y. *How to Access Free Open Source LLMs Like Llama 3 from Hugging Face Using Python API Step-by-Step*. Medium. https://medium.com/@yashpaddalwar/how-to-access-free-open-sourcellms-like-llama-3-from-hugging-face-using-python-api-step-by-step-5da80c98f4e3
- Vaswani, A., et al. (2017). *Attention Is All You Need*. https://arxiv.org/abs/1706.03762
- Hugging Face. *Inference Providers documentation*. https://huggingface.co/docs/inference-providers/en/index
- Groq. *GroqCloud and pricing information*. https://groq.com/groqcloud and https://groq.com/pricing
- Google AI for Developers. *Gemini API quickstart*. https://ai.google.dev/gemini-api/docs/quickstart
- Together AI. *Pricing*. https://www.together.ai/pricing
- Together AI Docs. *Serverless models*. https://docs.together.ai/docs/serverless-models
- Anthropic. *Claude*. https://www.anthropic.com/claude
- Google. *NotebookLM Help*. https://support.google.com/notebooklm/answer/16164461
- OpenAI. *What is ChatGPT?* https://help.openai.com/en/articles/6783457-what-is-chatgpt

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo [`LICENSE`](LICENSE) para más detalles.

## Créditos

Proyecto desarrollado para presentar alternativas prácticas de uso de LLMs:

- Locales con Ollama.
- Remotas con Groq y Hugging Face.
- Accesibles desde una interfaz web con Streamlit.

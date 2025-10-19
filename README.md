# Global Earthquake and Tsunami Data Analysis App

🌊 Vulcans: Sistema Inteligente de Análisis de Terremotos y Tsunamis

Bienvenido al repositorio Vulcans, un proyecto integral para el análisis, visualización y monitoreo de eventos sísmicos y tsunamis a nivel global. Este sistema combina ciencia de datos, visualización avanzada y desarrollo web para ofrecer una herramienta interactiva y escalable, útil tanto para expertos como para usuarios sin conocimientos técnicos.

---

## 📦 Estructura del Proyecto

```bash
├── app/         # Aplicación Streamlit (dashboard interactivo)
│   ├── main.py
│   ├── requirements.txt
│   ├── README.md
│   ├── components/
│   └── utils/
├── data/        # Datos fuente (CSV)
│   └── earthquake_data_tsunami.csv
├── docs/        # Documentación y análisis exploratorio
│   ├── eda.md
│   └── info.md
├── notebook/    # Jupyter Notebooks para EDA y preparación
│   ├── eda.ipynb
│   └── prep.ipynb
└── README.md    # Portada principal del repositorio
```

---

## 🚀 Descripción General

Vulcans es una plataforma de inteligencia sísmica que permite:

- Analizar patrones y correlaciones entre terremotos y tsunamis
- Identificar zonas de alto riesgo y tendencias temporales
- Visualizar datos geoespaciales y multivariables
- Facilitar la toma de decisiones y la comunicación de riesgos

El sistema está diseñado para ser modular, escalable y fácil de mantener, integrando las mejores prácticas de desarrollo en Python y Streamlit.

---

## 🧩 Componentes Clave

### 1. Datos

- **Fuente:** `data/earthquake_data_tsunami.csv` (eventos sísmicos y tsunamis globales)
- **Variables:** Magnitud, profundidad, año, mes, significancia, impacto comunitario, calidad del monitoreo, etc.

### 2. Análisis Exploratorio (EDA)

- **Notebooks:** `notebook/eda.ipynb`, `notebook/prep.ipynb`
- **Documentación:** `docs/eda.md` con storytelling, hallazgos y recomendaciones

### 3. Dashboard Interactivo

- **Streamlit:** Carpeta `app/` con componentes modulares
- **Visualizaciones:** Mapas globales, análisis de correlaciones, gráficos 3D, tendencias temporales
- **Filtros:** Por año, magnitud, profundidad, tipo de evento

### 4. Documentación

- **Guía técnica y narrativa:** `docs/eda.md` y `docs/info.md`
- **README:** Explicación funcional y técnica del proyecto

---

## 📊 Funcionalidades Destacadas

- Mapas interactivos de terremotos y tsunamis
- Matriz de correlaciones y análisis multivariable
- Tendencias históricas y patrones estacionales
- Filtros dinámicos y métricas clave
- Panel modular y escalable para futuras integraciones (ML, alertas, etc.)

---

## 🛠️ Instalación y Ejecución

1. Clona el repositorio:

    ```bash
    git clone https://github.com/[usuario]/Vulcans.git
    cd Vulcans
    ```

2. Instala las dependencias:

    ```bash
    pip install -r app/requirements.txt
    ```

3. Ejecuta el dashboard:

    ```bash
    cd app
    streamlit run main.py
    ```

---

## 📈 Futuras Expansiones

- Modelos de Machine Learning para predicción de tsunamis
- Integración con fuentes de datos en tiempo real
- Paneles personalizados para diferentes perfiles de usuario
- Exportación y reporte automatizado

---

## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue para sugerencias o mejoras antes de enviar un pull request.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## 👥 Créditos y Agradecimientos

- USGS por los datos sísmicos
- Comunidad Streamlit y Python
- Equipo Vulcans y colaboradores

---

# 🌊 Dashboard de Análisis Sísmico y Tsunamis

## 📋 Descripción de la Aplicación

Esta aplicación Streamlit proporciona una interfaz interactiva para el análisis y visualización de datos sísmicos globales. Está diseñada para facilitar la exploración de patrones en eventos sísmicos y su relación con la generación de tsunamis.

## 🏗️ Estructura de la Aplicación

```bash
app/
├── components/           # Componentes modulares de la interfaz
│   ├── analytics.py     # Análisis de correlaciones y multivariable
│   ├── maps.py         # Visualizaciones geoespaciales
│   ├── sidebar.py      # Filtros y controles interactivos
│   └── temporal.py     # Análisis de series temporales
├── utils/              # Utilidades y funciones auxiliares
│   ├── data_loader.py  # Carga y procesamiento de datos
│   └── styling.py      # Estilos personalizados
├── main.py            # Punto de entrada principal
└── README.md          # Este archivo
```

## 🔧 Componentes Principales

### 1. Main (`main.py`)

- Punto de entrada de la aplicación
- Configura la página y el diseño general
- Integra todos los componentes
- Maneja el flujo de datos entre componentes

### 2. Componentes (`components/`)

#### Sidebar (`sidebar.py`)

- Filtros interactivos para:
  - Rango de años
  - Rango de magnitud
  - Rango de profundidad
  - Filtro de tsunamis
- Resumen de filtros aplicados

#### Maps (`maps.py`)

- Mapa global de terremotos
- Mapa de tsunamis vs profundidad
- Visualización de zonas de alto riesgo
- Mapas interactivos con Plotly

#### Analytics (`analytics.py`)

- Matriz de correlaciones
- Análisis multivariable
- Gráficos 3D
- Distribuciones estadísticas

#### Temporal (`temporal.py`)

- Análisis de tendencias temporales
- Evolución de magnitudes
- Patrones estacionales
- Visualización de series temporales

### 3. Utilidades (`utils/`)

#### Data Loader (`data_loader.py`)

- Carga del dataset
- Preprocesamiento de datos
- Validación de tipos de datos
- Gestión de valores nulos

#### Styling (`styling.py`)

- Estilos CSS personalizados
- Temas y colores coherentes
- Mejoras de UX/UI
- Diseño responsivo

## 🚀 Cómo Ejecutar la Aplicación

1. **Preparar el Entorno**

```bash
# Crear y activar entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

2. **Ejecutar la Aplicación**

```bash
streamlit run main.py
```

## 📊 Características Principales

### Visualizaciones

- Mapas interactivos globales
- Gráficos de correlación
- Análisis 3D
- Series temporales animadas

### Interactividad

- Filtros dinámicos
- Zoom y selección en mapas
- Tooltips informativos
- Actualización en tiempo real

### Análisis

- Correlaciones estadísticas
- Patrones geoespaciales
- Tendencias temporales
- Distribuciones de variables

## 🛠️ Dependencias Principales

- `streamlit`: Framework principal
- `pandas`: Manipulación de datos
- `plotly`: Visualizaciones interactivas
- `numpy`: Operaciones numéricas
- `seaborn`: Visualizaciones estadísticas

## 🔄 Flujo de Datos

1. Carga inicial desde CSV
2. Preprocesamiento en `data_loader.py`
3. Filtrado en `sidebar.py`
4. Distribución a componentes
5. Actualización reactiva de visualizaciones

## 🎨 Diseño UI/UX

- Tema oscuro/claro
- Paleta de colores coherente
- Diseño responsivo
- Navegación intuitiva
- Mensajes informativos claros

## 📈 Rendimiento

- Optimización de carga de datos
- Caché de componentes pesados
- Paginación donde sea necesario
- Gestión eficiente de memoria

## 🔍 Depuración

Para modo debug:

```bash

streamlit run main.py -- --debug
```

## 🤝 Contribución al Desarrollo

1. Seguir estilo de código PEP 8
2. Documentar nuevas funciones
3. Actualizar README si es necesario
4. Testear en diferentes navegadores

---

📫 Para más información sobre el proyecto completo, consultar el [README principal](../README.md)

# 🚗 Análisis Exploratorio de Datos - Dataset Uber

## 📋 Descripción del Proyecto

Este proyecto realiza un análisis exploratorio exhaustivo del dataset de reservas de Uber con el objetivo de **predecir el porcentaje de cancelación** de viajes basado en diferentes parámetros.

## 🎯 Objetivos

1. **Explorar** la estructura y calidad de los datos
2. **Identificar** patrones en las cancelaciones de viajes  
3. **Analizar** correlaciones entre variables
4. **Preparar** los datos para modelado predictivo

## 📊 Dataset

- **Archivo**: `ncr_ride_bookings.csv`
- **Registros**: 150,000 reservas de viajes
- **Variables**: 21 columnas con información:
  - Temporal (fecha, hora)
  - Geográfica (pickup, drop location) 
  - Operacional (tipo de vehículo, tiempos de espera)
  - Financiera (valor del viaje, distancia)
  - Calidad (ratings de conductor y cliente)

## 🔍 Hallazgos Principales

### ⚡ Tasa de Cancelación General: **38.0%**
- 57,000 de 150,000 reservas fueron canceladas
- Tasa considerablemente alta para la industria

### 🚗 Principales Causas de Cancelación:
- **Cancelado por conductor**: 47.4% de las cancelaciones
- **Sin conductor encontrado**: 18.4% de las cancelaciones  
- **Cancelado por cliente**: 18.4% de las cancelaciones
- **Viajes incompletos**: 15.8% de las cancelaciones

### ⏰ Patrones Temporales:
- **Poca variación horaria**: diferencia de solo 2.8 puntos porcentuales entre hora pico y valle
- **Consistencia temporal** sugiere factores estructurales más que circunstanciales

### 🔗 Correlaciones Clave:
- **Avg CTAT** (tiempo de llegada del cliente): -0.320 correlación con cancelaciones
- **Ride Distance** (distancia del viaje): -0.313 correlación con cancelaciones
- **A mayor distancia y tiempo → menor probabilidad de cancelación**

## 📁 Estructura del Proyecto

```
├── ncr_ride_bookings.csv           # Dataset principal
├── hola_mundo.ipynb                # Notebook principal de análisis
├── uber_analysis.py                # Script de análisis básico
├── uber_analysis_part2.py          # Script de análisis visual  
├── uber_analysis_summary.py        # Script de resumen ejecutivo
├── uber_analysis_overview.png      # Gráficos principales
├── correlation_matrix.png          # Matriz de correlaciones
├── cdd/                           # Entorno virtual Python
└── README.md                      # Este archivo
```

## 🚀 Cómo Ejecutar

### 1. Configurar Entorno
```bash
# Activar entorno virtual
source cdd/bin/activate

# Verificar dependencias
python test_notebook.py
```

### 2. Ejecutar Análisis

**Opción A: Notebook Interactivo (Recomendado)**
```bash
jupyter notebook hola_mundo.ipynb
```

**Opción B: Scripts Python**
```bash
python uber_analysis.py                # Análisis básico
python uber_analysis_part2.py          # Análisis visual
python uber_analysis_summary.py        # Resumen ejecutivo
```

## 📊 Contenido del Notebook

### 1. 📦 Setup e Importación de Librerías
- Configuración del entorno de análisis
- Importación de pandas, matplotlib, seaborn

### 2. 📂 Carga y Exploración Básica
- Carga del dataset (150K registros, 21 columnas)
- Análisis de tipos de datos y valores faltantes
- Estadísticas descriptivas

### 3. 🧹 Limpieza y Preparación de Datos  
- Conversión de fechas y tiempos
- Extracción de características temporales
- Creación de variable objetivo (Is_Cancelled)

### 4. 📊 Análisis Exploratorio Visual
- Distribución de estados de booking
- Patrones temporales (cancelaciones por hora)
- Análisis por tipo de vehículo
- Análisis de métodos de pago

### 5. 🔗 Análisis de Correlaciones
- Matriz de correlación para variables numéricas
- Gráficos de dispersión para correlaciones significativas
- Identificación de variables predictivas

### 6. 💡 Insights y Conclusiones
- Resumen ejecutivo de hallazgos
- Identificación de factores clave
- Alertas y oportunidades detectadas

### 7. 🚀 Preparación para Modelado
- Variables candidatas identificadas
- Ingeniería de características sugerida
- Recomendaciones para próximos pasos

## 📈 Variables Clave Identificadas

### 🕐 Temporales
- Hour, DayOfWeek, Month, DayOfMonth
- Is_Weekend, Is_Peak_Hour (derivadas)

### 🏷️ Categóricas  
- Vehicle Type, Payment Method
- Pickup Location, Drop Location

### 📊 Numéricas Relevantes
- Avg CTAT, Avg VTAT
- Booking Value, Ride Distance
- Driver Ratings, Customer Rating

## ⚠️ Desafíos Identificados

1. **Datos Faltantes**: 80-90% de valores nulos en variables específicas de cancelación
2. **Correlaciones Débiles**: Variables numéricas con correlaciones < 0.35
3. **Alta Cardinalidad**: Ubicaciones con muchas categorías únicas
4. **Balanceamiento**: 38% cancelaciones vs 62% completadas

## 🔮 Próximos Pasos Recomendados

### 🧹 Preprocesamiento
- Imputación inteligente de valores faltantes
- Codificación de variables categóricas
- Normalización de variables numéricas
- Agrupación geográfica de ubicaciones

### 🎨 Ingeniería de Características
- Variables temporales avanzadas (estaciones, festividades)
- Distancias euclidianas entre ubicaciones
- Ratios derivados (precio/km, tiempo relativo)
- Agregaciones por zona geográfica

### 🤖 Modelado
- Algoritmos sugeridos: Random Forest, XGBoost, Logistic Regression
- Validación cruzada estratificada
- Optimización de hiperparámetros
- Análisis de importancia de características

### 📊 Evaluación
- Métricas: Precision, Recall, F1-Score, AUC-ROC
- Matriz de confusión detallada
- Análisis de casos límite y errores

## 💻 Dependencias

- Python 3.11+
- pandas 2.3.2
- numpy 2.3.2  
- matplotlib 3.10.6
- seaborn 0.13.2
- jupyter (opcional, para notebooks)

## 👥 Equipo

Proyecto de Ciencia de Datos - Análisis Predictivo de Cancelaciones Uber

---

**Estado**: ✅ Análisis Exploratorio Completado  
**Siguiente Fase**: 🤖 Modelado Predictivo  
**Última Actualización**: Septiembre 2025
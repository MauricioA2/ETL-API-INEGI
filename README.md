# ⛽ Gasoline Prices ETL Dashboard

Este proyecto implementa un pipeline de ETL en Python que descarga, transforma y almacena semanalmente los precios promedio nacionales de gasolina y diésel en México usando la API del INEGI. Los datos limpios se almacenan en una base de datos SQLite para ser visualizados en un dashboard interactivo (Power BI o Tableau).

---

## 📌 Objetivo

Simular un flujo de trabajo real de analista o ingeniero de datos:
- Extracción de datos desde una API pública (INEGI)
- Limpieza y transformación con pandas
- Persistencia en base de datos local
- Visualización profesional
- Automatización semanal

---

## 🧰 Tecnologías usadas

- Python 3.10+
- SQLite
- pandas, requests, python-dotenv
- Power BI o Tableau
- Git (estructura colaborativa simulada)
- `schedule`, `cron` o Airflow para automatización

---

## 🚀 Instalación y uso

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/gasoline-etl.git
cd gasoline-etl

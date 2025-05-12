from src.api_client import InegiAPIClient
from src.transformer import DataTransformer
from src.db_manager import DatabaseManager

def run_etl():
    series = {
        "magna": "493621",
        "premium": "493623",
        "diesel": "493625"
    }

    # 1. Extraer
    client = InegiAPIClient(series)
    raw_data = client.fetch_all()

    # 2. Transformar
    transformer = DataTransformer(raw_data)
    clean_df = transformer.transform()

    # 3. Guardar
    db = DatabaseManager()
    db.save_dataframe(clean_df)

    print("ETL ejecutado correctamente.")

if __name__ == '__main__':
    run_etl()
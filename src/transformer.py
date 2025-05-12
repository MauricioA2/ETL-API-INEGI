import pandas as pd

class DataTransformer:
    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    def transform(self):
        frames = []

        for fuel_type, data in self.raw_data.items():
            observations = data['Series'][0]['OBSERVATIONS']
            df = pd.DataFrame(observations)
            df['Fecha'] = pd.to_datetime(df['TIME_PERIOD'])
            df['Precio'] = pd.to_numeric(df['OBS_VALUE'], errors='coerce')
            df['Combustible'] = fuel_type
            frames.append(df[['Fecha', 'Precio', 'Combustible']])

        result = pd.concat(frames).sort_values(by='Fecha')
        return result.reset_index(drop=True)

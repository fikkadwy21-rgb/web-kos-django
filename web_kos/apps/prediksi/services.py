from pathlib import Path
import joblib
import pandas as pd
from django.conf import settings

MODEL_PATH = Path(settings.BASE_DIR) / "dataset" / "model_kos.joblib"
DATASET_PATH = Path(settings.BASE_DIR) / "dataset" / "kos_madiun.csv"

_model = None

def get_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def prediksi_harga_kos(jarak_km: float, rating: float, ac: str) -> float:
    model = get_model()
    ac_num = 1 if ac.lower() == "ya" else 0
    
    data_baru = pd.DataFrame({
        "jarak_km": [jarak_km],
        "rating": [rating],
        "ac_num": [ac_num],
    })
    
    hasil = model.predict(data_baru)[0]
    return round(float(hasil), 1)

def get_statistik_ac() -> dict:
    df = pd.read_csv(DATASET_PATH)
    rata_rata = df.groupby("ac")["harga"].mean().round(1).to_dict()
    return {
        "labels": list(rata_rata.keys()),
        "values": list(rata_rata.values()),
    }

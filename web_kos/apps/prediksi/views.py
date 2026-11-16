from django.shortcuts import render
from .services import prediksi_harga_kos, get_statistik_ac

def index(request):
    hasil_prediksi = None
    input_user = {
        "jarak_km": 1.0,
        "rating": 4.0,
        "ac": "ya",
    }

    if request.method == "POST":
        jarak_km = float(request.POST.get("jarak_km", 1.0))
        rating = float(request.POST.get("rating", 4.0))
        ac = request.POST.get("ac", "tidak")

        input_user = {
            "jarak_km": jarak_km,
            "rating": rating,
            "ac": ac,
        }
        hasil_prediksi = prediksi_harga_kos(jarak_km, rating, ac)

    statistik_ac = get_statistik_ac()

    context = {
        "hasil_prediksi": hasil_prediksi,
        "input_user": input_user,
        "chart_labels": statistik_ac["labels"],
        "chart_values": statistik_ac["values"],
    }
    return render(request, "prediksi/index.html", context)

document.addEventListener("DOMContentLoaded", function () {
    const labels = JSON.parse(document.getElementById("ac-labels").textContent);
    const values = JSON.parse(document.getElementById("ac-values").textContent);

    const ctx = document.getElementById("acChart").getContext("2d");
    new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels.map(l => "AC: " + l.toUpperCase()),
            datasets: [{
                label: "Rata-rata Harga (Ribu Rp)",
                data: values,
                backgroundColor: ["#2563eb", "#94a3b8"],
                borderRadius: 6
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
});

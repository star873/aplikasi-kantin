from flask import Flask, render_template, request

app = Flask(__name__)

menu = {
    "Nasi Goreng": 12000,
    "Mie Ayam": 10000,
    "Bakso": 13000,
    "Es Teh": 3000,
    "Capuccino": 5000
}

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None

    if request.method == "POST":
        nama = request.form["nama"]
        item = request.form["menu"]
        jumlah = int(request.form["jumlah"])
        bayar = int(request.form["bayar"])

        harga = menu[item]
        total = harga * jumlah
        kembalian = bayar - total

        hasil = {
            "nama": nama,
            "item": item,
            "jumlah": jumlah,
            "harga": harga,
            "total": total,
            "bayar": bayar,
            "kembalian": kembalian
        }

    return render_template("index.html", menu=menu, hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
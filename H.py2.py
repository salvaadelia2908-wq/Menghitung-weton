import tkinter as tk
from tkinter import ttk

# ====== Data Hari dan Pasaran beserta Nilai Neptu ======
hari_data = {
    "Senin": 4,
    "Selasa": 3,
    "Rabu": 7,
    "Kamis": 8,
    "Jumat": 6,
    "Sabtu": 9,
    "Minggu": 5
}

pasaran_data = {
    "Legi": 5,
    "Pahing": 9,
    "Pon": 7,
    "Wage": 4,
    "Kliwon": 8
}

# ====== Fungsi Hitung Weton ======
def hitung_weton():
    hari = combo_hari.get()
    pasaran = combo_pasaran.get()

    if hari and pasaran:
        neptu_hari = hari_data[hari]
        neptu_pasaran = pasaran_data[pasaran]
        total_neptu = neptu_hari + neptu_pasaran

        hasil_label.config(
            text=(
                f"Weton Anda: {hari} {pasaran}\n\n"
                f"🔸 Nilai Neptu Hari ({hari}): {neptu_hari}\n"
                f"🔸 Nilai Neptu Pasaran ({pasaran}): {neptu_pasaran}\n"
                f"💖 Total Neptu: {total_neptu}"
            ),
            fg="#800040"
        )
    else:
        hasil_label.config(text="⚠️ Silakan pilih hari dan pasaran terlebih dahulu!", fg="red")

# ====== Fungsi Reset ======
def reset_input():
    combo_hari.set('')
    combo_pasaran.set('')
    hasil_label.config(text="")

# ====== GUI Setup ======
window = tk.Tk()
window.title("🌸 Aplikasi Hitung Weton Jawa 🌸")
window.geometry("450x450")
window.config(bg="#ffc0cb")  # Warna pink lembut

# ====== Judul ======
judul = tk.Label(
    window,
    text="🪶 Perhitungan Weton Jawa 🪶",
    bg="#ffc0cb",
    fg="#800040",
    font=("Helvetica", 16, "bold")
)
judul.pack(pady=15)

# ====== Pilihan Hari ======
label_hari = tk.Label(window, text="Pilih Hari:", bg="#ffc0cb", fg="#800040", font=("Arial", 12, "bold"))
label_hari.pack(pady=5)

combo_hari = ttk.Combobox(window, values=list(hari_data.keys()), font=("Arial", 12), state="readonly", width=15)
combo_hari.pack(pady=5)

# ====== Pilihan Pasaran ======
label_pasaran = tk.Label(window, text="Pilih Pasaran:", bg="#ffc0cb", fg="#800040", font=("Arial", 12, "bold"))
label_pasaran.pack(pady=5)

combo_pasaran = ttk.Combobox(window, values=list(pasaran_data.keys()), font=("Arial", 12), state="readonly", width=15)
combo_pasaran.pack(pady=5)

# ====== Tombol Hitung ======
hitung_button = tk.Button(
    window,
    text="Hitung Weton 💫",
    command=hitung_weton,
    bg="#ff69b4",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="raised",
    padx=10,
    pady=5
)
hitung_button.pack(pady=15)

# ====== Tombol Reset ======
reset_button = tk.Button(
    window,
    text="Reset 🔄",
    command=reset_input,
    bg="#ffb6c1",
    fg="#800040",
    font=("Arial", 10, "bold"),
    relief="ridge",
    padx=8,
    pady=4
)
reset_button.pack()

# ====== Label Hasil ======
hasil_label = tk.Label(window, text="", bg="#ffc0cb", font=("Arial", 13, "bold"), justify="left")
hasil_label.pack(pady=25)

# ====== Jalankan GUI ======
window.mainloop()

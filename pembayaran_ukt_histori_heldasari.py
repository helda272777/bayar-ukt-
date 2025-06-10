
import tkinter as tk
from tkinter import messagebox
import sqlite3
import atexit

# Koneksi ke database SQLite
conn = sqlite3.connect("pembayaran_ukt.db")
cursor = conn.cursor()

# Buat tabel histori jika belum ada
cursor.execute("""
    CREATE TABLE IF NOT EXISTS histori_pembayaran (
        nim TEXT,
        nominal INTEGER,
        kode_va TEXT
    )
""")
conn.commit()

# Fungsi Login
def login_keedlink():
    nim = nim_entry.get()
    password = password_entry.get()

    if nim.strip() == "" or password.strip() == "":
        messagebox.showwarning("Login Gagal", "NIM dan password tidak boleh kosong.")
        return

    # Login berhasil
    login_frame.pack_forget()
    tagihan_frame.pack()

    nominal = 1480000
    kode_va = "1234567890"

    nominal_label.config(text=f"Nominal: Rp {nominal:,}")
    kode_va_label.config(text=f"Kode VA: {kode_va}")

    # Simpan histori ke database
    cursor.execute("INSERT INTO histori_pembayaran (nim, nominal, kode_va) VALUES (?, ?, ?)", 
                   (nim, nominal, kode_va))
    conn.commit()

    messagebox.showinfo("Login Sukses", f"Selamat datang, NIM {nim}!")

    # Tampilkan histori setelah login
    lihat_histori()

# Fungsi Pembayaran
def bayar_mbanking():
    messagebox.showinfo("Bayar m-Banking", "Buka aplikasi m-Banking dan masukkan Kode VA.")

# Fungsi Cek Status
def cek_status():
    messagebox.showinfo("Status Pembayaran", "Pembayaran berhasil dikonfirmasi.")

# Fungsi Lihat Histori
def lihat_histori():
    histori_window = tk.Toplevel(root)
    histori_window.title("Histori Pembayaran")
    histori_window.geometry("400x300")

    text_area = tk.Text(histori_window, wrap="word")
    scrollbar = tk.Scrollbar(histori_window, command=text_area.yview)
    text_area.config(yscrollcommand=scrollbar.set)

    text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    cursor.execute("SELECT * FROM histori_pembayaran")
    histori = cursor.fetchall()
    if not histori:
        text_area.insert(tk.END, "Belum ada histori pembayaran.")
    else:
        for data in histori:
            text_area.insert(tk.END, f"NIM: {data[0]}\nNominal: Rp {data[1]:,}\nKode VA: {data[2]}\n\n")

# Tutup koneksi saat keluar
atexit.register(lambda: conn.close())

# GUI Setup
root = tk.Tk()
root.title("Pembayaran UKT")
root.geometry("400x450")

# Judul
tk.Label(root, text="Pembayaran UKT menggunakan edlink", font=("Arial", 14, "bold"), wraplength=350, justify="center", bg="#416010", fg="#333").pack(pady=10)

# Frame Login
login_frame = tk.Frame(root, bg="#70864B", padx=5, pady=5)
tk.Label(login_frame, text="Login Edlink", font=("Arial", 10, "bold")).pack()
tk.Label(login_frame, text="NIM:").pack(padx=3, pady=3)
nim_entry = tk.Entry(login_frame)
nim_entry.pack(padx=3, pady=3)
tk.Label(login_frame, text="Password:").pack(padx=3, pady=3)
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack(padx=3, pady=3)
tk.Button(login_frame, text="Login", command=login_keedlink).pack(pady=3)
login_frame.pack(padx=5, pady=5)

# Frame Tagihan
tagihan_frame = tk.Frame(root)
nominal_label = tk.Label(tagihan_frame, text="Nominal: -")
nominal_label.pack(padx=3, pady=3)
kode_va_label = tk.Label(tagihan_frame, text="Kode VA: -")
kode_va_label.pack(padx=3, pady=3)

tk.Button(tagihan_frame, text="Bayar via m-Banking", command=bayar_mbanking).pack(padx=20)
tk.Button(tagihan_frame, text="Cek Status Pembayaran", command=cek_status).pack(pady=10)
tk.Button(tagihan_frame, text="Lihat Histori Pembayaran", command=lihat_histori).pack(pady=5)

# Sembunyikan tagihan_frame di awal
tagihan_frame.pack_forget()

# Jalankan aplikasi
root.mainloop()

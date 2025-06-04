import tkinter as tk
from tkinter import messagebox

def login_keedlink():
    nim = nim_entry.get()
    password = password_entry.get()
    
    if nim.strip() == "" or password.strip() == "" :
        messagebox.showwarning("Login Gagal", "NIM dan password tidak boleh kosong.")
        return
    
    # Tidak ada validasi khusus, siapa pun bisa login
    login_frame.pack_forget()
    tagihan_frame.pack()
    nominal_label.config(text="Nominal: Rp 1.480.000")
    kode_va_label.config(text="Kode VA: 1234567890")
    messagebox.showinfo("Login Sukses", f"Selamat datang, NIM {nim}!")

def bayar_mbanking():
    messagebox.showinfo("Bayar m-Banking", "Buka aplikasi m-Banking dan masukkan Kode VA.")

def cek_status():
    messagebox.showinfo("Status Pembayaran", "Pembayaran berhasil dikonfirmasi.")

# GUI Setup
root = tk.Tk()
root.title("Pembayaran UKT")
root.geometry("400x450")

# Judul
tk.Label(root, text="Pembayaran UKT menggunakan edlink", font=("Arial", 14, "bold"), wraplength=350, justify="center",bg="#416010", fg="#333").pack(pady=10)

# Frame Login
login_frame = tk.Frame(root,bg="#70864B", padx=5, pady=5)
tk.Label(login_frame, text="Login Edlink", font=("Arial", 10, "bold")).pack()
tk.Label(login_frame, text="NIM:").pack(padx=3, pady=3)
nim_entry = tk.Entry(login_frame)
nim_entry.pack(padx=3, pady=3)
tk.Label(login_frame, text="Password:").pack(padx=3, pady=3)
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack(padx=3, pady=3)
tk.Button(login_frame, text="Login", command=login_keedlink).pack(pady=3)
login_frame.pack(padx=5, pady=5)

# Frame Tagihan (akan muncul setelah login)
tagihan_frame = tk.Frame(root)
nominal_label = tk.Label(tagihan_frame, text="Nominal: -")
nominal_label.pack(padx=3, pady=3)
kode_va_label = tk.Label(tagihan_frame, text="Kode VA: -")
kode_va_label.pack(padx=3, pady=3)

tk.Button(tagihan_frame, text="Bayar via m-Banking", command=bayar_mbanking).pack(padx=20)
tk.Button(tagihan_frame, text="Cek Status Pembayaran", command=cek_status).pack(pady=20)

# Tidak langsung tampilkan tagihan_frame sampai login berhasil
tagihan_frame.pack_forget()

root.mainloop()
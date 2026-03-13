import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
import datetime

tanggal = datetime.datetime.now().strftime("%d-%m-%y")
waktu = datetime.datetime.now().strftime("%H:%M:%S")

attempts = 0

DAFTAR_BARANG = [
    "Ayam Goreng",
    "Ayam Bakar",
    "Rendang Daging",
    "Gulai Tunjang",
    "Gulai Telur Ikan",
    "Gulai Tambusu",
    "Daun Singkong",
    "Sayur Nangka",
    "Nasi Putih"
]

def login_system():
    global attempts

    username = name.get()
    password = pw.get()

    if username == "1" and password == "1":
        messagebox.showinfo("Login Berhasil", "Login Berhasil!!!")
        show_login.destroy()
        show_transaksi()

    else :
        attempts += 1
        if attempts >= 3 :
            messagebox.showwarning("Login Gagal", "Anda telah mencoba 3 kali. Program akan ditutup.")
            show_login.destroy()

        else:
            messagebox.showerror("Login Gagal", f"Username atau password salah. Anda telah mencoba {attempts}/3kali.")
            name.delete(0, tk.END)
            pw.delete(0, tk.END)

def sistem_transaksi():
    global nama, barang, jumlah, harga, uang, total, kembalian

    nama = nama_pembeli.get()
    barang = nama_barang.get()

    if not nama or not barang or not jumlah_Produk.get() or not harga_barang.get() or not Uang_Pembeli.get():
        messagebox.showerror("Error", "Semua field harus diisi.")
        return
    
    try :
        jumlah = int(jumlah_Produk.get())
        harga = int(harga_barang.get())
        uang = int(Uang_Pembeli.get())

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka saja untuk Jumlah Produk, Harga Produk, dan Uang Pembeli.")
        return
    
    total = jumlah * harga
    kembalian = uang - total
    kurang = total - uang

    if uang < total :
        messagebox.showerror("Error",f"Duit Pembeli Kurang Sebesar Rp.{kurang}")
        return
    
    elif jumlah <= 0 :
        messagebox.showerror("Error",f"Jumlah Barang Tidak Boleh 0 Atau Dibawah 0")
        return
    
    else :
        show_struk()
    
def show_transaksi():
    global nama_pembeli, nama_barang, jumlah_Produk, harga_barang, Uang_Pembeli, transaksi_window
    transaksi_window = tk.Tk()
    transaksi_window.title("Transaksi")
    transaksi_window.geometry("400x500")
    transaksi_window.configure(bg="#262525")

    tk.Label(transaksi_window, text="Nama Pembeli", bg="#262525", fg="white").pack(pady=10)
    nama_pembeli = tk.Entry(transaksi_window, width=30)
    nama_pembeli.pack(pady=5)

    tk.Label(transaksi_window, text="Nama Barang", bg="#262525", fg="white").pack(pady=10)
    nama_barang = ttk.Combobox(transaksi_window,values=DAFTAR_BARANG, state="readonly",width=30)
    nama_barang.pack(pady=5)

    tk.Label(transaksi_window, text="Jumlah Produk (Angka)", bg="#262525", fg="white").pack(pady=10)
    jumlah_Produk = tk.Entry(transaksi_window, width=30)
    jumlah_Produk.pack(pady=5)

    tk.Label(transaksi_window, text="Harga Produk (Angka)", bg="#262525", fg="white").pack(pady=10)
    harga_barang = tk.Entry(transaksi_window, width=30) 
    harga_barang.pack(pady=5)

    tk.Label(transaksi_window, text="Uang Pembeli (Angka)", bg="#262525", fg="white").pack(pady=10)
    Uang_Pembeli = tk.Entry(transaksi_window, width=30)
    Uang_Pembeli.pack(pady=5)

    tk.Button(transaksi_window, text="Total", bg="#0A5700", fg="#ffffff", command=sistem_transaksi,width=20).pack(pady=20)
    
    tk.Button(transaksi_window, text="Keluar", bg="#FF0000", fg="#ffffff", command=Destroy_Transaksi,width=20).pack(pady=10)
    
def show_struk():
    global Struk_window
    
    Struk_window = tk.Tk()
    Struk_window.title("Struk Pembayaran")
    Struk_window.geometry("300x375")

    tk.Label(Struk_window, text=f"Tanggal : {tanggal}                   Waktu : {waktu}").grid(sticky="w")
    tk.Label(Struk_window, text="============================================").grid(sticky="w")
    tk.Label(Struk_window, text=f"Nama Pembeli   : {nama}").grid(sticky="w")
    tk.Label(Struk_window, text="============================================").grid(sticky="w")
    tk.Label(Struk_window, text=f"Nama Barang    : {barang}").grid(sticky="w")
    tk.Label(Struk_window, text=f"Jumlah Produk  : {jumlah}").grid(sticky="w")
    tk.Label(Struk_window, text=f"Harga Produk   : {harga}").grid(sticky="w")
    tk.Label(Struk_window, text="============================================").grid(sticky="w")
    tk.Label(Struk_window, text=f"Tunai          : {uang}").grid(sticky="w")
    tk.Label(Struk_window, text=f"Total Harga    : {total}").grid(sticky="w")
    tk.Label(Struk_window, text="------------------------------").grid(sticky="w")
    tk.Label(Struk_window, text=f"Kembali        : {kembalian}").grid(sticky="w")
    tk.Button(Struk_window, text="Kembali Ke Transaksi", bg="#E20E0E", fg="white", command=next_struk).grid(sticky="w",pady=30, padx=90)
    transaksi_window.destroy()
    
def Destroy_Transaksi() :
    transaksi_window.destroy()
    
def next_struk ():
    Struk_window.destroy()
    show_transaksi()
    
def toggle_password():
    if show_pw.get():
        pw.config(show="")
    else:
        pw.config(show="*")

show_login = tk.Tk()
show_login.title("Sistem Login")
show_login.geometry("250x250")
show_login.configure(bg="#262525")

tk.Label(show_login, text="Username", bg="#262525", fg="#c90919", font=('arial',12,'bold')).pack(pady=5)
name = tk.Entry(show_login, width=30)
name.pack(pady=5, padx=10, fill='x')

tk.Label(show_login, text="Password", bg="#262525", fg="#c90919", font=('arial',12,'bold')).pack(pady=5)
pw_frame = tk.Frame(show_login, bg="#262525")
pw_frame.pack(pady=5, padx=10, fill='x')

pw = tk.Entry(pw_frame, show="*", width=28, relief="flat", bg="white")
pw.pack(side=tk.LEFT, fill='x', expand=True, padx=(2,0), pady=2)

show_pw = tk.IntVar()
checkbox = tk.Checkbutton(
    pw_frame, variable=show_pw,
    command=toggle_password, bg="white", activebackground="white",
    fg="#262525", selectcolor="white", width=2, bd=0, highlightthickness=0
)
checkbox.pack(side=tk.RIGHT, padx=(0,2), pady=2)

tk.Button(show_login, text="Login", command=login_system, bg="#FF0000", fg="white").pack(pady=10)

show_login.mainloop()

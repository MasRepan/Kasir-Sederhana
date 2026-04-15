# Kasir Sederhana (Python Tkinter)
Aplikasi kasir desktop sederhana berbasis **Python** dan **Tkinter** untuk simulasi transaksi penjualan.  
Project ini cocok untuk latihan dasar GUI Python, validasi input, dan alur transaksi (login -> input belanja -> struk).
## Fitur
- Login sederhana dengan batas percobaan maksimal 3 kali.
- Form transaksi dengan input:
  - Nama pembeli
  - Nama barang (dropdown/combobox)
  - Jumlah produk
  - Harga produk
  - Uang pembeli
- Validasi input kosong dan tipe data angka.
- Perhitungan otomatis:
  - Total harga (`jumlah * harga`)
  - Kembalian (`uang pembeli - total`)
- Notifikasi jika uang pembeli kurang.
- Tampilan struk pembayaran berisi tanggal, waktu, detail belanja, dan total.
## Teknologi
- Python 3
- Tkinter (built-in dari Python)
- ttk (komponen GUI tambahan dari Tkinter)
## Akun Login Default
- **Username:** `1`
- **Password:** `1`
## Catatan Penggunaan
- Nama barang dipilih dari daftar yang sudah disediakan di aplikasi.
- Input `Jumlah Produk`, `Harga Produk`, dan `Uang Pembeli` harus berupa angka.
- Jika total belanja lebih besar dari uang pembeli, transaksi akan ditolak.

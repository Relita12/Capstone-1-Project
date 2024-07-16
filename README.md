# CRUD Program: Simple Database Tele-Collection
Tele-collection adalah orang/karyawan di sebuah perusahaan pembiayaan yang melakukan penagihan angsuran ke customer/debitur melaui telephone. Database Tele-collection ini terdiri dari 9 kolom sebagai berikut:
1. idnumber: sebuah unique code sebagai nomor contract customer
2. nama: nama customer
3. tenor : jangka waktu yang diberikan perusahaan kepada customer untuk melunasi hutangnya
4. angsuran_ke: jumlah angsuran yang sudah dibayarkan customer
5. sisa_tenor: sisa angsuran yang belum dibayarkan
6. angsuran: cicilan yang harus dibayarkan pe bulan
7. phoneNo: nomor telephone customer
8. start_date: tanggal mulai Tele-Colllection melakukan penagihan
9. date_collect: hari/tanggal Tele-Collection melakukan penagihan setiap bulannya, date_collect diambil dari tanggal start_date


## Main Menu
Main menu pada program ini teridiri dari 5 fungsi utama sebagai berikut

### Menu 1: Read Data
Menu ini berfungsi untuk menampilakan database dalam bentuk tabulate menggunakan fungsi tabulate. Apabila menu read dipilih maka output yang keluar adalah database dalam bentuk tabel yang teridiri dari 9 kolom dan 14 baris

### Menu 2: Create New Customer Information
Menu ini berfungsi untuk menambahkan data/directory customer baru ke database. Menu ini akan meminta inputan/value untuk mengisi kolom nama, tenor, angsuran_ke, angsuran, phoneNo dan start_date. Sementara untuk kolom id_number, sisa_tenor, date_collect akan diupdate secara otomatis oleh program. Output dari program ini akan ditampilkan juga menggunakan fungsi read_data

### Menu 3: Update Customer Information
Menu ini berfungsi untuk melakukan edit pada database. Misal apabila ada data yang kurang valid di database, Tele-Collection dapat mengubah data tersebut menggunakan menu ini. Menu ini akan meminta input pasangan baris-kolom yang ingin di update datanya

### Menu 4: Delete Data
Menu ini berfungsi untuk melakukan delete pada directory/baris berdasarkan pasangan baris-kolom yang di input oleh Tele-Collection. Misalkan Tele-Collection ingin mendelete data customer yang angsurannya sudah lunas maka tele tinggal menginput kolom dengan sisa_tenor dan baris dengan value 0. Ketika menu ini di eksekuse maka semua directory database yang berisi sisa_tenor 0 akan di delete, dan data yang di delete akan dibackup di variabel recyclebin

### Menu 5: Filter Data
Menu ini fungsi untuk melakukan filter pada database berdasarkan kolom dan value yang ingin di filter oleh Tele-Collection. Misalkan Tele-Collection ingin mellakukkan penagihan dengan date_collect 29 maka program akan mengeluarkan output database yang date_collet nya 29 dalam bentuk tabel

### Menu 6: Exit
Menu ini berfungsi untuk keluar dari program Simple Database Telle-Collection


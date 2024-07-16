
from tabulate import tabulate
import datetime
database = [
{	'idnumber'	:	'DBTELE2400000001'	,	'nama'	:	'Vicky Setiawan'	,	'tenor'	:	40	,	'angsuran_ke'	:	40	,'sisa_tenor':0,	'angsuran'	:	5000000	,	'phoneNo'	:	'+6287870655359','start_date':'2021-04-01','date_collect':1	}	,
{	'idnumber'	:	'DBTELE2400000002'	,	'nama'	:	'Vicky Setiawan'	,	'tenor'	:	35	,'angsuran_ke'	:	2	,'sisa_tenor':33,	'angsuran'	:	3500000	,	'phoneNo'	:	'+6281806236888'	,'start_date':'2021-08-29','date_collect':29}	,
{	'idnumber'	:	'DBTELE2400000003'	,	'nama'	:	'Siti Hasmitayun'	,	'tenor'	:	50	,	'angsuran_ke'	:	34	,'sisa_tenor':16,	'angsuran'	:	1200000	,	'phoneNo'	:	'+6287878955359','start_date':'2020-06-05','date_collect':5	}	,
{	'idnumber'	:	'DBTELE2400000004'	,	'nama'	:	'Elyati Hutama'	,	'tenor'	:	50	,	'angsuran_ke'	:	50	,'sisa_tenor':0,	'angsuran'	:	2400000	,	'phoneNo'	:	'+6281112118812','start_date':'2020-06-05','date_collect':5	}	,
{	'idnumber'	:	'DBTELE2400000005'	,	'nama'	:	'Andi Raehan'	,	'tenor'	:	35	,	'angsuran_ke'	:	30	,'sisa_tenor':5,	'angsuran'	:	1000000	,	'phoneNo'	:	'+6281586550815','start_date':'2021-08-29','date_collect':29	}	,
{	'idnumber'	:	'DBTELE2400000006'	,	'nama'	:	'Jelly Situmorang'	,	'tenor'	:	30	,	'angsuran_ke'	:	16	,'sisa_tenor':14,	'angsuran'	:	1800000	,	'phoneNo'	:	'+6281872078916','start_date':'2022-01-26','date_collect':26	}	,
{	'idnumber'	:	'DBTELE2400000007'	,	'nama'	:	'Niko Nugroho'	,	'tenor'	:	45	,	'angsuran_ke'	:	24	,'sisa_tenor':21,	'angsuran'	:	2700000	,	'phoneNo'	:	'+6281197607174','start_date':'2020-11-02','date_collect':2	}	,
{	'idnumber'	:	'DBTELE2400000008'	,	'nama'	:	'Malvina Gunawan'	,	'tenor'	:	30	,'angsuran_ke'	:	29	,'sisa_tenor':1,	'angsuran'	:	3600000	,	'phoneNo'	:	'+6281580791677','start_date':'2022-01-26','date_collect':26	}	,
{	'idnumber'	:	'DBTELE2400000009'	,	'nama'	:	'Stepahnus Adrian'	,	'tenor'	:	40	,'angsuran_ke'	:	36	,'sisa_tenor':4,	'angsuran'	:	4100000	,	'phoneNo'	:	'+6281581761674','start_date':'2021-04-01','date_collect':1	}	,
{	'idnumber'	:	'DBTELE2400000010'	,	'nama'	:	'Deni Chandra'	,	'tenor'	:	35	,	'angsuran_ke'	:	11	,'sisa_tenor':24,	'angsuran'	:	2500000	,	'phoneNo'	:	'+6282196642573','start_date':'2021-08-29','date_collect':29	}	,
{	'idnumber'	:	'DBTELE2400000011'	,	'nama'	:	'Andrew Leonardo'	,	'tenor'	:	50	,	'angsuran_ke'	:	50	,'sisa_tenor':0,	'angsuran'	:	3900000	,	'phoneNo'	:	'+6281372669910','start_date':'2020-06-05','date_collect':5	}	,
{	'idnumber'	:	'DBTELE2400000012'	,	'nama'	:	'Johan Hermawan'	,	'tenor'	:	40	,	'angsuran_ke'	:	40	,'sisa_tenor':0,	'angsuran'	:	4200000	,	'phoneNo'	:	'+6281376669912','start_date':'2021-04-01','date_collect':1	}	,
{	'idnumber'	:	'DBTELE2400000013'	,	'nama'	:	'Henry Susilo'	,	'tenor'	:	50	,	'angsuran_ke'	:	47	,'sisa_tenor':3,	'angsuran'	:	3000000	,	'phoneNo'	:	'+6281378369910','start_date':'2020-06-05','date_collect':5}
]



# Fungsi untuk validasi angka
def input_numerik(prompt= 'masukkan angka: '):
  while True:
      inputan = input(prompt)
      if inputan.isdigit():
        return int(inputan) # berhenti loop
      else:
          print('input anda bukan angka')


# Fungsi Iuntuk validasi string
def input_string(prompt='masukkkan alphabet: '):
    while True:
      inputan=input(prompt)
      if inputan.replace(" ", "").isalpha():
        return inputan # berhenti loop
      else:
          print('input anda bukan alphabet')


# Fungsi untuk validasi nomor Telephone
def input_phoneNo(prompt= 'masukkan angka: '):
    while True:
      inputan = input(prompt)
      if inputan.isdigit() and len(inputan) in range (10,12):
        return int(inputan) # berhenti loop
      elif inputan.isdigit() and (len(inputan)>11 or len(inputan)<10) :
          print('nomor yang anda input tidak valid')
          input_numerik()
      else:
          print('input anda bukan angka')


#Fungsi untuk validasi tanggal
def input_tanggal(prompt='masukkan tanggal (yyyy-mm-dd): '):
  while True:
    inputan=input(prompt)
    try:
      datetime.datetime.strptime(inputan, '%Y-%m-%d')
      return inputan
    except ValueError:
      print('masukkan sesuai format')


#Fungsi untuk mengisi kolom idnumber secara otomatis untuk data baru
def idcode():
    global database
    for i in range(12,len(database)):
      database[i]['idnumber']='DBTELE'+str(int(database[i]['idnumber'][6:])+1)
      return database[i]['idnumber']


# Fungsi untuk mencari index dictionary berdasarkan key & value tertentu

def cari_index(key,value):
  a=[]
  for i,dict_item in enumerate(database):
    if dict_item.get(key) == value:
      a.append(i)
    else:
      continue
  return a


# Fungsi untuk menampilkan data dalam bentuk tabel
def read_data(data):
    print(tabulate(data, headers = 'keys', tablefmt = 'pretty'))


# Fungsi untuk menambah data baru
def create_data():
  idnumber=idcode()
  nama = input_string('masukkan nama customer baru: ').title()
  tenor = input_numerik('masukkan tenor customer baru: ')
  angsuran_ke = input_numerik('masukkan angsuran_ke customer baru: ')
  sisa_tenor=tenor-angsuran_ke
  angsuran = input_numerik('masukkan jumlah angsuran/bln customer baru: ')
  phoneNo = '+62'+ str(input_phoneNo('masukkan nomor telephone customer baru : +62 '))
  start_date=input_tanggal('masukkan tanggal mulai (yyyy-mm-dd): ')
  date_collect=start_date[9:]
  data_baru = {'idnumber':idnumber,'nama': nama, 'tenor': tenor, 'angsuran_ke': angsuran_ke,'sisa_tenor':sisa_tenor, 'angsuran':angsuran, 'phoneNo':phoneNo,'start_date':start_date,'date_collect':date_collect}
  database.append(data_baru)
  print('\nBerikut Database yang sudah diupdate\n')
  read_data(database)
  return database


# Fungsi untuk melakukan update pada database berdasarkan row dan kolom
def update_data():
  # milih index atau baris data yg mana
  row = input_numerik("pilih baris yang ingin diupdate: ")
  row=row-1

  # tanya kolom yang mana
  kolom = input('pilih kolom yang ingin diupdate: ')
  if kolom in database[0].keys():
    if kolom == 'nama':
      database[row][kolom] = input_string('masukkan nama terbaru: ').title()
    elif kolom == 'tenor':
      database[row][kolom] = input_numerik('masukkan tenor terbaru: ')
    elif kolom == 'angsuran_ke':
      database[row][kolom] = input_numerik('masukkan angsuran_ken terbaru: ')
    elif kolom == 'angsuran':
      database[row][kolom] = input_numerik('masukkan angsura  n terbaru: ')
    elif kolom == 'phoneNo':
      database[row][kolom] = '+62'+ str(input_phoneNo('masukkan nomor telephone terbaru: +62'))
    elif kolom == 'start_date':
      database[row][kolom] = input_tanggal('masukkan start_date terbaru: ')
    print('\nBerikut Database yang sudah diupdate\n')
    read_data(database)
    return database
  else:
    print('kolom tidak ada')


# Fungsi untuk melakukan delete pada Database berdasarkan key-value
def delete_data():
  global database
  key=input('masukkan nama kolom: ').lower()
  value=input('masukkan value yang dicari:')

  #Validasi value yang diinput
  if key=='idnumber' or key=='nama' or key=='phoneNo' or key=='start_date':
    value=value.title()
  elif key=='tenor'or key=='angsuran_ke' or key=='sisa_tenor' or key=='angsuran' or key=='date_collect':
    value=int(value)
  else:
    print('kolom tidak ada')
  
  #Memanggil fungsi cari_index untuk mengumpulkan index-index pasangan key-value yang ingin didelete
  n=cari_index(key,value)

  #Menyimpan pasangan key-value yang ingin didelete dalam variabel recycle_bin 
  recycle_bin=[database[i] for i in n]
  #read_data(recycle_bin)

  #Menghapus pasangan key-value pada database
  for i in recycle_bin:
    database.remove(i)

  #Menampilkan isi dari recycle_bin dan database terupdate
  if recycle_bin==[]:
    print('\nvalue tidak ditemukan di database'.upper())
    print('------------------------------------')
  else:
    print('\nBerikut data yang di terupdate\n')
    read_data(database)
    print('\nBerikut backup data yang di delete\n')
    read_data(recycle_bin)
    return database


#Fungsi untuk melakukan filter berdasarkan key-value
def filter_data():
  global database
  key=input('masukkan nama kolom: ').lower()
  value=input('masukkan value yang ingin di filter:')

  #Validasi value yang di input
  if key=='idnumber' or key=='nama' or key=='phoneNo' or key=='start_date':
    value=value.title()
  elif key=='tenor'or key=='angsuran_ke' or key=='sisa_tenor' or key=='angsuran' or key=='date_collect':
    value=int(value)
  else:
    print('kolom tidak ada')

  #Memanggil fungsi cari_index untuk mengumpulkan index-index pasangan key-value yang ingin difilter
  n=cari_index(key,value)

  #Menyimpan pasangan key-value yang ingin difilter dalam variabel filter
  filter=[database[i] for i in n]

  #Menampilkan isi dari variabel filter
  if filter==[]:
    print('\nvalue tidak ditemukan di database'.upper())
    print('------------------------------------')
  else:
    print('\nBerikut data yang di filter\n')
    read_data(filter)
    return filter



# Main Function (Fungsi Utama)
def main():
    while True:
        print('''
        Hy Tellecolection,
        What do you want to do?

        1. Read Data
        2. Create New Customer Information
        3. Update Customer Information
        4. Delete Data
        5. Filter Data
        6. Exit
        ''')

        inputan = input('masukkan menu: ')
        if inputan == '1':
            read_data(database)
        elif inputan == '2':
            create_data()
        elif inputan == '3':
            update_data()
        elif inputan == '4':
            delete_data()
        elif inputan == '5':
            filter_data()
        elif inputan == '6':
            break # keluar
        else:
            print('menu tidak ada')
main()
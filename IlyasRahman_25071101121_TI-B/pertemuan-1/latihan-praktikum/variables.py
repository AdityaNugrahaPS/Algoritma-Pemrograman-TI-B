#python variables -> variable names -> legal dan non legal

#nama legal
nama_depan = 'ilyas' #garis bawah
namaDepan = 'ilyas' #camel case
namadepan = 'ilyas' #karena variabel case sensitive maka namadepan dan namaDepan beda
nama1 = 'ilyas' #angka di belakang
_nama = 'ilyas' #garis bawah di depan
nama_depan_saya_yang_sangat_panjang = 'ilyas' #nama panjang masih legal

#nama tidak legal
1nama = 'ilyas' #angka di depan -> error
nama depan = 'ilyas' #spasi di tengah -> error  
nama-depan = 'ilyas' #minus di tengah -> error
@nama = 'ilyas' #karakter spesial di depan -> error
nama$depan = 'ilyas' #karakter spesial di tengah -> error
nama% = 'ilyas' #karakter spesial di belakang -> error
nama depan saya = 'ilyas' #spasi di tengah -> error
1nama$depan = 'ilyas' #angka di depan dan karakter spesial di tengah -> error   
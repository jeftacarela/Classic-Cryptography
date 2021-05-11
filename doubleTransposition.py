# Python3
import math 

key = "johanes"

# Proses Enkripsi 
def encryptMessage(msg): 
	cipher = "" 

	k_indx = 0

	msg_len = float(len(msg)) 
	msg_lst = list(msg) 
	key_lst = sorted(list(key)) 

	# Menghitung panjang kolom array 
	col = len(key) 
	
	# Menghitung panjang baris array 
	row = int(math.ceil(msg_len / col)) 

	# Mengisi karakter "_" 
	fill_null = int((row * col) - msg_len) 
	msg_lst.extend('_' * fill_null) 

	# Membuat array untuk diisi pesane 
	matrix = [msg_lst[i: i + col] 
			for i in range(0, len(msg_lst), col)] 

	# Membaca kolom pesan dengan menambah kunci 
	for _ in range(col): 
		curr_idx = key.index(key_lst[k_indx]) 
		cipher += ''.join([row[curr_idx] 
						for row in matrix]) 
		k_indx += 1

	return cipher 

# Proses Dekripsi 
def decryptMessage(cipher): 
	msg = "" 

	k_indx = 0

	# Index Pesan 
	msg_indx = 0
	msg_len = float(len(cipher)) 
	msg_lst = list(cipher) 

	# Menghitung Kolom Array 
	col = len(key) 
	
	# Menghitung Baris Array 
	row = int(math.ceil(msg_len / col)) 

	# convert key menjadi list dan di sort secara alfabetis berdasar urutan 
	key_lst = sorted(list(key)) 

	# membuat array baru untuk diisi hasil dekripsi
	dec_cipher = [] 
	for _ in range(row): 
		dec_cipher += [[None] * col] 

	# Membuat array baru berdasar nilai permutasi  
	for _ in range(col): 
		curr_idx = key.index(key_lst[k_indx]) 

		for j in range(row): 
			dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
			msg_indx += 1
		k_indx += 1

	# Handling String
	try: 
		msg = ''.join(sum(dec_cipher, [])) 
	except TypeError: 
		raise TypeError("This program cannot handle repeating words.") 

	null_count = msg.count('_') 

	if null_count > 0: 
		return msg[: -null_count] 

	return msg 

msg = "KriptografiDoubleTranspose"

cipher = encryptMessage(msg) 
duatranspose = encryptMessage(cipher)

print("Encrypted Message: {}".format(duatranspose)) 
print("Decrypted Message: {}".format(decryptMessage(cipher)))
print 


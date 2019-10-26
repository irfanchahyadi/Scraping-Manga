
"""
Database creator
Author: Irfan Chahyadi
Source: github.com/irfanchahyadi/Scraping-Manga

Run this file after edit / add manga list, when web gui not running.
"""

import sqlite3, os

FILENAME = 'manga.db'

if FILENAME in os.listdir():
	os.remove(FILENAME)

create_table_manga_list = """
	CREATE TABLE manga_list (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name VARCHAR(50) NOT NULL,
		image VARCHAR(50) NOT NULL,
		description VARCHAR NOT NULL);
	"""
create_table_manga_crawler = """
	CREATE TABLE manga_crawler (
		id INTEGER,
		lang_id VARCHAR(5),
		crawler VARCHAR(50) NOT NULL,
		sub_url VARCHAR(255) NOT NULL,
		selectors VARCHAR(255) NOT NULL);
	"""

create_table_manga_language = """
	CREATE TABLE manga_language (
		id VARCHAR(5),
		language VARCHAR(20));
	"""

insert_table_manga_list = """
	INSERT INTO manga_list (id, name, image, description) VALUES 
		(1, 'Naruto', 'naruto.jpg', 'Sebelum kelahiran Naruto, iblis rubah ekor sembilan telah menyerang Desa Konoha. Seorang pria yang dikenal sebagai Hokage ke-4 menyegel iblis dalam Naruto yang baru lahir, menyebabkan dia sadar tumbuh dibenci oleh sesama warga desa. Meskipun kurangnya bakat dalam banyak bidang ninjutsu, Naruto berusaha untuk hanya satu tujuan: untuk mendapatkan gelar Hokage, ninja terkuat di desanya. Menginginkan rasa hormat dia tidak pernah menerima, Naruto bekerja terhadap mimpinya dengan sesama teman Sasuke dan Sakura dan Kakashi guru mereka pergi melalui banyak cobaan dan pertempuran yang datang dengan menjadi seorang ninja.'),
		(2, 'One Piece', 'onepiece.jpg', 'Keagungan, Kemuliaan, Emas. Seorang bajak laut bernama Gold Roger, juga dikenal sebagai Raja Bajak Laut telah menaklukkan itu semua. Dia dieksekusi dengan alasan yang tidak diketahui, tetapi sebelum dia meninggal, dia mengungkapkan kata terakhir tentang Harta Karun legendaris yang bernama One Piece yang tersembunyi di Grand Line. 22 tahun setelah kematiannya, seorang bajak laut bernama Monkey D. Luffy muncul dan hanya memiliki satu tujuan, untuk menjadi "Raja Bajak Laut" berikutnya dan menemukan Harta "One Piece". Dan petualangan tanpa akhir pun dimulai.'),
		(3, 'One Punch Man', 'onepunchman.jpg', 'Dalam hal ini baru aksi - komedi , segala sesuatu tentang seorang pemuda bernama Saitama berteriak " RATA-RATA , " dari ekspresi tak bernyawa , kepala botak , untuk fisik mengesankan nya . Namun , rekan -rata tampan ini tidak memiliki masalah rata-rata ... Dia benar-benar seorang superhero yang mencari lawan tangguh ! Masalahnya adalah , setiap kali ia menemukan kandidat yang menjanjikan ia mengalahkan ingus keluar dari mereka dalam satu pukulan . Dapat Saitama akhirnya menemukan seorang penjahat jahat cukup kuat untuk menantangnya ? Ikuti Saitama melalui aktivitas seksual lucu saat ia mencari orang-orang jahat baru untuk menantang !'),
		(4, 'Boruto', 'boruto.jpg', 'Boruto Uzumaki adalah anak pertama dari Naruto Uzumaki, sang Hokage Ketujuh yang begitu dihormati karena jasanya dalam menyelamatkan dunia. Sama seperti ayahnya, ia juga terkenal bandel dan susah diatur. Cerita ini berfokus tentang Boruto dan teman-temannya sebagai ninja generasi baru yang diharapkan dapat melampaui generasi sebelumnya.'),
		(5, 'Nanatsu no Taizai', 'nanatsunotaizai.jpg', '"Tujuh Dosa Mematikan, " sekelompok ksatria jahat yang bersekongkol untuk menggulingkan kerajaan Britannia, yang dikatakan telah diberantas oleh Ksatria Suci, meskipun beberapa mengklaim bahwa mereka masih hidup. Sepuluh tahun kemudian, Ksatria suci mengadakan kudeta dan membunuh raja, untuk membuat perang suci baru. Elizabeth, putri ketiga raja, menetapkan perjalanan untuk menemukan "Tujuh Dosa Mematikan, " dan meminta bantuan mereka untuk mengambil kembali kerajaan'),
		(6, 'Dr. Stone', 'drstone.jpg', 'The science-fiction adventure series follows what happens when suddenly the world biggest-ever "crisis" arrives.'),
		(7, 'Boku no Hero Academia', 'bokunoheroacademia.jpg', 'Apa itu pahlawan? Bagi Izuku Midoriya, jawabannya sangatlah sederhana: “Pahlawan adalah seseorang yang selalu dicita-citakan” Dan siapakah pahlawan terbaik? Yah kalau itu, tentu saja sang legenda All Might. All Might adalah pahlawan nomor satu dan juga “Simbol Perdamaian” di dunia ini. Bahkan Izuku sekalipun tak akan pernah terbayangkan bahwa dia akan dipertemukan dengan pahlawan masa kecilnya.'),
		(8, 'Fairy Tail', 'fairytail.jpg', 'Berlatar di sebuah dunia fiksi, dimana terdapat Guild penyihir bernama "Fairy Tail". Guild ini bertempat di kota Magnolia, yang berada di Kerajaan Fiore. Saat ini guild ini dipimpin oleh Makarov. Lucy Heartfilia, seorang gadis 17 tahun yang ingin menjadi penyihir. Dia memutuskan untuk bergabung dengan salah satu Guild penyihir paling terkenal, Fairy Tail. Suatu hari, secara kebetulan ia bertemu dengan Natsu Dragneel yang mabuk kendaraan. Saat bertemu dengannya, Lucy tidak tahu bahwa Natsu adalah penyihir anggota dari guild Fairy Tail.'),
		(9, 'Detective Conan', 'detectiveconan.jpg', 'Shinichi Kudo adalah seorang detektif SMU berumur tujuh belas tahun yang biasa disebut "Sherlock Holmes moderen." Namun, suatu malam setelah kencan dengan kekasih masa kecilnya, Ran, Shinichi menyaksikan perdagangan ilegal dan, tertangkap basah oleh penjahat, tak sadarkan diri dan diberi obat yang seharusnya untuk membunuhnya. saat ia terbangun dan mendapati dirinya menyusut ke usia tujuh tahun. Dalam rangka untuk melacak orang-orang yang melakukan itu padanya, Shinichi menyembunyikan identitasnya dan tinggal bersama Ran, yang ayahnya kebetulan seorang detektif pas-pasan, dan dengan itu datang serangkaian pembunuhan dan misteri yang harus ia pecahkan.'),
		(10, 'Black Clover', 'blackclover.jpg', 'Asta adalah seorang anak muda yang bermimpi menjadi penyihir terhebat di kerajaan. Tapi dia punya satu masalah, dia tidak bisa menggunakan sihir. Nasib baik menghampirinya karena mendapatkan Grimoire lima daun yang sangat langka "Black Clover" yang memberinya kekuatan anti-sihir. Meskipun dia tidak bisa menggunakan sihir, tapi dia tetap bertekad untuk menjadi Raja Penyihir.'),
		(11, 'Shingeki no Kyojin', 'shingekinokyojin.jpg', 'Beberapa ratus tahun yang lalu, manusia hampir dibasmi oleh raksasa. Raksasa yang biasanya digambarkan tinggi, tampaknya tidak memiliki kecerdasan, memakan manusia, dan terburuk dari semua, tampaknya melakukannya untuk kesenangan dan bukan sebagai sumber makanan. Sebagian kecil manusia bertahan hidup dengan menutup diri di kota dilindungi oleh dinding yang sangat tinggi, bahkan lebih tinggi dari yang terbesar dari raksasa. Melangkah maju ke masa kini dan kota belum melihat raksasa di lebih dari 100 tahun. Remaja laki-laki Eren dan saudara angkatnya Mikasa menjadi saksi dari sesuatu yang sangat mengerikan seperti tembok kota dihancurkan oleh raksasa super yang muncul dari udara tipis. Para raksasa kecil membanjiri kota, dua anak menyaksikan dengan ngeri ibu mereka dimakan hidup-hidup. Eren bersumpah bahwa ia akan membunuh setiap raksasa dan membalas dendam untuk semua umat manusia.'),
		(12, 'Shokugeki no Souma', 'shokugekinosouma.jpg', 'Shokugeki no Soma menceritakan seorang pemuda bernama Sōma Yukihira, yang bercita-cita menjadi seorang full-time chef di restoran milik ayahnya dan melampaui keahlian memasak ayahnya. Namun beberapa saat setelah ia lulus dari SMP, ayahnya , Jōichirō Yukihira, mendapatkan pekerjaan baru di Amerika dan menutup restorannya. Walaupun begitu, semangat bertarung Sōma hidup kembali setelah menerima tantangan dari ayahnya yaitu untuk bertahan di sebuah sekolah kuliner elit dimana hanya 10% siswa yang dapat lulus dari sekolah tersebut.'),
		(13, 'Death Note', 'deathnote.jpg', 'Death Note bercerita tentang seorang pelajar (Light Yagami) yang merasa kalau dunia ini sudah membusuk oleh kejahatan. dan dia merasa bosan atas kadaan dunia yang seperti itu. Hal itu juga dirasakan oleh sang dewa kematian (Ryuk) yang merasa bosan atas kehampaan hidupnya di dunia dewa kematian. Ryuk, yang memiliki Death Note, merasa kalau akan lebih menarik jika buku itu dijatuhkan di dunia manusia agar dia terhibur.'),
		(14, 'BTOOOM!', 'btooom!.jpg', 'Sakamoto adalah seorang NEET berusia 22 tahun yang merupakan Top Player di sebuah game Online berjudul BTOOM. Suatu hari, ia bangun dan meyadari kalau dirinya telah terjebak di versi nyata dari game favoritenya itu. Hidupnya sekarang berada di dalam bahaya, akankah ia berhasil bertahan hingga bisa menemukan kenapa hal ini bisa terjadi?'),
		(15, 'Darwins Game', 'darwinsgame.jpg', 'Sudo Kaname suddenly gets involved in a death game through the mysterious mobile app "Darwins Game."');
	"""

insert_table_manga_crawler = """
	INSERT INTO manga_crawler (id, lang_id, crawler, sub_url, selectors) VALUES
		(1, 1, 'mangaku', 'baca-komik-naruto-terbaru-bahasa-indonesia', 'div.fndsosmed-social + div + p a'),
		(2, 1, 'mangaku', 'baca-komik-one-piece-bahasa-indonesia', 'div.fndsosmed-social + div a'),
		(3, 1, 'mangaku', 'komik-onepunch-man-bahasa-indonesia', 'div.fndsosmed-social + div a;div.fndsosmed-social + div + p + p a'),
		(4, 1, 'mangaku', 'baca-komik-naruto-terbaru-bahasa-indonesia', 'div.fndsosmed-social + div a'),
		(5, 1, 'mangaku', 'nanatsu-no-taizai-bahasa-indonesia', 'div.fndsosmed-social + div a;div.fndsosmed-social + div + p a;div.fndsosmed-social + div + p + p a'),
		(6, 1, 'mangaku', 'dr-stone-bahasa-indonesia', 'div.fndsosmed-social + div a'),
		(7, 1, 'mangaku', 'komik-online-boku-no-hero-academia-bahasa-indonesia', 'div.fndsosmed-social + div a'),
		(8, 1, 'mangaku', 'fairy-tail-terbaru-bahasa-indonesia', 'div.fndsosmed-social + div + p a'),
		(9, 1, 'mangaku', 'detectiv-conan-bahasa-indonesia-terbaru', 'div.fndsosmed-social + div a'),
		(10, 1, 'mangaku', 'black-clover-bahasa-indonesia', 'div.fndsosmed-social + div a'),
		(11, 1, 'mangaku', 'komik-shingeki-no-kyojin-attack-on-titan-bahasa-indonesia', 'div.fndsosmed-social + div a'),
		(12, 1, 'mangaku', 'shokugeki-no-souma-bahasa-indonesia', 'div.fndsosmed-social + div a'),
		(13, 1, 'mangaku', 'death-note-bahasa-indonesia', '#belowdesc ~ div[style*="border:1px"] > a'),
		(14, 1, 'mangaku', 'btooom-bahasa-indonesia', 'div.fndsosmed-social + div a'),
		(15, 1, 'mangaku', 'darwins-game', 'div.fndsosmed-social + div a');
	"""

insert_table_manga_language = """
	INSERT INTO manga_language (id, language) VALUES
		(1, 'Indonesia');
	"""

con = sqlite3.connect(FILENAME)
cur = con.cursor()

cur.execute(create_table_manga_list)
cur.execute(create_table_manga_crawler)
cur.execute(create_table_manga_language)

cur.execute(insert_table_manga_list)
con.commit()
cur.execute(insert_table_manga_crawler)
con.commit()
cur.execute(insert_table_manga_language)
con.commit()

PERANCANGAN SISTEM PEMESANAN DESAIN UNDANGAN BERBASIS WEB PADA 
TOKO DUA INSAN STORY


## BAB 1
## PENDAHULUAN

### 1.1 Latar Belakang

Di era digital saat ini, perkembangan teknologi informasi telah membawa perubahan signifikan dalam berbagai aspek kehidupan, termasuk dalam bidang bisnis dan layanan kreatif. Salah satu perubahan yang paling mencolok adalah peralihan dari sistem pemesanan konvensional menuju sistem berbasis online. Digitalisasi sistem pemesanan memberikan berbagai keuntungan, seperti kemudahan akses, fleksibilitas waktu, serta perluasan jangkauan pemasaran produk maupun jasa (Harianto dkk., 2021). Sejalan dengan perkembangan tersebut, penerapan website pada toko penjualan menjadi solusi penting agar pelanggan dapat melakukan pemesanan produk secara lebih mudah dan efisien.

Toko Dua Insan Story merupakan usaha lokal yang bergerak di bidang pembuatan desain undangan, baik dalam bentuk digital maupun cetak, untuk berbagai acara seperti pernikahan, tunangan, ulang tahun, dan acara resmi lainnya. Saat ini, proses pemesanan desain undangan masih dilakukan secara manual melalui pesan langsung di media sosial. Cara tersebut seringkali menimbulkan beberapa kendala, seperti risiko kesalahpahaman informasi, keterbatasan dalam melakukan penyesuaian desain secara interaktif, serta kesulitan pelanggan dalam melacak status pemesanan.

Melihat permasalahan tersebut, diperlukan sebuah sistem pemesanan desain undangan online yang mampu memberikan pengalaman pengguna (user experience) yang lebih baik, mudah diakses oleh berbagai kalangan, serta mempercepat proses komunikasi antara pelanggan dan penyedia jasa. Sistem ini diharapkan dapat menyediakan fitur-fitur seperti katalog desain undangan, formulir pemesanan online, pemilihan template dan warna, pengisian data acara, pratinjau desain secara real-time, serta sistem notifikasi untuk proses revisi dan konfirmasi pesanan.

Laravel merupakan framework berbasis PHP yang dirancang untuk mempermudah proses pengembangan aplikasi web dengan menerapkan pola arsitektur Model-View-Controller (MVC) (Valenty dkk., 2024). Framework ini menyediakan berbagai fitur bawaan seperti sistem routing, authentication, template engine (Blade), serta Object Relational Mapping (ORM) melalui Eloquent untuk mempermudah interaksi dengan basis data. Penerapan Laravel memberikan sejumlah keuntungan, antara lain peningkatan efisiensi waktu pengembangan, konsistensi kode, serta keamanan yang lebih baik dalam mengelola proses autentikasi dan transaksi data. Dengan sintaks yang bersih dan struktur yang terorganisir, Laravel banyak digunakan dalam pengembangan sistem informasi modern karena dapat meminimalisasi kesalahan logika dan mempercepat proses implementasi.

React merupakan library JavaScript yang dikembangkan untuk membangun antarmuka pengguna (user interface) yang dinamis dan responsif (Santoso dkk., 2023). React menggunakan konsep komponen (component-based architecture), yang memungkinkan pengembang untuk membangun elemen antarmuka secara modular dan dapat digunakan kembali. Dengan konsep Virtual DOM, React mampu memperbarui tampilan halaman secara efisien tanpa perlu memuat ulang seluruh konten, sehingga memberikan pengalaman pengguna yang lebih cepat dan interaktif.

Dalam penelitian ini, sistem pemesanan desain undangan online akan dikembangkan dengan menggunakan Laravel sebagai kerangka kerja utama pada sisi backend, dan React pada sisi frontend. Laravel akan menangani logika bisnis, autentikasi pengguna, pengelolaan data, serta integrasi dengan basis data dan layanan pihak ketiga. Sedangkan React akan digunakan untuk menampilkan antarmuka pengguna yang interaktif, dinamis, dan mudah digunakan. Untuk mendukung proses transaksi, sistem ini juga akan diintegrasikan dengan layanan payment gateway Midtrans, yang memungkinkan pengguna melakukan pembayaran melalui berbagai metode, seperti transfer bank, kartu debit/kredit, maupun e-wallet.

Dengan adanya sistem pemesanan desain undangan secara online ini, Toko Dua Insan Story diharapkan dapat meningkatkan efisiensi layanan, memperluas jangkauan pelanggan, serta mempermudah proses pengelolaan pemesanan. Pendekatan ini diharapkan mampu mendukung toko dalam memberikan layanan yang lebih profesional, responsif, serta sesuai dengan kebutuhan dan preferensi pelanggan.

### 1.2 Perumusan Masalah

Berdasarkan uraian permasalahan pada latar belakang, perumusan masalah dalam penelitian ini adalah:

"Bagaimana merancang dan membangun sebuah sistem pemesanan desain undangan berbasis web yang fungsional untuk menggantikan proses pemesanan manual pada Toko Dua Insan Story, sehingga dapat meningkatkan efisiensi komunikasi antara pelanggan dan penyedia jasa, meminimalisasi kesalahan informasi pemesanan, serta menyediakan fitur interaktif seperti katalog desain, pratinjau hasil secara real-time, dan integrasi pembayaran online untuk mendukung pelayanan yang cepat, transparan, dan profesional?"

### 1.3 Batasan Penelitian

Penelitian ini dibatasi agar tetap fokus pada tujuan yang ingin dicapai. Ruang lingkup penelitian meliputi perancangan sistem pemesanan desain undangan berbasis web menggunakan Laravel (backend) dan React.js (frontend) dengan basis data MySQL. Fitur utama yang dikembangkan mencakup katalog desain undangan, formulir pemesanan online, pengisian data acara oleh pelanggan, pratinjau desain secara real-time, notifikasi status pesanan, serta integrasi pembayaran online melalui Midtrans.

Aspek lain yang tidak termasuk dalam cakupan penelitian antara lain manajemen stok bahan cetak, pengaturan pengiriman fisik undangan, modul akuntansi lanjutan, serta fitur multi-user dengan peran kompleks (admin–desainer–pelanggan).

### 1.4 Tujuan Penelitian

Tujuan penelitian ini adalah merancang dan membangun sistem pemesanan desain undangan berbasis web menggunakan Laravel dan React.js dengan basis data MySQL pada Toko Dua Insan Story, sebagai pengganti proses pemesanan manual. Penelitian ini bertujuan meningkatkan efisiensi proses pemesanan dan komunikasi antara pelanggan dan penyedia jasa, mengurangi risiko kesalahan informasi, serta mempercepat proses konfirmasi pesanan.

Selain itu, sistem ini ditujukan untuk menyediakan antarmuka yang interaktif dan responsif sehingga pelanggan dapat memilih template desain, menyesuaikan data acara, dan melihat pratinjau desain secara real-time. Integrasi payment gateway Midtrans juga diharapkan mempermudah proses transaksi pembayaran secara aman dan efisien.

### 1.5 Manfaat Penelitian

#### a. Manfaat bagi Penulis

Penelitian ini memberikan kesempatan bagi penulis untuk merancang dan membangun aplikasi web secara full-stack, mulai dari perancangan backend hingga implementasi frontend. Penulis memperoleh pengalaman dalam penerapan arsitektur MVC pada Laravel, pengelolaan basis data MySQL, serta konsep komponen dan state management pada React.js. Hasil penelitian diharapkan menjadi portofolio yang bernilai dalam pengembangan aplikasi web modern.

#### b. Manfaat bagi Pengguna

Bagi Toko Dua Insan Story, manfaat utama penelitian ini adalah peningkatan efisiensi dan profesionalitas dalam proses pemesanan desain undangan. Sistem yang dikembangkan memudahkan pengelolaan pesanan secara terstruktur, mempercepat proses konfirmasi, serta meningkatkan kepuasan pelanggan melalui katalog desain, pratinjau real-time, dan notifikasi otomatis. Sistem juga membantu memperluas jangkauan pemasaran online.

### 1.6 Metodologi Perancangan Solusi

Metode perancangan perangkat lunak yang digunakan adalah Extreme Programming (XP). XP menekankan kolaborasi erat antara pengembang dan pengguna serta iterasi cepat dalam proses pengembangan. Kegiatan utama meliputi perencanaan, perancangan, pengkodean, dan pengujian.

#### a. Planning (Perencanaan)

Identifikasi masalah dilakukan melalui observasi dan wawancara dengan pemilik. Hasilnya berupa daftar kebutuhan fungsional dan non-fungsional serta analisis alur pemesanan manual yang kemudian dijadikan dasar rancangan solusi berbasis web.

#### b. Design (Perancangan)

Hasil analisis kebutuhan diterjemahkan ke dalam model dan rancangan sistem, termasuk arsitektur sistem, perancangan antarmuka menggunakan React.js, dan perancangan basis data menggunakan ERD. Pemodelan proses bisnis dan diagram UML juga disusun untuk memastikan keterpaduan komponen.

#### c. Coding (Pengkodean)

Implementasi dilakukan dengan menerjemahkan rancangan ke dalam kode menggunakan Laravel (backend) dan React.js (frontend). MySQL digunakan sebagai basis data untuk menyimpan data pemesanan dan informasi pelanggan.

#### d. Testing (Pengujian)

Setelah pengkodean, dilakukan pengujian fungsional untuk memverifikasi kesesuaian sistem terhadap kebutuhan pengguna, termasuk pengujian fitur pemesanan, pratinjau desain, notifikasi, dan integrasi pembayaran online.

### 1.7 Sistematika Penulisan

Berikut gambaran singkat sistematika penulisan laporan:

- **BAB 1 PENDAHULUAN**: Gambaran umum penelitian, meliputi latar belakang, perumusan masalah, batasan penelitian, tujuan dan manfaat, metodologi, dan sistematika penulisan.
- **BAB 2 GAMBARAN UMUM TOKO DUA INSAN STORY**: Profil objek penelitian, layanan, proses bisnis, dan struktur organisasi.
- **BAB 3 PERANCANGAN SOLUSI**: Analisis kebutuhan, desain sistem (UML, ERD), perancangan antarmuka, dan langkah implementasi.
- **BAB 4 PENUTUP**: Kesimpulan dan saran untuk pengembangan selanjutnya.

## BAB 2
## GAMBARAN UMUM TOKO DUA INSAN STORY

### 2.1 Profil Toko Dua Insan Story

Toko Dua Insan Story adalah sebuah usaha yang bergerak di bidang industri kreatif dan percetakan, khususnya berfokus pada penyediaan jasa pembuatan desain undangan pernikahan. Berlokasi di Kota Pontianak, Kalimantan Barat, Toko Dua Insan Story didirikan dan dikelola oleh Ihzah Mahendra. Usaha ini hadir untuk menjawab kebutuhan masyarakat akan undangan yang estetis dan modern, baik dalam format digital (undangan web interaktif) untuk disebarkan melalui media sosial, maupun format cetak fisik untuk keperluan acara formal.

Toko Dua Insan Story menyediakan beragam pilihan tema dan kategori desain, dengan fokus utama pada undangan pernikahan. Produk yang ditawarkan terbagi menjadi dua kategori utama, yaitu:

1. **Undangan Digital** - berbentuk undangan web interaktif yang dapat dikustomisasi dan dibagikan secara online
2. **Undangan Cetak** - produk fisik dengan berbagai pilihan ukuran, jenis kertas, dan material tambahan

Dengan komitmen untuk memberikan hasil desain yang berkualitas, unik, dan sesuai dengan keinginan pelanggan, Toko Dua Insan Story bertujuan untuk menjadi mitra terpercaya dalam melengkapi momen-momen bahagia setiap pelanggan melalui media undangan yang berkesan.

Sebelum dikembangkannya sistem ini, seluruh proses operasional dan sistem pemesanan di Toko Dua Insan Story masih berjalan sepenuhnya secara konvensional dan belum memanfaatkan sistem informasi yang terintegrasi. Promosi dilakukan melalui media sosial seperti Instagram dan Facebook, namun proses pemesanan masih dilakukan secara manual melalui pesan langsung (Direct Message) atau aplikasi pesan instan seperti WhatsApp. Pencatatan pesanan, data acara pelanggan, hingga rekapitulasi pembayaran masih dicatat dalam buku tulis atau aplikasi catatan sederhana di ponsel. Kondisi inilah yang menjadi dasar dilakukannya penelitian untuk merancang dan membangun sebuah sistem pemesanan desain undangan berbasis web yang dapat meningkatkan efisiensi operasional dan memberikan pengalaman pengguna yang lebih baik.
### 2.2 Struktur Organisasi

Dalam rangka memastikan operasional bisnis jasa berjalan dengan lancar dan tepat waktu, Toko Dua Insan Story menerapkan struktur organisasi yang sederhana namun fungsional. Struktur ini mencerminkan pembagian peran serta tanggung jawab yang jelas dalam mengelola seluruh kegiatan usaha kreatif. Setiap posisi dalam struktur ini dirancang untuk menjalankan fungsi spesifik, mulai dari manajemen, pelayanan pelanggan, hingga proses produksi desain. Meskipun sederhana, struktur organisasi ini bertujuan untuk memaksimalkan efisiensi kerja, memastikan kualitas desain terjaga, dan menjamin kepuasan pelanggan terhadap hasil akhir undangan.

---

**[Tempatkan Gambar Bagan Struktur Organisasi di sini]**

*Sumber: Toko Dua Insan Story, 2025*  
**Gambar 2.1** Struktur Organisasi Toko Dua Insan Story

---

Struktur organisasi Toko Dua Insan Story menerapkan model fungsional yang dirancang untuk memastikan operasional bisnis berjalan secara terstruktur. Pucuk pimpinan dipegang oleh Pemilik (Owner), Ihzah Mahendra, yang memiliki wewenang penuh dalam menentukan arah kebijakan bisnis, menyediakan modal, serta memantau perkembangan usaha secara keseluruhan. Dalam praktiknya, pemilik juga merangkap sebagai administrator sistem dan desainer, sehingga memiliki kontrol penuh terhadap operasional bisnis.

Struktur organisasi saat ini bersifat fleksibel mengingat skala usaha yang masih tergolong usaha mikro dan dikelola oleh satu orang utama. Tugas dan tanggung jawab mencakup:

#### a. Pemilik/Owner

Bertanggung jawab dalam menentukan arah kebijakan bisnis, menyediakan modal usaha, memantau perkembangan usaha, dan mengambil keputusan strategis terkait pengembangan produk dan layanan. Pemilik juga berperan aktif dalam memantau operasional sistem pemesanan berbasis web dan mengevaluasi kepuasan pelanggan.

#### b. Administrator/Customer Service

Bertugas di garda terdepan untuk melayani komunikasi dengan pelanggan melalui sistem website, mulai dari mengelola katalog produk, memproses pesanan yang masuk, melakukan konfirmasi pembayaran, mengunggah bukti desain (design proof) untuk persetujuan pelanggan, serta menangani pertanyaan dan keluhan pelanggan secara responsif. Administrator juga bertugas mengelola promo, ulasan pelanggan, dan memantau status pesanan melalui dashboard admin.

#### c. Desainer Grafis

Bertanggung jawab penuh atas proses produksi desain undangan, mulai dari menerjemahkan data acara pelanggan ke dalam visual desain yang menarik, melakukan revisi sesuai masukan pelanggan, hingga menyiapkan file akhir (baik format digital interaktif maupun siap cetak). Desainer juga berkoordinasi dengan admin dalam mengunggah design proof ke dalam sistem untuk mendapatkan persetujuan pelanggan sebelum melanjutkan proses ke tahap produksi atau aktivasi undangan digital.

Koordinasi antar lini dilakukan secara langsung melalui sistem berbasis web yang telah dikembangkan, sehingga setiap pesanan dapat dilacak statusnya secara real-time dan memastikan setiap pesanan dapat diselesaikan sesuai tenggat waktu.
### 2.3 Tata Laksana Sistem Berjalan

Pada sistem yang berjalan saat ini di Toko Dua Insan Story, seluruh proses operasional, terutama alur pemesanan dan pelaporan, masih dijalankan sepenuhnya secara manual tanpa dukungan sistem informasi yang terintegrasi. Belum ada implementasi sistem berbasis web yang digunakan dalam kegiatan sehari-hari. Proses bisnis yang berjalan saat ini dapat diuraikan sebagai berikut:

#### a. Proses Pemesanan Manual

Pelanggan yang tertarik untuk memesan desain undangan harus terlebih dahulu menghubungi admin atau pemilik toko melalui aplikasi pesan instan (WhatsApp atau Direct Message di Instagram). Pelanggan akan meminta informasi mengenai katalog produk, harga, dan tata cara pemesanan.

Admin kemudian memberikan format data pesanan secara manual, yang harus diisi oleh pelanggan melalui pesan teks. Format ini mencakup informasi seperti:

- Nama lengkap mempelai (pengantin pria dan wanita)
- Nama orang tua mempelai
- Tanggal dan waktu acara (akad dan resepsi)
- Lokasi acara (alamat lengkap)
- Jumlah undangan yang dibutuhkan (untuk cetak)
- Jenis produk (digital atau cetak)
- Pilihan desain atau template

Setelah pelanggan mengisi data secara manual, admin melakukan perhitungan total harga berdasarkan jenis produk, jumlah pesanan, dan tambahan biaya lainnya seperti biaya cetak atau add-on. Total harga kemudian disampaikan kepada pelanggan melalui pesan.

Pelanggan melakukan pembayaran melalui transfer bank ke rekening pemilik dan mengirimkan bukti transfer berupa foto atau screenshot ke admin. Admin kemudian memverifikasi pembayaran secara manual dengan memeriksa rekening bank dan mencocokkan nominal pembayaran dengan pesanan.

Setelah pembayaran dinyatakan valid, admin mencatat pesanan tersebut ke dalam buku pesanan manual atau catatan digital sederhana (misalnya aplikasi Notes atau Google Sheets) dan meneruskan data pesanan kepada desainer untuk diproses lebih lanjut.

#### b. Proses Produksi dan Revisi

Desainer menerima data pesanan dari admin, kemudian mulai membuat desain undangan sesuai dengan data yang diberikan. Setelah desain selesai, desainer mengirimkan hasil desain kepada admin dalam bentuk file gambar atau PDF melalui aplikasi pesan instan.

Admin kemudian meneruskan file desain kepada pelanggan untuk dilakukan proses approval (persetujuan). Pelanggan meninjau desain dan memberikan feedback apakah desain sudah sesuai atau memerlukan revisi. Proses ini dilakukan berulang kali melalui pesan, tanpa ada sistem tracking yang jelas. Jika terjadi kesalahan komunikasi atau pesan terlewat, dapat menyebabkan delay dalam proses produksi.

Setelah desain disetujui oleh pelanggan, desainer melanjutkan ke proses finalisasi. Untuk undangan digital, desainer akan menyiapkan file final yang dapat dibagikan melalui media sosial. Untuk undangan cetak, file final akan dikirim ke percetakan untuk dicetak sesuai jumlah yang dipesan.

#### c. Proses Pelaporan

Pada akhir periode (bulanan), pemilik atau admin melakukan rekapitulasi manual dengan mengambil buku catatan pesanan yang telah terisi selama satu bulan. Admin kemudian menjumlahkan seluruh pendapatan pesanan menggunakan kalkulator dan mencatat hasil rekapitulasi tersebut ke dalam buku laporan bulanan.

Laporan yang dibuat mencakup jumlah pesanan, total pendapatan, jenis produk yang terjual (digital atau cetak), serta metode pembayaran yang digunakan. Proses ini sangat memakan waktu dan rentan terhadap kesalahan perhitungan karena dilakukan secara manual.

Pemilik kemudian memeriksa laporan tersebut secara visual untuk mengevaluasi kinerja bisnis dan menentukan strategi pemasaran ke depan. Tidak ada sistem otomatis yang memberikan insight atau dashboard statistik untuk mendukung pengambilan keputusan.

#### d. Permasalahan yang Dihadapi

Berdasarkan analisis terhadap sistem yang berjalan saat ini, terdapat beberapa permasalahan yang dihadapi oleh Toko Dua Insan Story, antara lain:

- **Risiko kesalahan informasi tinggi**, karena proses pengisian data acara dilakukan secara manual melalui pesan teks yang rawan typo atau terlewat
- **Proses pemesanan memakan waktu lama**, karena pelanggan harus menunggu balasan admin secara manual
- **Pencatatan pesanan tidak terstruktur**, sehingga sulit untuk melacak status pesanan secara real-time
- **Proses approval desain tidak efisien**, karena dilakukan melalui pesan instan tanpa sistem tracking yang jelas
- **Tidak ada sistem notifikasi otomatis** untuk mengingatkan pelanggan atau admin terkait status pesanan
- **Proses pelaporan memakan waktu lama** dan rentan terhadap kesalahan perhitungan manual
- **Tidak ada sistem katalog produk yang terstruktur**, sehingga pelanggan harus bertanya satu per satu untuk melihat produk yang tersedia
- **Tidak ada integrasi pembayaran online**, sehingga proses verifikasi pembayaran harus dilakukan secara manual

---

![Gambar 2.2 - Sistem Berjalan Pemesanan Undangan](images/gambar_2_2.png)

*Sumber: Analisis Sistem Berjalan, 2025*  
**Gambar 2.2** Sistem Berjalan Pemesanan Undangan

---

Pada Gambar 2.2 ditunjukkan flowchart sistem berjalan untuk proses Pemesanan Undangan, yang memetakan interaksi antara Pelanggan dan Admin. Proses dimulai dari sisi Pelanggan yang Melihat promosi di media sosial dan menghubungi Admin. Admin kemudian Memberikan format data pesanan secara manual melalui chat. Selanjutnya, Pelanggan melakukan proses manual dengan Mengisi data acara dan mengirimkannya kembali.

Setelah Admin Menghitung total harga, Pelanggan melakukan pembayaran transfer. Admin menerima bukti transfer dan masuk ke alur pemeriksaan manual untuk memvalidasi pembayaran. Jika valid, Admin akan Mencatat pesanan ke dalam Buku Pesanan, yang ditandai dengan simbol dokumen. Terakhir, Admin meneruskan data tersebut kepada bagian Desainer untuk diproses, dan proses pemesanan dianggap selesai di tahap administrasi.

---

![Gambar 2.3 - Sistem Berjalan Laporan Penjualan](images/gambar_2_3.png)

*Sumber: Analisis Sistem Berjalan, 2025*  
**Gambar 2.3** Sistem Berjalan Laporan Penjualan

---

Pada Gambar 2.3 ditunjukkan flowchart sistem berjalan untuk proses Laporan Penjualan, yang dilakukan oleh Pemilik atau Admin. Proses dimulai saat Admin Mengambil buku catatan pesanan yang telah terisi selama satu periode. Selanjutnya, Admin melakukan serangkaian proses manual. Pertama, Admin Menjumlahkan semua pendapatan pesanan menggunakan kalkulator, yang ditandai dengan simbol operasi manual. Kedua, hasil rekapitulasi tersebut dicatat dan dibuat di Buku Laporan Bulanan, yang ditandai dengan simbol dokumen. Terakhir, Pemilik Memeriksa laporan tersebut secara visual untuk mengevaluasi kinerja bisnis, yang juga merupakan operasi manual. Proses manual ini diakhiri setelah laporan disetujui atau diarsipkan oleh Pemilik.

Berdasarkan analisis terhadap sistem yang berjalan saat ini, dapat disimpulkan bahwa diperlukan sebuah sistem informasi berbasis web yang dapat mengotomatisasi proses pemesanan, pembayaran, approval desain, notifikasi, serta pelaporan untuk meningkatkan efisiensi operasional dan memberikan pengalaman pengguna yang lebih baik bagi pelanggan Toko Dua Insan Story.

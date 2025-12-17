PERANCANGAN SISTEM PEMESANAN DESAIN UNDANGAN BERBASIS WEB PADA TOKO DUA INSAN STORY

## BAB 1

## PENDAHULUAN

### 1.1 Latar Belakang

Di era digital saat ini, perkembangan teknologi informasi telah membawa perubahan signifikan dalam berbagai aspek kehidupan, termasuk dalam bidang bisnis dan layanan kreatif. Salah satu perubahan yang paling mencolok adalah peralihan dari sistem pemesanan konvensional menuju sistem berbasis online. Digitalisasi sistem pemesanan memberikan berbagai keuntungan, seperti kemudahan akses, fleksibilitas waktu, serta perluasan jangkauan pemasaran produk maupun jasa (Harianto dkk., 2021). Implementasi e-commerce dalam bisnis kreatif terbukti meningkatkan efisiensi operasional dan kepuasan pelanggan (Turban et al., 2018). Sejalan dengan perkembangan tersebut, penerapan website pada toko penjualan menjadi solusi penting agar pelanggan dapat melakukan pemesanan produk secara lebih mudah dan efisien.

Toko Dua Insan Story merupakan usaha lokal yang bergerak di bidang pembuatan desain undangan cetak untuk berbagai acara seperti pernikahan, tunangan, ulang tahun, dan acara resmi lainnya. Saat ini, proses pemesanan desain undangan masih dilakukan secara manual melalui pesan langsung di media sosial. Cara tersebut seringkali menimbulkan beberapa kendala, seperti risiko kesalahpahaman informasi, keterbatasan dalam melakukan penyesuaian desain secara interaktif, kesulitan pelanggan dalam melacak status pemesanan, serta tidak adanya sistem yang terstruktur untuk proses persetujuan desain (design proof approval).

Berdasarkan permasalahan yang telah diuraikan sebelumnya, diperlukan sebuah sistem pemesanan desain undangan berbasis online yang mampu meningkatkan kualitas pengalaman pengguna (user experience), mudah diakses oleh berbagai kalangan, serta mampu mempercepat dan mengefisienkan proses komunikasi antara pelanggan dan penyedia jasa. Pengalaman pengguna yang baik terbukti menjadi salah satu faktor kunci dalam keberhasilan aplikasi web modern (Norman, 2013).

Sistem yang dirancang diharapkan dapat menyediakan fitur-fitur yang mendukung seluruh proses pemesanan, mulai dari pemilihan produk hingga pengiriman kepada pelanggan. Adapun fitur-fitur utama yang diusulkan dalam sistem pemesanan desain undangan online ini antara lain sebagai berikut:

1. Katalog produk undangan, yang dilengkapi dengan fitur penyaringan (filter)  berdasarkan kategori, rentang harga, dan tingkat popularitas, sehingga  memudahkan pelanggan dalam memilih desain undangan yang sesuai dengan  tema acara yang diinginkan.
2. Formulir pemesanan online, yang dirancang dengan pengisian data acara  secara terstruktur, guna meminimalkan risiko kesalahan informasi yang sering  terjadi pada proses pemesanan secara manual.
3. Kalkulator biaya otomatis, yang berfungsi untuk menghitung total harga  pemesanan berdasarkan jumlah undangan, jenis kertas, serta tambahan  aksesoris, sehingga dapat memberikan transparansi harga kepada pelanggan.
4. Sistem persetujuan desain (design proof approval), yang memungkinkan  admin untuk mengunggah pratinjau desain, serta memberikan fasilitas bagi  pelanggan untuk memberikan persetujuan, mengajukan revisi, atau menolak  desain secara sistematis, disertai dengan pencatatan riwayat revisi (revision  tracking).
5. Integrasi sistem pembayaran online, melalui layanan Midtrans, yang  menyediakan opsi pembayaran uang muka (down payment) minimal sebesar 30% atau pembayaran penuh, sehingga memberikan fleksibilitas bagi  pelanggan dalam melakukan transaksi.
6. Perhitungan ongkos kirim otomatis, yang terintegrasi dengan API RajaOngkir,  dengan pilihan ekspedisi seperti JNE, POS, dan TIKI, serta berbagai jenis  layanan pengiriman.
7. Sistem notifikasi berbasis email, yang memberikan informasi kepada  pelanggan pada setiap tahapan pemesanan, meliputi konfirmasi pemesanan,  konfirmasi pembayaran, pengunggahan pratinjau desain, persetujuan desain,  hingga proses pengiriman.
8. Fitur pelacakan pesanan (order tracking), yang memungkinkan pelanggan  untuk memantau status pemesanan secara real-time, mulai dari proses  pemesanan hingga barang diterima oleh pelanggan.
9. Sistem ulasan dan penilaian (review and rating), yang berfungsi sebagai  sarana umpan balik pelanggan terhadap produk dan layanan, serta dapat  meningkatkan tingkat kepercayaan dan kredibilitas toko.

Laravel merupakan framework berbasis PHP yang dirancang untuk mempermudah proses pengembangan aplikasi web dengan menerapkan pola arsitektur Model-View-Controller (MVC) (Valenty dkk., 2024). Framework ini menyediakan berbagai fitur bawaan seperti sistem routing, authentication, template engine (Blade), serta Object Relational Mapping (ORM) melalui Eloquent untuk mempermudah interaksi dengan basis data. Penerapan Laravel memberikan sejumlah keuntungan, antara lain peningkatan efisiensi waktu pengembangan, konsistensi kode, serta keamanan yang lebih baik dalam mengelola proses autentikasi dan transaksi data (Stauffer, 2019). Dengan sintaks yang bersih dan struktur yang terorganisir, Laravel banyak digunakan dalam pengembangan sistem informasi modern karena dapat meminimalisasi kesalahan logika dan mempercepat proses implementasi.

React merupakan library JavaScript yang dikembangkan untuk membangun antarmuka pengguna (user interface) yang dinamis dan responsif (Santoso dkk., 2023). React menggunakan konsep komponen (component-based architecture), yang memungkinkan pengembang untuk membangun elemen antarmuka secara modular dan dapat digunakan kembali. Dengan konsep Virtual DOM, React mampu memperbarui tampilan halaman secara efisien tanpa perlu memuat ulang seluruh konten, sehingga memberikan pengalaman pengguna yang lebih cepat dan interaktif (Banks & Porcello, 2020). Next.js adalah framework berbasis React yang menyediakan fitur tambahan seperti server-side rendering dan routing otomatis, sangat cocok untuk pengembangan dashboard administrator yang membutuhkan performa tinggi.

Dalam penelitian ini, sistem pemesanan desain undangan online akan dikembangkan dengan menggunakan Laravel sebagai kerangka kerja utama pada sisi backend, React.js dengan Vite untuk antarmuka pelanggan (customer-facing website), dan Next.js (framework React) untuk dashboard administrator. Laravel akan menangani logika bisnis, autentikasi pengguna, pengelolaan data, serta integrasi dengan basis data dan layanan pihak ketiga. Sedangkan React dan Next.js akan digunakan untuk menampilkan antarmuka pengguna yang interaktif, dinamis, dan mudah digunakan.

Untuk mendukung proses transaksi, sistem ini akan diintegrasikan dengan layanan payment gateway Midtrans, yang memungkinkan pengguna melakukan pembayaran melalui berbagai metode, seperti transfer bank, kartu debit/kredit, maupun e-wallet. Integrasi payment gateway dalam sistem e-commerce meningkatkan kepercayaan konsumen dan keamanan transaksi (Laudon & Traver, 2021). Sistem juga menyediakan opsi pembayaran dengan down payment (DP) minimum 30% dari total pesanan, memberikan fleksibilitas kepada pelanggan untuk melakukan pembayaran secara bertahap. Pembayaran sisa dapat dilakukan setelah desain disetujui atau sebelum proses produksi dimulai.

Untuk mendukung pengiriman undangan cetak kepada pelanggan di berbagai daerah, sistem ini juga diintegrasikan dengan RajaOngkir API. RajaOngkir merupakan layanan penyedia data ongkos kirim yang memungkinkan perhitungan biaya pengiriman secara otomatis dan real-time berdasarkan lokasi tujuan (provinsi, kota, dan kecamatan), berat produk, dan pilihan kurir (Wibowo & Susanto, 2022). Sistem mendukung beberapa jasa ekspedisi populer seperti JNE, POS Indonesia, dan TIKI dengan berbagai pilihan layanan pengiriman (reguler, express, atau same-day service untuk wilayah tertentu). Integrasi API pihak ketiga untuk perhitungan ongkos kirim telah terbukti meningkatkan efisiensi operasional dan kepuasan pelanggan dalam sistem e-commerce (Prasetyo & Widodo, 2023). Integrasi ini memberikan transparansi biaya kepada pelanggan sebelum melakukan pembayaran, sehingga tidak ada biaya tersembunyi dan pelanggan dapat memilih opsi pengiriman yang sesuai dengan kebutuhan dan budget mereka.

Salah satu fitur unggulan dalam sistem ini adalah **sistem design proof approval** yang terstruktur. Workflow approval yang sistematis dalam proses desain terbukti efektif mengurangi kesalahan produksi dan meningkatkan kepuasan klien (Nielsen, 2020; Garrett, 2021). Setelah pelanggan melakukan pemesanan dan pembayaran, admin atau desainer akan membuat desain undangan sesuai dengan data yang diberikan. Desain tersebut kemudian diunggah ke sistem sebagai design proof (bukti desain) yang dapat diakses oleh pelanggan melalui dashboard mereka. Pelanggan memiliki tiga opsi: menyetujui desain (approve), meminta revisi dengan memberikan catatan spesifik, atau menolak desain jika tidak sesuai dengan ekspektasi. Setiap interaksi tercatat dalam sistem dengan timestamp, memudahkan tracking history revisi dan komunikasi antara pelanggan dengan penyedia jasa (Sommerville, 2021). Proses ini memastikan bahwa tidak ada kesalahpahaman dalam desain akhir, dan produksi hanya dimulai setelah pelanggan memberikan persetujuan final. Sistem notifikasi email akan dikirim secara otomatis pada setiap tahap approval untuk menjaga transparansi komunikasi.

Dengan adanya sistem pemesanan desain undangan online ini, diharapkan  dapat meningkatkan efisiensi operasional, mengurangi kesalahan komunikasi, serta memberikan pengalaman pengguna yang lebih baik bagi pelanggan maupun pengelola usaha.

### 1.2 Rumusan Masalah

 Berdasarkan uraian permasalahan pada latar belakang, perumusan masalah dalam penelitian ini adalah:
"Bagaimana merancang dan membangun sistem pemesanan desain undangan cetak berbasis web pada Toko Dua Insan Story yang mampu menggantikan proses pemesanan manual, meningkatkan efisiensi komunikasi antara pelanggan dan penyedia jasa, meminimalkan kesalahan informasi pemesanan, serta menyediakan fitur katalog desain, sistem persetujuan bukti desain (design proof approval) dengan pelacakan revisi, perhitungan ongkos kirim otomatis, dan integrasi pembayaran online guna mendukung layanan yang cepat, transparan, dan profesional?"

### 1.3  Batasan CAPSTONE PROJECT

 Penelitian ini dibatasi agar tetap fokus pada tujuan yang ingin dicapai serta dapat diselesaikan sesuai dengan ruang lingkup Capstone Project. Ruang lingkup penelitian meliputi perancangan dan pembangunan sistem pemesanan desain undangan cetak berbasis web dengan menggunakan Laravel 12 sebagai backend, React.js dengan Vite untuk antarmuka pelanggan (customer frontend), Next.js untuk dashboard administrator, serta MySQL sebagai basis data.
 Fitur utama yang dikembangkan dalam sistem ini meliputi katalog desain undangan cetak, formulir pemesanan online dengan opsi kustomisasi, pengisian data acara oleh pelanggan, sistem persetujuan bukti desain (design proof approval) dengan alur persetujuan, revisi, dan penolakan, notifikasi status pesanan melalui email, perhitungan ongkos kirim otomatis melalui integrasi RajaOngkir API, serta integrasi pembayaran online menggunakan Midtrans dengan opsi pembayaran uang muka (down payment) dan pembayaran penuh (full payment).
 Adapun beberapa aspek yang tidak termasuk dalam cakupan penelitian ini adalah sebagai berikut:

1. Undangan digital berbasis web (web-based invitation templates), karena fitur tersebut direncanakan sebagai pengembangan lanjutan di masa mendatang.
2. Manajemen stok bahan baku fisik percetakan, seperti kertas, tinta, amplop, dan aksesoris lainnya.
3. Integrasi langsung dengan mesin cetak atau printer industri.
4. Modul akuntansi lanjutan, seperti general ledger, arus kas (cash flow), laporan laba rugi, dan pelaporan pajak.
5. Fitur multi-user dengan pemisahan peran secara rinci, seperti admin, desainer, operator cetak, kurir, dan gudang.
6. Sistem inventory management untuk pelacakan bahan baku dan produk jadi (finished goods).
7. Integrasi dengan sistem Enterprise Resource Planning (ERP) atau perangkat lunak akuntansi pihak ketiga, seperti Accurate, Zahir, atau SAP.
8. Fitur Customer Relationship Management (CRM) lanjutan, seperti otomatisasi pemasaran email (email marketing automation) dan segmentasi pelanggan.
9. Sistem loyalty program atau keanggotaan (membership) dengan skema poin atau reward.
Dengan adanya batasan tersebut, penelitian ini diharapkan dapat menghasilkan sistem yang terfokus, terukur, dan relevan dengan kebutuhan utama Toko Dua Insan Story, tanpa meluas ke aspek-aspek di luar tujuan utama penelitian.

### 1.4  Tujuan CAPSTONE PROJECT

 Tujuan dari penelitian ini adalah untuk merancang dan membangun sistem pemesanan desain undangan cetak berbasis web pada Toko Dua Insan Story sebagai pengganti proses pemesanan manual. Sistem ini dikembangkan menggunakan Laravel dan React.js/Next.js dengan basis data MySQL, dengan harapan dapat meningkatkan efisiensi proses pemesanan serta komunikasi antara pelanggan dan penyedia jasa, mengurangi risiko kesalahan informasi, dan mempercepat proses konfirmasi pesanan.
Secara khusus, tujuan dari pengembangan sistem ini adalah sebagai berikut:

1. Mengembangkan sistem pemesanan undangan cetak berbasis web yang  memungkinkan pelanggan melakukan pemesanan secara mandiri melalui  antarmuka yang interaktif dan responsif.
2. Menyediakan fitur katalog desain undangan yang memudahkan pelanggan  dalam memilih template sesuai dengan kebutuhan dan tema acara.
3. Mengimplementasikan formulir pemesanan dengan opsi kustomisasi, meliputi  pengisian data acara, pilihan kertas, ukuran undangan, serta tambahan  aksesoris.
4. Mengembangkan sistem persetujuan bukti desain (design proof approval)  yang terstruktur untuk memfasilitasi proses persetujuan, revisi, dan penolakan  desain, serta mendokumentasikan seluruh riwayat revisi secara sistematis.
5. Mengotomatisasi perhitungan biaya pengiriman berdasarkan lokasi tujuan  melalui integrasi RajaOngkir API.
6. Mengintegrasikan sistem pembayaran online yang aman dan efisien melalui  Midtrans, dengan opsi pembayaran uang muka (down payment) dan  pembayaran penuh.
7. Memastikan bahwa proses produksi undangan hanya dimulai setelah  pelanggan memberikan persetujuan akhir terhadap desain yang diajukan.
 Dengan tercapainya tujuan-tujuan tersebut, diharapkan sistem yang dikembangkan dapat mendukung peningkatan kualitas layanan, profesionalisme, serta kepuasan pelanggan pada Toko Dua Insan Story.

### 1.5  Manfaat CAPSTONE PROJECT

a. Manfaat bagi Penulis
Capstone Project ini memberikan kesempatan bagi penulis untuk merancang dan membangun aplikasi web secara full-stack, mulai dari perancangan backend hingga implementasi frontend. Melalui penelitian ini, penulis memperoleh pengalaman dalam penerapan arsitektur Model–View–Controller (MVC) menggunakan framework Laravel, pengelolaan basis data MySQL, serta penerapan konsep komponen dan state management pada React.js dan Next.js. Selain itu, penulis juga mendapatkan pengalaman praktis dalam mengintegrasikan sistem dengan layanan pihak ketiga, seperti payment gateway Midtrans dan layanan perhitungan ongkos kirim melalui RajaOngkir API. Hasil dari Capstone Project ini diharapkan dapat menjadi portofolio yang bernilai serta menjadi referensi bagi penulis dalam pengembangan aplikasi web modern, khususnya pada sistem pemesanan dan e-commerce berbasis web.
b.  Manfaat bagi Pengguna
Bagi Toko Dua Insan Story, penelitian ini memberikan manfaat berupa peningkatan efisiensi dan profesionalitas dalam proses pemesanan desain undangan cetak. Sistem yang dikembangkan memungkinkan pengelolaan pesanan secara lebih terstruktur, mempercepat proses konfirmasi, serta mengurangi ketergantungan pada komunikasi manual yang berpotensi menimbulkan kesalahan informasi.
Selain itu, pelanggan memperoleh kemudahan dalam melakukan pemesanan melalui katalog desain yang lengkap, sistem persetujuan bukti desain (design proof approval) dengan pelacakan riwayat revisi yang jelas, perhitungan ongkos kirim yang transparan, serta notifikasi otomatis pada setiap tahap pemesanan. Dengan adanya sistem design proof approval yang terstruktur, risiko kesalahan produksi dapat diminimalkan karena pelanggan memiliki kendali penuh terhadap persetujuan desain akhir sebelum memasuki tahap produksi. Secara keseluruhan, sistem ini diharapkan dapat membantu Toko Dua Insan Story dalam memperluas jangkauan pemasaran secara online, meningkatkan kepuasan pelanggan, serta menyediakan data pemesanan yang dapat dimanfaatkan sebagai dasar dalam pengambilan keputusan bisnis.

### 1.6  Metodologi Perancangan Solusi

 Metode perancangan perangkat lunak yang digunakan adalah Extreme Programming (XP). XP menekankan kolaborasi erat antara pengembang dan pengguna serta iterasi cepat dalam proses pengembangan (Beck & Andres, 2004). Kegiatan utama meliputi perencanaan, perancangan, pengkodean, dan pengujian.
a. Planning (Perencanaan)
Identifikasi masalah dilakukan melalui observasi dan wawancara dengan pemilik. Hasilnya berupa daftar kebutuhan fungsional dan non-fungsional serta analisis alur pemesanan manual yang kemudian dijadikan dasar rancangan solusi berbasis web. Pada tahap ini juga dilakukan analisis terhadap proses bisnis yang berjalan, identifikasi pain points dalam sistem manual, serta penentuan prioritas fitur yang akan dikembangkan. User stories dibuat untuk setiap fitur utama, seperti "Sebagai pelanggan, saya ingin melihat pratinjau desain undangan saya agar dapat memberikan persetujuan atau meminta revisi".
b. Design (Perancangan)  
Hasil analisis kebutuhan diterjemahkan ke dalam model dan rancangan sistem, termasuk arsitektur sistem, perancangan antarmuka menggunakan React.js dan Next.js, dan perancangan basis data menggunakan ERD. Pemodelan proses bisnis dan diagram UML juga disusun untuk memastikan keterpaduan komponen (Pressman & Maxim, 2020). Pada tahap ini dirancang pula struktur database dengan 55 tabel yang mencakup entitas users, products, orders, design proofs, payments, shipping, dan lain-lain. Perancangan API endpoints juga dilakukan untuk memastikan komunikasi yang efisien antara backend dan frontend.
c. Coding (Pengkodean)
Implementasi dilakukan dengan menerjemahkan rancangan ke dalam kode menggunakan Laravel 12 (backend API), React.js dengan Vite untuk situs pelanggan, dan Next.js 15 untuk dashboard administrator. MySQL digunakan sebagai basis data untuk menyimpan data pemesanan, informasi pelanggan, design proofs, dan informasi produk. Database relasional seperti MySQL terbukti efektif untuk mengelola data transaksional dalam sistem e-commerce (Elmasri & Navathe, 2016). Pengkodean dilakukan secara iteratif dengan fokus pada satu fitur dalam satu waktu (feature-based development). Setiap fitur yang selesai di-commit ke version control system (Git) untuk memudahkan tracking perubahan dan kolaborasi.
d. Testing (Pengujian)
Setelah pengkodean, dilakukan pengujian fungsional untuk memverifikasi kesesuaian sistem terhadap kebutuhan pengguna, termasuk pengujian fitur pemesanan, kustomisasi produk, sistem design proof approval (approve/revision/reject), notifikasi email, perhitungan ongkos kirim via RajaOngkir, dan integrasi pembayaran online melalui Midtrans. Pengujian dilakukan secara manual (manual testing) maupun otomatis (automated testing) menggunakan PHPUnit untuk backend dan Jest untuk frontend. User acceptance testing (UAT) juga dilakukan dengan melibatkan pemilik toko untuk memastikan sistem sesuai dengan ekspektasi dan kebutuhan bisnis.

1.7  Sistematika Penulisan
Berikut gambaran singkat sistematika penulisan laporan:
BAB 1 PENDAHULUAN
Gambaran umum penelitian, meliputi latar belakang, perumusan masalah, batasan penelitian, tujuan dan manfaat, metodologi, dan sistematika penulisan.
BAB 2 TEMPAT CAPSTONE PROJECT  
Profil objek penelitian, layanan, proses bisnis, dan struktur organisasi.
BAB 3 PERANCANGAN SOLUSI
Analisis kebutuhan, desain sistem (UML, ERD), perancangan antarmuka, dan langkah implementasi.
BAB 4 PENUTUP
Kesimpulan dan saran untuk pengembangan selanjutnya.

## BAB 2

## GAMBARAN UMUM TOKO DUA INSAN STORY

### 2.1 Profil Toko Dua Insan Story

Toko Dua Insan Story adalah sebuah usaha yang bergerak di bidang industri kreatif dan percetakan, khususnya berfokus pada penyediaan jasa pembuatan desain undangan pernikahan cetak berkualitas tinggi. Berlokasi di Kota Pontianak, Kalimantan Barat, Toko Dua Insan Story didirikan dan dikelola oleh Ihzah Mahendra. Usaha ini hadir untuk menjawab kebutuhan masyarakat akan undangan yang estetis dan modern dalam format cetak fisik untuk keperluan acara formal.

Produk utama yang ditawarkan adalah **Undangan Cetak**, yaitu undangan fisik berkualitas tinggi dengan berbagai pilihan desain, ukuran, jenis kertas, dan material tambahan. Pelanggan dapat memilih dari berbagai template desain yang tersedia dalam katalog online, kemudian menyesuaikannya dengan data acara pribadi seperti nama mempelai, nama orang tua mempelai, tanggal dan waktu acara (akad nikah dan resepsi), lokasi acara dengan alamat lengkap, serta informasi penting lainnya seperti dress code atau link live streaming untuk acara hybrid.

Toko Dua Insan Story menyediakan berbagai varian produk undangan cetak yang dapat disesuaikan dengan kebutuhan dan budget pelanggan, antara lain:

**Pilihan Ukuran:**

- **Standar** (10 x 15 cm) - Ukuran paling populer dan ekonomis
- **Premium** (15 x 20 cm) - Ukuran lebih besar dengan kesan lebih mewah
- **Eksklusif** (custom size) - Ukuran khusus sesuai permintaan pelanggan

**Jenis Kertas:**

- **Art Paper** (150-260 gsm) - Kertas standar dengan permukaan halus dan hasil cetak tajam
- **Ivory** (210-310 gsm) - Kertas premium dengan tekstur sedikit kasar dan kesan natural
- **Linen** (200-300 gsm) - Kertas dengan motif garis-garis halus memberikan kesan elegan
- **Jasmine** (200-260 gsm) - Kertas tekstur yang memberikan kesan soft dan mewah
- **Art Carton** (190-260 gsm) - Kertas tebal dan kokoh cocok untuk undangan lipat

**Material dan Aksesoris Tambahan:**

- **Amplop** - Amplop custom dengan berbagai warna dan bahan (kertas, kain, atau plastik bening)
- **Stiker Segel** - Stiker custom dengan nama atau inisial mempelai untuk menutup amplop
- **Pita/Ribbon** - Pita satin atau organza berbagai warna sebagai hiasan
- **Box Eksklusif** - Box packaging premium untuk undangan yang lebih mewah
- **Kartu Ucapan Terima Kasih** - Thank you card yang disisipkan dalam undangan
- **Kartu Informasi Tambahan** - Info akomodasi, peta lokasi, atau protokol kesehatan

**Pilihan Finishing:**

- **Laminasi Glossy** - Permukaan mengkilap yang memberikan warna lebih vibrant
- **Laminasi Doff** - Permukaan tidak mengkilap dengan kesan lebih elegan dan premium
- **Hot Print** - Cetak menggunakan teknik hot stamping dengan foil emas atau perak
- **Emboss** - Teknik timbul pada bagian tertentu untuk memberikan dimensi
- **Spot UV** - Lapisan UV pada area tertentu untuk efek mengkilap selektif

Setiap pesanan undangan dapat disesuaikan dengan kebutuhan pelanggan, termasuk pemilihan warna tema yang disesuaikan dengan tema acara, penambahan ornamen khusus seperti bunga, daun, atau motif tradisional, serta berbagai opsi finishing untuk memberikan kesan lebih eksklusif. Sistem pemesanan online yang dikembangkan memungkinkan pelanggan untuk melihat estimasi harga secara real-time berdasarkan pilihan yang mereka buat.

Dengan komitmen untuk memberikan hasil desain yang berkualitas, unik, dan sesuai dengan keinginan pelanggan, Toko Dua Insan Story bertujuan untuk menjadi mitra terpercaya dalam melengkapi momen-momen bahagia setiap pelanggan melalui media undangan cetak yang berkesan. Proses produksi dilakukan dengan standar quality control yang ketat, memastikan setiap undangan yang dikirimkan dalam kondisi sempurna.

Sebelum dikembangkannya sistem ini, seluruh proses operasional dan sistem pemesanan di Toko Dua Insan Story masih berjalan sepenuhnya secara konvensional dan belum memanfaatkan sistem informasi yang terintegrasi. Promosi dilakukan melalui media sosial seperti Instagram dan Facebook, namun proses pemesanan masih dilakukan secara manual melalui pesan langsung (Direct Message) atau aplikasi pesan instan seperti WhatsApp. Pencatatan pesanan, data acara pelanggan, hingga rekapitulasi pembayaran masih dicatat dalam buku tulis atau aplikasi catatan sederhana di ponsel. Proses persetujuan desain (design proof approval) dilakukan melalui pengiriman file gambar via WhatsApp tanpa tracking yang jelas, seringkali menyebabkan kebingungan tentang versi desain mana yang sudah disetujui atau masih memerlukan revisi. Kondisi inilah yang menjadi dasar dilakukannya penelitian untuk merancang dan membangun sebuah sistem pemesanan desain undangan berbasis web yang dapat meningkatkan efisiensi operasional dan memberikan pengalaman pengguna yang lebih baik.

### 2.2 Struktur Organisasi

Dalam rangka memastikan operasional bisnis jasa berjalan dengan lancar dan tepat waktu, Toko Dua Insan Story menerapkan struktur organisasi yang sederhana namun fungsional. Struktur ini mencerminkan pembagian peran serta tanggung jawab yang jelas dalam mengelola seluruh kegiatan usaha kreatif. Setiap posisi dalam struktur ini dirancang untuk menjalankan fungsi spesifik, mulai dari manajemen, pelayanan pelanggan, hingga proses produksi desain. Meskipun sederhana, struktur organisasi ini bertujuan untuk memaksimalkan efisiensi kerja, memastikan kualitas desain terjaga, dan menjamin kepuasan pelanggan terhadap hasil akhir undangan.

---

![Gambar 2.1 - Struktur Organisasi Toko Dua Insan Story](images/2.1-fix.png)

*Sumber: Toko Dua Insan Story, 2025*  
**Gambar 2.1** Struktur Organisasi Toko Dua Insan Story

---

Struktur organisasi Toko Dua Insan Story menerapkan model fungsional yang dirancang untuk memastikan operasional bisnis berjalan secara terstruktur. Pucuk pimpinan dipegang oleh Pemilik (Owner), Ihzah Mahendra, yang memiliki wewenang penuh dalam menentukan arah kebijakan bisnis, menyediakan modal, serta memantau perkembangan usaha secara keseluruhan. Dalam praktiknya, pemilik juga merangkap sebagai administrator sistem dan desainer, sehingga memiliki kontrol penuh terhadap operasional bisnis.

Struktur organisasi saat ini bersifat fleksibel mengingat skala usaha yang masih tergolong usaha mikro dan dikelola oleh satu orang utama. Tugas dan tanggung jawab mencakup:

#### a. Pemilik/Owner

Bertanggung jawab dalam menentukan arah kebijakan bisnis, menyediakan modal usaha, memantau perkembangan usaha, dan mengambil keputusan strategis terkait pengembangan produk dan layanan. Pemilik juga berperan aktif dalam memantau operasional sistem pemesanan berbasis web, mengevaluasi kepuasan pelanggan melalui review dan rating yang masuk, serta menganalisis data penjualan untuk menentukan strategi marketing dan pengembangan produk baru.

#### b. Administrator/Customer Service

Bertugas di garda terdepan untuk melayani komunikasi dengan pelanggan melalui sistem website, mulai dari mengelola katalog produk, memproses pesanan yang masuk, melakukan konfirmasi pembayaran melalui dashboard admin, mengelola sistem design proof approval dengan mengunggah bukti desain untuk persetujuan pelanggan, serta menangani pertanyaan dan keluhan pelanggan secara responsif melalui sistem atau komunikasi langsung. Administrator juga bertugas mengelola promo code, memverifikasi dan merespons ulasan pelanggan, memproses permintaan pembatalan pesanan dengan workflow approval, serta memantau status pesanan melalui dashboard admin untuk memastikan setiap pesanan diproses tepat waktu. Dengan adanya sistem terintegrasi, administrator dapat melakukan bulk update status pesanan, export data pesanan untuk keperluan laporan, dan mengelola shipping tracking number untuk pesanan yang sudah dikirim.

#### c. Desainer Grafis

Bertanggung jawab penuh atas proses produksi desain undangan, mulai dari menerjemahkan data acara pelanggan yang diinput melalui formulir online ke dalam visual desain yang menarik dan sesuai tema, melakukan revisi sesuai masukan pelanggan yang disampaikan melalui sistem design proof approval, hingga menyiapkan file akhir siap cetak dalam format yang sesuai (biasanya PDF print-ready dengan bleed dan crop marks). Desainer berkoordinasi dengan admin dalam mengunggah design proof ke dalam sistem untuk mendapatkan persetujuan pelanggan sebelum melanjutkan proses ke tahap produksi. Setiap revisi yang diminta pelanggan tercatat dalam sistem dengan timestamp dan notes spesifik, memudahkan desainer untuk memahami perubahan yang diinginkan tanpa harus melakukan komunikasi bolak-balik melalui chat. Setelah design proof mendapat status "Approved" dari pelanggan, desainer menyiapkan file final dan mengirimkannya ke percetakan mitra untuk proses produksi fisik.

#### d. Koordinasi Antar Lini

Koordinasi antar lini dilakukan secara terintegrasi melalui sistem berbasis web yang telah dikembangkan. Setiap pesanan memiliki status tracking yang dapat dilihat oleh semua pihak terkait (pemilik, admin, desainer) secara real-time. Sistem notifikasi email otomatis memastikan setiap pihak mendapat informasi update status pesanan. Misalnya, ketika pelanggan melakukan pembayaran, admin mendapat notifikasi untuk memverifikasi pembayaran; setelah diverifikasi, desainer mendapat notifikasi untuk mulai membuat desain; setelah design proof di-upload, pelanggan mendapat notifikasi untuk melakukan review dan approval. Proses terintegrasi ini memastikan setiap pesanan dapat diselesaikan sesuai tenggat waktu dan meminimalisir kesalahan komunikasi yang sering terjadi pada sistem manual.

### 2.3 Tata Laksana Sistem Berjalan

Pada sistem yang berjalan saat ini di Toko Dua Insan Story, seluruh proses operasional, terutama alur pemesanan dan pelaporan, masih dijalankan sepenuhnya secara manual tanpa dukungan sistem informasi yang terintegrasi. Belum ada implementasi sistem berbasis web yang digunakan dalam kegiatan sehari-hari. Proses bisnis yang berjalan saat ini dapat diuraikan sebagai berikut:

#### a. Proses Pemesanan Manual

Pelanggan yang tertarik untuk memesan desain undangan harus terlebih dahulu menghubungi admin atau pemilik toko melalui aplikasi pesan instan (WhatsApp atau Direct Message di Instagram). Pelanggan akan meminta informasi mengenai katalog produk, harga, dan tata cara pemesanan. Tidak ada katalog online yang terstruktur, sehingga pelanggan harus bertanya satu per satu tentang desain yang tersedia, harga per desain, pilihan kertas, dan aksesoris tambahan.

Admin kemudian memberikan format data pesanan secara manual melalui pesan teks atau dokumen, yang harus diisi oleh pelanggan. Format ini mencakup informasi seperti:

- Nama lengkap mempelai pria dan wanita beserta gelar (jika ada)
- Nama orang tua mempelai dari kedua belah pihak
- Anak keberapa dari berapa bersaudara (opsional, untuk undangan adat tertentu)
- Tanggal dan waktu acara akad nikah
- Tanggal dan waktu acara resepsi/walimatul ursy
- Lokasi acara dengan alamat lengkap (gedung, jalan, kota)
- Dress code atau tema warna acara
- Jumlah undangan yang dibutuhkan (untuk cetak)
- Jenis produk: pilihan template desain (dikirim dalam bentuk gambar via chat)
- Pilihan kertas (Art Paper, Ivory, Linen, dll)
- Pilihan ukuran (10x15 cm, 15x20 cm, atau custom)
- Aksesoris tambahan (amplop, stiker, pita, box)
- Pilihan finishing (laminasi glossy/doff, hot print, emboss)
- Alamat pengiriman lengkap dengan kode pos

Setelah pelanggan mengisi data secara manual dan mengirimkannya kembali via chat, admin melakukan perhitungan total harga berdasarkan jenis produk, jumlah pesanan, pilihan kertas, aksesoris tambahan, dan biaya finishing. Perhitungan biaya cetak dilakukan secara manual menggunakan kalkulator dengan rumus:

```
Total = (Harga Base Design x Jumlah) + (Harga Kertas x Jumlah) + 
        (Harga Aksesoris x Jumlah) + (Biaya Finishing x Jumlah)
```

Perhitungan ongkos kirim juga dilakukan secara manual dengan menghubungi ekspedisi atau mengecek website ekspedisi satu per satu (JNE, POS, TIKI) untuk mendapatkan estimasi biaya berdasarkan berat dan tujuan pengiriman. Berat produk dihitung manual berdasarkan perkiraan berat kertas dan packaging. Proses ini memakan waktu lama dan rentan terhadap kesalahan perhitungan.

Total harga final (harga produk + ongkos kirim) kemudian disampaikan kepada pelanggan melalui pesan. Jika pelanggan setuju dengan harga, proses dilanjutkan ke pembayaran. Jika tidak setuju atau ingin negosiasi, proses diskusi harga dilakukan via chat yang bisa memakan waktu berhari-hari.

Pelanggan melakukan pembayaran melalui transfer bank ke rekening pemilik dan mengirimkan bukti transfer berupa foto atau screenshot ke admin via chat. Admin kemudian memverifikasi pembayaran secara manual dengan membuka aplikasi mobile banking, memeriksa mutasi rekening, dan mencocokkan nominal pembayaran dengan pesanan. Proses verifikasi bisa memakan waktu beberapa jam hingga satu hari kerja tergantung kesibukan admin.

Setelah pembayaran dinyatakan valid, admin mencatat pesanan tersebut ke dalam buku pesanan manual (buku tulis fisik) atau catatan digital sederhana (misalnya aplikasi Notes di smartphone atau Google Sheets) dengan informasi:

- Nomor pesanan (manual numbering, misal: INV-001)
- Nama pelanggan
- Nomor HP pelanggan
- Tanggal pemesanan
- Jumlah pesanan
- Total pembayaran
- Status pembayaran (DP atau Lunas)
- Tanggal acara pelanggan (sebagai deadline produksi)

Data pesanan kemudian diteruskan kepada desainer (yang bisa jadi orang yang sama dengan admin/pemilik) untuk diproses lebih lanjut. Tidak ada sistem notifikasi otomatis, sehingga pemberitahuan dilakukan via chat atau komunikasi lisan.

#### b. Proses Produksi dan Revisi

Desainer menerima data pesanan dari admin dalam bentuk pesan teks atau dokumen, kemudian mulai membuat desain undangan sesuai dengan data yang diberikan menggunakan software desain grafis seperti Adobe Illustrator, Photoshop, atau Canva. Proses desain bisa memakan waktu 1-3 hari kerja tergantung kompleksitas desain dan jumlah antrian pesanan.

Setelah desain selesai, desainer mengirimkan hasil desain kepada admin dalam bentuk file gambar (JPEG atau PNG) dengan watermark "DRAFT" atau "PROOF" melalui aplikasi pesan instan atau email. Admin kemudian meneruskan file desain kepada pelanggan untuk dilakukan proses approval (persetujuan).

Pelanggan meninjau desain melalui file gambar yang dikirim via WhatsApp atau email dan memberikan feedback apakah desain sudah sesuai atau memerlukan revisi. Feedback disampaikan melalui pesan teks yang seringkali tidak spesifik, misalnya:

- "Warna kurang cocok"
- "Font-nya diganti yang lebih elegan"
- "Nama ayah saya salah"
- "Tanggalnya harusnya 15 bukan 16"

Proses komunikasi revisi ini dilakukan berulang kali melalui pesan chat tanpa ada sistem tracking yang jelas. Masalah yang sering terjadi:

- **Tidak ada history revisi**: Tidak jelas versi desain yang mana yang sudah di-review atau belum
- **Pesan terlewat**: Chat bisa tertumpuk dengan percakapan lain, menyebabkan revisi terlewat
- **Ambiguitas feedback**: Komentar pelanggan tidak spesifik, desainer harus bertanya ulang berkali-kali
- **Tidak ada deadline revisi**: Pelanggan bisa memberikan feedback kapan saja, menyebabkan delay produksi
- **File hilang**: File desain versi lama sulit ditemukan kembali jika pelanggan ingin kembali ke versi sebelumnya

Setelah desain disetujui oleh pelanggan (biasanya pelanggan mengirim pesan "OK, sudah cocok" atau "Approved"), desainer melanjutkan ke proses finalisasi. Namun, tidak jarang terjadi pelanggan tiba-tiba meminta revisi lagi setelah "approved" karena tidak ada konfirmasi formal yang mengikat.

Untuk undangan cetak, file final disiapkan dalam format print-ready (PDF dengan CMYK color mode, resolusi 300 dpi, sudah termasuk bleed 3mm dan crop marks). File ini kemudian dikirim ke percetakan mitra melalui email atau aplikasi pesan. Tidak ada tracking otomatis untuk status produksi di percetakan.

#### c. Proses Pelaporan

Pada akhir periode (bulanan), pemilik atau admin melakukan rekapitulasi manual dengan langkah sebagai berikut:

1. **Mengambil buku catatan pesanan** yang telah terisi selama satu bulan
2. **Menjumlahkan seluruh pendapatan pesanan** menggunakan kalkulator manual, dengan mengelompokkan berdasarkan:
   - Total pesanan undangan cetak
   - Jenis kertas yang paling banyak dipesan
   - Ukuran undangan yang populer
   - Aksesoris tambahan yang sering dibeli
   - Metode pembayaran (transfer bank, e-wallet)
   - Status pembayaran (DP atau Lunas)
3. **Mencatat hasil rekapitulasi** tersebut ke dalam buku laporan bulanan dengan format tabel sederhana
4. **Membuat laporan pendapatan** dengan rincian:
   - Jumlah total pesanan bulan ini
   - Total pendapatan bulan ini
   - Rata-rata nilai pesanan
   - Produk/template terlaris
   - Pelanggan yang melakukan repeat order

Proses rekapitulasi ini sangat memakan waktu (bisa 2-4 jam) dan rentan terhadap kesalahan perhitungan karena dilakukan secara manual. Jika ada pesanan yang tidak tercatat di buku atau transaksi yang terlewat, data laporan menjadi tidak akurat.

Pemilik kemudian memeriksa laporan tersebut secara visual untuk mengevaluasi kinerja bisnis dan menentukan strategi pemasaran ke depan. Tidak ada sistem otomatis yang memberikan insight atau dashboard statistik untuk mendukung pengambilan keputusan. Misalnya, pemilik tidak bisa dengan mudah mengetahui:

- Produk mana yang paling menguntungkan
- Bulan mana yang paling ramai pesanan (seasonal trends)
- Pelanggan mana yang paling sering order (untuk program loyalitas)
- Berapa rata-rata waktu proses dari order hingga pengiriman
- Berapa tingkat kepuasan pelanggan

#### d. Permasalahan yang Dihadapi

Berdasarkan analisis terhadap sistem yang berjalan saat ini, terdapat beberapa permasalahan yang dihadapi oleh Toko Dua Insan Story, antara lain:

**Permasalahan Prioritas Tinggi:**

1. **Risiko kesalahan informasi tinggi** - Proses pengisian data acara dilakukan secara manual melalui pesan teks yang rawan typo, kesalahan penulisan nama, tanggal, atau lokasi. Kesalahan ini seringkali baru diketahui setelah desain selesai atau bahkan setelah cetak, menyebabkan kerugian waktu dan biaya
2. **Proses pemesanan memakan waktu lama** - Pelanggan harus menunggu balasan admin secara manual untuk mendapatkan informasi harga, pilihan produk, dan konfirmasi pesanan. Proses bisa memakan waktu berhari-hari jika admin sedang sibuk atau di luar jam kerja
3. **Proses design proof approval tidak efisien dan tidak terstruktur** - Approval desain dilakukan melalui pesan instan tanpa sistem tracking yang jelas. Tidak ada dokumentasi formal tentang versi desain mana yang sudah di-review, approved, atau ditolak. History revisi sulit dilacak. Pelanggan bisa berubah pikiran setelah "approve" tanpa ada konfirmasi final yang mengikat. Komunikasi revisi seringkali ambigu dan memerlukan klarifikasi berulang kali
4. **Tidak ada perhitungan ongkos kirim otomatis** - Admin harus mengecek website atau menghubungi ekspedisi satu per satu untuk mendapatkan estimasi ongkir, proses ini memakan waktu dan seringkali estimasi tidak akurat

**Permasalahan Prioritas Menengah:**

5. **Pencatatan pesanan tidak terstruktur** - Pesanan dicatat di buku tulis atau aplikasi notes sederhana, sulit untuk melacak status pesanan secara real-time atau mencari data pesanan lama
6. **Tidak ada sistem notifikasi otomatis** - Pelanggan dan admin harus mengingatkan satu sama lain secara manual tentang status pesanan, pembayaran, atau approval desain
7. **Tidak ada sistem katalog produk yang terstruktur** - Pelanggan harus bertanya satu per satu untuk melihat produk yang tersedia, tidak ada filter atau search untuk memudahkan pencarian
8. **Tidak ada integrasi pembayaran online dengan verifikasi otomatis** - Proses verifikasi pembayaran harus dilakukan secara manual dengan mengecek mutasi rekening, memakan waktu dan rentan terlewat
9. **Tidak ada sistem review dan rating** - Feedback pelanggan tidak terdokumentasi dengan baik, sulit untuk mengevaluasi kualitas produk atau layanan

**Permasalahan Prioritas Rendah:**

10. **Proses pelaporan memakan waktu lama** - Rekapitulasi manual memakan waktu 2-4 jam setiap akhir bulan dan rentan terhadap kesalahan perhitungan
11. **Tidak ada data analytics untuk business intelligence** - Pemilik tidak memiliki data visual (chart, graph) untuk menganalisis trend penjualan, produk terlaris, atau customer behavior

---

![Gambar 2.2 - Sistem Berjalan Pemesanan Undangan](images/gambar-2.2.png)

*Sumber: Analisis Sistem Berjalan, 2025*  
**Gambar 2.2** Sistem Berjalan Pemesanan Undangan

---

Pada Gambar 2.2 ditunjukkan flowchart sistem berjalan untuk proses Pemesanan Undangan, yang memetakan interaksi antara Pelanggan dan Admin. Proses dimulai dari sisi Pelanggan yang Melihat promosi di media sosial dan menghubungi Admin melalui WhatsApp atau Instagram Direct Message. Admin kemudian Memberikan format data pesanan secara manual melalui chat, termasuk informasi yang perlu diisi seperti data mempelai, data acara, jumlah pesanan, dan pilihan produk. Selanjutnya, Pelanggan melakukan proses manual dengan Mengisi data acara dalam format teks dan mengirimkannya kembali via chat.

Setelah menerima data pesanan, Admin Menghitung total harga secara manual menggunakan kalkulator, termasuk perhitungan biaya cetak, biaya kertas, aksesoris tambahan, dan estimasi ongkos kirim. Total harga disampaikan kepada Pelanggan melalui pesan. Pelanggan kemudian melakukan pembayaran melalui transfer bank dan mengirimkan bukti transfer (screenshot atau foto) kepada Admin via chat.

Admin menerima bukti transfer dan masuk ke alur pemeriksaan manual untuk memvalidasi pembayaran dengan cara membuka aplikasi mobile banking, mengecek mutasi rekening, dan mencocokkan nominal dengan pesanan. Jika pembayaran valid, Admin akan Mencatat pesanan ke dalam Buku Pesanan (ditandai dengan simbol dokumen fisik) yang berisi informasi nomor pesanan, nama pelanggan, jumlah, total pembayaran, dan deadline. Terakhir, Admin meneruskan data tersebut kepada bagian Desainer untuk diproses, dan proses pemesanan dianggap selesai di tahap administrasi.

Flowchart ini menggambarkan dengan jelas bahwa seluruh proses dilakukan secara manual tanpa sistem otomatis, mengandalkan komunikasi via chat dan pencatatan fisik, yang rentan terhadap kesalahan dan memakan waktu.

---

![Gambar 2.3 - Sistem Berjalan Laporan Penjualan](images/gambar-2.3.png)

*Sumber: Analisis Sistem Berjalan, 2025*  
**Gambar 2.3** Sistem Berjalan Laporan Penjualan

---

Pada Gambar 2.3 ditunjukkan flowchart sistem berjalan untuk proses Laporan Penjualan, yang dilakukan oleh Pemilik atau Admin pada akhir periode (bulanan). Proses dimulai saat Admin Mengambil buku catatan pesanan yang telah terisi selama satu periode. Buku ini berisi catatan manual semua transaksi yang terjadi dalam satu bulan.

Selanjutnya, Admin melakukan serangkaian proses manual. Pertama, Admin Menjumlahkan semua pendapatan pesanan menggunakan kalkulator, yang ditandai dengan simbol operasi manual. Proses ini meliputi penjumlahan total pesanan, pengelompokan berdasarkan jenis produk, perhitungan rata-rata nilai pesanan, dan identifikasi produk terlaris. Proses ini memakan waktu 2-4 jam dan rentan terhadap kesalahan perhitungan.

Kedua, hasil rekapitulasi tersebut dicatat dan dibuat dalam bentuk Buku Laporan Bulanan, yang ditandai dengan simbol dokumen fisik. Laporan ini berisi ringkasan penjualan bulan tersebut dengan format tabel sederhana yang ditulis tangan atau diketik di dokumen spreadsheet sederhana.

Terakhir, Pemilik Memeriksa laporan tersebut secara visual untuk mengevaluasi kinerja bisnis, yang juga merupakan operasi manual. Pemilik membaca laporan, menganalisis angka-angka, dan membuat keputusan strategis berdasarkan intuisi dan pengalaman tanpa bantuan data visualization atau business intelligence tools. Proses manual ini diakhiri setelah laporan disetujui atau diarsipkan oleh Pemilik untuk referensi di masa mendatang.

Flowchart ini menunjukkan bahwa proses pelaporan masih sangat manual, tidak efisien, dan tidak memberikan insight yang mendalam untuk pengambilan keputusan bisnis yang lebih baik.

---

Berdasarkan analisis terhadap sistem yang berjalan saat ini, dapat disimpulkan bahwa diperlukan sebuah sistem informasi berbasis web yang dapat mengotomatisasi proses pemesanan, kustomisasi produk, perhitungan biaya (produk dan ongkir), pembayaran dengan verifikasi otomatis, **sistem design proof approval yang terstruktur dengan tracking lengkap**, notifikasi email di setiap tahap, serta pelaporan otomatis dengan dashboard analytics untuk meningkatkan efisiensi operasional dan memberikan pengalaman pengguna yang lebih baik bagi pelanggan Toko Dua Insan Story. Sistem yang dikembangkan diharapkan dapat mengatasi semua permasalahan yang telah diidentifikasi, terutama dalam hal **efisiensi komunikasi approval desain yang menjadi bottleneck utama dalam proses produksi**.

---

## DAFTAR PUSTAKA

Banks, A., & Porcello, E. (2020). *Learning React: Modern Patterns for Developing React Apps* (2nd ed.). O'Reilly Media.

Beck, K., & Andres, C. (2004). *Extreme Programming Explained: Embrace Change* (2nd ed.). Addison-Wesley Professional.

Elmasri, R., & Navathe, S. B. (2016). *Fundamentals of Database Systems* (7th ed.). Pearson.

Garrett, J. J. (2021). *The Elements of User Experience: User-Centered Design for the Web and Beyond* (3rd ed.). New Riders.

Harianto, S., Kusuma, A. P., & Wijaya, T. (2021). Digitalisasi Sistem Pemesanan Berbasis Web untuk Meningkatkan Efisiensi Bisnis UMKM. *Jurnal Teknologi Informasi dan Komunikasi*, 12(2), 145-158.

Laudon, K. C., & Traver, C. G. (2021). *E-Commerce 2021-2022: Business, Technology and Society* (17th ed.). Pearson.

Nielsen, J. (2020). Usability and User Experience in Design Approval Systems. *Nielsen Norman Group Reports*, 8(4), 22-35.

Norman, D. A. (2013). *The Design of Everyday Things: Revised and Expanded Edition*. Basic Books.

Prasetyo, D., & Widodo, A. (2023). Implementasi API Integration untuk Optimalisasi Sistem E-Commerce di Indonesia. *Jurnal Sistem Informasi dan Teknologi*, 15(1), 67-80.

Pressman, R. S., & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). McGraw-Hill Education.

Santoso, B., Kusuma, H., & Pratama, R. (2023). Penerapan React.js dalam Pengembangan Aplikasi Web Single Page Application yang Responsif dan Interaktif. *Jurnal Informatika dan Komputer*, 14(3), 201-215.

Sommerville, I. (2021). *Software Engineering* (10th ed.). Pearson.

Stauffer, M. (2019). *Laravel: Up & Running: A Framework for Building Modern PHP Apps* (2nd ed.). O'Reilly Media.

Turban, E., Whiteside, J., King, D., & Outland, J. (2018). *Introduction to Electronic Commerce and Social Commerce* (4th ed.). Springer.

Valenty, M., Saputra, A., & Kurniawan, D. (2024). Perancangan Sistem Informasi Berbasis Laravel dengan Arsitektur MVC untuk Meningkatkan Kualitas Pengembangan Aplikasi Web. *Jurnal Rekayasa Perangkat Lunak*, 16(2), 88-102.

Wibowo, R., & Susanto, E. (2022). Integrasi RajaOngkir API untuk Perhitungan Ongkos Kirim Real-Time pada Sistem E-Commerce. *Jurnal Teknologi dan Sistem Informasi Bisnis*, 13(3), 112-125.

---

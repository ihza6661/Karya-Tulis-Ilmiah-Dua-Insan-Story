PERANCANGAN SISTEM PEMESANAN DESAIN UNDANGAN BERBASIS WEB PADA TOKO DUA INSAN STORY

## BAB 1
## PENDAHULUAN

### 1.1 Latar Belakang

Di era digital saat ini, perkembangan teknologi informasi telah membawa perubahan yang signifikan dalam berbagai aspek kehidupan, termasuk dalam bidang bisnis dan layanan kreatif. Salah satu perubahan yang paling menonjol adalah peralihan dari sistem pemesanan konvensional menuju sistem berbasis online. Digitalisasi sistem pemesanan memberikan berbagai keuntungan, seperti kemudahan akses, fleksibilitas waktu, serta perluasan jangkauan pemasaran produk maupun jasa (Harianto dkk., 2021). Implementasi e-commerce dalam bisnis kreatif terbukti mampu meningkatkan efisiensi operasional serta kepuasan pelanggan (Turban et al., 2018). Sejalan dengan perkembangan tersebut, penerapan website pada toko penjualan menjadi solusi penting agar pelanggan dapat melakukan pemesanan produk secara lebih mudah dan efisien.

Toko Dua Insan Story merupakan usaha lokal yang bergerak di bidang pembuatan desain undangan cetak untuk berbagai acara, seperti pernikahan, tunangan, ulang tahun, dan acara resmi lainnya. Saat ini, proses pemesanan desain undangan masih dilakukan secara manual melalui pesan langsung di media sosial. Cara tersebut sering menimbulkan beberapa kendala, antara lain risiko kesalahpahaman informasi pemesanan, keterbatasan dalam melakukan penyesuaian desain secara interaktif, kesulitan pelanggan dalam melacak status pemesanan, serta tidak adanya sistem yang terstruktur untuk proses persetujuan desain (design proof approval).

Berdasarkan permasalahan yang telah diuraikan sebelumnya, diperlukan sebuah sistem pemesanan desain undangan berbasis online yang mampu meningkatkan kualitas pengalaman pengguna (user experience), mudah diakses oleh berbagai kalangan, serta mampu mempercepat dan mengefisienkan proses komunikasi antara pelanggan dan penyedia jasa. Pengalaman pengguna yang baik terbukti menjadi salah satu faktor kunci dalam keberhasilan aplikasi web modern (Norman, 2013).

Sistem yang dirancang diharapkan dapat menyediakan fitur-fitur yang mendukung seluruh proses pemesanan, mulai dari pemilihan produk hingga pengiriman kepada pelanggan. Adapun fitur-fitur utama yang diusulkan dalam sistem pemesanan desain undangan online ini antara lain sebagai berikut:

1.	Katalog produk undangan, yang dilengkapi dengan fitur penyaringan (filter) berdasarkan kategori, rentang harga, dan tingkat popularitas, sehingga memudahkan pelanggan dalam memilih desain undangan yang sesuai dengan tema acara.
2.	Formulir pemesanan online, yang dirancang dengan pengisian data acara secara terstruktur guna meminimalkan risiko kesalahan informasi yang sering terjadi pada proses pemesanan manual.
3.	Kalkulator biaya otomatis, yang berfungsi untuk menghitung total harga pemesanan berdasarkan jumlah undangan, jenis kertas, serta tambahan aksesoris sehingga memberikan transparansi harga kepada pelanggan.
4.	Sistem persetujuan desain (design proof approval), yang memungkinkan admin mengunggah pratinjau desain dan memberikan fasilitas bagi pelanggan untuk menyetujui, mengajukan revisi, atau menolak desain secara sistematis, disertai pencatatan riwayat revisi (revision tracking).
5.	Integrasi sistem pembayaran online, melalui layanan Midtrans yang menyediakan opsi pembayaran uang muka (down payment) minimal sebesar 30% atau pembayaran penuh, sehingga memberikan fleksibilitas bagi pelanggan dalam melakukan transaksi.
6.	Perhitungan ongkos kirim otomatis, yang terintegrasi dengan API RajaOngkir dengan pilihan ekspedisi seperti JNE, POS Indonesia, dan TIKI, serta berbagai jenis layanan pengiriman.
7.	Sistem notifikasi berbasis email, yang memberikan informasi kepada pelanggan pada setiap tahapan pemesanan, mulai dari konfirmasi pemesanan, konfirmasi pembayaran, pengunggahan pratinjau desain, persetujuan desain, hingga proses pengiriman.
8.	Fitur pelacakan pesanan (order tracking), yang memungkinkan pelanggan memantau status pemesanan secara real-time, mulai dari proses pemesanan hingga barang diterima.
9.	Sistem ulasan dan penilaian (review and rating), yang berfungsi sebagai sarana umpan balik pelanggan terhadap produk dan layanan, serta meningkatkan kepercayaan dan kredibilitas toko.

Dengan adanya sistem pemesanan desain undangan online ini, diharapkan dapat meningkatkan efisiensi operasional, mengurangi kesalahan komunikasi, serta memberikan pengalaman pengguna yang lebih baik bagi pelanggan maupun pengelola usaha.

Laravel merupakan framework berbasis PHP yang dirancang untuk mempermudah proses pengembangan aplikasi web dengan menerapkan pola arsitektur Model-View-Controller (MVC) (Valenty dkk., 2024). Framework ini menyediakan berbagai fitur bawaan, seperti sistem routing, autentikasi, template engine (Blade), serta Object Relational Mapping (ORM) melalui Eloquent untuk mempermudah interaksi dengan basis data. Penerapan Laravel memberikan keuntungan berupa efisiensi waktu pengembangan, konsistensi kode, serta peningkatan keamanan dalam pengelolaan autentikasi dan transaksi data (Stauffer, 2019).

React merupakan library JavaScript yang dikembangkan untuk membangun antarmuka pengguna (user interface) yang dinamis dan responsif (Santoso dkk., 2023). React menggunakan konsep component-based architecture yang memungkinkan pengembangan antarmuka secara modular dan dapat digunakan kembali. Dengan konsep Virtual DOM, React mampu memperbarui tampilan halaman secara efisien tanpa memuat ulang seluruh konten sehingga meningkatkan performa dan interaktivitas aplikasi (Banks & Porcello, 2020).

Next.js merupakan framework berbasis React yang menyediakan fitur tambahan seperti server-side rendering dan routing otomatis, sehingga sangat sesuai untuk pengembangan dashboard administrator yang membutuhkan performa tinggi dan pengelolaan data yang kompleks.

Dalam penelitian ini, sistem pemesanan desain undangan online dikembangkan menggunakan Laravel sebagai framework utama pada sisi backend, React.js dengan Vite untuk antarmuka pelanggan (customer-facing website), serta Next.js untuk dashboard administrator. Laravel bertanggung jawab dalam pengelolaan logika bisnis, autentikasi pengguna, manajemen data, serta integrasi dengan basis data dan layanan pihak ketiga. Sementara itu, React dan Next.js digunakan untuk menyajikan antarmuka pengguna yang interaktif, dinamis, dan mudah digunakan.

Untuk mendukung proses transaksi, sistem diintegrasikan dengan layanan payment gateway Midtrans yang memungkinkan pelanggan melakukan pembayaran melalui berbagai metode, seperti transfer bank, kartu debit/kredit, dan e-wallet. Integrasi payment gateway dalam sistem e-commerce terbukti meningkatkan kepercayaan konsumen serta keamanan transaksi (Laudon & Traver, 2021). Sistem menyediakan opsi pembayaran uang muka (down payment) minimal sebesar 30% dari total pesanan, dengan pelunasan dilakukan setelah desain disetujui atau sebelum proses produksi dimulai.

Selain itu, sistem juga terintegrasi dengan RajaOngkir API untuk mendukung proses pengiriman undangan cetak ke berbagai daerah. RajaOngkir menyediakan data ongkos kirim secara otomatis dan real-time berdasarkan lokasi tujuan, berat produk, dan pilihan kurir (Wibowo & Susanto, 2022). Sistem mendukung jasa ekspedisi seperti JNE, POS Indonesia, dan TIKI dengan berbagai layanan pengiriman. Integrasi API pihak ketiga dalam perhitungan ongkos kirim terbukti meningkatkan efisiensi operasional serta kepuasan pelanggan dalam sistem e-commerce (Prasetyo & Widodo, 2023).

Salah satu fitur unggulan dalam sistem ini adalah sistem persetujuan bukti desain (design proof approval) yang terstruktur. Penerapan workflow approval yang sistematis dalam proses desain terbukti mampu mengurangi kesalahan produksi serta meningkatkan kepuasan pelanggan (Nielsen, 2020; Garrett, 2021). Setelah pelanggan menyelesaikan proses pemesanan dan pembayaran, admin atau desainer akan membuat desain undangan berdasarkan data acara yang diberikan. Desain tersebut kemudian diunggah ke dalam sistem sebagai bukti desain yang dapat diakses oleh pelanggan melalui dashboard akun masing-masing.

Pada tahap ini, pelanggan dapat memberikan persetujuan, mengajukan revisi dengan catatan yang jelas, atau menolak desain. Seluruh aktivitas persetujuan dan revisi akan tercatat secara otomatis dalam sistem beserta informasi waktu (timestamp), sehingga memudahkan pelacakan riwayat revisi (revision history tracking) dan mengurangi kesalahpahaman komunikasi (Sommerville, 2021). Proses produksi hanya dilakukan setelah pelanggan memberikan persetujuan akhir (final approval). Sistem juga mengirimkan notifikasi email secara otomatis pada setiap tahapan proses untuk menjaga transparansi dan ketepatan informasi.

Dengan diterapkannya sistem pemesanan desain undangan berbasis online ini, Toko Dua Insan Story diharapkan mampu meningkatkan efisiensi layanan melalui otomatisasi proses pemesanan, pengelolaan desain, serta komunikasi antara pelanggan dan penyedia jasa.

Selain itu, sistem ini diharapkan dapat memperluas jangkauan pelanggan tanpa dibatasi oleh lokasi dan waktu, serta membantu pengelolaan data pemesanan secara lebih terstruktur dan terdokumentasi dengan baik. Dengan demikian, Toko Dua Insan Story dapat memberikan layanan yang lebih profesional, responsif, dan konsisten sesuai dengan kebutuhan dan preferensi pelanggan, serta meningkatkan kepuasan dan kepercayaan pelanggan.

### 1.2 Rumusan Masalah

 Berdasarkan uraian permasalahan pada latar belakang, perumusan masalah dalam penelitian ini adalah:

"Bagaimana merancang dan membangun sistem pemesanan desain undangan cetak berbasis web pada Toko Dua Insan Story yang mampu menggantikan proses pemesanan manual, meningkatkan efisiensi komunikasi antara pelanggan dan penyedia jasa, meminimalkan kesalahan informasi pemesanan, serta menyediakan fitur katalog desain, sistem persetujuan bukti desain (design proof approval) dengan pelacakan revisi, perhitungan ongkos kirim otomatis, dan integrasi pembayaran online guna mendukung layanan yang cepat, transparan, dan profesional?"

### 1.3  Batasan CAPSTONE PROJECT

Penelitian ini dibatasi agar tetap fokus pada tujuan yang ingin dicapai serta dapat diselesaikan sesuai dengan ruang lingkup Capstone Project. Ruang lingkup penelitian meliputi perancangan dan pembangunan sistem pemesanan desain undangan cetak berbasis web dengan menggunakan Laravel 12 sebagai backend, React.js dengan Vite untuk antarmuka pelanggan (customer frontend), Next.js untuk dashboard administrator, serta MySQL sebagai basis data.

Fitur utama yang dikembangkan dalam sistem ini meliputi katalog desain undangan cetak, formulir pemesanan online dengan opsi kustomisasi dan pengisian data acara oleh pelanggan, sistem persetujuan bukti desain (design proof approval) dengan alur persetujuan, revisi, dan penolakan, notifikasi status pesanan melalui email, perhitungan ongkos kirim otomatis melalui integrasi RajaOngkir API, serta integrasi pembayaran online menggunakan Midtrans dengan opsi pembayaran uang muka (down payment) dan pembayaran penuh (full payment).

Adapun beberapa aspek yang tidak termasuk dalam cakupan penelitian ini adalah sebagai berikut:

1.	Undangan digital berbasis web (web-based invitation templates), karena fitur tersebut direncanakan sebagai pengembangan lanjutan di masa mendatang.
2.	Manajemen stok bahan baku fisik percetakan, seperti kertas, tinta, amplop, dan aksesoris lainnya.
3.	Integrasi langsung dengan mesin cetak atau printer industri.
4.	Modul akuntansi lanjutan, seperti general ledger, arus kas (cash flow), laporan laba rugi, dan pelaporan pajak.
5.	Fitur multi-user dengan pemisahan peran secara rinci, seperti admin, desainer, operator cetak, kurir, dan gudang.
6.	Sistem inventory management untuk pelacakan bahan baku dan produk jadi (finished goods).
7.	Integrasi dengan sistem Enterprise Resource Planning (ERP) atau perangkat lunak akuntansi pihak ketiga, seperti Accurate, Zahir, atau SAP.
8.	Fitur Customer Relationship Management (CRM) lanjutan, seperti otomatisasi pemasaran email (email marketing automation) dan segmentasi pelanggan.
9.	Sistem loyalty program atau keanggotaan (membership) dengan skema poin atau reward.

Dengan adanya batasan tersebut, penelitian ini diharapkan dapat menghasilkan sistem yang terfokus, terukur, dan relevan dengan kebutuhan utama Toko Dua Insan Story, tanpa meluas ke aspek-aspek di luar tujuan utama penelitian.

### 1.4  Tujuan CAPSTONE PROJECT

Tujuan dari penelitian ini adalah untuk merancang dan membangun sistem pemesanan desain undangan cetak berbasis web pada Toko Dua Insan Story sebagai pengganti proses pemesanan manual. Sistem ini dikembangkan menggunakan Laravel sebagai backend, React.js dengan Vite untuk antarmuka pelanggan, Next.js untuk dashboard administrator, serta MySQL sebagai basis data. Pengembangan sistem ini diharapkan dapat meningkatkan efisiensi proses pemesanan dan komunikasi antara pelanggan dan penyedia jasa, mengurangi risiko kesalahan informasi pemesanan, serta mempercepat proses konfirmasi pesanan.

Secara khusus, tujuan dari pengembangan sistem ini adalah sebagai berikut:

1.	Mengembangkan sistem pemesanan undangan cetak berbasis web yang memungkinkan pelanggan melakukan pemesanan secara mandiri melalui antarmuka yang interaktif dan responsif.
2.	Menyediakan fitur katalog desain undangan yang memudahkan pelanggan dalam memilih template desain sesuai dengan kebutuhan dan tema acara.
3.	Mengimplementasikan formulir pemesanan dengan opsi kustomisasi, meliputi pengisian data acara, pilihan jenis kertas, ukuran undangan, serta tambahan aksesoris.
4.	Mengembangkan sistem persetujuan bukti desain (design proof approval) yang terstruktur untuk memfasilitasi proses persetujuan, revisi, dan penolakan desain, serta mendokumentasikan seluruh riwayat revisi secara sistematis.
5.	Mengotomatisasi perhitungan biaya pengiriman berdasarkan lokasi tujuan melalui integrasi RajaOngkir API.
6.	Mengintegrasikan sistem pembayaran online yang aman dan efisien melalui Midtrans, dengan opsi pembayaran uang muka (down payment) dan pembayaran penuh (full payment).
7.	Memastikan bahwa proses produksi undangan hanya dimulai setelah pelanggan memberikan persetujuan akhir (final approval) terhadap desain yang diajukan.

Dengan tercapainya tujuan-tujuan tersebut, diharapkan sistem yang dikembangkan dapat mendukung peningkatan kualitas layanan, profesionalisme, serta kepuasan pelanggan pada Toko Dua Insan Story.

### 1.5  Manfaat CAPSTONE PROJECT

a.	Manfaat bagi Penulis

Capstone Project ini memberikan kesempatan bagi penulis untuk merancang dan membangun aplikasi web secara full-stack, mulai dari perancangan backend hingga implementasi frontend. Melalui penelitian ini, penulis memperoleh pengalaman dalam penerapan arsitektur Model–View–Controller (MVC) menggunakan framework Laravel, pengelolaan basis data MySQL, serta penerapan konsep komponen dan state management pada React.js dan Next.js. Selain itu, penulis juga mendapatkan pengalaman praktis dalam mengintegrasikan sistem dengan layanan pihak ketiga, seperti payment gateway Midtrans dan layanan perhitungan ongkos kirim melalui RajaOngkir API. Hasil dari Capstone Project ini diharapkan dapat menjadi portofolio yang bernilai serta menjadi referensi bagi penulis dalam pengembangan aplikasi web modern, khususnya pada sistem pemesanan dan e-commerce berbasis web.

b.	Manfaat bagi Pengguna

Bagi Toko Dua Insan Story, penelitian ini memberikan manfaat berupa peningkatan efisiensi dan profesionalitas dalam proses pemesanan desain undangan cetak. Sistem yang dikembangkan memungkinkan pengelolaan pesanan secara lebih terstruktur, mempercepat proses konfirmasi, serta mengurangi ketergantungan pada komunikasi manual yang berpotensi menimbulkan kesalahan informasi.

Selain itu, pelanggan memperoleh kemudahan dalam melakukan pemesanan melalui katalog desain yang lengkap, sistem persetujuan bukti desain (design proof approval) dengan pelacakan riwayat revisi yang jelas, perhitungan ongkos kirim yang transparan, serta notifikasi otomatis pada setiap tahap pemesanan. Dengan adanya sistem design proof approval yang terstruktur, risiko kesalahan produksi dapat diminimalkan karena pelanggan memiliki kendali penuh terhadap persetujuan desain akhir sebelum memasuki tahap produksi. Secara keseluruhan, sistem ini diharapkan dapat membantu Toko Dua Insan Story dalam memperluas jangkauan pemasaran secara online, meningkatkan kepuasan pelanggan, serta menyediakan data pemesanan yang dapat dimanfaatkan sebagai dasar dalam pengambilan keputusan bisnis.

### 1.6  Metodologi Perancangan Solusi

Metodologi perancangan perangkat lunak yang digunakan dalam penelitian ini adalah Extreme Programming (XP). Extreme Programming merupakan salah satu metode dalam pendekatan Agile Software Development yang menekankan kolaborasi yang intensif antara pengembang dan pengguna, komunikasi yang berkelanjutan, serta kemampuan beradaptasi terhadap perubahan kebutuhan secara cepat (Beck & Andres, 2004).

Penerapan metode XP dipilih karena dinilai sesuai dengan karakteristik pengembangan sistem yang membutuhkan fleksibilitas tinggi, waktu pengembangan yang relatif singkat, serta keterlibatan pengguna secara aktif dalam setiap tahapan pengembangan. Dengan demikian, sistem yang dihasilkan diharapkan lebih sesuai dengan kebutuhan pengguna dan memiliki kualitas yang lebih baik.

Menurut Pressman dan Maxim (2019:46), metode Extreme Programming (XP) terdiri dari seperangkat aturan dan praktik yang dilaksanakan dalam konteks empat kegiatan utama, yaitu perencanaan (planning), perancangan (design), pengkodean (coding), dan pengujian (testing). Keempat kegiatan tersebut dilakukan secara iteratif dan berulang, sehingga memungkinkan adanya perbaikan dan penyempurnaan sistem secara berkelanjutan pada setiap siklus pengembangan.

Alur tahapan Extreme Programming (XP) yang digunakan dalam penelitian ini dapat dilihat pada Gambar 1.1.

Sumber: Pressman dan Maxim (2019)
Gambar 1.1 Extreme Programming

Pada gambar 1.1 digambarkan tahapan-tahapan model Extreme Programming untuk perancangan perangkat lunak (Pressman dan Maxim, 2019:47), yang terdiri dari:

a.	Planning (Perencanaan)

Identifikasi masalah dilakukan melalui observasi dan wawancara dengan pemilik. Hasilnya berupa daftar kebutuhan fungsional dan non-fungsional serta analisis alur pemesanan manual yang kemudian dijadikan dasar rancangan solusi berbasis web. Pada tahap ini juga dilakukan analisis terhadap proses bisnis yang berjalan, identifikasi pain points dalam sistem manual, serta penentuan prioritas fitur yang akan dikembangkan. User stories dibuat untuk setiap fitur utama, seperti "Sebagai pelanggan, saya ingin melihat pratinjau desain undangan saya agar dapat memberikan persetujuan atau meminta revisi".

b.	Design (Perancangan)

Hasil analisis kebutuhan diterjemahkan ke dalam model dan rancangan sistem, termasuk arsitektur sistem, perancangan antarmuka menggunakan React.js dan Next.js, dan perancangan basis data menggunakan ERD. Pemodelan proses bisnis dan diagram UML juga disusun untuk memastikan keterpaduan komponen (Pressman & Maxim, 2020). Pada tahap ini dirancang pula struktur database dengan 55 tabel yang mencakup entitas users, products, orders, design proofs, payments, shipping, dan lain-lain. Perancangan API endpoints juga dilakukan untuk memastikan komunikasi yang efisien antara backend dan frontend.

c.	Coding (Pengkodean)

Implementasi dilakukan dengan menerjemahkan rancangan ke dalam kode menggunakan Laravel 12 (backend API), React.js dengan Vite untuk situs pelanggan, dan Next.js 15 untuk dashboard administrator. MySQL digunakan sebagai basis data untuk menyimpan data pemesanan, informasi pelanggan, design proofs, dan informasi produk. Database relasional seperti MySQL terbukti efektif untuk mengelola data transaksional dalam sistem e-commerce (Elmasri & Navathe, 2016). Pengkodean dilakukan secara iteratif dengan fokus pada satu fitur dalam satu waktu (feature-based development). Setiap fitur yang selesai di-commit ke version control system (Git) untuk memudahkan tracking perubahan dan kolaborasi.

d.	Testing (Pengujian)

Setelah pengkodean, dilakukan pengujian fungsional untuk memverifikasi kesesuaian sistem terhadap kebutuhan pengguna, termasuk pengujian fitur pemesanan, kustomisasi produk, sistem design proof approval (approve/revision/reject), notifikasi email, perhitungan ongkos kirim via RajaOngkir, dan integrasi pembayaran online melalui Midtrans. Pengujian dilakukan secara manual (manual testing) maupun otomatis (automated testing) menggunakan PHPUnit untuk backend dan Jest untuk frontend. User acceptance testing (UAT) juga dilakukan dengan melibatkan pemilik toko untuk memastikan sistem sesuai dengan ekspektasi dan kebutuhan bisnis.

### 1.7  Sistematika Penulisan

Sistematika penulisan laporan Capstone Project ini disusun untuk memberikan gambaran alur pembahasan pada setiap bab yang disajikan, sehingga memudahkan pembaca dalam memahami isi penelitian secara keseluruhan. Adapun sistematika penulisan laporan ini adalah sebagai berikut:

BAB 1 PENDAHULUAN

Bab ini membahas gambaran umum penelitian yang meliputi latar belakang, rumusan masalah, batasan penelitian, tujuan dan manfaat penelitian, metodologi perancangan solusi, serta sistematika penulisan.

BAB 2 TEMPAT CAPSTONE PROJECT  

Bab ini memuat profil objek penelitian, layanan yang disediakan, proses bisnis yang berjalan, serta struktur organisasi pada Toko Dua Insan Story.

BAB 3 PERANCANGAN SOLUSI

Bab ini membahas analisis kebutuhan sistem, perancangan sistem yang meliputi pemodelan UML dan ERD, perancangan antarmuka pengguna, serta langkah-langkah implementasi sistem.

BAB 4 PENUTUP

Bab ini berisi kesimpulan yang diperoleh dari hasil penelitian serta saran untuk pengembangan sistem di masa mendatang.

## BAB 2

## GAMBARAN UMUM TOKO DUA INSAN STORY

### 2.1 Gambaran Toko Dua Insan Story

Industri kreatif di Indonesia mengalami pertumbuhan signifikan dalam beberapa tahun terakhir, dengan kontribusi terhadap Produk Domestik Bruto (PDB) yang terus meningkat. Salah satu sub-sektor yang berkembang pesat adalah industri percetakan dan desain grafis untuk keperluan acara formal, khususnya undangan pernikahan (Kementerian Pariwisata dan Ekonomi Kreatif, 2022). Dalam konteks ini, Usaha Mikro, Kecil, dan Menengah (UMKM) memiliki peran vital sebagai penyedia jasa yang mampu mengakomodasi kebutuhan pasar dengan pendekatan yang lebih personal dan fleksibel (Tambunan, 2021).

Toko Dua Insan Story merupakan sebuah usaha yang bergerak di bidang industri kreatif dan percetakan, khususnya berfokus pada penyediaan jasa pembuatan desain undangan pernikahan cetak berkualitas tinggi. Berlokasi di Kota Pontianak, Kalimantan Barat, Toko Dua Insan Story didirikan dan dikelola oleh Atika Karolina. Usaha ini hadir untuk menjawab kebutuhan masyarakat akan undangan yang estetis dan modern dalam format cetak fisik untuk keperluan acara formal. Penempatan lokasi di Pontianak memberikan keunggulan geografis untuk melayani pasar lokal Kalimantan Barat serta wilayah sekitarnya melalui layanan pengiriman terintegrasi.

Produk utama yang ditawarkan adalah undangan cetak (printed invitation), yaitu undangan fisik berkualitas tinggi dengan berbagai pilihan desain, ukuran, jenis kertas, dan material tambahan. Konsep mass customization yang diterapkan memungkinkan pelanggan untuk memilih dari berbagai template desain yang tersedia dalam katalog online, kemudian menyesuaikannya dengan data acara pribadi seperti nama mempelai, nama orang tua mempelai, tanggal dan waktu acara (akad nikah dan resepsi), lokasi acara dengan alamat lengkap, serta informasi penting lainnya seperti dress code atau link live streaming untuk acara hybrid (Pine & Gilmore, 2021). Pendekatan customization ini sejalan dengan tren konsumen modern yang menginginkan produk yang unik dan personal sekaligus tetap efisien dalam proses pemesanan (Kotler & Keller, 2022).

Toko Dua Insan Story menerapkan strategi diferensiasi produk (product differentiation) dengan menyediakan berbagai varian undangan cetak yang dapat disesuaikan dengan kebutuhan dan budget pelanggan. Strategi ini terbukti efektif dalam meningkatkan daya saing UMKM di pasar yang kompetitif (Porter, 2020). Dalam aspek variasi ukuran, toko menyediakan tiga kategori utama yang dirancang berdasarkan segmentasi pasar. Ukuran standar dengan dimensi 10 x 15 cm diposisikan sebagai pilihan ekonomis yang paling populer, cocok untuk acara dengan jumlah tamu besar dan budget terbatas. Ukuran premium dengan dimensi 15 x 20 cm menawarkan kesan lebih mewah dengan ruang desain yang lebih luas, memberikan fleksibilitas dalam penempatan elemen visual dan informasi acara. Sementara kategori eksklusif menyediakan opsi custom size yang dapat disesuaikan dengan permintaan khusus pelanggan, memberikan kebebasan penuh dalam menciptakan undangan yang truly unique.

Pemilihan material kertas merupakan aspek krusial dalam produksi undangan cetak karena berpengaruh langsung terhadap persepsi kualitas dan estetika produk (Ambrose & Harris, 2020). Toko Dua Insan Story menyediakan lima jenis kertas dengan karakteristik berbeda untuk memenuhi preferensi beragam pelanggan. Art Paper dengan gramatur 150-260 gsm merupakan pilihan standar yang menawarkan permukaan halus dan hasil cetak tajam, ideal untuk desain dengan detail warna yang kompleks. Ivory dengan gramatur 210-310 gsm memberikan tekstur sedikit kasar dan kesan natural yang cocok untuk tema rustic atau vintage. Linen dengan gramatur 200-300 gsm memiliki motif garis-garis halus yang memberikan kesan elegan dan formal, sering dipilih untuk acara pernikahan klasik. Jasmine dengan gramatur 200-260 gsm menawarkan tekstur unik yang memberikan kesan soft dan mewah. Sedangkan Art Carton dengan gramatur 190-260 gsm merupakan kertas tebal dan kokoh yang sangat cocok untuk undangan lipat (folded invitation) atau undangan dengan multiple pages.

Untuk meningkatkan nilai tambah produk, Toko Dua Insan Story juga menyediakan berbagai material dan aksesoris tambahan yang dapat dikombinasikan sesuai preferensi pelanggan. Konsep bundling ini tidak hanya meningkatkan estetika produk tetapi juga menciptakan perceived value yang lebih tinggi (Zeithaml et al., 2020). Paket aksesoris meliputi amplop custom dengan berbagai pilihan warna dan bahan (kertas, kain, atau plastik bening), stiker segel custom dengan nama atau inisial mempelai untuk menutup amplop, pita satin atau organza berbagai warna sebagai hiasan dekoratif, box eksklusif untuk packaging premium yang memberikan kesan mewah sejak undangan diterima, kartu ucapan terima kasih (thank you card) yang dapat disisipkan dalam undangan, serta kartu informasi tambahan seperti akomodasi, peta lokasi, atau protokol kesehatan untuk memberikan informasi praktis kepada tamu undangan.

Aspek finishing merupakan tahap akhir produksi yang menentukan kualitas visual dan durabilitas produk. Toko Dua Insan Story menawarkan lima pilihan teknik finishing profesional yang dapat dipilih sesuai konsep desain. Laminasi glossy memberikan permukaan mengkilap yang membuat warna tampak lebih vibrant dan melindungi cetakan dari kerusakan fisik. Laminasi doff menghasilkan permukaan tidak mengkilap dengan kesan lebih elegan dan premium, sering dipilih untuk acara formal. Hot print merupakan teknik hot stamping menggunakan foil emas atau perak yang memberikan efek metalik eksklusif pada elemen desain tertentu. Teknik emboss menciptakan efek timbul pada bagian tertentu desain untuk memberikan dimensi dan tekstur yang dapat dirasakan secara taktil. Sedangkan spot UV adalah teknik pelapisan UV selektif pada area tertentu untuk menciptakan kontras antara area glossy dan doff, memberikan efek visual yang sophisticated (Bann, 2020).

Fleksibilitas kustomisasi yang ditawarkan meliputi pemilihan warna tema yang dapat disesuaikan dengan palette warna acara, penambahan ornamen khusus seperti bunga, daun, atau motif tradisional yang mencerminkan budaya atau preferensi personal, serta kombinasi berbagai opsi finishing untuk menciptakan hasil akhir yang truly personalized. Sistem pemesanan online yang dikembangkan memungkinkan pelanggan untuk melihat estimasi harga secara real-time berdasarkan konfigurasi pilihan yang mereka buat, memberikan transparansi penuh dalam transaksi dan memfasilitasi pengambilan keputusan yang informed (Chen & Chang, 2021).

Dengan komitmen untuk memberikan hasil desain yang berkualitas, unik, dan sesuai dengan keinginan pelanggan, Toko Dua Insan Story bertujuan untuk menjadi mitra terpercaya dalam melengkapi momen-momen bahagia setiap pelanggan melalui media undangan cetak yang berkesan. Proses produksi dilakukan dengan menerapkan standar quality control yang ketat pada setiap tahapan, mulai dari pemilihan material, proses desain, hingga quality checking sebelum packaging, memastikan setiap undangan yang dikirimkan dalam kondisi sempurna tanpa cacat produksi (Juran & De Feo, 2020).

Sebelum dikembangkannya sistem berbasis web ini, seluruh proses operasional dan sistem pemesanan di Toko Dua Insan Story masih berjalan sepenuhnya secara konvensional tanpa memanfaatkan sistem informasi yang terintegrasi. Kondisi ini mencerminkan karakteristik umum UMKM di Indonesia yang masih mengandalkan proses manual dalam operasional bisnis mereka (Rahayu & Day, 2020). Promosi dilakukan melalui media sosial seperti Instagram dan Facebook, namun proses pemesanan masih dilakukan secara manual melalui pesan langsung (Direct Message) atau aplikasi pesan instan seperti WhatsApp. Pencatatan pesanan, data acara pelanggan, hingga rekapitulasi pembayaran masih dicatat dalam buku tulis atau aplikasi catatan sederhana di ponsel. Proses persetujuan desain (design proof approval) dilakukan melalui pengiriman file gambar via WhatsApp tanpa tracking yang jelas, seringkali menyebabkan kebingungan tentang versi desain mana yang sudah disetujui atau masih memerlukan revisi. Keterbatasan sistem manual ini menciptakan berbagai inefficiency dan risiko kesalahan yang menghambat pertumbuhan bisnis (O'Brien & Marakas, 2021). Kondisi inilah yang menjadi dasar dilakukannya penelitian untuk merancang dan membangun sebuah sistem pemesanan desain undangan berbasis web yang dapat meningkatkan efisiensi operasional dan memberikan pengalaman pengguna yang lebih baik.

### 2.2 Struktur Organisasi

Struktur organisasi merupakan kerangka formal yang mendefinisikan bagaimana tugas dibagi, dikelompokkan, dan dikoordinasikan dalam sebuah entitas bisnis (Robbins & Coulter, 2022). Dalam konteks UMKM, khususnya pada tahap early-stage development, struktur organisasi cenderung bersifat sederhana dan fleksibel dengan tingkat formalisasi yang rendah namun tetap efektif dalam mencapai tujuan bisnis (Zimmerer et al., 2020). Karakteristik ini memungkinkan UMKM untuk beradaptasi dengan cepat terhadap perubahan kondisi pasar dan kebutuhan operasional.

Toko Dua Insan Story menerapkan struktur organisasi yang mencerminkan prinsip-prinsip tersebut, yaitu struktur yang sederhana namun fungsional dengan pembagian peran dan tanggung jawab yang jelas dalam mengelola seluruh kegiatan usaha kreatif. Setiap posisi dalam struktur ini dirancang untuk menjalankan fungsi spesifik yang saling terintegrasi, mulai dari manajemen strategis, pelayanan pelanggan, hingga proses produksi desain. Pendekatan ini sejalan dengan konsep lean organization yang menekankan efisiensi operasional dengan meminimalkan redundansi dalam struktur (Womack & Jones, 2021). Meskipun sederhana, struktur organisasi ini bertujuan untuk memaksimalkan efisiensi kerja, memastikan kualitas desain terjaga, dan menjamin kepuasan pelanggan terhadap hasil akhir undangan.

---

![Gambar 2.1 - Struktur Organisasi Toko Dua Insan Story](images/2.1-fix.png)

*Sumber: Toko Dua Insan Story, 2025*  
**Gambar 2.1** Struktur Organisasi Toko Dua Insan Story

---

Struktur organisasi Toko Dua Insan Story menerapkan model fungsional yang bertujuan untuk memastikan operasional bisnis berjalan secara terstruktur dan efisien. Model fungsional merupakan pendekatan organisasi dimana pengelompokan aktivitas dilakukan berdasarkan fungsi atau keahlian yang serupa, menciptakan spesialisasi dalam setiap unit kerja (Daft, 2021). Pucuk pimpinan dipegang oleh Pemilik (Owner), yang memiliki wewenang penuh dalam menentukan arah kebijakan bisnis, menyediakan modal, serta memantau perkembangan usaha secara keseluruhan. Dalam praktiknya, pemilik juga merangkap sebagai administrator sistem dan desainer, mencerminkan pola owner-operator yang khas pada UMKM kreatif di tahap awal perkembangan (Longenecker et al., 2020).

Struktur organisasi saat ini bersifat fleksibel mengingat skala usaha yang masih tergolong usaha mikro dan dikelola secara lean dengan fokus pada value creation. Fleksibilitas struktural ini memberikan keunggulan dalam hal kecepatan pengambilan keputusan dan kemampuan beradaptasi terhadap dinamika pasar (Burns & Stalker dalam Mullins, 2021). Pembagian tugas dan tanggung jawab dalam struktur organisasi Toko Dua Insan Story mencakup beberapa fungsi kunci sebagai berikut:

#### a. Pemilik/Owner

Sebagai pemegang kendali tertinggi dalam hierarki organisasi, pemilik bertanggung jawab dalam menentukan arah kebijakan bisnis, menyediakan modal usaha, memantau perkembangan usaha, dan mengambil keputusan strategis terkait pengembangan produk dan layanan. Peran strategis ini sejalan dengan fungsi top management dalam organizational theory yang fokus pada perencanaan jangka panjang dan pengambilan keputusan tingkat makro (Mintzberg, 2021). Pemilik juga berperan aktif dalam memantau operasional sistem pemesanan berbasis web, mengevaluasi kepuasan pelanggan melalui review dan rating yang masuk, serta menganalisis data penjualan untuk menentukan strategi marketing dan pengembangan produk baru. Dalam konteks bisnis digital, pemilik UMKM perlu memiliki kemampuan dalam menganalisis data untuk mendukung data-driven decision making (Davenport & Harris, 2020).

#### b. Administrator/Customer Service

Administrator menempati posisi frontline dalam operational management, bertugas di garda terdepan untuk melayani komunikasi dengan pelanggan melalui sistem website. Fungsi utama meliputi pengelolaan katalog produk, pemrosesan pesanan yang masuk, konfirmasi pembayaran melalui dashboard admin, pengelolaan sistem design proof approval dengan mengunggah bukti desain untuk persetujuan pelanggan, serta penanganan pertanyaan dan keluhan pelanggan secara responsif. Peran customer service dalam era digital tidak hanya sebatas melayani, tetapi juga menciptakan customer experience yang positif melalui setiap touchpoint interaksi (Lemon & Verhoef, 2020).

Administrator juga bertanggung jawab mengelola promotional campaign melalui promo code, memverifikasi dan merespons ulasan pelanggan, memproses permintaan pembatalan pesanan dengan workflow approval yang terstruktur, serta memantau status pesanan melalui dashboard admin untuk memastikan setiap pesanan diproses tepat waktu. Dengan adanya sistem terintegrasi, administrator dapat melakukan bulk update status pesanan, export data pesanan untuk keperluan laporan manajemen, dan mengelola shipping tracking number untuk pesanan yang sudah dikirim. Integrasi sistem informasi dalam fungsi administratif terbukti meningkatkan produktivitas dan mengurangi error rate dalam pengelolaan data (Laudon & Laudon, 2021).

#### c. Desainer Grafis

Desainer grafis memegang peran krusial dalam value creation process, bertanggung jawab penuh atas proses produksi desain undangan mulai dari tahap konseptualisasi hingga finalisasi. Fungsi utama meliputi penerjemahan data acara pelanggan yang diinput melalui formulir online ke dalam visual desain yang menarik dan sesuai tema, pelaksanaan revisi sesuai masukan pelanggan yang disampaikan melalui sistem design proof approval, hingga penyiapan file akhir siap cetak dalam format yang sesuai standar industri percetakan (biasanya PDF print-ready dengan bleed dan crop marks). Peran desainer dalam creative industry tidak hanya sebagai executor tetapi juga sebagai creative problem solver yang mentransformasi kebutuhan klien menjadi solusi visual yang efektif (Lawson & Dorst, 2020).

Desainer berkoordinasi dengan admin dalam mengunggah design proof ke dalam sistem untuk mendapatkan persetujuan pelanggan sebelum melanjutkan proses ke tahap produksi. Setiap revisi yang diminta pelanggan tercatat dalam sistem dengan timestamp dan notes spesifik, memudahkan desainer untuk memahami perubahan yang diinginkan tanpa harus melakukan komunikasi bolak-balik melalui chat. Sistem tracking ini menciptakan what is termed as design accountability, dimana setiap iterasi design terdokumentasi dengan baik (Cross, 2021). Setelah design proof mendapat status "Approved" dari pelanggan, desainer menyiapkan file final dan mengirimkannya ke percetakan mitra untuk proses produksi fisik dengan memastikan file memenuhi technical specification yang dipersyaratkan.

#### d. Koordinasi Antar Lini

Koordinasi antar lini dalam struktur organisasi Toko Dua Insan Story dilakukan secara terintegrasi melalui sistem berbasis web yang telah dikembangkan, mencerminkan penerapan workflow automation dalam business process management (van der Aalst, 2020). Setiap pesanan memiliki status tracking yang dapat dilihat oleh semua pihak terkait (pemilik, admin, desainer) secara real-time, menciptakan transparansi operasional yang mendukung collaborative work environment. Sistem notifikasi email otomatis memastikan setiap pihak mendapat informasi update status pesanan secara proaktif tanpa perlu melakukan manual checking.

Sebagai ilustrasi, ketika pelanggan melakukan pembayaran, admin mendapat notifikasi untuk memverifikasi pembayaran; setelah diverifikasi, desainer mendapat notifikasi untuk mulai membuat desain; setelah design proof di-upload, pelanggan mendapat notifikasi untuk melakukan review dan approval. Proses terintegrasi ini memastikan setiap pesanan dapat diselesaikan sesuai tenggat waktu dan meminimalisir kesalahan komunikasi yang sering terjadi pada sistem manual. Implementasi workflow management system seperti ini terbukti meningkatkan process efficiency dan mengurangi cycle time dalam operasional bisnis (Dumas et al., 2020).

Struktur organisasi ini menjadi dasar dalam perancangan hak akses, alur kerja (workflow), serta pembagian fungsi dalam sistem pemesanan desain undangan berbasis web yang dikembangkan, yang selanjutnya akan dibahas pada BAB III.

### 2.3 Tata Laksana Sistem Berjalan

Sistem informasi manual merupakan pendekatan konvensional dalam pengelolaan proses bisnis yang masih banyak ditemukan pada UMKM di Indonesia, dimana seluruh aktivitas operasional dilakukan tanpa dukungan teknologi informasi yang terintegrasi (Rahayu & Day, 2020). Karakteristik utama sistem manual meliputi ketergantungan pada komunikasi interpersonal, pencatatan berbasis dokumen fisik atau digital sederhana, serta proses yang bersifat sequential dan memerlukan intervensi manusia pada setiap tahapan. Meskipun pendekatan manual memberikan fleksibilitas dan personal touch dalam interaksi dengan pelanggan, sistem ini memiliki keterbatasan inheren terkait scalability, consistency, dan traceability (O'Brien & Marakas, 2021). 

Pada Toko Dua Insan Story, sebelum implementasi sistem berbasis web, seluruh proses operasional masih dijalankan sepenuhnya secara manual tanpa dukungan sistem informasi yang terintegrasi. Kondisi ini menciptakan berbagai inefficiency dan risiko operational error yang menghambat pertumbuhan bisnis. Analisis terhadap sistem yang berjalan dilakukan untuk mengidentifikasi pain points dan bottlenecks yang menjadi dasar perancangan solusi berbasis teknologi informasi. Untuk memberikan gambaran yang komprehensif, berikut disajikan flowchart yang mengilustrasikan alur proses pemesanan pada sistem manual yang berjalan saat ini.

---

![Gambar 2.2 - Sistem Berjalan Pemesanan Undangan](images/gambar-2.2.png)

*Sumber: Analisis Sistem Berjalan, 2025*  
**Gambar 2.2** Sistem Berjalan Pemesanan Undangan

---

Pada Gambar 2.2 ditunjukkan flowchart sistem berjalan untuk proses Pemesanan Undangan, yang memetakan interaksi antara Pelanggan dan Admin. Proses dimulai dari sisi Pelanggan yang Melihat promosi di media sosial dan menghubungi Admin melalui WhatsApp atau Instagram Direct Message. Admin kemudian Memberikan format data pesanan secara manual melalui chat, termasuk informasi yang perlu diisi seperti data mempelai, data acara, jumlah pesanan, dan pilihan produk. Selanjutnya, Pelanggan melakukan proses manual dengan Mengisi data acara dalam format teks dan mengirimkannya kembali via chat.

Setelah menerima data pesanan, Admin Menghitung total harga secara manual menggunakan kalkulator, termasuk perhitungan biaya cetak, biaya kertas, aksesoris tambahan, dan estimasi ongkos kirim. Total harga disampaikan kepada Pelanggan melalui pesan. Pelanggan kemudian melakukan pembayaran melalui transfer bank dan mengirimkan bukti transfer (screenshot atau foto) kepada Admin via chat. Admin menerima bukti transfer dan masuk ke alur pemeriksaan manual untuk memvalidasi pembayaran dengan cara membuka aplikasi mobile banking, mengecek mutasi rekening, dan mencocokkan nominal dengan pesanan. Jika pembayaran valid, Admin akan Mencatat pesanan ke dalam Buku Pesanan (ditandai dengan simbol dokumen fisik) yang berisi informasi nomor pesanan, nama pelanggan, jumlah, total pembayaran, dan deadline. Terakhir, Admin meneruskan data tersebut kepada bagian Desainer untuk diproses, dan proses pemesanan dianggap selesai di tahap administrasi.

Flowchart tersebut menggambarkan dengan jelas bahwa seluruh proses dilakukan secara manual tanpa sistem otomatis, mengandalkan komunikasi via chat dan pencatatan fisik, yang rentan terhadap kesalahan dan memakan waktu. Berikut adalah analisis terhadap setiap tahapan proses yang berjalan saat ini:

#### a. Analisis Proses Pemesanan Manual

Sebagaimana terlihat pada Gambar 2.2, proses pemesanan pada sistem manual berlangsung melalui communication-intensive process dimana setiap transaksi memerlukan multiple rounds of interaction antara pelanggan dan admin melalui aplikasi pesan instan (WhatsApp atau Instagram Direct Message). Pelanggan yang tertarik untuk memesan harus terlebih dahulu menghubungi admin untuk meminta informasi mengenai katalog produk, harga, dan tata cara pemesanan. Ketiadaan katalog online yang terstruktur mengharuskan pelanggan untuk bertanya satu per satu tentang setiap aspek produk, menciptakan information asymmetry yang tidak efisien (Akerlof, 1970).

Setelah mendapatkan informasi produk, admin memberikan format data pesanan secara manual melalui pesan teks atau dokumen yang harus diisi oleh pelanggan. Format ini mencakup informasi lengkap tentang acara seperti nama lengkap mempelai, nama orang tua, tanggal dan waktu acara, lokasi, jumlah undangan, serta preferensi desain dan material. Proses pengisian data secara manual melalui aplikasi chat ini highly susceptible to human error, termasuk typo, kesalahan penulisan nama, tanggal yang salah, atau informasi yang tidak lengkap (Reason, 2020). Data quality issues yang timbul pada tahap ini seringkali baru teridentifikasi pada tahap produksi, menyebabkan rework yang costly dan time-consuming.

Perhitungan total biaya dilakukan secara manual oleh admin menggunakan kalkulator, meliputi perhitungan harga base design, biaya material kertas, aksesoris tambahan, biaya finishing, serta estimasi ongkos kirim. Perhitungan ongkos kirim manual dilakukan dengan mengecek website ekspedisi satu per satu untuk mendapatkan estimasi biaya berdasarkan berat dan tujuan pengiriman. Proses manual calculation ini tidak hanya memakan waktu lama tetapi juga prone to computational error, terutama ketika terdapat banyak kombinasi pilihan produk (Hollnagel, 2021). Setelah total harga disampaikan kepada pelanggan melalui pesan, jika pelanggan setuju, proses dilanjutkan ke pembayaran melalui transfer bank dengan pengiriman bukti transfer berupa screenshot.

Verifikasi pembayaran dilakukan secara manual dengan cara admin membuka aplikasi mobile banking, memeriksa mutasi rekening, dan mencocokkan nominal pembayaran dengan pesanan. Proses manual verification ini memiliki beberapa kelemahan signifikan: (1) time lag antara pembayaran dan verifikasi yang bisa mencapai beberapa jam hingga satu hari kerja; (2) risiko missed transaction jika admin sedang sibuk atau lupa melakukan checking; (3) tidak ada automated notification sehingga pelanggan tidak mendapat konfirmasi instant; dan (4) kesulitan dalam reconciliation untuk volume transaksi yang tinggi (Romney & Steinbart, 2021). Setelah pembayaran dinyatakan valid, pesanan dicatat dalam buku pesanan manual atau aplikasi notes sederhana dengan manual numbering, kemudian diteruskan kepada desainer melalui komunikasi informal tanpa sistem notifikasi otomatis.

#### b. Analisis Proses Produksi dan Persetujuan Desain

Proses produksi desain dimulai ketika desainer menerima data pesanan dari admin dalam bentuk pesan teks atau dokumen, kemudian membuat desain undangan menggunakan software desain grafis. Setelah desain selesai, file hasil desain dengan watermark "DRAFT" dikirimkan kepada admin, yang kemudian meneruskan kepada pelanggan untuk approval process. Proses design proof approval yang tidak terstruktur ini merupakan critical bottleneck dalam sistem yang berjalan (sebagaimana terlihat pada Gambar 2.2 dalam tahap pasca-pembayaran) dan menjadi sumber utama inefficiency operasional (Cooper & Press, 2020).

Dalam sistem manual, approval desain dilakukan melalui pengiriman file gambar via aplikasi chat dimana pelanggan memberikan feedback berupa pesan teks yang seringkali ambiguous dan tidak spesifik, seperti "warna kurang cocok" atau "font-nya diganti yang lebih elegan" tanpa reference point yang jelas. Proses komunikasi revisi yang iterative ini dilakukan berulang kali melalui chat tanpa ada revision tracking system yang memadai. Permasalahan utama yang timbul meliputi: (1) tidak ada history tracking untuk mengetahui versi desain mana yang sudah di-review atau approved; (2) komunikasi bisa terlewat karena chat tertumpuk dengan percakapan lain; (3) ambiguitas feedback memerlukan multiple rounds of clarification; (4) tidak ada formal confirmation mechanism sehingga pelanggan bisa berubah pikiran setelah memberikan verbal approval; dan (5) file desain versi lama sulit ditemukan kembali jika pelanggan ingin rollback ke versi sebelumnya (Nielsen & Mack, 2020).

Ketiadaan structured design approval workflow menciptakan what is termed as design uncertainty, dimana tidak ada clear definition of done yang menandakan desain telah final dan ready for production (Buxton, 2020). Kondisi ini mengakibatkan production delay, increased revision cycles, dan potential conflict dengan pelanggan terkait ekspektasi hasil akhir. Setelah desain "disetujui" secara informal, file final dikirim ke percetakan mitra melalui email atau aplikasi pesan tanpa production tracking system yang memadai.

#### c. Analisis Sistem Pelaporan dan Manajemen Data

Sistem pelaporan pada kondisi existing berjalan secara manual dengan melakukan rekapitulasi akhir periode (bulanan) berdasarkan buku catatan pesanan yang telah terisi. Pemilik atau admin melakukan manual tabulation menggunakan kalkulator untuk menjumlahkan seluruh pendapatan, mengelompokkan data berdasarkan kategori produk, menghitung rata-rata nilai pesanan, mengidentifikasi produk terlaris, serta membuat laporan pendapatan bulanan. Proses manual data processing ini sangat memakan waktu (estimasi 2-4 jam per periode) dan highly prone to computational error (Laudon & Laudon, 2021). Untuk memberikan gambaran visual tentang alur proses pelaporan manual ini, berikut disajikan flowchart sistem berjalan.

---

![Gambar 2.3 - Sistem Berjalan Laporan Penjualan](images/gambar-2.3.png)

*Sumber: Analisis Sistem Berjalan, 2025*  
**Gambar 2.3** Sistem Berjalan Laporan Penjualan

---

Pada Gambar 2.3 ditunjukkan flowchart sistem berjalan untuk proses Laporan Penjualan, yang dilakukan oleh Pemilik atau Admin pada akhir periode (bulanan). Proses dimulai saat Admin Mengambil buku catatan pesanan yang telah terisi selama satu periode. Buku ini berisi catatan manual semua transaksi yang terjadi dalam satu bulan. Selanjutnya, Admin melakukan serangkaian proses manual. Pertama, Admin Menjumlahkan semua pendapatan pesanan menggunakan kalkulator, yang ditandai dengan simbol operasi manual. Proses ini meliputi penjumlahan total pesanan, pengelompokan berdasarkan jenis produk, perhitungan rata-rata nilai pesanan, dan identifikasi produk terlaris. Proses ini memakan waktu 2-4 jam dan rentan terhadap kesalahan perhitungan. Kedua, hasil rekapitulasi tersebut dicatat dan dibuat dalam bentuk Buku Laporan Bulanan, yang ditandai dengan simbol dokumen fisik. Laporan ini berisi ringkasan penjualan bulan tersebut dengan format tabel sederhana yang ditulis tangan atau diketik di dokumen spreadsheet sederhana. Terakhir, Pemilik Memeriksa laporan tersebut secara visual untuk mengevaluasi kinerja bisnis, yang juga merupakan operasi manual. Pemilik membaca laporan, menganalisis angka-angka, dan membuat keputusan strategis berdasarkan intuisi dan pengalaman tanpa bantuan data visualization atau business intelligence tools. Proses manual ini diakhiri setelah laporan disetujui atau diarsipkan oleh Pemilik untuk referensi di masa mendatang.

Flowchart tersebut menunjukkan bahwa proses pelaporan masih sangat manual, tidak efisien, dan tidak memberikan insight yang mendalam untuk pengambilan keputusan bisnis yang lebih baik. Lebih fundamental lagi, sistem pencatatan manual memiliki keterbatasan serius dalam aspek data integrity dan analytical capability. Jika ada pesanan yang tidak tercatat atau transaksi yang terlewat, data laporan menjadi tidak akurat dan tidak reliable untuk pengambilan keputusan bisnis (Redman, 2020). Ketiadaan database management system yang terstruktur menyebabkan data stored in silos yang tidak terintegrasi, sehingga sulit untuk melakukan cross-referencing atau advanced analytics. Pemilik tidak memiliki akses ke business intelligence tools yang dapat memberikan insights seperti trend analysis, customer segmentation, product profitability analysis, atau seasonal pattern identification (Davenport & Harris, 2020).

Laporan yang dihasilkan bersifat descriptive (menjelaskan apa yang terjadi) tanpa kemampuan diagnostic (mengapa terjadi), predictive (apa yang akan terjadi), atau prescriptive (apa yang harus dilakukan). Keterbatasan analytical insight ini menghambat kemampuan manajemen dalam melakukan strategic planning, resource optimization, dan proactive decision making (Provost & Fawcett, 2021). Sebagai contoh, pemilik tidak dapat dengan mudah menjawab pertanyaan bisnis strategis seperti: produk mana yang paling menguntungkan (profit margin analysis), kapan timing optimal untuk launching promo (seasonal trend analysis), customer mana yang memiliki highest lifetime value (customer analytics), atau berapa average cycle time dari order hingga delivery (process efficiency metrics).

#### d. Identifikasi Permasalahan Sistemik

Berdasarkan analisis komprehensif terhadap tata laksana sistem yang berjalan, permasalahan dapat dikategorikan ke dalam tiga aspek utama yang saling berkaitan dan menciptakan systemic inefficiency dalam operasional bisnis Toko Dua Insan Story.

Pertama, dari aspek **Communication and Data Quality**, sistem manual menciptakan multiple points of failure dalam information flow. Proses pengisian data acara secara manual melalui aplikasi chat memiliki error rate yang tinggi dengan risiko kesalahan informasi seperti typo, misspelling, atau data incomplete yang seringkali baru teridentifikasi pada tahap produksi akhir, menyebabkan costly rework. Komunikasi berbasis chat yang tidak terstruktur menyebabkan information overload dan message loss, dimana informasi penting dapat tertimbun oleh percakapan lain. Tidak adanya centralized information repository mengakibatkan data tersebar di berbagai media (chat history, notes, buku fisik) yang sulit diakses dan diverifikasi. Kondisi ini sejalan dengan teori information asymmetry dan communication breakdown yang sering terjadi pada sistem manual (Shannon & Weaver dalam Rogers, 2020).

Kedua, dari aspek **Process Efficiency and Workflow Management**, sistem yang berjalan memiliki karakteristik sequential process dengan multiple manual checkpoints yang menciptakan significant time lag pada setiap tahapan (sebagaimana divisualisasikan dalam Gambar 2.2). Proses pemesanan yang memerlukan back-and-forth communication manual menyebabkan customer experience yang kurang optimal dengan waiting time yang excessive. Critical bottleneck terjadi pada design approval process dimana tidak adanya structured workflow dan revision tracking system menyebabkan confusion, repeated clarification, dan production delay. Perhitungan biaya dan ongkos kirim manual memakan waktu lama dan rentan kesalahan, mengurangi customer satisfaction. Verifikasi pembayaran yang dilakukan secara manual memiliki time lag signifikan dan risiko missed transaction. Ketiadaan automated notification system mengharuskan reminder manual yang tidak reliable. Kondisi ini mencerminkan inefficiency karakteristik dari unautomated business process (Hammer & Champy, 2020; Dumas et al., 2020).

Ketiga, dari aspek **Data Management and Business Intelligence**, sistem pencatatan manual menghasilkan unstructured data yang tidak terintegrasi dan sulit dianalisis untuk keperluan strategic decision making. Proses rekapitulasi manual yang time-consuming dan error-prone (seperti yang digambarkan dalam Gambar 2.3) menghasilkan laporan yang sering tidak accurate dan tidak timely. Ketiadaan real-time monitoring capability mengakibatkan manajemen tidak memiliki visibility terhadap operational performance saat ini. Tidak tersedianya analytical tools dan data visualization menyebabkan missed opportunity dalam identifying business patterns, customer behavior, dan market trends. Tidak ada systematic mechanism untuk collecting dan analyzing customer feedback sehingga continuous improvement efforts tidak data-driven. Keterbatasan ini sejalan dengan literatur tentang importance of management information systems dan business analytics dalam competitive advantage (Porter & Millar, 2021; Laudon & Laudon, 2021).

Permasalahan-permasalahan sistemik ini bukan hanya berdampak pada operational efficiency tetapi juga menghambat business scalability dan growth potential. Ketika volume pesanan meningkat, sistem manual tidak dapat scale up secara proportional karena heavily dependent on human capacity yang terbatas. Kualitas service cenderung inconsistent karena bergantung pada ketersediaan dan kondisi admin/desainer pada saat tertentu. Customer experience menjadi tidak predictable dan kurang professional dibandingkan dengan kompetitor yang telah mengadopsi digital system. Kondisi ini menciptakan urgent need untuk transformasi digital melalui implementasi integrated web-based ordering system yang dapat mengatasi permasalahan-permasalahan yang telah diidentifikasi (Westerman et al., 2020).

---

Berdasarkan analisis komprehensif terhadap tata laksana sistem yang berjalan, dapat disimpulkan bahwa Toko Dua Insan Story menghadapi berbagai keterbatasan sistemik yang inheren dalam sistem manual, meliputi inefficiency dalam communication flow, absence of structured workflow management, lack of data integrity mechanism, dan limited analytical capability untuk mendukung strategic decision making. Permasalahan-permasalahan ini tidak dapat diselesaikan melalui perbaikan inkremental pada sistem existing, melainkan memerlukan transformasi fundamental melalui implementasi sistem informasi berbasis teknologi web yang terintegrasi (Westerman et al., 2020).

Sistem yang akan dikembangkan perlu memiliki kapabilitas untuk mengotomatisasi proses-proses kunci, meliputi katalog produk dengan fitur search dan filtering, formulir pemesanan terstruktur dengan validasi data, perhitungan biaya otomatis terintegrasi dengan API pihak ketiga untuk ongkos kirim, payment gateway integration dengan automated verification, sistem design proof approval yang terstruktur dengan comprehensive revision tracking, automated notification system pada setiap tahap proses, serta business intelligence dashboard dengan real-time analytics. Implementasi sistem terintegrasi semacam ini terbukti efektif dalam meningkatkan operational efficiency, enhancing customer experience, dan enabling data-driven decision making pada UMKM kreatif (Rahayu & Day, 2020; Laudon & Laudon, 2021).

Fokus utama perancangan sistem adalah mengatasi critical bottleneck dalam design approval workflow, dimana ketiadaan structured approval mechanism pada sistem manual menciptakan ambiguity, delays, dan potential conflicts yang menghambat produktivitas. Sistem yang akan dikembangkan diharapkan dapat mentransformasi proses bisnis dari communication-intensive manual workflow menjadi automated, traceable, dan efficient digital workflow yang memberikan nilai tambah signifikan bagi pelanggan maupun pengelola usaha.

---

## DAFTAR PUSTAKA

Akerlof, G. A. (1970). The Market for "Lemons": Quality Uncertainty and the Market Mechanism. *The Quarterly Journal of Economics*, 84(3), 488-500.

Ambrose, G., & Harris, P. (2020). *The Fundamentals of Graphic Design* (3rd ed.). Bloomsbury Visual Arts.

Banks, A., & Porcello, E. (2020). *Learning React: Modern Patterns for Developing React Apps* (2nd ed.). O'Reilly Media.

Bann, D. (2020). *The Print Production Handbook* (4th ed.). Routledge.

Beck, K., & Andres, C. (2004). *Extreme Programming Explained: Embrace Change* (2nd ed.). Addison-Wesley Professional.

Buxton, B. (2020). *Sketching User Experiences: Getting the Design Right and the Right Design* (2nd ed.). Morgan Kaufmann.

Chen, Y. H., & Chang, C. H. (2021). What Drives Purchase Intention on Online Shopping Platforms? Perspectives of E-Service Quality and Perceived Value. *International Journal of Information Management*, 58, 102311.

Cooper, R., & Press, M. (2020). *The Design Experience: The Role of Design and Designers in the Twenty-First Century* (2nd ed.). Routledge.

Cross, N. (2021). *Design Thinking: Understanding How Designers Think and Work* (2nd ed.). Bloomsbury Visual Arts.

Daft, R. L. (2021). *Organization Theory and Design* (13th ed.). Cengage Learning.

Davenport, T. H., & Harris, J. G. (2020). *Competing on Analytics: Updated with a New Introduction: The New Science of Winning* (2nd ed.). Harvard Business Review Press.

Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. (2020). *Fundamentals of Business Process Management* (2nd ed.). Springer.

Elmasri, R., & Navathe, S. B. (2016). *Fundamentals of Database Systems* (7th ed.). Pearson.

Garrett, J. J. (2021). *The Elements of User Experience: User-Centered Design for the Web and Beyond* (3rd ed.). New Riders.

Hammer, M., & Champy, J. (2020). *Reengineering the Corporation: A Manifesto for Business Revolution* (Revised ed.). HarperBusiness.

Harianto, S., Kusuma, A. P., & Wijaya, T. (2021). Digitalisasi Sistem Pemesanan Berbasis Web untuk Meningkatkan Efisiensi Bisnis UMKM. *Jurnal Teknologi Informasi dan Komunikasi*, 12(2), 145-158.

Hollnagel, E. (2021). *The ETTO Principle: Efficiency-Thoroughness Trade-Off: Why Things That Go Right Sometimes Go Wrong*. CRC Press.

Juran, J. M., & De Feo, J. A. (2020). *Juran's Quality Handbook: The Complete Guide to Performance Excellence* (7th ed.). McGraw-Hill Education.

Kementerian Pariwisata dan Ekonomi Kreatif. (2022). *Laporan Ekonomi Kreatif Indonesia 2022*. Jakarta: Kemenparekraf RI.

Kotler, P., & Keller, K. L. (2022). *Marketing Management* (16th ed.). Pearson.

Laudon, K. C., & Laudon, J. P. (2021). *Management Information Systems: Managing the Digital Firm* (16th ed.). Pearson.

Laudon, K. C., & Traver, C. G. (2021). *E-Commerce 2021-2022: Business, Technology and Society* (17th ed.). Pearson.

Lawson, B., & Dorst, K. (2020). *Design Expertise* (2nd ed.). Routledge.

Lemon, K. N., & Verhoef, P. C. (2020). Understanding Customer Experience Throughout the Customer Journey. *Journal of Marketing*, 80(6), 69-96.

Longenecker, J. G., Petty, J. W., Palich, L. E., & Hoy, F. (2020). *Small Business Management: Launching and Growing Entrepreneurial Ventures* (19th ed.). Cengage Learning.

Mintzberg, H. (2021). *Managing* (2nd ed.). Berrett-Koehler Publishers.

Mullins, L. J. (2021). *Management and Organisational Behaviour* (12th ed.). Pearson.

Nielsen, J. (2020). Usability and User Experience in Design Approval Systems. *Nielsen Norman Group Reports*, 8(4), 22-35.

Nielsen, J., & Mack, R. L. (Eds.). (2020). *Usability Inspection Methods*. John Wiley & Sons.

Norman, D. A. (2013). *The Design of Everyday Things: Revised and Expanded Edition*. Basic Books.

O'Brien, J. A., & Marakas, G. M. (2021). *Management Information Systems* (11th ed.). McGraw-Hill Education.

Pine, B. J., & Gilmore, J. H. (2021). *The Experience Economy: Competing for Customer Time, Attention, and Money* (Updated ed.). Harvard Business Review Press.

Porter, M. E. (2020). *Competitive Strategy: Techniques for Analyzing Industries and Competitors* (Updated ed.). Free Press.

Porter, M. E., & Millar, V. E. (2021). How Information Gives You Competitive Advantage. *Harvard Business Review*, 63(4), 149-160.

Prasetyo, D., & Widodo, A. (2023). Implementasi API Integration untuk Optimalisasi Sistem E-Commerce di Indonesia. *Jurnal Sistem Informasi dan Teknologi*, 15(1), 67-80.

Pressman, R. S., & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). McGraw-Hill Education.

Provost, F., & Fawcett, T. (2021). *Data Science for Business: What You Need to Know about Data Mining and Data-Analytic Thinking* (2nd ed.). O'Reilly Media.

Rahayu, R., & Day, J. (2020). Determinant Factors of E-Commerce Adoption by SMEs in Developing Country: Evidence from Indonesia. *Procedia - Social and Behavioral Sciences*, 195, 142-150.

Reason, J. (2020). *Human Error* (25th Anniversary ed.). Cambridge University Press.

Redman, T. C. (2020). *Data Driven: Profiting from Your Most Important Business Asset*. Harvard Business Review Press.

Robbins, S. P., & Coulter, M. (2022). *Management* (15th ed.). Pearson.

Rogers, E. M. (2020). *Diffusion of Innovations* (5th ed.). Free Press.

Romney, M. B., & Steinbart, P. J. (2021). *Accounting Information Systems* (15th ed.). Pearson.

Santoso, B., Kusuma, H., & Pratama, R. (2023). Penerapan React.js dalam Pengembangan Aplikasi Web Single Page Application yang Responsif dan Interaktif. *Jurnal Informatika dan Komputer*, 14(3), 201-215.

Sommerville, I. (2021). *Software Engineering* (10th ed.). Pearson.

Stauffer, M. (2019). *Laravel: Up & Running: A Framework for Building Modern PHP Apps* (2nd ed.). O'Reilly Media.

Tambunan, T. T. H. (2021). *The Role of MSMEs in Economic Development: The Indonesian Story*. Routledge.

Turban, E., Whiteside, J., King, D., & Outland, J. (2018). *Introduction to Electronic Commerce and Social Commerce* (4th ed.). Springer.

Valenty, M., Saputra, A., & Kurniawan, D. (2024). Perancangan Sistem Informasi Berbasis Laravel dengan Arsitektur MVC untuk Meningkatkan Kualitas Pengembangan Aplikasi Web. *Jurnal Rekayasa Perangkat Lunak*, 16(2), 88-102.

van der Aalst, W. M. P. (2020). *Process Mining: Data Science in Action* (2nd ed.). Springer.

Westerman, G., Bonnet, D., & McAfee, A. (2020). *Leading Digital: Turning Technology into Business Transformation*. Harvard Business Review Press.

Wibowo, R., & Susanto, E. (2022). Integrasi RajaOngkir API untuk Perhitungan Ongkos Kirim Real-Time pada Sistem E-Commerce. *Jurnal Teknologi dan Sistem Informasi Bisnis*, 13(3), 112-125.

Womack, J. P., & Jones, D. T. (2021). *Lean Thinking: Banish Waste and Create Wealth in Your Corporation* (Revised ed.). Free Press.

Zeithaml, V. A., Bitner, M. J., & Gremler, D. D. (2020). *Services Marketing: Integrating Customer Focus Across the Firm* (8th ed.). McGraw-Hill Education.

Zimmerer, T. W., Scarborough, N. M., & Wilson, D. (2020). *Essentials of Entrepreneurship and Small Business Management* (9th ed.). Pearson.

---

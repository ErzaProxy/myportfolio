Nama : Muhammad Raihan Al Qadri Kusumaputra 
NPM : 2506602334 
Kelas : PBP B 

Penamaan versi saya: 0.<Assignement Ke-i>.<Update no-j>
(masih menggunakan 0. karena menurut saya belum 100% full release/selesai)
Penggunaan Generative AI pada Assignment 1 Meliputi:
v0.1.1:
AI Agent yang digunakan: Gemini Pro
- Pembuatan glassy effect di navbar, untuk sticky navbarnya sendiri saya buat secara pribadi untuk struktur dari navigation barnya, namun saya pribadi masih belum tahu cara implement glassy effect di css html, sehingga saya menggunakan AI untuk membantu saya melakukan hal tersebut.
- Mentranslasikan beberapa hal yang ada di figma saya, seperti ukuran, saran untuk implement pattern backgroundnya bagaimana (yang setelah itu saya coba implement dan sesuaikan tersendiri).
- mempelajari @keyframe dan keyframe apa saja yang related untuk ide ide saya (seperti fading text dan juga jumping button) yang setelah itu saya sesuaikan lagi sesuai dengan keperluan saya
v0.1.2:
- Membantu dalam mencari cara untuk membuat sistem carousel dan juga clickable changing image tanpa menggunakan javascript. dimana AI menyarankan untuk menggunakan metode hidden radio button (display: none), dan juga memanipulasi elemen dengan selector
- Debugging, pada awalnya terdapat bug pada layout site karena menggunakan fixed position untuk tiap bagiannya, sehingga section about me ada di height yang tidak seharusnya, sehingga AI menyarankan untuk menggunakan position relative dan memainkan marginnya
v0.1.3:
- Hanya untuk mengecek apakah dengan native html dan css posibble untuk membuat saat responsive nanti, card di carouselnya hanya ditampilkan 1 di mobile dan tablet, namun 2 desktop. supaya tidak perlu merombak terlalu banyak nanti saya ketika implement responsiveness
v0.1.4:
- Membantu debugging dalam responsivity, misalnya ada yang posisinya belum oke, atau tadi ada gambar yang menutupi teks, dsb.
- Last check memastikan tidak terdapat bug tersisa pada kode saya

Pertanyaan Reflektif:
Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?
Secara keseluruhan, saya lebih dominan menggunakan tag <div> dibandingkan elemen semantik HTML5 seperti <section>, <article>, atau <aside>. Hal ini terjadi karena saya jauh lebih terbiasa dengan <div>, dan pendekatannya terasa lebih selaras saat melakukan slicing desain dari Figma. Meskipun menggunakan tag non-semantik, kebutuhan desain saya tetap terpenuhi dengan baik karena saya mengompensasinya melalui penamaan atribut id dan class yang sangat deskriptif. Pendekatan ini memastikan struktur dan hierarki kode tetap mudah dibaca dan di-maintain, meskipun secara tag dasar semuanya menggunakan elemen pembungkus generik.

Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?
Tantangan terbesar dalam menjaga tata letak tetap responsif dan menarik adalah transisi dari tata letak statis/absolut (desain Figma) ke normal document flow (relatif). Awalnya, mempertahankan desain 1:1 sering kali memunculkan bug di mana section memiliki jarak kosong yang terlalu jauh atau elemen yang overlap saat ukuran layar mengecil. Elemen-elemen yang sebelumnya berjejer secara horizontal di desktop seperti foto profil dengan teks bio, atau tata letak kiri-kanan pada komponen Education—saya prioritaskan untuk ditumpuk secara vertikal (flex-direction: column). Saya juga memprioritaskan penyesuaian ukuran teks dan memberikan batasan lebar maksimal agar elemen tidak overflow ke luar batas layar (off-screen), sehingga secara visual tetap menarik di perangkat kecil.

Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?
Batasan utama yang sangat terasa pada static web murni adalah kekakuan dalam mengelola komponen yang memuat banyak data berulang, seperti carousel/slider pada bagian Experience dan Interest. Untuk saat ini, saya harus mengakalinya menggunakan trik CSS Hidden Radio Button murni karena ketiadaan JavaScript. Ini membuat struktur HTML menjadi repetitif, sangat panjang, dan sulit di-maintain saat mengatur responsivitasnya, bahkan ada yang harus saya rombak ulang idenya (carousel experience). Berdasarkan batasan tersebut, fungsionalitas yang paling ingin saya tambahkan pada iterasi selanjutnya adalah implementasi JavaScript murni untuk mengatur state navigasi carousel agar lebih luwes. 

Sebelumnya untuk versi v0.2.x saya saya izin membuat multiple css files, supaya menghindari terjadinya tumpang tindih style, dan juga menghindari code css yang terlalu panjang. pembedaan css untuk tiap page ini juga bertujuan supaya lebih mudah untuk melakukan tracking terhadap error dan sebagainya
AI Agent yang digunakan: Gemini Pro
v0.2.1:
- Membantu dalam pembuatan menu (banyak bug yang terjadi pada percobaan pertama), terutama dalam urusan ukuran dan layout.
- sempat ada bug dimana (nama).html gak bisa detect (nama).css sehingga saya meminta bantuan AI untuk mencari tahu ada masalah apa, namun tampaknya ia juga tidak paham, hingga entah somehow bagaimana ketika saya ubah nama filenya bisa, saya sendiri masih bingung hingga titik ini
- bantu mempercepat refaktor, nentuin attribut css apa aja yang perlu dipindah supaya lebih cepat

v0.2.2:
- Membantu membuat JSON File supaya lebih cepat aja untuk memasukkan data baru ke database. (Terinspirasi dari Yasmin kelas PBP B)
- Memastikan unit test sudah mengcover seluruh permintaan

1. Ketika pengguna membuka halaman portofolio, request dari browser pertama kali diterima oleh urls.py tingkat proyek, yang kemudian merutekannya ke urls.py tingkat aplikasi. URL di aplikasi akan mencocokkan path tersebut dan memanggil fungsi yang sesuai di dalam views.py. View bertindak sebagai otak dari alur ini; ia akan mengambil data yang dibutuhkan dari database melalui models.py, lalu mengirimkan data tersebut ke dalam template. Terakhir, template akan merender data tersebut menjadi halaman web utuh yang dikirim kembali sebagai respons untuk ditampilkan pada browser pengguna.
2. Menyimpan data portofolio pada model jauh lebih baik daripada menuliskannya langsung di dalam template karena membuat halaman web menjadi dinamis dan sangat mudah dikelola. Jika data ditulis langsung di HTML, setiap ada penambahan atau perubahan informasi proyek, pengembang harus membongkar dan mengedit kode sumber secara manual, yang rawan error dan tidak efisien. Dengan menggunakan model, data dipisahkan sepenuhnya dari struktur tampilan, sehingga pembaruan konten dapat dilakukan dengan mudah, misalnya melalui panel Admin, kapan saja tanpa perlu menyentuh kode aplikasi sama sekali.
3. makemigrations berfungsi untuk mendeteksi setiap perubahan yang dilakukan pada kode model dan membuatkan file riwayat instruksi dari perubahan tersebut, sedangkan migrate berfungsi untuk mengeksekusi instruksi tersebut agar struktur database benar-benar diperbarui sesuai skema. Contohnya, jika menambahkan struktur kolom baru seperti link_github pada model Project yang sudah ada, harus menjalankan makemigrations untuk mencatat rencana penambahan kolom tersebut, lalu menjalankan migrate agar kolom link_github benar-benar dibuat secara fisik di dalam tabel database.

AI Agent yang digunakan: Gemini Pro
v0.3.1:
- Karena saya kan ada beberapa pages yang tidak mengikuti format pages lainnya, saya ingin tau gimana caranya basenya bisa menghandle page saya yang gak ada navbar dsbnya (kayak index dan menu misalkan), dan Gemini memberikan solusi dan penjelasan tentang teknik blockingnya

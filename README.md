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
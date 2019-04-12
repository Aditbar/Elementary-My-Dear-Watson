;; data type

;; Primitif
;; 1. number
(quot 9 5)
(rem 9 5)

;; 2. character
\n 

;; gabung karakter jadi string
(str \y \o \o)

;; 3. Boolean
false
true
(and true false)
(not true)
(= 12 32)
(<= 2 4)

;; fungsion buat ngetes
(neg? 4)
(pos? -23)


;; collection
;; 1. list
'(1 2 3 4 5)

;; 2. vektor
[1 2 3 4]
[123 false :apapun [12 21] "yooo"]

;; 3. Keyword
:harus_nyambung

;; 4. String -> list of character
;; buktinya
(seq "jojon")

;; 5. map
;; urutan penting
{:nama "Budi" :umur 112 :elemen "Avatar"}

;; 6. set
;; urutan gak penting, isinya unique
#{1 2 3 4 5}
#{1 1 2 3 4}
(def mylist '(1 2 3 4 5 6 7 8 9))

(take 4 mylist)
(drop 4 mylist)
(first mylist)
(second mylist)
(rest mylist)
(last mylist)
(butlast mylist)

;; ambil elemen
(nth mylist 0)

(count mylist)


;; bedain conj ma cons di list dan vektor

;; masukin ke depan list, tapi gak bisa banyak
(cons 0 mylist)
;; (0 1 2 3 4 5 6 7 8)

(conj mylist 1 2 3)
;; (3 2 1 1 2 3 4 5 6 7 8 9)


(def myvec [1 2 3 4 5])
(cons 1 myvec)
;; [1 1 2 3 4 5]

;; masukin ke belakang vektor, bisa banyak
(conj myvec 1 2 3 4 5)
;; [1 2 3 4 5 1 2 3 4 5]

;; gabungin 2 hal
;; lebih fleksibel buat gabung2in
(concat mylist myvec)
(concat #{1 2 3} [1 2 3])
(concat myvec 1 2 3)

;; kalo ke map rada aneh

;; generate list
(range 1 10)
;; (1 2 3 4 5 6 7 8 9)

(range 10)
;; (0 1 2 3 4 5 6 7 8 9)

(range 1 10 2)

(repeat 10 2)



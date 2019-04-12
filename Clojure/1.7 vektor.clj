(def myvec [1 2 3 4 5 6])
;; ngebuat vektor
;; input collection
(vec '(1 2 3 4))

;; input bakal jadi elemen elemen di vektornya 
(vector 1 2 3 4 5)
;; [1 2 3 4 5]
(vector '(1 2 3))
;; [(1 2 3)]

(into [] mylist)
(into '() myvec)

;; ambil 1 dari vector
(nth myvec 2)

;; ambil beberapa
(subvec myvec 2 5)
;; [3 4 5]




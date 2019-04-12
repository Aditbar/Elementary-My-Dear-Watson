;; bakal jadi uniq

(set [1])
;; #{1}

(set [1 2 3])
;; #{1 2 3}

;; inpitnya bakal jadi elemen2nya
(hash-set 1 2 3 4 4)
;; #{1 2 3 4}


;; MAP
;; key and value

{1 2 3 4}
;; {1 2, 3 4}

(hash-map 1 2 3 4)
;; {1 2, 3 4}

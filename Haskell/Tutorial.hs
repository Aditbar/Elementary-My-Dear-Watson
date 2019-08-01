module One where

-- global scope, semua kenal
square x = x * x
cube x = x*x*x
quad x = square (square x)
add x y = x + y -- define function
abubakar = 12345 -- define data

-- commend namanya gak dibaca program

-- data type => primitif
-- numbers : rasional, integer, fractional, num, floating
-- Bool : True, False, &&, ||, == (uji kesamaan), /=
-- String : harus terletak diantara 2 kutip "contoh"
--         List of Char
--         "Joni " ++ "jojo" = "Joni jojo"
-- Char : ngutip 1 huruf pake kutip 1 'a'

-- data type => collection
-- list [] = kumpulan primitif types dengan type yang sama, panjang bebas
--          ['q','s','s'] == "qss"
-- tooples () = bisa sepasang, bisa isi 3, 4
--              kayak listm tapi isinya bisa campuran type
--              tapi gak bisa berkembang, panjang 2 cuma 2 (isinya tetap)
-- bisa list of list of something
-- [[1,2],[1,2,3]]
-- [(1,2),(3,4)]
-- bisa bikin range [1,2..10], [1,3..10]
-- [1,2] ++ [3,4] == [1,2,3,4]
-- 123 : [1,2,3] == [123,1,2,3]
-- 1:2:3:[] == [1,2,3]

-- definig functions & data
-- kalo mau define function atau data di ghci pake "let"
-- con : let kokom x = x*10 (function)
--       let done = [1,2,3] (data)
-- buat nulis negatif (-123)

kecap a b c = ((-b) + (sqrt (b^2-4*a*c))) / (2*a) --kusut
kecap2 a b c = ((-b) + det) / (2*a)
  where det = (sqrt (b^2-4*a*c)) -- local scope

-- Conditional
--1. guard ?
kecap3 a b c x
  | x == 1 = ((-b)+ det) / (2*a)
  | x == 2 = ((-b)- det) / (2*a)
  where det = sqrt (b^2-4*a*c)

--2. if
mutlak x = if x >= 0 then x else (-x)

isgede x
  | x > 1000000 = "GEDE"
  | 1000 <= x && x <= 1000000 = "yeah mayan"
  | otherwise = "kecil"

-- 3. Pattern Maching
sayhi "Jojon" = "Hi Jon"
sayhi "Koko" = "Gak kenal"
sayhi x = "Hello " ++ x

-- bisa juga pattern match ditulis dalam haskell
-- let (a:b:xs) = [1,2..5]
-- sehingga a = 1
-- b = 2
-- xs = [3,4,5]

--pattern maching juga berlaku pada tupple ()
-- tidak bisa dalam bentuk let [a,b,c] = [1,2,3,4] tidak ada masalah, tapi tidak bisa di panggil

-- Lambda Function
-- function yang gak perlu di difine, bisa di difine langsung di template
--  \ ini lambang lamda
-- (\x -> x*x ) panah untuk nandain si x mau diapain
-- contoh (\x -> x*x) 12
-- 144
-- bisa di namain
-- add = (\ x y -> x+y)

-- Types and type classes
-- m :: Num t = [t] bacanya there's a number t, dan m adalah list of t, t is a number
--contoh diatas adalh type
x :: int
x = 123

a :: integer
a = 1234

b :: Float
b = 12.34

-- ketika melakukan itu kita mendefinisikan type classes
-- function juga punya type
-- :t square
-- square :: Num a => a -> a
-- yang paling ujung adalah output dan hanya 1, sebelum => hanya penjelas
-- cara bacanya, square adalah suatu function yang menerima sebuah a dan menghasilkan a dimana a adalah number

-- :t iterate
-- iterate :: (a -> a) -> a -> [a]
-- outputnya jelas list of a
-- input 1 (a -> a) berarti function, yang inputnya a menghasilkan a
-- inpute 2 a
-- Eq adalah type yang bisa di uji kesamaanya
-- Enum adalah type yang ada terusannya dan dapat diuji <, >, dll
-- oderable adalah type yang hanya bisa diuji <, >, dll

---------------------- Bab 2 -------------------------------------
--guard akan mencari yang mana true duluan
ngasal x y
  | x == y = "sama"
  | x <= y = "Keciiiil"
  | x >= y = "GUEDEEE"
  | otherwise = "ngasal"
-- saat diinput 3 3 maka hasilnya akan "sama"

ngasal2 x
  | (0 < x) && (x < 5) = "0 sampai 5"
  | ((-2) < x) && (x < 3) = "mantap"
  | otherwise = "ngacooo"

-- fungsi recursion
-- n! = n * n-1 * n-2 .. 1
-- sekarang jelasin ke orang tolol dengan akurat
-- berpikir like a haskell
-- recur = mendefiniskan diri sendiri dengan cara yang berbeda
factorial n
  | n <= 1 = 1
  | otherwise = n * (factorial (n-1))

-- ada 2 bagian recursion, basis (exit point) dan recurannya
-- basis (exit point) mendefinisikan nilainya
-- butuh basis dimana, functionnya punya output yang jelas hasilnya
-- rekurrekuran dibutuhkan untuk mendekatkan function ke basis

-- oprasi : digunakan untuk list
-- kalo oprasi ++ hanya berlaku untuk menambahkan list ke list
-- contoh [1..2] ++ [3..5] = [1..5]
-- sedangkangkan 1 : [2..10] = [1..10]

-- pendalaman postulat
--let a:b = [1,2,3,4,5]
-- a = 1
-- b = [2,3,4,5]

--let [a,b] = [1,2,3,4,5]
-- a = error
-- b = error
-- gak bisa nyamain 2 ke 5

-- let [a:b] = [1,2,3,4,5]
-- a = error
-- b = error

-- let (a:b) = [1,2,3,4,5]
-- a = 1
-- b = [2,3,4,5]

-- ingat :t (:)
-- (:) :: a -> [a] -> [a]
-- inpunya 2, dimana input pertama ada adalah elemen dari list of elemen di input ke 2

-- let (a:b) = [5:[1,2,3,4,5]]
-- a = [5,1,2,3,4,5]
-- b = []

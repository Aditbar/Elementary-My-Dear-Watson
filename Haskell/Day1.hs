module One where

-- data collection
-- list []
-- tupple ()

x = 50
mylist = [1..10]

square x = x*x
cubic x = x*x*x
quad x = square(square x)

-- if function
mutlak x = if x < 0 then (-x) else x 

-- guard
mutlak2 x
 | x < 0 = (-x)
 | x > 0 = x
 | otherwise = x

-- x! = x*(x-1)*.....1

-- recursion
faktorial x
 | x <= 1 = 1
 | otherwise = x * faktorial (x-1)

-- 2 => basis sama recuran

faktorial2 1 = 1
faktorial2 x = x * faktorial2 (x-1)

faktorial3 x = if x <= 1 then 1 else x*faktorial3(x-1)

ngasal x 
 | x > 10 = "oke"
 | x > 50 = "banyak"
 | x > 3 = "kedikitan"
-- yang dibaca true duluan

rekur x
 | x == 3 = "tiga"
 | otherwise = rekur (x-1)

rekurrekuran x y
 | x == 5 = "udahan"
 | otherwise = rekurrekuran (x-y) y 





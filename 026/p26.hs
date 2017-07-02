-- module NumTheory where
import Data.Ratio

myQuotient, myRemainder :: Integral a => a -> a -> a

a `myQuotient` b   
	| b < 0 = ceiling (a % b)
	| b > 0 = floor (a % b)

a `myRemainder` b = a - b * (a `myQuotient` b)

-- main = 1 `myRemainder` 7

-- divisdriver :: Int -> Int
-- divisdriver x = divis x 1
-- 
-- divis :: Int -> Int -> Int
-- divis n d = do
-- 	let q = 0
-- 	let r = n
-- 	divisr q r d
-- 
-- divisr q r d = if r >= d
-- 		then divisr (succ q) (r-d) (d)
-- 		else r
-- 
-- p26 = map (divisdriver) [1..10]
	

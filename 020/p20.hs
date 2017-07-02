import Data.Char

factorial n = product [1..n]

main = do 
	y <- readLn
	let x = (factorial y)
	print x
	print (sum (map digitToInt $ show x))

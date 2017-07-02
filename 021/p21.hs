lowestFactorfromY x y 
	| rem x y == 0 	= y
	| otherwise	= lowestFactorfromY x (y-1) 

factors x y
	| (head y) == 1	= y
	| otherwise	= factors x ((lowestFactorfromY x ((head y)-1)):y)

main = do
	print (factors 10 [5])

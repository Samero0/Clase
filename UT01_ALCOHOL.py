age = int(input("How old are you?: "))

match age:
  
    case 0 | None:
        print(	'Not a person'	)
  
    case n if n < 17:
        print(	'Nope'	)
 
    case  n if n < 22:
        print(	'Not in the US'	)
  
    case _:
        print(	'Yes')  
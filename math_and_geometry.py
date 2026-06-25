#menu
while True:
    menu = ['choose an option',
        '1- triangle area calculater ',
        '2- square area calculater ' ,
        '3- circle area calculater',
        '4- pythagoras triad checker',
        '5- calculater',
        '6- exit']
    print("\n".join(menu))
    user_options = int(input('choose an option for the menu :'))
    
    match user_options:
        case 1:
            base=float(input("enter base "))
            height=float(input("enter height "))
            result=base * height/2
            print(f"formula: base * height /2\n the area is {result}")
        case 2:
            base1 = float(input('enter base '))
            base2 = float(input('enter base '))
            result = base1 * base2 
            print(f'formula: base1 * base2 \n the area is {result}' )
 
        case 3:
            radius=float(input("enter your radius of the circle: "))
            result=float(3.14*radius*radius)
            print(f"fourmula: 3.14*radius*radius \n the circle area is {result}")

      
#foundation
vegetarian = False
vegan = False
gluten_free = False
vegetarian_options = str("Here are your restaurant options: \n Main Street Pizza Company \n Corner Cafe \n Mama's Fine Italian \n The Chef's Kitchen")
vegan_options = str("Here are your restaurant options: \n Corner Cafe \n The Chef's Kitchen")
gluten_options = str("Here are your restaurant options: \n Main Street Pizza Company \n Corner Cafe \n The Chef's Kitchen")
no_options = str("Here are your restaurant options: \n Joe's Gourmet Burgers \n Main Street Pizza Company \n Corner Cafe \n Mama's Fine Italian \n The Chef's Kitchen")
#setting vegetarian
vege_response = str(input('Is anyone in your party vegetarian? '))
if vege_response == 'yes':
    vegetarian = True
#setting vegan
vegan_response = str(input('Is anyone in your party vegan? '))
if vegan_response == 'yes':
    vegan = True
#setting gluten free
gluten_response = str(input('Is anyone in your party gluten free? '))
if gluten_response == 'yes':
    gluten_free = True
#no restricted options
if vegetarian == False:
    if vegan == False:
        if gluten_free == False:
            print(no_options)
#restricted options
if vegetarian == True and vegan == True and gluten_free == True:
    print(vegan_options)
elif vegetarian == True and vegan == True and gluten_free == False:
    print(vegan_options)
elif vegetarian == True and vegan == False and gluten_free == False:
    print(vegetarian_options)
elif vegetarian == True and vegan == False and gluten_free == True:
    print(gluten_options)
elif vegetarian == False and vegan == False and gluten_free == True:
    print(gluten_options)
elif vegetarian == False and vegan == True and gluten_free == False:
    print(vegan_options)
elif vegetarian == False and vegan == False and gluten_free == True:
    print(gluten_options)

def max_three(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        print(num1)
    elif num2>=num1 and num2>=num3:
        print(num2)
    else:
        print(num3)


is_male = True
is_tall = True
if is_male:#this will do the condition if the is_mail true
    print("He is a male")
if is_tall or is_male:#if is tall true will do it or if is_mail true will do is
    print('you are a tall and male')
elif is_tall and not is_male:
    print('you are tall')
elif not is_tall and is_male:
    print('you are short male')
else:
    print('you are not a tall or male')
if is_tall and is_male:
    print('you are a tall male')
else:
    print('you are not a tall male')

max_three(10,45,2)
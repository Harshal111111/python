print("Welcome to the age calculator!!")
def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(f'You are age {age} years old')
y = int(input('Enter Your Birth Year \n'))
m = int(input('Enter Your Birth Month \n'))
d = int(input('Enter Your Birth Day \n'))
ageCalculator(y, m, d)

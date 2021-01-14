print("Welcome to 'Your Life in Weeks'")

age = int(input("What is your current age? "))

leap_years = age // 4
days = ((age - leap_years) * 365) + (leap_years * 366)
num_weeks = days // 52
num_days = round(((days / 52) - num_weeks) * 7, 0)

print(f"you have lived for {int(num_days)} days and {num_weeks} weeks")

def calculate_bmr(age,weigth,heigth,gender,activity_level):
    bmr = 0
    if gender == "male":
        bmr =  (10 * weigth) + (6.25* heigth) - (5 * age) + 5
    else:
        bmr = (10 * weigth) + (6.25 * heigth) - (5 * age) - 161
    bmr=bmr*float(activity_level)
    return bmr

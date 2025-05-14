def validateInputs(principal, rate, time):
    if not (isinstance(principal, (int, float)) and isinstance(rate, (int, float)) and isinstance(time, int)):
        return "Invalid input types."
    if principal <= 0 or rate <= 0 or time <= 0 or time > 50:
        return "Invalid input types."
    return None

def calculateSimpleInterest(principal, rate, time):
    error = validateInputs(principal, rate, time)
    if error:
        return error
    return round(principal * (1 + (rate / 100) * time), 2)

amount = int(input("How much money have you invested or borrowed? "))
rate = int(input("What is the rate of interest? "))
time = int(input("What is the duration (in years) "))

print(calculateSimpleInterest(amount, rate, time))
def calculate_paye(gross_salary):
    # Simplified PAYE calculation (actual rates may vary)
    if gross_salary <= 24000:
        return gross_salary * 0.1
    elif gross_salary <= 32333:
        return gross_salary * 0.25
    else:
        return gross_salary * 0.3

def calculate_nhif(gross_salary):
    # Simplified NHIF calculation (actual rates may vary)
    if gross_salary <= 5999:
        return 150
    elif gross_salary <= 7999:
        return 300
    elif gross_salary <= 11999:
        return 400
    elif gross_salary <= 14999:
        return 500
    elif gross_salary <= 19999:
        return 600
    elif gross_salary <= 24999:
        return 750
    elif gross_salary <= 29999:
        return 850
    elif gross_salary <= 34999:
        return 900
    elif gross_salary <= 39999:
        return 950
    elif gross_salary <= 44999:
        return 1000
    elif gross_salary <= 49999:
        return 1100
    elif gross_salary <= 59999:
        return 1200
    elif gross_salary <= 69999:
        return 1300
    elif gross_salary <= 79999:
        return 1400
    elif gross_salary <= 89999:
        return 1500
    elif gross_salary <= 99999:
        return 1600
    else:
        return 1700

def calculate_nssf():
    # NSSF deduction (simplified, actual rates may vary)
    return 400

def calculate_net_salary(basic_salary, benefits):
    gross_salary = basic_salary + benefits
    paye = calculate_paye(gross_salary)
    nhif = calculate_nhif(gross_salary)
    nssf = calculate_nssf()
    net_salary = gross_salary - (paye + nhif + nssf)

    return gross_salary, paye, nhif, nssf, net_salary

try:
    basic_salary = float(input("Enter basic salary: "))
    benefits = float(input("Enter benefits: "))

    gross_salary, paye, nhif, nssf, net_salary = calculate_net_salary(basic_salary, benefits)

    print(f"Gross Salary: Ksh {gross_salary:.2f}")
    print(f"PAYE (Tax): Ksh {paye:.2f}")
    print(f"NHIF Deductions: Ksh {nhif:.2f}")
    print(f"NSSF Deductions: Ksh {nssf:.2f}")
    print(f"Net Salary: Ksh {net_salary:.2f}")

except ValueError:
    print("Please enter valid numeric values for salary and benefits.")

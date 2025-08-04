---
Title: Financial Calculators
---

## Description of the code.

The code allows the user to choose which calculation they want to do between **"investment"** or **"bond"**.
The code is not **case-sensitive** which recognises any case as valid entries
The code issues an **appropriate error message** if the user doesn't type in a valid input.
The code requests multiple inputs from the user for each of the calculators. If selected, **Investment** asks the user to input the amount of money they are depositing, the interest rate (as a percentage), the number of years they plan on investing, and whether they want to calculate **simple** or **compound** interest. 

**Interest Formulae** 

**Simple interest:** *A* = *P*(1 + *r* x *t*)
The Python equivalent: A = P * (1 + r*t)

**Compound interest:** *A* = *P*(1 + *r*)^*t*
The Python equivalent: A = P * math.pow((1+r),t)

If selected, **Bond** asks the user to input the present value of the house, the interest rate, and the number of months they plan to take to repay the bond.

**Bond Repayment Formula:** *repayment* = *i* x *P* / 1 - (1+*i*)^-n
The Python equivalent: repayment = (1 * P)/(1-(1 + i)^**(-n))

Each option has to print out an answer based on the input received and respective formula.

## Code Application

This program allows the user to choose between two financial calculators:

**Investment Calculator** – calculates the future value of an investment based on user inputs such as deposit amount, interest rate, investment duration, and interest type (simple or compound).

**Home Loan (Bond) Calculator** – calculates the monthly repayment amount for a home loan based on the loan amount, interest rate, and repayment period.


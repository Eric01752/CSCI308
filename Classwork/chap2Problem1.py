STATE_TAX = .05
COUNTY_TAX = .025

amount = int(input("Enter a purchase amount:"))

amount_state = amount * STATE_TAX
amount_county = amount * COUNTY_TAX
sales_tax = amount_state + amount_county
sale_total = amount + sales_tax

print(f"Amount: {amount}\nState Tax: {STATE_TAX}\nCounty Tax: {COUNTY_TAX}\nSales Tax: {sales_tax}\nTotal: {sale_total}")

billing = 1200 #type int -> numero inteiro
cost = 750.0 # type float -> ponto fluetuante ou numero decimal
new_sales = 100
billing = billing + new_sales
tax = billing * 0.1
profit = billing - cost - tax

profit_margin = profit / billing



print("profit was of ", billing)
print("the cost was of ", cost)
print("profit was of ", profit) 
print("the profit margin was of ", round(profit_margin, 3))

#mod -> %resto da divisao 
print(10 % 3)
contract_time = 170
time_years = 170 /12
print("Time in years", int(time_years))
time_months = 170 % 12
print("time in months", time_months)
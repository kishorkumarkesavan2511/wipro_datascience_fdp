import sys

hosting_charge_per_hour = 0.51

cost_per_day = 0.51 * 24
cost_per_month = cost_per_day * 30
cost_per_week = cost_per_day * 7

print("Hosting charge per hour is : " + str(hosting_charge_per_hour))
print("Hosting charge per day is : " + str(cost_per_day))
print("Hosting charge per week is : " + str(cost_per_week))


operating_cost = int(input("Enter the operating cost , you like to spend in $ : "))

duration_days = operating_cost / cost_per_day

print(str(duration_days) +" days server will operate for amount " + str(operating_cost))


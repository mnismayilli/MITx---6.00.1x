outstanding_balance = float(raw_input("Enter the outstanding balance on your credit card: "))
annual_interest_rate = float(raw_input("Enter the annul credit card interest rate as a decimal: "))
min_monthly_payment_rate = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))

total = []
months = range(1,13)
for month in months:

	min_monthly_payment = outstanding_balance * min_monthly_payment_rate
	principal_paid = min_monthly_payment - outstanding_balance * annual_interest_rate/12
	remaining_balance = outstanding_balance - principal_paid

	print "Month: %d" % month
	print "Minmum mothly payment:", min_monthly_payment
	print "Principle paid:", principal_paid
	print "Remaining balance:", remaining_balance

	outstanding_balance = remaining_balance
	total.append(min_monthly_payment)

print "This is how much you paid a year:", sum(total)
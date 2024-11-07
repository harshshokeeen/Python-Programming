#(Ques7) WAP to calculate net salary of employee, take basic salary of employee and 
#calculate- 
#HRA 30% of basic salary, 
#DA 20% of the basic salary,
#TA 10% of the basic salary and 
#Net salary is sum up of basic salary+ allowances-pf.
#Pf is 1400 fix.

basicsal = float(input("Enter basic salary: "))

hra = basicsal*30/100
da = basicsal*20/100
ta = basicsal*10/100
pf = 1400

netsal = basicsal+(hra+da+ta)-pf

print("Net salary is:", netsal)
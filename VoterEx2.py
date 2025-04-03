while(True):
 age=int(input("Enter the Age Citizen:"))
 if(age in range(18,101)):
  print("\t{} years Age Citizen is Eligible to Vote:".format(age))
  break
else:
  print("\t{} year Age Citizen is not Eligible to Vote-try again:".format(age))
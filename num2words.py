import inflect
p = inflect.engine()
 
#words = p.number_to_words(1234)
# Prints one thousand, two hundred and thirty-four
#print(words)
month = ['january', 'feb', 'March', 'april', 'may', 'june', 'july', 'august', 'sept', 'oct', 'nov', 'dec']
a1,a2,a3=map(int,input("Enter the date seperated by / ").split("/"))
date = p.number_to_words(a1)
month1 = month[a2-1]
year = p.number_to_words(a3)
print(str(date) +" "+ (month1) +" "+ (year))

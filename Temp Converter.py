# DONE - write a function that converts Fahrenheit to Celsius
# DONE - write a function that converts Celsius to Fahrenheit
# DONE - main function  that will allow user to specify which conversion they want
# allows user to input "70 Celsius" or "20 Fahrenheit"
# create a repo and upload this code to git hub

def f_c (temp):

	celsius = (temp - 32) * 5/9
	
	return celsius
    
def c_f (temp):

        fahren = (temp * 9/5) + 32

        return fahren
    
def main():
		
		temp = float(raw_input("What is your current temperature?"))
		c_or_f = (raw_input("What type of temperature  measurement would you like to convert to? Celsius or Fahrenheit? "))
		
		if str(c_or_f == "Celsius" or "celsius"): 
		
			print "The temperature in celsius is %.2f" % f_c(temp)
			
		
		elif str(c_or_f ==  "Fahrenheit" or "fahrenheit"):
		
			print "The temperature in fahrenheit is %.2f" % c_f(temp)
			
		elif str(temp != "Celsius or "celsius" or "Fahrenheit" or "fahrenheit"):
		
			print "Your input is invalid. Please try again. "

main()
import math 
def TinhPi():
	pi = 3
	dau = 1
	e = 3 
	i = 1
	while (e >= math.pow(10, (-6))):
		e = 4 / ( 2 * i * ( 2 * i + 1 ) * ( 2 * i + 2 ))
		pi += dau*e
		dau = - dau
		i += 1
	return pi
  	
def main():
	pi = TinhPi();
	print("Pi la ", pi)

if __name__ == "__main__":
	print ("Bai 111B")
	print ("Ho Kim Thien Nga")
	main()
    

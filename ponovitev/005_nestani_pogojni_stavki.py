starost = int(input("Vnesi starost: "))
dan = int(input("Vnesi dan: "))
denar = int(input("Vnesi denar: "))

if(starost >= 18):
	if(denar > 0):
		if(dan == 6 or dan == 7):
			print("Lahko gre v klub")
		else:
			print("Klub je zaprt")
	else:
		print("Premalo ima denarja")
else:
	print("Ne mora iti ven")

print("Konec")

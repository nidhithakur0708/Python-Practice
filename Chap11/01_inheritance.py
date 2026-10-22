class Employee:
	company="ITC"
	def show(self):
			print(f"The name is {self.name} and the salary is {self.salary}")

##class Programmer():
	##company="ITC infotech"
	##def show(self):
		##print(f"The name is {self.name} and the salary is {self.salary}")
	##def showLanguage(self):
		##print(f"The name is {self.name} and the language is {self.language}")

class Programmer(Employee):
	company="ITC infotech"
	def showLanguage(self):
		print(f"The name is {self.name} and the language is {self.language}")

a=Employee()
b=Programmer()

print(a.company,b.company)
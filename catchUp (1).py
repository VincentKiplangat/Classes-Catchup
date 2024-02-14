# Python: Classes and Objects

# Our example will revolve around soldiers
# Objectives
# - Basics
# - Explanation self
# - Methods and attributes
# - Inheritance and Subclassing
# - Code bases with actual examples

class Soldier:
	# Class Attribute
	platoonMembers = 0
	annualRaisePct = 4 
	# Init method/ Constructors
	def __init__(self, age, education, heightCM, annualPay, weight,
		firstName, lastName):
		# Assigning attributes
		self.age = age 
		self.education = education
		self.heightCM = heightCM
		self.annualPay = annualPay
		self.weight = weight
		self.firstName = firstName
		self.lastName = lastName
		Soldier.platoonMembers += 1

	# Method for calculating BMI
	def calculateBMI(self):
		heightM = self.heightCM/100
		result = self.weight / (heightM * heightM)

		return round(result, 2)

	def increasePay(self):
		self.annualPay  *=   (1 + Soldier.annualRaisePct/100)	

	def printName(self):
		return "{} {}".format(self.firstName, self.lastName)


class Major(Soldier):
		def __init__(self, age, education, heightCM, annualPay, weight, firstName, lastName, unit = None):
			super().__init__(age, education, heightCM, annualPay, weight, firstName, lastName)

			if unit is None:
				self.unit = []
			else:
				self.unit = unit

		def printUnit(self):
			for soldier in self.unit:
				print("-->", soldier.printName())

		def removeSoldier(self, soldier):
			self.unit.remove(soldier)
			

		def addSoldier(self, soldier):
			self.unit.append(soldier)


# Creating objects from the class
sld1 = Soldier(19, "High School", 180, 500000, 80, "Jimmy", "Boy")
sld2 = Soldier(25, "University", 170, 505000, 95, "Susan", "Konney")

reacher = Major(45, "Masters", 210, 800000, 120, "Jack", "Reacher", [sld1, sld2])



# Checking whether reacher is an instance of Major

print(reacher.__dir__())






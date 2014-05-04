class StringCalculator:
	def add(self, str):
		if (str == ""):
			return 0
		else:
			split = str.split(",")
			sum = 0

			for num in split:
				sum += int(num)

			return sum


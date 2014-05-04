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

	def split(self, str, seps):
		res = [str]
		for sep in seps:
			s = res
			res = []
			for seq in s:
				res += seq.split(sep)
		return res


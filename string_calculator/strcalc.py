class StringCalculator:
	def add(self, str):
		if (str == ""):
			return 0
		else:
			sep = self.get_delimiter(str)
			s = self.get_content(str)
			split = self.split(s, sep)

			sum = 0
			for num in split:
				sum += int(num)

			return sum

	def get_delimiter(self, str):
		sep = ","
		if (len(str) > 4 and str[0:2] == "//"):
			sep = str[2]
		return [sep, "\n"]

	def get_content(self, str):
		if (len(str) > 4 and str[0:2] == "//"):
			return str[4:]
		else:
			return str

	def split(self, str, seps):
		res = [str]
		for sep in seps:
			s = res
			res = []
			for seq in s:
				res += seq.split(sep)
		return res


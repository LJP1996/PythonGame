import time as t
#类的方法名和属性名一样，当调用该方法时候，方法名会被属性名覆盖
class Mytime():

	def _init_(self):
		self.unit = ['年','月','天','小时','分钟','秒']
		self.prompt = "未开始计时"
		self.lasted = []
		self.begin = 0
		self.end = 0
	
	def _str_(self):
		return self.prompt
	_repr_ = _str_
	#开始计时
	def start(self):
		self.begin  = t.localtime()
		print("计时开始..")
	#停止计时
	def stop(self):
		self.end  = t.localtime()
		self._calc_()
		print("计时结束..")
		
	#内部方法，计算运行时间
	def _calc_(self):
		self.lasted = []
		self.prompt = "总共运行了"
		for index in range(6):
			self.lasted.append(self.end[index]-self.begin[index])
			if self.lasted[index]:
				self.prompt += str(self.lasted[index])
		print(self.prompt)
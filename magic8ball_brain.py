import random

class Magic8BallResponse:
	def __init__(self):
		self.responses = {
		    'positive': ["It is certain.",
		                 "It is decidedly so.",
		                 "Without a doubt.",
		                 "Yes - definitely.",
		                 "You may rely on it.",
		                 "As I see it, yes.",
		                 "Most likely.",
		                 "Outlook good.",
		                 "Yes.",
		                 "Signs point to yes."],
		    'neutral': ["Reply hazy, try again.",
		                "Ask again later.",
		                "Better not tell you now.",
		                "Cannot predict now.",
		                "Concentrate and ask again."],
		    'negative': ["Don't count on it.",
		                 "My reply is no.",
		                 "My sources say no.",
		                 "Outlook not so good.",
		                 "Very doubtful."]
		}

	def response(self):
		self.num_choice = random.randint(1, 20)
		if self.num_choice <= 10:
			self.answer = random.choice(self.responses['positive'])
		elif 10 < self.num_choice <= 15: 
			self.answer = random.choice(self.responses['neutral'])
		else: 
			self.answer = random.choice(self.responses['negative'])

		return self.answer


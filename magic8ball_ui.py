from tkinter import *
from PIL import ImageTk
from magic8ball_brain import Magic8BallResponse

class Magic8BallInterface:
	def __init__(self):
		self.user_questions = {}
		self.brain = Magic8BallResponse()

		# Creates the window for the application
		self.window = Tk()
		self.window.title("Magic 8 Ball")
		self.window.config(padx=50, pady=50, bg="white")

		# Creates the canvas so you can upload images and text
		self.canvas = Canvas(width=400, height=450, bg="white", highlightthickness=0)
		ball_img = ImageTk.PhotoImage(file="Images/magic-8-ball.png")
		self.ball_up_img = ImageTk.PhotoImage(file="Images/magic-8-ball-up.png")
		self.ball_down_img = ImageTk.PhotoImage(file="Images/magic-8-ball-down.png")
		self.ball_answer = ImageTk.PhotoImage(file="Images/magic-8-ball-tri.png")
		self.canvas_image = self.canvas.create_image(200, 200, image=ball_img)
		self.canvas_text = self.canvas.create_text(200, 400, text="Ask a question", font=("Arial", 30))
		self.canvas.grid(column=1, row=0, columnspan=2)

		# Creates a question box
		self.question_box = Entry(self.window, width=30)
		self.question_box.grid(column=0, row=2, columnspan=2)

		# Create buttons
		self.ask_button = Button(text="Shake 8 Ball", command=self.ask_8ball)
		self.ask_button.grid(column=2, row=2, pady=10)
		self.results_button = Button(text="Previous Questions", command=self.results)
		self.results_button.grid(column=2, row=3)

		self.window.mainloop()

	def response(self):
		self.question = self.question_box.get()
		self.answer = self.brain.response()
		self.canvas.itemconfig(self.canvas_text, text=self.answer)
		self.canvas.itemconfig(self.canvas_image, image=self.ball_answer)
		self.user_questions[self.question] = self.answer
		self.question_box.delete(0, 'end')

	def shake_8ball_image_down(self):
		self.canvas.itemconfig(self.canvas_image, image=self.ball_down_img)

	def ask_8ball(self):
		self.canvas.itemconfig(self.canvas_text, text="")
		self.canvas.itemconfig(self.canvas_image, image=self.ball_up_img)
		self.window.after(1000, func=self.shake_8ball_image_down)
		self.window.after(2000, func=self.response)

	def results(self):
		self.results = Tk()
		self.results.title("Previous questions and answers")
		self.results.config(padx=20, pady=20, bg="white")
		self.results_label = Label(self.results, text="Previous questions and answers", bg="white")
		self.results_label.grid(column=0, row=0)
		self.results_text = Text(self.results)
		self.results_text.grid(column=0, row=1)
		for key, item in self.user_questions.items():
			self.results_text.insert(INSERT, f"You asked: '{key}'. 8 Ball said: '{item}'\n")
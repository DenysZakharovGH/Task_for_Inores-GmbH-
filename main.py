# For test, you could make a program that starts to count from 0 to 1000.
# If you stop the running program by mouse or Touchscreen, we should see on the screen the number where it stoped.
# If you press start again, it should go on until the end. If you press stop and reset, the program should count again from Zero.



from tkinter import *

from threading import Timer,Event


class Custom_Timer():

   def __init__(self,t,hFunction):
        self.t=t
        self.hFunction = hFunction
        self.count = 0
        self.thread = Timer(self.t,self.handle_function)
        self.event = Event() # events of stopping timer


   def handle_function(self):
        if self.count < 1000 and not self.event.is_set(): # if timer isn't stopped
            self.count += 1
        if self.count == 1000: # if it goes to the end - stop it
            self.event.set()

        self.hFunction(self.count)
        self.thread = Timer(self.t,self.handle_function)
        self.thread.start()

   def start(self):
        self.thread.start()

   def cancel(self):
        self.thread.cancel()

   def stop(self):
       self.event.set()

   def _continue(self):
       self.event.clear()


def printer(count):
        lb.configure(text = count)


t = Custom_Timer(0.1,printer)
window = Tk()
window.title("Counter")
window.geometry("400x200")

global stop
stop = False # variable to switch actions on start button (start or continue)

def clicked_bt_start():
    global stop
    if stop == False:
        t.start()
    else:
        t._continue()

def clicked_bt_stop():
    global stop
    stop = True
    t.stop()

def clicked_bt_reset():
    t.count = 0


start_button = Button(text = "start",fg = "black",command = clicked_bt_start)
start_button.place(x=10,y = 0)

stop_button = Button(text = "stop",fg = "black",command = clicked_bt_stop)
stop_button.place(x=170,y = 0)

reset_button = Button(text = "reset",fg = "black",command = clicked_bt_reset)
reset_button.place(x=350,y = 0)

lb = Label(window, text="", font=("Arial Bold", 20))
lb.place(x=170,y=100) # показать поле


window.mainloop()
t.cancel() # cancel our threat

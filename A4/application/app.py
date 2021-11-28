import config
import student_enrollment as se
import addition_courses as ad
import tkinter as tk

class BaseFrame(tk.Frame):
    """An abstract base class for the frames that sit inside PythonGUI.

    Args:
      master (tk.Frame): The parent widget.
      controller (PythonGUI): The controlling Tk object.

    Attributes:
      controller (PythonGUI): The controlling Tk object.

    """

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the frame."""
        raise NotImplementedError


class Student(BaseFrame):
    """The application home page.

    Attributes:
      new_button (tk.Button): The button to switch to HomeFrame.

    """
    def create_widgets(self):
        """Create the base widgets for the frame."""
        lbl = tk.Label(self, text = "Course ID")
        lbl.grid()
        self.txt = tk.Entry(self, width=10)
        self.txt.grid(column =1, row =0)
        lbl1 = tk.Label(self, text = "Roll Number")
        lbl1.grid(column=0, row=1)
        self.txt1 = tk.Entry(self, width=10)
        self.txt1.grid(column =1, row =1)
        self.lbl4 = tk.Label(self, text = "")
        self.lbl4.grid(column=2, row=2)
        self.new_button = tk.Button(self,
                                    anchor=tk.W,
                                    command=self.clicked,
                                    padx=5,
                                    pady=5,
                                    text="Submit")
        self.new_button.grid(padx=5, pady=5, sticky=tk.W+tk.E)
        self.new_button = tk.Button(self,
                                    anchor=tk.W,
                                    command=lambda: self.controller.show_frame(HomeFrame),
                                    padx=5,
                                    pady=5,
                                    text="Home")
        self.new_button.grid(padx=5, pady=5, sticky=tk.W+tk.E)
    def clicked(self):
      outs = se.student_enroll(self.txt1.get(), self.txt.get(), config.cnx)
      self.txt.delete(0, 'end')
      self.txt1.delete(0, 'end')
      self.lbl4.config(text = outs)
      config.cnx.commit()

class Course(BaseFrame):
    """The application home page.

    Attributes:
      new_button (tk.Button): The button to switch to HomeFrame.

    """

    def create_widgets(self):
        """Create the base widgets for the frame."""
        lbl = tk.Label(self, text = "Course ID")
        lbl.grid()
        self.txt = tk.Entry(self, width=10)
        self.txt.grid(column =1, row =0)
        lbl1 = tk.Label(self, text = "Teacher ID")
        lbl1.grid(column=0, row=1)
        self.txt1 = tk.Entry(self, width=10)
        self.txt1.grid(column =1, row =1)
        lbl2 = tk.Label(self, text = "Department ID")
        lbl2.grid(column=0, row=2)
        self.txt2 = tk.Entry(self, width=10)
        self.txt2.grid(column =1, row =2)
        lbl3 = tk.Label(self, text = "Classroom")
        lbl3.grid(column=0, row=3)
        self.txt3 = tk.Entry(self, width=10)
        self.txt3.grid(column =1, row =3)
        self.lbl4 = tk.Label(self, text = "")
        self.lbl4.grid(column=2, row=4)
        self.new_button = tk.Button(self,
                                    anchor=tk.W,
                                    command=self.clicked,
                                    padx=5,
                                    pady=5,
                                    text="Submit")
        self.new_button.grid(padx=5, pady=5, sticky=tk.W+tk.E)
        self.new_button = tk.Button(self,
                                    anchor=tk.W,
                                    command=lambda: self.controller.show_frame(HomeFrame),
                                    padx=5,
                                    pady=5,
                                    text="Home")
        self.new_button.grid(padx=5, pady=5, sticky=tk.W+tk.E)
    def clicked(self):
      inp = (self.txt.get(), self.txt1.get(), self.txt2.get(), self.txt3.get())
      self.txt.delete(0, 'end')
      self.txt1.delete(0, 'end')
      self.txt2.delete(0, 'end')
      self.txt3.delete(0, 'end')
      outs = ad.add_course(inp, config.cnx)
      self.lbl4.config(text = outs)
      config.cnx.commit()

class HomeFrame(BaseFrame):
    """The application home page.

    Attributes:
      new_button (tk.Button): The button to switch to ExecuteFrame.

    """
    def create_widgets(self):
        """Create the base widgets for the frame."""
        self.new_button = tk.Button(self,
                                    anchor=tk.W,
                                    command=lambda: self.controller.show_frame(Student),
                                    padx=5,
                                    pady=5,
                                    text="Enroll Student")
        self.new_button.grid(padx=5, pady=5, sticky=tk.W+tk.E)
        self.new_button = tk.Button(self,
                                    anchor=tk.W,
                                    command=lambda: self.controller.show_frame(Course),
                                    padx=5,
                                    pady=5,
                                    text="Add Course")
        self.new_button.grid(padx=5, pady=5, sticky=tk.W+tk.E)


class PythonGUI(tk.Tk):
    """The main window of the GUI.

    Attributes:
      container (tk.Frame): The frame container for the sub-frames.
      frames (dict of tk.Frame): The available sub-frames.

    """

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Academic Database")
        self.geometry("500x500")
        self.create_widgets()
        self.resizable(1, 1)

    def create_widgets(self):
        """Create the widgets for the frame."""             
        #   Frame Container
        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky=tk.W+tk.E)

        #   Frames
        self.frames = {}
        for f in (HomeFrame, Student, Course): # defined subclasses of BaseFrame
            frame = f(self.container, self)
            frame.grid(row=2, column=2, sticky=tk.NW+tk.SE)
            self.frames[f] = frame
        self.show_frame(HomeFrame)

    def show_frame(self, cls):
        """Show the specified frame.

        Args:
          cls (tk.Frame): The class of the frame to show. 

        """
        self.frames[cls].tkraise()

if __name__ == "__main__":
    config.init()
    app = PythonGUI()
    app.mainloop()
    exit()
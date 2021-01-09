from tkinter import *


class TemperatureConverterGUI(Tk):
        __list1 = ["celcius", "fahrenheight", "kelvin"]
         
        def __init__(self):
                super().__init__()
                self.geometry('600x256')
                self.title('Temperature Converter')

        def frame1(self):
                self.frame1 = Frame(self)
                self.frame1.grid(row=0, column=0)
                self.frame1.pack()

        def list_menu1(self):
                self.variable1 = StringVar(self.frame1)
                self.variable1.set(self.__list1[0])
                list_menu1 = OptionMenu(self.frame1, self.variable1, *self.__list1)
                list_menu1.grid(row=0,column=0,columnspan=2, sticky=NSEW,padx=15,pady=20)

        def list_menu2(self):
                self.variable2 = StringVar(self.frame1)
                self.variable2.set(self.__list1[1])
                list_menu2 = OptionMenu(self.frame1, self.variable2, *self.__list1)
                list_menu2.grid(row=0, column=5, columnspan=2, sticky=NSEW, padx=15, pady=20)

        def convert_button(self):
                convert_button = Button(self.frame1, text="\N{BLACK RIGHTWARDS ARROW} \nconvert", relief=RAISED, width=8, height=3, fg="green",
                command = conv.conversion)
                convert_button.grid(row=0, column=3, padx=10, pady=10)

        def input_entry(self):
                self.input_entry1 = Entry(self.frame1, width=30, bg="white", fg="black")
                self.input_entry1.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=15, pady=20)

        def change_output_text_color(self, color):
                self.output_entry1.config(fg=color)

        def get_input(self):
                try:
                        text = self.input_entry1.get()
                        inputt = float(text)
                        return inputt
                except:
                        return False

        def get_var1(self):
                return self.variable1.get()

        def get_var2(self):
                return self.variable2.get()

        def output_entry(self):
                self.output_entry1 = Entry(self.frame1, width=30)
                self.output_entry1.grid(row=1, column=5, columnspan=2, sticky=NSEW, padx=15, pady=20)

        def update(self, result):
                self.output_entry1.delete(0, END)
                self.output_entry1.insert(0, result)

        def get_list(self):
                return self.__list1


class Convert():

        def ctof(self, temp):
                result = (temp*9/5) + 32
                return result

        def ctok(self, temp):
                result = temp + 273.15
                return result

        def ftoc(self, temp):
                result = (temp-32) * 5/9
                return result

        def ftok(self, temp):
                result = (temp-32) * 5/9 + 273.15
                return result

        def ktoc(self, temp):
                result = temp - 273.15
                return result

        def ktof(self, temp):
                result = (temp-273.15) * (9/5) + 32
                return result

        def conversion(self):
                try:
                        if window.get_input():
                                list1 = window.get_list()
                                var1 = window.get_var1()
                                var2 = window.get_var2()
                                temp = window.get_input()
                                window.change_output_text_color('black')
                                if var1 == list1[0] and var2 == list1[1]:
                                        window.update(self.ctof(temp))
                                elif var1 == list1[0] and var2 == list1[2]:
                                        window.update(self.ctok(temp))
                                elif var1 == list1[1] and var2 == list1[0]:
                                        window.update(self.ftoc(temp))
                                elif var1 == list1[1] and var2 == list1[2]:
                                        window.update(self.ftok(temp))
                                elif var1 == list1[2] and var2 == list1[0]:
                                        window.update(self.ktoc(temp))
                                elif var1 == list1[2] and var2 == list1[1]:
                                        window.update(self.ktof(temp))
                                elif var1 == var2:
                                        window.update(temp)
                                # window.update(window.get_list())
                        else:
                                window.update('Enter a valid value')
                                window.change_output_text_color('red')
                except:
                        window.update('invalid input')


if __name__ == '__main__':
    window = TemperatureConverterGUI()
    window.frame1()
    conv = Convert()
    window.list_menu1()
    window.list_menu2()
    window.input_entry()
    window.output_entry()
    window.convert_button()
    window.mainloop()

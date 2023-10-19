from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout



from kivy.config import Config
Config.set("graphics", 'resizable', 0)
Config.set("graphics", 'width', 400)
Config.set("graphics", 'height', 500)


class CalculatorApp(App):

    def update_label(self):
        self.lbl.text = self.form

    def add_number(self, instance):
        if self.form == '0':
            self.form = ''
        self.form += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        self.form += str(instance.text)
        self.update_label()

    def add_dot(self, instance):
        if self.lbl.text[-1] != '.':
            self.form += str(instance.text)
            self.update_label()

    def ac(self, instance):
        self.form = '0'
        self.update_label()

    def system_res(self, instance):
        self.update_label()

        if self.lbl.text[-1] != '+' and self.lbl.text[-1] != '*'\
                and self.lbl.text[-1] != '-' and self.lbl.text[-1] != '/' and self.lbl.text.find(".") < 1:

            if instance.text == 'bin':
                self.lbl.text = str(bin(eval(self.lbl.text))[2:])
                self.form = '0'

            elif instance.text == 'oct':
                self.lbl.text = str(oct(eval(self.lbl.text))[2:])
                self.form = '0'

            elif instance.text == 'hex':
                self.lbl.text = str(hex(eval(self.lbl.text))[2:])
                self.form = '0'

    def calculate(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.form = '0'

    def build(self):
        self.form = "0"
        bl = BoxLayout(orientation = "vertical", padding = 25)
        gl = GridLayout(cols = 4, spacing = 3, size_hint = (1, .6))

        self.lbl = Label(text = "0", font_size = 60, halign = 'right', valign = 'center', size_hint = (1, .4), text_size = (400, 500))
        bl.add_widget( self.lbl )

        gl.add_widget(Button(text = 'bin', background_color = (180/255,180/255,180/255), on_press = self.system_res))
        gl.add_widget(Button(text='oct', background_color = (180/255,180/255,180/255), on_press = self.system_res))
        gl.add_widget(Button(text='hex', background_color = (180/255,180/255,180/255), on_press = self.system_res))
        gl.add_widget(Button(text='/', background_color = (180/255,180/255,180/255), on_press = self.add_operation))

        gl.add_widget(Button(text='7', on_press = self.add_number))
        gl.add_widget(Button(text='8', on_press = self.add_number))
        gl.add_widget(Button(text='9', on_press = self.add_number))
        gl.add_widget(Button(text='*', background_color = (180/255,180/255,180/255), on_press = self.add_operation))

        gl.add_widget(Button(text='4', on_press = self.add_number))
        gl.add_widget(Button(text='5', on_press = self.add_number))
        gl.add_widget(Button(text='6', on_press = self.add_number))
        gl.add_widget(Button(text='+', background_color = (180/255,180/255,180/255), on_press = self.add_operation))

        gl.add_widget(Button(text='1', on_press = self.add_number))
        gl.add_widget(Button(text='2', on_press = self.add_number))
        gl.add_widget(Button(text='3', on_press = self.add_number))
        gl.add_widget(Button(text='-', background_color = (180/255,180/255,180/255), on_press = self.add_operation))

        gl.add_widget(Button(text='AC', on_press = self.ac))
        gl.add_widget(Button(text='0', on_press = self.add_number))
        gl.add_widget(Button(text='.', on_press = self.add_dot))
        gl.add_widget(Button(text='=', background_color = (180/255,180/255,180/255), on_press = self.calculate))

        bl.add_widget(gl)
        return bl


if __name__ == "__main__":
    CalculatorApp().run()

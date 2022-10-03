from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton, MDRoundFlatButton, MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
Theme = 'Light'
LmodeIco = 'brightness-5'
DmodeIco = 'brightness-2'
modeIco = DmodeIco
class quadFunk(MDApp):

    def modeFunc(self):
        # self.theme_cls.primary_palette = (
        #     "Orange" if self.theme_cls.primary_palette == "Orange" else "Orange"
            
        # )
        # self.theme_cls.theme_style = (
        #     "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        # )
        global LmodeIco,DmodeIco, modeIco, Theme
        if Theme == 'Dark':
            Theme = 'Light'
            modeIco = DmodeIco
            self.toolbar.right_action_items = [[modeIco, lambda x: self.modeFunc()]]
            self.theme_cls.theme_style = Theme
        else:
            Theme = 'Dark'
            modeIco = LmodeIco
            self.toolbar.right_action_items = [[modeIco, lambda x: self.modeFunc()]]
            self.theme_cls.theme_style = Theme

    def aNumber(self):
        if (len([*self.aVal.text])) >=1:
            numb = self.aVal.text
            # print(numb)
            if (len([*self.aVal.text])) > 1:
                if ([*numb])[1].isdigit() and ([*numb])[1] != 0:
                    self.aVal.error = False
                    a = float(self.aVal.text)
                    return a
                else:
                    self.aVal.error = True
            elif (len([*self.aVal.text])) == 1:
                if ([*numb])[0].isdigit() and ([*numb])[0] != 0:
                    self.aVal.error = False
                    a = float(self.aVal.text)
                    return a
                else:
                    self.aVal.error = True

    def bNumber(self):
        if (len([*self.bVal.text])) >=1:
            numb = self.bVal.text
            if (len([*self.bVal.text])) > 1:
                if ([*numb])[1].isdigit():
                    self.bVal.error = False
                    b = float(self.bVal.text)
                    return b
                else:
                    self.bVal.error = True
            elif (len([*self.bVal.text])) == 1:
                if ([*numb])[0].isdigit():
                    self.bVal.error = False
                    b = float(self.bVal.text)
                    return b
                else:
                    self.bVal.error = True

    def cNumber(self):
        if (len([*self.cVal.text])) >=1:
            numb = self.cVal.text
            if (len([*self.cVal.text])) > 1:
                if ([*numb])[1].isdigit():
                    self.cVal.error = False
                    c = float(self.cVal.text)
                    return c
                else:
                    self.cVal.error = True
            elif (len([*self.cVal.text])) == 1:
                if ([*numb])[0].isdigit():
                    self.cVal.error = False
                    c = float(self.cVal.text)
                    return c
                else:
                    self.cVal.error = True
                

    def calc(self,args):
        global a,b,c
        a='null'
        b='null'
        c='null'

        if self.aVal.text != '':
            a = self.aNumber()
            # print(a)
        if self.bVal.text != '':
            b = self.bNumber()
            # print(b)
        if self.cVal.text != '':
            c = self.cNumber()
            # print(c)

        if a==0:
            self.aVal.error = True
        else:
            if a!='null' and b!='null' and c!='null' and a!=None and b!=None and c!=None:
                X = -b/(2*a)
                if (X).is_integer():
                    X = int(X)
                else:
                    X = float(X)
                Y = (a*(X**2)+(b*X)+c)
                # print('X ir',X)
                # print('Y ir',Y)
                self.answer.text = 'X = '+str(X)+'\nY = '+str(Y)
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.1
        screen = MDScreen()
        self.toolbar = MDTopAppBar()
        self.toolbar.pos_hint = {'top':1}   
        self.toolbar.right_action_items = [[modeIco, lambda x: self.modeFunc()]]
        screen.add_widget(self.toolbar)

        screen.add_widget(Image(source='logou.png',pos_hint={'center_y':.75,'center_x':.5},size_hint=(.4,.4)))

        self.aVal = MDTextField(
            multiline = False,
            max_text_length=5,
            hint_text='Enter "a" value',
            halign="center",
            size_hint=(.6,1),
            pos_hint={'center_y':.5,'center_x':.5},
            font_size = 22,
            helper_text =  '"a" cannot be 0!',
            helper_text_mode =  "on_error"
        )

        self.bVal = MDTextField(
            multiline = False,
            max_text_length=5,
            hint_text='Enter "b" value',
            halign="center",
            size_hint=(.6,1),
            pos_hint={'center_y':.4,'center_x':.5},
            font_size = 22,
            helper_text =  '"b" cannot be string!',
            helper_text_mode =  "on_error"
        )
        self.cVal = MDTextField(
            multiline = False,
            max_text_length=5,
            hint_text='Enter "c" value',
            halign="center",
            size_hint=(.6,1),
            pos_hint={'center_y':.3,'center_x':.5},
            font_size = 22,
            helper_text =  '"c" cannot be string!',
            helper_text_mode =  "on_error"
        )
        screen.add_widget(self.aVal)
        screen.add_widget(self.bVal)
        screen.add_widget(self.cVal)


        self.formula = MDLabel(
            text = 'y=ax²+bx+c',
            halign="center",
            pos_hint={'center_y':.6,'center_x':.5},
            theme_text_color = 'Secondary',
            font_style = 'H5'
        )

        self.result = MDLabel(
            text = 'Result',
            halign="center",
            pos_hint={'center_y':.2,'center_x':.5},
            theme_text_color = 'Secondary'
        )

        self.answer = MDLabel(
            text = '',
            halign="center",
            pos_hint={'center_y':.1,'center_x':.5},
            theme_text_color = 'Primary',
            font_style = 'H5'
        )

        screen.add_widget(MDRectangleFlatButton(
            text = 'CALCULATE',
            font_size = 17,
            pos_hint={'center_y':.10,'center_x':.85},
            on_press = self.calc
            
        ))

        screen.add_widget(self.formula)
        screen.add_widget(self.result)
        screen.add_widget(self.answer)
        return screen
    def set_error_message(self):
        self.aVal.error = True
        


if __name__ == '__main__':
    quadFunk().run()
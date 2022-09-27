from kivy.lang import Builder

from kivymd.app import MDApp


class Test(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"

        return Builder.load_string(
            '''
MDScreen:

    MDBottomNavigation:
        panel_color: 1, 1, 1, 0

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Mail'
            icon: 'calculator-variant'
            

            MDLabel:
                text: 'Mail'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Twitter'
            icon: 'home'
           

            MDLabel:
                text: 'Twitter'
                halign: 'center'


        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'LinkedIN'
            icon: '/PicniGo_1.4/Иконки/45200.png'
            MDLabel



'''
        )


Test().run()
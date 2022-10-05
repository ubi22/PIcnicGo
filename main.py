
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.metrics import dp
from kivymd.uix.tab import MDTabsBase
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivy.properties import StringProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.card import MDCardSwipe
import datetime
from kivymd.uix.screen import MDScreen
from kivymd.uix.chip import MDChip
from kivy.animation import Animation
from kivy.factory import Factory
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.button import MDFlatButton
import webbrowser
from kivymd.uix.button import MDRaisedButton
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.fitimage import FitImage
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.core.window import Window
from kivy.core.window import Window

Window.size = (480,800)










class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class sDrawer(BoxLayout):
    pass



class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color
class IconListItem(OneLineIconListItem):
    icon = StringProperty()

class Tab(MDFloatLayout, MDTabsBase):
    pass

class PicnicGo(MDApp):
    pomi=""
    screen_manager = ObjectProperty()  # IMPORTANT!
    dialog = None
    dialogf = None
    dialogg = None
    dim = None
    dialogk = None
    kyda = int(0)
    sezon = int(0)
    g = int(0)
    fyx = int(0)

    def on_buil(self):
        tab = self.root.ids.rez
        tab.disebled = True

    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''

        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''

        print(instance_table, current_row)

    # Sorting Methods:
    # since the https://github.com/kivymd/KivyMD/pull/914 request, the
    # sorting method requires you to sort out the indexes of each data value
    # for the support of selections.
    #
    # The most common method to do this is with the use of the builtin function
    # zip and enumerate, see the example below for more info.
    #
    # The result given by these funcitons must be a list in the format of
    # [Indexes, Sorted_Row_Data]

    def plus(self):
        self.root.ids.tabs.switch_tab(self.root.ids.tabs.get_tab_list()[2])
    def sort_on_signal(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][2]))



    def vivod(self, *args):
        f = self.root.ids.ftt.text
        a = self.root.ids.coli.text
        if self.g == 1:
            if a == "":
                print("0")
            elif a == "0":
                print("0")
            else:
                if f == "":
                    print("0")
                elif f == "0":
                    print("0")
                else:
                    self.root.ids.tabs.switch_tab(self.root.ids.tabs.get_tab_list()[1])
                    f = float(self.root.ids.ftt.text)
                    a = float(self.root.ids.coli.text)
                    miso = .300 * a * f
                    ogyrzi = .55 * a * f
                    pomidor = .100 * a * f
                    zelen = .100 * a * f
                    luk = .50 * a * f
                    mychoe = .129 * a * f
                    sous = .1 * a * f
                    makaron = .70 * a * f
                    kartofel = .200 * a * f
                    self.root.ids.vivod.secondary_text = f"{miso}кг"
                    self.root.ids.mac.secondary_text = f"{makaron}кг"
                    self.root.ids.pomi.secondary_text = f"{pomidor}кг"
                    self.root.ids.sos.secondary_text = f"{sous}кг"
                    self.root.ids.luc.secondary_text = f"{luk}кг"
                    self.root.ids.zel.secondary_text = f"{zelen}кг"
                    self.root.ids.kar.secondary_text = f"{kartofel}кг"
                    self.root.ids.myc.secondary_text = f"{mychoe}кг"
                    self.root.ids.ogyr.secondary_text = f"{ogyrzi}кг"
        else:
            if a == "":
                print("0")
            elif a == "0":
                print("0")
            else:
                if f == "":
                    print("0")
                elif f == "0":
                    print("0")
                else:
                    self.root.ids.tabs.switch_tab(self.root.ids.tabs.get_tab_list()[1])
                    self.root.ids.vivod.secondary_text = ""
                    self.root.ids.scc.source = "/PicnicGo_версия 1.3/Иконки/главный.jpg"
                    self.root.ids.vivod.tertiary_text = ""
                    self.root.ids.vivod.text = ""
                    f = float(self.root.ids.ftt.text)
                    a = float(self.root.ids.coli.text)
                    ogyrzi = .55 * a * f
                    pomidor = .100 * a * f
                    zelen = .100 * a * f
                    luk = .50 * a * f
                    mychoe = .129 * a * f
                    sous = .1 * a * f
                    makaron = .70 * a * f
                    kartofel = .200 * a * f
                    self.root.ids.mac.secondary_text = f"{makaron}кг"
                    self.root.ids.pomi.secondary_text = f"{pomidor}кг"
                    self.root.ids.sos.secondary_text = f"{sous}кг"
                    self.root.ids.luc.secondary_text = f"{luk}кг"
                    self.root.ids.zel.secondary_text = f"{zelen}кг"
                    self.root.ids.kar.secondary_text = f"{kartofel}кг"
                    self.root.ids.myc.secondary_text = f"{mychoe}кг"
                    self.root.ids.ogyr.secondary_text = f"{ogyrzi}кг"

    def dialogfgr(self, *args):
        self.dialogf.dismiss(force=True)
        toast("Куда едите? На равнину")
        self.kyda = 2
        self.root.ids.i.text = "На равнину"
    def dialogfgb(self, *args):
        self.dialogf.dismiss(force=True)
        self.kyda = 3
        toast("Куда едите? На берег")
        self.root.ids.i.text = "На берег"
    def dialogfgl(self, *args):
        self.dialogf.dismiss(force=True)
        self.kyda = 4
        toast("Куда едите? В лес")
        self.root.ids.i.text = "В лес"


    def dialogggv(self, *args):
        self.dialogg.dismiss(force=True)
        self.sezon = 1
        toast("В какой сезон? Весна")
        self.root.ids.u.text = "Весна"
    def dialogggl(self, *args):
        self.dialogg.dismiss(force=True)
        self.sezon = 2
        toast("В какой сезон? Лето")
        self.root.ids.u.text = "Лето"
    def dialogggo(self, *args):
        self.dialogg.dismiss(force=True)
        self.sezon = 3
        toast("В какой сезон? Осень")
        self.root.ids.u.text = "Осень"
    def dialogggz(self, *args):
        self.dialogg.dismiss(force=True)
        self.sezon = 4
        toast("В какой сезон? Зима")
        self.root.ids.u.text = "Зима"



    def dialoy(self, *args):
        self.dialog.dismiss(force=True)
        toast("Вы вегетарианиц? Да")
        self.root.ids.vega.text = "Да"
        self.g = 2

    def dialon(self, *args):
        self.dialog.dismiss(force=True)
        toast("Вы вегетарианиц? Нет")
        self.root.ids.vega.text = "Нет"
        self.g = 1


    def calc(self):
        self.root.screen_manager.current = "scr 3"
    def clear(self):
        self.root.ids.calc_input.text = "0"

    def button_press(self, button):
        prior = self.root.ids.calc_input.text
        if "Error" in prior:
            prior = ""
        if prior == "0":
             self.root.ids.calc_input.text = ""
             self.root.ids.calc_input.text = f"{button}"
        else:
            self.root.ids.calc_input.text = f"{prior}{button}"
    def remove(self):
        prior = self.root.ids.calc_input.text
        prior = prior[:-1]
        self.root.ids.calc_input.text = prior
    def add(self):
        prior = self.root.ids.calc_input.text
        self.root.ids.calc_input.text = f"{prior}+"
    def subtract (self):
        prior = self.root.ids.calc_input.text
        self.root.ids.calc_input.text = f"{prior}-"
    def divide (self):
        prior = self.root.ids.calc_input.text
        self.root.ids.calc_input.text = f"{prior}/"
    def multiply (self):
        prior = self.root.ids.calc_input.text
        self.root.ids.calc_input.text = f"{prior}*"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )


    def file_manager_open(self):
        self.file_manager.show('/PicnicGo_версия 1.4/Иконки/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        self.pomi = path
        print(path)
        self.exit_manager()

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True
    def equals(self):
        prior = self.root.ids.calc_input.text
        try:
            answer = eval(prior)
            self.root.ids.calc_input.text = str(answer)
        except:
            self.root.ids.calc_input.text = "Error"
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            for number in num_list:
                answer = int(answer) + int(number)

            self.root.ids.calc_input.text = str(answer)

    def cuala(self):
        self.root.screen_manager.current = "scr 1"

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Вы вегетарианец?",
                buttons=[
                    MDFlatButton(
                        text="Нет",
                        on_release=self.dialon,
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="Да",
                        on_release=self.dialoy,
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),

                ],
            )
        self.dialog.open()
    def show_alerh_dialog(self):
        if not self.dialogk:
            self.dialogk = MDDialog(
                text="Куда добалять в",
                buttons=[
                    MDFlatButton(
                        text="Инстументы",
                        on_release=self.dialonf,
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="Подукты",
                        on_release=self.dialoyf,
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),

                ],
            )
        self.dialogk.open()
    def show_aler_dialog(self):
        if not self.dialogf:
            self.dialogf = MDDialog(
                text="Куда поедете?",
                buttons=[
                    MDFlatButton(
                        text="На равнину",
                        theme_text_color="Custom",
                        on_release=self.dialogfgr,
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="На берег",
                        theme_text_color="Custom",
                        on_release=self.dialogfgb,
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="В лес",
                        theme_text_color="Custom",
                        on_release=self.dialogfgl,
                        text_color=self.theme_cls.primary_color,
                    ),

                ],
            )
        self.dialogf.open()
    def show_alerr_dialog(self):
        if not self.dialogg:
            self.dialogg = MDDialog(
                text="В какой сезон?",
                buttons=[
                    MDFlatButton(
                        text="Зима",
                        theme_text_color="Custom",
                        on_release=self.dialogggz,
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="Весна",
                        theme_text_color="Custom",
                        on_release=self.dialogggv,
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="Лето",
                        theme_text_color="Custom",
                        on_release=self.dialogggl,
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="Осень",
                        theme_text_color="Custom",
                        on_release=self.dialogggo,
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialogg.open()
    def on_release_chip(self, instance_check):
        print(instance_check)

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''

        print(instance, value, date_range)

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
    icon = "/PicnicGo_версия 1.4/Иконки/главный.png"
    content = sDrawer()

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.screen = Builder.load_file("dfrty.kv")
    #     menu_items = [{"icon": "exit","text": "po",
    #                     "icon": "exit","text": "po",}]
    #     self.menu = MDDropdownMenu(
    #         cal=self.screen.ids.payment_type,
    #         items=menu_items,
    #         position="auto",
    #         width_mult=4,
    #     )
    #     self.menu.bind(on_release=self.set_item)
    #
    # def set_item(self, instance_menu, instance_menu_item):
    #     def set_item(interva):
    #         self.screen.ids.payment_type.text = instance_menu_item.text
    #         self.menu.dismiss()
    #         Clock.schedule_once(set_item, 0.5)
    def build(self):
        return Builder.load_file("dfrty.kv")
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        # return self.screen
    def createButton(self):
        conten = sDrawer()
        a = self.root.ids.fer.text
        f = self.root.ids.hy.text
        d = self.root.ids.ger.text
        if self.fyx == 0:
            conten.add_widget(FitImage(source=self.pomi,size_hint={0.25, 0.85}))
            conten.add_widget(ThreeLineListItem(text=f'{f}',secondary_text=f"{a} {d}"))
            self.root.ids.md_list.add_widget(conten)


    def on_fg(instance):
        webbrowser.open("https://vk.com/zv_k_team")
    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        print("tab clicked!" +tab_text)
    def on_star_click(self):
        pass

PicnicGo().run()
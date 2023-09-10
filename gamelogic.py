from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.metrics import dp, cm
from kivy.core.window import Window, WindowBase
from kivy.event import EventDispatcher
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import phase2_level
import random

import time
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
import winingfile
from kivy.animation import Animation
from kivy.storage.jsonstore import JsonStore
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, CardTransition, RiseInTransition
from kivy.uix.textinput import TextInput
import levels_game
import hint_logic
import coin_logic
import retrewingdata
import levels_game2
import coin_moving
import allhint
import phase3_level
import phase4_level
import coinmovement

build = Builder.load_file("screenappp.kv")
build = Builder.load_file("gamewindow.kv")
build = Builder.load_file("phase3_game.kv")
build = Builder.load_file("phase_4.kv")


class sounds():
    sound = SoundLoader.load("")

class ValidFilenameInput(TextInput):
    invalid_set = r"/\*:|'.?" + '"<>'

    max_length = 10

    def insert_text(self, substring, from_undo=True):
        self.size_hint = None, None
        self.background_normal = ""
        self.hint_text = "Example1234"
        self.halign = "center"
        self.foreground_color = "blue"

        self.height = dp(30)
        self.width = dp(200)
        self.multiline = False
        self.pos_hint = {"center_x": .5, "center_y": .5}

        if len(self.text) <= self.max_length:
            patch_name = [c for c in substring if c not in self.invalid_set]
            s = ''.join(patch_name)
            return super().insert_text(s, from_undo=from_undo)


obj = ValidFilenameInput()


class home(Screen,sounds,allhint.hint_all):
    def __init__(self, **kwargs):
        super(home, self).__init__(**kwargs)


        # print("working....")
        self.js = JsonStore("iq_score.json")
        self.ids.iqlogic.text = str(self.js.get("iq_score")["score"])




        self.save = Button()


        self.validjs = JsonStore("gamedata.json")
        self.deafultname = (self.validjs.get("game")["username"])
        if self.deafultname == "*******":
            Clock.schedule_once(self.username_popup)

        else:
            print("username already taken")

            self.ids.player_name.text = self.validjs.get("game")["username"]


    def on_touch_move(self, touch):
        if touch.ox - touch.x > 50 :
            print(touch.x,touch.ox)
            # screenapp.get_running_app().change_screen()

    def button(self,*args):
        print("ntg")

    def username_popup(self, *args):

        self.user_pop = Popup()
        self.user_pop.title = "Player Name"
        self.user_pop.title_color = 209 / 255, 27 / 255, 96 / 255
        self.user_pop.title_size = "20sp"
        self.user_pop.title_align = "center"
        self.user_pop.size_hint = .8, .3
        self.user_pop.separator_height = dp(0)
        self.user_pop.background_color = "yellow"
        self.user_pop.pos_hint = {"center_x": .5, "center_y": .5}
        self.l1 = BoxLayout()
        self.l1.orientation = "vertical"
        self.l1.spacing = dp(40)
        self.l1.padding = dp(10)

        self.save.text = "Save"
        self.save.background_normal = ""
        self.save.background_color = 1, .1, .1, 1
        self.save.font_size = "15sp"
        self.save.size_hint = None, None
        self.save.height = dp(25)
        self.save.width = dp(60)
        self.save.disabled = False
        self.save.pos_hint = {"center_x": .5, "center_y": .5}
        self.save.bind(on_press=self.saving_name)

        self.l1.add_widget(obj)
        self.l1.add_widget(self.save)
        self.user_pop.add_widget(self.l1)

        self.user_pop.auto_dismiss = False
        self.user_pop.open()

    def saving_name(self, *args):

        if len(obj.text) >= 1:

            self.js = JsonStore("gamedata.json")
            self.js.put("game", username=obj.text)
            self.username = self.js.get("game")["username"]
            self.ids.player_name.text = self.username



            self.user_pop.dismiss()


        else:
            self.user_pop.open()

    def auto_update_username(self):
        return self.username


class level(Screen):
    def __init__(self,**kwargs):
        super(level, self).__init__(**kwargs)
        pass
    def commingsoon(self,*args):
        self.ids.dcimg.source = "comingsoon.png"

    def pop(self,*args):
        self.ids.dcimg.source = "dc.png"
        time.sleep(.5)





class marvel(Screen):
    def __init__(self,**kwargs):
        super(marvel, self).__init__(**kwargs)
        pass
    def fr(self,*args):
        pass

class dc(Screen):
    pass


class level1(Screen, levels_game.level_game_comic, coin_logic.coin_logic_18, retrewingdata.retrew_data_json,
             winingfile.winninggame,coinmovement.movement,hint_logic.logic,allhint.hint_all):

    def __init__(self, **kwargs):
        super(level1, self).__init__(**kwargs)

        self.coin_js = JsonStore("coins_win.json")
        self.iqjs = JsonStore("iq_score.json")

        retrewingdata.retrew_data_json.__init__(self, filename="levels.json")
        retrewingdata.retrew_data_json.getting_items(self)
        self.hint_count = 0
        self.ids.coins.text = str(self.coin_js.get("coin_base")["coins"])
        self.ids.iq.text = str(self.iqjs.get("iq_score")["score"])



    # change everything to 18 comminications

    def levels_random(self):
        js = JsonStore("randomliststorage.json")
        l = js.get("random_level_list")["levels"]
        if l != []:
            ran = random.choice(l)

            print(ran)
            l.remove(ran)

            js.put("random_level_list", levels=l)

            return ran

        else:
            return 99


    def level1_hint(self):

            self.hint = Popup()
            self.hint.title = "Hint"
            self.hint.title_align = "center"
            self.hint.size_hint = .9,.2


            self.hint.separator_height = dp(0)
            self.hint.background_color = (100 / 255, 100 / 255, 100 / 255)
            self.layout = BoxLayout()
            self.layout.size_hint = 1,1
            self.button_coin = Button()
            self.button_free = Button()


            self.button_coin.text = "5 Coins"
            self.button_coin.bind(on_press = self.hint_coin)
            self.button_coin.size_hint = 1,.6
            self.button_coin.padding_x = .2
            self.button_coin.pos_hint = {"center_x":.1,"center_y":.55}
            self.button_coin.background_color = "red"
            self.layout.add_widget(self.button_coin)
            self.button_free.text = "Free Hint"
            self.button_free.size_hint = 1,.6
            self.button_free.padding_x = .2
            self.button_free.pos_hint = {"center_x": .1, "center_y": .55}
            self.button_free.background_color = "red"
            self.layout.add_widget(self.button_free)
            self.hint.add_widget(self.layout)
            print(self.count)
            self.hint.open()




    def hint_coin(self,*args):
        self.hint_count += 1
        print(self.hint_count)
        self.h = Popup()
        self.h.title = ""
        self.h.separator_height = dp(0)
        self.h.size_hint = .8, .2
        self.h.title = "Here is your Hint"
        self.h.title_align = "center"
        self.h.background_color = "green"
        self.lab= Label(text = "",pos_hint= {"center_x":5,"center_y":.7},bold = True)
        self.h.content = self.lab
        allhint.hint_all.hint_phase1(self)

        self.h.bind(on_touch_down = (self.kv))
        self.h.open()

        self.hint.dismiss()


    def kv(self,*args):
        self.h.dismiss()






    def winning(self):


        list = [self.level_2_ref, self.level_3_ref, self.level_4_ref, self.level_5_ref, self.level_6_ref,
                self.level_7_ref, self.level_8_ref, self.level_9_ref, self.level_10_ref, self.level_11_ref,
                self.level_12_ref, self.level_13_ref, self.level_14_ref,self.level_15_ref,self.level_16_ref,self.level_17_ref,self.level_18_ref,self.level_19_ref,self.level_20_ref,self.level_21_ref,
                self.level_22_ref,self.level_23_ref,self.level_24_ref,self.level_25_ref,self.level_26_ref,self.level_27_ref,self.level_28_ref,self.level_29_ref,self.level_30_ref,self.level_31_ref,self.level_32_ref,self.level_33_ref,self.level_34_ref,self.level_35_ref,self.level_36_ref,
                self.level_37_ref,self.level_38_ref,self.level_39_ref,self.level_40_ref,self.level_41_ref,self.level_42_ref,self.level_43_ref,self.level_44_ref,self.level_45_ref,self.level_46_ref,self.level_47_ref,self.level_48_ref,self.level_49_ref,self.level_50_ref,self.level_51_ref,self.level_52_ref,self.level_53_ref,self.level_54_ref,self.level_55_ref,self.level_56_ref,self.level_57_ref,self.level_58_ref,self.level_59_ref,
                self.level_60_ref,self.level_61_ref,self.level_62_ref,self.level_63_ref,self.level_64_ref,self.level_65_ref,self.level_66_ref,self.level_67_ref,self.level_68_ref,self.level_69_ref,self.level_70_ref,self.level_71_ref,self.level_72_ref,self.level_73_ref,self.level_74_ref,self.level_75_ref,self.level_76_ref,self.level_77_ref,self.level_78_ref,self.level_79_ref,self.level_80_ref,
                self.level_81_ref,self.level_82_ref,self.level_83_ref,self.level_84_ref,self.level_85_ref,self.level_86_ref,self.level_87_ref,self.level_88_ref,self.level_89_ref,self.level_90_ref,
                self.level_91_ref,self.level_92_ref,self.level_93_ref,self.level_94_ref,self.level_95_ref,self.level_96_ref,self.level_97_ref,self.level_98_ref,self.level_99_ref,self.level_100_ref,self.phase1_complete]


        if self.level == 1:

            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change8.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change4.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change7.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .8,
                                                                                        "center_y": .2}) and self.ids.change11.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        print("the level is",ret_value)
                        self.question_1_winning_popup(para=list[ret_value])





                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)



        elif self.level == 2:

            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .8, "center_y": .3}:
                    if self.ids.change.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,
                                                                                        "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])


                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)


        elif self.level == 3:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])


                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 4:

            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change4.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .35, "center_y": .2}:

                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])


                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 5:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .8, "center_y": .3}:
                    if self.ids.change2.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .2,
                                                                                        "center_y": .2}) and self.ids.change4.pos_hint in (
                            {"center_x": .5, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])


                    else:
                        Clock.schedule_once(self.coin_10_loosing)

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 6:

            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change16.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .35, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])



                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 7:

            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8, "center_y": .3}:
                    if self.ids.change2.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .35,
                                                                                        "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])


                    else:
                        Clock.schedule_once(self.coin_10_loosing)

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 8:

            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change11.pos_hint == {
                    "center_x": .5, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])


                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 9:

            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change12.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .35,
                                                                                         "center_y": .2}) and self.ids.change16.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        if self.ids.change2.pos_hint in (
                                {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3},
                                {"center_x": .5, "center_y": .2}) and self.ids.change7.pos_hint in (
                                {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3},
                                {"center_x": .5, "center_y": .2}) and self.ids.change9.pos_hint in (
                                {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3},
                                {"center_x": .5, "center_y": .2}):
                            if self.ids.change3.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .8,
                                                                                                 "center_y": .2}) and self.ids.change14.pos_hint in (
                                    {"center_x": .65, "center_y": .3}, {"center_x": .8, "center_y": .2}):
                                ret_value = self.levels_random()
                                self.question_1_winning_popup(para=list[ret_value])


                            else:
                                Clock.schedule_once(self.coin_10_loosing)
                        else:
                            Clock.schedule_once(self.coin_10_loosing)
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 10:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .2, "center_y": .2}:
                    if self.ids.change2.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .35,
                                                                                        "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .35, "center_y": .2}, {"center_x": .2, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 11:

            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .65, "center_y": .2}:

                    if self.ids.change3.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .35,
                                                                                        "center_y": .2}) and self.ids.change6.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        print("pass2")
                        if self.ids.change5.pos_hint in (
                                {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                                {"center_x": .8, "center_y": .2}) and self.ids.change8.pos_hint in (
                                {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .3},
                                {"center_x": .8, "center_y": .2}) and self.ids.change17.pos_hint in (
                                {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                                {"center_x": .8, "center_y": .2}):
                            if self.ids.change9.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .2,
                                                                                                "center_y": .2}) and self.ids.change13.pos_hint in (
                                    {"center_x": .5, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                                ret_value = self.levels_random()
                                self.question_1_winning_popup(para=list[ret_value])

                            else:
                                Clock.schedule_once(self.coin_10_loosing)

                        else:
                            Clock.schedule_once(self.coin_10_loosing)
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 12:

            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} and self.ids.change7.pos_hint == {
                    "center_x": .5, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .2,
                                                                                       "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 13:

            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change16.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                      "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .2, "center_y": .2}:
                    if self.ids.change4.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .35,
                                                                                        "center_y": .2}) and self.ids.change6.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 14:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()

                    self.question_1_winning_popup(para=list[ret_value])


                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 15:

            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                    allhint.hint_all.iq_logic(self)

                    self.hint_count = 0
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 16:

            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 17:

            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change7.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 18:

            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 19:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 20:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change10.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
                    print("noos")


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 21:

            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3}:
                    if self.ids.change2.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .35,
                                                                                        "center_y": .2}) and self.ids.change5.pos_hint in (
                            {"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
                    print("noos")


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 22:

            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 23:

            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 24:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .2, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .65,
                                                                                       "center_y": .3}) and self.ids.change8.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 25:

            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 26:

            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 27:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .2, "center_y": .2}:
                    if self.ids.change5.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change16.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 28:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change8.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .65,
                                                                                      "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()

                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 29:

            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3}:
                    if self.ids.change11.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5,
                                                                                         "center_y": .3}) and self.ids.change16.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
        elif self.level == 30:

            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change12.pos_hint == {"center_x": .35, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 31:

            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    if self.ids.change7.pos_hint in ({"center_x": .35, "center_y": .2}, {"center_x": .5,
                                                                                         "center_y": .2}) and self.ids.change13.pos_hint in (
                            {"center_x": .35, "center_y": .2}, {"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 32:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change10.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 33:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 34:

            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .8,
                                                                                      "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .35, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 35:

            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 36:

            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change8.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .5, "center_y": .2}:
                    if self.ids.change6.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change12.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 37:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change7.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 38:

            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 39:

            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 40:

            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .8,
                    "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} and self.ids.change.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change8.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change3.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,
                                                                                         "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3}, {"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 41:

            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 42:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 43:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 44:

            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3}:
                    if self.ids.change3.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change12.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change1.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change8.pos_hint in (
                            {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 45:

            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .65,
                                                                                     "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .8, "center_y": .2}:
                    if self.ids.change9.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .2,
                                                                                         "center_y": .2}) and self.ids.change11.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .2, "center_y": .2}) and self.ids.change6.pos_hint in (
                            {"center_x": .8, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change2.pos_hint in (
                            {"center_x": .8, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change12.pos_hint in (
                            {"center_x": .5, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change16.pos_hint in (
                            {"center_x": .5, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change4.pos_hint in (
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .35, "center_y": .1}) and self.ids.change10.pos_hint in (
                            {"center_x": .35, "center_y": .2}, {"center_x": .35, "center_y": .1}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)

        elif self.level == 46:

            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .8,
                                                                                      "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change3.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .2,
                                                                                        "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 47:

            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2} and self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .2}:
                    if self.ids.change6.pos_hint in ({"center_x": .5, "center_y": .2}, {"center_x": .65,
                                                                                        "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .2},
                            {"center_x": .65, "center_y": .2}) and self.ids.change.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change5.pos_hint in (
                            {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 48:

            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2} and self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .2}:
                    if self.ids.change6.pos_hint in ({"center_x": .5, "center_y": .2}, {"center_x": .65,
                                                                                        "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .2},
                            {"center_x": .65, "center_y": .2}) and self.ids.change.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change5.pos_hint in (
                            {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 49:

            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .5, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .35,
                                                                                       "center_y": .2}) and self.ids.change16.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .35, "center_y": .2}) and self.ids.change4.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change14.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .2, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change11.pos_hint in (
                            {"center_x": .2, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change2.pos_hint in (
                            {"center_x": .8, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change9.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 50:

            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change12.pos_hint == {"center_x": .65, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 51:

            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} and self.ids.change9.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .65,
                                                                                      "center_y": .2} and self.ids.change.pos_hint == {
                    "center_x": .8, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .2, "center_y": .1}:
                    if self.ids.change2.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change15.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change4.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)

        elif self.level == 52:

            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                      "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} and self.ids.change3.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change8.pos_hint == {"center_x": .65,
                                                                                      "center_y": .2} and self.ids.change2.pos_hint == {
                    "center_x": .8, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .2, "center_y": .1}:
                    if self.ids.change6.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .2,
                                                                                         "center_y": .2}) and self.ids.change11.pos_hint in (
                            {"center_x": .65, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 53:

            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                      "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                      "center_y": .2} and self.ids.change15.pos_hint == {
                    "center_x": .8, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .2, "center_y": .1}:
                    if self.ids.change8.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2},
                            {"center_x": .35, "center_y": .1}) and self.ids.change11.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2},
                            {"center_x": .35, "center_y": .1}) and self.ids.change12.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2},
                            {"center_x": .35, "center_y": .1}) and self.ids.change4.pos_hint in (
                            {"center_x": .8, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change6.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 54:

            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .35,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change9.pos_hint in ({"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1},
                                                     {"center_x": .35,
                                                      "center_y": .1}) and self.ids.change12.pos_hint in (
                            {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1},
                            {"center_x": .35, "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1},
                            {"center_x": .35, "center_y": .1}) and self.ids.change.pos_hint in (
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change5.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 55:

            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .35,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change9.pos_hint in ({"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1},
                                                     {"center_x": .35,
                                                      "center_y": .1}) and self.ids.change12.pos_hint in (
                            {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1},
                            {"center_x": .35, "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1},
                            {"center_x": .35, "center_y": .1}) and self.ids.change.pos_hint in (
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change5.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 56:

            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                      "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} and self.ids.change3.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change8.pos_hint == {"center_x": .65,
                                                                                      "center_y": .2} and self.ids.change2.pos_hint == {
                    "center_x": .8, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .2, "center_y": .1}:
                    if self.ids.change6.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .2,
                                                                                         "center_y": .2}) and self.ids.change11.pos_hint in (
                            {"center_x": .65, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 57:

            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change16.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .35, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])


                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 58:

            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change13.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2}:
                    if self.ids.change6.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,
                                                                                        "center_y": .3}) and self.ids.change8.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change1.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change3.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change5.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 59:

            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .8, "center_y": .3}:
                    if self.ids.change.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,
                                                                                        "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 60:

            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .2}:
                    if self.ids.change5.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .5,
                                                                                        "center_y": .2}) and self.ids.change14.pos_hint in (
                            {"center_x": .5, "center_y": .3}, {"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 61:

            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .8, "center_y": .3}:
                    if self.ids.change.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,
                                                                                        "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 62:

            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change7.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change17.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change5.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .5,
                                                                                         "center_y": .3}) and self.ids.change9.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 63:

            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change13.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2}:
                    if self.ids.change6.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,
                                                                                        "center_y": .3}) and self.ids.change8.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change1.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change3.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change5.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 64:

            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change11.pos_hint == {
                    "center_x": .5, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 65:

            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change16.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 66:

            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .2}, {"center_x": .5,
                                                                                        "center_y": .2}) and self.ids.change11.pos_hint in (
                            {"center_x": .35, "center_y": .2}, {"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 67:

            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                      "center_y": .2} and self.ids.change11.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .35,
                                                                                          "center_y": .2}) and self.ids.change9.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 68:

            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change9.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change5.pos_hint == {
                    "center_x": .5, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .65,
                                                                                       "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 69:

            if self.count in ([i for i in range(3, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .5, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 70:

            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .8,
                    "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change4.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65,
                             "center_y": .3}) and self.ids.change11.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change2.pos_hint in (
                            {"center_x": .5, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change9.pos_hint in (
                            {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 71:

            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .2} and self.ids.change15.pos_hint == {
                    "center_x": .65, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .8,
                                                                                       "center_y": .2} and self.ids.change8.pos_hint == {
                    "center_x": .2, "center_y": .1}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .2,
                                                                                       "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 72:

            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .5, "center_y": .3}:
                    if self.ids.change7.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65,
                                                                                         "center_y": .3}) and self.ids.change17.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 73:

            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .5,
                                                                                        "center_y": .3}) and self.ids.change11.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 74:

            if self.count in ([i for i in range(2, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .35, "center_y": .3}:
                    ret_value = self.levels_random()

                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 75:

            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                       "center_y": .2} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change4.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change8.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change2.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .2, "center_y": .2}) and self.ids.change6.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .2, "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2}) and self.ids.change14.pos_hint in (
                            {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 76:

            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change12.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .2,
                                                                                      "center_y": .2} and self.ids.change9.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .5, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                        "center_y": .2}) and self.ids.change16.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change4.pos_hint in (
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .65, "center_y": .3}, {"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 77:

            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change10.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                     "center_y": .2} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .1}:
                    if self.ids.change6.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3},
                                                     {"center_x": .65, "center_y": .3}, {"center_x": .35,
                                                                                         "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2}) and self.ids.change15.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2}) and self.ids.change13.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change11.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change5.pos_hint in (
                            {"center_x": .65, "center_y": .2},
                            {"center_x": .8, "center_y": .2}) and self.ids.change3.pos_hint in (
                            {"center_x": .65, "center_y": .2}, {"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 78:

            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change10.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                     "center_y": .2} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .1}:
                    if self.ids.change6.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3},
                                                     {"center_x": .65, "center_y": .3}, {"center_x": .35,
                                                                                         "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2}) and self.ids.change15.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2}) and self.ids.change13.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change11.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change5.pos_hint in (
                            {"center_x": .65, "center_y": .2},
                            {"center_x": .8, "center_y": .2}) and self.ids.change3.pos_hint in (
                            {"center_x": .65, "center_y": .2}, {"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 79:

            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change12.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .35,
                                                                                         "center_y": .2}) and self.ids.change16.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        if self.ids.change2.pos_hint in (
                                {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3},
                                {"center_x": .5, "center_y": .2}) and self.ids.change7.pos_hint in (
                                {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3},
                                {"center_x": .5, "center_y": .2}) and self.ids.change9.pos_hint in (
                                {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3},
                                {"center_x": .5, "center_y": .2}):
                            if self.ids.change3.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .8,
                                                                                                 "center_y": .2}) and self.ids.change14.pos_hint in (
                                    {"center_x": .65, "center_y": .3}, {"center_x": .8, "center_y": .2}):
                                ret_value = self.levels_random()
                                self.question_1_winning_popup(para=list[ret_value])

                            else:
                                Clock.schedule_once(self.coin_10_loosing)
                        else:
                            Clock.schedule_once(self.coin_10_loosing)
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 80:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                      "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .2, "center_y": .2}:
                    if self.ids.change11.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                          "center_y": .3}) and self.ids.change7.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 81:

            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                      "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change2.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .35,
                                                                                         "center_y": .2}) and self.ids.change7.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 82:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change16.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .5,

                                                                                      "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .8, "center_y": .3}:
                    if self.ids.change3.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .2,
                                                                                         "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 83:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .2, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,
                                                                                       "center_y": .3}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 84:

            if self.count in ([i for i in range(15, 19)]):
                if self.ids.change13.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change11.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change7.pos_hint == {"center_x": .8,
                                                                                      "center_y": .2}:
                    if self.ids.change.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change1.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change4.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change9.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .35, "center_y": .1}) and self.ids.change10.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .35, "center_y": .1}) and self.ids.change12.pos_hint in (
                            {"center_x": .65, "center_y": .1},
                            {"center_x": .8, "center_y": .1}) and self.ids.change16.pos_hint in (
                            {"center_x": .65, "center_y": .1},
                            {"center_x": .8, "center_y": .1}) and self.ids.change14.pos_hint in (
                            {"center_x": .65, "center_y": .2},
                            {"center_x": .5, "center_y": .1}) and self.ids.change2.pos_hint in (
                            {"center_x": .65, "center_y": .2}, {"center_x": .5, "center_y": .1}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 85:

            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 86:

            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .35,
                                                                                       "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change6.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .8,
                                                                                       "center_y": .2}) and self.ids.change12.pos_hint in (
                            {"center_x": .2, "center_y": .2}, {"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 87:

            if self.count in ([i for i in range(15, 19)]):
                if self.ids.change13.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change11.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change7.pos_hint == {"center_x": .8,
                                                                                      "center_y": .2}:
                    if self.ids.change.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change1.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change4.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change9.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .35, "center_y": .1}) and self.ids.change10.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .35, "center_y": .1}) and self.ids.change12.pos_hint in (
                            {"center_x": .65, "center_y": .1},
                            {"center_x": .8, "center_y": .1}) and self.ids.change16.pos_hint in (
                            {"center_x": .65, "center_y": .1},
                            {"center_x": .8, "center_y": .1}) and self.ids.change14.pos_hint in (
                            {"center_x": .65, "center_y": .2},
                            {"center_x": .5, "center_y": .1}) and self.ids.change2.pos_hint in (
                            {"center_x": .65, "center_y": .2}, {"center_x": .5, "center_y": .1}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 88:

            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change7.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .2,
                                                                                     "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .5,
                                                                                       "center_y": .2} and self.ids.change12.pos_hint == {
                    "center_x": .2, "center_y": .1}:
                    if self.ids.change17.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,
                                                                                          "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change9.pos_hint in (
                            {"center_x": .8, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change13.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 89:

            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change16.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .2,
                                                                                     "center_y": .2} and self.ids.change7.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2} and self.ids.change1.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change15.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .8,
                                                                                          "center_y": .2}) and self.ids.change14.pos_hint in (
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change9.pos_hint in (
                            {"center_x": .8, "center_y": .3},
                            {"center_x": .2, "center_y": .1}) and self.ids.change12.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 90:

            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change8.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .65,
                                                                                        "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .2, "center_y": .1}:
                    if self.ids.change.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .5,
                                                                                        "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .5, "center_y": .2}) and self.ids.change5.pos_hint in (
                            {"center_x": .2, "center_y": .2},
                            {"center_x": .8, "center_y": .2}) and self.ids.change2.pos_hint in (
                            {"center_x": .2, "center_y": .2}, {"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 91:

            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change7.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .2,
                                                                                     "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .5,
                                                                                       "center_y": .2} and self.ids.change12.pos_hint == {
                    "center_x": .2, "center_y": .1}:
                    if self.ids.change17.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,
                                                                                          "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change9.pos_hint in (
                            {"center_x": .8, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change13.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 92:

            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change12.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                      "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change7.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2} and self.ids.change4.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change14.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .2,
                                                                                          "center_y": .2}) and self.ids.change10.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 93:

            if self.count in ([i for i in range(14, 19)]):
                if self.ids.change1.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change10.pos_hint == {
                    "center_x": .8, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .2,
                                                                                      "center_y": .1} and self.ids.change15.pos_hint == {
                    "center_x": .35, "center_y": .1} and self.ids.change17.pos_hint == {"center_x": .5, "center_y": .1}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .3},
                                                    {"center_x": .2, "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .2, "center_y": .2}) and self.ids.change16.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .2, "center_y": .2}) and self.ids.change4.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change12.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change2.pos_hint in (
                            {"center_x": .5, "center_y": .2},
                            {"center_x": .65, "center_y": .1}) and self.ids.change14.pos_hint in (
                            {"center_x": .5, "center_y": .2}, {"center_x": .65, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 94:

            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change10.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change13.pos_hint == {"center_x": .65,
                                                                                       "center_y": .2} and self.ids.change2.pos_hint == {
                    "center_x": .8, "center_y": .2}:
                    if self.ids.change1.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .2,
                                                                                        "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .2, "center_y": .2}) and self.ids.change3.pos_hint in (
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .2, "center_y": .1}) and self.ids.change7.pos_hint in (
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .2, "center_y": .1}) and self.ids.change9.pos_hint in (
                            {"center_x": .8, "center_y": .3},
                            {"center_x": .35, "center_y": .1}) and self.ids.change14.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .35, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 95:

            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change6.pos_hint == {
                    "center_x": .5, "center_y": .2}:
                    if self.ids.change7.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .2,
                                                                                        "center_y": .1}) and self.ids.change9.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .2, "center_y": .1}) and self.ids.change2.pos_hint in (
                            {"center_x": .5, "center_y": .3}, {"center_x": .8, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change11.pos_hint in (
                            {"center_x": .5, "center_y": .3}, {"center_x": .8, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change14.pos_hint in (
                            {"center_x": .5, "center_y": .3}, {"center_x": .8, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change3.pos_hint in (
                            {"center_x": .2, "center_y": .2},
                            {"center_x": .8, "center_y": .2}) and self.ids.change13.pos_hint in (
                            {"center_x": .2, "center_y": .2}, {"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 96:

            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change12.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .2,
                                                                                      "center_y": .2} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change5.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change17.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change2.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change11.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change6.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change14.pos_hint in (
                            {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 97:

            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change6.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                      "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change1.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change12.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change8.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65,
                                                                                         "center_y": .3}) and self.ids.change16.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change5.pos_hint in (
                            {"center_x": .8, "center_y": .3},
                            {"center_x": .2, "center_y": .2}) and self.ids.change.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 98:

            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change9.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change13.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change8.pos_hint == {
                    "center_x": .8, "center_y": .2}:
                    if self.ids.change1.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65,
                                                                                         "center_y": .2}) and self.ids.change15.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change12.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change4.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .2, "center_y": .2}) and self.ids.change7.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 99:

            if self.count in ([i for i in range(14, 19)]):
                if self.ids.change7.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .65,
                                                                                      "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} and self.ids.change16.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .2, "center_y": .1}:
                    if self.ids.change.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2},
                            {"center_x": .5, "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2},
                            {"center_x": .5, "center_y": .1}) and self.ids.change9.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2},
                            {"center_x": .5, "center_y": .1}) and self.ids.change5.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .1}) and self.ids.change12.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .1}) and self.ids.change3.pos_hint in (
                            {"center_x": .8, "center_y": .2},
                            {"center_x": .35, "center_y": .1}) and self.ids.change15.pos_hint in (
                            {"center_x": .8, "center_y": .2}, {"center_x": .35, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 100:

            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change6.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change13.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} and self.ids.change4.pos_hint == {
                    "center_x": .5, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                        "center_y": .3}) and self.ids.change17.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)




    def phase1_complete(self, *args):
        self.phase_complete = Popup()
        self.phase_complete.title = "Phase 1"
        self.phase_complete.title_align = "center"
        self.phase_complete.title_size = '35sp'
        self.phase_complete.separator_height = dp(0)
        self.phase_complete.background_color = (79 / 255, 150 / 255, 220 / 255)
        self.lay = BoxLayout()
        self.lay.orientation = "vertical"
        self.lab = Label()
        self.lab.text = "Completed"
        self.lab.color = "red"
        self.lab.font_size = "30sp"
        self.lay.add_widget(self.lab)
        self.phase_complete.add_widget(self.lay)
        self.phase_complete.size_hint = 1, 1
        self.phase_complete.open()


class phase_2(Screen, phase2_level.phase2_questions, coin_logic.coin_logic_18, retrewingdata.retrew_data_json,
              winingfile.winninggame,coinmovement.movement,levels_game2.level_game_comic):
    def __init__(self, **kwargs):
        super(phase_2, self).__init__(**kwargs)
        retrewingdata.retrew_data_json.__init__(self, filename="phase2.json")
        retrewingdata.retrew_data_json.getting_items(self)
        self.coin_js = JsonStore("coins_win.json")
        self.iqjs = JsonStore("iq_score.json")
        self.hint_count = 0
        self.ids.coins.text = str(self.coin_js.get("coin_base")["coins"])
        self.ids.iq.text = str(self.iqjs.get("iq_score")["score"])
    def levels_random(self):


        js = JsonStore("randomliststorage1.json")
        l = js.get("random_level_list")["levels"]
        if l != []:
            ran = random.choice(l)

            print(ran)
            l.remove(ran)


            js.put("random_level_list", levels=l)


            return  ran
        else:
            return 99
    def phase1_complete(self, *args):
        self.phase_complete = Popup()
        self.phase_complete.title = "Phase 2"
        self.phase_complete.title_align = "center"
        self.phase_complete.title_size = '35sp'
        self.phase_complete.separator_height = dp(0)
        self.phase_complete.background_color = (79 / 255, 150 / 255, 220 / 255)
        self.lay = BoxLayout()
        self.lay.orientation = "vertical"
        self.lab = Label()
        self.lab.text = "Completed"
        self.lab.color = "red"
        self.lab.font_size = "30sp"
        self.lay.add_widget(self.lab)
        self.phase_complete.add_widget(self.lay)
        self.phase_complete.size_hint = 1, 1
        self.phase_complete.open()
    def level1_hint(self):

            self.hint = Popup()
            self.hint.title = "Hint"
            self.hint.title_align = "center"
            self.hint.size_hint = .9,.2


            self.hint.separator_height = dp(0)
            self.hint.background_color = (100 / 255, 100 / 255, 100 / 255)
            self.layout = BoxLayout()
            self.layout.size_hint = 1,1
            self.button_coin = Button()
            self.button_free = Button()
            self.button_coin.text = "3coins"
            self.button_coin.bind(on_press = self.hint_coin)
            self.button_coin.size_hint = 1,.6
            self.button_coin.padding_x = .2
            self.button_coin.pos_hint = {"center_x":.1,"center_y":.55}
            self.button_coin.background_color = "red"
            self.layout.add_widget(self.button_coin)
            self.button_free.text = "Free add"
            self.button_free.size_hint = 1,.6
            self.button_free.padding_x = .2
            self.button_free.pos_hint = {"center_x": .1, "center_y": .55}
            self.button_free.background_color = "red"
            self.layout.add_widget(self.button_free)
            self.hint.add_widget(self.layout)
            print(self.count)
            self.hint.open()




    def hint_coin(self,*args):
        self.hint_count += 1
        print(self.hint_count)
        self.h = Popup()
        self.h.title = ""
        self.h.separator_height = dp(0)
        self.h.size_hint = .8, .2
        self.h.title = "Here is your Hint"
        self.h.title_align = "center"
        self.h.background_color = "green"
        self.lab= Label(text = "",pos_hint= {"center_x":5,"center_y":.7},bold = True)
        self.h.content = self.lab
        allhint.hint_all.hint_phase1(self)

        self.h.bind(on_touch_down = (self.kv))
        self.h.open()

        self.hint.dismiss()


    def kv(self,*args):
        self.h.dismiss()


    def winning(self):
        list = [self.level_102_ref, self.level_103_ref, self.level_104_ref, self.level_105_ref, self.level_106_ref,
                self.level_107_ref, self.level_108_ref, self.level_109_ref, self.level_110_ref, self.level_111_ref,
                self.level_112_ref, self.level_113_ref, self.level_114_ref, self.level_115_ref, self.level_116_ref,
                self.level_117_ref, self.level_118_ref, self.level_119_ref, self.level_120_ref, self.level_121_ref,
                self.level_122_ref, self.level_123_ref, self.level_124_ref, self.level_125_ref, self.level_126_ref,
                self.level_127_ref, self.level_128_ref, self.level_129_ref, self.level_130_ref, self.level_131_ref,
                self.level_132_ref, self.level_133_ref, self.level_134_ref, self.level_135_ref, self.level_136_ref,
                self.level_137_ref, self.level_138_ref, self.level_139_ref, self.level_140_ref, self.level_141_ref,
                self.level_142_ref, self.level_143_ref, self.level_144_ref, self.level_145_ref, self.level_146_ref, self.level_147_ref, self.level_148_ref, self.level_149_ref, self.level_150_ref, self.level_151_ref,
                self.level_152_ref, self.level_153_ref, self.level_154_ref, self.level_155_ref, self.level_156_ref,
                self.level_157_ref, self.level_158_ref, self.level_159_ref,
                self.level_160_ref, self.level_161_ref, self.level_162_ref, self.level_163_ref, self.level_164_ref,
                self.level_165_ref, self.level_166_ref, self.level_167_ref, self.level_168_ref, self.level_169_ref,
                self.level_170_ref, self.level_171_ref, self.level_172_ref, self.level_173_ref, self.level_174_ref,
                self.level_175_ref, self.level_176_ref, self.level_177_ref, self.level_178_ref, self.level_179_ref,
                self.level_180_ref,
                self.level_181_ref, self.level_182_ref, self.level_183_ref, self.level_184_ref, self.level_185_ref,
                self.level_186_ref, self.level_187_ref, self.level_188_ref, self.level_189_ref, self.level_190_ref,
                self.level_191_ref, self.level_192_ref, self.level_193_ref, self.level_194_ref, self.level_195_ref,
                self.level_196_ref, self.level_197_ref, self.level_198_ref, self.level_199_ref, self.level_200_ref,self.phase1_complete]
        if self.level == 150:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change5.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .2, "center_y": .2}:
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 151:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .8, "center_y": .3}:
                    if self.ids.change.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,
                                                                                        "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 152:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change13.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .2, "center_y": .2}:
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 153:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change10.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .35,
                                                                                        "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change7.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} and self.ids.change11.pos_hint == {
                    "center_x": .8, "center_y": .2} :
                    if self.ids.change2.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .35,
                                                                                        "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .35, "center_y": .1}) and self.ids.change.pos_hint in (
                            {"center_x": .8, "center_y": .3},{"center_x": .5, "center_y": .2},{"center_x": .65, "center_y": .2},{"center_x": .2, "center_y": .1}) and self.ids.change5.pos_hint in ({"center_x": .8, "center_y": .3},{"center_x": .5, "center_y": .2},{"center_x": .65, "center_y": .2},{"center_x": .2, "center_y": .1}
                            ) and self.ids.change12.pos_hint in (
                            {"center_x": .8, "center_y": .3},{"center_x": .5, "center_y": .2},{"center_x": .65, "center_y": .2},{"center_x": .2, "center_y": .1}) and self.ids.change8.pos_hint in (
                            {"center_x": .8, "center_y": .3},{"center_x": .5, "center_y": .2},{"center_x": .65, "center_y": .2},{"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=self.level_101_ref)
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 154:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 155:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change9.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change13.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change8.pos_hint == {
                    "center_x": .8, "center_y": .2}:
                    if self.ids.change1.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65,
                                                                                         "center_y": .2}) and self.ids.change15.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change12.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change4.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .2, "center_y": .2}) and self.ids.change7.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 156:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change9.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change13.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change8.pos_hint == {
                    "center_x": .8, "center_y": .2}:
                    if self.ids.change1.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65,
                                                                                         "center_y": .2}) and self.ids.change15.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change12.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change4.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .2, "center_y": .2}) and self.ids.change7.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 157:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change16.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .2,
                                                                                     "center_y": .2} and self.ids.change7.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2} and self.ids.change1.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change15.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .8,
                                                                                          "center_y": .2}) and self.ids.change14.pos_hint in (
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change9.pos_hint in (
                            {"center_x": .8, "center_y": .3},
                            {"center_x": .2, "center_y": .1}) and self.ids.change12.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 158:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change13.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .2, "center_y": .2}:
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 159:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change10.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                     "center_y": .2} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .1}:
                    if self.ids.change6.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3},
                                                     {"center_x": .65, "center_y": .3}, {"center_x": .35,
                                                                                         "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2}) and self.ids.change15.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2}) and self.ids.change13.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change11.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change5.pos_hint in (
                            {"center_x": .65, "center_y": .2},
                            {"center_x": .8, "center_y": .2}) and self.ids.change3.pos_hint in (
                            {"center_x": .65, "center_y": .2}, {"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 160:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .65, "center_y": .2}:

                    if self.ids.change3.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .35,
                                                                                        "center_y": .2}) and self.ids.change6.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        print("pass2")
                        if self.ids.change5.pos_hint in (
                                {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                                {"center_x": .8, "center_y": .2}) and self.ids.change8.pos_hint in (
                                {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .3},
                                {"center_x": .8, "center_y": .2}) and self.ids.change17.pos_hint in (
                                {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                                {"center_x": .8, "center_y": .2}):
                            if self.ids.change9.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .2,
                                                                                                "center_y": .2}) and self.ids.change13.pos_hint in (
                                    {"center_x": .5, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                                ret_value = self.levels_random()
                                self.question_1_winning_popup(para=list[ret_value])
                            else:
                                Clock.schedule_once(self.coin_10_loosing)

                        else:
                            Clock.schedule_once(self.coin_10_loosing)
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 161:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3}:
                    if self.ids.change11.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5,
                                                                                         "center_y": .3}) and self.ids.change16.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
        elif self.level == 162:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .2, "center_y": .2}:
                    if self.ids.change5.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change16.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 163:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 164:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 165:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3}:
                    if self.ids.change11.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5,
                                                                                         "center_y": .3}) and self.ids.change16.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
        elif self.level == 166:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .2} and self.ids.change15.pos_hint == {
                    "center_x": .65, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .8,
                                                                                       "center_y": .2} and self.ids.change8.pos_hint == {
                    "center_x": .2, "center_y": .1}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .2,
                                                                                       "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 167:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change11.pos_hint == {
                    "center_x": .5, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 168:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .8,
                    "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} and self.ids.change.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change8.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change3.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,
                                                                                         "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3}, {"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 169:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                      "center_y": .2} and self.ids.change11.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .35,
                                                                                          "center_y": .2}) and self.ids.change9.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 170:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change16.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 171:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change11.pos_hint == {
                    "center_x": .5, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 172:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change9.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change5.pos_hint == {
                    "center_x": .5, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .65,
                                                                                       "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 173:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change9.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change5.pos_hint == {
                    "center_x": .5, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .65,
                                                                                       "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 174:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()

                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 175:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .8,
                    "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change4.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65,
                             "center_y": .3}) and self.ids.change11.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change2.pos_hint in (
                            {"center_x": .5, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change9.pos_hint in (
                            {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 176:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2} and self.ids.change15.pos_hint == {
                    "center_x": .35, "center_y": .2}:
                    if self.ids.change4.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .8, "center_y": .3} ) and self.ids.change12.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .8, "center_y": .3} ) and self.ids.change.pos_hint in ( {"center_x": .5, "center_y": .3} , {"center_x": .5, "center_y": .2} ) and self.ids.change16.pos_hint in ( {"center_x": .5, "center_y": .3} , {"center_x": .5, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 177:
            if self.count in ([i for i in range(14, 19)]):
                if self.ids.change6.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .65,
                                                                                      "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .35,
                                                                                     "center_y": .2} and self.ids.change16.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .65,
                                                                                        "center_y": .1} :
                    if self.ids.change2.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5,
                                                                                          "center_y": .1}) and self.ids.change10.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .5, "center_y": .1}) and self.ids.change1.pos_hint in (
                            {"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .2},{"center_x": .2, "center_y": .1}) and self.ids.change8.pos_hint in (
                            {"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .2},{"center_x": .2, "center_y": .1}) and self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .2},{"center_x": .2, "center_y": .1}) and self.ids.change4.pos_hint in ({"center_x": .8, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) and  self.ids.change15.pos_hint in ({"center_x": .8, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) and  self.ids.change13.pos_hint in ({"center_x": .8, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 178:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .2, "center_y": .2}:
                    if self.ids.change2.pos_hint in ( {"center_x": .35, "center_y": .2} , {"center_x": .5, "center_y": .2} ) and self.ids.change14.pos_hint in ( {"center_x": .35, "center_y": .2} , {"center_x": .5, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 179:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change9.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .65, "center_y": .2}  and self.ids.change7.pos_hint == {"center_x": .8, "center_y": .2} :
                    if self.ids.change1.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .8, "center_y": .3} ) and self.ids.change17.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .8, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 180:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change4.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change7.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2}:
                    if self.ids.change12.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .65, "center_y": .2} ) and self.ids.change8.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .65, "center_y": .2} )  and self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .5, "center_y": .2} ) and self.ids.change5.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .5, "center_y": .2} ) and self.ids.change2.pos_hint in ( {"center_x": .5, "center_y": .3} , {"center_x": .8, "center_y": .2} ) and  self.ids.change17.pos_hint in ( {"center_x": .5, "center_y": .3} , {"center_x": .8, "center_y": .2} ) and  self.ids.change11.pos_hint in ( {"center_x": .35, "center_y": .2} , {"center_x": .2, "center_y": .1} ) and self.ids.change6.pos_hint in ( {"center_x": .35, "center_y": .2} , {"center_x": .2, "center_y": .1} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 181:
            if self.count in ([i for i in range(2, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 182:
            if self.count in ([i for i in range(2, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 183:
            if self.count in ([i for i in range(2, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 184:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change7.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .2,
                                                                                     "center_y": .2} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .8,
                                                                                        "center_y": .2} and self.ids.change11.pos_hint ==  {"center_x": .2, "center_y": .1}:
                    if self.ids.change5.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .5,
                                                                                          "center_y": .2}) and self.ids.change13.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .5, "center_y": .2}) and self.ids.change.pos_hint in (
                            {"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) and self.ids.change9.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 185:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change1.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .5,
                                                                                      "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change13.pos_hint == {"center_x": .5,
                                                                                     "center_y": .2} :
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .65,
                                                                                          "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change2.pos_hint in (
                            {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .1}) and self.ids.change9.pos_hint in (
                            {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .1}) and self.ids.change4.pos_hint in ({"center_x": .8, "center_y": .3},{"center_x": .35, "center_y": .1}) and  self.ids.change12.pos_hint in ({"center_x": .8, "center_y": .3},{"center_x": .35, "center_y": .1}) and self.ids.change11.pos_hint in ({"center_x": .35, "center_y": .2},{"center_x": .8, "center_y": .2}) and self.ids.change7.pos_hint in ({"center_x": .35, "center_y": .2},{"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 186:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change7.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .2,
                                                                                     "center_y": .2} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .8,
                                                                                        "center_y": .2} and self.ids.change11.pos_hint ==  {"center_x": .2, "center_y": .1}:
                    if self.ids.change5.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .5,
                                                                                          "center_y": .2}) and self.ids.change13.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .5, "center_y": .2}) and self.ids.change.pos_hint in (
                            {"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) and self.ids.change9.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 187:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .5, "center_y": .2}  and self.ids.change15.pos_hint == {"center_x": .65, "center_y": .2} :
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .2} , {"center_x": .8, "center_y": .2} ) and self.ids.change17.pos_hint in ( {"center_x": .35, "center_y": .2} , {"center_x": .8, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 188:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change7.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} :
                    if self.ids.change3.pos_hint in ( {"center_x": .65, "center_y": .3} , {"center_x": .8, "center_y": .3} ) and self.ids.change14.pos_hint in ( {"center_x": .65, "center_y": .3} , {"center_x": .8, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 189:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and  self.ids.change7.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change16.pos_hint == {"center_x": .35, "center_y": .2}:
                    if self.ids.change.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .65, "center_y": .3} ) and self.ids.change5.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .65, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 190:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and  self.ids.change13.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change16.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change8.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change5.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change2.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .35, "center_y": .2} ) and self.ids.change6.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .35, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)

        elif self.level == 191:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and  self.ids.change7.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change16.pos_hint == {"center_x": .35, "center_y": .2}:
                    if self.ids.change.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .65, "center_y": .3} ) and self.ids.change5.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .65, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 192:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and  self.ids.change.pos_hint == {"center_x": .2, "center_y": .2} :
                    if self.ids.change2.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .8, "center_y": .3} ) and self.ids.change17.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .8, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 193:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and  self.ids.change2.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .5, "center_y": .2}:
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 194:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and  self.ids.change8.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .2, "center_y": .2} :
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 195:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2}  :
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3},{"center_x": .8, "center_y": .3}) and self.ids.change8.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3},{"center_x": .8, "center_y": .3}) and self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3},{"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 196:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    if self.ids.change7.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}) and self.ids.change11.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}) and self.ids.change3.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2}) and self.ids.change15.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 197:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and  self.ids.change.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change12.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change17.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change1.pos_hint == {"center_x": .8, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change13.pos_hint == {"center_x": .35, "center_y": .1} :
                    if  self.ids.change2.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .2, "center_y": .2}) and self.ids.change14.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 198:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and  self.ids.change12.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .8, "center_y": .2} :
                        ret_value = self.levels_random()


                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 199:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and  self.ids.change2.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .5, "center_y": .2}:
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 380:
            if self.count in ([i for i in range(3, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 200:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2}:
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}) and  self.ids.change13.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}) and  self.ids.change5.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}) and self.ids.change10.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}) and self.ids.change11.pos_hint in ( {"center_x": .5, "center_y": .2}, {"center_x": .65, "center_y": .2}) and  self.ids.change6.pos_hint in ( {"center_x": .5, "center_y": .2}, {"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)


        elif self.level == 101:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and  self.ids.change13.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .5, "center_y": .2} :
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3}) and  self.ids.change8.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3}) and  self.ids.change7.pos_hint in ( {"center_x": .65, "center_y": .2}, {"center_x": .8, "center_y": .2}) and self.ids.change15.pos_hint in ( {"center_x": .65, "center_y": .2}, {"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 102:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and  self.ids.change6.pos_hint == {"center_x": .8, "center_y": .3}:
                    if self.ids.change13.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .2}) and  self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 103:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 104:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} :
                    if self.ids.change6.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .8, "center_y": .3}) and  self.ids.change15.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 105:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} :
                    if self.ids.change5.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}) and  self.ids.change12.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 106:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 107:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and  self.ids.change6.pos_hint == {"center_x": .8, "center_y": .3}:
                    if self.ids.change13.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .2}) and  self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 108:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3}  and self.ids.change7.pos_hint == {"center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 109:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .8, "center_y": .2} and self.ids.change13.pos_hint == {"center_x": .2,
                                                                                        "center_y": .1} :
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2}) and  self.ids.change5.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2}) and self.ids.change17.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .2}) and  self.ids.change2.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}) and  self.ids.change6.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}) and  self.ids.change12.pos_hint in ( {"center_x": .8, "center_y": .3}, {"center_x": .2, "center_y": .2}) and  self.ids.change11.pos_hint in ( {"center_x": .8, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 110:
            if self.count in ([i for i in range(3, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 111:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 112:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 113:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 114:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change.pos_hint == {"center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 115:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and  self.ids.change5.pos_hint == {"center_x": .65, "center_y": .3}  and  self.ids.change8.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change14.pos_hint == {"center_x": .35, "center_y": .2}:
                    if self.ids.change6.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .5,
                                                                                        "center_y": .2}) and self.ids.change17.pos_hint in (
                    {"center_x": .2, "center_y": .2}, {"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 116:
            if self.count in ([i for i in range(13, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change4.pos_hint == {"center_x": .8,
                                                                                        "center_y": .2}  and self.ids.change14.pos_hint == {"center_x": .2, "center_y": .1}:
                    if self.ids.change1.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .2}) and  self.ids.change9.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .2}) and self.ids.change13.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .1}) and  self.ids.change16.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .1}) and  self.ids.change.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .5, "center_y": .1}) and  self.ids.change12.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .5, "center_y": .1}) and  self.ids.change3.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2},{"center_x": .2, "center_y": .2}) and   self.ids.change6.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2},{"center_x": .2, "center_y": .2}) and   self.ids.change11.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2},{"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 117:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change7.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2} and  self.ids.change12.pos_hint == {"center_x": .35, "center_y": .2} :
                    if self.ids.change2.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .5,
                                                                                        "center_y": .2}) and self.ids.change5.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2}) and  self.ids.change.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,"center_y": .3}) and self.ids.change17.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,"center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 118:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change10.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} :
                    if self.ids.change.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}) and  self.ids.change8.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 119:
            if self.count in ([i for i in range(13, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3}  and self.ids.change11.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change9.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change4.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change5.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3}) and  self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3}) and self.ids.change3.pos_hint in ( {"center_x": .2, "center_y": .2}, {"center_x": .2, "center_y": .1}) and  self.ids.change17.pos_hint in ( {"center_x": .2, "center_y": .2}, {"center_x": .2, "center_y": .1}) and  self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .1}, {"center_x": .5, "center_y": .1}) and  self.ids.change14.pos_hint in ( {"center_x": .35, "center_y": .1}, {"center_x": .5, "center_y": .1}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 120:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .65, "center_y": .3}  and self.ids.change11.pos_hint == {"center_x": .8, "center_y": .3}  and self.ids.change3.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change5.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2},{"center_x": .2, "center_y": .2}) and  self.ids.change12.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2},{"center_x": .2, "center_y": .2}) and  self.ids.change8.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2},{"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 121:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 122:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    if self.ids.change8.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .8, "center_y": .3}) and  self.ids.change17.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .8, "center_y": .3}) and  self.ids.change12.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .2, "center_y": .2}) and  self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 123:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change7.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change17.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2}) and  self.ids.change2.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2}) and  self.ids.change5.pos_hint in ( {"center_x": .5, "center_y": .3},{"center_x": .65, "center_y": .3}) and  self.ids.change12.pos_hint in ( {"center_x": .5, "center_y": .3},{"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 124:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change3.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change5.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .2, "center_y": .1}) and  self.ids.change15.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .2, "center_y": .1}) and  self.ids.change11.pos_hint in ( {"center_x": .35, "center_y": .2},{"center_x": .8, "center_y": .2}) and  self.ids.change1.pos_hint in ( {"center_x": .35, "center_y": .2},{"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 125:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .2, "center_y": .2} and  self.ids.change11.pos_hint == {"center_x": .35, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 126:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8, "center_y": .3}  and self.ids.change14.pos_hint == {"center_x": .2, "center_y": .2}  and self.ids.change12.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change3.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .5, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change5.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .5, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change7.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .5, "center_y": .3},{"center_x": .5, "center_y": .2}) and self.ids.change2.pos_hint in ( {"center_x": .8, "center_y": .2}, {"center_x": .2, "center_y": .1}) and self.ids.change16.pos_hint in ( {"center_x": .8, "center_y": .2}, {"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 127:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .65, "center_y": .3}  and self.ids.change11.pos_hint == {"center_x": .8, "center_y": .3}  and self.ids.change8.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change17.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change.pos_hint in ( {"center_x": .8, "center_y": .2}, {"center_x": .5, "center_y": .3},{"center_x": .35, "center_y": .2}) and  self.ids.change15.pos_hint in ( {"center_x": .8, "center_y": .2}, {"center_x": .5, "center_y": .3},{"center_x": .35, "center_y": .2}) and  self.ids.change13.pos_hint in ( {"center_x": .8, "center_y": .2}, {"center_x": .5, "center_y": .3},{"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 128:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .2, "center_y": .2} and  self.ids.change1.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change13.pos_hint == {"center_x": .65, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 129:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 130:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2}:
                    if self.ids.change3.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3}  ) and self.ids.change15.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 131:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .2, "center_y": .2}  and self.ids.change8.pos_hint == {"center_x": .65, "center_y": .2}  and self.ids.change17.pos_hint == {"center_x": .8, "center_y": .2} :
                    if self.ids.change1.pos_hint in ( {"center_x": .2, "center_y": .1}, {"center_x": .5, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change16.pos_hint in ({"center_x": .2, "center_y": .1}, {"center_x": .5, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change15.pos_hint in ({"center_x": .2, "center_y": .1}, {"center_x": .5, "center_y": .3},{"center_x": .5, "center_y": .2}) and self.ids.change3.pos_hint in ( {"center_x": .35, "center_y": .2}, {"center_x": .35, "center_y": .3}) and self.ids.change4.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .1}) and self.ids.change14.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 132:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change7.pos_hint == {"center_x": .8, "center_y": .3}  and self.ids.change17.pos_hint == {"center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 133:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 134:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .2, "center_y": .2} :
                    if self.ids.change12.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}  ) and self.ids.change15.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=lkist[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 135:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 136:
            if self.count in ([i for i in range(3, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 137:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2}:
                    if self.ids.change3.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3}  ) and self.ids.change15.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 138:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change7.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 139:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 140:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .8, "center_y": .2} and self.ids.change7.pos_hint == {"center_x": .2, "center_y": .1}:
                    if self.ids.change.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .35, "center_y": .2}  ) and self.ids.change17.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .35, "center_y": .2}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 141:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .5, "center_y": .3}  and self.ids.change12.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2}:
                    if self.ids.change8.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3}  ) and self.ids.change10.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 142:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 143:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                      "center_y": .2} and self.ids.change11.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .35,
                                                                                          "center_y": .2}) and self.ids.change9.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 144:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change16.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                      "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .2, "center_y": .2}:
                    if self.ids.change4.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .35,
                                                                                        "center_y": .2}) and self.ids.change6.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 145:
            if self.count in ([i for i in range(15, 19)]):
                if self.ids.change13.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change11.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change7.pos_hint == {"center_x": .8,
                                                                                      "center_y": .2}:
                    if self.ids.change.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change1.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change4.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change9.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .35, "center_y": .1}) and self.ids.change10.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .35, "center_y": .1}) and self.ids.change12.pos_hint in (
                            {"center_x": .65, "center_y": .1},
                            {"center_x": .8, "center_y": .1}) and self.ids.change16.pos_hint in (
                            {"center_x": .65, "center_y": .1},
                            {"center_x": .8, "center_y": .1}) and self.ids.change14.pos_hint in (
                            {"center_x": .65, "center_y": .2},
                            {"center_x": .5, "center_y": .1}) and self.ids.change2.pos_hint in (
                            {"center_x": .65, "center_y": .2}, {"center_x": .5, "center_y": .1}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 146:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .8, "center_y": .2} and self.ids.change7.pos_hint == {"center_x": .2, "center_y": .1}:
                    if self.ids.change.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .35, "center_y": .2}  ) and self.ids.change17.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .35, "center_y": .2}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 147:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 148:
            if self.count in ([i for i in range(14, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .8, "center_y": .3}  and self.ids.change6.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change9.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .2}  ) and self.ids.change1.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .2}  ) and self.ids.change16.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .35, "center_y": .1}  ) and self.ids.change15.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .35, "center_y": .1}  ) and self.ids.change7.pos_hint in ({"center_x": .5, "center_y": .1},{"center_x": .65, "center_y": .1}  ) and self.ids.change14.pos_hint in ({"center_x": .5, "center_y": .1},{"center_x": .65, "center_y": .1}  ) and  self.ids.change11.pos_hint in ({"center_x": .35, "center_y": .2},{"center_x": .2, "center_y": .1}  ) and  self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .2},{"center_x": .2, "center_y": .1}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 149:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
class phase_3(Screen,phase3_level.phase3_questions, coin_logic.coin_logic_18, retrewingdata.retrew_data_json,
              winingfile.winninggame,coinmovement.movement):
    def __init__(self, **kwargs):
        super(phase_3, self).__init__(**kwargs)
        retrewingdata.retrew_data_json.__init__(self, filename="phase3.json")
        retrewingdata.retrew_data_json.getting_items(self)
        self.coin_js = JsonStore("coins_win.json")
        self.iqjs = JsonStore("iq_score.json")
        self.hint_count = 0
        self.ids.coins.text = str(self.coin_js.get("coin_base")["coins"])
        self.ids.iq.text = str(self.iqjs.get("iq_score")["score"])


    def levels_random(self):


        js = JsonStore("randomliststorage2.json")
        l = js.get("random_level_list")["levels"]
        if l != []:
            ran = random.choice(l)

            print(ran)
            l.remove(ran)


            js.put("random_level_list", levels=l)


            return  ran
        else:
            return 179
    def phase1_complete(self, *args):
        self.phase_complete = Popup()
        self.phase_complete.title = "Phase 3"
        self.phase_complete.title_align = "center"
        self.phase_complete.title_size = '35sp'
        self.phase_complete.separator_height = dp(0)
        self.phase_complete.background_color = (79 / 255, 150 / 255, 220 / 255)
        self.lay = BoxLayout()
        self.lay.orientation = "vertical"
        self.lab = Label()
        self.lab.text = "Completed"
        self.lab.color = "red"
        self.lab.font_size = "30sp"
        self.lay.add_widget(self.lab)
        self.phase_complete.add_widget(self.lay)
        self.phase_complete.size_hint = 1, 1
        self.phase_complete.open()
    def level1_hint(self):

            self.hint = Popup()
            self.hint.title = "Hint"
            self.hint.title_align = "center"
            self.hint.size_hint = .9,.2


            self.hint.separator_height = dp(0)
            self.hint.background_color = (100 / 255, 100 / 255, 100 / 255)
            self.layout = BoxLayout()
            self.layout.size_hint = 1,1
            self.button_coin = Button()
            self.button_free = Button()
            self.button_coin.text = "3coins"
            self.button_coin.bind(on_press = self.hint_coin)
            self.button_coin.size_hint = 1,.6
            self.button_coin.padding_x = .2
            self.button_coin.pos_hint = {"center_x":.1,"center_y":.55}
            self.button_coin.background_color = "red"
            self.layout.add_widget(self.button_coin)
            self.button_free.text = "Free add"
            self.button_free.size_hint = 1,.6
            self.button_free.padding_x = .2
            self.button_free.pos_hint = {"center_x": .1, "center_y": .55}
            self.button_free.background_color = "red"
            self.layout.add_widget(self.button_free)
            self.hint.add_widget(self.layout)
            print(self.count)
            self.hint.open()




    def hint_coin(self,*args):
        self.hint_count += 1
        print(self.hint_count)
        self.h = Popup()
        self.h.title = ""
        self.h.separator_height = dp(0)
        self.h.size_hint = .8, .2
        self.h.title = "Here is your Hint"
        self.h.title_align = "center"
        self.h.background_color = "green"
        self.lab= Label(text = "",pos_hint= {"center_x":5,"center_y":.7},bold = True)
        self.h.content = self.lab
        allhint.hint_all.hint_phase1(self)

        self.h.bind(on_touch_down = (self.kv))
        self.h.open()

        self.hint.dismiss()


    def kv(self,*args):
        self.h.dismiss()

    def winning(self):
        list = [ self.level_202_ref, self.level_203_ref, self.level_204_ref, self.level_205_ref,
                self.level_206_ref, self.level_207_ref, self.level_208_ref, self.level_209_ref, self.level_210_ref,
                self.level_211_ref, self.level_212_ref, self.level_213_ref, self.level_214_ref, self.level_215_ref,
                self.level_216_ref, self.level_217_ref, self.level_218_ref, self.level_219_ref, self.level_220_ref,
                self.level_221_ref, self.level_222_ref, self.level_223_ref, self.level_224_ref, self.level_225_ref,
                self.level_226_ref, self.level_227_ref, self.level_228_ref, self.level_229_ref, self.level_230_ref,
                self.level_231_ref, self.level_232_ref, self.level_233_ref, self.level_234_ref, self.level_235_ref,
                self.level_236_ref, self.level_237_ref, self.level_238_ref, self.level_239_ref,
                self.level_240_ref, self.level_241_ref, self.level_242_ref, self.level_243_ref, self.level_244_ref,
                self.level_245_ref, self.level_246_ref, self.level_247_ref, self.level_248_ref, self.level_249_ref,
                self.level_250_ref, self.level_251_ref, self.level_252_ref, self.level_253_ref, self.level_254_ref,
                self.level_255_ref, self.level_256_ref, self.level_257_ref,
                self.level_258_ref, self.level_259_ref, self.level_260_ref, self.level_261_ref, self.level_262_ref,
                self.level_263_ref, self.level_264_ref, self.level_265_ref, self.level_266_ref, self.level_267_ref,
                self.level_268_ref, self.level_269_ref, self.level_270_ref, self.level_271_ref, self.level_272_ref,
                self.level_273_ref, self.level_274_ref, self.level_275_ref, self.level_276_ref, self.level_277_ref,
                self.level_278_ref,
                self.level_279_ref, self.level_280_ref, self.level_281_ref, self.level_282_ref, self.level_283_ref,
                self.level_284_ref, self.level_285_ref, self.level_286_ref, self.level_287_ref, self.level_288_ref,
                self.level_289_ref, self.level_290_ref, self.level_291_ref, self.level_292_ref, self.level_293_ref,
                self.level_294_ref, self.level_295_ref, self.level_296_ref, self.level_297_ref, self.level_298_ref,self.level_299_ref,self.level_300_ref,self.level_301_ref,self.level_302_ref,self.level_303_ref,self.level_304_ref,self.level_305_ref,self.level_306_ref,self.level_307_ref,self.level_308_ref,self.level_309_ref,self.level_310_ref,self.level_311_ref,self.level_312_ref,self.level_313_ref,self.level_314_ref,self.level_315_ref,self.level_316_ref,self.level_317_ref,self.level_318_ref,self.level_319_ref,self.level_320_ref,self.level_321_ref,self.level_322_ref,self.level_323_ref,self.level_324_ref,self.level_325_ref,self.level_326_ref,self.level_327_ref,self.level_328_ref,self.level_329_ref,self.level_330_ref,self.level_331_ref,self.level_332_ref,self.level_333_ref,self.level_334_ref,self.level_335_ref,self.level_336_ref,self.level_337_ref,self.level_338_ref,self.level_339_ref,self.level_340_ref,self.level_341_ref,self.level_342_ref,self.level_343_ref,self.level_344_ref,self.level_345_ref,self.level_346_ref,self.level_347_ref,self.level_348_ref,self.level_349_ref,self.level_350_ref,self.level_351_ref,self.level_352_ref,self.level_353_ref,self.level_354_ref,self.level_355_ref,self.level_356_ref,self.level_357_ref,self.level_358_ref,self.level_359_ref,self.level_360_ref,self.level_361_ref,self.level_362_ref,self.level_363_ref,self.level_364_ref,self.level_365_ref,self.level_366_ref,self.level_367_ref,self.level_368_ref,self.level_369_ref,self.level_370_ref,self.level_371_ref,self.level_372_ref,self.level_373_ref,self.level_374_ref,
                self.level_375_ref,self.level_376_ref,self.level_377_ref,self.level_378_ref,self.level_379_ref,self.level_380_ref,self.phase1_complete]
        if self.level == 201:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}  ) and self.ids.change9.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}  ) and self.ids.change4.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2}  ) and self.ids.change14.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 202:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 203:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 204:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change7.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 205:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8, "center_y": .3}  and self.ids.change4.pos_hint == {"center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 206:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}  ) and self.ids.change9.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}  ) and self.ids.change4.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2}  ) and self.ids.change14.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 207:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 208:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change12.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change8.pos_hint == {"center_x": .5, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 209:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change13.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change7.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change4.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .2, "center_y": .1}  ) and self.ids.change8.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .2, "center_y": .1}  ) and self.ids.change5.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .35, "center_y": .2}  ) and self.ids.change12.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .35, "center_y": .2}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 210:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .5, "center_y": .3}  and self.ids.change10.pos_hint == {"center_x": .2, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3},{"center_x": .8, "center_y": .3}  ) and self.ids.change5.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3},{"center_x": .8, "center_y": .3}  ) and self.ids.change9.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3},{"center_x": .8, "center_y": .3}  ) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 211:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change16.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .35, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 212:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 213:
            if self.count in ([i for i in range(3, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 214:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 215:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 216:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .5, "center_y": .3}  and self.ids.change10.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change4.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .65, "center_y": .2} :
                        if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3},{"center_x": .2, "center_y": .2} ) and self.ids.change17.pos_hint in ({"center_x": .2, "center_y": .3},{"center_x": .2, "center_y": .2} ):
                            ret_value = self.levels_random()
                            self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 217:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .5, "center_y": .3}  and self.ids.change4.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change7.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change12.pos_hint == {"center_x": .5, "center_y": .2}:
                        if self.ids.change6.pos_hint in ({"center_x": .2, "center_y": .3},{"center_x": .8, "center_y": .3} ) and self.ids.change9.pos_hint in ({"center_x": .2, "center_y": .3},{"center_x": .8, "center_y": .3} ) and  self.ids.change2.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2} ) and self.ids.change11.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2} ):
                            ret_value = self.levels_random()
                            self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 218:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8, "center_y": .3}:
                    if self.ids.change2.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .35,
                                                                                        "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 219:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 220:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 221:
            if self.count in ([i for i in range(14, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .8, "center_y": .3}  and self.ids.change16.pos_hint == {"center_x": .8, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5, "center_y": .1} and  self.ids.change4.pos_hint == {"center_x": .2, "center_y": .1}:
                    if self.ids.change.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .1}  ) and self.ids.change5.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .1}  ) and self.ids.change12.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .1}  ) and  self.ids.change3.pos_hint in ({"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change6.pos_hint in ({"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change10.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .2}) and   self.ids.change14.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .2}) and   self.ids.change8.pos_hint in ({"center_x": .35, "center_y": .2},{"center_x": .35, "center_y": .1}) and  self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .2},{"center_x": .35, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 222:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .8, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 223:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .5, "center_y": .3}  and self.ids.change4.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change.pos_hint == {"center_x": .5, "center_y": .2}:
                    if self.ids.change2.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .35, "center_y": .2},{"center_x": .65, "center_y": .3}  ) and self.ids.change6.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .35, "center_y": .2},{"center_x": .65, "center_y": .3}  ) and self.ids.change11.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .35, "center_y": .2},{"center_x": .65, "center_y": .3}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 224:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .8, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 225:
            if self.count in ([i for i in range(13, 19)]):
                if self.ids.change.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .8, "center_y": .3}  and self.ids.change8.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .65, "center_y": .2} :
                    if self.ids.change5.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .8, "center_y": .2},{"center_x": .5, "center_y": .1}  ) and self.ids.change6.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .8, "center_y": .2},{"center_x": .5, "center_y": .1}  ) and self.ids.change14.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .8, "center_y": .2},{"center_x": .5, "center_y": .1}  ) and  self.ids.change12.pos_hint in ({"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .3}) and  self.ids.change17.pos_hint in ({"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .3}) and  self.ids.change1.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .5, "center_y": .2}) and   self.ids.change13.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .5, "center_y": .2}) and   self.ids.change7.pos_hint in ({"center_x": .2, "center_y": .1},{"center_x": .35, "center_y": .1}) and  self.ids.change9.pos_hint in ({"center_x": .2, "center_y": .1},{"center_x": .35, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 226:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 227:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .35, "center_y": .3}  and self.ids.change4.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change5.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change8.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change2.pos_hint in ({"center_x": .8, "center_y": .3},{"center_x": .35, "center_y": .2}  ) and self.ids.change11.pos_hint in ({"center_x": .8, "center_y": .3},{"center_x": .35, "center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 228:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .35, "center_y": .3}  and self.ids.change4.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change5.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change8.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change2.pos_hint in ({"center_x": .8, "center_y": .3},{"center_x": .35, "center_y": .2}  ) and self.ids.change11.pos_hint in ({"center_x": .8, "center_y": .3},{"center_x": .35, "center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 229:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 230:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 231:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .5, "center_y": .2}:
                    if self.ids.change5.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2},{"center_x": .35, "center_y": .2}) and  self.ids.change6.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2},{"center_x": .35, "center_y": .2}) and  self.ids.change14.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2},{"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 232:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .35, "center_y": .3}  and self.ids.change4.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change5.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change8.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change2.pos_hint in ({"center_x": .8, "center_y": .3},{"center_x": .35, "center_y": .2}  ) and self.ids.change11.pos_hint in ({"center_x": .8, "center_y": .3},{"center_x": .35, "center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 233:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3}  and self.ids.change2.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change14.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .8, "center_y": .2}  ) and self.ids.change17.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .8, "center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 234:
            if self.count in ([i for i in range(13, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .5, "center_y": .3}  and self.ids.change2.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .8, "center_y": .2} and  self.ids.change14.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change4.pos_hint == {"center_x": .35, "center_y": .1} and self.ids.change9.pos_hint == {"center_x": .5, "center_y": .1} :

                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}  ) and self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3})  and  self.ids.change11.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change8.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change5.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2}) and  self.ids.change12.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 235:
            if self.count in ([i for i in range(13, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .5, "center_y": .3}  and self.ids.change2.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .8, "center_y": .2} and  self.ids.change14.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change4.pos_hint == {"center_x": .35, "center_y": .1} and self.ids.change9.pos_hint == {"center_x": .5, "center_y": .1} :

                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}  ) and self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3})  and  self.ids.change11.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change8.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change5.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2}) and  self.ids.change12.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 236:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change16.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .35, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 237:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change10.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} :
                    if  self.ids.change4.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3} ) and self.ids.change6.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 238:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2} :
                    if self.ids.change.pos_hint in ( {"center_x": .5, "center_y": .3} ,{"center_x": .35, "center_y": .2} ) and  self.ids.change17.pos_hint in ( {"center_x": .5, "center_y": .3} ,{"center_x": .35, "center_y": .2} ) and  self.ids.change7.pos_hint in ( {"center_x": .65, "center_y": .3} ,{"center_x": .5, "center_y": .2} ) and self.ids.change15.pos_hint in ( {"center_x": .65, "center_y": .3} ,{"center_x": .5, "center_y": .2} ) and self.ids.change5.pos_hint in ( {"center_x": .8, "center_y": .3} ,{"center_x": .65, "center_y": .2} ) and self.ids.change12.pos_hint in ( {"center_x": .8, "center_y": .3} ,{"center_x": .65, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 239:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 240:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3}  and self.ids.change11.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change4.pos_hint == {"center_x": .5, "center_y": .2}:
                    if self.ids.change.pos_hint in ( {"center_x": .5, "center_y": .3} ,{"center_x": .8, "center_y": .2} ) and  self.ids.change17.pos_hint in ( {"center_x": .5, "center_y": .3} ,{"center_x": .8, "center_y": .2} ) and  self.ids.change12.pos_hint in ( {"center_x": .65, "center_y": .3} ,{"center_x": .65, "center_y": .2} ) and self.ids.change5.pos_hint in ( {"center_x": .65, "center_y": .3} ,{"center_x": .65, "center_y": .2} ) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 241:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3}  and self.ids.change4.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change1.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3} ,{"center_x": .8, "center_y": .3} ) and  self.ids.change17.pos_hint in ( {"center_x": .35, "center_y": .3} ,{"center_x": .8, "center_y": .3} ) and  self.ids.change5.pos_hint in ( {"center_x": .2, "center_y": .2} ,{"center_x": .35, "center_y": .2} ) and self.ids.change12.pos_hint in ( {"center_x": .2, "center_y": .2} ,{"center_x": .35, "center_y": .2} ) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 242:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3}  and self.ids.change.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change11.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change2.pos_hint in ( {"center_x": .8, "center_y": .3} ,{"center_x": .2, "center_y": .2} ) and  self.ids.change12.pos_hint in ( {"center_x": .8, "center_y": .3} ,{"center_x": .2, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 243:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3}  and self.ids.change.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change11.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change2.pos_hint in ( {"center_x": .8, "center_y": .3} ,{"center_x": .2, "center_y": .2} ) and  self.ids.change12.pos_hint in ( {"center_x": .8, "center_y": .3} ,{"center_x": .2, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 244:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .8,
                                                                                      "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change3.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .2,
                                                                                        "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 245:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .8, "center_y": .3}:
                    if self.ids.change.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,
                                                                                        "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 246:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3}  and self.ids.change.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change11.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change2.pos_hint in ( {"center_x": .8, "center_y": .3} ,{"center_x": .2, "center_y": .2} ) and  self.ids.change12.pos_hint in ( {"center_x": .8, "center_y": .3} ,{"center_x": .2, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 247:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .8,
                                                                                      "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change3.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .2,
                                                                                        "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 248:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .8,
                                                                                      "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change3.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .2,
                                                                                        "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 249:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .2}:
                    if self.ids.change5.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .5,
                                                                                        "center_y": .2}) and self.ids.change14.pos_hint in (
                            {"center_x": .5, "center_y": .3}, {"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 250:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3}  and self.ids.change8.pos_hint == {"center_x": .8, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 251:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3}  and self.ids.change6.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5, "center_y": .2} :
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3},{"center_x": .2, "center_y": .2}) and self.ids.change8.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3},{"center_x": .2, "center_y": .2}) and self.ids.change17.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3},{"center_x": .2, "center_y": .2}) and  self.ids.change2.pos_hint in ( {"center_x": .5, "center_y": .3},{"center_x": .35, "center_y": .2} )and  self.ids.change14.pos_hint in ( {"center_x": .5, "center_y": .3},{"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 252:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3}  and self.ids.change8.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .65, "center_y": .3}  and  self.ids.change.pos_hint == {"center_x": .2, "center_y": .2}  and  self.ids.change17.pos_hint == {"center_x": .35, "center_y": .2} :
                    if   self.ids.change3.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3} )and  self.ids.change12.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)

        elif self.level == 253:
            if self.count in ([i for i in range(3, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 254:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3}:
                    if self.ids.change6.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .2, "center_y": .2}) and  self.ids.change9.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 255:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2}:
                    if self.ids.change5.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .8, "center_y": .3}) and  self.ids.change7.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 256:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} :
                    if self.ids.change5.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}) and  self.ids.change12.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 257:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .5, "center_y": .2} :
                    if self.ids.change12.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .65, "center_y": .3}) and  self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .65, "center_y": .3}) and   self.ids.change7.pos_hint in ( {"center_x": .65, "center_y": .2} , {"center_x": .8, "center_y": .2}) and self.ids.change5.pos_hint in ( {"center_x": .65, "center_y": .2} , {"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 258:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 259:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .8, "center_y": .2} and self.ids.change13.pos_hint == {"center_x": .2,
                                                                                        "center_y": .1} :
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2}) and  self.ids.change5.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2}) and self.ids.change17.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .2}) and  self.ids.change2.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}) and  self.ids.change6.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}) and  self.ids.change12.pos_hint in ( {"center_x": .8, "center_y": .3}, {"center_x": .2, "center_y": .2}) and  self.ids.change11.pos_hint in ( {"center_x": .8, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 260:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3}  and self.ids.change.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 261:
            if self.count in ([i for i in range(3, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 262:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3}  and self.ids.change12.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .8, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 263:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 264:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .65,
                                                                                       "center_y": .2}  :
                    if self.ids.change.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}) and self.ids.change17.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}) and self.ids.change2.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3}) and  self.ids.change14.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3}) and  self.ids.change6.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .5, "center_y": .2}) and  self.ids.change11.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 265:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and  self.ids.change5.pos_hint == {"center_x": .65, "center_y": .3}  and  self.ids.change8.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change14.pos_hint == {"center_x": .35, "center_y": .2}:
                    if self.ids.change6.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .5,
                                                                                        "center_y": .2}) and self.ids.change17.pos_hint in (
                    {"center_x": .2, "center_y": .2}, {"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 266:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and  self.ids.change6.pos_hint == {"center_x": .8, "center_y": .3}:
                    if self.ids.change13.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .2}) and  self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 267:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .2}, {"center_x": .5,
                                                                                        "center_y": .2}) and self.ids.change11.pos_hint in (
                            {"center_x": .35, "center_y": .2}, {"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 268:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 269:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 270:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change4.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2} and self.ids.change1.pos_hint == {
                    "center_x": .65, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .8, "center_y": .2} :

                    if self.ids.change12.pos_hint in ({"center_x": .5, "center_y": .2}, {"center_x": .2,
                                                                                        "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1}) and self.ids.change.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,"center_y": .2},{"center_x": .35, "center_y": .1}) and  self.ids.change5.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,"center_y": .2},{"center_x": .35, "center_y": .1}) and  self.ids.change9.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,"center_y": .2},{"center_x": .35, "center_y": .1}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 271:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change4.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2} and self.ids.change1.pos_hint == {
                    "center_x": .65, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .8, "center_y": .2} :

                    if self.ids.change12.pos_hint in ({"center_x": .5, "center_y": .2}, {"center_x": .2,
                                                                                        "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1}) and self.ids.change.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,"center_y": .2},{"center_x": .35, "center_y": .1}) and  self.ids.change5.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,"center_y": .2},{"center_x": .35, "center_y": .1}) and  self.ids.change9.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,"center_y": .2},{"center_x": .35, "center_y": .1}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 272:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} :
                    if  self.ids.change3.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3}) and self.ids.change12.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 273:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} :
                    if  self.ids.change3.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3}) and self.ids.change12.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level ==274:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change13.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .2, "center_y": .2}:
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level ==275:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change8.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change17.pos_hint == {"center_x": .35, "center_y": .2}:
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 276:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3}  and self.ids.change12.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .8, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 277:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change16.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .35, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 278:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .2, "center_y": .2} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 279:
            if self.count in ([i for i in range(3, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .35, "center_y": .3} :
                    if  self.ids.change2.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .3}) and self.ids.change8.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 280:
            if self.count in ([i for i in range(3, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .35, "center_y": .3} :
                    if  self.ids.change2.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .3}) and self.ids.change8.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 281:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2} and self.ids.change8.pos_hint == {
                    "center_x": .8, "center_y": .2} :
                    if self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2}) and self.ids.change16.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2}) and self.ids.change6.pos_hint in ( {"center_x": .35, "center_y": .2}, {"center_x": .5, "center_y": .2}) and self.ids.change7.pos_hint in ( {"center_x": .35, "center_y": .2}, {"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 282:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2} and self.ids.change8.pos_hint == {
                    "center_x": .8, "center_y": .2} :
                    if self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2}) and self.ids.change16.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2}) and self.ids.change6.pos_hint in ( {"center_x": .35, "center_y": .2}, {"center_x": .5, "center_y": .2}) and self.ids.change7.pos_hint in ( {"center_x": .35, "center_y": .2}, {"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 283:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .2, "center_y": .2} and  self.ids.change11.pos_hint == {"center_x": .35, "center_y": .2} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 284:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .8,
                                                                                      "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change3.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .2,
                                                                                        "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 285:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .35,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change9.pos_hint in ({"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1},
                                                     {"center_x": .35,
                                                      "center_y": .1}) and self.ids.change12.pos_hint in (
                            {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1},
                            {"center_x": .35, "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1},
                            {"center_x": .35, "center_y": .1}) and self.ids.change.pos_hint in (
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change5.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 286:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change16.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .2,
                                                                                     "center_y": .2} and self.ids.change7.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2} and self.ids.change1.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change15.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .8,
                                                                                          "center_y": .2}) and self.ids.change14.pos_hint in (
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change9.pos_hint in (
                            {"center_x": .8, "center_y": .3},
                            {"center_x": .2, "center_y": .1}) and self.ids.change12.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 287:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change7.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .2,
                                                                                     "center_y": .2} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .8,
                                                                                        "center_y": .2} and self.ids.change11.pos_hint ==  {"center_x": .2, "center_y": .1}:
                    if self.ids.change5.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .5,
                                                                                          "center_y": .2}) and self.ids.change13.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .5, "center_y": .2}) and self.ids.change.pos_hint in (
                            {"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) and self.ids.change9.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 288:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change7.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .2,
                                                                                     "center_y": .2} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .8,
                                                                                        "center_y": .2} and self.ids.change11.pos_hint ==  {"center_x": .2, "center_y": .1}:
                    if self.ids.change5.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .5,
                                                                                          "center_y": .2}) and self.ids.change13.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .5, "center_y": .2}) and self.ids.change.pos_hint in (
                            {"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) and self.ids.change9.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 289:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()

                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 290:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()

                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 291:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .8, "center_y": .3}:
                    if  self.ids.change6.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2}) and self.ids.change11.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 292:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .8, "center_y": .3}:
                    if  self.ids.change6.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2}) and self.ids.change11.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 293:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .8, "center_y": .3}:
                    if  self.ids.change6.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2}) and self.ids.change11.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 294:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .8, "center_y": .3}:
                    ret_value = self.levels_random()

                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 295:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} :
                    if  self.ids.change3.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .35, "center_y": .2}) and self.ids.change7.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .35, "center_y": .2}) and self.ids.change11.pos_hint in ( {"center_x": .8, "center_y": .3},{"center_x": .2, "center_y": .2}) and self.ids.change15.pos_hint in ( {"center_x": .8, "center_y": .3},{"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 296:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                      "center_y": .2} and self.ids.change11.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .35,
                                                                                          "center_y": .2}) and self.ids.change9.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 297:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8, "center_y": .3}:
                    ret_value = self.levels_random()

                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 298:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .8, "center_y": .3}:
                    ret_value = self.levels_random()

                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 299:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8, "center_y": .3}:
                    ret_value = self.levels_random()

                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 300:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} :
                    if  self.ids.change.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .3}) and self.ids.change4.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 301:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3}:
                    if self.ids.change11.pos_hint in ({"center_x": .35, "center_y": .3},
                                                    {"center_x": .8, "center_y": .3}) and self.ids.change15.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 302:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .2, "center_y": .2}:
                    if self.ids.change2.pos_hint in ({"center_x": .35, "center_y": .3},
                                                    {"center_x": .65, "center_y": .3}) and self.ids.change16.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 303:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8, "center_y": .3}:
                    ret_value = self.levels_random()

                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 304:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change1.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change7.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change6.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}) and self.ids.change11.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 305:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .8,
                    "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change4.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65,
                             "center_y": .3}) and self.ids.change11.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change2.pos_hint in (
                            {"center_x": .5, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change9.pos_hint in (
                            {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 306:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and  self.ids.change13.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change16.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change8.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change5.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change2.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .35, "center_y": .2} ) and self.ids.change6.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .35, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 307:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .35,
                                                                                        "center_y": .2}:
                    if self.ids.change6.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .2, "center_y": .2} ) and self.ids.change11.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .2, "center_y": .2} ) and  self.ids.change2.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .2, "center_y": .1} ) and  self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .2, "center_y": .1} ) and  self.ids.change10.pos_hint in ( {"center_x": .8, "center_y": .3} , {"center_x": .8, "center_y": .2} ) and  self.ids.change12.pos_hint in ( {"center_x": .8, "center_y": .3} , {"center_x": .8, "center_y": .2} ) and  self.ids.change1.pos_hint in ( {"center_x": .5, "center_y": .2} , {"center_x": .65, "center_y": .2} ) and  self.ids.change7.pos_hint in ( {"center_x": .5, "center_y": .2} , {"center_x": .65, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 308:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .35,
                                                                                        "center_y": .2}:
                    if self.ids.change6.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .2, "center_y": .2} ) and self.ids.change11.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .2, "center_y": .2} ) and  self.ids.change2.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .2, "center_y": .1} ) and  self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .2, "center_y": .1} ) and  self.ids.change10.pos_hint in ( {"center_x": .8, "center_y": .3} , {"center_x": .8, "center_y": .2} ) and  self.ids.change12.pos_hint in ( {"center_x": .8, "center_y": .3} , {"center_x": .8, "center_y": .2} ) and  self.ids.change1.pos_hint in ( {"center_x": .5, "center_y": .2} , {"center_x": .65, "center_y": .2} ) and  self.ids.change7.pos_hint in ( {"center_x": .5, "center_y": .2} , {"center_x": .65, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 309:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .8,
                                                                                      "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change3.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .2,
                                                                                        "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 310:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3}:
                    if self.ids.change8.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .8, "center_y": .3} ) and self.ids.change14.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .8, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 311:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .2, "center_y": .2}:
                    if self.ids.change5.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change16.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 312:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change12.pos_hint == {"center_x": .35, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 313:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change7.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .2,
                                                                                     "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .5,
                                                                                       "center_y": .2} and self.ids.change12.pos_hint == {
                    "center_x": .2, "center_y": .1}:
                    if self.ids.change17.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,
                                                                                          "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .65, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change9.pos_hint in (
                            {"center_x": .8, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change13.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 314:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()

                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 315:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .2, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .65,
                                                                                       "center_y": .3}) and self.ids.change8.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 316:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()

                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 317:
            if self.count in ([i for i in range(4, 19)]):
                if   self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} :
                    if self.ids.change6.pos_hint in ( {"center_x": .2, "center_y": .3} ,{"center_x": .65, "center_y": .3}) and  self.ids.change16.pos_hint in ( {"center_x": .2, "center_y": .3} ,{"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 318:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change16.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .35, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 319:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 320:
            if self.count in ([i for i in range(4, 19)]):
                if   self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} :
                    if self.ids.change6.pos_hint in ( {"center_x": .2, "center_y": .3} ,{"center_x": .65, "center_y": .3}) and  self.ids.change16.pos_hint in ( {"center_x": .2, "center_y": .3} ,{"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 321:
            if self.count in ([i for i in range(4, 19)]):
                if   self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .35,
                                                                                        "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .8, "center_y": .3}:
                    if self.ids.change5.pos_hint in ( {"center_x": .5, "center_y": .3} ,{"center_x": .2, "center_y": .2}) and  self.ids.change8.pos_hint in ( {"center_x": .5, "center_y": .3} ,{"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 322:
            if self.count in ([i for i in range(15, 19)]):
                if self.ids.change13.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change11.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change7.pos_hint == {"center_x": .8,
                                                                                      "center_y": .2}:
                    if self.ids.change.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change1.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change4.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change9.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},
                            {"center_x": .35, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .35, "center_y": .1}) and self.ids.change10.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .35, "center_y": .1}) and self.ids.change12.pos_hint in (
                            {"center_x": .65, "center_y": .1},
                            {"center_x": .8, "center_y": .1}) and self.ids.change16.pos_hint in (
                            {"center_x": .65, "center_y": .1},
                            {"center_x": .8, "center_y": .1}) and self.ids.change14.pos_hint in (
                            {"center_x": .65, "center_y": .2},
                            {"center_x": .5, "center_y": .1}) and self.ids.change2.pos_hint in (
                            {"center_x": .65, "center_y": .2}, {"center_x": .5, "center_y": .1}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 323:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 324:
            if self.count in ([i for i in range(6, 19)]):
                if   self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .8, "center_y": .3}:
                    if self.ids.change6.pos_hint in ( {"center_x": .35, "center_y": .3} ,{"center_x": .2, "center_y": .2}) and  self.ids.change11.pos_hint in ( {"center_x": .35, "center_y": .3} ,{"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 325:
            if self.count in ([i for i in range(10, 19)]):
                if   self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change12.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change2.pos_hint in ( {"center_x": .35, "center_y": .3} ,{"center_x": .2, "center_y": .2}) and  self.ids.change14.pos_hint in ( {"center_x": .35, "center_y": .3} ,{"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 326:
            if self.count in ([i for i in range(13, 19)]):
                if   self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change9.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .8, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change13.pos_hint == {"center_x": .35, "center_y": .1} and self.ids.change15.pos_hint == {"center_x": .5, "center_y": .1}:
                    if self.ids.change8.pos_hint in ( {"center_x": .35, "center_y": .3} ,{"center_x": .65, "center_y": .2}) and  self.ids.change16.pos_hint in ( {"center_x": .35, "center_y": .3} ,{"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 327:
            if self.count in ([i for i in range(13, 19)]):
                if   self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change9.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .8, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change13.pos_hint == {"center_x": .35, "center_y": .1} and self.ids.change15.pos_hint == {"center_x": .5, "center_y": .1}:
                    if self.ids.change8.pos_hint in ( {"center_x": .35, "center_y": .3} ,{"center_x": .65, "center_y": .2}) and  self.ids.change16.pos_hint in ( {"center_x": .35, "center_y": .3} ,{"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 328:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3}  and self.ids.change7.pos_hint == {"center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 329:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2} and self.ids.change13.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .65,
                                                                                       "center_y": .2}  and self.ids.change12.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change6.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2} ) and self.ids.change2.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2} ) and self.ids.change10.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3} ) and  self.ids.change14.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 330:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .8,
                                                                                       "center_y": .2} :
                    if self.ids.change1.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .1} ) and self.ids.change4.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .1} ) and self.ids.change8.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2} ) and  self.ids.change10.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2} ) and  self.ids.change12.pos_hint in ( {"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .1} ) and   self.ids.change17.pos_hint in ( {"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .1} ) and   self.ids.change.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .8, "center_y": .3} ,{"center_x": .35, "center_y": .2}) and  self.ids.change5.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .8, "center_y": .3} ,{"center_x": .35, "center_y": .2}) and  self.ids.change3.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .8, "center_y": .3} ,{"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 331:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .2} :
                    if self.ids.change5.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .5, "center_y": .2} ) and self.ids.change7.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .5, "center_y": .2} ) and self.ids.change11.pos_hint in ( {"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .2} ) and  self.ids.change8.pos_hint in ( {"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .2} ) and  self.ids.change.pos_hint in ( {"center_x": .8, "center_y": .2}, {"center_x": .2, "center_y": .1} ) and   self.ids.change3.pos_hint in ( {"center_x": .8, "center_y": .2}, {"center_x": .2, "center_y": .1} ) and   self.ids.change6.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3} ,{"center_x": .8, "center_y": .3}) and  self.ids.change13.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3} ,{"center_x": .8, "center_y": .3}) and  self.ids.change15.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3} ,{"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 332:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change1.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change7.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change6.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}) and self.ids.change11.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 333:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .2, "center_y": .1}:
                    if self.ids.change.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2} ) and self.ids.change14.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2} ) and self.ids.change2.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .2} ) and  self.ids.change6.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .2} ) and  self.ids.change9.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .5, "center_y": .2} ) and   self.ids.change15.pos_hint in (  {"center_x": .5, "center_y": .3}, {"center_x": .5, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 334:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .2} and self.ids.change15.pos_hint == {
                    "center_x": .65, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .8,
                                                                                       "center_y": .2} and self.ids.change8.pos_hint == {
                    "center_x": .2, "center_y": .1}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .2,
                                                                                       "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 335:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .2} :
                    if self.ids.change6.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .8,
                                                                                       "center_y": .3}) and self.ids.change16.pos_hint in (
                            {"center_x": .65, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 336:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .35, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 337:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2} :
                    if self.ids.change.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .8,
                                                                                       "center_y": .3}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 338:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .8,
                                                                                       "center_y": .2} :
                    if self.ids.change1.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .5,"center_y": .2}) and self.ids.change16.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2}) and  self.ids.change11.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,"center_y": .2}) and  self.ids.change4.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,"center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 339:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 340:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 341:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .2} :
                    if self.ids.change6.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .8,
                                                                                       "center_y": .3}) and self.ids.change16.pos_hint in (
                            {"center_x": .65, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 342:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3}  and self.ids.change15.pos_hint == {"center_x": .8, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 343:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .35,
                    "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .2} and self.ids.change16.pos_hint == {
                    "center_x": .65, "center_y": .2}  and  self.ids.change8.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change12.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,
                                                                                       "center_y": .3}) and self.ids.change9.pos_hint in (
                            {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 344:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .35,
                    "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .5,
                                                                                       "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .2}  and  self.ids.change8.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change5.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,
                                                                                       "center_y": .3}) and self.ids.change12.pos_hint in (
                            {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 345:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .65,
                    "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .8, "center_y": .3} :
                    if self.ids.change5.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2}) and self.ids.change6.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2}) and  self.ids.change15.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2}) and  self.ids.change12.pos_hint in ({"center_x": .35, "center_y": .2}, {"center_x": .5, "center_y": .2}) and  self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .2}, {"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 346:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .35,
                    "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5, "center_y": .3}  and self.ids.change4.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5, "center_y": .2}:
                    if self.ids.change14.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .65, "center_y": .2}) and self.ids.change15.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .65, "center_y": .2}) and  self.ids.change6.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .2}) and  self.ids.change11.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .2}) and  self.ids.change9.pos_hint in ({"center_x": .8, "center_y": .2}, {"center_x": .2, "center_y": .1}) and  self.ids.change17.pos_hint in ({"center_x": .8, "center_y": .2}, {"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 347:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change3.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change5.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .2, "center_y": .1}) and  self.ids.change15.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .2, "center_y": .1}) and  self.ids.change11.pos_hint in ( {"center_x": .35, "center_y": .2},{"center_x": .8, "center_y": .2}) and  self.ids.change1.pos_hint in ( {"center_x": .35, "center_y": .2},{"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 348:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 349:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 350:
            if self.count in ([i for i in range(13, 19)]):
                if self.ids.change4.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change17.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .8, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change8.pos_hint == {"center_x": .35, "center_y": .1} and self.ids.change16.pos_hint == {"center_x": .5, "center_y": .1}:
                    if self.ids.change5.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2},{"center_x": .8,"center_y": .3}) and self.ids.change12.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2},{"center_x": .8,"center_y": .3}) and self.ids.change15.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2},{"center_x": .8,"center_y": .3}) :
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 351:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .5, "center_y": .3} :
                    if  self.ids.change11.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3}) and  self.ids.change14.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 352:
            if self.count in ([i for i in range(13, 19)]):
                if self.ids.change4.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change17.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .8, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change8.pos_hint == {"center_x": .35, "center_y": .1} and self.ids.change16.pos_hint == {"center_x": .5, "center_y": .1}:
                    if self.ids.change5.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2},{"center_x": .8,"center_y": .3}) and self.ids.change12.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2},{"center_x": .8,"center_y": .3}) and self.ids.change15.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2},{"center_x": .8,"center_y": .3}) :
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 353:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .5, "center_y": .3} and  self.ids.change14.pos_hint == {"center_x": .65, "center_y": .3} :
                    if  self.ids.change3.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}) and  self.ids.change10.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}) and  self.ids.change1.pos_hint in ( {"center_x": .2, "center_y": .2},{"center_x": .35, "center_y": .2}) and  self.ids.change17.pos_hint in ( {"center_x": .2, "center_y": .2},{"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 354:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .35, "center_y": .3} and  self.ids.change7.pos_hint == {"center_x": .5, "center_y": .3}  and self.ids.change14.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .8, "center_y": .3}:
                    if  self.ids.change11.pos_hint in ( {"center_x": .2, "center_y": .2},{"center_x": .35, "center_y": .2}) and  self.ids.change.pos_hint in ( {"center_x": .2, "center_y": .2},{"center_x": .35, "center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 355:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 356:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 357:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 358:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 359:
            self.question_1_winning_popup(para=self.level_360_ref)
            # if self.count in ([i for i in range(12, 19)]):
            #     print('vvvvvvvvvvvvvv')
            #
            #
            #     if self.ids.change4.pos_hint == {"center_x": 65, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .65,"center_y": .2} and self.ids.change15.pos_hint == {
            #         "center_x": .8, "center_y": .2} and self.ids.change8.pos_hint == {"center_x": .35, "center_y": .1}:
            #
            #         print('sdd')
            #         if self.ids.change6.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .2},{"center_x": .8,"center_y": .3},{"center_x": .2,"center_y": .1}) and self.ids.change17.pos_hint in (
            #                {"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .2},{"center_x": .8,"center_y": .3},{"center_x": .2,"center_y": .1}) and self.ids.change16.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .2},{"center_x": .8,"center_y": .3},{"center_x": .2,"center_y": .1}) and  self.ids.change14.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .2},{"center_x": .8,"center_y": .3},{"center_x": .2,"center_y": .1}) and  self.ids.change5.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .2}) and  self.ids.change10.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .2}) and  self.ids.change.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .2, "center_y": .2}) and  self.ids.change7.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .2, "center_y": .2}):
            #
            #             self.question_1_winning_popup(para=self.level_360_ref)
            #         else:
            #             Clock.schedule_once(self.coin_10_loosing)
            #     else:
            #         Clock.schedule_once(self.coin_10_loosing)
            # else:
            #     print('NOTHING')
            #     Clock.schedule_once(self.coin_10_loosing)
            #
            # print(self.count)
            # self.count = 0
            # print(self.count)
        elif self.level == 360:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} :
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .5,
                                                                                         "center_y": .3}) and self.ids.change17.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 361:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3}  and  self.ids.change6.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change8.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change2.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change14.pos_hint == {"center_x": .65, "center_y": .2} and  self.ids.change11.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .35,
                                                                                         "center_y": .2}) and self.ids.change10.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 362:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change11.pos_hint == {
                    "center_x": .5, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 363:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .8,
                                                                                      "center_y": .2} :
                    if self.ids.change1.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .2} ) and  self.ids.change17.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .2} ) and  self.ids.change12.pos_hint in ( {"center_x": .2, "center_y": .1},{"center_x": .5, "center_y": .3} ) and self.ids.change16.pos_hint in ( {"center_x": .2, "center_y": .1},{"center_x": .5, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 364:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3}:
                    if self.ids.change9.pos_hint in ( {"center_x": .2, "center_y": .2},{"center_x": .35, "center_y": .2} ) and  self.ids.change11.pos_hint in ( {"center_x": .2, "center_y": .2},{"center_x": .35, "center_y": .2} ) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 365:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change13.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2}:
                    if self.ids.change6.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,
                                                                                        "center_y": .3}) and self.ids.change8.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change1.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change3.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change5.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 366:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .2, "center_y": .2} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 367:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .8,
                                                                                      "center_y": .2} :
                    if self.ids.change1.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .2} ) and  self.ids.change17.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .2} ) and  self.ids.change12.pos_hint in ( {"center_x": .2, "center_y": .1},{"center_x": .5, "center_y": .3} ) and self.ids.change16.pos_hint in ( {"center_x": .2, "center_y": .1},{"center_x": .5, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 368:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                       "center_y": .2} and self.ids.change7.pos_hint == {
                    "center_x": .65, "center_y": .2} and self.ids.change4.pos_hint == {"center_x": .8,
                                                                                      "center_y": .2}  and  self.ids.change11.pos_hint == {"center_x": .35, "center_y": .1}:
                    if self.ids.change16.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .35, "center_y": .2} ) and  self.ids.change2.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .35, "center_y": .2} ) and  self.ids.change5.pos_hint in ( {"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .1} ) and self.ids.change1.pos_hint in ( {"center_x": .2, "center_y": .1},{"center_x": .5, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 369:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
        elif self.level == 370:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} :
                    if self.ids.change2.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .2, "center_y": .2}  ) and self.ids.change8.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .2, "center_y": .2}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
        elif self.level == 371:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3}  and self.ids.change.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .5, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
        elif self.level == 372:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3}  and self.ids.change.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .5, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
        elif self.level == 373:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
        elif self.level == 374:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
        elif self.level == 375:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 376:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                       "center_y": .2}  and self.ids.change11.pos_hint == {"center_x": .8, "center_y": .2} and self.ids.change13.pos_hint == {"center_x": .2, "center_y": .1}:
                    if self.ids.change3.pos_hint in ( {"center_x": .5, "center_y": .3},{"center_x": .65, "center_y": .2}  ) and self.ids.change6.pos_hint in ( {"center_x": .5, "center_y": .3},{"center_x": .65, "center_y": .2}  ) and self.ids.change12.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .35, "center_y": .2}  ) and  self.ids.change15.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .35, "center_y": .2}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
        elif self.level == 377:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2}  :
                    if self.ids.change3.pos_hint in ( {"center_x": .8, "center_y": .3},{"center_x": .35, "center_y": .2}  ) and self.ids.change12.pos_hint in ( {"center_x": .8, "center_y": .3},{"center_x": .35, "center_y": .2}  ) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
        elif self.level == 378:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change17.pos_hint == {"center_x": .65,
                                                                                       "center_y": .2}  and self.ids.change.pos_hint == {"center_x": .8, "center_y": .2}:
                    print("ff")
                    if self.ids.change4.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}  ) and self.ids.change6.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}  ) and self.ids.change13.pos_hint in ( {"center_x": .2, "center_y": .2},{"center_x": .35, "center_y": .2}  ) and  self.ids.change5.pos_hint in ( {"center_x": .2, "center_y": .2},{"center_x": .35, "center_y": .2}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
        elif self.level == 379:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)



class phase_4(Screen,phase4_level.phase4_questions, coin_logic.coin_logic_18, retrewingdata.retrew_data_json,
              winingfile.winninggame,coinmovement.movement):
    def __init__(self, **kwargs):
        super(phase_4, self).__init__(**kwargs)
        retrewingdata.retrew_data_json.__init__(self, filename="phase4.json")
        retrewingdata.retrew_data_json.getting_items(self)
        self.coin_js = JsonStore("coins_win.json")
        self.iqjs = JsonStore("iq_score.json")
        self.hint_count = 0
        self.ids.coins.text = str(self.coin_js.get("coin_base")["coins"])
        self.ids.iq.text = str(self.iqjs.get("iq_score")["score"])

    def levels_random(self):


        js = JsonStore("randomliststorage3.json")
        l = js.get("random_level_list")["levels"]
        if l != []:
            ran = random.choice(l)
            print(ran)
            l.remove(ran)


            js.put("random_level_list", levels=l)


            return  ran
        else:
            return 199
    def phase1_complete(self, *args):
        self.phase_complete = Popup()
        self.phase_complete.title = "Phase 4"
        self.phase_complete.title_align = "center"
        self.phase_complete.title_size = '35sp'
        self.phase_complete.separator_height = dp(0)
        self.phase_complete.background_color = (79 / 255, 150 / 255, 220 / 255)
        self.lay = BoxLayout()
        self.lay.orientation = "vertical"
        self.lab = Label()
        self.lab.text = "Completed"
        self.lab.color = "red"
        self.lab.font_size = "30sp"
        self.lay.add_widget(self.lab)
        self.phase_complete.add_widget(self.lay)
        self.phase_complete.size_hint = 1, 1
        self.phase_complete.open()
    def level1_hint(self):

            self.hint = Popup()
            self.hint.title = "Hint"
            self.hint.title_align = "center"
            self.hint.size_hint = .9,.2


            self.hint.separator_height = dp(0)
            self.hint.background_color = (100 / 255, 100 / 255, 100 / 255)
            self.layout = BoxLayout()
            self.layout.size_hint = 1,1
            self.button_coin = Button()
            self.button_free = Button()
            self.button_coin.text = "3coins"
            self.button_coin.bind(on_press = self.hint_coin)
            self.button_coin.size_hint = 1,.6
            self.button_coin.padding_x = .2
            self.button_coin.pos_hint = {"center_x":.1,"center_y":.55}
            self.button_coin.background_color = "red"
            self.layout.add_widget(self.button_coin)
            self.button_free.text = "Free add"
            self.button_free.size_hint = 1,.6
            self.button_free.padding_x = .2
            self.button_free.pos_hint = {"center_x": .1, "center_y": .55}
            self.button_free.background_color = "red"
            self.layout.add_widget(self.button_free)
            self.hint.add_widget(self.layout)
            print(self.count)
            self.hint.open()




    def hint_coin(self,*args):
        self.hint_count += 1
        print(self.hint_count)
        self.h = Popup()
        self.h.title = ""
        self.h.separator_height = dp(0)
        self.h.size_hint = .8, .2
        self.h.title = "Here is your Hint"
        self.h.title_align = "center"
        self.h.background_color = "green"
        self.lab= Label(text = "",pos_hint= {"center_x":5,"center_y":.7},bold = True)
        self.h.content = self.lab
        allhint.hint_all.hint_phase1(self)

        self.h.bind(on_touch_down = (self.kv))
        self.h.open()

        self.hint.dismiss()


    def kv(self,*args):
        self.h.dismiss()
    def winning(self):
        list = [self.level_401_ref, self.level_402_ref, self.level_403_ref, self.level_404_ref,
                self.level_405_ref, self.level_406_ref, self.level_407_ref, self.level_408_ref, self.level_409_ref,
                self.level_410_ref, self.level_411_ref, self.level_412_ref, self.level_413_ref, self.level_414_ref,
                self.level_415_ref, self.level_416_ref, self.level_417_ref, self.level_418_ref, self.level_419_ref,
                self.level_420_ref, self.level_421_ref, self.level_422_ref, self.level_423_ref, self.level_424_ref,
                self.level_425_ref, self.level_426_ref, self.level_427_ref, self.level_428_ref, self.level_429_ref,
                self.level_430_ref, self.level_431_ref, self.level_432_ref, self.level_433_ref, self.level_434_ref,
                self.level_435_ref, self.level_436_ref, self.level_437_ref, self.level_438_ref,
                self.level_439_ref, self.level_440_ref, self.level_441_ref, self.level_442_ref, self.level_443_ref,
                self.level_444_ref, self.level_445_ref, self.level_446_ref, self.level_447_ref, self.level_448_ref,
                self.level_449_ref, self.level_450_ref, self.level_451_ref, self.level_452_ref, self.level_453_ref,
                self.level_454_ref, self.level_455_ref, self.level_456_ref,
                self.level_457_ref, self.level_458_ref, self.level_459_ref, self.level_460_ref, self.level_461_ref,
                self.level_462_ref, self.level_463_ref, self.level_464_ref, self.level_465_ref, self.level_466_ref,
                self.level_467_ref, self.level_468_ref, self.level_469_ref, self.level_470_ref, self.level_471_ref,
                self.level_472_ref, self.level_473_ref, self.level_474_ref, self.level_475_ref, self.level_476_ref,
                self.level_477_ref,
                self.level_478_ref, self.level_479_ref, self.level_480_ref, self.level_481_ref, self.level_482_ref,
                self.level_483_ref, self.level_484_ref, self.level_485_ref, self.level_486_ref, self.level_487_ref,
                self.level_488_ref, self.level_489_ref, self.level_490_ref, self.level_491_ref, self.level_492_ref,
                self.level_493_ref, self.level_494_ref, self.level_495_ref, self.level_496_ref, self.level_497_ref,
                self.level_498_ref, self.level_499_ref, self.level_500_ref, self.level_501_ref, self.level_502_ref,
                self.level_503_ref, self.level_504_ref, self.level_505_ref, self.level_506_ref, self.level_507_ref,
                self.level_508_ref, self.level_509_ref, self.level_510_ref, self.level_511_ref, self.level_512_ref,
                self.level_513_ref, self.level_514_ref, self.level_515_ref, self.level_516_ref, self.level_517_ref,
                self.level_518_ref, self.level_519_ref, self.level_520_ref, self.level_521_ref, self.level_522_ref,
                self.level_523_ref, self.level_524_ref, self.level_525_ref, self.level_526_ref, self.level_527_ref,
                self.level_528_ref, self.level_529_ref, self.level_530_ref, self.level_531_ref, self.level_532_ref,
                self.level_533_ref, self.level_534_ref, self.level_535_ref, self.level_536_ref, self.level_537_ref,
                self.level_538_ref, self.level_539_ref, self.level_540_ref, self.level_541_ref, self.level_542_ref,
                self.level_543_ref, self.level_544_ref, self.level_545_ref, self.level_546_ref, self.level_547_ref,
                self.level_548_ref, self.level_549_ref, self.level_550_ref, self.level_551_ref, self.level_552_ref,
                self.level_553_ref, self.level_554_ref, self.level_555_ref, self.level_556_ref, self.level_557_ref,
                self.level_558_ref, self.level_559_ref, self.level_560_ref, self.level_561_ref, self.level_562_ref,
                self.level_563_ref, self.level_564_ref, self.level_565_ref, self.level_566_ref, self.level_567_ref,
                self.level_568_ref, self.level_569_ref, self.level_570_ref, self.level_571_ref, self.level_572_ref,
                self.level_573_ref,
                self.level_574_ref, self.level_575_ref, self.level_576_ref, self.level_577_ref, self.level_578_ref,
                self.level_579_ref,self.level_580_ref,self.level_581_ref,self.level_582_ref,self.level_583_ref,self.level_584_ref,self.level_585_ref,self.level_586_ref,self.level_587_ref,self.level_588_ref,self.level_589_ref,self.level_590_ref,self.level_591_ref,self.level_592_ref,self.level_593_ref,self.level_594_ref,self.level_595_ref,self.level_596_ref,self.level_597_ref,self.level_598_ref,self.level_599_ref,self.level_600_ref,self.phase1_complete]
        if self.level == 400:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change13.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change4.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change5.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3},{"center_x": .5, "center_y": .2}  ) and self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3},{"center_x": .5, "center_y": .2}   ) and self.ids.change15.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3},{"center_x": .5, "center_y": .2}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 401:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 402:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 403:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .8, "center_y": .3} :
                    if self.ids.change6.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .2})  and  self.ids.change11.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .2})  and  self.ids.change1.pos_hint in ( {"center_x": .5, "center_y": .3},{"center_x": .8, "center_y": .2}) and  self.ids.change4.pos_hint in ( {"center_x": .5, "center_y": .3},{"center_x": .8, "center_y": .2}) and  self.ids.change17.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .35, "center_y": .2}) and self.ids.change12.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .35, "center_y": .2}) and self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2}) and self.ids.change14.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2}) and self.ids.change5.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 404:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} :
                    if self.ids.change.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3} ) and self.ids.change16.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 405:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} :
                    if self.ids.change.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3} ) and self.ids.change16.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 406:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3}  and self.ids.change17.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .2, "center_y": .2}  and self.ids.change6.pos_hint == {"center_x": .35, "center_y": .2} :
                    if self.ids.change.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .2} ) and self.ids.change5.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 407:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and  self.ids.change5.pos_hint == {"center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 408:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and  self.ids.change13.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .35, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 409:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .2, "center_y": .2} :
                    if self.ids.change13.pos_hint in ({"center_x": .5, "center_y": .3},
                                                    {"center_x": .65, "center_y": .3}) and self.ids.change15.pos_hint in (
                    {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}) and self.ids.change4.pos_hint in ({"center_x": .35, "center_y": .2},{"center_x": .5, "center_y": .2}) and  self.ids.change7.pos_hint in ({"center_x": .35, "center_y": .2},{"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 410:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .2, "center_y": .2} :
                    if self.ids.change13.pos_hint in ({"center_x": .5, "center_y": .3},
                                                    {"center_x": .65, "center_y": .3}) and self.ids.change15.pos_hint in (
                    {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}) and self.ids.change4.pos_hint in ({"center_x": .35, "center_y": .2},{"center_x": .5, "center_y": .2}) and  self.ids.change7.pos_hint in ({"center_x": .35, "center_y": .2},{"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 411:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3}  and self.ids.change17.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .2, "center_y": .2}  and self.ids.change5.pos_hint == {"center_x": .35, "center_y": .2} and  self.ids.change6.pos_hint == {"center_x": .5, "center_y": .2}:
                    if self.ids.change3.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2} ) and self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 412:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 413:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3}  and self.ids.change10.pos_hint == {"center_x": .2, "center_y": .2} :
                    if self.ids.change6.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .2} ) and self.ids.change15.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .2} ) and  self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .2} ) and self.ids.change13.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 414:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and  self.ids.change15.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change17.pos_hint == {"center_x": .35, "center_y": .2} and  self.ids.change6.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change3.pos_hint == {"center_x": .65, "center_y": .2} and  self.ids.change11.pos_hint == {"center_x": .8, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 415:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3}  and self.ids.change11.pos_hint == {"center_x": .2, "center_y": .2}  and  self.ids.change7.pos_hint == {"center_x": .65, "center_y": .2}  and  self.ids.change17.pos_hint == {"center_x": .35, "center_y": .1} :
                    if self.ids.change3.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2} ) and self.ids.change6.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2} ) and  self.ids.change14.pos_hint in ( {"center_x": .8, "center_y": .3}, {"center_x": .2, "center_y": .1} ) and self.ids.change15.pos_hint in ( {"center_x": .8, "center_y": .3}, {"center_x": .2, "center_y": .1} ) and self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .2}, {"center_x": .8, "center_y": .2} ) and self.ids.change12.pos_hint in ( {"center_x": .35, "center_y": .2}, {"center_x": .8, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 416:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3}  and self.ids.change11.pos_hint == {"center_x": .2, "center_y": .2}  and  self.ids.change7.pos_hint == {"center_x": .65, "center_y": .2}  and  self.ids.change17.pos_hint == {"center_x": .35, "center_y": .1} :
                    if self.ids.change3.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2} ) and self.ids.change6.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2} ) and  self.ids.change14.pos_hint in ( {"center_x": .8, "center_y": .3}, {"center_x": .2, "center_y": .1} ) and self.ids.change15.pos_hint in ( {"center_x": .8, "center_y": .3}, {"center_x": .2, "center_y": .1} ) and self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .2}, {"center_x": .8, "center_y": .2} ) and self.ids.change12.pos_hint in ( {"center_x": .35, "center_y": .2}, {"center_x": .8, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 417:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change13.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3}  and self.ids.change15.pos_hint == {"center_x": .2, "center_y": .2} :
                    if self.ids.change6.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3} ) and self.ids.change9.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3} ) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 418:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .35,
                                                                                        "center_y": .2}  and self.ids.change11.pos_hint == {"center_x": .8, "center_y": .2}  and  self.ids.change5.pos_hint == {"center_x": .2, "center_y": .1} :
                    if self.ids.change3.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .2} ) and self.ids.change17.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .2} ) and  self.ids.change7.pos_hint in ( {"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .1} ) and self.ids.change15.pos_hint in ( {"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .1} ) and self.ids.change2.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2} ) and self.ids.change12.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2} ) and self.ids.change8.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 419:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .35,
                                                                                        "center_y": .2}  and self.ids.change11.pos_hint == {"center_x": .8, "center_y": .2}  and  self.ids.change5.pos_hint == {"center_x": .2, "center_y": .1} :
                    if self.ids.change3.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .2} ) and self.ids.change17.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .2} ) and  self.ids.change7.pos_hint in ( {"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .1} ) and self.ids.change15.pos_hint in ( {"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .1} ) and self.ids.change2.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2} ) and self.ids.change12.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2} ) and self.ids.change8.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 420:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .35,
                                                                                        "center_y": .2}  and self.ids.change11.pos_hint == {"center_x": .8, "center_y": .2}  and  self.ids.change5.pos_hint == {"center_x": .2, "center_y": .1} :
                    if self.ids.change3.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .2} ) and self.ids.change17.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .2} ) and  self.ids.change7.pos_hint in ( {"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .1} ) and self.ids.change15.pos_hint in ( {"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .1} ) and self.ids.change2.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2} ) and self.ids.change12.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2} ) and self.ids.change8.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 421:
            if self.count in ([i for i in range(15, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2}  and self.ids.change17.pos_hint == {"center_x": .2, "center_y": .1}  and  self.ids.change14.pos_hint == {"center_x": .35, "center_y": .1}  and  self.ids.change4.pos_hint == {"center_x": .5, "center_y": .1} and  self.ids.change12.pos_hint == {"center_x": .8, "center_y": .1} and  self.ids.change.pos_hint == {"center_x": .35, "center_y": .3 }  and  self.ids.change1.pos_hint == {"center_x": .2, "center_y": .2} :
                    if self.ids.change9.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .8, "center_y": .3} ) and self.ids.change11.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .8, "center_y": .3} ) and self.ids.change3.pos_hint in ( {"center_x": .35, "center_y": .2}, {"center_x": .8, "center_y": .2} ) and self.ids.change5.pos_hint in ({"center_x": .35, "center_y": .2}, {"center_x": .8, "center_y": .2} ) and self.ids.change8.pos_hint in ({"center_x": .65, "center_y": .2}, {"center_x": .65, "center_y": .1} ) and  self.ids.change10.pos_hint in ({"center_x": .65, "center_y": .2}, {"center_x": .65, "center_y": .1} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 422:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2}  :
                    if self.ids.change2.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2} ) and self.ids.change17.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2} )  and self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3} ) and  self.ids.change11.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 423:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2}  :
                    if self.ids.change2.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2} ) and self.ids.change17.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2} )  and self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3} ) and  self.ids.change11.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 424:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change13.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3}  and self.ids.change15.pos_hint == {"center_x": .2, "center_y": .2} :
                    if self.ids.change6.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3} ) and self.ids.change9.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3} ) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 425:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3}  and self.ids.change8.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change10.pos_hint == {"center_x": .35, "center_y": .2}:
                    if self.ids.change12.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2} ) and self.ids.change4.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2} ) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 426:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} :
                    if self.ids.change.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .3} ) and self.ids.change5.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .3} ) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 427:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3}  and self.ids.change11.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .5, "center_y": .2}:
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .2} ) and self.ids.change9.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .35, "center_y": .2} ) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 428:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3}  and self.ids.change15.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .35, "center_y": .2} :
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3} ) and self.ids.change13.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3} ) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 429:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3}  and self.ids.change15.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .35, "center_y": .2} :
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3} ) and self.ids.change13.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3} ) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 430:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3}  and self.ids.change14.pos_hint == {"center_x": .65, "center_y": .3}:
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 431:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2}  and self.ids.change15.pos_hint == {"center_x": .35, "center_y": .2}:
                    if self.ids.change2.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}) and self.ids.change6.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}) and self.ids.change5.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .5, "center_y": .2}) and self.ids.change12.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 432:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3}  and self.ids.change15.pos_hint == {"center_x": .65, "center_y": .3}:
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 433:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3}  and self.ids.change5.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change1.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change8.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .8, "center_y": .3}) and self.ids.change14.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .8, "center_y": .3}) :
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 434:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .5, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .35,
                                                                                       "center_y": .2}) and self.ids.change16.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .35, "center_y": .2}) and self.ids.change4.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change14.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .2, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change11.pos_hint in (
                            {"center_x": .2, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change2.pos_hint in (
                            {"center_x": .8, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change9.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 435:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3}  and self.ids.change15.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .35, "center_y": .2} :
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3} ) and self.ids.change13.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3} ) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 436:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3}:
                    if self.ids.change3.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3} ) and self.ids.change17.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3} ) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 437:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3}  and self.ids.change11.pos_hint == {"center_x": .65, "center_y": .3}:
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 438:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3}  and self.ids.change11.pos_hint == {"center_x": .65, "center_y": .3}:
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 439:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3}:
                    if self.ids.change3.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,
                                                                                        "center_y": .3}) and self.ids.change17.pos_hint in (
                    {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 440:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3}:
                    if self.ids.change3.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,
                                                                                        "center_y": .3}) and self.ids.change17.pos_hint in (
                    {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 441:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 442:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 443:
            if self.count in ([i for i in range(3, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 444:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 445:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 446:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 447:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change17.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change9.pos_hint == {"center_x": .8, "center_y": .2} :
                    if self.ids.change12.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,"center_y": .2}) and self.ids.change10.pos_hint in (
                    {"center_x": .65, "center_y": .3}, {"center_x": .65, "center_y": .2}) and self.ids.change3.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .5,"center_y": .2}) and  self.ids.change5.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .5,"center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 448:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5, "center_y": .3}:
                    if self.ids.change5.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .8,
                                                                                        "center_y": .3}) and self.ids.change17.pos_hint in (
                    {"center_x": .65, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 449:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change4.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2} and self.ids.change1.pos_hint == {
                    "center_x": .65, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .8, "center_y": .2} :

                    if self.ids.change12.pos_hint in ({"center_x": .5, "center_y": .2}, {"center_x": .2,
                                                                                        "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1}) and self.ids.change.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,"center_y": .2},{"center_x": .35, "center_y": .1}) and  self.ids.change5.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,"center_y": .2},{"center_x": .35, "center_y": .1}) and  self.ids.change9.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,"center_y": .2},{"center_x": .35, "center_y": .1}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 450:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 451:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .35, "center_y": .2}  :
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .5,
                                                                                        "center_y": .2}) and self.ids.change5.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 452:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change12.pos_hint == {"center_x": .35, "center_y": .2} and  self.ids.change2.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change17.pos_hint == {"center_x": .65, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 453:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3}  and self.ids.change.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .5, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
        elif self.level == 454:
            if self.count in ([i for i in range(2, 19)]):
                if self.ids.change4.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .35, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
        elif self.level == 455:
            if self.count in ([i for i in range(13, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change7.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change8.pos_hint == {"center_x": .8, "center_y": .2}  and self.ids.change16.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change2.pos_hint == {"center_x": .5, "center_y": .1} :
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .35,"center_y": .2}) and self.ids.change3.pos_hint in (
                    {"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .2}) and  self.ids.change17.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .5,"center_y": .2},{"center_x": .35,"center_y": .1}) and  self.ids.change6.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .5,"center_y": .2},{"center_x": .35,"center_y": .1}) and  self.ids.change15.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .5,"center_y": .2},{"center_x": .35,"center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 456:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change7.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .8, "center_y": .2}  and self.ids.change6.pos_hint == {"center_x": .2, "center_y": .1}:
                    if self.ids.change12.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .8,"center_y": .3}) and self.ids.change8.pos_hint in (
                    {"center_x": .2, "center_y": .3}, {"center_x": .8, "center_y": .3}) and  self.ids.change3.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,"center_y": .3}) and  self.ids.change16.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,"center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 457:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change12.pos_hint == {"center_x": .5, "center_y": .2} :
                    if self.ids.change6.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,"center_y": .3}) and self.ids.change13.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}) and  self.ids.change3.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .65,"center_y": .2}) and  self.ids.change8.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .65,"center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 458:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change9.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change13.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change8.pos_hint == {
                    "center_x": .8, "center_y": .2}:
                    if self.ids.change1.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65,
                                                                                         "center_y": .2}) and self.ids.change15.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change12.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change4.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .2, "center_y": .2}) and self.ids.change7.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 459:
            if self.count in ([i for i in range(13, 19)]):
                if self.ids.change10.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change3.pos_hint == {"center_x": .35, "center_y": .1} and self.ids.change12.pos_hint == {"center_x": .5, "center_y": .1} :
                    if self.ids.change1.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .5,"center_y": .2}) and self.ids.change15.pos_hint in (
                    {"center_x": .5, "center_y": .3}, {"center_x": .5, "center_y": .2}) and  self.ids.change17.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,"center_y": .2}) and  self.ids.change9.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,"center_y": .2}) and  self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,"center_y": .3},{"center_x": .35, "center_y": .2}, {"center_x": .8,"center_y": .2}) and  self.ids.change11.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,"center_y": .3},{"center_x": .35, "center_y": .2}, {"center_x": .8,"center_y": .2})  and  self.ids.change7.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,"center_y": .3},{"center_x": .35, "center_y": .2}, {"center_x": .8,"center_y": .2}) and  self.ids.change13.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,"center_y": .3},{"center_x": .35, "center_y": .2}, {"center_x": .8,"center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 460:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change4.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .8,
                                                                                      "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change12.pos_hint == {"center_x": .35,
                                                                                       "center_y": .2} :
                    if self.ids.change9.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5,
                                                                                         "center_y": .3}) and self.ids.change6.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .5, "center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 461:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .2, "center_y": .2} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 462:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change1.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change13.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change7.pos_hint == {"center_x": .8, "center_y": .2} :
                    if self.ids.change17.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .2,"center_y": .2}) and self.ids.change10.pos_hint in (
                    {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}) and  self.ids.change.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,"center_y": .3}) and  self.ids.change14.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,"center_y": .3}) and  self.ids.change16.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .2,"center_y": .1}) and  self.ids.change9.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .2,"center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 463:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .8, "center_y": .3}:
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .2,"center_y": .2}) and self.ids.change12.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .2}) and  self.ids.change5.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .35,"center_y": .2}) and  self.ids.change10.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .35,"center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 464:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3}  and self.ids.change4.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change1.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3} ,{"center_x": .8, "center_y": .3} ) and  self.ids.change17.pos_hint in ( {"center_x": .35, "center_y": .3} ,{"center_x": .8, "center_y": .3} ) and  self.ids.change5.pos_hint in ( {"center_x": .2, "center_y": .2} ,{"center_x": .35, "center_y": .2} ) and self.ids.change12.pos_hint in ( {"center_x": .2, "center_y": .2} ,{"center_x": .35, "center_y": .2} ) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 465:
            if self.count in ([i for i in range(14, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change7.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change8.pos_hint == {"center_x": .8, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .2, "center_y": .1}  and self.ids.change17.pos_hint == {"center_x": .5, "center_y": .1}:
                    if self.ids.change1.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5,"center_y": .2}) and self.ids.change3.pos_hint in (
                    {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .2}) and  self.ids.change.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,"center_y": .1}) and  self.ids.change13.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,"center_y": .1}) and  self.ids.change16.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,"center_y": .2}) and  self.ids.change5.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,"center_y": .2}) and self.ids.change6.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .35,"center_y": .1}) and  self.ids.change12.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .35,"center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 466:
            if self.count in ([i for i in range(13, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .5, "center_y": .3}  and self.ids.change2.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .8, "center_y": .2} and  self.ids.change14.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change4.pos_hint == {"center_x": .35, "center_y": .1} and self.ids.change9.pos_hint == {"center_x": .5, "center_y": .1} :

                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}  ) and self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3})  and  self.ids.change11.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change8.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change5.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2}) and  self.ids.change12.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 467:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change13.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .8, "center_y": .3}:
                    if self.ids.change11.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,"center_y": .3}, {"center_x": .2,"center_y": .2}) and self.ids.change15.pos_hint in (
                    {"center_x": .5, "center_y": .3}, {"center_x": .65,"center_y": .3}, {"center_x": .2,"center_y": .2}) and  self.ids.change8.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,"center_y": .3}, {"center_x": .2,"center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 468:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change12.pos_hint == {"center_x": .5, "center_y": .2} :
                    if self.ids.change6.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,"center_y": .3}) and self.ids.change13.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}) and  self.ids.change3.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .65,"center_y": .2}) and  self.ids.change8.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .65,"center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 469:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change12.pos_hint == {"center_x": .35, "center_y": .2} and  self.ids.change2.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change17.pos_hint == {"center_x": .65, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 470:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .5, "center_y": .3}:
                    if self.ids.change5.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65,"center_y": .3}) and self.ids.change17.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 471:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2} and self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .5, "center_y": .2} :
                    if self.ids.change13.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3}) and self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3}) and self.ids.change.pos_hint in ( {"center_x": .5, "center_y": .3},{"center_x": .65, "center_y": .2}) and  self.ids.change4.pos_hint in ( {"center_x": .5, "center_y": .3},{"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 472:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change13.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change17.pos_hint == {"center_x": .5, "center_y": .2} :
                    if self.ids.change5.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2}) and self.ids.change16.pos_hint in ({"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2}) and self.ids.change10.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2}) and  self.ids.change6.pos_hint in ({"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 473:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .2,
                                                                                       "center_y": .2} and self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .5, "center_y": .2} :
                    if self.ids.change13.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3}) and self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .65, "center_y": .3}) and self.ids.change.pos_hint in ( {"center_x": .5, "center_y": .3},{"center_x": .65, "center_y": .2}) and  self.ids.change4.pos_hint in ( {"center_x": .5, "center_y": .3},{"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 474:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change13.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5,"center_y": .3}) and self.ids.change8.pos_hint in (
                    {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 475:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} :
                    if self.ids.change6.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .5,"center_y": .3},{"center_x": .65,"center_y": .3}) and self.ids.change17.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .5,"center_y": .3},{"center_x": .65,"center_y": .3})  and  self.ids.change14.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .5,"center_y": .3},{"center_x": .65,"center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 476:
            if self.count in ([i for i in range(3, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5, "center_y": .3} :
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 477:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5, "center_y": .3}  and  self.ids.change6.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change16.pos_hint == {"center_x": .8, "center_y": .3}:
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 478:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change16.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8, "center_y": .3} :
                    if  self.ids.change3.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .65, "center_y": .3}) and  self.ids.change7.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .65, "center_y": .3}) :
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 479:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change16.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8, "center_y": .3} :
                    if  self.ids.change3.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .65, "center_y": .3}) and  self.ids.change7.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .65, "center_y": .3}) :
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 480:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .35, "center_y": .2}  and  self.ids.change4.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change17.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change7.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .2}) and self.ids.change9.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .2}) and self.ids.change11.pos_hint in ( {"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .1}) and  self.ids.change3.pos_hint in ( {"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 481:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .5, "center_y": .3}  and  self.ids.change6.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change5.pos_hint == {"center_x": .8, "center_y": .3}:
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 482:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .2, "center_y": .2}  and  self.ids.change9.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change17.pos_hint == {"center_x": .65, "center_y": .2} and  self.ids.change2.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .35, "center_y": .2}) and self.ids.change3.pos_hint in ( {"center_x": .35, "center_y": .3},{"center_x": .35, "center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)

            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 483:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5, "center_y": .3}  and  self.ids.change7.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change11.pos_hint == {"center_x": .8, "center_y": .3} and   self.ids.change16.pos_hint == {"center_x": .2, "center_y": .2} and   self.ids.change2.pos_hint == {"center_x": .35, "center_y": .2} and   self.ids.change12.pos_hint == {"center_x": .5, "center_y": .2}:
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 484:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    if self.ids.change7.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}) and self.ids.change11.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}) and self.ids.change3.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2}) and self.ids.change15.pos_hint in ({"center_x": .5, "center_y": .3},{"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 485:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and  self.ids.change16.pos_hint == {"center_x": .5, "center_y": .3}  and  self.ids.change.pos_hint == {"center_x": .8, "center_y": .3}  and  self.ids.change5.pos_hint == {"center_x": .2, "center_y": .2} :
                    if self.ids.change9.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,
                                                                                         "center_y": .2}) and self.ids.change6.pos_hint in (
                    {"center_x": .65, "center_y": .3},
                    {"center_x": .35, "center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 486:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change13.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5, "center_y": .3}  and  self.ids.change8.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change6.pos_hint == {"center_x": .8, "center_y": .3} and   self.ids.change15.pos_hint == {"center_x": .2, "center_y": .2} and   self.ids.change17.pos_hint == {"center_x": .35, "center_y": .2} :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 487:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change4.pos_hint == {"center_x": .35,"center_y": .2} :
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,"center_y": .3}) and self.ids.change12.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .3}) and self.ids.change7.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,"center_y": .3}) and  self.ids.change10.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,"center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 488:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5, "center_y": .3}  and  self.ids.change6.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change16.pos_hint == {"center_x": .8, "center_y": .3} :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 489:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                                       "center_y": .2} and self.ids.change15.pos_hint == {
                    "center_x": .65, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .8,
                                                                                       "center_y": .2} and self.ids.change8.pos_hint == {
                    "center_x": .2, "center_y": .1}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .2,
                                                                                       "center_y": .2}) and self.ids.change17.pos_hint in (
                            {"center_x": .2, "center_y": .3}, {"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 490:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .8,
                                                                                       "center_y": .2} :
                    if self.ids.change1.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .5,"center_y": .2}) and self.ids.change16.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2}) and  self.ids.change11.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,"center_y": .2}) and  self.ids.change4.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,"center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 491:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .8,
                                                                                       "center_y": .2} :
                    if self.ids.change1.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .5,"center_y": .2}) and self.ids.change16.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2}) and  self.ids.change11.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,"center_y": .2}) and  self.ids.change4.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,"center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 492:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change7.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .2,
                                                                                     "center_y": .2} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .8,
                                                                                        "center_y": .2} and self.ids.change11.pos_hint ==  {"center_x": .2, "center_y": .1}:
                    if self.ids.change5.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .5,
                                                                                          "center_y": .2}) and self.ids.change13.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .5, "center_y": .2}) and self.ids.change.pos_hint in (
                            {"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) and self.ids.change9.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 493:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change7.pos_hint == {
                    "center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .35,
                                                                                      "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .2,
                                                                                     "center_y": .2} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .8,
                                                                                        "center_y": .2} and self.ids.change11.pos_hint ==  {"center_x": .2, "center_y": .1}:
                    if self.ids.change5.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .5,
                                                                                          "center_y": .2}) and self.ids.change13.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .5, "center_y": .2}) and self.ids.change.pos_hint in (
                            {"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) and self.ids.change17.pos_hint in (
                            {"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) and self.ids.change9.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .65, "center_y": .2},{"center_x": .35, "center_y": .1}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 494:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .8,
                                                                                       "center_y": .2} :
                    if self.ids.change1.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .5,"center_y": .2}) and self.ids.change16.pos_hint in (
                            {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2}) and  self.ids.change11.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,"center_y": .2}) and  self.ids.change4.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .65,"center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 495:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and  self.ids.change13.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change16.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change8.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change5.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change2.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .35, "center_y": .2} ) and self.ids.change6.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .35, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 496:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3}:
                    if self.ids.change3.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .65, "center_y": .3} ) and self.ids.change7.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .65, "center_y": .3} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 497:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and  self.ids.change13.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change16.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change8.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change5.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change2.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .35, "center_y": .2} ) and self.ids.change6.pos_hint in ( {"center_x": .2, "center_y": .3} , {"center_x": .35, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 498:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5, "center_y": .3}  and self.ids.change.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change12.pos_hint == {"center_x": .8, "center_y": .2} :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 499:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5, "center_y": .3}  and self.ids.change17.pos_hint == {"center_x": .65, "center_y": .3}:
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 500:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and  self.ids.change6.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change5.pos_hint == {"center_x": .65, "center_y": .2} and  self.ids.change15.pos_hint == {"center_x": .8, "center_y": .2} and  self.ids.change10.pos_hint == {"center_x": .2, "center_y": .1}:
                    if self.ids.change13.pos_hint in ( {"center_x": .5, "center_y": .3} , {"center_x": .35, "center_y": .2} ) and self.ids.change17.pos_hint in ( {"center_x": .5, "center_y": .3} , {"center_x": .35, "center_y": .2} ) and  self.ids.change3.pos_hint in ( {"center_x": .8, "center_y": .3} , {"center_x": .5, "center_y": .2}, {"center_x": .35, "center_y": .1} ) and   self.ids.change12.pos_hint in ( {"center_x": .8, "center_y": .3} , {"center_x": .5, "center_y": .2}, {"center_x": .35, "center_y": .1} ) and   self.ids.change7.pos_hint in ( {"center_x": .8, "center_y": .3} , {"center_x": .5, "center_y": .2}, {"center_x": .35, "center_y": .1} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 501:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2} and  self.ids.change6.pos_hint == {"center_x": .35, "center_y": .2} and  self.ids.change9.pos_hint == {"center_x": .8, "center_y": .2} :
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .65, "center_y": .2} ) and self.ids.change5.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .65, "center_y": .2} ) and  self.ids.change2.pos_hint in ( {"center_x": .5, "center_y": .3} , {"center_x": .65, "center_y": .3}, {"center_x": .5, "center_y": .2} ) and   self.ids.change3.pos_hint in ( {"center_x": .5, "center_y": .3} , {"center_x": .65, "center_y": .3}, {"center_x": .5, "center_y": .2} ) and   self.ids.change11.pos_hint in ( {"center_x": .5, "center_y": .3} , {"center_x": .65, "center_y": .3}, {"center_x": .5, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 502:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} and  self.ids.change6.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change5.pos_hint == {"center_x": .65, "center_y": .2} and  self.ids.change15.pos_hint == {"center_x": .8, "center_y": .2} and  self.ids.change10.pos_hint == {"center_x": .2, "center_y": .1}:
                    if self.ids.change13.pos_hint in ( {"center_x": .5, "center_y": .3} , {"center_x": .35, "center_y": .2} ) and self.ids.change17.pos_hint in ( {"center_x": .5, "center_y": .3} , {"center_x": .35, "center_y": .2} ) and  self.ids.change3.pos_hint in ( {"center_x": .8, "center_y": .3} , {"center_x": .5, "center_y": .2}, {"center_x": .35, "center_y": .1} ) and   self.ids.change12.pos_hint in ( {"center_x": .8, "center_y": .3} , {"center_x": .5, "center_y": .2}, {"center_x": .35, "center_y": .1} ) and   self.ids.change7.pos_hint in ( {"center_x": .8, "center_y": .3} , {"center_x": .5, "center_y": .2}, {"center_x": .35, "center_y": .1} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 503:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5, "center_y": .3}  and self.ids.change10.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change16.pos_hint == {"center_x": .8, "center_y": .3}:
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 504:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3}:
                    if self.ids.change11.pos_hint in ({"center_x": .35, "center_y": .3},
                                                    {"center_x": .8, "center_y": .3}) and self.ids.change15.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 505:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .5, "center_y": .3}  and self.ids.change10.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change16.pos_hint == {"center_x": .8, "center_y": .3}:
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 506:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} :
                    if  self.ids.change.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .3}) and self.ids.change4.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 507:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change1.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change7.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change6.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}) and self.ids.change11.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 508:
            if self.count in ([i for i in range(15, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .8, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change5.pos_hint == {"center_x": .35, "center_y": .1} and self.ids.change3.pos_hint == {"center_x": .5, "center_y": .1}:
                    if self.ids.change9.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .8, "center_y": .1}) and self.ids.change12.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .1}) and self.ids.change4.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}) and self.ids.change6.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}) and self.ids.change11.pos_hint in ( {"center_x": .65, "center_y": .2}, {"center_x": .65, "center_y": .1}) and self.ids.change13.pos_hint in ( {"center_x": .65, "center_y": .2}, {"center_x": .65, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 509:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .35,
                                                                                        "center_y": .2} and self.ids.change10.pos_hint == {
                    "center_x": .5, "center_y": .2} and self.ids.change13.pos_hint == {"center_x": .65, "center_y": .2} :
                    if self.ids.change6.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .3}) and self.ids.change8.pos_hint in (  {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .3}) and self.ids.change11.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}) and self.ids.change12.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 510:
            if self.count in ([i for i in range(13, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change13.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change16.pos_hint == {"center_x": .5, "center_y": .1}:
                    if self.ids.change.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .35, "center_y": .1}) and self.ids.change4.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .35, "center_y": .1}) and self.ids.change8.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2}, {"center_x": .8, "center_y": .2}) and self.ids.change11.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2}, {"center_x": .8, "center_y": .2}) and self.ids.change15.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2}, {"center_x": .8, "center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 511:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change16.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .2} :
                    if self.ids.change6.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3}) and self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 512:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .2} and self.ids.change1.pos_hint == {"center_x": .35, "center_y": .1}:
                    if self.ids.change10.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .3}) and self.ids.change13.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .3}) and self.ids.change5.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .8, "center_y": .3}, {"center_x": .8, "center_y": .2}) and self.ids.change6.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .8, "center_y": .3}, {"center_x": .8, "center_y": .2}) and self.ids.change14.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .8, "center_y": .3}, {"center_x": .8, "center_y": .2})  and self.ids.change16.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .2, "center_y": .1}) and self.ids.change17.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 513:
            if self.count in ([i for i in range(13, 19)]):
                if self.ids.change15.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .8, "center_y": .2} and  self.ids.change17.pos_hint == {"center_x": .2, "center_y": .1}:

                    if self.ids.change9.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .2}) and self.ids.change14.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .2}) and self.ids.change2.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .5, "center_y": .1}) and self.ids.change13.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .5, "center_y": .1}) and self.ids.change5.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .1})  and self.ids.change11.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .35, "center_y": .1}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 514:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} :

                    if self.ids.change6.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}) and self.ids.change13.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 515:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} :

                    if self.ids.change6.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}) and self.ids.change13.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 516:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} :

                    if self.ids.change1.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}) and self.ids.change6.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 517:
            if self.count in ([i for i in range(13, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .5, "center_y": .3}  and self.ids.change2.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .8, "center_y": .2} and  self.ids.change14.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change4.pos_hint == {"center_x": .35, "center_y": .1} and self.ids.change9.pos_hint == {"center_x": .5, "center_y": .1} :

                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3}  ) and self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3},{"center_x": .8, "center_y": .3})  and  self.ids.change11.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change8.pos_hint in ({"center_x": .65, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change5.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2}) and  self.ids.change12.pos_hint in ({"center_x": .2, "center_y": .2},{"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 518:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3} :

                    if self.ids.change6.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}) and self.ids.change13.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 519:
            if self.count in ([i for i in range(15, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .8, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change5.pos_hint == {"center_x": .35, "center_y": .1} and self.ids.change3.pos_hint == {"center_x": .5, "center_y": .1}:
                    if self.ids.change9.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .8, "center_y": .1}) and self.ids.change12.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .1}) and self.ids.change4.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}) and self.ids.change6.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}) and self.ids.change11.pos_hint in ( {"center_x": .65, "center_y": .2}, {"center_x": .65, "center_y": .1}) and self.ids.change13.pos_hint in ( {"center_x": .65, "center_y": .2}, {"center_x": .65, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 520:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .8,
                    "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change4.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65,
                             "center_y": .3}) and self.ids.change11.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change2.pos_hint in (
                            {"center_x": .5, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change9.pos_hint in (
                            {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 521:
            if self.count in ([i for i in range(3, 19)]):
                if self.ids.change4.pos_hint == {"center_x": .35, "center_y": .3} :
                    if self.ids.change16.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5,
                                                                                         "center_y": .3}) and self.ids.change14.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .5, "center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 522:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .65,
                                                                                        "center_y": .3}  and self.ids.change17.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .2, "center_y": .2}  and self.ids.change6.pos_hint == {"center_x": .35, "center_y": .2} :
                    if self.ids.change.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .2} ) and self.ids.change5.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .2} ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 523:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change13.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3}  and self.ids.change3.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8, "center_y": .3} :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 524:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change13.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 525:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change13.pos_hint == {"center_x": .2, "center_y": .3}   and self.ids.change11.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .8, "center_y": .3}:
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .2, "center_y": .2}  ) and self.ids.change5.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .2, "center_y": .2}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 526:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3}   and self.ids.change.pos_hint == {"center_x": .35,
                                                                                        "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    if self.ids.change4.pos_hint in ( {"center_x": .5, "center_y": .3} , {"center_x": .8, "center_y": .3}  ) and self.ids.change15.pos_hint in ( {"center_x": .5, "center_y": .3} , {"center_x": .8, "center_y": .3}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 527:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3}   and self.ids.change11.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .35, "center_y": .2} :
                    if self.ids.change1.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .2, "center_y": .2}  ) and self.ids.change13.pos_hint in ( {"center_x": .35, "center_y": .3} , {"center_x": .2, "center_y": .2}  ):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 528:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .35,
                                                                                         "center_y": .2}) and self.ids.change12.pos_hint in (
                    {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 529:
            if self.count in ([i for i in range(8, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .8,
                    "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .35,
                                                                                        "center_y": .2} and self.ids.change12.pos_hint == {
                    "center_x": .5, "center_y": .2}  :
                    if self.ids.change7.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .65,
                                                                                         "center_y": .3}) and self.ids.change9.pos_hint in (
                    {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .3}) and  self.ids.change15.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .2,
                                                                                         "center_y": .2}) and self.ids.change4.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .2,
                                                                                         "center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 530:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .2, "center_y": .2}   and self.ids.change3.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change13.pos_hint == {"center_x": .65, "center_y": .2} :
                    if self.ids.change6.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change10.pos_hint in (
                    {"center_x": .8, "center_y": .3}, {"center_x": .65, "center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 531:
            if self.count in ([i for i in range(3, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change7.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3}:
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 532:


            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change5.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3}:
                    if self.ids.change6.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .65,
                                                                                        "center_y": .3}) and self.ids.change16.pos_hint in (
                    {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 533:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change16.pos_hint == {"center_x": .5,
                                                                      "center_y": .3} and  self.ids.change11.pos_hint == {"center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 534:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                      "center_y": .3} and  self.ids.change14.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change17.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change5.pos_hint == {"center_x": .2, "center_y": .2} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 535:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                      "center_y": .3} and  self.ids.change14.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change17.pos_hint == {"center_x": .2, "center_y": .2} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 536:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                      "center_y": .3} and  self.ids.change14.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change17.pos_hint == {"center_x": .2, "center_y": .2} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 537:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                      "center_y": .3} and  self.ids.change.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change12.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change4.pos_hint == {"center_x": .2, "center_y": .2} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 538:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .35,
                                                                                        "center_y": .2} :
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65,"center_y": .3}) and self.ids.change11.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3}) and self.ids.change17.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .2,"center_y": .2})  and self.ids.change7.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .2,"center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 539:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change13.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                      "center_y": .3} and  self.ids.change6.pos_hint == {"center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 540:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change9.pos_hint == {"center_x": .35,
                                                                                        "center_y": .2} :
                    if self.ids.change.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65,"center_y": .3}) and self.ids.change11.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3}) and self.ids.change17.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .2,"center_y": .2})  and self.ids.change7.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .2,"center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 541:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .5,
                                                                      "center_y": .3} and  self.ids.change14.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change17.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change5.pos_hint == {"center_x": .2, "center_y": .2} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 542:
            if self.count in ([i for i in range(3, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                      "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 543:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .5,
                                                                      "center_y": .3} and  self.ids.change15.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change17.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change6.pos_hint == {"center_x": .2, "center_y": .2} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 544:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change10.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .2,
                                                                                        "center_y": .2} and self.ids.change13.pos_hint == {
                    "center_x": .35, "center_y": .2} and self.ids.change3.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change11.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .2,
                                                                                         "center_y": .1}) and self.ids.change17.pos_hint in (
                    {"center_x": .5, "center_y": .3}, {"center_x": .2, "center_y": .1}) and self.ids.change9.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .5,
                                                                                         "center_y": .2}) and self.ids.change14.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .5,
                                                                                         "center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 545:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change10.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change9.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .8, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change11.pos_hint == {"center_x": .35, "center_y": .1}:
                    if self.ids.change3.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .5,
                                                                                         "center_y": .2}) and self.ids.change8.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .5, "center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 546:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .5,
                    "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    if self.ids.change6.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change12.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}) and self.ids.change17.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .35,
                                                                                         "center_y": .2}) and self.ids.change1.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .35,
                                                                                         "center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 547:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .65,
                    "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .8, "center_y": .3}  and  self.ids.change1.pos_hint == {"center_x": .2, "center_y": .1} and  self.ids.change8.pos_hint == {"center_x": .35, "center_y": .1}:
                    if self.ids.change9.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5,"center_y": .2}) and self.ids.change12.pos_hint in (
                    {"center_x": .2, "center_y": .3}, {"center_x": .5, "center_y": .2}) and self.ids.change14.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,
                                                                                         "center_y": .2}) and self.ids.change16.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,
                                                                                         "center_y": .2})  and self.ids.change3.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .2,"center_y": .2},{"center_x": .65, "center_y": .2}, {"center_x": .8,"center_y": .2}) and self.ids.change6.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .2,"center_y": .2},{"center_x": .65, "center_y": .2}, {"center_x": .8,"center_y": .2}) and self.ids.change11.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .2,"center_y": .2},{"center_x": .65, "center_y": .2}, {"center_x": .8,"center_y": .2}) and self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .2,"center_y": .2},{"center_x": .65, "center_y": .2}, {"center_x": .8,"center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 548:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .65,
                    "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .2,
                                                                                      "center_y": .1} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .1}:
                    if self.ids.change9.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .5,
                                                                                        "center_y": .2}) and self.ids.change12.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .5, "center_y": .2}) and self.ids.change14.pos_hint in (
                    {"center_x": .65, "center_y": .3}, {"center_x": .35,
                                                        "center_y": .2}) and self.ids.change16.pos_hint in (
                    {"center_x": .65, "center_y": .3}, {"center_x": .35,
                                                        "center_y": .2}) and self.ids.change3.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .2},
                    {"center_x": .65, "center_y": .2},
                    {"center_x": .8, "center_y": .2}) and self.ids.change6.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .2},
                    {"center_x": .65, "center_y": .2},
                    {"center_x": .8, "center_y": .2}) and self.ids.change11.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .2},
                    {"center_x": .65, "center_y": .2},
                    {"center_x": .8, "center_y": .2}) and self.ids.change17.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .2},
                    {"center_x": .65, "center_y": .2}, {"center_x": .8, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 549:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change4.pos_hint == {"center_x": .5, "center_y": .3} :
                    if self.ids.change6.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .65,
                                                                                         "center_y": .3}) and self.ids.change16.pos_hint in (
                    {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .3}) and self.ids.change9.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 550:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .35,
                    "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .2, "center_y": .2}  and  self.ids.change14.pos_hint == {"center_x": .8, "center_y": .2} and  self.ids.change17.pos_hint == {"center_x": .2, "center_y": .1}:
                    if self.ids.change7.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .35,"center_y": .2}) and self.ids.change16.pos_hint in (
                    {"center_x": .5, "center_y": .3}, {"center_x": .35,"center_y": .2}) and self.ids.change5.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .5,
                                                                                         "center_y": .2}) and self.ids.change11.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .5,
                                                                                         "center_y": .2})  and self.ids.change.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .65,"center_y": .2}) and self.ids.change2.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .65,"center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 551:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change4.pos_hint == {"center_x": .5, "center_y": .3} :
                    if self.ids.change6.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .65,
                                                                                         "center_y": .3}) and self.ids.change16.pos_hint in (
                    {"center_x": .2, "center_y": .3}, {"center_x": .65, "center_y": .3}) and self.ids.change9.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 552:
            if self.count in ([i for i in range(2, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3}  and self.ids.change6.pos_hint == {"center_x": .35, "center_y": .3} :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 553:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .65,
                    "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .35, "center_y": .2}  and  self.ids.change17.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change12.pos_hint == {"center_x": .65, "center_y": .2}:
                    if self.ids.change3.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .2,"center_y": .1}) and self.ids.change10.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .2,"center_y": .1}) and self.ids.change.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change11.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3})  and self.ids.change5.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .8,"center_y": .2}) and self.ids.change13.pos_hint in ({"center_x": .2, "center_y": .2}, {"center_x": .8,"center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 554:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .35,
                    "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .5, "center_y": .3}  and  self.ids.change15.pos_hint == {"center_x": .8, "center_y": .3} :
                    if self.ids.change1.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .2,"center_y": .2}) and self.ids.change4.pos_hint in (
                    {"center_x": .65, "center_y": .3}, {"center_x": .2,"center_y": .2}) and self.ids.change9.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .35,"center_y": .2}) and  self.ids.change14.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .35,"center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 555:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2,
                    "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .65, "center_y": .3}  and  self.ids.change4.pos_hint == {"center_x": .8, "center_y": .3} :
                    if self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .5,"center_y": .3}) and self.ids.change12.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .5,"center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 556:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2,"center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .5, "center_y": .3}  and  self.ids.change5.pos_hint == {"center_x": .65, "center_y": .3}  and self.ids.change12.pos_hint == {"center_x": .8,"center_y": .3} and self.ids.change4.pos_hint == {"center_x": .35,"center_y": .2} :
                    if self.ids.change17.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .2,"center_y": .2}) and self.ids.change8.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .2,"center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 557:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .8,
                    "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .35,
                                                                                      "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .65, "center_y": .2}:
                    if self.ids.change4.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .35, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65,
                             "center_y": .3}) and self.ids.change11.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change2.pos_hint in (
                            {"center_x": .5, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change9.pos_hint in (
                            {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 558:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change3.pos_hint == {"center_x": .2,"center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3}  and  self.ids.change7.pos_hint == {"center_x": .5, "center_y": .3}  and self.ids.change17.pos_hint == {"center_x": .8,"center_y": .3} and self.ids.change14.pos_hint == {"center_x": .2,"center_y": .2}  and  self.ids.change10.pos_hint == {"center_x": .35,"center_y": .2} and  self.ids.change5.pos_hint == {"center_x": .5,"center_y": .2} and  self.ids.change6.pos_hint == {"center_x": .65,"center_y": .2} and  self.ids.change16.pos_hint == {"center_x": .8,"center_y": .2} and  self.ids.change2.pos_hint == {"center_x": .2,"center_y": .1}:
                    if self.ids.change.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .35,"center_y": .1}) and self.ids.change9.pos_hint in (
                    {"center_x": .65, "center_y": .3}, {"center_x": .35,"center_y": .1}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 559:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                      "center_y": .3} and  self.ids.change16.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change2.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change12.pos_hint == {"center_x": .2, "center_y": .2}  and self.ids.change4.pos_hint == {"center_x": .35, "center_y": .2} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 560:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .35,
                    "center_y": .3} and self.ids.change1.pos_hint == {"center_x": .5,
                                                                      "center_y": .3} and  self.ids.change10.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change12.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change3.pos_hint == {"center_x": .2, "center_y": .2} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 561:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change14.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change1.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change5.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change7.pos_hint == {"center_x": .8, "center_y": .2}:
                    if self.ids.change6.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}) and self.ids.change11.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 562:
            if self.count in ([i for i in range(15, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change2.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .8, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change5.pos_hint == {"center_x": .35, "center_y": .1} and self.ids.change3.pos_hint == {"center_x": .5, "center_y": .1}:
                    if self.ids.change9.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .8, "center_y": .1}) and self.ids.change12.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .1}) and self.ids.change4.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}) and self.ids.change6.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .2}) and self.ids.change11.pos_hint in ( {"center_x": .65, "center_y": .2}, {"center_x": .65, "center_y": .1}) and self.ids.change13.pos_hint in ( {"center_x": .65, "center_y": .2}, {"center_x": .65, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 563:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} :
                    if  self.ids.change3.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .35, "center_y": .2}) and self.ids.change7.pos_hint in ( {"center_x": .65, "center_y": .3},{"center_x": .35, "center_y": .2}) and self.ids.change11.pos_hint in ( {"center_x": .8, "center_y": .3},{"center_x": .2, "center_y": .2}) and self.ids.change15.pos_hint in ( {"center_x": .8, "center_y": .3},{"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 564:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .65, "center_y": .3}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 565:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change11.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change7.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 566:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .2, "center_y": .2} and  self.ids.change11.pos_hint == {"center_x": .35, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)


            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 567:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change4.pos_hint == {
                    "center_x": .5, "center_y": .3}:
                    if  self.ids.change17.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .65, "center_y": .3}) and self.ids.change9.pos_hint in ( {"center_x": .2, "center_y": .3},{"center_x": .65, "center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 568:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .65, "center_y": .2} :
                    if self.ids.change5.pos_hint in ( {"center_x": .35, "center_y": .2}, {"center_x": .5, "center_y": .2}) and self.ids.change14.pos_hint in ( {"center_x": .35, "center_y": .2}, {"center_x": .5, "center_y": .2}) and self.ids.change17.pos_hint in ( {"center_x": .8, "center_y": .2}, {"center_x": .2, "center_y": .1}) and self.ids.change11.pos_hint in ( {"center_x": .8, "center_y": .2}, {"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 569:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .65, "center_y": .2} :
                    if self.ids.change5.pos_hint in ( {"center_x": .35, "center_y": .2}, {"center_x": .5, "center_y": .2}) and self.ids.change14.pos_hint in ( {"center_x": .35, "center_y": .2}, {"center_x": .5, "center_y": .2}) and self.ids.change17.pos_hint in ( {"center_x": .8, "center_y": .2}, {"center_x": .2, "center_y": .1}) and self.ids.change11.pos_hint in ( {"center_x": .8, "center_y": .2}, {"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 570:
            if self.count in ([i for i in range(7, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3}  and self.ids.change11.pos_hint == {"center_x": .35, "center_y": .2}:
                    if self.ids.change17.pos_hint in ( {"center_x": .8, "center_y": .3}, {"center_x": .2, "center_y": .2}) and self.ids.change5.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .2, "center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 571:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change13.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change10.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change4.pos_hint == {"center_x": .65, "center_y": .3}:
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 572:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change12.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .2, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 573:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .8, "center_y": .2} :
                    if self.ids.change8.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2}) and self.ids.change10.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2}) and  self.ids.change5.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2}, {"center_x": .65, "center_y": .2}) and  self.ids.change11.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2}, {"center_x": .65, "center_y": .2}) and  self.ids.change12.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2}, {"center_x": .65, "center_y": .2}) and  self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2}, {"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 574:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change14.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .8,
                                                                                        "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .2}  and  self.ids.change12.pos_hint == {"center_x": .35, "center_y": .2}  and  self.ids.change5.pos_hint == {"center_x": .65, "center_y": .2} :
                    if self.ids.change6.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change2.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .2}) and  self.ids.change11.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .2, "center_y": .3},{"center_x": .5, "center_y": .2}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 575:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change7.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3}  and  self.ids.change16.pos_hint == {"center_x": .8, "center_y": .3}  :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 576:
            if self.count in ([i for i in range(6, 19)]):
                if self.ids.change10.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change15.pos_hint == {"center_x": .5,
                                                                                        "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .2, "center_y": .2} :
                    if self.ids.change4.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .8, "center_y": .3}) and  self.ids.change8.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .8, "center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 577:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change1.pos_hint == {
                    "center_x": .8, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .5,
                                                                                        "center_y": .2} and self.ids.change14.pos_hint == {
                    "center_x": .8, "center_y": .2} :
                    if self.ids.change8.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2}) and self.ids.change10.pos_hint in ( {"center_x": .2, "center_y": .3}, {"center_x": .35, "center_y": .2}) and  self.ids.change5.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2}, {"center_x": .65, "center_y": .2}) and  self.ids.change11.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2}, {"center_x": .65, "center_y": .2}) and  self.ids.change12.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2}, {"center_x": .65, "center_y": .2}) and  self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3},{"center_x": .2, "center_y": .2}, {"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 578:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change2.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} :
                    if self.ids.change8.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}) and self.ids.change10.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 579:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    if self.ids.change15.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .35, "center_y": .3}) and self.ids.change7.pos_hint in ( {"center_x": .5, "center_y": .3}, {"center_x": .35, "center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 580:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change15.pos_hint == {
                    "center_x": .5, "center_y": .3} :
                    if self.ids.change4.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .3}) and self.ids.change6.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 581:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .5, "center_y": .3}  and self.ids.change3.pos_hint == {"center_x": .8, "center_y": .3}:
                    if self.ids.change7.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .3}) and self.ids.change15.pos_hint in ( {"center_x": .65, "center_y": .3}, {"center_x": .35, "center_y": .3}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 582:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .65, "center_y": .3}:
                    if self.ids.change10.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change15.pos_hint in (
                    {"center_x": .2, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)

        elif self.level == 583:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change7.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .65, "center_y": .3}:
                    if self.ids.change10.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change15.pos_hint in (
                    {"center_x": .2, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)

        elif self.level == 584:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change10.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .65, "center_y": .3}:
                    if self.ids.change1.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change14.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .8, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 585:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change14.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change12.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change15.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change2.pos_hint == {"center_x": .8, "center_y": .2}  and self.ids.change8.pos_hint == {"center_x": .2, "center_y": .2} :
                    if self.ids.change3.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,
                                                                                         "center_y": .3}) and self.ids.change6.pos_hint in (
                    {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}) and  self.ids.change10.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .65,"center_y": .2}) and   self.ids.change17.pos_hint in ({"center_x": .8, "center_y": .3}, {"center_x": .65,"center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 586:
            if self.count in ([i for i in range(5, 19)]):
                if self.ids.change9.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8, "center_y": .3}:
                    if self.ids.change14.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,
                                                                                         "center_y": .3}) and self.ids.change17.pos_hint in (
                    {"center_x": .5, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 587:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change3.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change11.pos_hint == {"center_x": .65, "center_y": .2} :
                    if self.ids.change8.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .8,
                                                                                         "center_y": .3}) and self.ids.change10.pos_hint in (
                    {"center_x": .2, "center_y": .3}, {"center_x": .8, "center_y": .3}) and  self.ids.change12.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .2,"center_y": .2}) and   self.ids.change14.pos_hint in ({"center_x": .65, "center_y": .3}, {"center_x": .2,"center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 588:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .5, "center_y": .3} and  self.ids.change14.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change9.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change12.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change16.pos_hint == {"center_x": .35, "center_y": .2} and  self.ids.change3.pos_hint == {"center_x": .65, "center_y": .2} and  self.ids.change1.pos_hint == {"center_x": .8, "center_y": .2} and  self.ids.change10.pos_hint == {"center_x": .35, "center_y": .1}:
                    if self.ids.change5.pos_hint in ({"center_x": .5, "center_y": .2}, {"center_x": .2,
                                                                                         "center_y": .1}) and self.ids.change13.pos_hint in (
                    {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 589:
            if self.count in ([i for i in range(4, 19)]):
                if self.ids.change5.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change6.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .65, "center_y": .3} :
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 590:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change12.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change17.pos_hint == {
                    "center_x": .5, "center_y": .2}:
                    if self.ids.change.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .35,
                                                                                       "center_y": .2}) and self.ids.change16.pos_hint in (
                            {"center_x": .2, "center_y": .3},
                            {"center_x": .35, "center_y": .2}) and self.ids.change4.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change14.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .8, "center_y": .2}) and self.ids.change8.pos_hint in (
                            {"center_x": .2, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change11.pos_hint in (
                            {"center_x": .2, "center_y": .2},
                            {"center_x": .2, "center_y": .1}) and self.ids.change2.pos_hint in (
                            {"center_x": .8, "center_y": .3},
                            {"center_x": .65, "center_y": .2}) and self.ids.change9.pos_hint in (
                            {"center_x": .8, "center_y": .3}, {"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()

                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 591:
            if self.count in ([i for i in range(15, 19)]):
                if self.ids.change11.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .8,
                                                                                       "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .2, "center_y": .2} and self.ids.change16.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change8.pos_hint == {"center_x": .8, "center_y": .2} and self.ids.change4.pos_hint == {"center_x": .2, "center_y": .1} and self.ids.change12.pos_hint == {"center_x": .35, "center_y": .1} and self.ids.change6.pos_hint == {"center_x": .8, "center_y": .1}:
                    if self.ids.change3.pos_hint in ({"center_x": .5, "center_y": .3}, {"center_x": .65,
                                                                                       "center_y": .3}) and self.ids.change15.pos_hint in (
                            {"center_x": .5, "center_y": .3},
                            {"center_x": .65, "center_y": .3}) and self.ids.change14.pos_hint in (
                            {"center_x": .5, "center_y": .2},
                            {"center_x": .65, "center_y": .1}) and self.ids.change7.pos_hint in (
                            {"center_x": .5, "center_y": .2},
                            {"center_x": .65, "center_y": .1}) and self.ids.change.pos_hint in (
                            {"center_x": .35, "center_y": .3},{"center_x": .35, "center_y": .2},{"center_x": .5, "center_y": .1}) and self.ids.change2.pos_hint in (
                            {"center_x": .35, "center_y": .3},{"center_x": .35, "center_y": .2},{"center_x": .5, "center_y": .1}) and self.ids.change13.pos_hint in (
                            {"center_x": .35, "center_y": .3},{"center_x": .35, "center_y": .2},{"center_x": .5, "center_y": .1}) :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                    else:
                        Clock.schedule_once(self.coin_10_loosing)
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)
            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 592:
            if self.count in ([i for i in range(10, 19)]):
                if self.ids.change10.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change14.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3}  and self.ids.change16.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change5.pos_hint == {"center_x": .2, "center_y": .2} and self.ids.change9.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change6.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change17.pos_hint == {"center_x": .65, "center_y": .2} and self.ids.change1.pos_hint == {"center_x": .8, "center_y": .2}:
                    ret_value = self.levels_random()
                    self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 593:
            if self.count in ([i for i in range(9, 19)]):
                if  self.ids.change15.pos_hint == {"center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .5,
                                                                                       "center_y": .3} and self.ids.change3.pos_hint == {
                    "center_x": .65, "center_y": .3}  and self.ids.change17.pos_hint == {"center_x": .8, "center_y": .3} and self.ids.change13.pos_hint == {"center_x": .35, "center_y": .2} and self.ids.change.pos_hint == {"center_x": .5, "center_y": .2} and self.ids.change9.pos_hint == {"center_x": .65, "center_y": .2} :
                    if self.ids.change7.pos_hint in ( {"center_x": .2, "center_y": .3} ,{"center_x": .2, "center_y": .2}) and self.ids.change12.pos_hint in ( {"center_x": .2, "center_y": .3} ,{"center_x": .2, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 594:
            if self.count in ([i for i in range(5, 19)]):
                if  self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {"center_x": .35,
                                                                                       "center_y": .3} and self.ids.change13.pos_hint == {
                    "center_x": .5, "center_y": .3}  and self.ids.change4.pos_hint == {"center_x": .65, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .8, "center_y": .3} :
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 595:
            if self.count in ([i for i in range(4, 19)]):
                if  self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .35,
                                                                                       "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .5, "center_y": .3}  and self.ids.change11.pos_hint == {"center_x": .65, "center_y": .3}:
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 596:
            if self.count in ([i for i in range(7, 19)]):
                if  self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change2.pos_hint == {"center_x": .65,
                                                                                       "center_y": .3} and self.ids.change12.pos_hint == {
                    "center_x": .8, "center_y": .3}  :
                    if self.ids.change.pos_hint in ( {"center_x": .35, "center_y": .3} ,{"center_x": .2, "center_y": .2}) and self.ids.change15.pos_hint in ( {"center_x": .35, "center_y": .3} ,{"center_x": .2, "center_y": .2}) and self.ids.change5.pos_hint in ( {"center_x": .5, "center_y": .3} ,{"center_x": .35, "center_y": .2}) and self.ids.change11.pos_hint in ( {"center_x": .5, "center_y": .3} ,{"center_x": .35, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 597:
            if self.count in ([i for i in range(12, 19)]):
                if self.ids.change6.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change8.pos_hint == {
                    "center_x": .35, "center_y": .3} and self.ids.change11.pos_hint == {"center_x": .5, "center_y": .3} and  self.ids.change14.pos_hint == {"center_x": .65, "center_y": .3} and  self.ids.change9.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change12.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change16.pos_hint == {"center_x": .35, "center_y": .2} and  self.ids.change3.pos_hint == {"center_x": .65, "center_y": .2} and  self.ids.change1.pos_hint == {"center_x": .8, "center_y": .2} and  self.ids.change10.pos_hint == {"center_x": .35, "center_y": .1}:
                    if self.ids.change5.pos_hint in ({"center_x": .5, "center_y": .2}, {"center_x": .2,
                                                                                         "center_y": .1}) and self.ids.change13.pos_hint in (
                    {"center_x": .5, "center_y": .2}, {"center_x": .2, "center_y": .1}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 598:
            if self.count in ([i for i in range(9, 19)]):
                if self.ids.change17.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .5, "center_y": .3} and self.ids.change6.pos_hint == {"center_x": .8, "center_y": .3} and  self.ids.change11.pos_hint == {"center_x": .2, "center_y": .2} and  self.ids.change5.pos_hint == {"center_x": .35, "center_y": .2} and  self.ids.change3.pos_hint == {"center_x": .5, "center_y": .2} and  self.ids.change15.pos_hint == {"center_x": .65, "center_y": .2} :
                    if self.ids.change2.pos_hint in ({"center_x": .35, "center_y": .3}, {"center_x": .65,
                                                                                         "center_y": .3}) and self.ids.change13.pos_hint in (
                    {"center_x": .35, "center_y": .3}, {"center_x": .65, "center_y": .3}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 599:
            if self.count in ([i for i in range(4, 19)]):
                if  self.ids.change8.pos_hint == {"center_x": .2, "center_y": .3} and self.ids.change.pos_hint == {"center_x": .35,
                                                                                       "center_y": .3} and self.ids.change16.pos_hint == {
                    "center_x": .5, "center_y": .3}  and self.ids.change11.pos_hint == {"center_x": .65, "center_y": .3}:
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])
                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)
        elif self.level == 600:
            if self.count in ([i for i in range(11, 19)]):
                if self.ids.change.pos_hint == {"center_x": .5, "center_y": .3} and self.ids.change9.pos_hint == {
                    "center_x": .65, "center_y": .3} and self.ids.change17.pos_hint == {"center_x": .35,
                                                                                        "center_y": .2}:
                    if self.ids.change6.pos_hint in ({"center_x": .2, "center_y": .3}, {"center_x": .2,
                                                                                        "center_y": .2}) and self.ids.change11.pos_hint in (
                    {"center_x": .2, "center_y": .3},
                    {"center_x": .2, "center_y": .2}) and self.ids.change2.pos_hint in (
                    {"center_x": .35, "center_y": .3},
                    {"center_x": .2, "center_y": .1}) and self.ids.change15.pos_hint in (
                    {"center_x": .35, "center_y": .3},
                    {"center_x": .2, "center_y": .1}) and self.ids.change10.pos_hint in (
                    {"center_x": .8, "center_y": .3},
                    {"center_x": .8, "center_y": .2}) and self.ids.change12.pos_hint in (
                    {"center_x": .8, "center_y": .3},
                    {"center_x": .8, "center_y": .2}) and self.ids.change1.pos_hint in (
                    {"center_x": .5, "center_y": .2},
                    {"center_x": .65, "center_y": .2}) and self.ids.change7.pos_hint in (
                    {"center_x": .5, "center_y": .2}, {"center_x": .65, "center_y": .2}):
                        ret_value = self.levels_random()
                        self.question_1_winning_popup(para=list[ret_value])

                else:
                    Clock.schedule_once(self.coin_10_loosing)
            else:
                print('NOTHING')
                Clock.schedule_once(self.coin_10_loosing)

            print(self.count)
            self.count = 0
            print(self.count)




class screenapp(App):
    def build(self):


        self.sm = ScreenManager()
        self.sm.add_widget(home(name="home"))
        self.sm.add_widget(level(name="level"))
        self.sm.add_widget(marvel(name="marvel"))
        self.sm.add_widget(dc(name="dc"))
        self.sm.add_widget(level1(name="game"))
        self.sm.add_widget(phase_2(name="phase2"))
        self.sm.add_widget(phase_3(name = "phase3"))
        self.sm.add_widget(phase_4(name = "phase4"))
        self.sm.current = "home"

        return self.sm
    def change_screen(self):
        self.sm.switch_to(level(),direction = "right")
    def quit_app(self):
        screenapp.stop()

screenapp().run()

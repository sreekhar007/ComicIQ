from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class winninggame:
    def __init__(self):
        pass
    def coin_10_loosing(self, *args):
        if self.ids.change.pos_hint != {"center_x": .12, "center_y": .7}:
            self.ids.change.pos_hint = {"center_x": .12, "center_y": .7}
            self.ids.change.disabled = False
        if self.ids.change1.pos_hint != {"center_x": .27, "center_y": .7}:
            self.ids.change1.pos_hint = {"center_x": .27, "center_y": .7}
            self.ids.change1.disabled = False
        if self.ids.change2.pos_hint != {"center_x": .42, "center_y": .7}:
            self.ids.change2.pos_hint = {"center_x": .42, "center_y": .7}
            self.ids.change2.disabled = False
        if self.ids.change3.pos_hint != {"center_x": .57, "center_y": .7}:
            self.ids.change3.pos_hint = {"center_x": .57, "center_y": .7}
            self.ids.change3.disabled = False
        if self.ids.change4.pos_hint != {"center_x": .72, "center_y": .7}:
            self.ids.change4.pos_hint = {"center_x": .72, "center_y": .7}
            self.ids.change4.disabled = False
        if self.ids.change5.pos_hint != {"center_x": .87, "center_y": .7}:
            self.ids.change5.pos_hint = {"center_x": .87, "center_y": .7}
            self.ids.change5.disabled = False
        if self.ids.change6.pos_hint != {"center_x": .12, "center_y": .62}:
            self.ids.change6.pos_hint = {"center_x": .12, "center_y": .62}
            self.ids.change6.disabled = False
        if self.ids.change7.pos_hint != {"center_x": .27, "center_y": .62}:
            self.ids.change7.pos_hint = {"center_x": .27, "center_y": .62}
            self.ids.change7.disabled = False
        if self.ids.change8.pos_hint != {"center_x": .42, "center_y": .62}:
            self.ids.change8.pos_hint = {"center_x": .42, "center_y": .62}
            self.ids.change8.disabled = False
        if self.ids.change9.pos_hint != {"center_x": .57, "center_y": .62}:
            self.ids.change9.pos_hint = {"center_x": .57, "center_y": .62}
            self.ids.change9.disabled = False
        if self.ids.change10.pos_hint != {"center_x": .72, "center_y": .62}:
            self.ids.change10.pos_hint = {"center_x": .72, "center_y": .62}
            self.ids.change10.disabled = False
        if self.ids.change11.pos_hint != {"center_x": .87, "center_y": .62}:
            self.ids.change11.pos_hint = {"center_x": .87, "center_y": .62}
            self.ids.change11.disabled = False
        if self.ids.change12.pos_hint != {"center_x": .12, "center_y": .54}:
            self.ids.change12.pos_hint = {"center_x": .12, "center_y": .54}
            self.ids.change12.disabled = False
        if self.ids.change13.pos_hint != {"center_x": .27, "center_y": .54}:
            self.ids.change13.pos_hint = {"center_x": .27, "center_y": .54}
            self.ids.change13.disabled = False
        if self.ids.change14.pos_hint != {"center_x": .42, "center_y": .54}:
            self.ids.change14.pos_hint = {"center_x": .42, "center_y": .54}
            self.ids.change14.disabled = False
        if self.ids.change15.pos_hint != {"center_x": .57, "center_y": .54}:
            self.ids.change15.pos_hint = {"center_x": .57, "center_y": .54}
            self.ids.change15.disabled = False
        if self.ids.change16.pos_hint != {"center_x": .72, "center_y": .54}:
            self.ids.change16.pos_hint = {"center_x": .72, "center_y": .54}
            self.ids.change16.disabled = False
        if self.ids.change17.pos_hint != {"center_x": .87, "center_y": .54}:
            self.ids.change17.pos_hint = {"center_x": .87, "center_y": .54}
            self.ids.change17.disabled = False
    def question_1_winning_popup(self, *args, para):
        print("correct")
        self.win_pop = Popup()
        self.win_pop.title = "Good Job!"
        self.win_pop.title_align = "center"
        self.win_pop.title_size = '30sp'
        self.win_pop.separator_height = dp(0)

        self.win_pop.background_color = (73 / 255, 232 / 255, 203 / 255)

        self.layout = BoxLayout()
        self.layout.orientation = "vertical"
        self.lab = Label()
        self.lab.text = "You Won"
        self.lab.font_size = '30sp'

        self.but = Button()

        self.but.text = "Next"
        self.but.size_hint = 1, .1
        self.but.font_size = "20sp"

        self.but.background_color = (228 / 255, 1, 1, 1)
        self.but.bind(on_press=para)
        self.but.pos_hint = {"center_x": .5}
        self.layout.add_widget(self.lab)
        self.layout.add_widget(self.but)
        self.win_pop.add_widget(self.layout)
        self.win_pop.size_hint = 1, 1
        self.win_pop.open()

    def but_state(self):
        self.but = Button()
        return  self.but.state
    def changing_words_blanks(self, levelcounter=None, *args, level, question, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o,
                              p, q, r, em_1, em_2, em_3, em_4, em_5, em_6, em_7, em_8, em_9, em_10, em_11, em_12, em_13,
                              em_14, em_15):
        print("current level", self.level)
        self.count = 0

        self.win_pop.dismiss()
        Clock.schedule_once(self.coin_10_loosing)

        self.json.put("gamescreen", level=level, question=question,
                      words=[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r], levelcounter=levelcounter,
                      vacentbox=[em_1, em_2, em_3, em_4, em_5, em_6, em_7, em_8, em_9, em_10, em_11, em_12, em_13,
                                 em_14,
                                 em_15])
        self.getting_items()

        self.ids.level_indi.text = self.json.get("gamescreen")["levelcounter"]
        self.level = level
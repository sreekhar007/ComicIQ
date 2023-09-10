from kivy.metrics import dp
from kivy.clock import Clock
from kivy.uix.popup import Popup

class logic():
    def __init__(self):
        pass
    def rep(self,*args):
        self.h = Popup()
        self.h.title = ""
        self.h.separator_height = dp(0)
        self.h.size_hint = .2,.1
        self.h.open()






    def hint_coin(self,*args):
        self.hint_count += 1
        self.rep()


        # if self.level == 1:
        #     if self.hint_count == 1:
        #         self.ids.change.pos_hint = {"center_x": .2, "center_y": .3}
        #         self.rep()
        #     elif self.hint_count == 2:
        #         self.ids.change1.pos_hint = {"center_x": .35, "center_y": .3}
        #         self.rep()
        #     elif self.hint_count == 3:
        #         self.ids.change2.pos_hint = {"center_x": .5,"center_y": .3}
        #         self.rep()
        #     elif self.hint_count == 4:
        #         self.ids.change6.pos_hint = {"center_x": .65, "center_y": .3}
        #         self.rep()
        #     elif self.hint_count == 5:
        #         self.ids.change7.pos_hint = {"center_x": .8, "center_y": .3}
        #         self.rep()
        #     elif self.hint_count == 6:
        #         self.ids.change5.pos_hint = {"center_x": .2, "center_y": .2}
        #         self.rep()
        #     elif self.hint_count == 7:
        #         self.ids.change3.pos_hint = {"center_x": .35, "center_y": .2}
        #         self.rep()
        #     elif self.hint_count == 8:
        #         self.ids.change8.pos_hint = {"center_x": .5, "center_y": .2}
        #         self.rep()
        #     elif self.hint_count == 9:
        #         self.ids.change4.pos_hint = {"center_x": .65, "center_y": .2}
        #         self.rep()
        #     elif self.hint_count == 10:
        #         self.ids.change11.pos_hint=  {"center_x": .8, "center_y": .2}
        #         self.rep()
        #     else:
        #         print("hints over")


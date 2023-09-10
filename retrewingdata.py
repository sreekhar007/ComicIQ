from kivy.metrics import dp, cm
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class retrew_data_json():
    def __init__(self,filename):
        self.count = 0


        self.json = JsonStore(filename)

        self.level = self.json.get("gamescreen")["level"]

        self.question = Label()

        self.question.font_size = dp(18)
        self.question.pos_hint = {"center_y": .98, "center_x": .5}
        self.question.text_size = (cm(8), cm(6))


        self.add_widget(self.question)

    def getting_items(self):
        self.question.text = self.json.get("gamescreen")["question"]
        self.ids.level_indi.text = self.json.get("gamescreen")["levelcounter"]
        # we have to use loops
        self.ids.image.source = self.json.get("gamescreen")["words"][0]
        self.ids.image1.source = self.json.get("gamescreen")["words"][1]
        self.ids.image2.source = self.json.get("gamescreen")["words"][2]
        self.ids.image3.source = self.json.get("gamescreen")["words"][3]
        self.ids.image4.source = self.json.get("gamescreen")["words"][4]
        self.ids.image5.source = self.json.get("gamescreen")["words"][5]
        self.ids.image6.source = self.json.get("gamescreen")["words"][6]
        self.ids.image7.source = self.json.get("gamescreen")["words"][7]
        self.ids.image8.source = self.json.get("gamescreen")["words"][8]
        self.ids.image9.source = self.json.get("gamescreen")["words"][9]
        self.ids.image10.source = self.json.get("gamescreen")["words"][10]
        self.ids.image11.source = self.json.get("gamescreen")["words"][11]
        self.ids.image12.source = self.json.get("gamescreen")["words"][12]
        self.ids.image13.source = self.json.get("gamescreen")["words"][13]
        self.ids.image14.source = self.json.get("gamescreen")["words"][14]
        self.ids.image15.source = self.json.get("gamescreen")["words"][15]
        self.ids.image16.source = self.json.get("gamescreen")["words"][16]
        self.ids.image17.source = self.json.get("gamescreen")["words"][17]

        self.ids.borbox.source = self.json.get("gamescreen")["vacentbox"][0]
        self.ids.borbox1.source = self.json.get("gamescreen")["vacentbox"][1]
        self.ids.borbox2.source = self.json.get("gamescreen")["vacentbox"][2]
        self.ids.borbox3.source = self.json.get("gamescreen")["vacentbox"][3]
        self.ids.borbox4.source = self.json.get("gamescreen")["vacentbox"][4]
        self.ids.borbox5.source = self.json.get("gamescreen")["vacentbox"][5]
        self.ids.borbox6.source = self.json.get("gamescreen")["vacentbox"][6]
        self.ids.borbox7.source = self.json.get("gamescreen")["vacentbox"][7]
        self.ids.borbox8.source = self.json.get("gamescreen")["vacentbox"][8]
        self.ids.borbox9.source = self.json.get("gamescreen")["vacentbox"][9]
        self.ids.borbox10.source = self.json.get("gamescreen")["vacentbox"][10]
        self.ids.borbox11.source = self.json.get("gamescreen")["vacentbox"][11]
        self.ids.borbox12.source = self.json.get("gamescreen")["vacentbox"][12]
        self.ids.borbox13.source = self.json.get("gamescreen")["vacentbox"][13]
        self.ids.borbox14.source = self.json.get("gamescreen")["vacentbox"][14]

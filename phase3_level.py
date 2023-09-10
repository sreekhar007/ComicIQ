import kivy
from kivy.storage.jsonstore import JsonStore
import coin_inc
import allhint

import levels_game2
class phase3_questions(coin_inc.coininc,allhint.hint_all):
    def __init__(self):

        # {"gamescreen": {"level": 201, "question": "Who destroyed Asgard in the movie Thor Ragnarok",
        #                 "words": ["wordbox_u.png", "wordbox_e.png", "wordbox_p.png", "wordbox_o.png", "wordbox_r.png",
        #                           "wordbox_h.png", "wordbox_t.png", "wordbox_q.png", "wordbox.png", "wordbox_u.png",
        #                           "wordbox_k.png", "wordbox_l.png", "wordbox_l.png", "wordbox_o.png", "wordbox_r.png",
        #                           "wordbox_h.png", "wordbox_o.png", "wordbox_s.png"], "levelcounter": "1/100",
        #                 "vacentbox": ["bor.png", "bor.png", "bor.png", "bor.png", "bor.png", "bor.png", "mix.png",
        #                               "mix.png", "mix.png", "mix.png", "mix.png", "mix.png", "mix.png", "mix.png",
        #                               "mix.png"]}}
        self.counters = ["2/180", "3/180", "4/180", "5/180", "6/180", "7/180", "8/180", "9/180", "10/180", "11/180",
                         "12/180", "13/180", "14/180", "15/180",
                         "16/180", "17/180", "18/180", "19/180", "20/180", "21/180", "22/180", "23/180", "24/180",
                         "25/180", "26/180", "27/180", "28/180", "29/180", "30/180",
                         "31/180", "32/180", "33/180", "34/180", "35/180", "36/180", "37/180", "38/180", "39/180",
                         "40/180", "41/180", "42/180", "43/180", "44/180", "45/180",
                         "46/180", "47/180", "48/180", "49/180", "50/180", "51/180", "52/180", "53/180", "54/180",
                         "55/180", "56/180", "57/180", "58/180", "59/180", "60/180",
                         "61/180", "62/180", "63/180", "64/180", "65/180", "66/180", "67/180", "68/180", "69/180",
                         "70/180", "71/180", "72/180", "73/180", "74/180", "75/180",
                         "76/180", "77/180", "78/180", "79/180", "80/180", "81/180", "82/180", "83/180", "84/180",
                         "85/180", "86/180", "87/180", "88/180", "89/180", "90/180",
                         "91/180", "92/180", "93/180", "94/180", "95/180", "96/180", "97/180", "98/180", "99/180",
                         "100/180", "101/180", "102/180", "103/180", "104/180", "105/180", "106/180", "107/180",
                         "108/180", "109/180", "110/180", "111/180", "112/180", "113/180", "114/180", "115/180",
                         "116/180", "117/180", "118/180", "119/180", "120/180", "121/180", "122/180", "123/180",
                         "124/180", "125/180", "126/180", "127/180", "128/180", "129/180", "130/180", "131/180",
                         "132/180", "133/180", "134/180", "135/180", "136/180", "137/180", "138/180", "139/180",
                         "140/180", "141/180", "142/180", "143/180", "144/180", "145/180", "146/180", "147/180",
                         "148/180", "149/180", "150/180", "151/180", "152/180", "153/180", "154/180", "155/180",
                         "156/180", "157/180", "158/180", "159/180", "160/180", "161/180", "162/180", "163/180",
                         "164/180", "165/180", "166/180", "167/180", "168/180", "169/180", "170/180", "171/180",
                         "172/180", "173/180", "174/180", "175/180", "176/180", "177/180", "178/180", "179/180",
                         "180/180"]
    def counter(self,*args):

        lev_coun = JsonStore("counter2.json")
        lst = lev_coun.get("random_level_list")["number"]
        s = lev_coun.get("random_level_list")["number"][0]

        lst.remove(s)
        lev_coun.put("random_level_list",number = lst )

        return  self.counters[s]
    def  level_202_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=202,
                                   question="Who is the main villain in the movie Thor Ragnarok",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_s.png", c="wordbox_k.png", d="wordbox_s.png",
                                   e="wordbox_p.png", f="wordbox_e.png", g="wordbox_i.png",
                                   h="wordbox_t.png", i="wordbox_q.png", j="wordbox_k.png",
                                   k="wordbox_f.png", l="wordbox_n.png", m="wordbox.png",
                                   n="wordbox_o.png", o="wordbox_p.png", p="wordbox_s.png",
                                   q="wordbox_d.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_203_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=203,
                                   question="By whom was Thor's hammer Mjølnir destroyed in the movie Thor Ragnarok",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_s.png", c="wordbox_k.png", d="wordbox_s.png",
                                   e="wordbox_p.png", f="wordbox_e.png", g="wordbox_i.png",
                                   h="wordbox_t.png", i="wordbox_q.png", j="wordbox_k.png",
                                   k="wordbox_f.png", l="wordbox_n.png", m="wordbox.png",
                                   n="wordbox_o.png", o="wordbox_p.png", p="wordbox_s.png",
                                   q="wordbox_d.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_204_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=204,
                                   question="Who was the champion on the Sakaar planet in the movie Thor Ragnarok",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_p.png", c="wordbox_h.png", d="wordbox_s.png", e="wordbox_m.png",
                                   f="wordbox_n.png",
                                   g="wordbox.png", h="wordbox_l.png", i="wordbox_z.png", j="wordbox_t.png",
                                   k="wordbox_u.png",
                                   l="wordbox_j.png", m="wordbox_f.png", n="wordbox_q.png", o="wordbox_p.png",
                                   p="wordbox_k.png", q="wordbox_t.png", r="wordbox_g.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_205_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=205,
                                   question="Where was Odin located on Earth in the movie Thor Ragnarok",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_p.png", c="wordbox_s.png", d="wordbox_t.png", e="wordbox_y.png",
                                   f="wordbox_v.png",
                                   g="wordbox.png", h="wordbox_d.png", i="wordbox_o.png", j="wordbox_k.png",
                                   k="wordbox_v.png",
                                   l="wordbox_q.png", m="wordbox_n.png", n="wordbox_m.png", o="wordbox_t.png",
                                   p="wordbox_u.png", q="wordbox_w.png", r="wordbox_l.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_206_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=206,
                                   question="By whom was Asgard destroyed in the movie Thor Ragnarok",
                                   levelcounter=str(self.count), a="wordbox_u.png",
                                   b="wordbox_e.png", c="wordbox_p.png", d="wordbox_o.png", e="wordbox_r.png",
                                   f="wordbox_h.png",
                                   g="wordbox_t.png", h="wordbox_q.png", i="wordbox.png", j="wordbox_u.png",
                                   k="wordbox_k.png",
                                   l="wordbox_l.png", m="wordbox_l.png", n="wordbox_o.png", o="wordbox_r.png",
                                   p="wordbox_h.png", q="wordbox_o.png", r="wordbox_s.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_207_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=207,
                                   question="What is the name of Thor's sister",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_s.png", c="wordbox_k.png", d="wordbox_s.png",
                                   e="wordbox_p.png", f="wordbox_e.png", g="wordbox_i.png",
                                   h="wordbox_t.png", i="wordbox_q.png", j="wordbox_k.png",
                                   k="wordbox_f.png", l="wordbox_n.png", m="wordbox.png",
                                   n="wordbox_o.png", o="wordbox_p.png", p="wordbox_s.png",
                                   q="wordbox_d.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_208_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=208,
                                   question="Who assists Thor in his journey from the planet Sakaar to Asgard, making this voyage possible",
                                   levelcounter=str(self.count), a="wordbox_y.png",
                                   b="wordbox_t.png", c="wordbox_p.png", d="wordbox.png",
                                   e="wordbox_m.png", f="wordbox_r.png", g="wordbox_v.png",
                                   h="wordbox_p.png", i="wordbox_e.png", j="wordbox_s.png",
                                   k="wordbox_c.png", l="wordbox_l.png", m="wordbox_i.png",
                                   n="wordbox_n.png", o="wordbox_k.png", p="wordbox_j.png",
                                   q="wordbox_q.png", r="wordbox_t.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_209_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=209,
                                   question="Who was the character responsible for organizing and overseeing the gladiatorial fights on the planet Sakaar",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_d.png", c="wordbox_k.png", d="wordbox_c.png",
                                   e="wordbox_e.png", f="wordbox.png", g="wordbox_g.png",
                                   h="wordbox_t.png", i="wordbox_r.png", j="wordbox_q.png",
                                   k="wordbox_v.png", l="wordbox_n.png", m="wordbox.png",
                                   n="wordbox_s.png", o="wordbox_o.png", p="wordbox_u.png",
                                   q="wordbox_p.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_210_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=210,
                                   question="On which planet do Thor and Loki land after falling from the Bifrost in the movie Thor Ragnarok",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_q.png", c="wordbox_p.png", d="wordbox_u.png",
                                   e="wordbox_v.png", f="wordbox.png", g="wordbox_n.png",
                                   h="wordbox_c.png", i="wordbox_q.png", j="wordbox.png",
                                   k="wordbox_r.png", l="wordbox_v.png", m="wordbox_k.png",
                                   n="wordbox_n.png", o="wordbox_c.png", p="wordbox_s.png",
                                   q="wordbox_p.png", r="wordbox_t.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_211_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=211,
                                   question="Where was Doctor Strange located in Earth in the movie Thor Ragnarok",
                                   levelcounter=str(self.count),a="wordbox_f.png",
                                   b="wordbox_d.png", c="wordbox_y.png", d="wordbox.png", e="wordbox_r.png",
                                   f="wordbox_k.png",
                                   g="wordbox_e.png", h="wordbox_p.png", i="wordbox_s.png", j="wordbox_w.png",
                                   k="wordbox_c.png",
                                   l="wordbox_o.png", m="wordbox_m.png", n="wordbox_s.png", o="wordbox_l.png",
                                   p="wordbox_t.png", q="wordbox_n.png", r="wordbox_q.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")

    def level_212_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=212,
                                   question="Who causes Thor to lose his Right eye in the movie Thor Ragnarok",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_s.png", c="wordbox_k.png", d="wordbox_s.png",
                                   e="wordbox_p.png", f="wordbox_e.png", g="wordbox_i.png",
                                   h="wordbox_t.png", i="wordbox_q.png", j="wordbox_k.png",
                                   k="wordbox_f.png", l="wordbox_n.png", m="wordbox.png",
                                   n="wordbox_o.png", o="wordbox_p.png", p="wordbox_s.png",
                                   q="wordbox_d.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_213_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=213,
                                   question="From which realm does Hela originate in the movie Thor Ragnarok",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_k.png", c="wordbox_t.png", d="wordbox_p.png",
                                   e="wordbox_t.png", f="wordbox_o.png", g="wordbox_v.png",
                                   h="wordbox_n.png", i="wordbox_e.png", j="wordbox_s.png",
                                   k="wordbox_c.png", l="wordbox_u.png", m="wordbox_l.png",
                                   n="wordbox_u.png", o="wordbox_q.png", p="wordbox_n.png",
                                   q="wordbox_d.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_214_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=214,
                                   question="What is the name of the stick wielded by the Grandmaster in the movie Thor Ragnarok",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_n.png", c="wordbox_m.png", d="wordbox_s.png",
                                   e="wordbox_q.png", f="wordbox_y.png", g="wordbox_e.png",
                                   h="wordbox_o.png", i="wordbox_l.png", j="wordbox_p.png",
                                   k="wordbox_v.png", l="wordbox_b.png", m="wordbox_o.png",
                                   n="wordbox_t.png", o="wordbox_o.png", p="wordbox_n.png",
                                   q="wordbox_u.png", r="wordbox.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_215_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=215,
                                   question="Who assists Thor in robbing the Grandmaster's spaceship in the movie Thor Ragnarok",
                                   levelcounter=str(self.count), a="wordbox_f.png",
                                   b="wordbox.png", c="wordbox_l.png", d="wordbox_e.png", e="wordbox_q.png",
                                   f="wordbox_s.png",
                                   g="wordbox_k.png", h="wordbox_n.png", i="wordbox_b.png", j="wordbox_w.png",
                                   k="wordbox_e.png",
                                   l="wordbox_i.png", m="wordbox_m.png", n="wordbox_p.png", o="wordbox_f.png",
                                   p="wordbox_h.png", q="wordbox_o.png", r="wordbox_g.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_216_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=216,
                                   question="What is Odin's main power in the Marvel Cinematic Universe (MCU)",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_t.png", c="wordbox_r.png", d="wordbox_q.png", e="wordbox_c.png",
                                   f="wordbox_m.png",
                                   g="wordbox_i.png", h="wordbox_p.png", i="wordbox_d.png", j="wordbox_s.png",
                                   k="wordbox_n.png",
                                   l="wordbox_b.png", m="wordbox.png", n="wordbox_f.png", o="wordbox_u.png",
                                   p="wordbox_e.png", q="wordbox_v.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_217_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=217,
                                   question="What is the name of Hela's army in the movie Thor Ragnarok",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_o.png", c="wordbox_r.png", d="wordbox_k.png", e="wordbox_h.png",
                                   f="wordbox_s.png",
                                   g="wordbox_e.png", h="wordbox_j.png", i="wordbox_o.png", j="wordbox_e.png",
                                   k="wordbox_d.png",
                                   l="wordbox_r.png", m="wordbox.png", n="wordbox_m.png", o="wordbox_i.png",
                                   p="wordbox_b.png", q="wordbox_n.png", r="wordbox_c.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_218_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=218,
                                   question="Who played the role of the barber in the movie Thor Ragnarok",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_d.png", c="wordbox_e.png", d="wordbox_f.png", e="wordbox_c.png",
                                   f="wordbox.png",
                                   g="wordbox_t.png", h="wordbox_o.png", i="wordbox_p.png", j="wordbox_l.png",
                                   k="wordbox_d.png",
                                   l="wordbox_n.png", m="wordbox_m.png", n="wordbox_p.png", o="wordbox_s.png",
                                   p="wordbox_b.png", q="wordbox_o.png", r="wordbox_e.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_219_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=219,
                                   question="Who is the fellow jailer and ally to Thor in the movie Thor Ragnarok",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_p.png", c="wordbox_m.png", d="wordbox_u.png", e="wordbox_c.png",
                                   f="wordbox_m.png",
                                   g="wordbox_t.png", h="wordbox_s.png", i="wordbox_o.png", j="wordbox_n.png",
                                   k="wordbox_b.png",
                                   l="wordbox_h.png", m="wordbox_v.png", n="wordbox_g.png", o="wordbox_s.png",
                                   p="wordbox_r.png", q="wordbox_t.png", r="wordbox_u.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_220_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=220,
                                   question="What is the name of Korg's friend in the movie Thor Ragnarok",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_p.png", c="wordbox_o.png", d="wordbox_u.png", e="wordbox_c.png",
                                   f="wordbox_n.png",
                                   g="wordbox_t.png", h="wordbox_s.png", i="wordbox_m.png", j="wordbox_n.png",
                                   k="wordbox_b.png",
                                   l="wordbox_i.png", m="wordbox_v.png", n="wordbox_g.png", o="wordbox_s.png",
                                   p="wordbox_e.png", q="wordbox_t.png", r="wordbox_u.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_221_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=221,
                                   question="what is the name of the Neurosurgeon doctor in the Doctor Strange movie",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_h.png", c="wordbox_k.png", d="wordbox_s.png", e="wordbox.png",
                                   f="wordbox_e.png",
                                   g="wordbox_s.png", h="wordbox_o.png", i="wordbox_n.png", j="wordbox_u.png",
                                   k="wordbox_t.png",
                                   l="wordbox_p.png", m="wordbox_e.png", n="wordbox_d.png", o="wordbox_t.png",
                                   p="wordbox_g.png", q="wordbox_r.png", r="wordbox_n.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="bor.png", em_15="mix.png")
    def level_222_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=222,
                                   question="Which part of Doctor Strange's body was affected in the car accident depicted in the Doctor Strange movie",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_t.png", c="wordbox_o.png", d="wordbox_d.png", e="wordbox_p.png",
                                   f="wordbox_m.png",
                                   g="wordbox_h.png", h="wordbox_k.png", i="wordbox_u.png", j="wordbox_o.png",
                                   k="wordbox_s.png",
                                   l="wordbox_l.png", m="wordbox_o.png", n="wordbox_b.png", o="wordbox.png",
                                   p="wordbox_g.png", q="wordbox_c.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_223_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=223,
                                   question="Where does Stephen Strange go to seek a solution for his hands in the movie Doctor Strange",
                                   levelcounter=str(self.count), a="wordbox_j.png",
                                   b="wordbox_o.png", c="wordbox.png", d="wordbox_n.png", e="wordbox_r.png",
                                   f="wordbox_p.png",
                                   g="wordbox.png", h="wordbox_u.png", i="wordbox_k.png", j="wordbox_b.png",
                                   k="wordbox_v.png",
                                   l="wordbox.png", m="wordbox_c.png", n="wordbox_m.png", o="wordbox_q.png",
                                   p="wordbox_s.png", q="wordbox_t.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_224_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=224,
                                   question="In which country is the mystical location of Kamar-Taj situated in the movie Doctor Strange",
                                   levelcounter=str(self.count), a="wordbox_c.png",
                                   b="wordbox_v.png", c="wordbox_m.png", d="wordbox_p.png", e="wordbox_u.png",
                                   f="wordbox_s.png",
                                   g="wordbox_n.png", h="wordbox_j.png", i="wordbox_o.png", j="wordbox_k.png",
                                   k="wordbox_l.png",
                                   l="wordbox_m.png", m="wordbox_t.png", n="wordbox.png", o="wordbox_q.png",
                                   p="wordbox_b.png", q="wordbox_h.png", r="wordbox_e.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_225_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=225,
                                   question="What is the name of the locket that Doctor Strange wears",
                                   levelcounter=str(self.count), a="wordbox_y.png",
                                   b="wordbox.png", c="wordbox_m.png", d="wordbox_b.png", e="wordbox_k.png",
                                   f="wordbox_o.png",
                                   g="wordbox_o.png", h="wordbox_t.png", i="wordbox_g.png", j="wordbox_t.png",
                                   k="wordbox_f.png",
                                   l="wordbox_n.png", m="wordbox_e.png", n="wordbox.png", o="wordbox_o.png",
                                   p="wordbox_u.png", q="wordbox_q.png", r="wordbox_e.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="mix.png", em_15="mix.png")
    def level_226_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=226,
                                   question="What is the name of the stone contained within the Eye of Agamotto locket",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_t.png", c="wordbox_m.png", d="wordbox_e.png", e="wordbox_s.png",
                                   f="wordbox_h.png",
                                   g="wordbox_l.png", h="wordbox_r.png", i="wordbox_c.png", j="wordbox_n.png",
                                   k="wordbox_d.png",
                                   l="wordbox_o.png", m="wordbox_x.png", n="wordbox_g.png", o="wordbox.png",
                                   p="wordbox_b.png", q="wordbox_u.png", r="wordbox_f.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_227_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=227,
                                   question="Who is the greatest student in Kamar-Taj in the past, as depicted in the movie Doctor Strange",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox_o.png", c="wordbox_i.png", d="wordbox_n.png", e="wordbox_e.png",
                                   f="wordbox_l.png",
                                   g="wordbox_k.png", h="wordbox_q.png", i="wordbox_u.png", j="wordbox_t.png",
                                   k="wordbox_p.png",
                                   l="wordbox_i.png", m="wordbox_c.png", n="wordbox_p.png", o="wordbox.png",
                                   p="wordbox_b.png", q="wordbox_s.png", r="wordbox_v.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_228_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=228,
                                   question="What is the name of the main villain in the movie Doctor Strange",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox_o.png", c="wordbox_i.png", d="wordbox_n.png", e="wordbox_e.png",
                                   f="wordbox_l.png",
                                   g="wordbox_k.png", h="wordbox_q.png", i="wordbox_u.png", j="wordbox_t.png",
                                   k="wordbox_p.png",
                                   l="wordbox_i.png", m="wordbox_c.png", n="wordbox_p.png", o="wordbox.png",
                                   p="wordbox_b.png", q="wordbox_s.png", r="wordbox_v.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_229_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=229,
                                   question="Who was the head of the library in Kamar-Taj in the movie Doctor Strange",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_t.png", c="wordbox_f.png", d="wordbox_v.png", e="wordbox_b.png",
                                   f="wordbox_w.png",
                                   g="wordbox_o.png", h="wordbox_l.png", i="wordbox_m.png", j="wordbox_t.png",
                                   k="wordbox_u.png",
                                   l="wordbox_c.png", m="wordbox.png", n="wordbox_g.png", o="wordbox_q.png",
                                   p="wordbox_m.png", q="wordbox_s.png", r="wordbox_n.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_230_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=230,
                                   question="To which dimension does the Ancient One take Stephen Strange ,in the movie Doctor Strange",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_t.png", c="wordbox_r.png", d="wordbox_u.png", e="wordbox_o.png",
                                   f="wordbox.png",
                                   g="wordbox_d.png", h="wordbox_i.png", i="wordbox_o.png", j="wordbox_l.png",
                                   k="wordbox_m.png",
                                   l="wordbox_g.png", m="wordbox_s.png", n="wordbox_o.png", o="wordbox_i.png",
                                   p="wordbox_k.png", q="wordbox_h.png", r="wordbox_m.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_231_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=231,
                                   question="Who is the ruler of the Dark Dimension",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_n.png", c="wordbox_t.png", d="wordbox_g.png", e="wordbox_q.png",
                                   f="wordbox_m.png",
                                   g="wordbox_m.png", h="wordbox_k.png", i="wordbox_t.png", j="wordbox_d.png",
                                   k="wordbox_v.png",
                                   l="wordbox_u.png", m="wordbox.png", n="wordbox_b.png", o="wordbox_m.png",
                                   p="wordbox_h.png", q="wordbox_c.png", r="wordbox_r.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_232_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=232,
                                   question="Who tore the pages from the Book of Cagliostro in the movie Doctor Strange",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox_o.png", c="wordbox_i.png", d="wordbox_n.png", e="wordbox_e.png",
                                   f="wordbox_l.png",
                                   g="wordbox_k.png", h="wordbox_q.png", i="wordbox_u.png", j="wordbox_t.png",
                                   k="wordbox_p.png",
                                   l="wordbox_i.png", m="wordbox_c.png", n="wordbox_p.png", o="wordbox.png",
                                   p="wordbox_b.png", q="wordbox_s.png", r="wordbox_v.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_233_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=233,
                                   question="What is the name of the book from which Kaecilius tears off the pages in the movie Doctor Strange",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_q.png", c="wordbox_g.png", d="wordbox_v.png", e="wordbox_n.png",
                                   f="wordbox_s.png",
                                   g="wordbox_t.png", h="wordbox_h.png", i="wordbox_c.png", j="wordbox_u.png",
                                   k="wordbox_p.png",
                                   l="wordbox_l.png", m="wordbox.png", n="wordbox_k.png", o="wordbox_i.png",
                                   p="wordbox_h.png", q="wordbox_r.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_234_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=234,
                                   question="Who traps Dormammu in the Infinity Time Loop in the movie Doctor Strange",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_k.png", c="wordbox_s.png", d="wordbox_p.png", e="wordbox_g.png",
                                   f="wordbox_r.png",
                                   g="wordbox_d.png", h="wordbox_v.png", i="wordbox_t.png", j="wordbox_e.png",
                                   k="wordbox.png",
                                   l="wordbox_t.png", m="wordbox_r.png", n="wordbox_q.png", o="wordbox_n.png",
                                   p="wordbox_c.png", q="wordbox_m.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="mix.png", em_15="mix.png")
    def level_235_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=235,
                                   question="Who becomes the protector of the Time Stone after the death of the Ancient One in the movie Doctor Strange",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_k.png", c="wordbox_s.png", d="wordbox_p.png", e="wordbox_g.png",
                                   f="wordbox_r.png",
                                   g="wordbox_d.png", h="wordbox_v.png", i="wordbox_t.png", j="wordbox_e.png",
                                   k="wordbox.png",
                                   l="wordbox_t.png", m="wordbox_r.png", n="wordbox_q.png", o="wordbox_n.png",
                                   p="wordbox_c.png", q="wordbox_m.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="mix.png", em_15="mix.png")
    def level_236_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=236, question="To which Sanctum does Stephen Strange enter during the fight with Kaecilius in the movie Doctor Strange",
                                   levelcounter=str(self.count), a="wordbox_f.png",
                                   b="wordbox_d.png", c="wordbox_y.png", d="wordbox.png", e="wordbox_r.png",
                                   f="wordbox_k.png",
                                   g="wordbox_e.png", h="wordbox_p.png", i="wordbox_s.png", j="wordbox_w.png",
                                   k="wordbox_c.png",
                                   l="wordbox_o.png", m="wordbox_m.png", n="wordbox_s.png", o="wordbox_l.png",
                                   p="wordbox_t.png", q="wordbox_n.png", r="wordbox_q.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_237_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=237,
                                   question="Who welcomes Stephen Strange to Kamar-Taj in the movie Doctor Strange",
                                   levelcounter=str(self.count), a="wordbox_d.png",
                                   b="wordbox_p.png", c="wordbox_q.png", d="wordbox_s.png", e="wordbox_o.png",
                                   f="wordbox_u.png",
                                   g="wordbox_o.png", h="wordbox_k.png", i="wordbox_t.png", j="wordbox_v.png",
                                   k="wordbox_m.png",
                                   l="wordbox_h.png", m="wordbox_b.png", n="wordbox_y.png", o="wordbox_r.png",
                                   p="wordbox_v.png", q="wordbox_c.png", r="wordbox_n.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_238_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=238,
                                   question="What is the name of Doctor Strange's primary magical technique",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_t.png", c="wordbox_l.png", d="wordbox_u.png", e="wordbox_o.png",
                                   f="wordbox_g.png",
                                   g="wordbox_o.png", h="wordbox_n.png", i="wordbox_k.png", j="wordbox_s.png",
                                   k="wordbox_r.png",
                                   l="wordbox_c.png", m="wordbox_g.png", n="wordbox_v.png", o="wordbox_t.png",
                                   p="wordbox_n.png", q="wordbox_u.png", r="wordbox_i.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_239_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=239,
                                   question="In which dimension does Dormammu reside in the movie Doctor Strange",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_t.png", c="wordbox_r.png", d="wordbox_u.png", e="wordbox_o.png",
                                   f="wordbox.png",
                                   g="wordbox_d.png", h="wordbox_i.png", i="wordbox_o.png", j="wordbox_l.png",
                                   k="wordbox_m.png",
                                   l="wordbox_g.png", m="wordbox_s.png", n="wordbox_o.png", o="wordbox_i.png",
                                   p="wordbox_k.png", q="wordbox_h.png", r="wordbox_m.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_240_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=240,
                                   question="What is the name of the mystical practice and abilities of Doctor Strange",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_k.png", c="wordbox_y.png", d="wordbox_l.png", e="wordbox_r.png",
                                   f="wordbox_t.png",
                                   g="wordbox.png", h="wordbox_y.png", i="wordbox_m.png", j="wordbox_u.png",
                                   k="wordbox_h.png",
                                   l="wordbox_c.png", m="wordbox_t.png", n="wordbox_q.png", o="wordbox_i.png",
                                   p="wordbox_v.png", q="wordbox_b.png", r="wordbox_s.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_241_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=241,
                                   question="What is the name of the person who plays the role of Peter Parker in SpiderMan Homecomming",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_d.png", c="wordbox_f.png", d="wordbox_t.png", e="wordbox.png",
                                   f="wordbox_l.png",
                                   g="wordbox_s.png", h="wordbox_u.png", i="wordbox_k.png", j="wordbox_m.png",
                                   k="wordbox_n.png",
                                   l="wordbox_q.png", m="wordbox_l.png", n="wordbox_h.png", o="wordbox_v.png",
                                   p="wordbox_s.png", q="wordbox_p.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_242_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=242,
                                   question="What is the name of Adrian Toomes' daughter in the movie SpiderMan Homecoming",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_k.png", c="wordbox_o.png", d="wordbox_q.png", e="wordbox_v.png",
                                   f="wordbox_z.png",
                                   g="wordbox_m.png", h="wordbox_x.png", i="wordbox_l.png", j="wordbox_b.png",
                                   k="wordbox_u.png",
                                   l="wordbox_s.png", m="wordbox_o.png", n="wordbox_c.png", o="wordbox_e.png",
                                   p="wordbox_j.png", q="wordbox_n.png", r="wordbox_i.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_243_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=243,
                                   question="Whom does Peter Parker invite to the Homecoming party in the movie SpiderMan Homecoming",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_k.png", c="wordbox_o.png", d="wordbox_q.png", e="wordbox_v.png",
                                   f="wordbox_z.png",
                                   g="wordbox_m.png", h="wordbox_x.png", i="wordbox_l.png", j="wordbox_b.png",
                                   k="wordbox_u.png",
                                   l="wordbox_s.png", m="wordbox_o.png", n="wordbox_c.png", o="wordbox_e.png",
                                   p="wordbox_j.png", q="wordbox_n.png", r="wordbox_i.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_244_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=244,
                                   question="Who sent the FBI agents to the Staten Island Ferry in the movie SpiderMan Homecoming",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_p.png", c="wordbox_k.png", d="wordbox_t.png", e="wordbox_m.png",
                                   f="wordbox_o.png",
                                   g="wordbox.png", h="wordbox_d.png", i="wordbox_t.png", j="wordbox_l.png",
                                   k="wordbox_y.png",
                                   l="wordbox_m.png", m="wordbox_n.png", n="wordbox_q.png", o="wordbox_g.png",
                                   p="wordbox_r.png", q="wordbox_v.png", r="wordbox_k.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_245_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=245,
                                   question="Who came to save the passengers and Spider-Man in the Staten Island Ferry in Spiderman Homecoming",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_f.png", c="wordbox_i.png", d="wordbox_q.png", e="wordbox_c.png",
                                   f="wordbox.png",
                                   g="wordbox_p.png", h="wordbox_s.png", i="wordbox_m.png", j="wordbox_j.png",
                                   k="wordbox_g.png",
                                   l="wordbox_c.png", m="wordbox_r.png", n="wordbox_o.png", o="wordbox_b.png",
                                   p="wordbox_h.png", q="wordbox_l.png", r="wordbox_n.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_246_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=246,
                                   question="What is the name of the girl that Peter Parker wants to date in Spiderman Homecoming",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_k.png", c="wordbox_o.png", d="wordbox_q.png", e="wordbox_v.png",
                                   f="wordbox_z.png",
                                   g="wordbox_m.png", h="wordbox_x.png", i="wordbox_l.png", j="wordbox_b.png",
                                   k="wordbox_u.png",
                                   l="wordbox_s.png", m="wordbox_o.png", n="wordbox_c.png", o="wordbox_e.png",
                                   p="wordbox_j.png", q="wordbox_n.png", r="wordbox_i.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_247_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=247,
                                   question="Who gifts the Spider-Man suit to Peter Parker in Spiderman Homecoming",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_p.png", c="wordbox_k.png", d="wordbox_t.png", e="wordbox_m.png",
                                   f="wordbox_o.png",
                                   g="wordbox.png", h="wordbox_d.png", i="wordbox_t.png", j="wordbox_l.png",
                                   k="wordbox_y.png",
                                   l="wordbox_m.png", m="wordbox_n.png", n="wordbox_q.png", o="wordbox_g.png",
                                   p="wordbox_r.png", q="wordbox_v.png", r="wordbox_k.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_248_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=248,
                                   question="Who installed a tracker in the Spider-Man suit in Spiderman Homecoming",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_p.png", c="wordbox_k.png", d="wordbox_t.png", e="wordbox_m.png",
                                   f="wordbox_o.png",
                                   g="wordbox.png", h="wordbox_d.png", i="wordbox_t.png", j="wordbox_l.png",
                                   k="wordbox_y.png",
                                   l="wordbox_m.png", m="wordbox_n.png", n="wordbox_q.png", o="wordbox_g.png",
                                   p="wordbox_r.png", q="wordbox_v.png", r="wordbox_k.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_249_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=249,
                                   question="What is the name of the technology used by Adrian Toomes to make money in Spiderman Homecoming",
                                   levelcounter=str(self.count), a="wordbox_f.png",
                                   b="wordbox_t.png", c="wordbox_p.png", d="wordbox_h.png", e="wordbox_k.png",
                                   f="wordbox_i.png",
                                   g="wordbox_o.png", h="wordbox_m.png", i="wordbox_c.png", j="wordbox_q.png",
                                   k="wordbox_r.png",
                                   l="wordbox_v.png", m="wordbox.png", n="wordbox_g.png", o="wordbox_i.png",
                                   p="wordbox_f.png", q="wordbox_u.png", r="wordbox_b.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_250_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=250,
                                   question="What is the name of the artificial intelligence system in the Spider-Man suit in Spiderman Homecoming",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_s.png", c="wordbox_d.png", d="wordbox_f.png", e="wordbox_r.png",
                                   f="wordbox_q.png",
                                   g="wordbox_v.png", h="wordbox_p.png", i="wordbox_n.png", j="wordbox_y.png",
                                   k="wordbox_t.png",
                                   l="wordbox_q.png", m="wordbox_e.png", n="wordbox_m.png", o="wordbox_x.png",
                                   p="wordbox.png", q="wordbox_h.png", r="wordbox_l.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_251_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=251,
                                   question="What is the name of Peter Parker's best friend in Spiderman Homecoming",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox.png", c="wordbox_d.png", d="wordbox_q.png", e="wordbox_p.png",
                                   f="wordbox_u.png",
                                   g="wordbox_l.png", h="wordbox_n.png", i="wordbox_e.png", j="wordbox_v.png",
                                   k="wordbox_s.png",
                                   l="wordbox_t.png", m="wordbox_k.png", n="wordbox_f.png", o="wordbox_d.png",
                                   p="wordbox_u.png", q="wordbox_m.png", r="wordbox_e.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_252_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=252,
                                   question="Who portrayed the villain in the movie SpiderMan Homecoming",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_p.png", c="wordbox_o.png", d="wordbox_u.png", e="wordbox_m.png",
                                   f="wordbox_d.png",
                                   g="wordbox_k.png", h="wordbox_s.png", i="wordbox_l.png", j="wordbox_b.png",
                                   k="wordbox_q.png",
                                   l="wordbox_t.png", m="wordbox_u.png", n="wordbox_c.png", o="wordbox_q.png",
                                   p="wordbox_v.png", q="wordbox_y.png", r="wordbox_e.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_253_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=253,
                                   question="What is the name of Peter Quill's father in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_g.png", c="wordbox_t.png", d="wordbox_l.png", e="wordbox_s.png",
                                   f="wordbox_u.png",
                                   g="wordbox_m.png", h="wordbox_d.png", i="wordbox_e.png", j="wordbox_k.png",
                                   k="wordbox_s.png",
                                   l="wordbox_n.png", m="wordbox_h.png", n="wordbox_n.png", o="wordbox_f.png",
                                   p="wordbox.png", q="wordbox_o.png", r="wordbox_l.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_254_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=254,
                                   question="Who is the leader of the Sovereign people in the movie Guardians ofthe Galaxy Vol 2",
                                   levelcounter=str(self.count), a="wordbox_y.png",
                                   b="wordbox_p.png", c="wordbox_k.png", d="wordbox_s.png", e="wordbox_l.png",
                                   f="wordbox_f.png",
                                   g="wordbox.png", h="wordbox_n.png", i="wordbox_k.png", j="wordbox.png",
                                   k="wordbox_t.png",
                                   l="wordbox_p.png", m="wordbox_h.png", n="wordbox_o.png", o="wordbox_q.png",
                                   p="wordbox_j.png", q="wordbox_f.png", r="wordbox_e.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_255_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=255,
                                   question="What type of batteries did Rocket steal from the Sovereign planet in Guardians of the Galaxy Vol 2",
                                   levelcounter=str(self.count), a="wordbox_u.png",
                                   b="wordbox_t.png", c="wordbox_s.png", d="wordbox_p.png", e="wordbox_q.png",
                                   f="wordbox.png",
                                   g="wordbox_o.png", h="wordbox.png", i="wordbox_t.png", j="wordbox_y.png",
                                   k="wordbox_l.png",
                                   l="wordbox_m.png", m="wordbox_x.png", n="wordbox_s.png", o="wordbox_j.png",
                                   p="wordbox_n.png", q="wordbox_h.png", r="wordbox_q.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_256_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=256,
                                   question="Who places and triggers the bomb inside Ego's planet in Guardians of the Galaxy Vol 2",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_d.png", c="wordbox_f.png", d="wordbox_g.png",
                                   e="wordbox_e.png", f="wordbox_o.png", g="wordbox_h.png",
                                   h="wordbox_k.png", i="wordbox_r.png", j="wordbox_h.png",
                                   k="wordbox_j.png", l="wordbox_b.png", m="wordbox_o.png",
                                   n="wordbox_l.png", o="wordbox_i.png", p="wordbox_k.png",
                                   q="wordbox_c.png", r="wordbox_t.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_257_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=257,
                                   question="What is the name of Ego's son",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_o.png", c="wordbox_j.png", d="wordbox_u.png",
                                   e="wordbox_f.png", f="wordbox_l.png", g="wordbox_k.png",
                                   h="wordbox_l.png", i="wordbox_q.png", j="wordbox_p.png",
                                   k="wordbox_m.png", l="wordbox_i.png", m="wordbox_e.png",
                                   n="wordbox_k.png", o="wordbox_y.png", p="wordbox_e.png",
                                   q="wordbox_s.png", r="wordbox_r.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_258_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=258,
                                   question="Who steals the batteries from the Sovereign people in Guardians of the Galaxy Vol 2",
                                   levelcounter=str(self.count), a="wordbox_c.png",
                                   b="wordbox_m.png", c="wordbox_q.png", d="wordbox_k.png",
                                   e="wordbox_l.png", f="wordbox_x.png", g="wordbox_z.png",
                                   h="wordbox.png", i="wordbox_r.png", j="wordbox_b.png",
                                   k="wordbox_p.png", l="wordbox_e.png", m="wordbox_o.png",
                                   n="wordbox_d.png", o="wordbox_y.png", p="wordbox_f.png",
                                   q="wordbox_n.png", r="wordbox_t.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_259_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=259,
                                   question="Who sacrifices their life to save Peter Quill in Guardians of the Galaxy Vol 2",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_z.png", c="wordbox_d.png", d="wordbox_w.png",
                                   e="wordbox_t.png", f="wordbox_o.png", g="wordbox_d.png",
                                   h="wordbox_y.png", i="wordbox_x.png", j="wordbox_p.png",
                                   k="wordbox_p.png", l="wordbox_u.png", m="wordbox_u.png",
                                   n="wordbox.png", o="wordbox_w.png", p="wordbox_n.png",
                                   q="wordbox_x.png", r="wordbox_n.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_260_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=260,
                                   question="Who serves as Ego's personal assistant in Guardians of the Galaxy Vol 2",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_q.png", c="wordbox_k.png", d="wordbox_o.png",
                                   e="wordbox_b.png", f="wordbox_i.png", g="wordbox_l.png",
                                   h="wordbox_c.png", i="wordbox_n.png", j="wordbox_m.png",
                                   k="wordbox_p.png", l="wordbox_f.png", m="wordbox_m.png",
                                   n="wordbox_j.png", o="wordbox_s.png", p="wordbox.png",
                                   q="wordbox_k.png", r="wordbox_f.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_261_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=261,
                                   question="How many Infinity Stones were formed during the universe's creation in the (MCU)",
                                   levelcounter=str(self.count), a="wordbox_y.png",
                                   b="wordbox_q.png", c="wordbox_n.png", d="wordbox_i.png",
                                   e="wordbox_p.png", f="wordbox_t.png", g="wordbox_n.png",
                                   h="wordbox_s.png", i="wordbox_q.png", j="wordbox_f.png",
                                   k="wordbox_x.png", l="wordbox_m.png", m="wordbox_h.png",
                                   n="wordbox_m.png", o="wordbox_k.png", p="wordbox_g.png",
                                   q="wordbox_j.png", r="wordbox_d.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_262_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=262,
                                   question="Which Infinity Stone does Loki possess in Avengers Infinity War",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_e.png", c="wordbox_t.png", d="wordbox_q.png",
                                   e="wordbox_p.png", f="wordbox_l.png", g="wordbox_f.png",
                                   h="wordbox_s.png", i="wordbox_k.png", j="wordbox.png",
                                   k="wordbox_b.png", l="wordbox_x.png", m="wordbox_c.png",
                                   n="wordbox_n.png", o="wordbox_h.png", p="wordbox_f.png",
                                   q="wordbox_j.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_263_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=263,
                                   question="Who kills Loki in Avengers Infinity War",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_o.png", c="wordbox_l.png", d="wordbox_t.png", e="wordbox_q.png",
                                   f="wordbox.png",
                                   g="wordbox_m.png", h="wordbox_g.png", i="wordbox_q.png", j="wordbox_n.png",
                                   k="wordbox_f.png",
                                   l="wordbox_v.png", m="wordbox_k.png", n="wordbox_s.png", o="wordbox_p.png",
                                   p="wordbox_d.png", q="wordbox_u.png", r="wordbox_h.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_264_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=264,
                                   question="What is the name of the spaceship used by the Asgardians in Avengers Infinity War",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_q.png", c="wordbox_t.png", d="wordbox_c.png", e="wordbox_p.png",
                                   f="wordbox_n.png",
                                   g="wordbox.png", h="wordbox_l.png", i="wordbox_m.png", j="wordbox_q.png",
                                   k="wordbox_v.png",
                                   l="wordbox.png", m="wordbox_e.png", n="wordbox_g.png", o="wordbox_t.png",
                                   p="wordbox_h.png", q="wordbox_p.png", r="wordbox_s.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_265_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=265,
                                   question="Where is the Reality Stone located, in Avengers Infinity War",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_b.png", c="wordbox_o.png", d="wordbox_c.png",
                                   e="wordbox.png", f="wordbox_w.png", g="wordbox_e.png",
                                   h="wordbox_g.png", i="wordbox_h.png", j="wordbox_k.png",
                                   k="wordbox_f.png", l="wordbox_k.png", m="wordbox_p.png",
                                   n="wordbox_l.png", o="wordbox_r.png", p="wordbox_d.png",
                                   q="wordbox_j.png", r="wordbox_e.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_266_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=266,
                                   question="Whom did Thanos sacrifice in order to obtain the Soul Stone in Avengers Infinity War",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_l.png", c="wordbox_i.png", d="wordbox_g.png",
                                   e="wordbox_j.png", f="wordbox_b.png", g="wordbox_r.png",
                                   h="wordbox_c.png", i="wordbox_n.png", j="wordbox_f.png",
                                   k="wordbox_k.png", l="wordbox_o.png", m="wordbox_g.png",
                                   n="wordbox.png", o="wordbox_h.png", p="wordbox.png",
                                   q="wordbox_d.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_267_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=267,
                                   question="Who serves as the guide to reach the Soul Stone in Avengers Infinity War",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_n.png", c="wordbox_o.png", d="wordbox_u.png", e="wordbox_q.png",
                                   f="wordbox_s.png",
                                   g="wordbox_k.png", h="wordbox_p.png", i="wordbox_r.png", j="wordbox_m.png",
                                   k="wordbox_c.png",
                                   l="wordbox_l.png", m="wordbox_g.png", n="wordbox_t.png", o="wordbox_e.png",
                                   p="wordbox_o.png", q="wordbox_d.png", r="wordbox_q.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_268_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=268,
                                   question="Which stone did Thanos use to reverse time and retrieve the destroyed Mind Stone in Avengers Infinity War",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_t.png", c="wordbox_m.png", d="wordbox_e.png", e="wordbox_s.png",
                                   f="wordbox_h.png",
                                   g="wordbox_l.png", h="wordbox_r.png", i="wordbox_c.png", j="wordbox_n.png",
                                   k="wordbox_d.png",
                                   l="wordbox_o.png", m="wordbox_x.png", n="wordbox_g.png", o="wordbox.png",
                                   p="wordbox_b.png", q="wordbox_u.png", r="wordbox_f.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_269_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=269,
                                   question="What is the name of the stone that allows for manipulation of time in MCU",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_t.png", c="wordbox_m.png", d="wordbox_e.png", e="wordbox_s.png",
                                   f="wordbox_h.png",
                                   g="wordbox_l.png", h="wordbox_r.png", i="wordbox_c.png", j="wordbox_n.png",
                                   k="wordbox_d.png",
                                   l="wordbox_o.png", m="wordbox_x.png", n="wordbox_g.png", o="wordbox.png",
                                   p="wordbox_b.png", q="wordbox_u.png", r="wordbox_f.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_270_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=270,
                                   question="What is the name of the weapon that Thor wields to attack Thanos in Avengers Infinity War",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox.png", c="wordbox_m.png", d="wordbox_f.png", e="wordbox_s.png",
                                   f="wordbox_r.png",
                                   g="wordbox_o.png", h="wordbox_l.png", i="wordbox_p.png", j="wordbox_r.png",
                                   k="wordbox_b.png",
                                   l="wordbox_q.png", m="wordbox_e.png", n="wordbox_t.png", o="wordbox_l.png",
                                   p="wordbox_v.png", q="wordbox_k.png", r="wordbox_e.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_271_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=271,
                                   question="What is the name of Thor's new weapon in Avengers Infinity War",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox.png", c="wordbox_m.png", d="wordbox_f.png", e="wordbox_s.png",
                                   f="wordbox_r.png",
                                   g="wordbox_o.png", h="wordbox_l.png", i="wordbox_p.png", j="wordbox_r.png",
                                   k="wordbox_b.png",
                                   l="wordbox_q.png", m="wordbox_e.png", n="wordbox_t.png", o="wordbox_l.png",
                                   p="wordbox_v.png", q="wordbox_k.png", r="wordbox_e.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_272_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=272,
                                   question="On which planet do Iron Man and the Guardians of the Galaxy team fight Thanos in Avengers Infinity War",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_q.png", c="wordbox_i.png", d="wordbox_t.png", e="wordbox_l.png",
                                   f="wordbox_v.png",
                                   g="wordbox_g.png", h="wordbox_f.png", i="wordbox.png", j="wordbox_s.png",
                                   k="wordbox_w.png",
                                   l="wordbox_p.png", m="wordbox_t.png", n="wordbox_v.png", o="wordbox_m.png",
                                   p="wordbox_h.png", q="wordbox_b.png", r="wordbox_n.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_273_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=273,
                                   question="What is the native planet of Thanos in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_q.png", c="wordbox_i.png", d="wordbox_t.png", e="wordbox_l.png",
                                   f="wordbox_v.png",
                                   g="wordbox_g.png", h="wordbox_f.png", i="wordbox.png", j="wordbox_s.png",
                                   k="wordbox_w.png",
                                   l="wordbox_p.png", m="wordbox_t.png", n="wordbox_v.png", o="wordbox_m.png",
                                   p="wordbox_h.png", q="wordbox_b.png", r="wordbox_n.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_274_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=274,
                                   question="What is the name of Iron Man's suit in Avengers Infinity War",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_t.png", c="wordbox_q.png", d="wordbox_s.png", e="wordbox_p.png",
                                   f="wordbox_k.png",
                                   g="num_0.png", h="num_9.png", i="wordbox.png", j="wordbox_f.png",
                                   k="wordbox_t.png",
                                   l="num_8.png", m="wordbox_o.png", n="wordbox_m.png", o="wordbox_b.png",
                                   p="wordbox_l.png", q="num_7.png", r="num_5.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_275_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=275,
                                   question="What is the name of the stone that is extracted from the Aether",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_f.png", c="wordbox_p.png", d="wordbox_q.png", e="wordbox_b.png",
                                   f="wordbox.png",
                                   g="wordbox_l.png", h="wordbox_c.png", i="wordbox_r.png", j="wordbox_i.png",
                                   k="wordbox_n.png",
                                   l="wordbox_k.png", m="wordbox_v.png", n="wordbox_t.png", o="wordbox_k.png",
                                   p="wordbox_q.png", q="wordbox_b.png", r="wordbox_y.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_276_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=276,
                                   question="What is the name of the Infinity stone used for teleportation",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_e.png", c="wordbox_t.png", d="wordbox_q.png",
                                   e="wordbox_p.png", f="wordbox_l.png", g="wordbox_f.png",
                                   h="wordbox_s.png", i="wordbox_k.png", j="wordbox.png",
                                   k="wordbox_b.png", l="wordbox_x.png", m="wordbox_c.png",
                                   n="wordbox_n.png", o="wordbox_h.png", p="wordbox_f.png",
                                   q="wordbox_j.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_277_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=277, question="Where does Thanos spaceship land on Earth to collect the Time Stone in Avengers Infinity War",
                                   levelcounter=str(self.count), a="wordbox_f.png",
                                   b="wordbox_d.png", c="wordbox_y.png", d="wordbox.png", e="wordbox_r.png",
                                   f="wordbox_k.png",
                                   g="wordbox_e.png", h="wordbox_p.png", i="wordbox_s.png", j="wordbox_w.png",
                                   k="wordbox_c.png",
                                   l="wordbox_o.png", m="wordbox_m.png", n="wordbox_s.png", o="wordbox_l.png",
                                   p="wordbox_t.png", q="wordbox_n.png", r="wordbox_q.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_278_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=278,
                                   question="Where does Thanos go after the Snap in Avengers Infinity War",
                                   levelcounter=str(self.count), a="wordbox_d.png",
                                   b="wordbox_k.png", c="wordbox_p.png", d="wordbox_l.png", e="wordbox_m.png",
                                   f="wordbox_e.png",
                                   g="wordbox_s.png", h="wordbox_g.png", i="wordbox_q.png", j="wordbox_t.png",
                                   k="wordbox_f.png",
                                   l="wordbox_m.png", m="wordbox.png", n="wordbox_m.png", o="wordbox_v.png",
                                   p="wordbox_n.png", q="wordbox_p.png", r="wordbox_r.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_279_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=279,
                                   question="What metal is the Infinity Gauntlet made of in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="wordbox_f.png",
                                   b="wordbox_t.png", c="wordbox_u.png", d="wordbox_p.png", e="wordbox_s.png",
                                   f="wordbox_s.png",
                                   g="wordbox_h.png", h="wordbox_h.png", i="wordbox_u.png", j="wordbox_t.png",
                                   k="wordbox_t.png",
                                   l="wordbox_p.png", m="wordbox_s.png", n="wordbox_t.png", o="wordbox_r.png",
                                   p="wordbox_c.png", q="wordbox_p.png", r="wordbox_i.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_280_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=280,
                                   question="What material is Stormbreaker made of in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="wordbox_f.png",
                                   b="wordbox_t.png", c="wordbox_u.png", d="wordbox_p.png", e="wordbox_s.png",
                                   f="wordbox_s.png",
                                   g="wordbox_h.png", h="wordbox_h.png", i="wordbox_u.png", j="wordbox_t.png",
                                   k="wordbox_t.png",
                                   l="wordbox_p.png", m="wordbox_s.png", n="wordbox_t.png", o="wordbox_r.png",
                                   p="wordbox_c.png", q="wordbox_p.png", r="wordbox_i.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_281_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=281,
                                   question="Where is the Infinity Gauntlet created in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_p.png", c="wordbox_e.png", d="wordbox_f.png", e="wordbox_d.png",
                                   f="wordbox_m.png",
                                   g="wordbox_l.png", h="wordbox_l.png", i="wordbox_r.png", j="wordbox_k.png",
                                   k="wordbox_v.png",
                                   l="wordbox_u.png", m="wordbox.png", n="wordbox_k.png", o="wordbox_b.png",
                                   p="wordbox_i.png", q="wordbox_i.png", r="wordbox_h.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_282_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=282,
                                   question="Where is Stormbreaker, the weapon wielded by Thor is forged",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_p.png", c="wordbox_e.png", d="wordbox_f.png", e="wordbox_d.png",
                                   f="wordbox_m.png",
                                   g="wordbox_l.png", h="wordbox_l.png", i="wordbox_r.png", j="wordbox_k.png",
                                   k="wordbox_v.png",
                                   l="wordbox_u.png", m="wordbox.png", n="wordbox_k.png", o="wordbox_b.png",
                                   p="wordbox_i.png", q="wordbox_i.png", r="wordbox_h.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_283_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=283,
                                   question="What species inhabits Nidavellir in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_k.png", c="wordbox_q.png", d="wordbox_n.png", e="wordbox_n.png",
                                   f="wordbox_v.png",
                                   g="wordbox_d.png", h="wordbox_p.png", i="wordbox_t.png", j="wordbox.png",
                                   k="wordbox_m.png",
                                   l="wordbox_s.png", m="wordbox_w.png", n="wordbox_f.png", o="wordbox_h.png",
                                   p="wordbox_c.png", q="wordbox_m.png", r="wordbox_e.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_284_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=284,
                                   question="Who gives a speech to the MIT students in Captain America Civil War",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_p.png", c="wordbox_k.png", d="wordbox_t.png", e="wordbox_m.png",
                                   f="wordbox_o.png",
                                   g="wordbox.png", h="wordbox_d.png", i="wordbox_t.png", j="wordbox_l.png",
                                   k="wordbox_y.png",
                                   l="wordbox_m.png", m="wordbox_n.png", n="wordbox_q.png", o="wordbox_g.png",
                                   p="wordbox_r.png", q="wordbox_v.png", r="wordbox_k.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_285_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=285,
                                   question="Whom do the Avengers meet to discuss the Sokovia Accords in Captain America Civil War",
                                   levelcounter=str(self.count), a="wordbox_d.png",
                                   b="wordbox_l.png", c="wordbox.png", d="wordbox_o.png", e="wordbox_t.png",
                                   f="wordbox_d.png",
                                   g="wordbox_p.png", h="wordbox_e.png", i="wordbox_k.png", j="wordbox_s.png",
                                   k="wordbox_n.png",
                                   l="wordbox_u.png", m="wordbox_s.png", n="wordbox_m.png", o="wordbox_r.png",
                                   p="wordbox_q.png", q="wordbox_h.png", r="wordbox_s.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_286_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=286,
                                   question="Who gets injured in the fight between the two Avengers groups in Captain America Civil War",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_d.png", c="wordbox_m.png", d="wordbox_t.png", e="wordbox.png",
                                   f="wordbox_p.png",
                                   g="wordbox_f.png", h="wordbox_h.png", i="wordbox_v.png", j="wordbox_s.png",
                                   k="wordbox_o.png",
                                   l="wordbox_l.png", m="wordbox_s.png", n="wordbox_x.png", o="wordbox_e.png",
                                   p="wordbox_e.png", q="wordbox_j.png", r="wordbox_q.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_287_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=287,
                                   question="Who is the character known as Agent 13 in the movie Captain America Civil War",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_n.png", c="wordbox_p.png", d="wordbox_k.png", e="wordbox_c.png",
                                   f="wordbox.png",
                                   g="wordbox_d.png", h="wordbox_s.png", i="wordbox_q.png", j="wordbox_r.png",
                                   k="wordbox_h.png",
                                   l="wordbox_e.png", m="wordbox_l.png", n="wordbox.png", o="wordbox_t.png",
                                   p="wordbox_o.png", q="wordbox_g.png", r="wordbox_r.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")

    def level_288_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=288,
                                   question="Who is the relative of Peggy Carter that appears as Agent 13 in the movie Captain America Civil War",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_n.png", c="wordbox_p.png", d="wordbox_k.png", e="wordbox_c.png",
                                   f="wordbox.png",
                                   g="wordbox_d.png", h="wordbox_s.png", i="wordbox_q.png", j="wordbox_r.png",
                                   k="wordbox_h.png",
                                   l="wordbox_e.png", m="wordbox_l.png", n="wordbox.png", o="wordbox_t.png",
                                   p="wordbox_o.png", q="wordbox_g.png", r="wordbox_r.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_289_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=289,
                                   question="Which agency did Sharon Carter work for before joining the CIA in Captain America Civil War",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_f.png", c="wordbox_n.png", d="wordbox_c.png", e="wordbox_k.png",
                                   f="wordbox_h.png",
                                   g="wordbox_m.png", h="wordbox_q.png", i="wordbox_d.png", j="wordbox_o.png",
                                   k="wordbox_e.png",
                                   l="wordbox.png", m="wordbox_w.png", n="wordbox_n.png", o="wordbox_i.png",
                                   p="wordbox_v.png", q="wordbox_b.png", r="wordbox_l.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_290_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=290,
                                   question="In which year did Peggy Carter pass away in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="num_5.png",
                                   b="num_9.png", c="num_7.png", d="num_8.png", e="num_3.png",
                                   f="num_0.png",
                                   g="num_2.png", h="num_9.png", i="num_4.png", j="num_1.png",
                                   k="num_3.png",
                                   l="num_8.png", m="num_5.png", n="num_4.png", o="num_5.png",
                                   p="num_3.png", q="num_6.png", r="num_7.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_291_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=291,
                                   question="Who was killed in the bomb blast that took place in Vienna in the movie Civil War",
                                   levelcounter=str(self.count),a="wordbox_f.png",
                                   b="wordbox_q.png", c="wordbox_c.png", d="wordbox_v.png", e="wordbox_p.png",
                                   f="wordbox_t.png",
                                   g="wordbox.png", h="wordbox_m.png", i="wordbox_h.png", j="wordbox_s.png",
                                   k="wordbox_f.png",
                                   l="wordbox.png", m="wordbox_l.png", n="wordbox_k.png", o="wordbox_v.png",
                                   p="wordbox_q.png", q="wordbox_j.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_292_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=292,
                                   question="Who was the king of Wakanda in 1992 in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count),a="wordbox_f.png",
                                   b="wordbox_q.png", c="wordbox_c.png", d="wordbox_v.png", e="wordbox_p.png",
                                   f="wordbox_t.png",
                                   g="wordbox.png", h="wordbox_m.png", i="wordbox_h.png", j="wordbox_s.png",
                                   k="wordbox_f.png",
                                   l="wordbox.png", m="wordbox_l.png", n="wordbox_k.png", o="wordbox_v.png",
                                   p="wordbox_q.png", q="wordbox_j.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_293_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=293,
                                   question="Who is the father of T'Challa in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count),a="wordbox_f.png",
                                   b="wordbox_q.png", c="wordbox_c.png", d="wordbox_v.png", e="wordbox_p.png",
                                   f="wordbox_t.png",
                                   g="wordbox.png", h="wordbox_m.png", i="wordbox_h.png", j="wordbox_s.png",
                                   k="wordbox_f.png",
                                   l="wordbox.png", m="wordbox_l.png", n="wordbox_k.png", o="wordbox_v.png",
                                   p="wordbox_q.png", q="wordbox_j.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_294_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=294,
                                   question="What is the name of T'Challa's sister in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="wordbox_u.png",
                                   b="wordbox_f.png", c="wordbox_p.png", d="wordbox_m.png", e="wordbox_n.png",
                                   f="wordbox_j.png",
                                   g="wordbox_n.png", h="wordbox_m.png", i="wordbox_h.png", j="wordbox_q.png",
                                   k="wordbox_r.png",
                                   l="wordbox_v.png", m="wordbox_s.png", n="wordbox_k.png", o="wordbox_p.png",
                                   p="wordbox_t.png", q="wordbox_i.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_295_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=295,
                                   question="Who becomes the new king of Wakanda after the death of T'Chaka in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="wordbox_c.png",
                                   b="wordbox_k.png", c="wordbox_q.png", d="wordbox.png", e="wordbox_s.png",
                                   f="wordbox_u.png",
                                   g="wordbox_s.png", h="wordbox.png", i="wordbox_f.png", j="wordbox_p.png",
                                   k="wordbox_o.png",
                                   l="wordbox_l.png", m="wordbox_t.png", n="wordbox_n.png", o="wordbox_j.png",
                                   p="wordbox_l.png", q="wordbox_b.png", r="wordbox_h.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_296_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=296,
                                   question="What is the name of the rare and valuable metal found exclusively in Wakanda in the MCU",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_f.png", c="wordbox_n.png", d="wordbox_o.png", e="wordbox.png",
                                   f="wordbox_t.png",
                                   g="wordbox_u.png", h="wordbox_d.png", i="wordbox_q.png", j="wordbox_i.png",
                                   k="wordbox_c.png",
                                   l="wordbox_m.png", m="wordbox_s.png", n="wordbox_r.png", o="wordbox_t.png",
                                   p="wordbox_v.png", q="wordbox_g.png", r="wordbox_i.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_297_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=297,
                                   question="Who is the leader of the Jabari tribe in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox_s.png", c="wordbox_k.png", d="wordbox_v.png", e="wordbox_t.png",
                                   f="wordbox_p.png",
                                   g="wordbox_f.png", h="wordbox_p.png", i="wordbox_q.png", j="wordbox_n.png",
                                   k="wordbox_y.png",
                                   l="wordbox_b.png", m="wordbox.png", n="wordbox_j.png", o="wordbox_c.png",
                                   p="wordbox_u.png", q="wordbox_h.png", r="wordbox_f.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_298_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=298,
                                   question="Who saves T'Challa after his fight with Killmonger in the Black Panther movie",
                                   levelcounter=str(self.count), a="wordbox_u.png",
                                   b="wordbox_f.png", c="wordbox_p.png", d="wordbox_m.png", e="wordbox_n.png",
                                   f="wordbox_j.png",
                                   g="wordbox_n.png", h="wordbox_m.png", i="wordbox_h.png", j="wordbox_q.png",
                                   k="wordbox_r.png",
                                   l="wordbox_v.png", m="wordbox_s.png", n="wordbox_k.png", o="wordbox_p.png",
                                   p="wordbox_t.png", q="wordbox_i.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_299_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=299,
                                   question="Who challenges T'Challa in a ritual combat for the throne of Wakanda in the Black Panther movie",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox_s.png", c="wordbox_k.png", d="wordbox_v.png", e="wordbox_t.png",
                                   f="wordbox_p.png",
                                   g="wordbox_f.png", h="wordbox_p.png", i="wordbox_q.png", j="wordbox_n.png",
                                   k="wordbox_y.png",
                                   l="wordbox_b.png", m="wordbox.png", n="wordbox_j.png", o="wordbox_c.png",
                                   p="wordbox_u.png", q="wordbox_h.png", r="wordbox_f.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_300_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=300,
                                   question="Who leads the Wakandan soldiers, including the Dora Milaje, in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_s.png", c="wordbox_t.png", d="wordbox_u.png", e="wordbox_o.png",
                                   f="wordbox_b.png",
                                   g="wordbox_f.png", h="wordbox_n.png", i="wordbox_k.png", j="wordbox_t.png",
                                   k="wordbox_q.png",
                                   l="wordbox_m.png", m="wordbox_y.png", n="wordbox_h.png", o="wordbox_j.png",
                                   p="wordbox_v.png", q="wordbox_e.png", r="wordbox_g.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_301_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=301,
                                   question="What is the name of T'Challa's girlfriend in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_s.png", c="wordbox_i.png", d="wordbox_v.png", e="wordbox_t.png",
                                   f="wordbox_p.png",
                                   g="wordbox_f.png", h="wordbox_p.png", i="wordbox_q.png", j="wordbox_p.png",
                                   k="wordbox_y.png",
                                   l="wordbox.png", m="wordbox_k.png", n="wordbox_j.png", o="wordbox_c.png",
                                   p="wordbox.png", q="wordbox_h.png", r="wordbox_f.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_302_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=302,
                                   question="To which tribe does M'Baku belong in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox_s.png", c="wordbox.png", d="wordbox_t.png", e="wordbox_u.png",
                                   f="wordbox_r.png",
                                   g="wordbox_j.png", h="wordbox_f.png", i="wordbox_l.png", j="wordbox_b.png",
                                   k="wordbox_o.png",
                                   l="wordbox_n.png", m="wordbox_i.png", n="wordbox_c.png", o="wordbox_p.png",
                                   p="wordbox_o.png", q="wordbox.png", r="wordbox_h.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_303_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=303,
                                   question="What is the name of T'Chaka's younger brother in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_c.png", c="wordbox_q.png", d="wordbox_s.png", e="wordbox_t.png",
                                   f="wordbox_b.png",
                                   g="wordbox_p.png", h="wordbox_k.png", i="wordbox_j.png", j="wordbox_v.png",
                                   k="wordbox_l.png",
                                   l="wordbox_k.png", m="wordbox_u.png", n="wordbox_f.png", o="wordbox_q.png",
                                   p="wordbox_m.png", q="wordbox_o.png", r="wordbox_p.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_304_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=304,
                                   question="What is the villainous alter ego of Erik Stevens in the Black Panther movie",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_g.png", c="wordbox_j.png", d="wordbox_q.png", e="wordbox_h.png",
                                   f="wordbox_e.png",
                                   g="wordbox_l.png", h="wordbox_r.png", i="wordbox_f.png", j="wordbox_o.png",
                                   k="wordbox_p.png",
                                   l="wordbox_l.png", m="wordbox_m.png", n="wordbox_s.png", o="wordbox_n.png",
                                   p="wordbox_u.png", q="wordbox_j.png", r="wordbox_k.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_305_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=305,
                                   question="With whom did Captain America choose to spend his life after returning the stones",
                                   levelcounter=str(self.count), a="wordbox_g.png",
                                   b="wordbox_k.png", c="wordbox_r.png", d="wordbox_m.png", e="wordbox_e.png",
                                   f="wordbox_d.png",
                                   g="wordbox.png", h="wordbox_q.png", i="wordbox_e.png", j="wordbox_r.png",
                                   k="wordbox_v.png",
                                   l="wordbox_g.png", m="wordbox_p.png", n="wordbox_h.png", o="wordbox_t.png",
                                   p="wordbox_o.png", q="wordbox_c.png", r="wordbox_y.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_306_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=306,
                                   question="To whom did Steve Rogers pass on the Captain America shield in the Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_k.png", c="wordbox_s.png", d="wordbox_v.png", e="wordbox_q.png",
                                   f="wordbox_n.png",
                                   g="wordbox_s.png", h="wordbox_g.png", i="wordbox_o.png", j="wordbox_c.png",
                                   k="wordbox_m.png",
                                   l="wordbox_h.png", m="wordbox_j.png", n="wordbox_i.png", o="wordbox_f.png",
                                   p="wordbox_w.png", q="wordbox_l.png", r="wordbox_u.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_307_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=307,
                                   question="Who wields the power of the Infinity Stones to reverse the effects of the snap and bring back the disappeared people",
                                   levelcounter=str(self.count), a="wordbox_u.png",
                                   b="wordbox_n.png", c="wordbox_r.png", d="wordbox_f.png", e="wordbox_q.png",
                                   f="wordbox_v.png",
                                   g="wordbox_b.png", h="wordbox_n.png", i="wordbox_k.png", j="wordbox_c.png",
                                   k="wordbox_e.png",
                                   l="wordbox_b.png", m="wordbox_e.png", n="wordbox_m.png", o="wordbox_p.png",
                                   p="wordbox_r.png", q="wordbox_s.png", r="wordbox.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_308_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=308,
                                   question="Who goes to the Sanctum Sanctorum to collect the Time Stone from the Ancient One in Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox_u.png",
                                   b="wordbox_n.png", c="wordbox_r.png", d="wordbox_f.png", e="wordbox_q.png",
                                   f="wordbox_v.png",
                                   g="wordbox_b.png", h="wordbox_n.png", i="wordbox_k.png", j="wordbox_c.png",
                                   k="wordbox_e.png",
                                   l="wordbox_b.png", m="wordbox_e.png", n="wordbox_m.png", o="wordbox_p.png",
                                   p="wordbox_r.png", q="wordbox_s.png", r="wordbox.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_309_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0

        self.changing_words_blanks(level=309,
                                   question="Who sacrifices their life at the end of Avengers Endgame movie",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_p.png", c="wordbox_k.png", d="wordbox_t.png", e="wordbox_m.png",
                                   f="wordbox_o.png",
                                   g="wordbox.png", h="wordbox_d.png", i="wordbox_t.png", j="wordbox_l.png",
                                   k="wordbox_y.png",
                                   l="wordbox_m.png", m="wordbox_n.png", n="wordbox_q.png", o="wordbox_g.png",
                                   p="wordbox_r.png", q="wordbox_v.png", r="wordbox_k.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_310_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=310,
                                   question="In which city does Natasha Romanoff find Clint Barton in Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox_q.png",
                                   b="wordbox_p.png", c="wordbox_k.png", d="wordbox_n.png", e="wordbox_c.png",
                                   f="wordbox_l.png",
                                   g="wordbox_y.png", h="wordbox_l.png", i="wordbox_o.png", j="wordbox_f.png",
                                   k="wordbox_j.png",
                                   l="wordbox_s.png", m="wordbox_p.png", n="wordbox_h.png", o="wordbox_o.png",
                                   p="wordbox_s.png", q="wordbox_e.png", r="wordbox_t.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_311_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=311,
                                   question="Whom does Thor meet when he goes back in time to retrieve the Reality Stone in Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_v.png", c="wordbox_i.png", d="wordbox_o.png", e="wordbox_l.png",
                                   f="wordbox_g.png",
                                   g="wordbox_r.png", h="wordbox_x.png", i="wordbox_u.png", j="wordbox_f.png",
                                   k="wordbox_h.png",
                                   l="wordbox_n.png", m="wordbox_s.png", n="wordbox_b.png", o="wordbox.png",
                                   p="wordbox_t.png", q="wordbox_g.png", r="wordbox_q.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_312_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=312,
                                   question="What item does Thor bring back with him to the present time after retrieving the Reality Stone in Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_c.png", c="wordbox_o.png", d="wordbox_l.png", e="wordbox_p.png",
                                   f="wordbox_k.png",
                                   g="wordbox_j.png", h="wordbox.png", i="wordbox_t.png", j="wordbox_m.png",
                                   k="wordbox_v.png",
                                   l="wordbox_n.png", m="wordbox_r.png", n="wordbox_g.png", o="wordbox_b.png",
                                   p="wordbox_i.png", q="wordbox_f.png", r="wordbox_c.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_313_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=313,
                                   question="Who does Tony Stark encounter in the year 1970 when he travels back in time in Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox_d.png",
                                   b="wordbox_m.png", c="wordbox_w.png", d="wordbox_t.png", e="wordbox_l.png",
                                   f="wordbox_o.png",
                                   g="wordbox_c.png", h="wordbox_h.png", i="wordbox.png", j="wordbox_r.png",
                                   k="wordbox_f.png",
                                   l="wordbox_q.png", m="wordbox_k.png", n="wordbox_r.png", o="wordbox_s.png",
                                   p="wordbox_p.png", q="wordbox_v.png", r="wordbox.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_314_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=314,
                                   question="To which year did Steve and Tony Stark travel to get the Space Stone after missing it in 2012 in Avengers Endgame",
                                   levelcounter=str(self.count), a="num_5.png",
                                   b="num_8.png", c="num_2.png", d="num_8.png", e="num_3.png",
                                   f="num_9.png",
                                   g="num_1.png", h="num_9.png", i="num_4.png", j="num_7.png",
                                   k="num_3.png",
                                   l="num_8.png", m="num_5.png", n="num_4.png", o="num_5.png",
                                   p="num_3.png", q="num_0.png", r="num_2.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_315_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=315,
                                   question="Where did the Thor travel to in order to retrieve the Reality Stone in Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_o.png", c="wordbox_s.png", d="wordbox_t.png", e="wordbox_v.png",
                                   f="wordbox_n.png",
                                   g="wordbox_t.png", h="wordbox_f.png", i="wordbox.png", j="wordbox_r.png",
                                   k="wordbox_q.png",
                                   l="wordbox_b.png", m="wordbox_d.png", n="wordbox_i.png", o="wordbox_x.png",
                                   p="wordbox_u.png", q="wordbox_n.png", r="wordbox_g.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_316_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=316,
                                   question="To which years did the Avengers travel to obtain the Power Stone and the Soul Stone in Avengers Endgame",
                                   levelcounter=str(self.count), a="num_5.png",
                                   b="num_9.png", c="num_7.png", d="num_8.png", e="num_3.png",
                                   f="num_0.png",
                                   g="num_2.png", h="num_9.png", i="num_6.png", j="num_1.png",
                                   k="num_3.png",
                                   l="num_8.png", m="num_5.png", n="num_6.png", o="num_5.png",
                                   p="num_3.png", q="num_4.png", r="num_7.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_317_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=317,
                                   question="In which years are the Time Stone and the Mind Stone found in Avengers Endgame",
                                   levelcounter=str(self.count), a="num_5.png",
                                   b="num_9.png", c="num_7.png", d="num_8.png", e="num_3.png",
                                   f="num_0.png",
                                   g="num_2.png", h="num_9.png", i="num_6.png", j="num_1.png",
                                   k="num_3.png",
                                   l="num_8.png", m="num_5.png", n="num_6.png", o="num_5.png",
                                   p="num_3.png", q="num_2.png", r="num_7.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_318_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=318, question="In which city are the Time Stone, Mind Stone, and Space Stone found in the Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox_f.png",
                                   b="wordbox_d.png", c="wordbox_y.png", d="wordbox.png", e="wordbox_r.png",
                                   f="wordbox_k.png",
                                   g="wordbox_e.png", h="wordbox_p.png", i="wordbox_s.png", j="wordbox_w.png",
                                   k="wordbox_c.png",
                                   l="wordbox_o.png", m="wordbox_m.png", n="wordbox_s.png", o="wordbox_l.png",
                                   p="wordbox_t.png", q="wordbox_n.png", r="wordbox_q.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_319_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=319,
                                   question="On which planet did the Avengers obtain the Power Stone in the movie Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_f.png", c="wordbox_l.png", d="wordbox_q.png", e="wordbox_n.png",
                                   f="wordbox_o.png",
                                   g="wordbox_m.png", h="wordbox_k.png", i="wordbox_p.png", j="wordbox_t.png",
                                   k="wordbox_l.png",
                                   l="wordbox_g.png", m="wordbox_q.png", n="wordbox_s.png", o="wordbox.png",
                                   p="wordbox_u.png", q="wordbox_b.png", r="wordbox_h.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_320_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=320,
                                   question="To which year did the Avengers travel to retrieve the Reality Stone in the movie Avengers Endgame",
                                   levelcounter=str(self.count), a="num_5.png",
                                   b="num_9.png", c="num_7.png", d="num_8.png", e="num_6.png",
                                   f="num_0.png",
                                   g="num_2.png", h="num_9.png", i="num_6.png", j="num_1.png",
                                   k="num_6.png",
                                   l="num_8.png", m="num_5.png", n="num_6.png", o="num_5.png",
                                   p="num_9.png", q="num_3.png", r="num_7.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_321_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=321,
                                   question="On which planet did the Avengers obtain the Soul Stone in the movie Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox_v.png",
                                   b="wordbox_i.png", c="wordbox_k.png", d="wordbox_q.png", e="wordbox_p.png",
                                   f="wordbox_r.png",
                                   g="wordbox_p.png", h="wordbox_s.png", i="wordbox_r.png", j="wordbox_u.png",
                                   k="wordbox_n.png",
                                   l="wordbox_c.png", m="wordbox_m.png", n="wordbox_j.png", o="wordbox_g.png",
                                   p="wordbox_p.png", q="wordbox_h.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_322_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=322,
                                   question="Who sacrifices their life for the Soul Stone in Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox.png", c="wordbox_o.png", d="wordbox_b.png", e="wordbox.png",
                                   f="wordbox_c.png",
                                   g="wordbox_h.png", h="wordbox_m.png", i="wordbox_p.png", j="wordbox.png",
                                   k="wordbox_n.png",
                                   l="wordbox_r.png", m="wordbox_f.png", n="wordbox_t.png", o="wordbox_o.png",
                                   p="wordbox_s.png", q="wordbox_f.png", r="wordbox_n.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="bor.png", em_15="bor.png")
    def level_323_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=323,
                                   question="Who escapes with the Space Stone when Steve and Tony try to retrieve it in the Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox_f.png",
                                   b="wordbox.png", c="wordbox_l.png", d="wordbox_e.png", e="wordbox_q.png",
                                   f="wordbox_s.png",
                                   g="wordbox_k.png", h="wordbox_n.png", i="wordbox_b.png", j="wordbox_w.png",
                                   k="wordbox_e.png",
                                   l="wordbox_i.png", m="wordbox_m.png", n="wordbox_p.png", o="wordbox_f.png",
                                   p="wordbox_h.png", q="wordbox_o.png", r="wordbox_g.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_324_ref(self,*args) :
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=324,
                                   question="What is the name of Pepper Potts suit in Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox_f.png",
                                   b="wordbox_t.png", c="wordbox_p.png", d="wordbox_u.png", e="wordbox_q.png",
                                   f="wordbox_v.png",
                                   g="wordbox_e.png", h="wordbox_n.png", i="wordbox_p.png", j="wordbox_t.png",
                                   k="wordbox_k.png",
                                   l="wordbox_e.png", m="wordbox_s.png", n="wordbox_m.png", o="wordbox_o.png",
                                   p="wordbox_c.png", q="wordbox_d.png", r="wordbox_r.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_325_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=325,
                                   question="What is the name of the wristband used for time travel in Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_f.png", c="wordbox_u.png", d="wordbox_y.png", e="wordbox_l.png",
                                   f="wordbox_g.png",
                                   g="wordbox_q.png", h="wordbox_j.png", i="wordbox.png", j="wordbox_o.png",
                                   k="wordbox_n.png",
                                   l="wordbox_s.png", m="wordbox_p.png", n="wordbox_v.png", o="wordbox_u.png",
                                   p="wordbox_b.png", q="wordbox_m.png", r="wordbox_h.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_326_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=326,
                                   question="Who destroyed Thanos spaceship in the movie Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox_c.png",
                                   b="wordbox_h.png", c="wordbox_p.png", d="wordbox_s.png", e="wordbox_i.png",
                                   f="wordbox_r.png",
                                   g="wordbox_t.png", h="wordbox_q.png", i="wordbox.png", j="wordbox_m.png",
                                   k="wordbox_s.png",
                                   l="wordbox_v.png", m="wordbox_o.png", n="wordbox_e.png", o="wordbox_n.png",
                                   p="wordbox_l.png", q="wordbox.png", r="wordbox_b.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="mix.png", em_15="mix.png")
    def level_327_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=327,
                                   question="Who rescues Tony Stark from space and brings him back to Earth in the Avengers Endgame",
                                   levelcounter=str(self.count), a="wordbox_c.png",
                                   b="wordbox_h.png", c="wordbox_p.png", d="wordbox_s.png", e="wordbox_i.png",
                                   f="wordbox_r.png",
                                   g="wordbox_t.png", h="wordbox_q.png", i="wordbox.png", j="wordbox_m.png",
                                   k="wordbox_s.png",
                                   l="wordbox_v.png", m="wordbox_o.png", n="wordbox_e.png", o="wordbox_n.png",
                                   p="wordbox_l.png", q="wordbox.png", r="wordbox_b.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="mix.png", em_15="mix.png")
    def level_328_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=328,
                                   question="Who accompanies Iron Man in the spaceship when they are stranded in space in the Avengers Endgame movie",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_o.png", c="wordbox_f.png", d="wordbox_g.png",
                                   e="wordbox_c.png", f="wordbox_l.png", g="wordbox_h.png",
                                   h="wordbox.png", i="wordbox_k.png", j="wordbox_n.png",
                                   k="wordbox_m.png", l="wordbox_d.png", m="wordbox_u.png",
                                   n="wordbox_h.png", o="wordbox_k.png", p="wordbox_c.png",
                                   q="wordbox_m.png", r="wordbox_b.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_329_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=329,
                                   question="Who does Scott Lang, meet after the Thanos snap in the Avengers Endgame movie",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_f.png", c="wordbox.png", d="wordbox_t.png",
                                   e="wordbox_e.png", f="wordbox_h.png", g="wordbox.png",
                                   h="wordbox_q.png", i="wordbox_c.png", j="wordbox_h.png",
                                   k="wordbox_s.png", l="wordbox_p.png", m="wordbox_g.png",
                                   n="wordbox_l.png", o="wordbox_s.png", p="wordbox_n.png",
                                   q="wordbox_o.png", r="wordbox_d.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_330_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=330,
                                   question="Who is the vibranium dealer in the Black Panther movie",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_u.png", c="wordbox_f.png", d="wordbox_s.png",
                                   e="wordbox_u.png", f="wordbox_s.png", g="wordbox.png",
                                   h="wordbox_o.png", i="wordbox_l.png", j="wordbox_d.png",
                                   k="wordbox_l.png", l="wordbox_k.png", m="wordbox_e.png",
                                   n="wordbox_j.png", o="wordbox_y.png", p="wordbox_v.png",
                                   q="wordbox_q.png", r="wordbox_e.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_331_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=331,
                                   question="What is the name of the CIA agent in the Black Panther movie",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_k.png", c="wordbox_v.png", d="wordbox_s.png",
                                   e="wordbox_m.png", f="wordbox_r.png", g="wordbox_e.png",
                                   h="wordbox_r.png", i="wordbox_t.png", j="wordbox_q.png",
                                   k="wordbox_b.png", l="wordbox_t.png", m="wordbox_c.png",
                                   n="wordbox_e.png", o="wordbox_f.png", p="wordbox_e.png",
                                   q="wordbox_u.png", r="wordbox_o.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_332_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=332,
                                   question="Who is the primary antagonist in the Black Panther movie",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_g.png", c="wordbox_j.png", d="wordbox_q.png", e="wordbox_h.png",
                                   f="wordbox_e.png",
                                   g="wordbox_l.png", h="wordbox_r.png", i="wordbox_f.png", j="wordbox_o.png",
                                   k="wordbox_p.png",
                                   l="wordbox_l.png", m="wordbox_m.png", n="wordbox_s.png", o="wordbox_n.png",
                                   p="wordbox_u.png", q="wordbox_j.png", r="wordbox_k.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_333_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=333,
                                   question="What is the name of the special herb that grants enhanced abilities associated with the Black Panther suit",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_f.png", c="wordbox_e.png", d="wordbox_k.png", e="wordbox_k.png",
                                   f="wordbox_t.png",
                                   g="wordbox_e.png", h="wordbox_o.png", i="wordbox_r.png", j="wordbox.png",
                                   k="wordbox_k.png",
                                   l="wordbox_d.png", m="wordbox_s.png", n="wordbox_l.png", o="wordbox_h.png",
                                   p="wordbox.png", q="wordbox_v.png", r="wordbox_p.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_334_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=334,
                                   question="Who is responsible for the deaths of Tony Stark's parents in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_p.png", c="wordbox_r.png", d="wordbox_e.png", e="wordbox_o.png",
                                   f="wordbox_t.png",
                                   g="wordbox_m.png", h="wordbox_u.png", i="wordbox_s.png", j="wordbox_k.png",
                                   k="wordbox_c.png",
                                   l="wordbox_y.png", m="wordbox_x.png", n="wordbox.png", o="wordbox_q.png",
                                   p="wordbox_n.png", q="wordbox_h.png", r="wordbox_b.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_335_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=335,
                                   question="In the Civil War movie, who does Falcon approach to seek help for Steve Rogers team",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_k.png", c="wordbox_n.png", d="wordbox_l.png", e="wordbox_p.png",
                                   f="wordbox_f.png",
                                   g="wordbox_t.png", h="wordbox_f.png", i="wordbox_s.png", j="wordbox_w.png",
                                   k="wordbox_c.png",
                                   l="wordbox_q.png", m="wordbox.png", n="wordbox_j.png", o="wordbox_g.png",
                                   p="wordbox_v.png", q="wordbox_t.png", r="wordbox_u.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_336_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=336,
                                   question="In the Civil War movie, what is the alternate name of Sharon Carter",
                                   levelcounter=str(self.count), a="wordbox_g.png",
                                   b="num_4.png", c="wordbox_f.png", d="num_9.png", e="wordbox_j.png",
                                   f="wordbox_e.png",
                                   g="num_3.png", h="num_7.png", i="wordbox.png", j="wordbox_t.png",
                                   k="wordbox_k.png",
                                   l="wordbox_q.png", m="wordbox_n.png", n="num_5.png", o="wordbox_v.png",
                                   p="wordbox_f.png", q="num_8.png", r="num_1.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_337_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=337,
                                   question="In which city did the bomb blast orchestrated by the Winter Soldier occur in the Civil War movie",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_f.png", c="wordbox_k.png", d="wordbox_q.png", e="wordbox_p.png",
                                   f="wordbox_v.png",
                                   g="wordbox.png", h="wordbox_p.png", i="wordbox_e.png", j="wordbox_p.png",
                                   k="wordbox_i.png",
                                   l="wordbox_o.png", m="wordbox_t.png", n="wordbox_j.png", o="wordbox_c.png",
                                   p="wordbox_f.png", q="wordbox_h.png", r="wordbox_n.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_338_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=338,
                                   question="Who is the main antagonist responsible for manipulating the Avengers to fight amongst themselves in the Civil War",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_e.png", c="wordbox_f.png", d="wordbox_k.png", e="wordbox_m.png",
                                   f="wordbox_l.png",
                                   g="wordbox_o.png", h="wordbox_k.png", i="wordbox_j.png", j="wordbox_u.png",
                                   k="wordbox_d.png",
                                   l="wordbox_m.png", m="wordbox_t.png", n="wordbox_c.png", o="wordbox_j.png",
                                   p="wordbox_v.png", q="wordbox_e.png", r="wordbox_z.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_339_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=339,
                                   question="What is the term used to describe the action of using the Infinity Stones to erase half of all life in the universe",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_t.png", c="wordbox_m.png", d="wordbox_l.png", e="wordbox_q.png",
                                   f="wordbox.png",
                                   g="wordbox_n.png", h="wordbox_o.png", i="wordbox_p.png", j="wordbox_k.png",
                                   k="wordbox_f.png",
                                   l="wordbox_t.png", m="wordbox_l.png", n="wordbox_j.png", o="wordbox_x.png",
                                   p="wordbox_h.png", q="wordbox_c.png", r="wordbox_k.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_340_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=340,
                                   question="In which year does Janet van Dyne shrink into the quantum realm in Ant-Man and the wasp movie",
                                   levelcounter=str(self.count), a="num_6.png",
                                   b="num_3.png", c="num_8.png", d="num_4.png",
                                   e="num_5.png", f="num_0.png", g="num_1.png",
                                   h="num_6.png", i="num_5.png", j="num_7.png",
                                   k="num_2.png", l="num_6.png", m="num_0.png",
                                   n="num_0.png", o="num_3.png", p="num_2.png",
                                   q="num_9.png", r="num_4.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_341_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=341,
                                   question="Luis, Dave, and Kurt Goreshter are the best friends of whom",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_k.png", c="wordbox_n.png", d="wordbox_l.png", e="wordbox_p.png",
                                   f="wordbox_f.png",
                                   g="wordbox_t.png", h="wordbox_f.png", i="wordbox_s.png", j="wordbox_w.png",
                                   k="wordbox_c.png",
                                   l="wordbox_q.png", m="wordbox.png", n="wordbox_j.png", o="wordbox_g.png",
                                   p="wordbox_v.png", q="wordbox_t.png", r="wordbox_u.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_342_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=342,
                                   question="Who kidnaps Scott Lang in the Ant-Man and the Wasp movie",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox.png", c="wordbox_k.png", d="wordbox_f.png",
                                   e="wordbox_b.png", f="wordbox_o.png", g="wordbox_d.png",
                                   h="wordbox_j.png", i="wordbox_g.png", j="wordbox_m.png",
                                   k="wordbox_i.png", l="wordbox_e.png", m="wordbox_s.png",
                                   n="wordbox_l.png", o="wordbox_n.png", p="wordbox_t.png",
                                   q="wordbox_c.png", r="wordbox_w.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_343_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=343,
                                   question="Who is the black market dealer in the Ant-Man and the Wasp movie",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_b.png", c="wordbox_d.png", d="wordbox_i.png",
                                   e="wordbox_y.png", f="wordbox_r.png", g="wordbox_o.png",
                                   h="wordbox_k.png", i="wordbox_h.png", j="wordbox_n.png",
                                   k="wordbox_g.png", l="wordbox_s.png", m="wordbox_n.png",
                                   n="wordbox_j.png", o="wordbox_u.png", p="wordbox_e.png",
                                   q="wordbox_c.png", r="wordbox_f.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_344_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=344,
                                   question="Who indirectly attacks the Pym family in the Ant-Man and the Wasp movie",
                                   levelcounter=str(self.count),a="wordbox_i.png",
                               b="wordbox.png",c="wordbox_j.png",d="wordbox_o.png",
                               e="wordbox_c.png",f="wordbox_l.png",g="wordbox_s.png",
                               h="wordbox_h.png",i="wordbox_r.png",j="wordbox_b.png",
                               k="wordbox_g.png",l="wordbox_t.png",m="wordbox_l.png",
                               n="wordbox_f.png",o="wordbox_e.png",p="wordbox_d.png",
                               q="wordbox_q.png",r="wordbox_k.png",

                               em_1="bor.png",em_2="bor.png",em_3="bor.png",em_4="bor.png",em_5="bor.png",em_6="bor.png",em_7="bor.png",
                               em_8="bor.png",em_9="bor.png",em_10="bor.png",em_11="mix.png",em_12="mix.png",em_13="mix.png",em_14="mix.png",em_15="mix.png"


                               )
    def level_345_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=345,
                                   question="Who is the character known as Ghost in the Ant-Man and the Wasp movie",
                                   levelcounter=str(self.count), a="wordbox_v.png",
                                   b="wordbox_d.png", c="wordbox_s.png", d="wordbox_b.png",
                                   e="wordbox_l.png", f="wordbox.png", g="wordbox.png",
                                   h="wordbox_n.png", i="wordbox_t.png", j="wordbox_w.png",
                                   k="wordbox_c.png", l="wordbox_f.png", m="wordbox_r.png",
                                   n="wordbox_m.png", o="wordbox_e.png", p="wordbox.png",
                                   q="wordbox_o.png", r="wordbox_r.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_346_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=346,
                                   question="Who is the father of Ava Starr in the Ant-Man and the Wasp movie",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_b.png", c="wordbox_l.png", d="wordbox_f.png",
                                   e="wordbox_h.png", f="wordbox_t.png", g="wordbox_s.png",
                                   h="wordbox_e.png", i="wordbox_g.png", j="wordbox_r.png",
                                   k="wordbox_c.png", l="wordbox_s.png", m="wordbox_k.png",
                                   n="wordbox_j.png", o="wordbox.png", p="wordbox.png",
                                   q="wordbox_d.png", r="wordbox_r.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_347_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=347,
                                   question="Who uses the Wasp suit after Janet van Dyne",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_n.png", c="wordbox_x.png", d="wordbox_y.png",
                                   e="wordbox_b.png", f="wordbox_e.png", g="wordbox_v.png",
                                   h="wordbox_g.png", i="wordbox.png", j="wordbox_f.png",
                                   k="wordbox_i.png", l="wordbox_n.png", m="wordbox_p.png",
                                   n="wordbox_c.png", o="wordbox_d.png", p="wordbox_e.png",
                                   q="wordbox_z.png", r="wordbox_o.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_348_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=348,
                                   question="Who's snap turns the Hank Pym family into ashes",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_o.png", c="wordbox_l.png", d="wordbox_t.png", e="wordbox_q.png",
                                   f="wordbox.png",
                                   g="wordbox_m.png", h="wordbox_g.png", i="wordbox_q.png", j="wordbox_n.png",
                                   k="wordbox_f.png",
                                   l="wordbox_v.png", m="wordbox_k.png", n="wordbox_s.png", o="wordbox_p.png",
                                   p="wordbox_d.png", q="wordbox_u.png", r="wordbox_h.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_349_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=349,
                                   question="Whose snap makes half of the Earth's population turn to ashes",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_o.png", c="wordbox_l.png", d="wordbox_t.png", e="wordbox_q.png",
                                   f="wordbox.png",
                                   g="wordbox_m.png", h="wordbox_g.png", i="wordbox_q.png", j="wordbox_n.png",
                                   k="wordbox_f.png",
                                   l="wordbox_v.png", m="wordbox_k.png", n="wordbox_s.png", o="wordbox_p.png",
                                   p="wordbox_d.png", q="wordbox_u.png", r="wordbox_h.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_350_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=350,
                                   question="What is the name of the superhero who derives their powers from the Light Engine in MCU",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_b.png", c="wordbox_x.png", d="wordbox_r.png",
                                   e="wordbox_c.png", f="wordbox.png", g="wordbox_y.png",
                                   h="wordbox_t.png", i="wordbox_e.png", j="wordbox_i.png",
                                   k="wordbox_v.png", l="wordbox_p.png", m="wordbox.png",
                                   n="wordbox_z.png", o="wordbox_q.png", p="wordbox.png",
                                   q="wordbox_l.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_351_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=351,
                                   question="On which planet does Vers live in the Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_e.png", c="wordbox_g.png", d="wordbox_l.png",
                                   e="wordbox_i.png", f="wordbox_d.png", g="wordbox_m.png",
                                   h="wordbox_p.png", i="wordbox_h.png", j="wordbox_k.png",
                                   k="wordbox_f.png", l="wordbox.png", m="wordbox_n.png",
                                   n="wordbox_q.png", o="wordbox.png", p="wordbox_o.png",
                                   q="wordbox_j.png", r="wordbox_c.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_352_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=352,
                                   question="What is the superhero name of the character Vers",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_b.png", c="wordbox_x.png", d="wordbox_r.png",
                                   e="wordbox_c.png", f="wordbox.png", g="wordbox_y.png",
                                   h="wordbox_t.png", i="wordbox_e.png", j="wordbox_i.png",
                                   k="wordbox_v.png", l="wordbox_p.png", m="wordbox.png",
                                   n="wordbox_z.png", o="wordbox_q.png", p="wordbox.png",
                                   q="wordbox_l.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_353_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=353,
                                   question="Who trains Vers in combat skills on the planet Hala in the Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_g.png", c="wordbox_f.png", d="wordbox_o.png",
                                   e="wordbox.png", f="wordbox_y.png", g="wordbox_n.png",
                                   h="wordbox_j.png", i="wordbox_b.png", j="wordbox_h.png",
                                   k="wordbox_o.png", l="wordbox_e.png", m="wordbox_d.png",
                                   n="wordbox_q.png", o="wordbox_r.png", p="wordbox_i.png",
                                   q="wordbox_c.png", r="wordbox_g.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_354_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=354,
                                   question="Who is the Kree operative that the team led by Vers aims to rescue in the Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_p.png", c="wordbox_z.png", d="wordbox_o.png",
                                   e="wordbox.png", f="wordbox_d.png", g="wordbox_q.png",
                                   h="wordbox_h.png", i="wordbox_y.png", j="wordbox_b.png",
                                   k="wordbox_t.png", l="wordbox_r.png", m="wordbox_w.png",
                                   n="wordbox_c.png", o="wordbox_l.png", p="wordbox_v.png",
                                   q="wordbox_x.png", r="wordbox_s.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_355_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=355,
                                   question="On which planet was Soh-Larr trapped in the Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_d.png", c="wordbox_s.png", d="wordbox_r.png",
                                   e="wordbox_p.png", f="wordbox_t.png", g="wordbox_c.png",
                                   h="wordbox_o.png", i="wordbox_p.png", j="wordbox_q.png",
                                   k="wordbox_q.png", l="wordbox_b.png", m="wordbox_n.png",
                                   n="wordbox_p.png", o="wordbox_b.png", p="wordbox_f.png",
                                   q="wordbox.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_356_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=356,
                                   question="What is the name of the Skrull general in the Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_x.png", c="wordbox_b.png", d="wordbox_z.png",
                                   e="wordbox_s.png", f="wordbox_q.png", g="wordbox_c.png",
                                   h="wordbox_t.png", i="wordbox_y.png", j="wordbox_w.png",
                                   k="wordbox_r.png", l="wordbox.png", m="wordbox_u.png",
                                   n="wordbox_d.png", o="wordbox_o.png", p="wordbox_e.png",
                                   q="wordbox_v.png", r="wordbox_p.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_357_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=357,
                                   question="On which planet did Captain Marvel crash-land after falling from a Kree spaceship in the Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_g.png",
                                   b="wordbox_v.png", c="wordbox_t.png", d="wordbox_q.png", e="wordbox_p.png",
                                   f="wordbox_m.png",
                                   g="wordbox_h.png", h="wordbox_p.png", i="wordbox_r.png", j="wordbox_k.png",
                                   k="wordbox.png",
                                   l="wordbox_c.png", m="wordbox_o.png", n="wordbox_l.png", o="wordbox_e.png",
                                   p="wordbox_m.png", q="wordbox_i.png", r="wordbox_b.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_358_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=358,
                                   question="What was the name of the C-53 planet in the Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_g.png",
                                   b="wordbox_v.png", c="wordbox_t.png", d="wordbox_q.png", e="wordbox_p.png",
                                   f="wordbox_m.png",
                                   g="wordbox_h.png", h="wordbox_p.png", i="wordbox_r.png", j="wordbox_k.png",
                                   k="wordbox.png",
                                   l="wordbox_c.png", m="wordbox_o.png", n="wordbox_l.png", o="wordbox_e.png",
                                   p="wordbox_m.png", q="wordbox_i.png", r="wordbox_b.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_359_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=359,
                                   question="Who is Vers' best friend in the Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_t.png", c="wordbox_q.png", d="wordbox_q.png",
                                   e="wordbox_i.png", f="wordbox_m.png", g="wordbox.png",
                                   h="wordbox_r.png", i="wordbox_u.png", j="wordbox_v.png",
                                   k="wordbox_m.png", l="wordbox_p.png", m="wordbox_w.png",
                                   n="wordbox_b.png", o="wordbox.png", p="wordbox_e.png",
                                   q="wordbox.png", r="wordbox.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_360_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=360,
                                   question="What is the name of the cat that appears in the Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox.png", c="wordbox_h.png", d="wordbox_i.png",
                                   e="wordbox_b.png", f="wordbox_e.png", g="wordbox_k.png",
                                   h="wordbox_n.png", i="wordbox_j.png", j="wordbox_g.png",
                                   k="wordbox_c.png", l="wordbox_d.png", m="wordbox_s.png",
                                   n="wordbox_l.png", o="wordbox_m.png", p="wordbox_g.png",
                                   q="wordbox_f.png", r="wordbox_o.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_361_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=361,
                                   question="Who plays the character of carol danvers in the captain marvel movie",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_q.png", c="wordbox_s.png", d="wordbox_y.png",
                                   e="wordbox_p.png", f="wordbox_i.png", g="wordbox_l.png",
                                   h="wordbox_x.png", i="wordbox.png", j="wordbox_v.png",
                                   k="wordbox_r.png", l="wordbox_n.png", m="wordbox_e.png",
                                   n="wordbox_w.png", o="wordbox_o.png", p="wordbox_z.png",
                                   q="wordbox_m.png", r="wordbox_b.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_362_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=362,
                                   question="Who plays the S.H.I.E.L.D. agent who accompanies Vers in the Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox.png", c="wordbox_u.png", d="wordbox_l.png", e="wordbox_s.png",
                                   f="wordbox_r.png",
                                   g="wordbox_p.png", h="wordbox_g.png", i="wordbox_t.png", j="wordbox_f.png",
                                   k="wordbox.png",
                                   l="wordbox_y.png", m="wordbox_q.png", n="wordbox_k.png", o="wordbox_m.png",
                                   p="wordbox_i.png", q="wordbox_d.png", r="wordbox_c.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_363_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=363,
                                   question="Who invented the light engine in the Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_z.png",
                                   b="wordbox_w.png", c="wordbox.png", d="wordbox_m.png",
                                   e="wordbox_q.png", f="wordbox_y.png", g="wordbox_r.png",
                                   h="wordbox_d.png", i="wordbox_p.png", j="wordbox_e.png",
                                   k="wordbox_o.png", l="wordbox_x.png", m="wordbox_n.png",
                                   n="wordbox_l.png", o="wordbox_s.png", p="wordbox_t.png",
                                   q="wordbox_n.png", r="wordbox_w.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_364_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=364,
                                   question="What is Dr. Wendy Lawson's alias in the Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_q.png",
                                   b="wordbox_e.png", c="wordbox_t.png", d="wordbox_m.png",
                                   e="wordbox_s.png", f="wordbox_p.png", g="wordbox_d.png",
                                   h="wordbox.png", i="wordbox_u.png", j="wordbox_l.png",
                                   k="wordbox_w.png", l="wordbox_l.png", m="wordbox_z.png",
                                   n="wordbox_o.png", o="wordbox_x.png", p="wordbox_v.png",
                                   q="wordbox_y.png", r="wordbox_r.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_365_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=365,
                                   question="What was the power source used to fuel the light engine in the Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_t.png", c="wordbox_q.png", d="wordbox_e.png", e="wordbox_f.png",
                                   f="wordbox_e.png",
                                   g="wordbox_s.png", h="wordbox_b.png", i="wordbox_s.png", j="wordbox_j.png",
                                   k="wordbox.png",
                                   l="wordbox_o.png", m="wordbox_m.png", n="wordbox_r.png", o="wordbox_k.png",
                                   p="wordbox_c.png", q="wordbox_n.png", r="wordbox_t.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_366_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=366,
                                   question="In which desert does the fight between Captain Marvel and Yon-Rogg occur in the Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_q.png",
                                   b="wordbox_t.png", c="wordbox_s.png", d="wordbox_e.png",
                                   e="wordbox_r.png", f="wordbox_u.png", g="wordbox_p.png",
                                   h="wordbox_m.png", i="wordbox_w.png", j="wordbox_v.png",
                                   k="wordbox_x.png", l="wordbox_o.png", m="wordbox_l.png",
                                   n="wordbox.png", o="wordbox_n.png", p="wordbox_z.png",
                                   q="wordbox_j.png", r="wordbox_y.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_367_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=367,
                                   question="What is the Name of the supreme intelligence person on the earth in Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_z.png",
                                   b="wordbox_w.png", c="wordbox.png", d="wordbox_m.png",
                                   e="wordbox_q.png", f="wordbox_y.png", g="wordbox_r.png",
                                   h="wordbox_d.png", i="wordbox_p.png", j="wordbox_e.png",
                                   k="wordbox_o.png", l="wordbox_x.png", m="wordbox_n.png",
                                   n="wordbox_l.png", o="wordbox_s.png", p="wordbox_t.png",
                                   q="wordbox_n.png", r="wordbox_w.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_368_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=368,
                                   question="What name does Vers go by on Earth in the Captain Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_r.png", c="wordbox.png", d="wordbox_y.png",
                                   e="wordbox_e.png", f="wordbox_r.png", g="wordbox_w.png",
                                   h="wordbox_v.png", i="wordbox_t.png", j="wordbox_c.png",
                                   k="wordbox_n.png", l="wordbox_s.png", m="wordbox_u.png",
                                   n="wordbox_d.png", o="wordbox_x.png", p="wordbox_z.png",
                                   q="wordbox.png", r="wordbox_o.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_369_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=369,
                                   question="What is the name of the AI system that Tony Stark uses to guide Peter Parker in the Spider-Man: Far From Home",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_q.png", c="wordbox_z.png", d="wordbox_m.png",
                                   e="wordbox_r.png", f="wordbox_x.png", g="wordbox_u.png",
                                   h="wordbox_y.png", i="wordbox_e.png", j="wordbox_n.png",
                                   k="wordbox_i.png", l="wordbox_o.png", m="wordbox_v.png",
                                   n="wordbox_p.png", o="wordbox_s.png", p="wordbox_h.png",
                                   q="wordbox_l.png", r="wordbox_d.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_370_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=370,
                                   question="What type of suit does Spider-Man wear in the SpiderMan Far From Home movie, before creating his main suit",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_x.png", c="wordbox_t.png", d="wordbox_p.png",
                                   e="wordbox_y.png", f="wordbox_l.png", g="wordbox_w.png",
                                   h="wordbox_q.png", i="wordbox_t.png", j="wordbox_n.png",
                                   k="wordbox_m.png", l="wordbox_s.png", m="wordbox_h.png",
                                   n="wordbox_r.png", o="wordbox_v.png", p="wordbox.png",
                                   q="wordbox_z.png", r="wordbox_o.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_371_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=371,
                                   question="What character does Jake Gyllenhaal portray in the movie Spider-Man Far From Home",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_x.png", c="wordbox_t.png", d="wordbox_d.png",
                                   e="wordbox_u.png", f="wordbox_m.png", g="wordbox_g.png",
                                   h="wordbox_v.png", i="wordbox_c.png", j="wordbox_y.png",
                                   k="wordbox_i.png", l="wordbox_q.png", m="wordbox_w.png",
                                   n="wordbox_s.png", o="wordbox_o.png", p="wordbox_z.png",
                                   q="wordbox_e.png", r="wordbox_b.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_372_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=372,
                                   question="Who is the main antagonist in the movie SpiderMan Far From Home",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_x.png", c="wordbox_t.png", d="wordbox_d.png",
                                   e="wordbox_u.png", f="wordbox_m.png", g="wordbox_g.png",
                                   h="wordbox_v.png", i="wordbox_c.png", j="wordbox_y.png",
                                   k="wordbox_i.png", l="wordbox_q.png", m="wordbox_w.png",
                                   n="wordbox_s.png", o="wordbox_o.png", p="wordbox_z.png",
                                   q="wordbox_e.png", r="wordbox_b.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_373_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=373,
                                   question="What is the name of the high-tech glasses given to Peter Parker by Tony Stark in Far From Home",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_q.png", c="wordbox_z.png", d="wordbox_m.png",
                                   e="wordbox_r.png", f="wordbox_x.png", g="wordbox_u.png",
                                   h="wordbox_y.png", i="wordbox_e.png", j="wordbox_n.png",
                                   k="wordbox_i.png", l="wordbox_o.png", m="wordbox_v.png",
                                   n="wordbox_p.png", o="wordbox_s.png", p="wordbox_h.png",
                                   q="wordbox_l.png", r="wordbox_d.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_374_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=374,
                                   question="What is the name of the technology used by the Mysterio in the far from home movie",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_k.png", c="wordbox_p.png", d="wordbox_t.png",
                                   e="wordbox_q.png", f="wordbox_s.png", g="wordbox_s.png",
                                   h="wordbox_l.png", i="wordbox_f.png", j="wordbox_o.png",
                                   k="wordbox_m.png", l="wordbox_p.png", m="wordbox_r.png",
                                   n="wordbox_j.png", o="wordbox_s.png", p="wordbox_t.png",
                                   q="wordbox_k.png", r="wordbox_b.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_375_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=375,
                                   question="What is the name of the organization led by Nick Fury and Maria Hill in the movie SpiderMan Far From Home",
                                   levelcounter=str(self.count),a="wordbox_o.png",
                                   b="wordbox_s.png", c="wordbox_b.png", d="wordbox_k.png", e="wordbox_m.png",
                                   f="wordbox_l.png",
                                   g="wordbox_e.png", h="wordbox_p.png", i="wordbox_q.png", j="wordbox_d.png",
                                   k="wordbox_m.png",
                                   l="wordbox_g.png", m="wordbox_f.png", n="wordbox_t.png", o="wordbox_i.png",
                                   p="wordbox.png", q="wordbox_n.png", r="wordbox_h.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_376_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=376,
                                   question="What is the name of the  Mysterio in the far from home movie",
                                   levelcounter=str(self.count), a="wordbox_v.png",
                                   b="wordbox_t.png", c="wordbox_p.png", d="wordbox_e.png",
                                   e="wordbox_o.png", f="wordbox_q.png", g="wordbox_e.png",
                                   h="wordbox_d.png", i="wordbox_u.png", j="wordbox_l.png",
                                   k="wordbox_b.png", l="wordbox_c.png", m="wordbox_n.png",
                                   n="wordbox_k.png", o="wordbox_m.png", p="wordbox_n.png",
                                   q="wordbox_w.png", r="wordbox_i.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_377_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=377,
                                   question="Who portrays the character of MJ in the movie SpiderMan Far From Home",
                                   levelcounter=str(self.count), a="wordbox_z.png",
                                   b="wordbox_s.png", c="wordbox_t.png", d="wordbox.png",
                                   e="wordbox_b.png", f="wordbox_o.png", g="wordbox_w.png",
                                   h="wordbox_d.png", i="wordbox_c.png", j="wordbox_v.png",
                                   k="wordbox_u.png", l="wordbox_e.png", m="wordbox.png",
                                   n="wordbox_f.png", o="wordbox_g.png", p="wordbox_n.png",
                                   q="wordbox_x.png", r="wordbox_y.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_378_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=378,
                                   question="Who portrays the character of Peter Parker in the movie SpiderMan Far From Home",
                                   levelcounter=str(self.count), a="wordbox_d.png",
                                   b="wordbox_y.png", c="wordbox_t.png", d="wordbox_z.png",
                                   e="wordbox_o.png", f="wordbox_l.png", g="wordbox_o.png",
                                   h="wordbox_w.png", i="wordbox.png", j="wordbox_b.png",
                                   k="wordbox_h.png", l="wordbox_q.png", m="wordbox_b.png",
                                   n="wordbox_l.png", o="wordbox_u.png", p="wordbox_m.png",
                                   q="wordbox_v.png", r="wordbox_n.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_379_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=379,
                                   question="What is the  name of  carol Danvers on the hela planet in caption Marvel movie",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_c.png", c="wordbox_k.png", d="wordbox_j.png",
                                   e="wordbox.png", f="wordbox_e.png", g="wordbox_n.png",
                                   h="wordbox_i.png", i="wordbox_v.png", j="wordbox_f.png",
                                   k="wordbox_g.png", l="wordbox_d.png", m="wordbox_o.png",
                                   n="wordbox_h.png", o="wordbox_l.png", p="wordbox_m.png",
                                   q="wordbox_b.png", r="wordbox_s.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_380_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=380,
                                   question="In the movie Avengers Endgame, who or what is the reason for Scott Lang to come out from the Quantum Realm",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_f.png", c="wordbox_p.png", d="wordbox_c.png",
                                   e="wordbox_d.png", f="wordbox_l.png", g="wordbox_m.png",
                                   h="wordbox.png", i="wordbox_q.png", j="wordbox_s.png",
                                   k="wordbox_l.png", l="wordbox_f.png", m="wordbox_o.png",
                                   n="wordbox_f.png", o="wordbox_m.png", p="wordbox_p.png",
                                   q="wordbox_t.png", r="wordbox_q.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )





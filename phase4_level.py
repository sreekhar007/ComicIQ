import levels_game2
import coin_inc
import allhint
from kivy.storage.jsonstore import JsonStore
class phase4_questions(coin_inc.coininc,allhint.hint_all):
    def __init__(self):
        # {"gamescreen": {"level": 400,
        #                 "question": "Where is the fictional town of Westview located in the WandaVision series",
        #                 "words": ["wordbox_w.png", "wordbox_k.png", "wordbox_r.png", "wordbox_f.png", "wordbox_y.png",
        #                           "wordbox_e.png", "wordbox_k.png", "wordbox_f.png", "wordbox_j.png", "wordbox_l.png",
        #                           "wordbox_p.png", "wordbox_t.png", "wordbox_n.png", "wordbox_s.png", "wordbox_o.png",
        #                           "wordbox_e.png", "wordbox_t.png", "wordbox_e.png"], "levelcounter": "1/200",
        #                 "vacentbox": ["bor.png", "bor.png", "bor.png", "bor.png", "bor.png", "bor.png", "bor.png",
        #                               "bor.png", "bor.png", "mix.png", "mix.png", "mix.png", "mix.png", "mix.png",
        #                               "mix.png"]}}
        self.counters = ["2/200", "3/200", "4/200", "5/200", "6/200", "7/200", "8/200", "9/200", "10/200", "11/200",
                         "12/200", "13/200", "14/200", "15/200",
                         "16/200", "17/200", "18/200", "19/200", "20/200", "21/200", "22/200", "23/200", "24/200",
                         "25/200", "26/200", "27/200", "28/200", "29/200", "30/200",
                         "31/200", "32/200", "33/200", "34/200", "35/200", "36/200", "37/200", "38/200", "39/200",
                         "40/200", "41/200", "42/200", "43/200", "44/200", "45/200",
                         "46/200", "47/200", "48/200", "49/200", "50/200", "51/200", "52/200", "53/200", "54/200",
                         "55/200", "56/200", "57/200", "58/200", "59/200", "60/200",
                         "61/200", "62/200", "63/200", "64/200", "65/200", "66/200", "67/200", "68/200", "69/200",
                         "70/200", "71/200", "72/200", "73/200", "74/200", "75/200",
                         "76/200", "77/200", "78/200", "79/200", "80/200", "81/200", "82/200", "83/200", "84/200",
                         "85/200", "86/200", "87/200", "88/200", "89/200", "90/200",
                         "91/200", "92/200", "93/200", "94/200", "95/200", "96/200", "97/200", "98/200", "99/200",
                         "100/200", "101/200", "102/200", "103/200", "104/200", "105/200", "106/200", "107/200",
                         "108/200", "109/200", "110/200", "111/200", "112/200", "113/200", "114/200", "115/200",
                         "116/200", "117/200", "118/200", "119/200", "120/200", "121/200", "122/200", "123/200",
                         "124/200", "125/200", "126/200", "127/200", "128/200", "129/200", "130/200", "131/200",
                         "132/200", "133/200", "134/200", "135/200", "136/200", "137/200", "138/200", "139/200",
                         "140/200", "141/200", "142/200", "143/200", "144/200", "145/200", "146/200", "147/200",
                         "148/200", "149/200", "150/200", "151/200", "152/200", "153/200", "154/200", "155/200",
                         "156/200", "157/200", "158/200", "159/200", "160/200", "161/200", "162/200", "163/200",
                         "164/200", "165/200", "166/200", "167/200", "168/200", "169/200", "170/200", "171/200",
                         "172/200", "173/200", "174/200", "175/200", "176/200", "177/200", "178/200", "179/200",
                         "180/200","181/200","182/200","183/200","184/200","185/200","186/200","187/200","188/200","189/200","190/200",
                         "191/200","192/200","193/200","194/200","195/200","196/200","181/200","197/200","198/200","199/200","200/200"]
    def counter(self,*args):

        lev_coun = JsonStore("counter3.json")
        lst = lev_coun.get("random_level_list")["number"]
        s = lev_coun.get("random_level_list")["number"][0]

        lst.remove(s)
        lev_coun.put("random_level_list",number = lst)
        return self.counters[s]
    def level_401_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0

        self.changing_words_blanks(level=401,
                                   question="What is the name of the neighbor who frequently visits Wanda's house in the WandaVision series",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_p.png", c="wordbox.png", d="wordbox_q.png",
                                   e="wordbox_t.png", f="wordbox_f.png", g="wordbox_g.png",
                                   h="wordbox_t.png", i="wordbox_l.png", j="wordbox_e.png",
                                   k="wordbox_f.png", l="wordbox_n.png", m="wordbox_s.png",
                                   n="wordbox_w.png", o="wordbox_m.png", p="wordbox_b.png",
                                   q="wordbox_l.png", r="wordbox_f.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_402_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=402,
                                   question="Who invited Arthur Hart to Wanda's house in the WandaVision series",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_p.png", c="wordbox.png", d="wordbox_q.png",
                                   e="wordbox_t.png", f="wordbox_f.png", g="wordbox_g.png",
                                   h="wordbox_t.png", i="wordbox_l.png", j="wordbox_e.png",
                                   k="wordbox_f.png", l="wordbox_n.png", m="wordbox_s.png",
                                   n="wordbox_w.png", o="wordbox_m.png", p="wordbox_b.png",
                                   q="wordbox_l.png", r="wordbox_f.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_403_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=403,
                                   question="Who plays the character of Vision's boss,in the WandaVision series",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_t.png", c="wordbox_k.png", d="wordbox_o.png",
                                   e="wordbox_t.png", f="wordbox_r.png", g="wordbox.png",
                                   h="wordbox_p.png", i="wordbox_u.png", j="wordbox_s.png",
                                   k="wordbox_l.png", l="wordbox.png", m="wordbox_h.png",
                                   n="wordbox_f.png", o="wordbox_r.png", p="wordbox_l.png",
                                   q="wordbox_s.png", r="wordbox_h.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_404_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=404,
                                   question="Who is the younger twin among the children of Wanda",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_s.png", c="wordbox_p.png", d="wordbox_q.png",
                                   e="wordbox_v.png", f="wordbox_i.png", g="wordbox_t.png",
                                   h="wordbox_m.png", i="wordbox_y.png", j="wordbox_s.png",
                                   k="wordbox_o.png", l="wordbox_n.png", m="wordbox_b.png",
                                   n="wordbox_m.png", o="wordbox_s.png", p="wordbox_o.png",
                                   q="wordbox_l.png", r="wordbox_q.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_405_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=405,
                                   question="Who is the elder twin among the children of Wanda",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox_s.png", c="wordbox_p.png", d="wordbox_q.png",
                                   e="wordbox_v.png", f="wordbox_o.png", g="wordbox_v.png",
                                   h="wordbox_h.png", i="wordbox_y.png", j="wordbox_s.png",
                                   k="wordbox_k.png", l="wordbox_n.png", m="wordbox_t.png",
                                   n="wordbox_h.png", o="wordbox_s.png", p="wordbox_k.png",
                                   q="wordbox_m.png", r="wordbox_q.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_406_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=406,
                                   question="What is the name of the book featured in the WandaVision series",
                                   levelcounter=str(self.count), a="wordbox_d.png",
                                   b="wordbox_p.png", c="wordbox_o.png", d="wordbox_q.png",
                                   e="wordbox_v.png", f="wordbox_d.png", g="wordbox_l.png",
                                   h="wordbox_n.png", i="wordbox.png", j="wordbox_r.png",
                                   k="wordbox_m.png", l="wordbox_f.png", m="wordbox_k.png",
                                   n="wordbox_f.png", o="wordbox_m.png", p="wordbox_j.png",
                                   q="wordbox_f.png", r="wordbox_h.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_407_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=407,
                                   question="What is the name of the dog in the WandaVision series",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_t.png", c="wordbox_j.png", d="wordbox_q.png",
                                   e="wordbox_v.png", f="wordbox_y.png", g="wordbox_s.png",
                                   h="wordbox_m.png", i="wordbox_v.png", j="wordbox.png",
                                   k="wordbox_n.png", l="wordbox_t.png", m="wordbox_f.png",
                                   n="wordbox_r.png", o="wordbox_g.png", p="wordbox_o.png",
                                   q="wordbox_k.png", r="wordbox_b.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_408_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=408,
                                   question="In what geometric shape did Wanda create the town of Westview in the WandaVision series",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_f.png", c="wordbox_g.png", d="wordbox_q.png",
                                   e="wordbox_x.png", f="wordbox_t.png", g="wordbox.png",
                                   h="wordbox_t.png", i="wordbox_h.png", j="wordbox_s.png",
                                   k="wordbox_j.png", l="wordbox_c.png", m="wordbox_c.png",
                                   n="wordbox_o.png", o="wordbox_b.png", p="wordbox_s.png",
                                   q="wordbox_n.png", r="wordbox_p.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_409_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=409,
                                   question="Who sends Monica Rambeau to investigate the anomaly in Westview in the WandaVision series",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_p.png", c="wordbox_j.png", d="wordbox_q.png",
                                   e="wordbox_o.png", f="wordbox_s.png", g="wordbox_b.png",
                                   h="wordbox_o.png", i="wordbox_n.png", j="wordbox_y.png",
                                   k="wordbox_k.png", l="wordbox_f.png", m="wordbox_t.png",
                                   n="wordbox_m.png", o="wordbox_k.png", p="wordbox_m.png",
                                   q="wordbox.png", r="wordbox_w.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_410_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=410,
                                   question="Who is the FBI agent that Monica meets for case details in the WandaVision series",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_p.png", c="wordbox_j.png", d="wordbox_q.png",
                                   e="wordbox_o.png", f="wordbox_s.png", g="wordbox_b.png",
                                   h="wordbox_o.png", i="wordbox_n.png", j="wordbox_y.png",
                                   k="wordbox_k.png", l="wordbox_f.png", m="wordbox_t.png",
                                   n="wordbox_m.png", o="wordbox_k.png", p="wordbox_m.png",
                                   q="wordbox.png", r="wordbox_w.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_411_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=411,
                                   question="Who is the character that Wanda meets at the country club meeting in the WandaVision series",
                                   levelcounter=str(self.count), a="wordbox_g.png",
                                   b="wordbox_k.png", c="wordbox_t.png", d="wordbox_e.png",
                                   e="wordbox_p.png", f="wordbox_i.png", g="wordbox_n.png",
                                   h="wordbox_q.png", i="wordbox_r.png", j="wordbox.png",
                                   k="wordbox_s.png", l="wordbox_y.png", m="wordbox_d.png",
                                   n="wordbox_p.png", o="wordbox_j.png", p="wordbox_e.png",
                                   q="wordbox_s.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_412_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=412,
                                   question="Which organization operates similarly to S.H.I.E.L.D. in the WandaVision series",
                                   levelcounter=str(self.count), a="wordbox_w.png",
                                   b="wordbox_c.png", c="wordbox_o.png", d="wordbox_t.png",
                                   e="wordbox_p.png", f="wordbox_k.png", g="wordbox_k.png",
                                   h="wordbox_s.png", i="wordbox_q.png", j="wordbox_j.png",
                                   k="wordbox_h.png", l="wordbox_s.png", m="wordbox_r.png",
                                   n="wordbox_g.png", o="wordbox_u.png", p="wordbox_m.png",
                                   q="wordbox_s.png", r="wordbox_d.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_413_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=413,
                                   question="What is the name of the town that Wanda creates as her own world in the WandaVision series",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_p.png", c="wordbox_k.png", d="wordbox_s.png",
                                   e="wordbox_l.png", f="wordbox_t.png", g="wordbox_w.png",
                                   h="wordbox_n.png", i="wordbox_v.png", j="wordbox_o.png",
                                   k="wordbox_i.png", l="wordbox_u.png", m="wordbox_j.png",
                                   n="wordbox_e.png", o="wordbox_u.png", p="wordbox_w.png",
                                   q="wordbox_q.png", r="wordbox_h.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_414_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=414,
                                   question="Which scientist does S.W.O.R.D. approach for scientific expertise in the WandaVision series",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_f.png", c="wordbox_r.png", d="wordbox_i.png",
                                   e="wordbox_k.png", f="wordbox_c.png", g="wordbox_w.png",
                                   h="wordbox_q.png", i="wordbox_d.png", j="wordbox_v.png",
                                   k="wordbox_n.png", l="wordbox_s.png", m="wordbox_y.png",
                                   n="wordbox_k.png", o="wordbox_u.png", p="wordbox_l.png",
                                   q="wordbox_n.png", r="wordbox_e.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_415_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=415,
                                   question="Who is the director of the S.W.O.R.D. team in the WandaVision series",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_t.png", c="wordbox_k.png", d="wordbox_y.png",
                                   e="wordbox_e.png", f="wordbox_f.png", g="wordbox_y.png",
                                   h="wordbox_w.png", i="wordbox_k.png", j="wordbox_l.png",
                                   k="wordbox_q.png", l="wordbox_h.png", m="wordbox.png",
                                   n="wordbox_s.png", o="wordbox_r.png", p="wordbox_r.png",
                                   q="wordbox_u.png", r="wordbox_d.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_416_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=416,
                                   question="Who is responsible for sending a person to find Monica in the WandaVision series",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_t.png", c="wordbox_k.png", d="wordbox_y.png",
                                   e="wordbox_e.png", f="wordbox_f.png", g="wordbox_y.png",
                                   h="wordbox_w.png", i="wordbox_k.png", j="wordbox_l.png",
                                   k="wordbox_q.png", l="wordbox_h.png", m="wordbox.png",
                                   n="wordbox_s.png", o="wordbox_r.png", p="wordbox_r.png",
                                   q="wordbox_u.png", r="wordbox_d.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_417_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=417,
                                   question="where did the Natasha Romanoff spent her childhood",
                                   levelcounter=str(self.count), a="wordbox_u.png",
                                   b="wordbox_p.png", c="wordbox_i.png", d="wordbox_q.png",
                                   e="wordbox_t.png", f="wordbox_c.png", g="wordbox_s.png",
                                   h="wordbox_k.png", i="wordbox_v.png", j="wordbox_s.png",
                                   k="wordbox_j.png", l="wordbox_m.png", m="wordbox_w.png",
                                   n="wordbox_r.png", o="wordbox_q.png", p="wordbox.png",
                                   q="wordbox_n.png", r="wordbox_o.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_418_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=418,
                                   question="What is the name of Natasha Romanoff's sister in the Marvel Cinematic Universe",
                                   levelcounter=str(self.count), a="wordbox_y.png",
                                   b="wordbox_k.png", c="wordbox_e.png", d="wordbox_l.png",
                                   e="wordbox_u.png", f="wordbox_v.png", g="wordbox_b.png",
                                   h="wordbox.png", i="wordbox_e.png", j="wordbox_s.png",
                                   k="wordbox_s.png", l="wordbox_o.png", m="wordbox_e.png",
                                   n="wordbox_p.png", o="wordbox_n.png", p="wordbox.png",
                                   q="wordbox_q.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_419_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=419,
                                   question="Whom did Dreykov send Taskmaster to kill in the film Black Widow",
                                   levelcounter=str(self.count), a="wordbox_y.png",
                                   b="wordbox_k.png", c="wordbox_e.png", d="wordbox_l.png",
                                   e="wordbox_u.png", f="wordbox_v.png", g="wordbox_b.png",
                                   h="wordbox.png", i="wordbox_e.png", j="wordbox_s.png",
                                   k="wordbox_s.png", l="wordbox_o.png", m="wordbox_e.png",
                                   n="wordbox_p.png", o="wordbox_n.png", p="wordbox.png",
                                   q="wordbox_q.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_420_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=420,
                                   question="Who sent the antidotes to Natasha Romanoff in the film Black Widow",
                                   levelcounter=str(self.count), a="wordbox_y.png",
                                   b="wordbox_k.png", c="wordbox_e.png", d="wordbox_l.png",
                                   e="wordbox_u.png", f="wordbox_v.png", g="wordbox_b.png",
                                   h="wordbox.png", i="wordbox_e.png", j="wordbox_s.png",
                                   k="wordbox_s.png", l="wordbox_o.png", m="wordbox_e.png",
                                   n="wordbox_p.png", o="wordbox_n.png", p="wordbox.png",
                                   q="wordbox_q.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_421_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=421,
                                   question="Who is referred to as the Red Guardian in the movie Black Widow",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_i.png", c="wordbox_f.png", d="wordbox_s.png",
                                   e="wordbox_k.png", f="wordbox_s.png", g="wordbox.png",
                                   h="wordbox_x.png", i="wordbox_o.png", j="wordbox_e.png",
                                   k="wordbox_o.png", l="wordbox_e.png", m="wordbox_v.png",
                                   n="wordbox_q.png", o="wordbox.png", p="wordbox_h.png",
                                   q="wordbox_d.png", r="wordbox_t.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="bor.png", em_15="bor.png"

                                   )
    def level_422_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=422,
                                   question="Who is revealed to be Taskmaster in the movie Black Widow",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_k.png", c="wordbox.png", d="wordbox_p.png",
                                   e="wordbox_q.png", f="wordbox_i.png", g="wordbox_u.png",
                                   h="wordbox_f.png", i="wordbox_d.png", j="wordbox_t.png",
                                   k="wordbox_s.png", l="wordbox_n.png", m="wordbox_o.png",
                                   n="wordbox_c.png", o="wordbox_s.png", p="wordbox_f.png",
                                   q="wordbox_v.png", r="wordbox.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_423_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=423,
                                   question="What is the name of General Dreykov's daughter in the movie Black Widow",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_k.png", c="wordbox.png", d="wordbox_p.png",
                                   e="wordbox_q.png", f="wordbox_i.png", g="wordbox_u.png",
                                   h="wordbox_f.png", i="wordbox_d.png", j="wordbox_t.png",
                                   k="wordbox_s.png", l="wordbox_n.png", m="wordbox_o.png",
                                   n="wordbox_c.png", o="wordbox_s.png", p="wordbox_f.png",
                                   q="wordbox_v.png", r="wordbox.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_424_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=424,
                                   question="In which country did Alexei Shostakov, conduct his spy activities in the movie Black Widow",
                                   levelcounter=str(self.count), a="wordbox_u.png",
                                   b="wordbox_p.png", c="wordbox_i.png", d="wordbox_q.png",
                                   e="wordbox_t.png", f="wordbox_c.png", g="wordbox_s.png",
                                   h="wordbox_k.png", i="wordbox_v.png", j="wordbox_s.png",
                                   k="wordbox_j.png", l="wordbox_m.png", m="wordbox_w.png",
                                   n="wordbox_r.png", o="wordbox_q.png", p="wordbox.png",
                                   q="wordbox_n.png", r="wordbox_o.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_425_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=425,
                                   question="In which region of Russia was Alexei Shostakov, imprisoned in the movie Black Widow",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_p.png", c="wordbox_i.png", d="wordbox_k.png", e="wordbox_i.png",
                                   f="wordbox_f.png",
                                   g="wordbox_o.png", h="wordbox_l.png", i="wordbox_r.png", j="wordbox_k.png",
                                   k="wordbox.png",
                                   l="wordbox_w.png", m="wordbox_s.png", n="wordbox_y.png", o="wordbox_m.png",
                                   p="wordbox_o.png", q="wordbox_e.png", r="wordbox_q.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_426_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=426,
                                   question="What is the name of ShangChi's father in the movie the Legend of the Ten Rings",
                                   levelcounter=str(self.count), a="wordbox_w.png",
                                   b="wordbox_k.png", c="wordbox_p.png", d="wordbox_t.png", e="wordbox_o.png",
                                   f="wordbox_w.png",
                                   g="wordbox_l.png", h="wordbox_s.png", i="wordbox_e.png", j="wordbox_z.png",
                                   k="wordbox_u.png",
                                   l="wordbox_k.png", m="wordbox_j.png", n="wordbox_y.png", o="wordbox_q.png",
                                   p="wordbox_c.png", q="wordbox.png", r="wordbox_n.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_427_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=427,
                                   question="What is the name of Wenwu's son in the movie the Legend of the Ten Rings",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_k.png", c="wordbox.png", d="wordbox_o.png", e="wordbox_j.png",
                                   f="wordbox_i.png",
                                   g="wordbox_m.png", h="wordbox_p.png", i="wordbox_s.png", j="wordbox_h.png",
                                   k="wordbox_k.png",
                                   l="wordbox_g.png", m="wordbox_c.png", n="wordbox_q.png", o="wordbox_o.png",
                                   p="wordbox_v.png", q="wordbox_k.png", r="wordbox_n.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_428_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=428,
                                   question="What is the name of Xu Wenwu's daughter in the movie the Legend of the Ten Rings",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_p.png", c="wordbox.png", d="wordbox_k.png", e="wordbox_q.png",
                                   f="wordbox_t.png",
                                   g="wordbox_x.png", h="wordbox_t.png", i="wordbox_u.png", j="wordbox_l.png",
                                   k="wordbox_o.png",
                                   l="wordbox_g.png", m="wordbox_u.png", n="wordbox_i.png", o="wordbox_w.png",
                                   p="wordbox_n.png", q="wordbox_v.png", r="wordbox_k.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_429_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=429,
                                   question="What is the name of ShangChi's sister in the movie the Legend of the Ten Rings",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_p.png", c="wordbox.png", d="wordbox_k.png", e="wordbox_q.png",
                                   f="wordbox_t.png",
                                   g="wordbox_x.png", h="wordbox_t.png", i="wordbox_u.png", j="wordbox_l.png",
                                   k="wordbox_o.png",
                                   l="wordbox_g.png", m="wordbox_u.png", n="wordbox_i.png", o="wordbox_w.png",
                                   p="wordbox_n.png", q="wordbox_v.png", r="wordbox_k.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_430_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=430,
                                   question="What is the name of the hidden village that Xu Wenwu aims to reach in the movie the Legend of the Ten Rings",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_k.png", c="wordbox_l.png", d="wordbox_v.png", e="wordbox_u.png",
                                   f="wordbox_m.png",
                                   g="wordbox_j.png", h="wordbox_t.png", i="wordbox_p.png", j="wordbox_f.png",
                                   k="wordbox.png",
                                   l="wordbox_q.png", m="wordbox_p.png", n="wordbox_c.png", o="wordbox_o.png",
                                   p="wordbox_n.png", q="wordbox_b.png", r="wordbox_d.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_431_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=431,
                                   question="By what name is Xu Wenwu known in the movie the Legend of the Ten Rings",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox_k.png", c="wordbox.png", d="wordbox_p.png", e="wordbox_q.png",
                                   f="wordbox_n.png",
                                   g="wordbox.png", h="wordbox_f.png", i="wordbox_q.png", j="wordbox_d.png",
                                   k="wordbox_o.png",
                                   l="wordbox_r.png", m="wordbox_n.png", n="wordbox_v.png", o="wordbox_p.png",
                                   p="wordbox_i.png", q="wordbox_d.png", r="wordbox_w.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_432_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=432,
                                   question="What is the name of ShangChi's best friend in the movie the Legend of the Ten Rings",
                                   levelcounter=str(self.count), a="wordbox_w.png",
                                   b="wordbox_q.png", c="wordbox_u.png", d="wordbox.png", e="wordbox_v.png",
                                   f="wordbox_p.png",
                                   g="wordbox_k.png", h="wordbox_s.png", i="wordbox_t.png", j="wordbox_n.png",
                                   k="wordbox_u.png",
                                   l="wordbox_q.png", m="wordbox_d.png", n="wordbox_f.png", o="wordbox_p.png",
                                   p="wordbox_y.png", q="wordbox_o.png", r="wordbox_l.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_433_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=433,
                                   question="Who attacks Shang-Chi in the bus in the movie the Legend of the Ten Rings",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_t.png", c="wordbox_z.png", d="wordbox_p.png", e="wordbox_l.png",
                                   f="wordbox_o.png",
                                   g="wordbox.png", h="wordbox_p.png", i="wordbox_r.png", j="wordbox_q.png",
                                   k="wordbox_k.png",
                                   l="wordbox_i.png", m="wordbox_q.png", n="wordbox_j.png", o="wordbox_r.png",
                                   p="wordbox_m.png", q="wordbox_v.png", r="wordbox_f.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_434_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=434,
                                   question="With whom does Wong fight in the underground fight club in  the Legend of the Ten Rings",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_k.png", c="wordbox_i.png", d="wordbox_p.png", e="wordbox_o.png",
                                   f="wordbox_l.png",
                                   g="wordbox_m.png", h="wordbox_f.png", i="wordbox_n.png", j="wordbox_i.png",
                                   k="wordbox_s.png",
                                   l="wordbox_n.png", m="wordbox_b.png", n="wordbox_q.png", o="wordbox_o.png",
                                   p="wordbox_u.png", q="wordbox.png", r="wordbox_t.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_435_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=435,
                                   question="Who is revealed to be the owner of the underground fight club in the Legend of the Ten Rings",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_p.png", c="wordbox.png", d="wordbox_k.png", e="wordbox_q.png",
                                   f="wordbox_t.png",
                                   g="wordbox_x.png", h="wordbox_t.png", i="wordbox_u.png", j="wordbox_l.png",
                                   k="wordbox_o.png",
                                   l="wordbox_g.png", m="wordbox_u.png", n="wordbox_i.png", o="wordbox_w.png",
                                   p="wordbox_n.png", q="wordbox_v.png", r="wordbox_k.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_436_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=436,
                                   question="Who is the main antagonist in the movie Thor Love and Thunder",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_s.png", c="wordbox_p.png", d="wordbox_r.png", e="wordbox_q.png",
                                   f="wordbox_k.png",
                                   g="wordbox_k.png", h="wordbox_v.png", i="wordbox_g.png", j="wordbox_n.png",
                                   k="wordbox_t.png",
                                   l="wordbox_f.png", m="wordbox_m.png", n="wordbox_p.png", o="wordbox_j.png",
                                   p="wordbox_c.png", q="wordbox_f.png", r="wordbox_r.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_437_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=437,
                                   question="What is the name of the god that Gorr prays to for his daughter in Thor Love and Thunder",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox_r.png", c="wordbox_n.png", d="wordbox_q.png", e="wordbox_x.png",
                                   f="wordbox_v.png",
                                   g="wordbox_p.png", h="wordbox_k.png", i="wordbox_t.png", j="wordbox_l.png",
                                   k="wordbox_l.png",
                                   l="wordbox_u.png", m="wordbox_o.png", n="wordbox_b.png", o="wordbox_h.png",
                                   p="wordbox.png", q="wordbox_k.png", r="wordbox_g.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_438_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=438,
                                   question="Who was the first god killed by Gorr in Thor Love and Thunder",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox_r.png", c="wordbox_n.png", d="wordbox_q.png", e="wordbox_x.png",
                                   f="wordbox_v.png",
                                   g="wordbox_p.png", h="wordbox_k.png", i="wordbox_t.png", j="wordbox_l.png",
                                   k="wordbox_l.png",
                                   l="wordbox_u.png", m="wordbox_o.png", n="wordbox_b.png", o="wordbox_h.png",
                                   p="wordbox.png", q="wordbox_k.png", r="wordbox_g.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_439_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=439,
                                   question="Who takes the children of New Asgard as hostages in Thor Love and Thunder",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_s.png", c="wordbox_p.png", d="wordbox_r.png", e="wordbox_q.png",
                                   f="wordbox_k.png",
                                   g="wordbox_k.png", h="wordbox_v.png", i="wordbox_g.png", j="wordbox_n.png",
                                   k="wordbox_t.png",
                                   l="wordbox_f.png", m="wordbox_m.png", n="wordbox_p.png", o="wordbox_j.png",
                                   p="wordbox_c.png", q="wordbox_f.png", r="wordbox_r.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_440_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=440,
                                   question="Who makes the wish to Eternity to bring back the child in Thor Love and Thunder",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_s.png", c="wordbox_p.png", d="wordbox_r.png", e="wordbox_q.png",
                                   f="wordbox_k.png",
                                   g="wordbox_k.png", h="wordbox_v.png", i="wordbox_g.png", j="wordbox_n.png",
                                   k="wordbox_t.png",
                                   l="wordbox_f.png", m="wordbox_m.png", n="wordbox_p.png", o="wordbox_j.png",
                                   p="wordbox_c.png", q="wordbox_f.png", r="wordbox_r.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_441_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=441,
                                   question="Who takes care of Gorr the God Butcher's daughter in Thor Love and Thunder",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_f.png", c="wordbox_c.png", d="wordbox_o.png", e="wordbox_k.png",
                                   f="wordbox_d.png",
                                   g="wordbox_h.png", h="wordbox_l.png", i="wordbox_t.png", j="wordbox_p.png",
                                   k="wordbox_m.png",
                                   l="wordbox_l.png", m="wordbox_b.png", n="wordbox_m.png", o="wordbox_x.png",
                                   p="wordbox_j.png", q="wordbox.png", r="wordbox_r.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_442_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=442,
                                   question="What is the name of Gorr the God Butcher's daughter in Thor Love and Thunder",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_k.png", c="wordbox_p.png", d="wordbox_q.png", e="wordbox_t.png",
                                   f="wordbox_s.png",
                                   g="wordbox_m.png", h="wordbox_l.png", i="wordbox_k.png", j="wordbox_n.png",
                                   k="wordbox_b.png",
                                   l="wordbox_v.png", m="wordbox_e.png", n="wordbox_v.png", o="wordbox_c.png",
                                   p="wordbox_j.png", q="wordbox_q.png", r="wordbox_s.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_443_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=443,
                                   question="What is the name of Heimdall's son in Thor Love and Thunder",
                                   levelcounter=str(self.count), a="wordbox_q.png",
                                   b="wordbox_q.png", c="wordbox_x.png", d="wordbox_t.png", e="wordbox_p.png",
                                   f="wordbox_s.png",
                                   g="wordbox_s.png", h="wordbox_m.png", i="wordbox.png", j="wordbox_o.png",
                                   k="wordbox_n.png",
                                   l="wordbox_u.png", m="wordbox_b.png", n="wordbox_n.png", o="wordbox_l.png",
                                   p="wordbox_c.png", q="wordbox_g.png", r="wordbox_j.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_444_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=444,
                                   question="Who sends Hercules to kill Thor in Thor Love and Thunder",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_p.png", c="wordbox_v.png", d="wordbox_t.png", e="wordbox_k.png",
                                   f="wordbox_e.png",
                                   g="wordbox_z.png", h="wordbox_f.png", i="wordbox_l.png", j="wordbox_d.png",
                                   k="wordbox_u.png",
                                   l="wordbox_q.png", m="wordbox_n.png", n="wordbox_p.png", o="wordbox_s.png",
                                   p="wordbox_b.png", q="wordbox_o.png", r="wordbox_m.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_445_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=445,
                                   question="Who is the father of Hercules in Thor Love and Thunder",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_p.png", c="wordbox_v.png", d="wordbox_t.png", e="wordbox_k.png",
                                   f="wordbox_e.png",
                                   g="wordbox_z.png", h="wordbox_f.png", i="wordbox_l.png", j="wordbox_d.png",
                                   k="wordbox_u.png",
                                   l="wordbox_q.png", m="wordbox_n.png", n="wordbox_p.png", o="wordbox_s.png",
                                   p="wordbox_b.png", q="wordbox_o.png", r="wordbox_m.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_446_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=446,
                                   question="What is the name of the god with the Thunderbolt weapon in Thor Love and Thunder",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_p.png", c="wordbox_v.png", d="wordbox_t.png", e="wordbox_k.png",
                                   f="wordbox_e.png",
                                   g="wordbox_z.png", h="wordbox_f.png", i="wordbox_l.png", j="wordbox_d.png",
                                   k="wordbox_u.png",
                                   l="wordbox_q.png", m="wordbox_n.png", n="wordbox_p.png", o="wordbox_s.png",
                                   p="wordbox_b.png", q="wordbox_o.png", r="wordbox_m.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_447_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=447,
                                   question="What is the name of the sword used to kill the gods in Thor Love and Thunder",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_e.png", c="wordbox_j.png", d="wordbox_o.png", e="wordbox_q.png",
                                   f="wordbox_o.png",
                                   g="wordbox_n.png", h="wordbox_p.png", i="wordbox_s.png", j="wordbox_d.png",
                                   k="wordbox_r.png",
                                   l="wordbox_t.png", m="wordbox_r.png", n="wordbox_t.png", o="wordbox_c.png",
                                   p="wordbox_l.png", q="wordbox_k.png", r="wordbox_w.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_448_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=448,
                                   question="Who gave the Necrosword to Gorr",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_p.png", c="wordbox_q.png", d="wordbox_y.png", e="wordbox_x.png",
                                   f="wordbox_l.png",
                                   g="wordbox_u.png", h="wordbox_k.png", i="wordbox_m.png", j="wordbox_o.png",
                                   k="wordbox_p.png",
                                   l="wordbox_v.png", m="wordbox_s.png", n="wordbox_h.png", o="wordbox_g.png",
                                   p="wordbox_b.png", q="wordbox_t.png", r="wordbox_l.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_449_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=449,
                                   question="What is the key to the Forge of Eternity",
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
    def level_450_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=450,
                                   question="To which realm did Gorr take the children in Thor Love and Thunder",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_k.png", c="wordbox_o.png", d="wordbox_p.png", e="wordbox_j.png",
                                   f="wordbox_b.png",
                                   g="wordbox.png", h="wordbox_c.png", i="wordbox_s.png", j="wordbox_e.png",
                                   k="wordbox_d.png",
                                   l="wordbox_f.png", m="wordbox_f.png", n="wordbox_b.png", o="wordbox_w.png",
                                   p="wordbox_v.png", q="wordbox_m.png", r="wordbox_j.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_451_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=451,
                                   question="What is the name of the book that Strange is searching for with America Chavez in Doctor Strange in the Multiverse of Madness",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_j.png", c="wordbox_c.png", d="wordbox.png", e="wordbox_g.png",
                                   f="wordbox_i.png",
                                   g="wordbox_s.png", h="wordbox_v.png", i="wordbox_h.png", j="wordbox_q.png",
                                   k="wordbox_p.png",
                                   l="wordbox_k.png", m="wordbox_k.png", n="wordbox_o.png", o="wordbox_n.png",
                                   p="wordbox_l.png", q="wordbox_t.png", r="wordbox_g.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_452_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=452,
                                   question="According to the people in the movie No Way Home, who is believed to have killed Mysterio",
                                   levelcounter=str(self.count), a="wordbox_z.png",
                                   b="wordbox_i.png", c="wordbox.png", d="wordbox_u.png",
                                   e="wordbox_p.png", f="wordbox_y.png", g="wordbox_e.png",
                                   h="wordbox_v.png", i="wordbox_s.png", j="wordbox_t.png",
                                   k="wordbox_r.png", l="wordbox_o.png", m="wordbox_m.png",
                                   n="wordbox_b.png", o="wordbox_x.png", p="wordbox_d.png",
                                   q="wordbox_w.png", r="wordbox_n.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_453_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=453,
                                   question="Who reveals the identity of the SpiderMan",
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
    def level_454_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=454,
                                   question="What was Peter Parker's age in the SpiderMan No Way Home movie",
                                   levelcounter=str(self.count), a="num_0.png",
                                   b="num_9.png", c="num_3.png", d="num_7.png",
                                   e="num_1.png", f="num_2.png", g="num_4.png",
                                   h="num_8.png", i="num_8.png", j="num_4.png",
                                   k="num_0.png", l="num_6.png", m="num_6.png",
                                   n="num_2.png", o="num_9.png", p="num_5.png",
                                   q="num_5.png", r="num_3.png",

                                   em_1="bor.png", em_2="bor.png", em_3="mix.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_455_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=455,
                                   question="What is the name of Peter Parker's girlfriend in No Way home movie",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_p.png", c="wordbox_s.png", d="wordbox_l.png",
                                   e="wordbox_d.png", f="wordbox_m.png", g="wordbox_e.png",
                                   h="wordbox_h.png", i="wordbox_o.png", j="wordbox_b.png",
                                   k="wordbox_i.png", l="wordbox_j.png", m="wordbox_y.png",
                                   n="wordbox_c.png", o="wordbox_w.png", p="wordbox_e.png",
                                   q="wordbox_n.png", r="wordbox_e.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_456_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=456,
                                   question="Who is the lawyer for Peter Parker in the movie No Way Home",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_q.png", c="wordbox_c.png", d="wordbox_t.png",
                                   e="wordbox_u.png", f="wordbox_p.png", g="wordbox_k.png",
                                   h="wordbox_r.png", i="wordbox_m.png", j="wordbox_l.png",
                                   k="wordbox_n.png", l="wordbox_d.png", m="wordbox_m.png",
                                   n="wordbox_s.png", o="wordbox_o.png", p="wordbox_w.png",
                                   q="wordbox_t.png", r="wordbox_v.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def  level_457_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=457,
                                   question="Who is Peter Parker's guardian",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_u.png", c="wordbox_t.png", d="wordbox_r.png",
                                   e="wordbox_y.png", f="wordbox_o.png", g="wordbox.png",
                                   h="wordbox_s.png", i="wordbox_r.png", j="wordbox_m.png",
                                   k="wordbox_q.png", l="wordbox_l.png", m="wordbox_e.png",
                                   n="wordbox.png", o="wordbox_n.png", p="wordbox_w.png",
                                   q="wordbox_p.png", r="wordbox_z.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_458_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=458,
                                   question="In the movie Spider-Man No Way Home, with whom is Aunt May in a relationship",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox.png", c="wordbox_o.png", d="wordbox_k.png", e="wordbox_h.png",
                                   f="wordbox_d.png",
                                   g="wordbox_m.png", h="wordbox_h.png", i="wordbox_n.png", j="wordbox_y.png",
                                   k="wordbox_j.png",
                                   l="wordbox_s.png", m="wordbox_p.png", n="wordbox_g.png", o="wordbox_u.png",
                                   p="wordbox.png", q="wordbox_q.png", r="wordbox_p.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_459_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=459,
                                   question="What is the name of the character with eight mechanical arms in the SpiderMan No Way Home movie",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_c.png", c="wordbox_x.png", d="wordbox_u.png",
                                   e="wordbox_r.png", f="wordbox_z.png", g="wordbox_b.png",
                                   h="wordbox_o.png", i="wordbox_v.png", j="wordbox_t.png",
                                   k="wordbox_d.png", l="wordbox_o.png", m="wordbox_s.png",
                                   n="wordbox_o.png", o="wordbox_y.png", p="wordbox_c.png",
                                   q="wordbox_p.png", r="wordbox_t.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_460_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=460,
                                   question="What is the name of the villian who has the ability to control electricity in No Way Home Movie",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_h.png", c="wordbox_t.png", d="wordbox_g.png",
                                   e="wordbox_l.png", f="wordbox_k.png", g="wordbox_e.png",
                                   h="wordbox_d.png", i="wordbox_f.png", j="wordbox_e.png",
                                   k="wordbox_j.png", l="wordbox_q.png", m="wordbox_o.png",
                                   n="wordbox_n.png", o="wordbox_c.png", p="wordbox_m.png",
                                   q="wordbox_r.png", r="wordbox_i.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_461_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=461,
                                   question="In the movie No Way Home, what is the name of the villain with the ability to transform his body into a reptile-like form",
                                   levelcounter=str(self.count), a="wordbox_w.png",
                                   b="wordbox_i.png", c="wordbox_h.png", d="wordbox_c.png",
                                   e="wordbox_m.png", f="wordbox_b.png", g="wordbox_g.png",
                                   h="wordbox_j.png", i="wordbox_l.png", j="wordbox_e.png",
                                   k="wordbox_f.png", l="wordbox_r.png", m="wordbox_d.png",
                                   n="wordbox_p.png", o="wordbox_o.png", p="wordbox_z.png",
                                   q="wordbox_k.png", r="wordbox.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_462_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=462,
                                   question="In the movie No Way Home, what is the name of the villain who flies and wears a green colored suit",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_r.png", c="wordbox_t.png", d="wordbox_l.png",
                                   e="wordbox_z.png", f="wordbox_u.png", g="wordbox_v.png",
                                   h="wordbox_i.png", i="wordbox_y.png", j="wordbox_n.png",
                                   k="wordbox_g.png", l="wordbox_o.png", m="wordbox_w.png",
                                   n="wordbox_b.png", o="wordbox_e.png", p="wordbox_x.png",
                                   q="wordbox_n.png", r="wordbox_g.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_463_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=463,
                                   question="What is the name of the villian who has the ability to transfer his body to sand",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_g.png", c="wordbox_z.png", d="wordbox_c.png",
                                   e="wordbox_b.png", f="wordbox_n.png", g="wordbox_y.png",
                                   h="wordbox_f.png", i="wordbox_s.png", j="wordbox_e.png",
                                   k="wordbox_n.png", l="wordbox_t.png", m="wordbox.png",
                                   n="wordbox_h.png", o="wordbox_m.png", p="wordbox_x.png",
                                   q="wordbox_u.png", r="wordbox_d.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_464_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=464,
                                   question="What is the name of the actor who plays the role of SpiderMan in the 616 MCU",
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
    def level_465_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=465,
                                   question="What is the name of actor who plays the role of Spide-Man in amazing Spiderman movies",
                                   levelcounter=str(self.count), a="wordbox_d.png",
                                   b="wordbox.png", c="wordbox_m.png", d="wordbox.png",
                                   e="wordbox_x.png", f="wordbox_r.png", g="wordbox_e.png",
                                   h="wordbox_g.png", i="wordbox_f.png", j="wordbox_y.png",
                                   k="wordbox_w.png", l="wordbox_z.png", m="wordbox_e.png",
                                   n="wordbox_d.png", o="wordbox_n.png", p="wordbox_i.png",
                                   q="wordbox_r.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="bor.png", em_15="mix.png"

                                   )
    def level_466_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=466,
                                   question="Who helps Peter Parker to make the world forget his identity in SpiderMan No Way Home",
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
    def level_467_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=467,
                                   question="To which dimension does Doctor Strange takes SpiderMan in No Way Home movie",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_q.png", c="wordbox_p.png", d="wordbox_l.png", e="wordbox_n.png",
                                   f="wordbox_i.png",
                                   g="wordbox_k.png", h="wordbox_v.png", i="wordbox_r.png", j="wordbox_l.png",
                                   k="wordbox_f.png",
                                   l="wordbox_r.png", m="wordbox_c.png", n="wordbox_m.png", o="wordbox_s.png",
                                   p="wordbox_r.png", q="wordbox_t.png", r="wordbox_u.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_468_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=468,
                                   question="Who were killed by the Green Goblin in SpiderMan No Way Home",
                                   levelcounter=str(self.count),  a="wordbox_k.png",
                                   b="wordbox_u.png", c="wordbox_t.png", d="wordbox_r.png",
                                   e="wordbox_y.png", f="wordbox_o.png", g="wordbox.png",
                                   h="wordbox_s.png", i="wordbox_r.png", j="wordbox_m.png",
                                   k="wordbox_q.png", l="wordbox_l.png", m="wordbox_e.png",
                                   n="wordbox.png", o="wordbox_n.png", p="wordbox_w.png",
                                   q="wordbox_p.png", r="wordbox_z.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_469_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=469,
                                   question="Who traps Doctor Strange in the Mirror Dimension In No Way Home",
                                   levelcounter=str(self.count), a="wordbox_z.png",
                                   b="wordbox_i.png", c="wordbox.png", d="wordbox_u.png",
                                   e="wordbox_p.png", f="wordbox_y.png", g="wordbox_e.png",
                                   h="wordbox_v.png", i="wordbox_s.png", j="wordbox_t.png",
                                   k="wordbox_r.png", l="wordbox_o.png", m="wordbox_m.png",
                                   n="wordbox_b.png", o="wordbox_x.png", p="wordbox_d.png",
                                   q="wordbox_w.png", r="wordbox_n.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_470_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=470,
                                   question="What is the name of the spaceship that the Eternals arrive on Earth in the Eternals movie",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_h.png", c="wordbox_i.png", d="wordbox_c.png",
                                   e="wordbox_l.png", f="wordbox_o.png", g="wordbox_p.png",
                                   h="wordbox_n.png", i="wordbox_d.png", j="wordbox_g.png",
                                   k="wordbox.png", l="wordbox_f.png", m="wordbox_m.png",
                                   n="wordbox_k.png", o="wordbox_e.png", p="wordbox_b.png",
                                   q="wordbox_j.png", r="wordbox_o.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_471_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=471,
                                   question="Who is the creator of the Eternals",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_m.png", c="wordbox_i.png", d="wordbox_n.png",
                                   e="wordbox_l.png", f="wordbox_f.png", g="wordbox_s.png",
                                   h="wordbox_c.png", i="wordbox_g.png", j="wordbox_t.png",
                                   k="wordbox_k.png", l="wordbox_d.png", m="wordbox_b.png",
                                   n="wordbox_e.png", o="wordbox_h.png", p="wordbox_e.png",
                                   q="wordbox.png", r="wordbox_j.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_472_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=472,
                                   question="What is the name of the process of the birth of a new Celestials in the Eternals movie",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_n.png", c="wordbox_p.png", d="wordbox_r.png",
                                   e="wordbox_y.png", f="wordbox_e.png", g="wordbox_e.png",
                                   h="wordbox_z.png", i="wordbox_x.png", j="wordbox_q.png",
                                   k="wordbox_e.png", l="wordbox_o.png", m="wordbox_l.png",
                                   n="wordbox_m.png", o="wordbox_z.png", p="wordbox_g.png",
                                   q="wordbox_e.png", r="wordbox_c.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"
                                   )
    def level_473_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=473,
                                   question="Who is responsible for creating the Deviants in the Eternals movie",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_m.png", c="wordbox_i.png", d="wordbox_n.png",
                                   e="wordbox_l.png", f="wordbox_f.png", g="wordbox_s.png",
                                   h="wordbox_c.png", i="wordbox_g.png", j="wordbox_t.png",
                                   k="wordbox_k.png", l="wordbox_d.png", m="wordbox_b.png",
                                   n="wordbox_e.png", o="wordbox_h.png", p="wordbox_e.png",
                                   q="wordbox.png", r="wordbox_j.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_474_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=474,
                                   question="Who is the Prime Eternal in the Eternals movie",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_n.png", c="wordbox_v.png", d="wordbox_q.png",
                                   e="wordbox_y.png", f="wordbox_o.png", g="wordbox_u.png",
                                   h="wordbox_r.png", i="wordbox.png", j="wordbox_t.png",
                                   k="wordbox_x.png", l="wordbox_k.png", m="wordbox_m.png",
                                   n="wordbox_j.png", o="wordbox_p.png", p="wordbox_w.png",
                                   q="wordbox_s.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_475_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=475,
                                   question="On which B.C year did the Eternals arrive on Earth in the movie",
                                   levelcounter=str(self.count), a="num_1.png",
                                   b="num_1.png", c="num_8.png", d="num_4.png",
                                   e="num_7.png", f="num_9.png", g="num_0.png",
                                   h="num_2.png", i="num_2.png", j="num_5.png",
                                   k="num_8.png", l="num_3.png", m="num_6.png",
                                   n="num_7.png", o="num_0.png", p="num_4.png",
                                   q="num_9.png", r="num_0.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_476_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=476,
                                   question="Who is the leader of the Deviants in the Eternals movie",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_x.png", c="wordbox_q.png", d="wordbox_w.png",
                                   e="wordbox_y.png", f="wordbox_p.png", g="wordbox_b.png",
                                   h="wordbox_l.png", i="wordbox_k.png", j="wordbox_z.png",
                                   k="wordbox_p.png", l="wordbox_s.png", m="wordbox_u.png",
                                   n="wordbox_v.png", o="wordbox_n.png", p="wordbox_t.png",
                                   q="wordbox_m.png", r="wordbox_r.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_477_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=477,
                                   question="Who kills the Deviants leader in the Eternals movie",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_s.png", c="wordbox_g.png", d="wordbox_t.png",
                                   e="wordbox_u.png", f="wordbox_p.png", g="wordbox_n.png",
                                   h="wordbox_o.png", i="wordbox_r.png", j="wordbox_f.png",
                                   k="wordbox_e.png", l="wordbox_d.png", m="wordbox_c.png",
                                   n="wordbox_h.png", o="wordbox_v.png", p="wordbox_b.png",
                                   q="wordbox.png", r="wordbox_q.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_478_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=478,
                                   question="who takes the powers of all the other Eternals and stops the Emergence in Eternals movie",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_u.png", c="wordbox_l.png", d="wordbox_s.png",
                                   e="wordbox_n.png", f="wordbox_r.png", g="wordbox_x.png",
                                   h="wordbox_s.png", i="wordbox_q.png", j="wordbox_m.png",
                                   k="wordbox_p.png", l="wordbox_o.png", m="wordbox_i.png",
                                   n="wordbox_h.png", o="wordbox_v.png", p="wordbox_g.png",
                                   q="wordbox_e.png", r="wordbox_w.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_479_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=479,
                                   question="Who becomes the Prime Eternal after the death of Ajak in the movie Eternals",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_u.png", c="wordbox_l.png", d="wordbox_s.png",
                                   e="wordbox_n.png", f="wordbox_r.png", g="wordbox_x.png",
                                   h="wordbox_s.png", i="wordbox_q.png", j="wordbox_m.png",
                                   k="wordbox_p.png", l="wordbox_o.png", m="wordbox_i.png",
                                   n="wordbox_h.png", o="wordbox_v.png", p="wordbox_g.png",
                                   q="wordbox_e.png", r="wordbox_w.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_480_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=480,
                                   question="In the movie Eternals, who is Sersi's partner in the museum",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_s.png", c="wordbox_q.png", d="wordbox_n.png",
                                   e="wordbox_t.png", f="wordbox_o.png", g="wordbox_i.png",
                                   h="wordbox.png", i="wordbox_p.png", j="wordbox.png",
                                   k="wordbox_y.png", l="wordbox_n.png", m="wordbox_e.png",
                                   n="wordbox_x.png", o="wordbox_w.png", p="wordbox_d.png",
                                   q="wordbox_z.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_481_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=481,
                                   question="What is the name of the Eternal becomes a hero in Mumbai",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_r.png", c="wordbox_x.png", d="wordbox_l.png",
                                   e="wordbox_t.png", f="wordbox_o.png", g="wordbox_g.png",
                                   h="wordbox_y.png", i="wordbox_u.png", j="wordbox_w.png",
                                   k="wordbox_p.png", l="wordbox_k.png", m="wordbox_z.png",
                                   n="wordbox_q.png", o="wordbox_v.png", p="wordbox_n.png",
                                   q="wordbox_m.png", r="wordbox_s.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_482_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=482,
                                   question="In the movie Eternals, what is the name of Kingo's personal assistant",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_j.png", c="wordbox_l.png", d="wordbox.png",
                                   e="wordbox_b.png", f="wordbox_p.png", g="wordbox_h.png",
                                   h="wordbox_k.png", i="wordbox_f.png", j="wordbox_t.png",
                                   k="wordbox_c.png", l="wordbox_u.png", m="wordbox_i.png",
                                   n="wordbox_n.png", o="wordbox_g.png", p="wordbox_r.png",
                                   q="wordbox_d.png", r="wordbox_e.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_483_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=483,
                                   question="What is the name of the creatures that kills Gilgamesh in the Eternals movie",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_d.png", c="wordbox_t.png", d="wordbox_k.png",
                                   e="wordbox_e.png", f="wordbox_m.png", g="wordbox_v.png",
                                   h="wordbox_i.png", i="wordbox_g.png", j="wordbox_c.png",
                                   k="wordbox_f.png", l="wordbox.png", m="wordbox_s.png",
                                   n="wordbox_j.png", o="wordbox_d.png", p="wordbox_h.png",
                                   q="wordbox_n.png", r="wordbox_b.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_484_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=484,
                                   question="What is the name of the city where Sersi and Sprite lives in the movie",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_k.png", c="wordbox_t.png", d="wordbox_n.png", e="wordbox_q.png",
                                   f="wordbox_v.png",
                                   g="wordbox_t.png", h="wordbox_o.png", i="wordbox.png", j="wordbox_c.png",
                                   k="wordbox_h.png",
                                   l="wordbox_o.png", m="wordbox_v.png", n="wordbox_m.png", o="wordbox_c.png",
                                   p="wordbox_n.png", q="wordbox_k.png", r="wordbox_d.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_485_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=485,
                                   question="In the movie Eternals, what is the name of the Eternal who identifies as LGBTQ  character",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_e.png", c="wordbox_k.png", d="wordbox_f.png",
                                   e="wordbox_j.png", f="wordbox_o.png", g="wordbox_s.png",
                                   h="wordbox_g.png", i="wordbox_p.png", j="wordbox_s.png",
                                   k="wordbox_l.png", l="wordbox_d.png", m="wordbox_h.png",
                                   n="wordbox_m.png", o="wordbox_i.png", p="wordbox_c.png",
                                   q="wordbox.png", r="wordbox_b.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_486_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=486,
                                   question="What is the name of the Celestial in the movie",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_p.png", c="wordbox_r.png", d="wordbox_q.png",
                                   e="wordbox_z.png", f="wordbox_y.png", g="wordbox_h.png",
                                   h="wordbox_t.png", i="wordbox_s.png", j="wordbox_v.png",
                                   k="wordbox_w.png", l="wordbox_o.png", m="wordbox_u.png",
                                   n="wordbox.png", o="wordbox_n.png", p="wordbox_e.png",
                                   q="wordbox_x.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_487_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=487,
                                   question="What is the name of the Eternal with superhuman speed",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_b.png", c="wordbox_l.png", d="wordbox_f.png",
                                   e="wordbox_i.png", f="wordbox_o.png", g="wordbox_e.png",
                                   h="wordbox_k.png", i="wordbox_g.png", j="wordbox_c.png",
                                   k="wordbox_k.png", l="wordbox_j.png", m="wordbox.png",
                                   n="wordbox_n.png", o="wordbox_h.png", p="wordbox_m.png",
                                   q="wordbox_d.png", r="wordbox_r.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_488_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=488,
                                   question="What is the name of the Eternal with the ability to control the human minds",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_c.png", c="wordbox_n.png", d="wordbox_d.png",
                                   e="wordbox_j.png", f="wordbox_p.png", g="wordbox_i.png",
                                   h="wordbox_l.png", i="wordbox_h.png", j="wordbox_u.png",
                                   k="wordbox_e.png", l="wordbox_k.png", m="wordbox_o.png",
                                   n="wordbox_q.png", o="wordbox_r.png", p="wordbox_m.png",
                                   q="wordbox_g.png", r="wordbox_f.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_489_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=489,
                                   question="Who assists Zemo in his escape from jail in the Falcon and The Winter Soldier",
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
    def level_490_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=490,
                                   question="Who is responsible for the death of Dr.Nagel in the Falcon and The Winter Soldier",
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
    def level_491_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=491,
                                   question="Whom do the Wakandan soldiers take in to custody in Falcon and The Winter Soldier",
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
    def level_492_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=492,
                                   question="Who is responsible for the death of Selby in the Falcon and The Winter Soldier",
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
    def level_493_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=493,
                                   question="Who is revealed to be the Power Broker in the Falcon and The Winter Soldier series",
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


    def level_494_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=494,
                                   question="Whom do Bucky Barnes and Sam Wilson meet in jail in the Falcon and The Winter Soldier",
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
    def level_495_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=495,
                                   question="Who takes up the mantle of Captain America in the Falcon and The Winter Soldier",
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
    def level_496_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=496,
                                   question="What is the name of Sam Wilson's sister",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_g.png", c="wordbox_f.png", d="wordbox.png", e="wordbox_j.png",
                                   f="wordbox_n.png",
                                   g="wordbox_i.png", h="wordbox.png", i="wordbox_o.png", j="wordbox_l.png",
                                   k="wordbox_e.png",
                                   l="wordbox_k.png", m="wordbox_q.png", n="wordbox_p.png", o="wordbox_m.png",
                                   p="wordbox_s.png", q="wordbox_t.png", r="wordbox_h.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_497_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=497,
                                   question="Who hands over the shield to the government in the Falcon and The Winter Soldier",
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
    def level_498_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=498,
                                   question="Who is announced as the new Captain America by the government in the Falcon and The Winter Soldier",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_t.png", c="wordbox_k.png", d="wordbox_x.png", e="wordbox.png",
                                   f="wordbox_q.png",
                                   g="wordbox_h.png", h="wordbox_z.png", i="wordbox_j.png", j="wordbox_v.png",
                                   k="wordbox_e.png",
                                   l="wordbox_o.png", m="wordbox_r.png", n="wordbox_w.png", o="wordbox_u.png",
                                   p="wordbox_y.png", q="wordbox_l.png", r="wordbox_p.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_499_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=499,
                                   question="Whom does John Walker, the new Captain America, kill in the Falcon and The Winter Soldier",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_p.png", c="wordbox_i.png", d="wordbox_y.png", e="wordbox_t.png",
                                   f="wordbox_s.png",
                                   g="wordbox_s.png", h="wordbox_u.png", i="wordbox_n.png", j="wordbox_m.png",
                                   k="wordbox_p.png",
                                   l="wordbox_x.png", m="wordbox_c.png", n="wordbox_l.png", o="wordbox_t.png",
                                   p="wordbox_g.png", q="wordbox_h.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_500_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=500,
                                   question="Which gang does Nico belong to in the Falcon and The Winter Soldier",
                                   levelcounter=str(self.count), a="wordbox_w.png",
                                   b="wordbox_l.png", c="wordbox_k.png", d="wordbox_s.png", e="wordbox_o.png",
                                   f="wordbox_h.png",
                                   g="wordbox_m.png", h="wordbox_s.png", i="wordbox_z.png", j="wordbox_f.png",
                                   k="wordbox_r.png",
                                   l="wordbox_g.png", m="wordbox_s.png", n="wordbox.png", o="wordbox_x.png",
                                   p="wordbox_e.png", q="wordbox_y.png", r="wordbox.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_501_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=501,
                                   question="What is the superhero alias adopted by Lemar Hoskins in the Falcon and The Winter Soldier",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_f.png", c="wordbox_t.png", d="wordbox_t.png", e="wordbox_q.png",
                                   f="wordbox.png",
                                   g="wordbox_s.png", h="wordbox_n.png", i="wordbox_b.png", j="wordbox_r.png",
                                   k="wordbox_h.png",
                                   l="wordbox_t.png", m="wordbox_f.png", n="wordbox_l.png", o="wordbox_j.png",
                                   p="wordbox_e.png", q="wordbox_d.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_502_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=502,
                                   question="What is the name of the activist group in the Falcon and The Winter Soldier",
                                   levelcounter=str(self.count), a="wordbox_w.png",
                                   b="wordbox_l.png", c="wordbox_k.png", d="wordbox_s.png", e="wordbox_o.png",
                                   f="wordbox_h.png",
                                   g="wordbox_m.png", h="wordbox_s.png", i="wordbox_z.png", j="wordbox_f.png",
                                   k="wordbox_r.png",
                                   l="wordbox_g.png", m="wordbox_s.png", n="wordbox.png", o="wordbox_x.png",
                                   p="wordbox_e.png", q="wordbox_y.png", r="wordbox.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_503_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=503,
                                   question="What is the name of the new king of Wakanda in the movie Black Panther Wakanda Forever",
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
    def level_504_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=504,
                                   question="who rescued both shuri and Riri Williams from the talokan cit in Wakanda Forever",
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
    def level_505_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=505,
                                   question="who created the artificial heart shaped hearb in wakanda fowerever",
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
    def level_506_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=506,
                                   question="With whom did the shuri goes to meet iron heart in the wakanda forever",
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
    def level_507_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=507,
                                   question="Whom did the shuri saw after taking the heart shaped hearb in Wakanda Forever",
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
    def level_508_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=508,
                                   question="Whose wedding did Strange attend in the Multiverse of Madness movie",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_x.png", c="wordbox_t.png", d="wordbox_m.png",
                                   e="wordbox_i.png", f="wordbox_l.png", g="wordbox_i.png",
                                   h="wordbox_q.png", i="wordbox_c.png", j="wordbox_r.png",
                                   k="wordbox_y.png", l="wordbox_e.png", m="wordbox_r.png",
                                   n="wordbox_e.png", o="wordbox_s.png", p="wordbox_n.png",
                                   q="wordbox.png", r="wordbox_h.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="bor.png", em_15="bor.png"

                                   )
    def level_509_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=509,
                                   question="What is the name of the monster that Wanda sents to attacks America Chavez in the Madness movie ",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_v.png", c="wordbox_w.png", d="wordbox_r.png",
                                   e="wordbox_l.png", f="wordbox_r.png", g="wordbox_g.png",
                                   h="wordbox_q.png", i="wordbox_g.png", j="wordbox_u.png",
                                   k="wordbox_o.png", l="wordbox.png", m="wordbox.png",
                                   n="wordbox_s.png", o="wordbox_p.png", p="wordbox_m.png",
                                   q="wordbox_n.png", r="wordbox_x.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_510_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=510,
                                   question="What is the name of the superhero has the ability to create starshaped portals that allow her to travel through the multiverse",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_q.png", c="wordbox_h.png", d="wordbox_l.png",
                                   e="wordbox_e.png", f="wordbox_r.png", g="wordbox_v.png",
                                   h="wordbox_w.png", i="wordbox.png", j="wordbox_y.png",
                                   k="wordbox_c.png", l="wordbox.png", m="wordbox_m.png",
                                   n="wordbox_c.png", o="wordbox_x.png", p="wordbox.png",
                                   q="wordbox_z.png", r="wordbox_i.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_511_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=511,
                                   question="What is the name of the magic on the walls of Mount Wundagore",
                                   levelcounter=str(self.count), a="wordbox_d.png",
                                   b="wordbox_l.png", c="wordbox_t.png", d="wordbox_q.png",
                                   e="wordbox_e.png", f="wordbox_o.png", g="wordbox_h.png",
                                   h="wordbox_p.png", i="wordbox_j.png", j="wordbox_n.png",
                                   k="wordbox_f.png", l="wordbox_k.png", m="wordbox_m.png",
                                   n="wordbox_g.png", o="wordbox_i.png", p="wordbox_h.png",
                                   q="wordbox_c.png", r="wordbox_b.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_512_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=512,
                                   question="what is the name of the superhero in the illuminati group in 838 who is mastery of mechanical,aerospace and electrical engineering",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_s.png", c="wordbox_z.png", d="wordbox_h.png",
                                   e="wordbox_y.png", f="wordbox_r.png", g="wordbox_r.png",
                                   h="wordbox_p.png", i="wordbox_c.png", j="wordbox_o.png",
                                   k="wordbox_e.png", l="wordbox_q.png", m="wordbox.png",
                                   n="wordbox_e.png", o="wordbox_r.png", p="wordbox_x.png",
                                   q="wordbox_d.png", r="wordbox_d.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_513_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=513,
                                   question="Who is the head of the illuminati group in Multiverse of madness movie",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_w.png", c="wordbox_r.png", d="wordbox_n.png",
                                   e="wordbox_x.png", f="wordbox_e.png", g="wordbox_z.png",
                                   h="wordbox_h.png", i="wordbox_v.png", j="wordbox.png",
                                   k="wordbox_m.png", l="wordbox_e.png", m="wordbox_s.png",
                                   n="wordbox_r.png", o="wordbox.png", p="wordbox_c.png",
                                   q="wordbox_y.png", r="wordbox_i.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_514_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=514,
                                   question="Who Destroyes the Darkhold book in the Madness movie",
                                   levelcounter=str(self.count),  a="wordbox_r.png",
                                   b="wordbox_g.png", c="wordbox_h.png", d="wordbox_t.png",
                                   e="wordbox_i.png", f="wordbox_o.png", g="wordbox.png",
                                   h="wordbox_g.png", i="wordbox_w.png", j="wordbox_r.png",
                                   k="wordbox_e.png", l="wordbox_t.png", m="wordbox_j.png",
                                   n="wordbox.png", o="wordbox_s.png", p="wordbox_n.png",
                                   q="wordbox_f.png", r="wordbox_d.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )

    def level_515_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=515,
                                   question="Who kills the entire Illuminati group in the 838 universe",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_g.png", c="wordbox_h.png", d="wordbox_t.png",
                                   e="wordbox_i.png", f="wordbox_o.png", g="wordbox.png",
                                   h="wordbox_g.png", i="wordbox_w.png", j="wordbox_r.png",
                                   k="wordbox_e.png", l="wordbox_t.png", m="wordbox_j.png",
                                   n="wordbox.png", o="wordbox_s.png", p="wordbox_n.png",
                                   q="wordbox_f.png", r="wordbox_d.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_516_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=516,
                                   question="Who is the Sorcerer Supreme in the 838 universe in the Madness movie",
                                   levelcounter=str(self.count), a="wordbox_y.png",
                                   b="wordbox_o.png", c="wordbox_i.png", d="wordbox_c.png",
                                   e="wordbox_h.png", f="wordbox_z.png", g="wordbox_o.png",
                                   h="wordbox_b.png", i="wordbox_g.png", j="wordbox_m.png",
                                   k="wordbox_d.png", l="wordbox_e.png", m="wordbox_k.png",
                                   n="wordbox_l.png", o="wordbox_r.png", p="wordbox_j.png",
                                   q="wordbox_f.png", r="wordbox_x.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_517_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=517,
                                   question="Who performed a dreamwalk from the 838 universe to the 616 universe in the Multiverse of Madness movie",
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
    def level_518_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=518,
                                   question="Who performed a dreamwalk from the 616 universe to the 838 universe in the Multiverse of Madness movie",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_g.png", c="wordbox_h.png", d="wordbox_t.png",
                                   e="wordbox_i.png", f="wordbox_o.png", g="wordbox.png",
                                   h="wordbox_g.png", i="wordbox_w.png", j="wordbox_r.png",
                                   k="wordbox_e.png", l="wordbox_t.png", m="wordbox_j.png",
                                   n="wordbox.png", o="wordbox_s.png", p="wordbox_n.png",
                                   q="wordbox_f.png", r="wordbox_d.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_519_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=519,
                                   question="Who works as a scientist in the Illuminati 838 universe lab in the Madness movie",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_x.png", c="wordbox_t.png", d="wordbox_m.png",
                                   e="wordbox_i.png", f="wordbox_l.png", g="wordbox_i.png",
                                   h="wordbox_q.png", i="wordbox_c.png", j="wordbox_r.png",
                                   k="wordbox_y.png", l="wordbox_e.png", m="wordbox_r.png",
                                   n="wordbox_e.png", o="wordbox_s.png", p="wordbox_n.png",
                                   q="wordbox.png", r="wordbox_h.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="bor.png", em_15="bor.png"

                                   )
    def level_520_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=520,
                                   question="Who is Captain America in the 838 univers",
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
    def level_521_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=521,
                                   question="What is the name of the universe in which Chavez and Strange encounter the Illuminati group in the  Multiverde of Madness",
                                   levelcounter=str(self.count), a="num_1.png",
                                   b="num_6.png", c="num_4.png", d="num_9.png",
                                   e="num_3.png", f="num_0.png", g="num_5.png",
                                   h="num_2.png", i="num_7.png", j="num_2.png",
                                   k="num_7.png", l="num_4.png", m="num_0.png",
                                   n="num_6.png", o="num_8.png", p="num_5.png",
                                   q="num_8.png", r="num_1.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_522_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=522,
                                   question="What is the name of the book from which Wanda obtains her DarkMagic in the Mukriverse of Madness",
                                   levelcounter=str(self.count), a="wordbox_d.png",
                                   b="wordbox_p.png", c="wordbox_o.png", d="wordbox_q.png",
                                   e="wordbox_v.png", f="wordbox_d.png", g="wordbox_l.png",
                                   h="wordbox_n.png", i="wordbox.png", j="wordbox_r.png",
                                   k="wordbox_m.png", l="wordbox_f.png", m="wordbox_k.png",
                                   n="wordbox_f.png", o="wordbox_m.png", p="wordbox_j.png",
                                   q="wordbox_f.png", r="wordbox_h.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_523_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=523,
                                   question="Name of the king for talokan city in the wakanda forever movie",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_p.png", c="wordbox_q.png", d="wordbox_o.png",
                                   e="wordbox_l.png", f="wordbox_s.png", g="wordbox_s.png",
                                   h="wordbox_p.png", i="wordbox_t.png", j="wordbox_c.png",
                                   k="wordbox_x.png", l="wordbox_m.png", m="wordbox_b.png",
                                   n="wordbox_n.png", o="wordbox_g.png", p="wordbox_r.png",
                                   q="wordbox_h.png", r="wordbox_j.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_524_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=524,
                                   question="Who is responsible for attacking Wakanda in the Wakanda Forever",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_p.png", c="wordbox_q.png", d="wordbox_o.png",
                                   e="wordbox_l.png", f="wordbox_s.png", g="wordbox_s.png",
                                   h="wordbox_p.png", i="wordbox_t.png", j="wordbox_c.png",
                                   k="wordbox_x.png", l="wordbox_m.png", m="wordbox_b.png",
                                   n="wordbox_n.png", o="wordbox_g.png", p="wordbox_r.png",
                                   q="wordbox_h.png", r="wordbox_j.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_525_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=525,
                                   question="what is the name of the namor's cousin",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_p.png", c="wordbox_q.png", d="wordbox_o.png",
                                   e="wordbox_l.png", f="wordbox.png", g="wordbox_s.png",
                                   h="wordbox_p.png", i="wordbox_t.png", j="wordbox_c.png",
                                   k="wordbox_x.png", l="wordbox_m.png", m="wordbox_b.png",
                                   n="wordbox_n.png", o="wordbox_g.png", p="wordbox_r.png",
                                   q="wordbox_h.png", r="wordbox_j.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_526_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=526,
                                   question="what is the name of the island that Nakia lives in the wakanda forever movie",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_f.png", c="wordbox_q.png", d="wordbox_v.png",
                                   e="wordbox_i.png", f="wordbox_k.png", g="wordbox_p.png",
                                   h="wordbox_c.png", i="wordbox_h.png", j="wordbox_u.png",
                                   k="wordbox_t.png", l="wordbox_n.png", m="wordbox_k.png",
                                   n="wordbox_j.png", o="wordbox_m.png", p="wordbox_i.png",
                                   q="wordbox_o.png", r="wordbox_p.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_527_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=527,
                                   question="what is the name of the city under water in the wakanda forever movie",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox.png", c="wordbox_q.png", d="wordbox_s.png",
                                   e="wordbox_u.png", f="wordbox_n.png", g="wordbox_o.png",
                                   h="wordbox_u.png", i="wordbox_j.png", j="wordbox_t.png",
                                   k="wordbox_v.png", l="wordbox_l.png", m="wordbox_b.png",
                                   n="wordbox.png", o="wordbox_j.png", p="wordbox_i.png",
                                   q="wordbox_k.png", r="wordbox_h.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_528_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=528,
                                   question="What are the people of Talokan called in the Wakanda forever movie",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_q.png", c="wordbox_i.png", d="wordbox_p.png",
                                   e="wordbox_j.png", f="wordbox_f.png", g="wordbox_o.png",
                                   h="wordbox_n.png", i="wordbox_v.png", j="wordbox.png",
                                   k="wordbox_s.png", l="wordbox_k.png", m="wordbox_t.png",
                                   n="wordbox_f.png", o="wordbox_u.png", p="wordbox_e.png",
                                   q="wordbox_m.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_529_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=529,
                                   question="In which ocean is the city of Wakanda located",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_k.png", c="wordbox_n.png", d="wordbox_f.png",
                                   e="wordbox_t.png", f="wordbox_p.png", g="wordbox_s.png",
                                   h="wordbox.png", i="wordbox_p.png", j="wordbox.png",
                                   k="wordbox_m.png", l="wordbox_i.png", m="wordbox_c.png",
                                   n="wordbox_k.png", o="wordbox_u.png", p="wordbox_t.png",
                                   q="wordbox_h.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_530_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=530,
                                   question="What is the name of the Tchalla's son",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_q.png", c="wordbox_v.png", d="wordbox_i.png",
                                   e="wordbox_m.png", f="wordbox_n.png", g="wordbox_s.png",
                                   h="wordbox_p.png", i="wordbox_o.png", j="wordbox_c.png",
                                   k="wordbox_s.png", l="wordbox_h.png", m="wordbox_j.png",
                                   n="wordbox_t.png", o="wordbox_g.png", p="wordbox_u.png",
                                   q="wordbox_k.png", r="wordbox.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_531_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=531,
                                   question="By which authority was Loki arrested in the series",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_p.png", c="wordbox_q.png", d="wordbox_t.png",
                                   e="wordbox_u.png", f="wordbox_q.png", g="wordbox_m.png",
                                   h="wordbox.png", i="wordbox_f.png", j="wordbox_v.png",
                                   k="wordbox_l.png", l="wordbox_g.png", m="wordbox_j.png",
                                   n="wordbox_s.png", o="wordbox_x.png", p="wordbox_b.png",
                                   q="wordbox_h.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_532_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=532,
                                   question="In which year does Loki use the Tesseract to escape from the authority of S.H.I.E.L.D",
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
    def level_533_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=533,
                                   question="What is the name of the desert that Loki travels through using the Tesseract in the Loki series",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_k.png", c="wordbox_p.png", d="wordbox_q.png",
                                   e="wordbox_v.png", f="wordbox_c.png", g="wordbox_t.png",
                                   h="wordbox_p.png", i="wordbox_g.png", j="wordbox_m.png",
                                   k="wordbox_s.png", l="wordbox_i.png", m="wordbox_p.png",
                                   n="wordbox_q.png", o="wordbox_d.png", p="wordbox_h.png",
                                   q="wordbox_b.png", r="wordbox_v.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_534_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=534,
                                   question="Who is responsible for handling the Loki case in the TVA",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_v.png", c="wordbox_b.png", d="wordbox_k.png",
                                   e="wordbox_p.png", f="wordbox_s.png", g="wordbox_g.png",
                                   h="wordbox_m.png", i="wordbox_n.png", j="wordbox_o.png",
                                   k="wordbox_h.png", l="wordbox_v.png", m="wordbox_q.png",
                                   n="wordbox_p.png", o="wordbox_i.png", p="wordbox_j.png",
                                   q="wordbox_c.png", r="wordbox_u.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_535_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=535,
                                   question="What is the name of the female Loki variant in the series Loki",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_k.png", c="wordbox_p.png", d="wordbox_t.png",
                                   e="wordbox_k.png", f="wordbox_y.png", g="wordbox_m.png",
                                   h="wordbox_o.png", i="wordbox_s.png", j="wordbox_n.png",
                                   k="wordbox_l.png", l="wordbox_f.png", m="wordbox_u.png",
                                   n="wordbox_b.png", o="wordbox_v.png", p="wordbox_c.png",
                                   q="wordbox_h.png", r="wordbox_e.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_536_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=536,
                                   question="Who kills He Who Remains in the Loki series",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_k.png", c="wordbox_p.png", d="wordbox_t.png",
                                   e="wordbox_k.png", f="wordbox_y.png", g="wordbox_m.png",
                                   h="wordbox_o.png", i="wordbox_s.png", j="wordbox_n.png",
                                   k="wordbox_l.png", l="wordbox_f.png", m="wordbox_u.png",
                                   n="wordbox_b.png", o="wordbox_v.png", p="wordbox_c.png",
                                   q="wordbox_h.png", r="wordbox_e.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_537_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=537,
                                   question="What is the name of the device used to create the time doors in the Loki series",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_k.png", c="wordbox_l.png", d="wordbox_o.png",
                                   e="wordbox_d.png", f="wordbox_v.png", g="wordbox_c.png",
                                   h="wordbox_t.png", i="wordbox_k.png", j="wordbox_e.png",
                                   k="wordbox_q.png", l="wordbox_h.png", m="wordbox.png",
                                   n="wordbox_g.png", o="wordbox_h.png", p="wordbox_s.png",
                                   q="wordbox_v.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_538_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=538,
                                   question="Who is responsible for pruning Mobius in the Loki series",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_p.png", c="wordbox_r.png", d="wordbox_k.png",
                                   e="wordbox_s.png", f="wordbox_m.png", g="wordbox_s.png",
                                   h="wordbox_n.png", i="wordbox_l.png", j="wordbox.png",
                                   k="wordbox_f.png", l="wordbox_o.png", m="wordbox_v.png",
                                   n="wordbox_u.png", o="wordbox_q.png", p="wordbox_h.png",
                                   q="wordbox_g.png", r="wordbox_n.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_539_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=539,
                                   question="Where are people sent when they are pruned in the Loki series",
                                   levelcounter=str(self.count), a="wordbox_q.png",
                                   b="wordbox_t.png", c="wordbox_o.png", d="wordbox_n.png",
                                   e="wordbox_u.png", f="wordbox_s.png", g="wordbox_d.png",
                                   h="wordbox_s.png", i="wordbox_k.png", j="wordbox_p.png",
                                   k="wordbox_i.png", l="wordbox_t.png", m="wordbox_n.png",
                                   n="wordbox_v.png", o="wordbox_b.png", p="wordbox_k.png",
                                   q="wordbox_j.png", r="wordbox_s.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_540_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=540,
                                   question="Who is the judge in the TVA in the Loki series",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_p.png", c="wordbox_r.png", d="wordbox_k.png",
                                   e="wordbox_s.png", f="wordbox_m.png", g="wordbox_s.png",
                                   h="wordbox_n.png", i="wordbox_l.png", j="wordbox.png",
                                   k="wordbox_f.png", l="wordbox_o.png", m="wordbox_v.png",
                                   n="wordbox_u.png", o="wordbox_q.png", p="wordbox_h.png",
                                   q="wordbox_g.png", r="wordbox_n.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_541_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=541,
                                   question="Who helps Sylvie and Loki to escape from the dark monster in the Void in the Loki series",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_v.png", c="wordbox_b.png", d="wordbox_k.png",
                                   e="wordbox_p.png", f="wordbox_s.png", g="wordbox_g.png",
                                   h="wordbox_m.png", i="wordbox_n.png", j="wordbox_o.png",
                                   k="wordbox_h.png", l="wordbox_v.png", m="wordbox_q.png",
                                   n="wordbox_p.png", o="wordbox_i.png", p="wordbox_j.png",
                                   q="wordbox_c.png", r="wordbox_u.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_542_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=542,
                                   question="Who inflicts harm on Loki in the time loop in the Loki series",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_k.png", c="wordbox_p.png", d="wordbox_l.png",
                                   e="wordbox_l.png", f="wordbox_f.png", g="wordbox_n.png",
                                   h="wordbox_q.png", i="wordbox_s.png", j="wordbox_v.png",
                                   k="wordbox_w.png", l="wordbox_m.png", m="wordbox_p.png",
                                   n="wordbox_t.png", o="wordbox_v.png", p="wordbox_j.png",
                                   q="wordbox_b.png", r="wordbox_f.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_543_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=543,
                                   question="What is the name of the dark monster that resides in the Void in the Loki series",
                                   levelcounter=str(self.count), a="wordbox_f.png",
                                   b="wordbox_k.png", c="wordbox_s.png", d="wordbox_i.png",
                                   e="wordbox_p.png", f="wordbox_p.png", g="wordbox_h.png",
                                   h="wordbox_c.png", i="wordbox.png", j="wordbox_m.png",
                                   k="wordbox_n.png", l="wordbox_l.png", m="wordbox_x.png",
                                   n="wordbox_s.png", o="wordbox_q.png", p="wordbox_o.png",
                                   q="wordbox_j.png", r="wordbox_t.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_544_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=544,
                                   question="Who is chosen as the avatar of the Khonshu god in the Moon Knight series",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_s.png", c="wordbox_l.png", d="wordbox_t.png",
                                   e="wordbox_y.png", f="wordbox_p.png", g="wordbox.png",
                                   h="wordbox_q.png", i="wordbox_z.png", j="wordbox_c.png",
                                   k="wordbox_m.png", l="wordbox_r.png", m="wordbox_n.png",
                                   n="wordbox_e.png", o="wordbox_c.png", p="wordbox_b.png",
                                   q="wordbox_x.png", r="wordbox_r.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_545_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=545,
                                   question="What is the name of Marc Spector's mother",
                                   levelcounter=str(self.count), a="wordbox_d.png",
                                   b="wordbox_z.png", c="wordbox_o.png", d="wordbox_e.png",
                                   e="wordbox_m.png", f="wordbox_y.png", g="wordbox_t.png",
                                   h="wordbox_v.png", i="wordbox_e.png", j="wordbox_c.png",
                                   k="wordbox_p.png", l="wordbox_r.png", m="wordbox_s.png",
                                   n="wordbox_u.png", o="wordbox_q.png", p="wordbox_n.png",
                                   q="wordbox_l.png", r="wordbox_w.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_546_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=546,
                                   question="What is the name of Marc Spector's brother",
                                   levelcounter=str(self.count), a="wordbox_w.png",
                                   b="wordbox_l.png", c="wordbox_o.png", d="wordbox_x.png",
                                   e="wordbox_t.png", f="wordbox_p.png", g="wordbox.png",
                                   h="wordbox_z.png", i="wordbox_s.png", j="wordbox_d.png",
                                   k="wordbox_u.png", l="wordbox_r.png", m="wordbox.png",
                                   n="wordbox_v.png", o="wordbox_n.png", p="wordbox_q.png",
                                   q="wordbox_y.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_547_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=547,
                                   question="Who was the avatar of Khonshu before Marc Spector in the Moon Knight series",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_o.png", c="wordbox_q.png", d="wordbox_r.png",
                                   e="wordbox_n.png", f="wordbox_y.png", g="wordbox_r.png",
                                   h="wordbox_u.png", i="wordbox_w.png", j="wordbox.png",
                                   k="wordbox_x.png", l="wordbox_r.png", m="wordbox.png",
                                   n="wordbox_z.png", o="wordbox_h.png", p="wordbox_b.png",
                                   q="wordbox_h.png", r="wordbox_r.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_548_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=548,
                                   question="Whom does the Ammit goddess selsect as her avatar in the Moon Knight series",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_o.png", c="wordbox_q.png", d="wordbox_r.png",
                                   e="wordbox_n.png", f="wordbox_y.png", g="wordbox_r.png",
                                   h="wordbox_u.png", i="wordbox_w.png", j="wordbox.png",
                                   k="wordbox_x.png", l="wordbox_r.png", m="wordbox.png",
                                   n="wordbox_z.png", o="wordbox_h.png", p="wordbox_b.png",
                                   q="wordbox_h.png", r="wordbox_r.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_549_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=549,
                                   question="Whom does the Taweret goddess select as her avatar in the Moon Knight series",
                                   levelcounter=str(self.count), a="wordbox_c.png",
                                   b="wordbox_b.png", c="wordbox_o.png", d="wordbox_g.png",
                                   e="wordbox_y.png", f="wordbox_k.png", g="wordbox_l.png",
                                   h="wordbox_h.png", i="wordbox_j.png", j="wordbox.png",
                                   k="wordbox_f.png", l="wordbox_d.png", m="wordbox_n.png",
                                   n="wordbox_e.png", o="wordbox_m.png", p="wordbox_i.png",
                                   q="wordbox_l.png", r="wordbox.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_550_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=550,
                                   question="Who killed Arthur Harrow in the Moon Knight series",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_b.png", c="wordbox_l.png", d="wordbox_n.png",
                                   e="wordbox_o.png", f="wordbox_k.png", g="wordbox_d.png",
                                   h="wordbox_c.png", i="wordbox_q.png", j="wordbox_j.png",
                                   k="wordbox_p.png", l="wordbox_k.png", m="wordbox.png",
                                   n="wordbox_f.png", o="wordbox_e.png", p="wordbox_m.png",
                                   q="wordbox_c.png", r="wordbox_y.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_551_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=551,
                                   question="What is the name of Marc Spector's wife in the Moon Knight series",
                                   levelcounter=str(self.count), a="wordbox_c.png",
                                   b="wordbox_b.png", c="wordbox_o.png", d="wordbox_g.png",
                                   e="wordbox_y.png", f="wordbox_k.png", g="wordbox_l.png",
                                   h="wordbox_h.png", i="wordbox_j.png", j="wordbox.png",
                                   k="wordbox_f.png", l="wordbox_d.png", m="wordbox_n.png",
                                   n="wordbox_e.png", o="wordbox_m.png", p="wordbox_i.png",
                                   q="wordbox_l.png", r="wordbox.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_552_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=552,
                                   question="What is Marc Spector's locker number in the Moon Knight series",
                                   levelcounter=str(self.count), a="num_1.png",
                                   b="num_0.png", c="num_7.png", d="num_9.png",
                                   e="num_6.png", f="num_2.png", g="num_3.png",
                                   h="num_0.png", i="num.png", j="num_4.png",
                                   k="num_5.png", l="num.png", m="num_9.png",
                                   n="num_5.png", o="num_8.png", p="num_2.png",
                                   q="num_7.png", r="num_1.png",

                                   em_1="bor.png", em_2="bor.png", em_3="mix.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_553_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=553,
                                   question="Who works at the National Art Gallery in the Moon Knight series",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_l.png", c="wordbox_y.png", d="wordbox_t.png",
                                   e="wordbox_z.png", f="wordbox_n.png", g="wordbox_w.png",
                                   h="wordbox_s.png", i="wordbox_q.png", j="wordbox_g.png",
                                   k="wordbox_t.png", l="wordbox_e.png", m="wordbox.png",
                                   n="wordbox_n.png", o="wordbox_m.png", p="wordbox_v.png",
                                   q="wordbox_x.png", r="wordbox_r.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_554_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=554,
                                   question="What is the name of the Egyptian goddess who resembles a hippopotamus in the Moon Knight series",
                                   levelcounter=str(self.count), a="wordbox_q.png",
                                   b="wordbox_e.png", c="wordbox_v.png", d="wordbox_n.png",
                                   e="wordbox_e.png", f="wordbox_l.png", g="wordbox.png",
                                   h="wordbox_u.png", i="wordbox_o.png", j="wordbox_t.png",
                                   k="wordbox_p.png", l="wordbox_w.png", m="wordbox_x.png",
                                   n="wordbox_s.png", o="wordbox_t.png", p="wordbox_r.png",
                                   q="wordbox_z.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_555_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=555,
                                   question="What is the name of the goddess that Arthur Harrow worships in the Moon Knight series",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_z.png", c="wordbox_u.png", d="wordbox_r.png",
                                   e="wordbox_t.png", f="wordbox_o.png", g="wordbox_s.png",
                                   h="wordbox_y.png", i="wordbox.png", j="wordbox_v.png",
                                   k="wordbox_p.png", l="wordbox_i.png", m="wordbox_m.png",
                                   n="wordbox_x.png", o="wordbox_q.png", p="wordbox_l.png",
                                   q="wordbox_w.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_556_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=556,
                                   question="Which god does Marc Spector's avatar resemble in the Moon Knight series",
                                   levelcounter=str(self.count), a="wordbox_q.png",
                                   b="wordbox_c.png", c="wordbox_m.png", d="wordbox_f.png",
                                   e="wordbox_u.png", f="wordbox_n.png", g="wordbox_b.png",
                                   h="wordbox_l.png", i="wordbox_h.png", j="wordbox_g.png",
                                   k="wordbox_e.png", l="wordbox_k.png", m="wordbox_s.png",
                                   n="wordbox_j.png", o="wordbox_d.png", p="wordbox_o.png",
                                   q="wordbox_i.png", r="wordbox_h.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_557_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=557,
                                   question="Who becomes the captain America in the what if series",
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
    def level_558_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=558,
                                   question="What is the name of the iron suit made by haward stark to Steve in the what if series",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_w.png", c="wordbox_e.png", d="wordbox_h.png",
                                   e="wordbox_b.png", f="wordbox_o.png", g="wordbox_m.png",
                                   h="wordbox_d.png", i="wordbox_j.png", j="wordbox_r.png",
                                   k="wordbox_t.png", l="wordbox_l.png", m="wordbox_y.png",
                                   n="wordbox_q.png", o="wordbox_s.png", p="wordbox_x.png",
                                   q="wordbox_p.png", r="wordbox.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_559_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=559,
                                   question="Who forms the superhero team to defeat Ultron in what if series",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_n.png", c="wordbox_h.png", d="wordbox_i.png",
                                   e="wordbox_r.png", f="wordbox_k.png", g="wordbox_g.png",
                                   h="wordbox_w.png", i="wordbox_l.png", j="wordbox_f.png",
                                   k="wordbox.png", l="wordbox_d.png", m="wordbox_e.png",
                                   n="wordbox_m.png", o="wordbox_t.png", p="wordbox_b.png",
                                   q="wordbox_c.png", r="wordbox_j.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_560_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=560,
                                   question="Who kills the Thanos in the what if series",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_t.png", c="wordbox_y.png", d="wordbox_n.png",
                                   e="wordbox_b.png", f="wordbox_s.png", g="wordbox_v.png",
                                   h="wordbox_z.png", i="wordbox_u.png", j="wordbox_w.png",
                                   k="wordbox_r.png", l="wordbox_q.png", m="wordbox_o.png",
                                   n="wordbox_x.png", o="wordbox_p.png", p="wordbox_l.png",
                                   q="wordbox_c.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_561_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=561,
                                   question="Who saves the Tony stark from the tenrings gang in what if serie",
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
    def level_562_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=562,
                                   question="whom did the Stephen strange lost in the car accident in what if series",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_x.png", c="wordbox_t.png", d="wordbox_m.png",
                                   e="wordbox_i.png", f="wordbox_l.png", g="wordbox_i.png",
                                   h="wordbox_q.png", i="wordbox_c.png", j="wordbox_r.png",
                                   k="wordbox_y.png", l="wordbox_e.png", m="wordbox_r.png",
                                   n="wordbox_e.png", o="wordbox_s.png", p="wordbox_n.png",
                                   q="wordbox.png", r="wordbox_h.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="bor.png", em_15="bor.png"

                                   )
    def level_563_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=563,
                                   question="what is the name of the kid taken by the Ravagers in what if series",
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
    def level_564_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=564,
                                   question="who came to take the revenge for Thor death in What if series",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_i.png", c="wordbox_n.png", d="wordbox_v.png", e="wordbox_x.png",
                                   f="wordbox_p.png",
                                   g="wordbox_q.png", h="wordbox_t.png", i="wordbox_g.png", j="wordbox_o.png",
                                   k="wordbox.png",
                                   l="wordbox_n.png", m="wordbox_k.png", n="wordbox_m.png", o="wordbox_z.png",
                                   p="wordbox_v.png", q="wordbox_h.png", r="wordbox_l.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_565_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=565,
                                   question="what is the name of the county where hope van deyn sent on a Sheild machine",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_s.png", c="wordbox_d.png", d="wordbox_n.png",
                                   e="wordbox_q.png", f="wordbox_p.png", g="wordbox_t.png",
                                   h="wordbox_i.png", i="wordbox_w.png", j="wordbox_u.png",
                                   k="wordbox_v.png", l="wordbox.png", m="wordbox_r.png",
                                   n="wordbox_x.png", o="wordbox_z.png", p="wordbox_y.png",
                                   q="wordbox_o.png", r="wordbox_k.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_566_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=566,
                                   question="Who killed all the avengers in the what if series",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_b.png", c="wordbox_q.png", d="wordbox_i.png",
                                   e="wordbox.png", f="wordbox_c.png", g="wordbox_p.png",
                                   h="wordbox_g.png", i="wordbox_n.png", j="wordbox_e.png",
                                   k="wordbox_j.png", l="wordbox_m.png", m="wordbox_o.png",
                                   n="wordbox_d.png", o="wordbox_y.png", p="wordbox_l.png",
                                   q="wordbox_k.png", r="wordbox_f.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_567_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=567,
                                   question="what is the name of the watcher for 616 universe",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_n.png", c="wordbox_d.png", d="wordbox_j.png",
                                   e="wordbox_t.png", f="wordbox_g.png", g="wordbox_o.png",
                                   h="wordbox_l.png", i="wordbox_i.png", j="wordbox_u.png",
                                   k="wordbox_f.png", l="wordbox_c.png", m="wordbox.png",
                                   n="wordbox_b.png", o="wordbox_m.png", p="wordbox_k.png",
                                   q="wordbox_k.png", r="wordbox_u.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_568_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=568,
                                   question="Who rescued Man-Thing in WareWolf by Night series",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_f.png", c="wordbox_r.png", d="wordbox_m.png",
                                   e="wordbox_n.png", f="wordbox_s.png", g="wordbox_u.png",
                                   h="wordbox_p.png", i="wordbox_j.png", j="wordbox_q.png",
                                   k="wordbox_c.png", l="wordbox_l.png", m="wordbox_k.png",
                                   n="wordbox_h.png", o="wordbox_s.png", p="wordbox_f.png",
                                   q="wordbox_e.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_569_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=569,
                                   question="With whom does Elsa Bloodstone work to rescue Man-Thing in WareWolf by Night series",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_f.png", c="wordbox_r.png", d="wordbox_m.png",
                                   e="wordbox_n.png", f="wordbox_s.png", g="wordbox_u.png",
                                   h="wordbox_p.png", i="wordbox_j.png", j="wordbox_q.png",
                                   k="wordbox_c.png", l="wordbox_l.png", m="wordbox_k.png",
                                   n="wordbox_h.png", o="wordbox_s.png", p="wordbox_f.png",
                                   q="wordbox_e.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_570_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=570,
                                   question="Against whom did Jack Russell fight to rescue Man-Thing in WareWolf by Night serie",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_f.png", c="wordbox_p.png", d="wordbox_q.png",
                                   e="wordbox_m.png", f="wordbox_s.png", g="wordbox_l.png",
                                   h="wordbox_v.png", i="wordbox_f.png", j="wordbox_u.png",
                                   k="wordbox_d.png", l="wordbox.png", m="wordbox_r.png",
                                   n="wordbox_o.png", o="wordbox_h.png", p="wordbox_b.png",
                                   q="wordbox_j.png", r="wordbox_s.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_571_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=571,
                                   question="What is the name of Ulysses Bloodstone's daughter in  WareWolf by Night serie",
                                   levelcounter=str(self.count), a="wordbox_f.png",
                                   b="wordbox_p.png", c="wordbox_q.png", d="wordbox_m.png",
                                   e="wordbox.png", f="wordbox_j.png", g="wordbox_l.png",
                                   h="wordbox_d.png", i="wordbox_c.png", j="wordbox_d.png",
                                   k="wordbox_s.png", l="wordbox_h.png", m="wordbox_q.png",
                                   n="wordbox_e.png", o="wordbox_b.png", p="wordbox_k.png",
                                   q="wordbox_n.png", r="wordbox_f.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_572_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=572,
                                   question="Who is the sister of Star-Lord",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_q.png", c="wordbox_k.png", d="wordbox_o.png",
                                   e="wordbox_b.png", f="wordbox_i.png", g="wordbox_l.png",
                                   h="wordbox_c.png", i="wordbox_n.png", j="wordbox_f.png",
                                   k="wordbox_p.png", l="wordbox_f.png", m="wordbox_m.png",
                                   n="wordbox_j.png", o="wordbox_s.png", p="wordbox.png",
                                   q="wordbox_k.png", r="wordbox_f.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_573_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=573,
                                   question="What is the name of the female superhero in the Ms.Marvel series",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_l.png", c="wordbox_u.png", d="wordbox_o.png",
                                   e="wordbox_i.png", f="wordbox.png", g="wordbox_h.png",
                                   h="wordbox_q.png", i="wordbox_k.png", j="wordbox_j.png",
                                   k="wordbox_k.png", l="wordbox.png", m="wordbox.png",
                                   n="wordbox_p.png", o="wordbox_n.png", p="wordbox.png",
                                   q="wordbox_g.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_574_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=574,
                                   question="What is the name of Kamala Khan's brother in the Ms.Marvel series",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_e.png", c="wordbox.png", d="wordbox_i.png",
                                   e="wordbox_d.png", f="wordbox_n.png", g="wordbox.png",
                                   h="wordbox_l.png", i="wordbox_c.png", j="wordbox_k.png",
                                   k="wordbox_f.png", l="wordbox.png", m="wordbox_h.png",
                                   n="wordbox_g.png", o="wordbox_m.png", p="wordbox_j.png",
                                   q="wordbox_b.png", r="wordbox_r.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_575_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=575,
                                   question="What is the name of Kamala Khan's best friend in the Ms.Marvel series",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_q.png", c="wordbox_y.png", d="wordbox_n.png",
                                   e="wordbox_z.png", f="wordbox_p.png", g="wordbox_d.png",
                                   h="wordbox_r.png", i="wordbox_x.png", j="wordbox_t.png",
                                   k="wordbox_m.png", l="wordbox_b.png", m="wordbox_u.png",
                                   n="wordbox_w.png", o="wordbox_s.png", p="wordbox_k.png",
                                   q="wordbox_o.png", r="wordbox_v.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_576_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=576,
                                   question="Who is known as Red Dagger in the Ms. Marvel series",
                                   levelcounter=str(self.count), a="wordbox_f.png",
                                   b="wordbox_o.png", c="wordbox_j.png", d="wordbox_f.png",
                                   e="wordbox_e.png", f="wordbox_i.png", g="wordbox.png",
                                   h="wordbox_b.png", i="wordbox_e.png", j="wordbox_h.png",
                                   k="wordbox_k.png", l="wordbox_l.png", m="wordbox_d.png",
                                   n="wordbox_g.png", o="wordbox_c.png", p="wordbox_r.png",
                                   q="wordbox_n.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_577_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=577,
                                   question="Who helps Sana Ali reach her father during the partition time in the Ms. Marvel series",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_l.png", c="wordbox_u.png", d="wordbox_o.png",
                                   e="wordbox_i.png", f="wordbox.png", g="wordbox_h.png",
                                   h="wordbox_q.png", i="wordbox_k.png", j="wordbox_j.png",
                                   k="wordbox_k.png", l="wordbox.png", m="wordbox.png",
                                   n="wordbox_p.png", o="wordbox_n.png", p="wordbox.png",
                                   q="wordbox_g.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_578_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=578,
                                   question="What is the name of the species that comes from the Noor Dimension in the Ms. Marvel series",
                                   levelcounter=str(self.count), a="wordbox_q.png",
                                   b="wordbox_m.png", c="wordbox_k.png", d="wordbox_f.png",
                                   e="wordbox_k.png", f="wordbox_l.png", g="wordbox_s.png",
                                   h="wordbox_t.png", i="wordbox_e.png", j="wordbox_p.png",
                                   k="wordbox_e.png", l="wordbox_o.png", m="wordbox_r.png",
                                   n="wordbox_f.png", o="wordbox_s.png", p="wordbox_j.png",
                                   q="wordbox_q.png", r="wordbox_h.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_579_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=579,
                                   question="What is the name of the dimension from which Najma and Aisha come in the Ms. Marvel series",
                                   levelcounter=str(self.count), a="wordbox_q.png",
                                   b="wordbox_j.png", c="wordbox_g.png", d="wordbox_r.png",
                                   e="wordbox_p.png", f="wordbox_h.png", g="wordbox_b.png",
                                   h="wordbox_o.png", i="wordbox_m.png", j="wordbox_i.png",
                                   k="wordbox_l.png", l="wordbox_d.png", m="wordbox_k.png",
                                   n="wordbox_c.png", o="wordbox_f.png", p="wordbox_o.png",
                                   q="wordbox_e.png", r="wordbox_n.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_580_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=580,
                                   question="What is the name of Aisha's daughter in the Ms. Marvel series",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_f.png", c="wordbox_j.png", d="wordbox_e.png",
                                   e="wordbox.png", f="wordbox_b.png", g="wordbox.png",
                                   h="wordbox_m.png", i="wordbox_i.png", j="wordbox_c.png",
                                   k="wordbox_h.png", l="wordbox_s.png", m="wordbox_k.png",
                                   n="wordbox_l.png", o="wordbox_d.png", p="wordbox_n.png",
                                   q="wordbox_p.png", r="wordbox_g.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_581_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=581,
                                   question="What is the name of the person who marries Aisha in the Ms.Marvel series",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_z.png", c="wordbox_y.png", d="wordbox_n.png",
                                   e="wordbox_x.png", f="wordbox_o.png", g="wordbox_v.png",
                                   h="wordbox.png", i="wordbox_q.png", j="wordbox_u.png",
                                   k="wordbox_p.png", l="wordbox_h.png", m="wordbox_s.png",
                                   n="wordbox_r.png", o="wordbox_t.png", p="wordbox.png",
                                   q="wordbox_w.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_582_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=582,
                                   question="Whose bracelet does Kamala Khan use in the Ms. Marvel series",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_o.png", c="wordbox_n.png", d="wordbox_s.png",
                                   e="wordbox_k.png", f="wordbox_d.png", g="wordbox_j.png",
                                   h="wordbox_i.png", i="wordbox_l.png", j="wordbox_g.png",
                                   k="wordbox.png", l="wordbox_f.png", m="wordbox_p.png",
                                   n="wordbox_h.png", o="wordbox_e.png", p="wordbox.png",
                                   q="wordbox_m.png", r="wordbox_c.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_583_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=583,
                                   question="Who is the grandmother of Kamala Khan in the Ms. Marvel series",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_o.png", c="wordbox_n.png", d="wordbox_s.png",
                                   e="wordbox_k.png", f="wordbox_d.png", g="wordbox_j.png",
                                   h="wordbox_i.png", i="wordbox_l.png", j="wordbox_g.png",
                                   k="wordbox.png", l="wordbox_f.png", m="wordbox_p.png",
                                   n="wordbox_h.png", o="wordbox_e.png", p="wordbox.png",
                                   q="wordbox_m.png", r="wordbox_c.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_584_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=584,
                                   question="Who was selected as the board member for the mosque in the Ms. Marvel series",
                                   levelcounter=str(self.count), a="wordbox_y.png",
                                   b="wordbox.png", c="wordbox_q.png", d="wordbox_w.png",
                                   e="wordbox_p.png", f="wordbox_s.png", g="wordbox_u.png",
                                   h="wordbox_v.png", i="wordbox_r.png", j="wordbox_t.png",
                                   k="wordbox_k.png", l="wordbox_l.png", m="wordbox_o.png",
                                   n="wordbox_i.png", o="wordbox.png", p="wordbox_m.png",
                                   q="wordbox_x.png", r="wordbox_n.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_585_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=585,
                                   question="Who is the main antagonist in the She-Hulk series",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_f.png", c="wordbox_s.png", d="wordbox_d.png",
                                   e="wordbox_c.png", f="wordbox_z.png", g="wordbox_d.png",
                                   h="wordbox_y.png", i="wordbox_h.png", j="wordbox_t.png",
                                   k="wordbox_p.png", l="wordbox_f.png", m="wordbox_e.png",
                                   n="wordbox_z.png", o="wordbox_o.png", p="wordbox_l.png",
                                   q="wordbox_x.png", r="wordbox_p.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_586_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=586,
                                   question="What is the name of Hulk's son",
                                   levelcounter=str(self.count), a="wordbox_g.png",
                                   b="wordbox_o.png", c="wordbox_f.png", d="wordbox_e.png",
                                   e="wordbox_i.png", f="wordbox_r.png", g="wordbox_b.png",
                                   h="wordbox_n.png", i="wordbox_j.png", j="wordbox_s.png",
                                   k="wordbox_m.png", l="wordbox_c.png", m="wordbox_h.png",
                                   n="wordbox_k.png", o="wordbox.png", p="wordbox_d.png",
                                   q="wordbox_l.png", r="wordbox.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_587_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=587,
                                   question="What is the superhero name of Matt Murdock",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_j.png", c="wordbox_q.png", d="wordbox_v.png",
                                   e="wordbox_g.png", f="wordbox_m.png", g="wordbox.png",
                                   h="wordbox_p.png", i="wordbox_d.png", j="wordbox_w.png",
                                   k="wordbox_d.png", l="wordbox_l.png", m="wordbox_e.png",
                                   n="wordbox_o.png", o="wordbox_e.png", p="wordbox_h.png",
                                   q="wordbox_n.png", r="wordbox_r.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_588_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=588,
                                   question="Who designed the Leapfrog suit for Jennifer Walters in the She-Hulk series",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_s.png", c="wordbox_w.png", d="wordbox_b.png",
                                   e="wordbox_z.png", f="wordbox_o.png", g="wordbox_l.png",
                                   h="wordbox_m.png", i="wordbox_u.png", j="wordbox_j.png",
                                   k="wordbox_n.png", l="wordbox_k.png", m="wordbox.png",
                                   n="wordbox_o.png", o="wordbox_e.png", p="wordbox_x.png",
                                   q="wordbox_c.png", r="wordbox_y.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_589_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=589,
                                   question="Who takes Abomination from the DODC facility to the fight club in the She-Hulk series",
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
    def level_590_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=590,
                                   question="What is the superhero form name of Emil Blonsky in the She-Hulk series",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_k.png", c="wordbox_i.png", d="wordbox_p.png", e="wordbox_o.png",
                                   f="wordbox_l.png",
                                   g="wordbox_m.png", h="wordbox_f.png", i="wordbox_n.png", j="wordbox_i.png",
                                   k="wordbox_s.png",
                                   l="wordbox_n.png", m="wordbox_b.png", n="wordbox_q.png", o="wordbox_o.png",
                                   p="wordbox_u.png", q="wordbox.png", r="wordbox_t.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_591_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=591,
                                   question="Who handles the Emil Blonsky case in the She-Hulk series",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_k.png", c="wordbox_e.png", d="wordbox_n.png",
                                   e="wordbox_l.png", f="wordbox_i.png", g="wordbox_s.png",
                                   h="wordbox_r.png", i="wordbox.png", j="wordbox_f.png",
                                   k="wordbox_m.png", l="wordbox_j.png", m="wordbox_t.png",
                                   n="wordbox_e.png", o="wordbox_r.png", p="wordbox_n.png",
                                   q="wordbox_w.png", r="wordbox_q.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="bor.png", em_15="bor.png"

                                   )
    def level_592_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=592,
                                   question="Who takes inspiration from Hawkeye in the Hawkeye series",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_p.png", c="wordbox_q.png", d="wordbox_e.png",
                                   e="wordbox_n.png", f="wordbox_i.png", g="wordbox_h.png",
                                   h="wordbox_w.png", i="wordbox.png", j="wordbox_s.png",
                                   k="wordbox_k.png", l="wordbox_m.png", m="wordbox_s.png",
                                   n="wordbox_v.png", o="wordbox_t.png", p="wordbox_l.png",
                                   q="wordbox_b.png", r="wordbox_o.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_593_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=593,
                                   question="What is the alternate name for Jack Duquesne in the Hawkeye series",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_c.png", c="wordbox_b.png", d="wordbox_r.png",
                                   e="wordbox_y.png", f="wordbox_l.png", g="wordbox_z.png",
                                   h="wordbox_s.png", i="wordbox_t.png", j="wordbox_n.png",
                                   k="wordbox_q.png", l="wordbox_o.png", m="wordbox_s.png",
                                   n="wordbox_m.png", o="wordbox_v.png", p="wordbox_w.png",
                                   q="wordbox_x.png", r="wordbox_d.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_594_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=594,
                                   question="What is the name of the Kate's dog in Hawkeye series",
                                   levelcounter=str(self.count), a="wordbox_y.png",
                                   b="wordbox_i.png", c="wordbox_g.png", d="wordbox_x.png",
                                   e="wordbox_k.png", f="wordbox_e.png", g="wordbox_n.png",
                                   h="wordbox_h.png", i="wordbox_u.png", j="wordbox_f.png",
                                   k="wordbox_f.png", l="wordbox_b.png", m="wordbox_m.png",
                                   n="wordbox_c.png", o="wordbox_j.png", p="wordbox_d.png",
                                   q="wordbox_z.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_595_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=595,
                                   question="Who kills the Armand Duquesne III in Hawkeye series",
                                   levelcounter=str(self.count), a="wordbox_c.png",
                                   b="wordbox_k.png", c="wordbox_p.png", d="wordbox_t.png",
                                   e="wordbox_l.png", f="wordbox_v.png", g="wordbox_s.png",
                                   h="wordbox_j.png", i="wordbox_e.png", j="wordbox_q.png",
                                   k="wordbox_n.png", l="wordbox_o.png", m="wordbox_f.png",
                                   n="wordbox_s.png", o="wordbox_b.png", p="wordbox_l.png",
                                   q="wordbox_h.png", r="wordbox_g.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_596_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=596,
                                   question="Who killed Maya Lopez's father",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_f.png", c="wordbox_g.png", d="wordbox_l.png",
                                   e="wordbox_o.png", f="wordbox_n.png", g="wordbox_m.png",
                                   h="wordbox_s.png", i="wordbox_k.png", j="wordbox_u.png",
                                   k="wordbox_j.png", l="wordbox_n.png", m="wordbox_p.png",
                                   n="wordbox_q.png", o="wordbox_b.png", p="wordbox_i.png",
                                   q="wordbox_c.png", r="wordbox_h.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_597_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=597,
                                   question="What is the name of the person who makes the superhero suits in the She-Hulk series",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_s.png", c="wordbox_w.png", d="wordbox_b.png",
                                   e="wordbox_z.png", f="wordbox_o.png", g="wordbox_l.png",
                                   h="wordbox_m.png", i="wordbox_u.png", j="wordbox_j.png",
                                   k="wordbox_n.png", l="wordbox_k.png", m="wordbox.png",
                                   n="wordbox_o.png", o="wordbox_e.png", p="wordbox_x.png",
                                   q="wordbox_c.png", r="wordbox_y.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_598_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=598,
                                   question="What is the original name of the character Echo",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_t.png", c="wordbox.png", d="wordbox_e.png",
                                   e="wordbox_d.png", f="wordbox_p.png", g="wordbox_l.png",
                                   h="wordbox_s.png", i="wordbox_g.png", j="wordbox_y.png",
                                   k="wordbox_h.png", l="wordbox_o.png", m="wordbox_r.png",
                                   n="wordbox.png", o="wordbox_q.png", p="wordbox_z.png",
                                   q="wordbox_n.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_599_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=599,
                                   question="Who is the leader of the track suit gang in Hawkeye series",
                                   levelcounter=str(self.count), a="wordbox_c.png",
                                   b="wordbox_k.png", c="wordbox_p.png", d="wordbox_t.png",
                                   e="wordbox_l.png", f="wordbox_v.png", g="wordbox_s.png",
                                   h="wordbox_j.png", i="wordbox_e.png", j="wordbox_q.png",
                                   k="wordbox_n.png", l="wordbox_o.png", m="wordbox_f.png",
                                   n="wordbox_s.png", o="wordbox_b.png", p="wordbox_l.png",
                                   q="wordbox_h.png", r="wordbox_g.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_600_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=600,
                                   question="From whom did Jennifer Lawrence's character get her powers",
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




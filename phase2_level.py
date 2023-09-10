from kivy.storage.jsonstore import JsonStore
import coin_inc
import allhint
import levels_game2
class phase2_questions(coin_inc.coininc,allhint.hint_all):
    def __init__(self):
        self.counters = ["2/100", "3/100", "4/100", "5/100", "6/100", "7/100", "8/100", "9/100", "10/100", "11/100",
                         "12/100", "13/100", "14/100", "15/100",
                         "16/100", "17/100", "18/100", "19/100", "20/100", "21/100", "22/100", "23/100", "24/100",
                         "25/100", "26/100", "27/100", "28/100", "29/100", "30/100",
                         "31/100", "32/100", "33/100", "34/100", "35/100", "36/100", "37/100", "38/100", "39/100",
                         "40/100", "41/100", "42/100", "43/100", "44/100", "45/100",
                         "46/100", "47/100", "48/100", "49/100", "50/100", "51/100", "52/100", "53/100", "54/100",
                         "55/100", "56/100", "57/100", "58/100", "59/100", "60/100",
                         "61/100", "62/100", "63/100", "64/100", "65/100", "66/100", "67/100", "68/100", "69/100",
                         "70/100", "71/100", "72/100", "73/100", "74/100", "75/100",
                         "76/100", "77/100", "78/100", "79/100", "80/100", "81/100", "82/100", "83/100", "84/100",
                         "85/100", "86/100", "87/100", "88/100", "89/100", "90/100",
                         "91/100", "92/100", "93/100", "94/100", "95/100", "96/100", "97/100", "98/100", "99/100",
                         "100/100"]
    def counter(self,*args):

        lev_coun = JsonStore("counter1.json")
        lst = lev_coun.get("random_level_list")["number"]
        s = lev_coun.get("random_level_list")["number"][0]

        lst.remove(s)
        lev_coun.put("random_level_list",number = lst)

        return  self.counters[s]
    def level_150_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=150,
                                   question="What is Name Of The Gamora's Sister",
                                   levelcounter=str(self.count), a="wordbox_u.png",
                                   b="wordbox_k.png", c="wordbox_b.png", d="wordbox_t.png", e="wordbox_v.png",
                                   f="wordbox_n.png",
                                   g="wordbox_e.png", h="wordbox_x.png", i="wordbox_l.png", j="wordbox_q.png",
                                   k="wordbox_o.png",
                                   l="wordbox_k.png", m="wordbox_k.png", n="wordbox_d.png", o="wordbox_m.png",
                                   p="wordbox_t.png", q="wordbox_p.png", r="wordbox.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_151_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=151,
                                   question="Who saves the passengers from the hijacked plane in Iron Man 3 movie",
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
    def level_152_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=152,
                                   question="What is the name of the suit mainly used in Iron Man 3 movie",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_t.png", c="wordbox_q.png", d="wordbox_s.png", e="wordbox_p.png",
                                   f="wordbox_k.png",
                                   g="num_2.png", h="num_9.png", i="wordbox.png", j="wordbox_f.png",
                                   k="wordbox_t.png",
                                   l="num_8.png", m="wordbox_o.png", n="wordbox_m.png", o="wordbox_b.png",
                                   p="wordbox_l.png", q="num_7.png", r="num_4.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_153_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=153,
                                   question="What is the name of the kid who helps Tony Stark in Iron Man 3 movie",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_y.png", c="wordbox_r.png", d="wordbox_p.png", e="wordbox_f.png",
                                   f="wordbox_e.png",
                                   g="wordbox_t.png", h="wordbox_k.png", i="wordbox_e.png", j="wordbox_o.png",
                                   k="wordbox_h.png",
                                   l="wordbox_n.png", m="wordbox_e.png", n="wordbox.png", o="wordbox_q.png",
                                   p="wordbox_l.png", q="wordbox_m.png", r="wordbox_r.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_154_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=154, question="What is the name of the AI used in Iron Man 3 movie",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_p.png", c="wordbox_i.png", d="wordbox_c.png", e="wordbox_h.png",
                                   f="wordbox_s.png",
                                   g="wordbox_j.png", h="wordbox_h.png", i="wordbox_m.png", j="wordbox_k.png",
                                   k="wordbox.png",
                                   l="wordbox_p.png", m="wordbox_n.png", n="wordbox_o.png", o="wordbox_r.png",
                                   p="wordbox_l.png", q="wordbox_z.png", r="wordbox_v.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_155_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=155,
                                   question="Who is the bodyguard for Tony Stark in the movie Iron Man 3",
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
    def level_156_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=156,
                                   question="Which friend of Tony Stark was injured in the explosion in the movie Iron Man 3",
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
    def level_157_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=157,
                                   question="Who saves the President in Iron Man 3 movie",
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
    def level_158_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=158,
                                   question="What is the name of the suit used by Tony to rescue Pepper Potts in Iron Man 3 movie",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_t.png", c="wordbox_q.png", d="wordbox_s.png", e="wordbox_p.png",
                                   f="wordbox_k.png",
                                   g="num_2.png", h="num_9.png", i="wordbox.png", j="wordbox_f.png",
                                   k="wordbox_t.png",
                                   l="num_8.png", m="wordbox_o.png", n="wordbox_m.png", o="wordbox_b.png",
                                   p="wordbox_l.png", q="num_7.png", r="num_4.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_159_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=159,
                                   question="Who killed Aldrich Killian in Iron Man 3",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_k.png", c="wordbox_s.png", d="wordbox_t.png", e="wordbox_m.png",
                                   f="wordbox_t.png",
                                   g="wordbox_p.png", h="wordbox_c.png", i="wordbox_e.png", j="wordbox_q.png",
                                   k="wordbox_r.png",
                                   l="wordbox_e.png", m="wordbox_l.png", n="wordbox_p.png", o="wordbox_g.png",
                                   p="wordbox_p.png", q="wordbox_d.png", r="wordbox_p.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_160_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=160,
                                   question="What did the Tony Stark removed at the end of Iron Man 3 movie",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_e.png", c="wordbox_q.png", d="wordbox.png", e="wordbox_s.png",
                                   f="wordbox_r.png",
                                   g="wordbox.png", h="wordbox_k.png", i="wordbox_r.png", j="wordbox_c.png",
                                   k="wordbox_l.png",
                                   l="wordbox_t.png", m="wordbox_f.png", n="wordbox_c.png", o="wordbox_o.png",
                                   p="wordbox_n.png", q="wordbox_m.png", r="wordbox_r.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_161_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=161,
                                   question="How many realms that Asgard protecting",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox.png", c="wordbox_i.png", d="wordbox_t.png", e="wordbox_k.png",
                                   f="wordbox_l.png",
                                   g="wordbox_m.png", h="wordbox_q.png", i="wordbox_e.png", j="wordbox_s.png",
                                   k="wordbox_b.png",
                                   l="wordbox_n.png", m="wordbox_l.png", n="wordbox_t.png", o="wordbox_y.png",
                                   p="wordbox_o.png", q="wordbox_n.png", r="wordbox_g.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_162_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=162,
                                   question="Name of the queen where killed by Malekith in Asgard",
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
    def level_163_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=163,
                                   question="Who helps the Thor to enter Svartalfheim in Thor dark world movie",
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
    def level_164_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=164,
                                   question="Who is killed by Malekith in Svartalfheim in Thor Dark World",
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
    def level_165_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=165,
                                   question="How Many Realms does Convergence happen",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox.png", c="wordbox_i.png", d="wordbox_t.png", e="wordbox_k.png",
                                   f="wordbox_l.png",
                                   g="wordbox_m.png", h="wordbox_q.png", i="wordbox_e.png", j="wordbox_s.png",
                                   k="wordbox_b.png",
                                   l="wordbox_n.png", m="wordbox_l.png", n="wordbox_t.png", o="wordbox_y.png",
                                   p="wordbox_o.png", q="wordbox_n.png", r="wordbox_g.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_166_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=166,
                                   question="What is the name of the winter soldier in CaptianAmerica Winter Soldier movie",
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
    def level_167_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=167,
                                   question="Name of the Sheild director in the Winter Soldier movie",
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
    def level_168_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=168,
                                   question="Thor's girlfriend name",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_p.png", c="wordbox_k.png", d="wordbox_e.png", e="wordbox_q.png",
                                   f="wordbox_f.png",
                                   g="wordbox_l.png", h="wordbox_v.png", i="wordbox_r.png", j="wordbox_n.png",
                                   k="wordbox_u.png",
                                   l="wordbox_s.png", m="wordbox.png", n="wordbox_w.png", o="wordbox_o.png",
                                   p="wordbox_j.png", q="wordbox_b.png", r="wordbox_e.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_169_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=169,
                                   question="Which material does the hand of the Winter Soldier made off",
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
    def level_170_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=170,
                                   question="To whom the Winter Soldier working for",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_r.png", c="wordbox_f.png", d="wordbox_p.png", e="wordbox_o.png",
                                   f="wordbox_l.png",
                                   g="wordbox_q.png", h="wordbox_l.png", i="wordbox_y.png", j="wordbox_x.png",
                                   k="wordbox_b.png",
                                   l="wordbox.png", m="wordbox_n.png", n="wordbox_d.png", o="wordbox_g.png",
                                   p="wordbox_s.png", q="wordbox_h.png", r="wordbox_c.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_171_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=171,
                                   question="Name of the Person Facks his Death in Winter Soldier movie",
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
    def level_172_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=172,
                                   question="What is the name of the doctor who made the Winter Soldier's bionic arm",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_f.png", c="wordbox_d.png", d="wordbox_n.png", e="wordbox_k.png",
                                   f="wordbox_l.png",
                                   g="wordbox_z.png", h="wordbox_c.png", i="wordbox_r.png", j="wordbox_o.png",
                                   k="wordbox_t.png",
                                   l="wordbox_h.png", m="wordbox_s.png", n="wordbox_i.png", o="wordbox_t.png",
                                   p="wordbox_m.png", q="wordbox_g.png", r="wordbox.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_173_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=173,
                                   question="Name of the person transfers his Mind into a Computer in the Winter Soldier movie",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_f.png", c="wordbox_d.png", d="wordbox_n.png", e="wordbox_k.png",
                                   f="wordbox_l.png",
                                   g="wordbox_z.png", h="wordbox_c.png", i="wordbox_r.png", j="wordbox_o.png",
                                   k="wordbox_t.png",
                                   l="wordbox_h.png", m="wordbox_s.png", n="wordbox_i.png", o="wordbox_t.png",
                                   p="wordbox_m.png", q="wordbox_g.png", r="wordbox.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_174_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=174,
                                   question="Which facility did Arnim Zola intend to rebuild Hydra",
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
    def level_175_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=175,
                                   question="Name of the old women that Steve Rogers meet in the winter soldier movie",
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
    def level_176_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=176,
                                   question="Name of the powerful terrorist leader in Iron Man 3 movie",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_k.png", c="wordbox_d.png", d="wordbox_t.png", e="wordbox.png",
                                   f="wordbox_p.png",
                                   g="wordbox_o.png", h="wordbox_f.png", i="wordbox_m.png", j="wordbox_c.png",
                                   k="wordbox_q.png",
                                   l="wordbox_v.png", m="wordbox.png", n="wordbox_r.png", o="wordbox_s.png",
                                   p="wordbox_i.png", q="wordbox_n.png", r="wordbox_t.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_177_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=177,
                                   question="Name of the villain in Iron Man 3 movie",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_l.png", c="wordbox.png", d="wordbox_p.png", e="wordbox_i.png",
                                   f="wordbox_r.png",
                                   g="wordbox_d.png", h="wordbox_t.png", i="wordbox_l.png", j="wordbox_v.png",
                                   k="wordbox.png",
                                   l="wordbox_h.png", m="wordbox_o.png", n="wordbox_i.png", o="wordbox_c.png",
                                   p="wordbox_i.png", q="wordbox_k.png", r="wordbox_l.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="bor.png", em_15="mix.png")
    def level_178_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=178,
                                   question="In the movie IronMan 3, to which city do the IronMan suit pieces fly",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_t.png", c="wordbox_l.png", d="wordbox_p.png", e="wordbox_d.png",
                                   f="wordbox_h.png",
                                   g="wordbox_r.png", h="wordbox_k.png", i="wordbox_g.png", j="wordbox_v.png",
                                   k="wordbox_d.png",
                                   l="wordbox_i.png", m="wordbox_n.png", n="wordbox_o.png", o="wordbox_l.png",
                                   p="wordbox_k.png", q="wordbox_m.png", r="wordbox_s.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_179_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=179,
                                   question="What is the name of James Rhodes suit",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox.png", c="wordbox_w.png", d="wordbox_m.png", e="wordbox_c.png",
                                   f="wordbox_t.png",
                                   g="wordbox_k.png", h="wordbox_e.png", i="wordbox_o.png", j="wordbox_i.png",
                                   k="wordbox_d.png",
                                   l="wordbox_n.png", m="wordbox_p.png", n="wordbox_v.png", o="wordbox_h.png",
                                   p="wordbox_f.png", q="wordbox_r.png", r="wordbox.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_180_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=180,
                                   question="What was War Machine renamed as in Iron Man 3 movie",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_k.png", c="wordbox_o.png", d="wordbox_c.png", e="wordbox_n.png",
                                   f="wordbox_r.png",
                                   g="wordbox_t.png", h="wordbox.png", i="wordbox_i.png", j="wordbox_f.png",
                                   k="wordbox_v.png",
                                   l="wordbox_t.png", m="wordbox_i.png", n="wordbox_q.png", o="wordbox_p.png",
                                   p="wordbox_s.png", q="wordbox_m.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_181_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=181,
                                   question="How many people were rescued from the hijacked plane in the movie IronMan 3",
                                   levelcounter=str(self.count), a="num_9.png",
                                   b="num_4.png", c="num_9.png", d="num_4.png", e="num_5.png",
                                   f="num_2.png",
                                   g="num_2.png", h="num_7.png", i="num_3.png", j="num_5.png",
                                   k="num_7.png",
                                   l="num_6.png", m="num_1.png", n="num_2.png", o="num_6.png",
                                   p="num_4.png", q="num_8.png", r="num_9.png",
                                   em_1="bor.png", em_2="bor.png", em_3="mix.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_182_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=182,
                                   question="How many number of suits where destroyed in Iron Man 3 movie",
                                   levelcounter=str(self.count), a="num_9.png",
                                   b="num_4.png", c="num_9.png", d="num_3.png", e="num_1.png",
                                   f="num_2.png",
                                   g="num_7.png", h="num_3.png", i="num_1.png", j="num_5.png",
                                   k="num_7.png",
                                   l="num_6.png", m="num_1.png", n="num_3.png", o="num_6.png",
                                   p="num_1.png", q="num_8.png", r="num_9.png",
                                   em_1="bor.png", em_2="bor.png", em_3="mix.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_183_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=183,
                                   question="How many years for caption america according to the Winter Soldier movie ",
                                   levelcounter=str(self.count), a="num_7.png",
                                   b="num_9.png", c="num_4.png", d="num_7.png", e="num_2.png",
                                   f="num_1.png",
                                   g="num_2.png", h="num_1.png", i="num_8.png", j="num_7.png",
                                   k="num_6.png",
                                   l="num_9.png", m="num_5.png", n="num_4.png", o="num_3.png",
                                   p="num_1.png", q="num_8.png", r="num_2.png",
                                   em_1="bor.png", em_2="bor.png", em_3="mix.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_184_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=184,
                                   question="Name of the agent 13 in the Winter Soldier movie",
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
    def level_185_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=185,
                                   question="What is the name of the object that the masked man throws under Nick Fury's SUV in the movie Winter Soldier",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox.png", c="wordbox_n.png", d="wordbox_k.png", e="wordbox_e.png",
                                   f="wordbox_f.png",
                                   g="wordbox_q.png", h="wordbox_i.png", i="wordbox_v.png", j="wordbox_n.png",
                                   k="wordbox_t.png",
                                   l="wordbox_i.png", m="wordbox_e.png", n="wordbox_c.png", o="wordbox_s.png",
                                   p="wordbox_u.png", q="wordbox_g.png", r="wordbox_m.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_186_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=186,
                                   question="Who was appointed to watch over Steve Rogers in the movie The Winter Soldier",
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
    def level_187_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=187,
                                   question="Where did Steve Rogers train during World War II",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_k.png", c="wordbox_m.png", d="wordbox_t.png", e="wordbox_p.png",
                                   f="wordbox_o.png",
                                   g="wordbox_i.png", h="wordbox_b.png", i="wordbox.png", j="wordbox_j.png",
                                   k="wordbox_e.png",
                                   l="wordbox_q.png", m="wordbox_c.png", n="wordbox_v.png", o="wordbox_l.png",
                                   p="wordbox_g.png", q="wordbox_k.png", r="wordbox_h.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_188_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=188,
                                   question="How many Helicarriers were there in the Project Insight in the movie Winter Soldier",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_t.png", c="wordbox_k.png", d="wordbox_e.png", e="wordbox_f.png",
                                   f="wordbox_p.png",
                                   g="wordbox_c.png", h="wordbox_r.png", i="wordbox_l.png", j="wordbox_m.png",
                                   k="wordbox_h.png",
                                   l="wordbox_s.png", m="wordbox_n.png", n="wordbox_o.png", o="wordbox_e.png",
                                   p="wordbox_q.png", q="wordbox_p.png", r="wordbox_m.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_189_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=189,
                                   question="What was the name of the project that Nick Fury was involved in during the movie Winter Soldier",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_k.png", c="wordbox_o.png", d="wordbox_l.png", e="wordbox_q.png",
                                   f="wordbox_i.png",
                                   g="wordbox_v.png", h="wordbox_h.png", i="wordbox_n.png", j="wordbox_c.png",
                                   k="wordbox_d.png",
                                   l="wordbox_j.png", m="wordbox_m.png", n="wordbox_s.png", o="wordbox_o.png",
                                   p="wordbox_g.png", q="wordbox_t.png", r="wordbox_p.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_190_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=190,
                                   question="Who was Steve Rogers' running partner in the movie Winter Soldier",
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
    def level_191_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=191,
                                   question="What was the name of the mobile satellite launch platform project in the movie Winter Soldier",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_k.png", c="wordbox_o.png", d="wordbox_l.png", e="wordbox_q.png",
                                   f="wordbox_i.png",
                                   g="wordbox_v.png", h="wordbox_h.png", i="wordbox_n.png", j="wordbox_c.png",
                                   k="wordbox_d.png",
                                   l="wordbox_j.png", m="wordbox_m.png", n="wordbox_s.png", o="wordbox_o.png",
                                   p="wordbox_g.png", q="wordbox_t.png", r="wordbox_p.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_192_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=192,
                                   question="What is the name of the object that has the power to destroy the entire galaxy or the nine realms",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_f.png", c="wordbox_e.png", d="wordbox_k.png", e="wordbox_l.png",
                                   f="wordbox_o.png",
                                   g="wordbox_l.png", h="wordbox_s.png", i="wordbox_t.png", j="wordbox_p.png",
                                   k="wordbox_v.png",
                                   l="wordbox.png", m="wordbox_h.png", n="wordbox_n.png", o="wordbox_b.png",
                                   p="wordbox_j.png", q="wordbox_m.png", r="wordbox_e.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_193_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=193,
                                   question="Who was the primary villain in the movie Thor The Dark World",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_f.png", c="wordbox_e.png", d="wordbox_o.png", e="wordbox_p.png",
                                   f="wordbox_m.png",
                                   g="wordbox_s.png", h="wordbox.png", i="wordbox_u.png", j="wordbox_i.png",
                                   k="wordbox_v.png",
                                   l="wordbox_h.png", m="wordbox_k.png", n="wordbox_d.png", o="wordbox_l.png",
                                   p="wordbox_j.png", q="wordbox_q.png", r="wordbox_v.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_194_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=194,
                                   question="What is the name of the person who escapes from the Asgard prison and becomes the loyal warrior for Malekith in the Thor Dark World",
                                   levelcounter=str(self.count), a="wordbox_v.png",
                                   b="wordbox_m.png", c="wordbox_f.png", d="wordbox_o.png", e="wordbox_o.png",
                                   f="wordbox_t.png",
                                   g="wordbox_l.png", h="wordbox_n.png", i="wordbox_r.png", j="wordbox_t.png",
                                   k="wordbox_d.png",
                                   l="wordbox_g.png", m="wordbox_q.png", n="wordbox_h.png", o="wordbox.png",
                                   p="wordbox_y.png", q="wordbox_j.png", r="wordbox_i.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_195_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=195,
                                   question="What is the name of the planet located outside of the Nine Realms",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_d.png", c="wordbox_p.png", d="wordbox_k.png", e="wordbox_o.png",
                                   f="wordbox_l.png",
                                   g="wordbox_p.png", h="wordbox_n.png", i="wordbox.png", j="wordbox_q.png",
                                   k="wordbox_v.png",
                                   l="wordbox_m.png", m="wordbox_s.png", n="wordbox_v.png", o="wordbox_f.png",
                                   p="wordbox_r.png", q="wordbox_h.png", r="wordbox.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_196_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=196,
                                   question="Where is Greenwich located in the Thor Dark World movie",
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
    def level_197_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=197,
                                   question="What is the name of the realm where Malekith retrieves the Aether in the Thor Dark World",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_e.png", c="wordbox.png", d="wordbox_c.png", e="wordbox_u.png",
                                   f="wordbox_l.png",
                                   g="wordbox_s.png", h="wordbox_q.png", i="wordbox_y.png", j="wordbox_r.png",
                                   k="wordbox_g.png",
                                   l="wordbox_v.png", m="wordbox_f.png", n="wordbox_m.png", o="wordbox.png",
                                   p="wordbox_k.png", q="wordbox_i.png", r="wordbox_h.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_198_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=198,
                                   question="What is the name of Jane Foster's best friend",
                                   levelcounter=str(self.count), a="wordbox_d.png",
                                   b="wordbox_p.png", c="wordbox_o.png", d="wordbox_e.png", e="wordbox_q.png",
                                   f="wordbox_y.png",
                                   g="wordbox_i.png", h="wordbox_v.png", i="wordbox_n.png", j="wordbox_r.png",
                                   k="wordbox_u.png",
                                   l="wordbox_w.png", m="wordbox_c.png", n="wordbox_t.png", o="wordbox_l.png",
                                   p="wordbox_s.png", q="wordbox_m.png", r="wordbox.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_199_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=199,
                                   question="Whom does Thor seek to kill in the movie Thor The Dark World",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_f.png", c="wordbox_e.png", d="wordbox_o.png", e="wordbox_p.png",
                                   f="wordbox_m.png",
                                   g="wordbox_s.png", h="wordbox.png", i="wordbox_u.png", j="wordbox_i.png",
                                   k="wordbox_v.png",
                                   l="wordbox_h.png", m="wordbox_k.png", n="wordbox_d.png", o="wordbox_l.png",
                                   p="wordbox_j.png", q="wordbox_q.png", r="wordbox_v.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")

    def level_200_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=200,
                                   question="Who is the high ranking shield agent after nick fury in Shield Organization",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_f.png", c="wordbox_v.png", d="wordbox_r.png", e="wordbox_k.png",
                                   f="wordbox_i.png",
                                   g="wordbox_l.png", h="wordbox_v.png", i="wordbox_m.png", j="wordbox_d.png",
                                   k="wordbox_i.png",
                                   l="wordbox_l.png", m="wordbox_q.png", n="wordbox.png", o="wordbox_p.png",
                                   p="wordbox_h.png", q="wordbox_f.png", r="wordbox_j.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")

    def level_101_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=101,
                                   question="What is the name of the team leader for the Guardians of the Galaxy team",
                                   levelcounter=str(self.count), a="wordbox_e.png",
                                   b="wordbox_d.png", c="wordbox_u.png", d="wordbox_b.png",
                                   e="wordbox_t.png", f="wordbox_i.png", g="wordbox_j.png",
                                   h="wordbox_l.png", i="wordbox_e.png", j="wordbox_f.png",
                                   k="wordbox_r.png", l="wordbox_c.png", m="wordbox.png",
                                   n="wordbox_q.png", o="wordbox_h.png", p="wordbox_l.png",
                                   q="wordbox_g.png", r="wordbox_p.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_102_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=102,
                                   question="What is Star-Lord's girlfriend name in the Guardians of the Galaxy movie",
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

    def level_103_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=103,
                                   question="With Whome did Ronan deal to destroy the Xander planet",
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

    def level_104_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=104,
                                   question="What is the name of the villian in the Guardians of the Galaxy movie",
                                   levelcounter=str(self.count), a="wordbox_j.png",
                                   b="wordbox_b.png", c="wordbox_i.png", d="wordbox_g.png",
                                   e="wordbox_o.png", f="wordbox_h.png", g="wordbox_n.png",
                                   h="wordbox_d.png", i="wordbox_f.png", j="wordbox.png",
                                   k="wordbox_k.png", l="wordbox_c.png", m="wordbox_e.png",
                                   n="wordbox_e.png", o="wordbox_r.png", p="wordbox_n.png",
                                   q="wordbox_l.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )

    def level_105_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=105,
                                   question="What is the name of the superhero that looks like a tree",
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
    def level_106_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=106,
                                   question="What is the name of the stone that Ronan is searching for, in the Guardians of the Galaxy movie",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_v.png", c="wordbox_w.png", d="wordbox_n.png",
                                   e="wordbox_t.png", f="wordbox_s.png", g="wordbox_p.png",
                                   h="wordbox_k.png", i="wordbox_r.png", j="wordbox_q.png",
                                   k="wordbox_v.png", l="wordbox_o.png", m="wordbox_l.png",
                                   n="wordbox_t.png", o="wordbox_e.png", p="wordbox_m.png",
                                   q="wordbox_d.png", r="wordbox_c.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_107_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=107,
                                   question="What is the name of the elder daughter of Thanos",
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
    def level_108_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=108,
                                   question="What is the name of the Gamora's sister",
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
    def level_109_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=109,
                                   question="What is the name of the person who brings Peter Quill to the planet Xander,from planet Earth",
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
    def level_110_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=110,
                                   question="What did Star-Lord rob from the planet Morag",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_f.png", c="wordbox_k.png", d="wordbox_j.png",
                                   e="wordbox_i.png", f="wordbox_d.png", g="wordbox_h.png",
                                   h="wordbox_p.png", i="wordbox_o.png", j="wordbox_b.png",
                                   k="wordbox_n.png", l="wordbox_e.png", m="wordbox_q.png",
                                   n="wordbox_c.png", o="wordbox_m.png", p="wordbox_g.png",
                                   q="wordbox_l.png", r="wordbox_r.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_111_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=111,
                                   question="On which planet does the orb found by Quill in the Guardians of the Galaxy movie",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_h.png", c="wordbox_j.png", d="wordbox_o.png",
                                   e="wordbox_h.png", f="wordbox_d.png", g="wordbox_g.png",
                                   h="wordbox_e.png", i="wordbox_k.png", j="wordbox_m.png",
                                   k="wordbox_f.png", l="wordbox.png", m="wordbox_l.png",
                                   n="wordbox_n.png", o="wordbox_i.png", p="wordbox_r.png",
                                   q="wordbox_f.png", r="wordbox_c.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_112_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=112,
                                   question="Which stone was in the orb in the Guardians of the Galaxy movie",
                                   levelcounter=str(self.count),a="wordbox.png",
                                   b="wordbox_v.png", c="wordbox_w.png", d="wordbox_n.png",
                                   e="wordbox_t.png", f="wordbox_s.png", g="wordbox_p.png",
                                   h="wordbox_k.png", i="wordbox_r.png", j="wordbox_q.png",
                                   k="wordbox_v.png", l="wordbox_o.png", m="wordbox_l.png",
                                   n="wordbox_t.png", o="wordbox_e.png", p="wordbox_m.png",
                                   q="wordbox_d.png", r="wordbox_c.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_113_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=113,
                                   question="What is the name of the superhero that looks like a raccoon",
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
    def level_114_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=114,
                                   question="On which planet does the final fight happen in the Guardians of the Galaxy movie",
                                   levelcounter=str(self.count),a="wordbox_r.png",
                               b="wordbox_b.png",c="wordbox_l.png",d="wordbox_f.png",
                               e="wordbox_c.png",f="wordbox.png",g="wordbox_i.png",
                               h="wordbox_o.png",i="wordbox_x.png",j="wordbox_g.png",
                               k="wordbox_j.png",l="wordbox_e.png",m="wordbox_n.png",
                               n="wordbox_p.png",o="wordbox_k.png",p="wordbox_m.png",
                               q="wordbox_h.png",r="wordbox_d.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_115_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=115,
                                   question="To which planet does Quill and his group travel with the Orb in the Guardians of the Galaxy movie",
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
    def level_116_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=116,
                                   question="Whom did Quill and his group meet first on the Knowhere planet in the Guardians of the Galaxy movie",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_t.png", c="wordbox_y.png", d="wordbox_e.png",
                                   e="wordbox_i.png", f="wordbox_l.png", g="wordbox_e.png",
                                   h="wordbox_z.png", i="wordbox_o.png", j="wordbox_t.png",
                                   k="wordbox_x.png", l="wordbox_e.png", m="wordbox_n.png",
                                   n="wordbox.png", o="wordbox_v.png", p="wordbox_p.png",
                                   q="wordbox.png", r="wordbox_r.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_117_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=117,
                                   question="From which place in Earth does Yondu Udonta bring Peter Quill",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox.png", c="wordbox_i.png", d="wordbox_b.png",
                                   e="wordbox_d.png", f="wordbox_i.png", g="wordbox_g.png",
                                   h="wordbox_u.png", i="wordbox_f.png", j="wordbox_m.png",
                                   k="wordbox_e.png", l="wordbox_o.png", m="wordbox_r.png",
                                   n="wordbox_j.png", o="wordbox_h.png", p="wordbox_c.png",
                                   q="wordbox_l.png", r="wordbox_s.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_118_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=118,
                                   question="On which year does Yondu Udonta bring Quill",
                                   levelcounter=str(self.count),a="num_8.png",
                                   b="num_5.png", c="num_5.png", d="num_3.png", e="num_6.png",
                                   f="num_9.png",
                                   g="num_4.png", h="num_6.png", i="num_8.png", j="num_4.png",
                                   k="num_1.png",
                                   l="num_6.png", m="num_0.png", n="num_3.png", o="num_5.png",
                                   p="num_4.png", q="num_0.png", r="num_7.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_119_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=119,
                                   question="What is the name of Peter Quill's mother",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_r.png", c="wordbox_q.png", d="wordbox_i.png",
                                   e="wordbox_u.png", f="wordbox_e.png", g="wordbox_d.png",
                                   h="wordbox_x.png", i="wordbox_m.png", j="wordbox_h.png",
                                   k="wordbox_y.png", l="wordbox_t.png", m="wordbox_o.png",
                                   n="wordbox_p.png", o="wordbox_l.png", p="wordbox_e.png",
                                   q="wordbox_z.png", r="wordbox_i.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_120_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=120,
                                   question="From which planet does Thanos bring Gamora",
                                   levelcounter=str(self.count), a="wordbox_z.png",
                                   b="wordbox.png", c="wordbox_l.png", d="wordbox_r.png",
                                   e="wordbox_c.png", f="wordbox_e.png", g="wordbox_h.png",
                                   h="wordbox_t.png", i="wordbox_e.png", j="wordbox_f.png",
                                   k="wordbox_j.png", l="wordbox_b.png", m="wordbox_e.png",
                                   n="wordbox_d.png", o="wordbox_k.png", p="wordbox_i.png",
                                   q="wordbox_g.png", r="wordbox_o.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"
                                   )
    def level_121_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=121,
                                   question="Who killed the DRAX family",
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
    def level_122_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=122,
                                   question="What would be the superhero form name of Scot Lang",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_h.png", c="wordbox_i.png", d="wordbox_t.png",
                                   e="wordbox_x.png", f="wordbox_c.png", g="wordbox_m.png",
                                   h="wordbox_d.png", i="wordbox.png", j="wordbox_e.png",
                                   k="wordbox_f.png", l="wordbox_z.png", m="wordbox_n.png",
                                   n="wordbox_g.png", o="wordbox_y.png", p="wordbox_n.png",
                                   q="wordbox_i.png", r="wordbox.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_123_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=123,
                                   question=" What is the name of Scott Lang's daughter",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_x.png", c="wordbox.png", d="wordbox_d.png",
                                   e="wordbox_o.png", f="wordbox_s.png", g="wordbox_z.png",
                                   h="wordbox_e.png", i="wordbox_m.png", j="wordbox_i.png",
                                   k="wordbox_n.png", l="wordbox_y.png", m="wordbox_s.png",
                                   n="wordbox_p.png", o="wordbox_c.png", p="wordbox_g.png",
                                   q="wordbox_q.png", r="wordbox_l.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_124_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=124,
                                   question="What is the name of Hank Pym's daughter",
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
    def level_125_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=125,
                                   question="Who invented the Pym particles",
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
    def level_126_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=126,
                                   question="Who invented the Yellow Jacket in the Ant-Man movie",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_y.png", c="wordbox_s.png", d="wordbox_r.png",
                                   e="wordbox_b.png", f="wordbox_r.png", g="wordbox_o.png",
                                   h="wordbox_r.png", i="wordbox_p.png", j="wordbox_e.png",
                                   k="wordbox_m.png", l="wordbox_x.png", m="wordbox_c.png",
                                   n="wordbox_z.png", o="wordbox_n.png", p="wordbox_l.png",
                                   q="wordbox_s.png", r="wordbox_d.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_127_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=127,
                                   question="Name of the prison that Scott released in the Ant-Man movie",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_q.png", c="wordbox_w.png", d="wordbox_t.png",
                                   e="wordbox_d.png", f="wordbox.png", g="wordbox_s.png",
                                   h="wordbox_y.png", i="wordbox_e.png", j="wordbox_v.png",
                                   k="wordbox_z.png", l="wordbox_u.png", m="wordbox_x.png",
                                   n="wordbox_n.png", o="wordbox_r.png", p="wordbox_n.png",
                                   q="wordbox_p.png", r="wordbox_i.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_128_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=128,
                                   question="What is the name of the police officer that Scott's wife lives within ,in the Ant-Man movie",
                                   levelcounter=str(self.count), a="wordbox_z.png",
                                   b="wordbox_t.png", c="wordbox_b.png", d="wordbox_l.png",
                                   e="wordbox_p.png", f="wordbox_y.png", g="wordbox.png",
                                   h="wordbox_d.png", i="wordbox_i.png", j="wordbox_e.png",
                                   k="wordbox_h.png", l="wordbox_x.png", m="wordbox_m.png",
                                   n="wordbox_n.png", o="wordbox_f.png", p="wordbox_o.png",
                                   q="wordbox_c.png", r="wordbox_j.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_129_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=129,
                                   question="What is the name of the friend of Scott",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_j.png", c="wordbox.png", d="wordbox_p.png",
                                   e="wordbox_u.png", f="wordbox_d.png", g="wordbox_c.png",
                                   h="wordbox_l.png", i="wordbox_f.png", j="wordbox_n.png",
                                   k="wordbox_g.png", l="wordbox_o.png", m="wordbox_k.png",
                                   n="wordbox_i.png", o="wordbox_m.png", p="wordbox_b.png",
                                   q="wordbox_s.png", r="wordbox_e.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_130_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=130,
                                   question="Which country releases the missile to America in the Ant-Man movie",
                                   levelcounter=str(self.count), a="wordbox_q.png",
                                   b="wordbox_m.png", c="wordbox_i.png", d="wordbox_o.png",
                                   e="wordbox_c.png", f="wordbox_t.png", g="wordbox_s.png",
                                   h="wordbox_f.png", i="wordbox_l.png", j="wordbox_v.png",
                                   k="wordbox_n.png", l="wordbox_k.png", m="wordbox_f.png",
                                   n="wordbox_g.png", o="wordbox_m.png", p="wordbox_o.png",
                                   q="wordbox.png", r="wordbox_p.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_131_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=131,
                                   question="What is the name of Hope's mother",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_n.png", c="wordbox_t.png", d="wordbox.png",
                                   e="wordbox_e.png", f="wordbox_b.png", g="wordbox.png",
                                   h="wordbox_h.png", i="wordbox_d.png", j="wordbox_x.png",
                                   k="wordbox_p.png", l="wordbox_j.png", m="wordbox_z.png",
                                   n="wordbox_v.png", o="wordbox_e.png", p="wordbox_n.png",
                                   q="wordbox_n.png", r="wordbox_y.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_132_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=132,
                                   question="What is the name of the Avenger that Scott fights with in the Ant-Man movie",
                                   levelcounter=str(self.count), a="wordbox_c.png",
                                   b="wordbox_w.png", c="wordbox_d.png", d="wordbox_v.png",
                                   e="wordbox_y.png", f="wordbox_l.png", g="wordbox_z.png",
                                   h="wordbox_o.png", i="wordbox_h.png", j="wordbox_f.png",
                                   k="wordbox_p.png", l="wordbox_b.png", m="wordbox.png",
                                   n="wordbox_x.png", o="wordbox_g.png", p="wordbox_h.png",
                                   q="wordbox_k.png", r="wordbox_n.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_133_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=133,
                                   question="What is the superhero form name of Janet van Dyne",
                                   levelcounter=str(self.count), a="wordbox_x.png",
                                   b="wordbox_w.png", c="wordbox_y.png", d="wordbox_v.png",
                                   e="wordbox_h.png", f="wordbox_s.png", g="wordbox_b.png",
                                   h="wordbox_z.png", i="wordbox_p.png", j="wordbox_r.png",
                                   k="wordbox_q.png", l="wordbox_o.png", m="wordbox.png",
                                   n="wordbox_n.png", o="wordbox_l.png", p="wordbox_t.png",
                                   q="wordbox_m.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_134_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=134,
                                   question="What is the nickname that Scott calls the 247 ant in the Ant-Man movie",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox.png", c="wordbox_w.png", d="wordbox_l.png",
                                   e="wordbox_d.png", f="wordbox_l.png", g="wordbox_v.png",
                                   h="wordbox_x.png", i="wordbox_s.png", j="wordbox_o.png",
                                   k="wordbox_p.png", l="wordbox_i.png", m="wordbox_n.png",
                                   n="wordbox_z.png", o="wordbox_y.png", p="wordbox_n.png",
                                   q="wordbox_m.png", r="wordbox_q.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_135_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=135,
                                   question="which colour disk is used to make the objects bigger",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox_l.png", c="wordbox_z.png", d="wordbox_o.png",
                                   e="wordbox_t.png", f="wordbox_v.png", g="wordbox_y.png",
                                   h="wordbox_d.png", i="wordbox_h.png", j="wordbox_u.png",
                                   k="wordbox_g.png", l="wordbox_x.png", m="wordbox_f.png",
                                   n="wordbox_e.png", o="wordbox_z.png", p="wordbox_b.png",
                                   q="wordbox_h.png", r="wordbox.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_136_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=136,
                                   question="which colour disk is used to make the objects smaller",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_e.png", c="wordbox_f.png", d="wordbox_g.png",
                                   e="wordbox_k.png", f="wordbox_n.png", g="wordbox_c.png",
                                   h="wordbox_j.png", i="wordbox_l.png", j="wordbox_r.png",
                                   k="wordbox_x.png", l="wordbox_b.png", m="wordbox_t.png",
                                   n="wordbox_h.png", o="wordbox_d.png", p="wordbox_i.png",
                                   q="wordbox_v.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_137_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=137,
                                   question="Which fictional country do the Avengers strive to save from Ultron's threat in the Age of Ultron movie",
                                   levelcounter=str(self.count), a="wordbox_q.png",
                                   b="wordbox_m.png", c="wordbox_i.png", d="wordbox_o.png",
                                   e="wordbox_c.png", f="wordbox_t.png", g="wordbox_s.png",
                                   h="wordbox_f.png", i="wordbox_l.png", j="wordbox_v.png",
                                   k="wordbox_n.png", l="wordbox_k.png", m="wordbox_f.png",
                                   n="wordbox_g.png", o="wordbox_m.png", p="wordbox_o.png",
                                   q="wordbox.png", r="wordbox_p.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_138_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=138,
                                   question="Which stone is on the forehead of Vision",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_y.png", c="wordbox_c.png", d="wordbox_g.png",
                                   e="wordbox_b.png", f="wordbox_f.png", g="wordbox_e.png",
                                   h="wordbox_n.png", i="wordbox_d.png", j="wordbox_f.png",
                                   k="wordbox_p.png", l="wordbox_x.png", m="wordbox_h.png",
                                   n="wordbox_z.png", o="wordbox_h.png", p="wordbox_g.png",
                                   q="wordbox.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_139_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=139,
                                   question="Who gives the power to wake up the Vision in Age of Ultron movie",
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
    def level_140_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=140,
                                   question="Which Avenger was killed by Ultron in the Age of Ultron movie",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_u.png", c="wordbox_f.png", d="wordbox_v.png",
                                   e="wordbox_p.png", f="wordbox_l.png", g="wordbox_t.png",
                                   h="wordbox_r.png", i="wordbox_p.png", j="wordbox_c.png",
                                   k="wordbox_y.png", l="wordbox_s.png", m="wordbox_k.png",
                                   n="wordbox_t.png", o="wordbox_q.png", p="wordbox_e.png",
                                   q="wordbox_o.png", r="wordbox_i.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_141_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=141,
                                   question="Who can lift the Mjölnir except Thor in the Ultron movie",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_r.png", c="wordbox_v.png", d="wordbox.png",
                                   e="wordbox_t.png", f="wordbox_l.png", g="wordbox_u.png",
                                   h="wordbox_z.png", i="wordbox_i.png", j="wordbox_m.png",
                                   k="wordbox_i.png", l="wordbox_x.png", m="wordbox_o.png",
                                   n="wordbox_q.png", o="wordbox_y.png", p="wordbox_s.png",
                                   q="wordbox_b.png", r="wordbox_p.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_142_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=142,
                                   question="Who is the villain in the Avengers Age of Ultron movie",
                                   levelcounter=str(self.count), a="wordbox_x.png",
                                   b="wordbox_l.png", c="wordbox_s.png", d="wordbox_y.png",
                                   e="wordbox_v.png", f="wordbox_u.png", g="wordbox_o.png",
                                   h="wordbox_q.png", i="wordbox.png", j="wordbox_r.png",
                                   k="wordbox_c.png", l="wordbox_p.png", m="wordbox_w.png",
                                   n="wordbox_z.png", o="wordbox_t.png", p="wordbox_d.png",
                                   q="wordbox_n.png", r="wordbox_b.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_143_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=143,
                                   question="With which material was the vision made off",
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
    def level_144_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=144,
                                   question="Who helps Natasha to escape from Ultron's cage",

                                   levelcounter=str(self.count), a="wordbox_w.png",
                                   b="wordbox_s.png", c="wordbox_y.png", d="wordbox_d.png", e="wordbox_e.png",
                                   f="wordbox_f.png",
                                   g="wordbox_e.png", h="wordbox_t.png", i="wordbox_l.png", j="wordbox.png",
                                   k="wordbox_o.png",
                                   l="wordbox_p.png", m="wordbox_m.png", n="wordbox_k.png", o="wordbox_g.png",
                                   p="wordbox_x.png", q="wordbox_h.png", r="wordbox_n.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_145_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=145,
                                   question="Who can reduce the anger of Hulk",
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
    def level_146_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=146,
                                   question="What is the name of the Avenger who possesses superhuman speed in the movie Avengers Age of Ultron",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_u.png", c="wordbox_f.png", d="wordbox_v.png",
                                   e="wordbox_p.png", f="wordbox_l.png", g="wordbox_t.png",
                                   h="wordbox_r.png", i="wordbox_p.png", j="wordbox_c.png",
                                   k="wordbox_y.png", l="wordbox_s.png", m="wordbox_k.png",
                                   n="wordbox_t.png", o="wordbox_q.png", p="wordbox_e.png",
                                   q="wordbox_o.png", r="wordbox_i.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )
    def level_147_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=147,
                                   question="Which organization aids the Avengers in evacuating the civilians from the floating city in the movie Age of Ultron",
                                   levelcounter=str(self.count), a="wordbox_o.png",
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
    def level_148_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=148,
                                   question="What is the name of the character Quicksilver",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_i.png", c="wordbox_y.png", d="wordbox_t.png",
                                   e="wordbox_h.png", f="wordbox_p.png", g="wordbox.png",
                                   h="wordbox_f.png", i="wordbox_e.png", j="wordbox_x.png",
                                   k="wordbox_z.png", l="wordbox_m.png", m="wordbox_g.png",
                                   n="wordbox_r.png", o="wordbox_f.png", p="wordbox_o.png",
                                   q="wordbox_o.png", r="wordbox_m.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="bor.png", em_15="mix.png"

                                   )
    def level_149_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=149,
                                   question="What is the name of the AI system introduced by Tony Stark by replacing J.A.R.V.I.S",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_p.png", c="wordbox_b.png", d="wordbox_i.png",
                                   e="wordbox_z.png", f="wordbox_h.png", g="wordbox_k.png",
                                   h="wordbox_g.png", i="wordbox_y.png", j="wordbox_h.png",
                                   k="wordbox_j.png", l="wordbox_f.png", m="wordbox_b.png",
                                   n="wordbox_d.png", o="wordbox_c.png", p="wordbox_x.png",
                                   q="wordbox.png", r="wordbox_e.png",

                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png"

                                   )



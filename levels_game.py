from kivy.storage.jsonstore import JsonStore
import coin_inc
import allhint
class level_game_comic(coin_inc.coininc,allhint.hint_all):
    def __init__(self):
        self.counters = ["2/100", "3/100", "4/100", "5/100", "6/100", "7/100", "8/100", "9/100", "10/100", "11/100","12/100","13/100","14/100","15/100",
                         "16/100","17/100","18/100","19/100","20/100","21/100","22/100","23/100","24/100","25/100","26/100","27/100","28/100","29/100","30/100",
                         "31/100","32/100","33/100","34/100","35/100","36/100","37/100","38/100","39/100","40/100","41/100","42/100","43/100","44/100","45/100",
                         "46/100","47/100","48/100","49/100","50/100","51/100","52/100","53/100","54/100","55/100","56/100","57/100","58/100","59/100","60/100",
                         "61/100","62/100","63/100","64/100","65/100","66/100","67/100","68/100","69/100","70/100","71/100","72/100","73/100","74/100","75/100",
                         "76/100","77/100","78/100","79/100","80/100","81/100","82/100","83/100","84/100","85/100","86/100","87/100","88/100","89/100","90/100",
                         "91/100","92/100","93/100","94/100","95/100","96/100","97/100","98/100","99/100","100/100"]


    def counter(self,*args):

        lev_coun = JsonStore("counter.json")
        lst = lev_coun.get("random_level_list")["number"]
        s = lev_coun.get("random_level_list")["number"][0]

        lst.remove(s)
        lev_coun.put("random_level_list",number = lst )

        return  self.counters[s]


    def level_2_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0

        self.changing_words_blanks(level=2,
                                   question="Which character did Tony Stark play in the Marvel Cinematic Universe",
                                    levelcounter=str(self.count),a="wordbox_m.png",
                                   b="wordbox_s.png", c="wordbox_b.png", d="wordbox_j.png", e="wordbox_n.png",
                                   f="wordbox_d.png",
                                   g="wordbox_k.png", h="wordbox_r.png", i="wordbox_f.png", j="wordbox_n.png",
                                   k="wordbox_c.png",
                                   l="wordbox_s.png", m="wordbox_o.png", n="wordbox_w.png", o="wordbox.png",
                                   p="wordbox_v.png", q="wordbox_i.png", r="wordbox_d.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")

    def level_3_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=3, question="What is the name of the first AI system used by Iron Man",
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

    def level_4_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=4, question="What was the name of the first missile created by Tony Stark",
                                 levelcounter=str(self.count),a="wordbox_h.png",
                                   b="wordbox.png", c="wordbox_p.png", d="wordbox_v.png", e="wordbox_j.png",
                                   f="wordbox_s.png",
                                   g="wordbox.png", h="wordbox_m.png", i="wordbox_s.png", j="wordbox_r.png",
                                   k="wordbox_n.png",
                                   l="wordbox_o.png", m="wordbox_d.png", n="wordbox_c.png", o="wordbox_k.png",
                                   p="wordbox_i.png", q="wordbox_f.png", r="wordbox_e.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")

    def level_5_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=5, question="Who helped Tony Stark create his first suit",
                                    levelcounter=str(self.count),a="wordbox_d.png",
                                   b="wordbox_p.png", c="wordbox_n.png", d="wordbox_f.png", e="wordbox_n.png",
                                   f="wordbox_k.png",
                                   g="wordbox_j.png", h="wordbox_e.png", i="wordbox_o.png", j="wordbox_i.png",
                                   k="wordbox_b.png",
                                   l="wordbox_s.png", m="wordbox_d.png", n="wordbox.png", o="wordbox_y.png",
                                   p="wordbox_m.png", q="wordbox_t.png", r="wordbox_m.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")

    def level_6_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=6, question="In which city was Marvel Comics started",
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

    def level_7_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=7,
                                   question="Who was the editor-in-chief and publisher of Marvel Comics in the past",
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

    def level_8_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=8,
                                   question="Who is the director of S.H.I.E.L.D",
                                levelcounter=str(self.count),a="wordbox_n.png",
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

    def level_9_ref(self, *args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=9,
                                   question="What was the name of Howard Stark's best friend",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_f.png", c="wordbox_n.png", d="wordbox_o.png", e="wordbox_p.png",
                                   f="wordbox_v.png",
                                   g="wordbox_d.png", h="wordbox_n.png", i="wordbox_t.png", j="wordbox_n.png",
                                   k="wordbox_s.png",
                                   l="wordbox_g.png", m="wordbox.png", n="wordbox_d.png", o="wordbox_o.png",
                                   p="wordbox_c.png", q="wordbox.png", r="wordbox_x.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_10_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=10,
                                   question="For which country did Tony Stark supply weapons",
                                   levelcounter=str(self.count), a="wordbox_c.png",
                                   b="wordbox_k.png", c="wordbox.png", d="wordbox_p.png", e="wordbox_r.png",
                                   f="wordbox_t.png",
                                   g="wordbox_m.png", h="wordbox_s.png", i="wordbox_n.png", j="wordbox_o.png",
                                   k="wordbox_t.png",
                                   l="wordbox_i.png", m="wordbox_k.png", n="wordbox_g.png", o="wordbox_e.png",
                                   p="wordbox_v.png", q="wordbox_b.png", r="wordbox.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_11_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=11,
                                   question="What object saved Tony Stark's life",
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
    def level_12_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=12,
                                   question="What organization took Tony Stark hostage",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_f.png", c="wordbox_l.png", d="wordbox_r.png", e="wordbox_p.png",
                                   f="wordbox_o.png",
                                   g="wordbox_v.png", h="wordbox_s.png", i="wordbox_k.png", j="wordbox_t.png",
                                   k="wordbox_m.png",
                                   l="wordbox_g.png", m="wordbox_e.png", n="wordbox_j.png", o="wordbox_b.png",
                                   p="wordbox_i.png", q="wordbox_l.png", r="wordbox_n.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_13_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=13,
                                   question="What is the name of the Avenger who fights with bow and arrows",
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
    def level_14_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=14,
                                   question="What is the name of the organization that forms the Avengers team",
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
    def level_15_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=15,
                                   question="What is the name of the Avenger who attacks with thunderstorms and a hammer",
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
    def level_16_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=16,
                                   question="Who is also called the God of Mischief",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox.png", c="wordbox_e.png", d="wordbox_i.png", e="wordbox_x.png",
                                   f="wordbox_q.png",
                                   g="wordbox_o.png", h="wordbox_m.png", i="wordbox_g.png", j="wordbox_c.png",
                                   k="wordbox_d.png",
                                   l="wordbox_l.png", m="wordbox_t.png", n="wordbox.png", o="wordbox_p.png",
                                   p="wordbox_k.png", q="wordbox_m.png", r="wordbox_s.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")

    def level_17_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=17,
                                   question="What is the name of the Avenger who can't manage his anger and turns green",
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
    def level_18_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=18,
                                   question=" Who is the villain in the Avengers movie",
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
    def level_19_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=19,
                                   question="What character was shown in the end credit scene of the Avengers movie",
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
    def level_20_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=20,
                                   question="In which country was Banner hiding in incredible hulk movie",
                                   levelcounter=str(self.count), a="wordbox_z.png",
                                   b="wordbox_k.png", c="wordbox_n.png", d="wordbox_o.png", e="wordbox.png",
                                   f="wordbox_v.png",
                                   g="wordbox_d.png", h="wordbox_g.png", i="wordbox_i.png", j="wordbox_o.png",
                                   k="wordbox_b.png",
                                   l="wordbox_p.png", m="wordbox_r.png", n="wordbox_y.png", o="wordbox_u.png",
                                   p="wordbox_t.png", q="wordbox_v.png", r="wordbox_l.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_21_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=21,
                                   question="Who drinks the drink with a drop of Bruce Banner's blood in incredible hulk movie",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_k.png", c="wordbox_e.png", d="wordbox_m.png", e="wordbox_o.png",
                                   f="wordbox_e.png",
                                   g="wordbox_f.png", h="wordbox_o.png", i="wordbox_v.png", j="wordbox_l.png",
                                   k="wordbox_n.png",
                                   l="wordbox_d.png", m="wordbox.png", n="wordbox_i.png", o="wordbox_x.png",
                                   p="wordbox_s.png", q="wordbox_q.png", r="wordbox_t.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_22_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=22,
                                   question="With whom did Mr. Green chat in incredible hulk movie",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_o.png", c="wordbox_s.png", d="wordbox_b.png", e="wordbox_t.png",
                                   f="wordbox_f.png",
                                   g="wordbox_y.png", h="wordbox_q.png", i="wordbox_t.png", j="wordbox_u.png",
                                   k="wordbox_d.png",
                                   l="wordbox_g.png", m="wordbox_l.png", n="wordbox_p.png", o="wordbox_k.png",
                                   p="wordbox_c.png", q="wordbox_v.png", r="wordbox_e.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_23_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=23,
                                   question=" What is the superhero name of Bruce Banner",
                                   levelcounter=str(self.count), a="wordbox_f.png",
                                   b="wordbox_d.png", c="wordbox_k.png", d="wordbox_d.png", e="wordbox_p.png",
                                   f="wordbox_t.png",
                                   g="wordbox_x.png", h="wordbox_g.png", i="wordbox_u.png", j="wordbox_f.png",
                                   k="wordbox.png",
                                   l="wordbox_l.png", m="wordbox_h.png", n="wordbox_n.png", o="wordbox_o.png",
                                   p="wordbox_m.png", q="wordbox_b.png", r="wordbox_w.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_24_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=24,
                                   question="What is Thor's citizenship",
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
    def level_25_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=25,
                                   question="What is Thor's father's name",
                                   levelcounter=str(self.count), a="wordbox_b.png",
                                   b="wordbox_k.png", c="wordbox_t.png", d="wordbox_n.png", e="wordbox_p.png",
                                   f="wordbox_s.png",
                                   g="wordbox_i.png", h="wordbox_v.png", i="wordbox_g.png", j="wordbox_k.png",
                                   k="wordbox_l.png",
                                   l="wordbox_o.png", m="wordbox_d.png", n="wordbox_h.png", o="wordbox_m.png",
                                   p="wordbox_y.png", q="wordbox_q.png", r="wordbox_v.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_26_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=26,
                                   question=" What is the name of Thor's brother",
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
    def level_27_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=27,
                                   question="What is the name of Thor's mother",
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
    def level_28_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=28,
                                   question="What is the name of the villain in the Thor movie",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_f.png", c="wordbox_k.png", d="wordbox_p.png", e="wordbox_u.png",
                                   f="wordbox_n.png",
                                   g="wordbox_o.png", h="wordbox_s.png", i="wordbox_l.png", j="wordbox.png",
                                   k="wordbox_c.png",
                                   l="wordbox_x.png", m="wordbox_e.png", n="wordbox_b.png", o="wordbox_m.png",
                                   p="wordbox_k.png", q="wordbox_g.png", r="wordbox_y.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_29_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=29,
                                   question="How many realms did Thor protect",
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
    def level_30_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=30,
                                   question="What is the name of Thor's hammer",
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
    def level_31_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=31,
                                   question="What is the name of the gatekeeper for Asgard",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_k.png", c="wordbox_i.png", d="wordbox_e.png", e="wordbox_d.png",
                                   f="wordbox_t.png",
                                   g="wordbox_n.png", h="wordbox_l.png", i="wordbox_b.png", j="wordbox.png",
                                   k="wordbox_v.png",
                                   l="wordbox_g.png", m="wordbox_p.png", n="wordbox_l.png", o="wordbox_k.png",
                                   p="wordbox_h.png", q="wordbox_s.png", r="wordbox_m.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_32_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=32,
                                   question="What is the name of the sword used by Heimdall",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_u.png", c="wordbox_b.png", d="wordbox_t.png", e="wordbox_o.png",
                                   f="wordbox_l.png",
                                   g="wordbox_d.png", h="wordbox_q.png", i="wordbox_f.png", j="wordbox_v.png",
                                   k="wordbox_h.png",
                                   l="wordbox_m.png", m="wordbox_n.png", n="wordbox_m.png", o="wordbox_p.png",
                                   p="wordbox_k.png", q="wordbox_t.png", r="wordbox_r.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_33_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=33,
                                   question="Who protects the Mjolnir on Earth in thor movie",
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
    def level_34_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=34,
                                   question="What is the name of the bridge that connects Midgard to Asgard",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_p.png", c="wordbox_v.png", d="wordbox_f.png", e="wordbox_m.png",
                                   f="wordbox_s.png",
                                   g="wordbox_c.png", h="wordbox.png", i="wordbox_i.png", j="wordbox_l.png",
                                   k="wordbox_t.png",
                                   l="wordbox_g.png", m="wordbox_r.png", n="wordbox_q.png", o="wordbox_m.png",
                                   p="wordbox_b.png", q="wordbox_x.png", r="wordbox_m.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_35_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=35,
                                   question="Who is the most powerful person in Asgard",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_b.png", c="wordbox_o.png", d="wordbox_f.png", e="wordbox_c.png",
                                   f="wordbox_k.png",
                                   g="wordbox_n.png", h="wordbox_g.png", i="wordbox_v.png", j="wordbox_d.png",
                                   k="wordbox_q.png",
                                   l="wordbox_t.png", m="wordbox_m.png", n="wordbox_p.png", o="wordbox_i.png",
                                   p="wordbox_u.png", q="wordbox_j.png", r="wordbox_f.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_36_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=36,
                                   question="What is the name of Loki's father",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_r.png", c="wordbox_k.png", d="wordbox_f.png", e="wordbox_l.png",
                                   f="wordbox_b.png",
                                   g="wordbox.png", h="wordbox_p.png", i="wordbox_t.png", j="wordbox_v.png",
                                   k="wordbox_u.png",
                                   l="wordbox_q.png", m="wordbox.png", n="wordbox_e.png", o="wordbox_i.png",
                                   p="wordbox_o.png", q="wordbox_g.png", r="wordbox_h.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_37_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=37,
                                   question="What is the name of Loki's mother",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_t.png", c="wordbox_f.png", d="wordbox_m.png", e="wordbox_b.png",
                                   f="wordbox_k.png",
                                   g="wordbox_g.png", h="wordbox_u.png", i="wordbox_q.png", j="wordbox_y.png",
                                   k="wordbox_p.png",
                                   l="wordbox.png", m="wordbox_l.png", n="wordbox_c.png", o="wordbox_n.png",
                                   p="wordbox_e.png", q="wordbox_q.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_38_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=38,
                                   question="Who allows the Jotunheim people to enter Asgard in thor movie",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox.png", c="wordbox_q.png", d="wordbox_y.png", e="wordbox_n.png",
                                   f="wordbox_p.png",
                                   g="wordbox_k.png", h="wordbox_w.png", i="wordbox_s.png", j="wordbox_i.png",
                                   k="wordbox_t.png",
                                   l="wordbox_o.png", m="wordbox_n.png", n="wordbox.png", o="wordbox_l.png",
                                   p="wordbox_h.png", q="wordbox_t.png", r="wordbox_g.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_39_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=39,
                                   question="Who banished Thor from Asgard in thor movie",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_k.png", c="wordbox_d.png", d="wordbox_t.png", e="wordbox_p.png",
                                   f="wordbox_q.png",
                                   g="wordbox_o.png", h="wordbox_l.png", i="wordbox_n.png", j="wordbox_m.png",
                                   k="wordbox_p.png",
                                   l="wordbox_s.png", m="wordbox_x.png", n="wordbox_u.png", o="wordbox_i.png",
                                   p="wordbox_g.png", q="wordbox_f.png", r="wordbox_p.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_40_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=40,
                                   question="What is the name of the heroine character in the Thor movie",
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
    def level_41_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=41,
                                   question="On which planet did Thor first meet Jane Foster in Thor movie",
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
    def level_42_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=42,
                                   question="What is the name of the university where Betty Ross and Bruce Banner worked together",
                                   levelcounter=str(self.count), a="wordbox_u.png",
                                   b="wordbox_t.png", c="wordbox_k.png", d="wordbox_p.png", e="wordbox_o.png",
                                   f="wordbox_l.png",
                                   g="wordbox_g.png", h="wordbox_v.png", i="wordbox_m.png", j="wordbox_k.png",
                                   k="wordbox_f.png",
                                   l="wordbox_c.png", m="wordbox_e.png", n="wordbox_m.png", o="wordbox_r.png",
                                   p="wordbox_q.png", q="wordbox_o.png", r="wordbox_b.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_43_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=43,
                                   question="What is the name of the university that Banner wants to go to",
                                   levelcounter=str(self.count), a="wordbox_u.png",
                                   b="wordbox_t.png", c="wordbox_k.png", d="wordbox_p.png", e="wordbox_o.png",
                                   f="wordbox_l.png",
                                   g="wordbox_g.png", h="wordbox_v.png", i="wordbox_m.png", j="wordbox_k.png",
                                   k="wordbox_f.png",
                                   l="wordbox_c.png", m="wordbox_e.png", n="wordbox_m.png", o="wordbox_r.png",
                                   p="wordbox_q.png", q="wordbox_o.png", r="wordbox_b.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_44_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=44,
                                   question="Which radiation was Bruce Banner exposed to",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_m.png", c="wordbox_f.png", d="wordbox.png", e="wordbox_p.png",
                                   f="wordbox_s.png",
                                   g="wordbox_k.png", h="wordbox_l.png", i="wordbox_m.png", j="wordbox_d.png",
                                   k="wordbox_s.png",
                                   l="wordbox_u.png", m="wordbox.png", n="wordbox_b.png", o="wordbox_q.png",
                                   p="wordbox_g.png", q="wordbox_c.png", r="wordbox_v.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_45_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=45,
                                   question="Who played the role of Bruce Banner in The Incredible Hulk movie",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_l.png", c="wordbox_r.png", d="wordbox_p.png", e="wordbox_n.png",
                                   f="wordbox_k.png",
                                   g="wordbox_r.png", h="wordbox_t.png", i="wordbox_f.png", j="wordbox_d.png",
                                   k="wordbox_n.png",
                                   l="wordbox_d.png", m="wordbox_o.png", n="wordbox_m.png", o="wordbox_w.png",
                                   p="wordbox_v.png", q="wordbox_o.png", r="wordbox_e.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_46_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=46,
                                   question="Who came to Thaddeus Ross to discuss the team formation in The Incredible Hulk movie",
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
    def level_47_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=47,
                                   question="What is the name of the heroine character in The Incredible Hulk movie",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_k.png", c="wordbox_o.png", d="wordbox_m.png", e="wordbox_b.png",
                                   f="wordbox_t.png",
                                   g="wordbox_s.png", h="wordbox_p.png", i="wordbox_e.png", j="wordbox_q.png",
                                   k="wordbox_y.png",
                                   l="wordbox_u.png", m="wordbox_v.png", n="wordbox_r.png", o="wordbox_g.png",
                                   p="wordbox_c.png", q="wordbox_m.png", r="wordbox_s.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_48_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=48,
                                   question="What is the name of the scientist who works with Bruce Banner in the Incredible Hulk movie",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_k.png", c="wordbox_o.png", d="wordbox_m.png", e="wordbox_b.png",
                                   f="wordbox_t.png",
                                   g="wordbox_s.png", h="wordbox_p.png", i="wordbox_e.png", j="wordbox_q.png",
                                   k="wordbox_y.png",
                                   l="wordbox_u.png", m="wordbox_v.png", n="wordbox_r.png", o="wordbox_g.png",
                                   p="wordbox_c.png", q="wordbox_m.png", r="wordbox_s.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_49_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=49,
                                   question="What is the name of the villain in The Incredible Hulk movie",
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
    def level_50_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=50,
                                   question="Where does Laufey lives",
                                   levelcounter=str(self.count), a="wordbox_h.png",
                                   b="wordbox_k.png", c="wordbox_i.png", d="wordbox_p.png", e="wordbox_q.png",
                                   f="wordbox_u.png",
                                   g="wordbox_e.png", h="wordbox_b.png", i="wordbox_n.png", j="wordbox_l.png",
                                   k="wordbox_t.png",
                                   l="wordbox_c.png", m="wordbox_m.png", n="wordbox_g.png", o="wordbox_o.png",
                                   p="wordbox_c.png", q="wordbox.png", r="wordbox_j.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_51_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=51,
                                   question="What is the name of the actor who plays the role of General Thaddeus Ross in the Incredible Hulk movie",
                                   levelcounter=str(self.count), a="wordbox_r.png",
                                   b="wordbox_p.png", c="wordbox_i.png", d="wordbox_s.png", e="wordbox_l.png",
                                   f="wordbox_u.png",
                                   g="wordbox_q.png", h="wordbox.png", i="wordbox_o.png", j="wordbox_h.png",
                                   k="wordbox_c.png",
                                   l="wordbox_t.png", m="wordbox_w.png", n="wordbox_k.png", o="wordbox_m.png",
                                   p="wordbox_i.png", q="wordbox_o.png", r="wordbox_l.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_52_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=52,
                                   question="Who transformed into Abomination in The Incredible Hulk movie",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_t.png", c="wordbox_k.png", d="wordbox_n.png", e="wordbox_p.png",
                                   f="wordbox_m.png",
                                   g="wordbox_l.png", h="wordbox_c.png", i="wordbox_s.png", j="wordbox_g.png",
                                   k="wordbox_d.png",
                                   l="wordbox_l.png", m="wordbox_b.png", n="wordbox_q.png", o="wordbox_e.png",
                                   p="wordbox_y.png", q="wordbox_c.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_53_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=53,
                                   question="Who helps Bruce Banner to cure the Hulk formation in The Incredible Hulk movie",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox_c.png", c="wordbox_t.png", d="wordbox_o.png", e="wordbox_e.png",
                                   f="wordbox_n.png",
                                   g="wordbox_e.png", h="wordbox_p.png", i="wordbox_s.png", j="wordbox_g.png",
                                   k="wordbox.png",
                                   l="wordbox_s.png", m="wordbox_s.png", n="wordbox_b.png", o="wordbox_u.png",
                                   p="wordbox_r.png", q="wordbox_f.png", r="wordbox_l.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_54_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=54,
                                   question="What is the name of the army general in The Incredible Hulk movie",
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
    def level_55_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=55,
                                   question="What is the name of Betty Ross's father in The Incredible Hulk movie",
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
    def level_56_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=56,
                                   question="What is the name of the normal form of the Abomination in The Incredible Hulk movie",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_t.png", c="wordbox_k.png", d="wordbox_n.png", e="wordbox_p.png",
                                   f="wordbox_m.png",
                                   g="wordbox_l.png", h="wordbox_c.png", i="wordbox_s.png", j="wordbox_g.png",
                                   k="wordbox_d.png",
                                   l="wordbox_l.png", m="wordbox_b.png", n="wordbox_q.png", o="wordbox_e.png",
                                   p="wordbox_y.png", q="wordbox_c.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_57_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=57,
                                   question="In which city does the space portal was opened in the Avengers movie",
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
    def level_58_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=58,
                                   question="What is the name of the stone that Loki has in the Avengers movie",
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
    def level_59_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=59,
                                   question="Who sacrifices his life in the Avengers movie to save Newyork from a missile",
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
    def level_60_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=60,
                                   question="What is the name of the Thanos army",
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
    def level_61_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=61,
                                   question="What is the name of the Avenger who fights with a armor in the Avengers movie",
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
    def level_62_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=62,
                                   question="What is the name of the tree that protects the world in the caption america the first avanger movie",
                                   levelcounter=str(self.count), a="wordbox_d.png",
                                   b="wordbox_o.png", c="wordbox_i.png", d="wordbox_k.png", e="wordbox_c.png",
                                   f="wordbox_g.png",
                                   g="wordbox_y.png", h="wordbox_r.png", i="wordbox_f.png", j="wordbox_g.png",
                                   k="wordbox_j.png",
                                   l="wordbox_q.png", m="wordbox_t.png", n="wordbox_k.png", o="wordbox.png",
                                   p="wordbox_n.png", q="wordbox_l.png", r="wordbox_s.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_63_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=63,
                                   question="What is the name of the stone that Hitler searched for in the caption america the first avanger movie",
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
    def level_64_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=64,
                                   question="What is the name of the person in S.H.I.E.L.D. who has a single eye",
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
    def level_65_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=65,
                                   question="What is the name of the villain group in Captain America the first Avenger movie",
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
    def level_66_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=66,
                                   question="What is the name of the villain in Captain America the first Avenger movie",
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
    def level_67_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=67,
                                   question="What is the name of the material that Captain America's shield is made of",
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
    def level_68_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=68,
                                   question="What is the name of the doctor who worked for Red Skull",
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
    def level_69_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=69,
                                   question="How many doses of the Super Soldier Serum were injected into Steve Rogers",
                                   levelcounter=str(self.count), a="wordbox_x.png",
                                   b="wordbox_q.png", c="wordbox_o.png", d="wordbox_t.png", e="wordbox_p.png",
                                   f="wordbox_l.png",
                                   g="wordbox_m.png", h="wordbox_s.png", i="wordbox_n.png", j="wordbox_k.png",
                                   k="wordbox_e.png",
                                   l="wordbox_k.png", m="wordbox.png", n="wordbox_z.png", o="wordbox_l.png",
                                   p="wordbox_s.png", q="wordbox_q.png", r="wordbox_t.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_70_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=70,
                                  question="What is the name of Steve Rogers' girlfriend",
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
    def level_71_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=71,
                                   question="What is the name of Steve Rogers' best friend",
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
    def level_72_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=72,
                                   question="When was Marvel Comics discovered",
                                   levelcounter=str(self.count), a="num_0.png",
                                   b="num_7.png", c="num_4.png", d="num_7.png", e="num_2.png",
                                   f="num_1.png",
                                   g="num_6.png", h="num_9.png", i="num_8.png", j="num_4.png",
                                   k="num_5.png",
                                   l="num_8.png", m="num_7.png", n="num_3.png", o="num_0.png",
                                   p="num_2.png", q="num_5.png", r="num_9.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_73_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=73,
                                   question="When was The Incredible Hulk movie released",
                                   levelcounter=str(self.count), a="num_0.png",
                                   b="num_7.png", c="num_1.png", d="num_7.png", e="num_3.png",
                                   f="num_5.png",
                                   g="num_4.png", h="num_3.png", i="num_2.png", j="num_6.png",
                                   k="num_1.png",
                                   l="num_0.png", m="num_8.png", n="num_9.png", o="num_1.png",
                                   p="num_5.png", q="num_6.png", r="num_3.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_74_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=74,
                                   question="How many years was Captain America in sleep in ice",
                                   levelcounter=str(self.count), a="num_7.png",
                                   b="num_1.png", c="num_2.png", d="num_4.png", e="num_5.png",
                                   f="num_9.png",
                                   g="num_6.png", h="num_6.png", i="num_5.png", j="num_5.png",
                                   k="num_9.png",
                                   l="num_0.png", m="num_6.png", n="num_3.png", o="num_9.png",
                                   p="num_8.png", q="num_3.png", r="num_2.png",
                                   em_1="bor.png", em_2="bor.png", em_3="mix.png", em_4="mix.png", em_5="mix.png",
                                   em_6="mix.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_75_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=75,
                                   question="Who is the villain in the movie iron man2",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_p.png", c="wordbox.png", d="wordbox_q.png", e="wordbox_v.png",
                                   f="wordbox_t.png",
                                   g="wordbox.png", h="wordbox_s.png", i="wordbox_v.png", j="wordbox_b.png",
                                   k="wordbox_k.png",
                                   l="wordbox_d.png", m="wordbox_o.png", n="wordbox_m.png", o="wordbox_n.png",
                                   p="wordbox_f.png", q="wordbox_c.png", r="wordbox_n.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_76_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=76,
                                   question="In which city was the stark headquarters set up in the movie ironman 2",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_p.png", c="wordbox_f.png", d="wordbox_t.png", e="wordbox_i.png",
                                   f="wordbox_d.png",
                                   g="wordbox_o.png", h="wordbox_m.png", i="wordbox_i.png", j="wordbox_r.png",
                                   k="wordbox_h.png",
                                   l="wordbox_l.png", m="wordbox_c.png", n="wordbox_g.png", o="wordbox_n.png",
                                   p="wordbox_q.png", q="wordbox.png", r="wordbox_s.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_77_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=77,
                                   question="In the movie iron man 2, whom did Tony Stark appointed as the CEO of star industries",
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
    def level_78_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=78,
                                   question="Who was Tony Stark's personal assistant in Iron man 1 movie",
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
    def level_79_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=79,
                                   question="Who is the father of ivan Vanko",
                                   levelcounter=str(self.count), a="wordbox_k.png",
                                   b="wordbox_f.png", c="wordbox_n.png", d="wordbox_o.png", e="wordbox_p.png",
                                   f="wordbox_v.png",
                                   g="wordbox_d.png", h="wordbox_n.png", i="wordbox_t.png", j="wordbox_n.png",
                                   k="wordbox_s.png",
                                   l="wordbox_g.png", m="wordbox.png", n="wordbox_d.png", o="wordbox_o.png",
                                   p="wordbox_c.png", q="wordbox.png", r="wordbox_x.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_80_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=80,
                                   question="In which city does Ivan Vanko live in iron man 2 movie",
                                   levelcounter=str(self.count), a="wordbox_w.png",
                                   b="wordbox_k.png", c="wordbox_s.png", d="wordbox_t.png", e="wordbox_g.png",
                                   f="wordbox_q.png",
                                   g="wordbox_v.png", h="wordbox_o.png", i="wordbox_q.png", j="wordbox_m.png",
                                   k="wordbox_x.png",
                                   l="wordbox_o.png", m="wordbox_b.png", n="wordbox_n.png", o="wordbox_c.png",
                                   p="wordbox_e.png", q="wordbox_y.png", r="wordbox_r.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_81_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=81,
                                   question="What is the name of the race in which tony stark participated in iron man 2",
                                   levelcounter=str(self.count), a="wordbox_g.png",
                                   b="wordbox_m.png", c="wordbox_r.png", d="wordbox_t.png", e="wordbox_p.png",
                                   f="wordbox_v.png",
                                   g="wordbox_u.png", h="wordbox_r.png", i="wordbox_o.png", j="wordbox_i.png",
                                   k="wordbox_c.png",
                                   l="wordbox.png", m="wordbox_d.png", n="wordbox_f.png", o="wordbox_x.png",
                                   p="wordbox_s.png", q="wordbox_n.png", r="wordbox_h.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_82_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=82,
                                   question="The Grad prix race is started in which city",
                                   levelcounter=str(self.count), a="wordbox_p.png",
                                   b="wordbox_n.png", c="wordbox_t.png", d="wordbox_o.png", e="wordbox_q.png",
                                   f="wordbox_s.png",
                                   g="wordbox_s.png", h="wordbox_q.png", i="wordbox_o.png", j="wordbox_h.png",
                                   k="wordbox_c.png",
                                   l="wordbox_d.png", m="wordbox.png", n="wordbox_f.png", o="wordbox_l.png",
                                   p="wordbox_p.png", q="wordbox_m.png", r="wordbox_s.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_83_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=83,
                                   question="What is the name of Justin Hammer's company in ironman 2",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox_p.png", c="wordbox_n.png", d="wordbox.png", e="wordbox_h.png",
                                   f="wordbox_v.png",
                                   g="wordbox_o.png", h="wordbox_c.png", i="wordbox_t.png", j="wordbox_e.png",
                                   k="wordbox_b.png",
                                   l="wordbox_l.png", m="wordbox_r.png", n="wordbox_n.png", o="wordbox_q.png",
                                   p="wordbox_s.png", q="wordbox_o.png", r="wordbox_m.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="mix.png",
                                   em_8="mix.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_84_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=84,
                                   question="Who is Tony Stark new personal assistant in the iron man 2 movie",
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
    def level_85_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=85,
                                   question="Which organization does Natasha Romanoff work for",
                                   levelcounter=str(self.count),  a="wordbox_o.png",
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
    def level_86_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=86,
                                   question="What is the alternate name of the Natasha Romanoff",
                                   levelcounter=str(self.count), a="wordbox_w.png",
                                   b="wordbox_p.png", c="wordbox_i.png", d="wordbox_s.png", e="wordbox_b.png",
                                   f="wordbox_v.png",
                                   g="wordbox_d.png", h="wordbox_m.png", i="wordbox.png", j="wordbox_h.png",
                                   k="wordbox_t.png",
                                   l="wordbox_k.png", m="wordbox_w.png", n="wordbox_f.png", o="wordbox_c.png",
                                   p="wordbox_l.png", q="wordbox_o.png", r="wordbox_p.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_87_ref(self,*args):

        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=87,
                                   question="What is the name of the Avenger who is the best friend of Clint Barton",
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
    def level_88_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=88,
                                   question="Who is Tony Stark's father",
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
    def level_89_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=89,
                                   question="Who is Tony Stark's best friend",
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
    def level_90_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=90,
                                   question="What was the name of the S.H.I.E.L.D. agent that traveled with Tony Stark in the Iron Man 1 movie",
                                   levelcounter=str(self.count), a="wordbox_l.png",
                                   b="wordbox_m.png", c="wordbox_o.png", d="wordbox_d.png", e="wordbox_i.png",
                                   f="wordbox_o.png",
                                   g="wordbox_f.png", h="wordbox_u.png", i="wordbox_p.png", j="wordbox_h.png",
                                   k="wordbox_q.png",
                                   l="wordbox_v.png", m="wordbox_k.png", n="wordbox_c.png", o="wordbox_n.png",
                                   p="wordbox_m.png", q="wordbox_s.png", r="wordbox_l.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_91_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=91,
                                   question="Who conducted the experiment on Steve Rogers",
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
    def level_92_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=92,
                                   question="What material is used to make Captain America's suit",
                                   levelcounter=str(self.count), a="wordbox_m.png",
                                   b="wordbox_k.png", c="wordbox_r.png", d="wordbox_t.png", e="wordbox_n.png",
                                   f="wordbox_o.png",
                                   g="wordbox_c.png", h="wordbox_l.png", i="wordbox_v.png", j="wordbox.png",
                                   k="wordbox_u.png",
                                   l="wordbox_p.png", m="wordbox_d.png", n="wordbox_s.png", o="wordbox_u.png",
                                   p="wordbox_o.png", q="wordbox_i.png", r="wordbox_w.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_93_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=93,
                                   question="Who accepted Steve Rogers' army application",
                                   levelcounter=str(self.count), a="wordbox.png",
                                   b="wordbox_b.png", c="wordbox_e.png", d="wordbox_l.png", e="wordbox_r.png",
                                   f="wordbox_k.png",
                                   g="wordbox_f.png", h="wordbox_m.png", i="wordbox.png", j="wordbox_h.png",
                                   k="wordbox_s.png",
                                   l="wordbox_p.png", m="wordbox_r.png", n="wordbox_c.png", o="wordbox_e.png",
                                   p="wordbox_i.png", q="wordbox.png", r="wordbox_n.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="bor.png", em_15="mix.png")
    def level_94_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=94,
                                   question="What is the name of the serum that was injected into Steve Rogers",
                                   levelcounter=str(self.count), a="wordbox_o.png",
                                   b="wordbox_s.png", c="wordbox_i.png", d="wordbox_e.png", e="wordbox_k.png",
                                   f="wordbox_t.png",
                                   g="wordbox_v.png", h="wordbox_e.png", i="wordbox_s.png", j="wordbox_r.png",
                                   k="wordbox_l.png",
                                   l="wordbox_m.png", m="wordbox_u.png", n="wordbox_d.png", o="wordbox_r.png",
                                   p="wordbox_h.png", q="wordbox_p.png", r="wordbox_q.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_95_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=95,
                                   question="What is the name of Captain America",
                                   levelcounter=str(self.count), a="wordbox_t.png",
                                   b="wordbox_c.png", c="wordbox_e.png", d="wordbox_r.png", e="wordbox_v.png",
                                   f="wordbox_p.png",
                                   g="wordbox_g.png", h="wordbox_s.png", i="wordbox_k.png", j="wordbox_s.png",
                                   k="wordbox_m.png",
                                   l="wordbox_e.png", m="wordbox_h.png", n="wordbox_r.png", o="wordbox_e.png",
                                   p="wordbox_j.png", q="wordbox_n.png", r="wordbox_o.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_96_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=96,
                                   question="What element caused the deterioration of Tony Stark in Iron Man 2",
                                   levelcounter=str(self.count), a="wordbox_i.png",
                                   b="wordbox_k.png", c="wordbox.png", d="wordbox_f.png", e="wordbox_o.png",
                                   f="wordbox_u.png",
                                   g="wordbox_l.png", h="wordbox_n.png", i="wordbox_d.png", j="wordbox_q.png",
                                   k="wordbox_v.png",
                                   l="wordbox.png", m="wordbox_p.png", n="wordbox_t.png", o="wordbox_l.png",
                                   p="wordbox_s.png", q="wordbox_g.png", r="wordbox_m.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_97_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=97,
                                   question="What is the name of the material invented by the tony stark as the alternative to Palladiunm",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_u.png", c="wordbox_p.png", d="wordbox_c.png", e="wordbox_o.png",
                                   f="wordbox_s.png",
                                   g="wordbox_b.png", h="wordbox_k.png", i="wordbox.png", j="wordbox_d.png",
                                   k="wordbox_v.png",
                                   l="wordbox_t.png", m="wordbox_m.png", n="wordbox_f.png", o="wordbox_g.png",
                                   p="wordbox_i.png", q="wordbox.png", r="wordbox_l.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")
    def level_98_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=98,
                                   question="Who is the bodyguard to Tony Stark in the iron man 2 ",
                                   levelcounter = str(self.count), a="wordbox_t.png",
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
    def level_99_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=99,
                                   question="What is the Profession of Jane Forster in the Thor Movie",
                                   levelcounter=str(self.count), a="wordbox_s.png",
                                   b="wordbox_o.png", c="wordbox_k.png", d="wordbox_i.png", e="wordbox_r.png",
                                   f="wordbox_t.png",
                                   g="wordbox_c.png", h="wordbox.png", i="wordbox_l.png", j="wordbox_s.png",
                                   k="wordbox_h.png",
                                   l="wordbox_b.png", m="wordbox_t.png", n="wordbox_v.png", o="wordbox_p.png",
                                   p="wordbox_i.png", q="wordbox_y.png", r="wordbox_s.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="bor.png", em_10="bor.png", em_11="bor.png", em_12="bor.png",
                                   em_13="bor.png", em_14="bor.png", em_15="mix.png")
    def level_100_ref(self,*args):
        self.count = self.counter()
        self.win_coin()
        allhint.hint_all.iq_logic(self)
        self.hint_count = 0
        self.changing_words_blanks(level=100,
                                   question="In Which Regiment does Bucky get a job in the army in Captain America The First Avenger",
                                   levelcounter=str(self.count), a="wordbox_n.png",
                                   b="wordbox_o.png", c="wordbox_t.png", d="wordbox_p.png", e="wordbox_y.png",
                                   f="wordbox_q.png",
                                   g="wordbox_i.png", h="wordbox_s.png", i="wordbox_u.png", j="wordbox_l.png",
                                   k="wordbox_f.png",
                                   l="wordbox_k.png", m="wordbox_c.png", n="wordbox_r.png", o="wordbox_k.png",
                                   p="wordbox.png", q="wordbox_b.png", r="wordbox_n.png",
                                   em_1="bor.png", em_2="bor.png", em_3="bor.png", em_4="bor.png", em_5="bor.png",
                                   em_6="bor.png", em_7="bor.png",
                                   em_8="bor.png", em_9="mix.png", em_10="mix.png", em_11="mix.png", em_12="mix.png",
                                   em_13="mix.png", em_14="mix.png", em_15="mix.png")






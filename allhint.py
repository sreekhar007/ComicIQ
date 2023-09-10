from kivy.storage.jsonstore import JsonStore
class hint_all():
    def __init__(self):
        pass

    def hintff(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,lst):
        if  self.coin_js.get("coin_base")["coins"] != 0:

            if self.hint_count == lst[0]:

                    self.hint_usage()

                    self.lab.text = a



            elif self.hint_count == lst[1]:
                self.hint_usage()
                self.lab.text = b


            elif self.hint_count == lst[2]:
                self.hint_usage()
                self.lab.text = c



            elif self.hint_count == lst[3]:
                 self.hint_usage()
                 self.lab.text = d


            elif self.hint_count == lst[4]:
                self.hint_usage()
                self.lab.text = e


            elif self.hint_count == lst[5]:
                self.hint_usage()
                self.lab.text = f


            elif self.hint_count == lst[6]:
                self.hint_usage()
                self.lab.text = g
            elif self.hint_count == lst[7]:
                self.hint_usage()
                self.lab.text = h
            elif self.hint_count == lst[8]:
                self.hint_usage()
                self.lab.text = i
            elif self.hint_count == lst[9]:
                self.hint_usage()
                self.lab.text = j
            elif self.hint_count == lst[10]:
                self.hint_usage()
                self.lab.text = k
            elif self.hint_count == lst[11]:
                self.hint_usage()
                self.lab.text = l
            elif self.hint_count == lst[12]:
                self.hint_usage()
                self.lab.text = m
            elif self.hint_count == lst[13]:
                self.hint_usage()
                self.lab.text = n
            elif self.hint_count == lst[14]:
                self.hint_usage()
                self.lab.text = o


            else:
                self.lab.text = "No more Hints in This Level"
        else:
            self.lab.text = "Not Enough Coins"

    def hint_usage(self):
        self.coin_js = JsonStore("coins_win.json")

        self.ref_coin = int(self.ids.coins.text) - 5
        print(self.ref_coin)
        self.coin_js.put("coin_base", coins=self.ref_coin)
        self.ids.coins.text = str(self.coin_js.get("coin_base")["coins"])
    def iq_logic(self):
        print("hints used",self.hint_count)
        self.percent = self.hint_count * 2
        self.iq = self.percent/100 * 5
        self.iqscore = 5 - self.iq
        self.js_iq = JsonStore("iq_score.json")
        self.all_iq = self.iqscore + int(self.js_iq.get("iq_score")["score"])
        self.js_iq.put("iq_score",score = self.all_iq)
        self.ids.iq.text = str(self.js_iq.get("iq_score")["score"])


        print(self.iqscore)

    def hint_phase1(self):
        self.t = "No More Hints in This Level"
        if self.level == 1:
            self.hintff(a="C", b="H", c="R", d="I", e="S", f="E", g="V", h="A", i="N", j="S", k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])

        elif self.level == 2:
            self.hintff(a="I", b="R", c="O", d="N", e="M", f="A", g="N", h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 3:
            self.hintff(a="J", b="A", c="R", d="V", e="I", f="S", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 4:
            self.hintff(a="J", b="E", c="R", d="I", e="C", f="H", g="O", h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 5:
            self.hintff(a="Y", b="I", c="N", d="S", e="E", f="N", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 6:
            self.hintff(a="N", b="E", c="W", d="Y", e="O", f="R", g="K", h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 7:
            self.hintff(a="S", b="T", c="A", d="N", e="L", f="E", g="E", h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 8:
            self.hintff(a="N", b="I", c="C", d="K", e="F", f="U", g="R", h="Y", i=self.t, j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 9:
            self.hintff(a="A", b="N", c="T", d="O", e="N", f="V", g="A", h="N", i="K", j="O", k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 10:
            self.hintff(a="A", b="M", c="E", d="R", e="I", f="C", g="A", h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 11:
            self.hintff(a="A", b="R", c="C", d="R", e="E", f="A", g="C", h="T", i="O", j="R", k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 12:
            self.hintff(a="T", b="E", c="N", d="R", e="I", f="N", g="G", h="S", i=self.t, j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 13:
            self.hintff(a="H", b="A", c="W", d="K", e="E", f="Y", g="E", h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 14:
            self.hintff(a="S", b="H", c="I", d="E", e="L", f="D", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 15:
            self.hintff(a="T", b="H", c="O", d="R", e=self.t, f=self.t, g=self.t, h=self.t, i=self.t, j=self.t,
                        k=self.t, l=self.t, m=self.t, n=self.t, o=self.t,
                        lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 16:
            self.hintff(a="L", b="O", c="K", d="I", e=self.t, f=self.t, g=self.t, h=self.t, i=self.t, j=self.t,
                        k=self.t, l=self.t, m=self.t, n=self.t, o=self.t,
                        lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 17:
            self.hintff(a="H", b="U", c="L", d="K", e=self.t, f=self.t, g=self.t, h=self.t, i=self.t, j=self.t,
                        k=self.t, l=self.t, m=self.t, n=self.t, o=self.t,
                        lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 18:
            self.hintff(a="L", b="O", c="K", d="I", e=self.t, f=self.t, g=self.t, h=self.t, i=self.t, j=self.t,
                        k=self.t, l=self.t, m=self.t, n=self.t, o=self.t,
                        lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 19:
            self.hintff(a="T", b="H", c="A", d="N", e="O", f="S", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 20:
            self.hintff(a="B", b="R", c="A", d="Z", e="I", f="L", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 21:
            self.hintff(a="S", b="T", c="A", d="N", e="L", f="E", g="E", h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 22:
            self.hintff(a="B", b="L", c="U", d="E", e=self.t, f=self.t, g=self.t, h=self.t, i=self.t, j=self.t,
                        k=self.t, l=self.t, m=self.t, n=self.t, o=self.t,
                        lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 23:
            self.hintff(a="H", b="U", c="L", d="K", e=self.t, f=self.t, g=self.t, h=self.t, i=self.t, j=self.t,
                        k=self.t, l=self.t, m=self.t, n=self.t, o=self.t,
                        lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 24:
            self.hintff(a="A", b="S", c="G", d="A", e="R", f="D", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 25:
            self.hintff(a="O", b="D", c="I", d="I", e="N", f=self.t, g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 26:
            self.hintff(a="L", b="O", c="K", d="I", e=self.t, f=self.t, g=self.t, h=self.t, i=self.t, j=self.t,
                        k=self.t, l=self.t, m=self.t, n=self.t, o=self.t,
                        lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 27:
            self.hintff(a="F", b="R", c="I", d="G", e="G", f="A", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 28:
            self.hintff(a="L", b="A", c="U", d="F", e="E", f="Y", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 29:
            self.hintff(a="N", b="I", c="N", d="E", e=self.t, f=self.t, g=self.t, h=self.t, i=self.t, j=self.t,
                        k=self.t, l=self.t, m=self.t, n=self.t, o=self.t,
                        lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 30:
            self.hintff(a="M", b="J", c="O", d="L", e="N", f="I", g="R", h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 31:
            self.hintff(a="H", b="E", c="I", d="M", e="D", f="A", g="L", h="L", i=self.t, j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 32:
            self.hintff(a="H", b="O", c="F", d="U", e="N", f="D", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 33:
            self.hintff(a="S", b="H", c="I", d="E", e="L", f="D", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 34:
            self.hintff(a="B", b="I", c="F", d="R", e="O", f="S", g="T", h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 35:
            self.hintff(a="O", b="D", c="I", d="N", e=self.t, f=self.t, g=self.t, h=self.t, i=self.t, j=self.t,
                        k=self.t, l=self.t, m=self.t, n=self.t, o=self.t,
                        lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 36:
            self.hintff(a="F", b="A", c="R", d="B", e="A", f="U", g="T", h="I", i=self.t, j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 37:
            self.hintff(a="L", b="A", c="U", d="F", e="E", f="Y", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 38:
            self.hintff(a="L", b="O", c="K", d="I", e=self.t, f=self.t, g=self.t, h=self.t, i=self.t, j=self.t,
                        k=self.t, l=self.t, m=self.t, n=self.t, o=self.t,
                        lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 39:
            self.hintff(a="O", b="D", c="I", d="N", e=self.t, f=self.t, g=self.t, h=self.t, i=self.t, j=self.t,
                        k=self.t, l=self.t, m=self.t, n=self.t, o=self.t,
                        lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 40:
            self.hintff(a="J", b="A", c="N", d="E", e="F", f="O", g="S", h="T", i="E", j="R", k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 41:
            self.hintff(a="E", b="A", c="R", d="T", e="H", f=self.t, g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 42:
            self.hintff(a="C", b="U", c="L", d="V", e="E", f="R", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 43:
            self.hintff(a="C", b="U", c="L", d="V", e="E", f="R", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 44:
            self.hintff(a="G", b="A", c="M", d="M", e="A", f=self.t, g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 45:
            self.hintff(a="E", b="D", c="W", d="A", e="R", f="D", g="N", h="O", i="R", j="T", k="O", l="N", m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 46:
            self.hintff(a="T", b="O", c="N", d="Y", e="S", f="T", g="A", h="R", i="K", j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 47:
            self.hintff(a="B", b="E", c="T", d="T", e="Y", f="R", g="O", h="S", i="S", j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 48:
            self.hintff(a="B", b="E", c="T", d="T", e="Y", f="R", g="O", h="S", i="S", j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 49:
            self.hintff(a="A", b="B", c="O", d="M", e="I", f="N", g="A", h="T", i="I", j="O", k="N", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 50:
            self.hintff(a="J", b="O", c="T", d="U", e="N", f="H", g="E", h="I", i="M", j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 51:
            self.hintff(a="W", b="I", c="L", d="L", e="A", f="M", g="H", h="U", i="R", j="T", k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 52:
            self.hintff(a="E", b="M", c="I", d="L", e="B", f="L", g="O", h="N", i="S", j="K", k="Y", l=self.t, m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 53:
            self.hintff(a="S", b="A", c="M", d="U", e="E", f="L", g="S", h="T", i="E", j="R", k="N", l="S", m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 54:
            self.hintff(a="T", b="H", c="A", d="D", e="D", f="E", g="U", h="S", i="R", j="O", k="S", l="S", m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 55:
            self.hintff(a="T", b="H", c="A", d="D", e="D", f="E", g="U", h="S", i="R", j="O", k="S", l="S", m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 56:
            self.hintff(a="E", b="M", c="I", d="L", e="B", f="L", g="O", h="N", i="S", j="K", k="Y", l=self.t, m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 57:
            self.hintff(a="N", b="E", c="W", d="Y", e="O", f="R", g="K", h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 58:
            self.hintff(a="T", b="E", c="S", d="S", e="E", f="R", g="A", h="C", i="T", j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 59:
            self.hintff(a="I", b="R", c="O", d="N", e="M", f="A", g="N", h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 60:
            self.hintff(a="C", b="H", c="I", d="T", e="A", f="U", g="R", h="I", i=self.t, j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 61:
            self.hintff(a="I", b="R", c="O", d="N", e="M", f="A", g="N", h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 62:
            self.hintff(a="Y", b="G", c="G", d="D", e="R", f="A", g="S", h="I", i="L", j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 63:
            self.hintff(a="T", b="E", c="S", d="S", e="E", f="R", g="A", h="C", i="T", j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 64:
            self.hintff(a="N", b="I", c="C", d="K", e="F", f="U", g="R", h="Y", i=self.t, j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 65:
            self.hintff(a="H", b="Y", c="D", d="R", e="A", f=self.t, g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 66:
            self.hintff(a="R", b="E", c="D", d="S", e="K", f="U", g="L", h="L", i=self.t, j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 67:
            self.hintff(a="V", b="I", c="B", d="R", e="A", f="N", g="I", h="U", i="M", j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 68:
            self.hintff(a="A", b="R", c="N", d="I", e="M", f="Z", g="O", h="L", i="A", j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 69:
            self.hintff(a="O", b="N", c="E", d=self.t, e=self.t, f=self.t, g=self.t, h=self.t, i=self.t, j=self.t,
                        k=self.t, l=self.t, m=self.t, n=self.t, o=self.t,
                        lst=[1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 70:
            self.hintff(a="P", b="E", c="G", d="G", e="Y", f="C", g="A", h="R", i="T", j="E", k="R", l=self.t, m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 71:
            self.hintff(a="B", b="U", c="C", d="K", e="Y", f="B", g="A", h="R", i="N", j="E", k="S", l=self.t, m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 72:
            self.hintff(a="1", b="9", c="3", d="9", e=self.t, f=self.t, g=self.t, h=self.t, i=self.t, j=self.t,
                        k=self.t, l=self.t, m=self.t, n=self.t, o=self.t,
                        lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 73:
            self.hintff(a="2", b="0", c="0", d="8", e=self.t, f=self.t, g=self.t, h=self.t, i=self.t, j=self.t,
                        k=self.t, l=self.t, m=self.t, n=self.t, o=self.t,
                        lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 74:
            self.hintff(a="7", b="0", c=self.t, d=self.t, e=self.t, f=self.t, g=self.t, h=self.t, i=self.t, j=self.t,
                        k=self.t, l=self.t, m=self.t, n=self.t, o=self.t,
                        lst=[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        elif self.level == 75:
            self.hintff(a="I", b="V", c="A", d="N", e="V", f="A", g="N", h="K", i="O", j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 76:
            self.hintff(a="C", b="A", c="L", d="I", e="F", f="O", g="R", h="N", i="I", j="A", k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 77:
            self.hintff(a="P", b="E", c="P", d="P", e="E", f="R", g="P", h="O", i="T", j="T", k="S", l=self.t, m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 78:
            self.hintff(a="P", b="E", c="P", d="P", e="E", f="R", g="P", h="O", i="T", j="T", k="S", l=self.t, m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 79:
            self.hintff(a="A", b="N", c="T", d="O", e="N", f="V", g="A", h="N", i="K", j="O", k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 80:
            self.hintff(a="M", b="O", c="S", d="C", e="O", f="W", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 81:
            self.hintff(a="G", b="R", c="A", d="N", e="D", f="P", g="R", h="I", i="X", j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 82:
            self.hintff(a="M", b="O", c="N", d="A", e="C", f="O", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 83:
            self.hintff(a="H", b="A", c="M", d="M", e="E", f="R", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 84:
            self.hintff(a="N", b="A", c="T", d="A", e="S", f="H", g="A", h="R", i="O", j="M", k="A", l="N", m="O",
                        n="F", o="F", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        elif self.level == 85:
            self.hintff(a="S", b="H", c="I", d="E", e="L", f="D", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t,
                        l=self.t, m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 86:
            self.hintff(a="B", b="L", c="A", d="C", e="K", f="W", g="I", h="D", i="O", j="W", k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 87:
            self.hintff(a="N", b="A", c="T", d="A", e="S", f="H", g="A", h="R", i="O", j="M", k="A", l="N", m="O",
                        n='F', o="F", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        elif self.level == 88:
            self.hintff(a="H", b="O", c="W", d="A", e="R", f="D", g="S", h="T", i="A", j="R", k="K", l=self.t, m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 89:
            self.hintff(a="J", b="A", c="M", d="E", e="S", f="R", g="H", h="O", i="D", j="E", k="S", l=self.t, m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 90:
            self.hintff(a="P", b="H", c="I", d="L", e="C", f="O", g="U", h="L", i="S", j="O", k="N", l=self.t, m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 91:
            self.hintff(a="H", b="O", c="W", d="A", e="R", f="D", g="S", h="T", i="A", j="R", k="K", l=self.t, m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 92:
            self.hintff(a="D", b="U", c="R", d="A", e="L", f="U", g="M", h="I", i="N", j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 93:
            self.hintff(a="A", b="B", c="R", d="A", e="H", f="A", g="M", h="E", i="R", j="S", k="K", l="I", m="N",
                        n="E", o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0])
        elif self.level == 94:
            self.hintff(a="S", b="U", c="P", d="E", e="R", f="S", g="O", h="L", i="D", j="I", k="E", l="R", m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 95:
            self.hintff(a="S", b="T", c="E", d="V", e="E", f="R", g="O", h="G", i="E", j="R", k="S", l=self.t, m=self.t,
                        n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 96:
            self.hintff(a="P", b="A", c="L", d="L", e="A", f="D", g="I", h="U", i="M", j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 97:
            self.hintff(a="B", b="A", c="D", d="A", e="S", f="S", g="I", h="U", i="M", j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 98:
            self.hintff(a="H", b="A", c="P", d="P", e="Y", f="H", g="O", h="G", i="A", j="N", k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 99:
            self.hintff(a="A", b="S", c="T", d="R", e="O", f="P", g="H", h="Y", i="S", j="I", k="C", l="I", m="S",
                        n="T", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0])
        elif self.level == 100:
            self.hintff(a="I", b="N", c="F", d="A", e="N", f="T", g="R", h="Y", i=self.t, j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 101:
            self.hintff(a="P", b="E", c="T", d="E", e="R", f="Q", g="U", h="I", i="L", j="L", k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 102:
            self.hintff(a="G", b="A", c="M", d="O", e="R", f="A", g=self.t, h=self.t, i=self.t, j=self.t, k=self.t, l=self.t,
                        m=self.t, n=self.t, o=self.t, lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 103:
            self.hintff(a="T", b="H", c="A", d="N", e="O", f="S", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 104:
            self.hintff(a="R", b="O", c="N", d="A", e="N", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 105:
            self.hintff(a="G", b="R", c="O", d="O", e="T", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 106:
            self.hintff(a="S", b="P", c="A", d="C", e="E", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 107:
            self.hintff(a="G", b="A", c="M", d="O", e="R", f="A", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 108:
            self.hintff(a="N", b="E", c="B", d="U", e="L", f="A", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 109:
            self.hintff(a="Y", b="O", c="N", d="D", e="U", f="U", g="D", h="O", i="N", j="T", k="A", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 110:
            self.hintff(a="O", b="R", c="B", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 111:
            self.hintff(a="M", b="O", c="R", d="A", e="G", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 112:
            self.hintff(a="S", b="P", c="A", d="C", e="E", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 113:
            self.hintff(a="R", b="O", c="C", d="K", e="E", f="T", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 114:
            self.hintff(a="X", b="A", c="N", d="D", e="E", f="R", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 115:
            self.hintff(a="K", b="N", c="O", d="W", e="H", f="E", g="R", h="E", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 116:
            self.hintff(a="T", b="A", c="N", d="E", e="L", f="E", g="E", h="R", i="T", j="I", k="V", l="A", m="N",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 0])
        elif self.level == 117:
            self.hintff(a="M", b="I", c="S", d="S", e="O", f="U", g="R", h="I", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 118:
            self.hintff(a="1", b="9", c="8", d="8", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 119:
            self.hintff(a="M", b="E", c="R", d="E", e="D", f="I", g="T", h="H", i="Q", j="U", k="I", l="L", m="L",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 0])
        elif self.level == 120:
            self.hintff(a="Z", b="E", c="H", d="O", e="B", f="E", g="R", h="E", i="I", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 121:
            self.hintff(a="T", b="H", c="A", d="N", e="O", f="S", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 122:
            self.hintff(a="A", b="N", c="T", d="M", e="A", f="N", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 123:
            self.hintff(a="C", b="A", c="S", d="S", e="I", f="E", g="L", h="A", i="N", j="G", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 124:
            self.hintff(a="H", b="O", c="P", d="E", e="V", f="A", g="N", h="D", i="Y", j="N", k="E", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 125:
            self.hintff(a="H", b="A", c="N", d="K", e="P", f="Y", g="M", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 126:
            self.hintff(a="D", b="A", c="R", d="R", e="E", f="N", g="C", h="R", i="O", j="S", k="S", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 127:
            self.hintff(a="S", b="A", c="N", d="Q", e="E", f="N", g="T", h="I", i="N", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 128:
            self.hintff(a="J", b="I", c="M", d="P", e="A", f="X", g="T", h="O", i="N", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 129:
            self.hintff(a="L", b="U", c="I", d="S", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 130:
            self.hintff(a="S", b="O", c="V", d="I", e="E", f="T", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 5, 6 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 131:
            self.hintff(a="J", b="A", c="N", d="E", e="T", f="V", g="A", h="N", i="D", j="Y", k="N", l="E", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 132:
            self.hintff(a="F", b="A", c="L", d="C", e="O", f="N", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 133:
            self.hintff(a="W", b="A", c="S", d="P", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 134:
            self.hintff(a="A", b="N", c="T", d="O", e="N", f="Y", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 135:
            self.hintff(a="B", b="L", c="U", d="E", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 136:
            self.hintff(a="R", b="E", c="D", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 137:
            self.hintff(a="S", b="O", c="K", d="O", e="V", f="I", g="A", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 138:
            self.hintff(a="M", b="I", c="N", d="D", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 139:
            self.hintff(a="T", b="H", c="O", d="R", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 140:
            self.hintff(a="Q", b="U", c="I", d="C", e="K", f="S", g="I", h="L", i="V", j="E", k="R", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 141:
            self.hintff(a="V", b="I", c="S", d="I", e="O", f="N", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 142:
            self.hintff(a="U", b="L", c="T", d="R", e="O", f="N", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 143:
            self.hintff(a="V", b="I", c="B", d="R", e="A", f="N", g="I", h="U", i="M", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 144:
            self.hintff(a="H", b="A", c="W", d="K", e="E", f="Y", g="E", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 145:
            self.hintff(a="N", b="A", c="T", d="A", e="S", f="H", g="A", h="R", i="O", j="M", k="A", l="N", m="O",
                        n="F", o="F", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        elif self.level == 146:
            self.hintff(a="Q", b="U", c="I", d="C", e="K", f="S", g="I", h="L", i="V", j="E", k="R", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 147:
            self.hintff(a="S", b="H", c="I", d="E", e="L", f="D", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 148:
            self.hintff(a="P", b="I", c="E", d="T", e="R", f="O", g="M", h="A", i="X", j="I", k="M", l="O", m="F",
                        n="F", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0])
        elif self.level == 149:
            self.hintff(a="F", b="R", c="I", d="D", e="A", f="Y", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 150:
            self.hintff(a="N", b="E", c="B", d="U", e="L", f="A", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 151:
            self.hintff(a="I", b="R", c="O", d="N", e="M", f="A", g="N", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 152:
            self.hintff(a="M", b="A", c="R", d="K", e="4", f="2", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 153:
            self.hintff(a="H", b="A", c="R", d="L", e="E", f="Y", g="K", h="E", i="E", j="N", k="E", l="R", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 154:
            self.hintff(a="F", b="R", c="I", d="D", e="A", f="Y", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 155:
            self.hintff(a="H", b="A", c="P", d="P", e="Y", f="H", g="O", h="G", i="A", j="N", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 156:
            self.hintff(a="H", b="A", c="P", d="P", e="Y", f="H", g="O", h="G", i="A", j="N", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 157:
            self.hintff(a="J", b="A", c="M", d="E", e="S", f="R", g="H", h="O", i="D", j="E", k="S", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 158:
            self.hintff(a="M", b="A", c="R", d="K", e="4", f="2", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 159:
            self.hintff(a="P", b="E", c="P", d="P", e="E", f="R", g="P", h="O", i="T", j="T", k="S", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 160:
            self.hintff(a="A", b="R", c="C", d="R", e="E", f="C", g="A", h="T", i="O", j="R", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 161:
            self.hintff(a="N", b="I", c="N", d="E", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 162:
            self.hintff(a="F", b="R", c="I", d="G", e="G", f="A", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 163:
            self.hintff(a="L", b="O", c="K", d="I", e="Y", f="H", g="O", h="G", i="A", j="N", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 164:
            self.hintff(a="L", b="O", c="K", d="I", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 165:
            self.hintff(a="N", b="I", c="N", d="E", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 166:
            self.hintff(a="B", b="U", c="C", d="K", e="Y", f="B", g="A", h="R", i="N", j="E", k="S", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 167:
            self.hintff(a="N", b="I", c="C", d="K", e="F", f="U", g="R", h="Y", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 168:
            self.hintff(a="J", b="A", c="N", d="E", e="F", f="O", g="S", h="T", i="E", j="R", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 169:
            self.hintff(a="V", b="I", c="B", d="R", e="A", f="N", g="I", h="U", i="M", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 170:
            self.hintff(a="H", b="Y", c="D", d="R", e="A", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 171:
            self.hintff(a="N", b="I", c="C", d="K", e="F", f="U", g="R", h="Y", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 172:
            self.hintff(a="A", b="R", c="N", d="I", e="M", f="Z", g="O", h="L", i="A", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 173:
            self.hintff(a="A", b="R", c="N", d="I", e="M", f="Z", g="O", h="L", i="A", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 174:
            self.hintff(a="S", b="H", c="I", d="E", e="L", f="D", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 175:
            self.hintff(a="P", b="E", c="G", d="G", e="Y", f="C", g="A", h="R", i="T", j="E", k="R", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 176:
            self.hintff(a="M", b="A", c="N", d="D", e="A", f="R", g="I", h="N", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 177:
            self.hintff(a="A", b="L", c="D", d="R", e="I", f="C", g="H", h="K", i="I", j="L", k="L", l="I", m="A",
                        n="N", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0])
        elif self.level == 178:
            self.hintff(a="R", b="O", c="S", d="E", e="H", f="I", g="L", h="L", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 179:
            self.hintff(a="W", b="A", c="R", d="M", e="A", f="C", g="H", h="I", i="N", j="E", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 180:
            self.hintff(a="I", b="R", c="O", d="N", e="P", f="A", g="T", h="R", i="I", j="O", k="T", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 181:
            self.hintff(a="1", b="3", c="", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 182:
            self.hintff(a="4", b="2", c="", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 183:
            self.hintff(a="9", b="6", c="", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 184:
            self.hintff(a="S", b="H", c="A", d="R", e="O", f="N", g="C", h="A", i="R", j="T", k="E", l="R", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 185:
            self.hintff(a="M", b="A", c="G", d="N", e="E", f="T", g="I", h="C", i="M", j="I", k="N", l="E", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 186:
            self.hintff(a="S", b="H", c="A", d="R", e="O", f="N", g="C", h="A", i="R", j="T", k="E", l="R", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 187:
            self.hintff(a="C", b="A", c="M", d="P", e="L", f="E", g="H", h="I", i="G", j="H", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 188:
            self.hintff(a="T", b="H", c="R", d="E", e="E", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 189:
            self.hintff(a="I", b="N", c="S", d="I", e="G", f="H", g="T", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 190:
            self.hintff(a="S", b="A", c="M", d="W", e="I", f="L", g="S", h="O", i="N", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 191:
            self.hintff(a="I", b="N", c="S", d="I", e="G", f="H", g="T", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 192:
            self.hintff(a="A", b="E", c="T", d="H", e="E", f="R", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6,0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 193:
            self.hintff(a="M", b="A", c="L", d="E", e="K", f="I", g="T", h="H", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 194:
            self.hintff(a="A", b="L", c="G", d="R", e="I", f="M", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 195:
            self.hintff(a="S", b="A", c="K", d="A", e="A", f="R", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 196:
            self.hintff(a="L", b="O", c="N", d="D", e="O", f="N", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 197:
            self.hintff(a="S", b="V", c="A", d="R", e="T", f="A", g="L", h="T", i="H", j="E", k="I", l="M", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 0, 0, 0])
        elif self.level == 198:
            self.hintff(a="D", b="A", c="R", d="C", e="Y", f="L", g="E", h="W", i="I", j="S", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 0, 0, 0, 0, 0])

        elif self.level == 199:
            self.hintff(a="M", b="A", c="L", d="E", e="K", f="I", g="T", h="H", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 200:
            self.hintff(a="M", b="A", c="R", d="I", e="A", f="H", g="I", h="L", i="L", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 201:
            self.hintff(a="S", b="U", c="R", d="T", e="U", f="R", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 202:
            self.hintff(a="H", b="E", c="L", d="A", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 203:
            self.hintff(a="H", b="E", c="L", d="A", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 204:
            self.hintff(a="H", b="U", c="L", d="K", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 205:
            self.hintff(a="N", b="O", c="R", d="W", e="A", f="Y", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 206:
            self.hintff(a="S", b="U", c="R", d="T", e="U", f="R", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 207:
            self.hintff(a="H", b="E", c="L", d="A", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 208:
            self.hintff(a="V", b="A", c="L", d="K", e="Y", f="R", g="I", h="E", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 209:
            self.hintff(a="G", b="R", c="A", d="N", e="D", f="M", g="A", h="S", i="T", j="E", k="R", l="", m="",
                        n="", o="", lst=[1, 2, 3 ,4, 5, 6, 7, 8, 9 ,10, 11, 0, 0, 0, 0])
        elif self.level == 210:
            self.hintff(a="S", b="A", c="K", d="A", e="A", f="R", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 211:
            self.hintff(a="N", b="E", c="W", d="Y", e="O", f="K", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 212:
            self.hintff(a="H", b="E", c="L", d="A", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 213:
            self.hintff(a="H", b="E", c="L", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 214:
            self.hintff(a="M", b="E", c="L", d="T", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 215:
            self.hintff(a="L", b="O", c="K", d="I", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 216:
            self.hintff(a="O", b="D", c="I", d="N", e="F", f="O", g="R", h="C", i="E", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 217:
            self.hintff(a="E", b="I", c="N", d="H", e="E", f="R", g="J", h="A", i="R", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 218:
            self.hintff(a="S", b="T", c="A", d="N", e="L", f="E", g="E", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 219:
            self.hintff(a="K", b="O", c="R", d="G", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 220:
            self.hintff(a="M", b="E", c="I", d="K", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 221:
            self.hintff(a="S", b="T", c="E", d="P", e="H", f="E", g="N", h="S", i="T", j="R", k="A", l="N", m="G",
                        n="E", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 0])
        elif self.level == 222:
            self.hintff(a="H", b="A", c="N", d="D", e="S", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 223:
            self.hintff(a="K", b="A", c="M", d="A", e="R", f="T", g="A", h="J", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 224:
            self.hintff(a="N", b="E", c="P", d="A", e="L", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 225:
            self.hintff(a="E", b="Y", c="E", d="O", e="F", f="A", g="G", h="A", i="M", j="O", k="T", l="T", m="O",
                        n="", o="", lst=[1, 2, 3, 4, 5,6, 7, 8, 9 ,10, 11, 12, 13, 0, 0])
        elif self.level == 226:
            self.hintff(a="T", b="I", c="M", d="E", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 227:
            self.hintff(a="K", b="A", c="E", d="C", e="I", f="L", g="I", h="U", i="S", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 228:
            self.hintff(a="K", b="A", c="E", d="C", e="I", f="L", g="I", h="U", i="S", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 229:
            self.hintff(a="W", b="O", c="N", d="G", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 230:
            self.hintff(a="D", b="A", c="R", d="K", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 231:
            self.hintff(a="D", b="O", c="R", d="M", e="A", f="M", g="M", h="U", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 232:
            self.hintff(a="K", b="A", c="E", d="C", e="I", f="L", g="I", h="U", i="S", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 233:
            self.hintff(a="C", b="A", c="G", d="L", e="I", f="O", g="S", h="T", i="R", j="O", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 0, 0, 0, 0, 0])
        elif self.level == 234:
            self.hintff(a="D", b="O", c="C", d="T", e="O", f="R", g="S", h="T", i="R", j="A", k="N", l="G", m="E",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 0, 0])
        elif self.level == 235:
            self.hintff(a="D", b="O", c="C", d="T", e="O", f="R", g="S", h="T", i="R", j="A", k="N", l="G", m="E",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 0, 0])
        elif self.level == 236:
            self.hintff(a="N", b="E", c="W", d="Y", e="O", f="R", g="K", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 237:
            self.hintff(a="M", b="O", c="R", d="D", e="O", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 238:
            self.hintff(a="S", b="L", c="I", d="N", e="G", f="R", g="I", h="N", i="G", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 239:
            self.hintff(a="D", b="A", c="R", d="K", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 240:
            self.hintff(a="M", b="Y", c="S", d="T", e="I", f="C", g="A", h="R", i="T", j="S", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 0, 0, 0, 0, 0])
        elif self.level == 241:
            self.hintff(a="T", b="O", c="M", d="H", e="O", f="L", g="L", h="A", i="N", j="D", k="N", l="G", m="E",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 0, 0, 0, 0, 0])
        elif self.level == 242:
            self.hintff(a="L", b="I", c="Z", d="T", e="O", f="O", g="M", h="E", i="S", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 243:
            self.hintff(a="L", b="I", c="Z", d="T", e="O", f="O", g="M", h="E", i="S", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 244:
            self.hintff(a="T", b="O", c="N", d="Y", e="S", f="T", g="A", h="R", i="K", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 245:
            self.hintff(a="I", b="R", c="O", d="N", e="M", f="A", g="N", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 246:
            self.hintff(a="L", b="I", c="Z", d="T", e="O", f="O", g="M", h="E", i="S", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 247:
            self.hintff(a="T", b="O", c="N", d="Y", e="S", f="T", g="A", h="R", i="K", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 248:
            self.hintff(a="T", b="O", c="N", d="Y", e="S", f="T", g="A", h="R", i="K", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 249:
            self.hintff(a="C", b="H", c="I", d="T", e="A", f="U", g="R", h="I", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 250:
            self.hintff(a="K", b="A", c="R", d="E", e="N", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 251:
            self.hintff(a="N", b="E", c="D", d="L", e="E", f="E", g="D", h="S", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 252:
            self.hintff(a="V", b="U", c="L", d="T", e="U", f="R", g="E", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 253:
            self.hintff(a="E", b="G", c="O", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 254:
            self.hintff(a="A", b="Y", c="E", d="S", e="H", f="A", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 255:
            self.hintff(a="A", b="N", c="U", d="L", e="A", f="X", g="", h="", i="K", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 256:
            self.hintff(a="G", b="R", c="O", d="O", e="T", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 257:
            self.hintff(a="P", b="E", c="T", d="E", e="R", f="Q", g="U", h="I", i="L", j="L", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 0, 0, 0, 0, 0])
        elif self.level == 258:
            self.hintff(a="R", b="O", c="C", d="K", e="E", f="T", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 259:
            self.hintff(a="Y", b="O", c="N", d="D", e="U", f="U", g="D", h="O", i="N", j="T", k="A", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 0, 0, 0, 0])
        elif self.level == 260:
            self.hintff(a="M", b="A", c="N", d="T", e="I", f="S", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 261:
            self.hintff(a="S", b="I", c="X", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 262:
            self.hintff(a="S", b="P", c="A", d="C", e="E", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 263:
            self.hintff(a="T", b="H", c="A", d="N", e="O", f="S", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 264:
            self.hintff(a="S", b="T", c="A", d="T", e="E", f="S", g="M", h="A", i="N", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 265:
            self.hintff(a="K", b="N", c="O", d="W", e="H", f="E", g="R", h="E", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 266:
            self.hintff(a="G", b="A", c="M", d="O", e="R", f="A", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 267:
            self.hintff(a="R", b="E", c="D", d="S", e="K", f="U", g="L", h="L", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 268:
            self.hintff(a="T", b="I", c="M", d="E", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 269:
            self.hintff(a="T", b="I", c="M", d="E", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 270:
            self.hintff(a="S", b="T", c="R", d="O", e="M", f="B", g="R", h="E", i="A", j="K", k="E", l="R", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 0, 0, 0])
        elif self.level == 271:
            self.hintff(a="S", b="T", c="R", d="O", e="M", f="B", g="R", h="E", i="A", j="K", k="E", l="R", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 0, 0, 0])
        elif self.level == 272:
            self.hintff(a="T", b="I", c="T", d="A", e="N", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 273:
            self.hintff(a="T", b="I", c="T", d="A", e="N", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 274:
            self.hintff(a="M", b="A", c="R", d="K", e="4", f="2", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 275:
            self.hintff(a="R", b="E", c="A", d="L", e="I", f="T", g="Y", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 276:
            self.hintff(a="S", b="P", c="A", d="C", e="E", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 277:
            self.hintff(a="N", b="E", c="W", d="Y", e="O", f="R", g="K", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 278:
            self.hintff(a="G", b="A", c="R", d="D", e="E", f="N", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 279:
            self.hintff(a="U", b="R", c="U", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 280:
            self.hintff(a="U", b="R", c="U", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 281:
            self.hintff(a="N", b="I", c="D", d="A", e="V", f="E", g="L", h="L", i="I", j="R", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 0, 0, 0, 0, 0])
        elif self.level == 282:
            self.hintff(a="N", b="I", c="D", d="A", e="V", f="E", g="L", h="L", i="I", j="R", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 0, 0, 0, 0, 0])
        elif self.level == 283:
            self.hintff(a="D", b="W", c="A", d="R", e="V", f="E", g="S", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 284:
            self.hintff(a="T", b="O", c="N", d="Y", e="S", f="T", g="A", h="R", i="K", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 285:
            self.hintff(a="T", b="H", c="A", d="D", e="D", f="E", g="U", h="S", i="R", j="O", k="S", l="S", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 0, 0, 0])
        elif self.level == 286:
            self.hintff(a="J", b="A", c="M", d="E", e="S", f="R", g="H", h="O", i="D", j="E", k="S", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 0, 0, 0, 0])
        elif self.level == 287:
            self.hintff(a="S", b="H", c="A", d="R", e="O", f="N", g="C", h="A", i="R", j="T", k="E", l="R", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 0, 0, 0])
        elif self.level == 288:
            self.hintff(a="S", b="H", c="A", d="R", e="O", f="N", g="C", h="A", i="R", j="T", k="E", l="R", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 0, 0, 0])
        elif self.level == 289:
            self.hintff(a="S", b="H", c="I", d="E", e="L", f="D", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 290:
            self.hintff(a="2", b="0", c="1", d="6", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 291:
            self.hintff(a="T", b="C", c="H", d="A", e="K", f="A", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 292:
            self.hintff(a="T", b="C", c="H", d="A", e="K", f="A", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 293:
            self.hintff(a="T", b="C", c="H", d="A", e="K", f="A", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 294:
            self.hintff(a="S", b="H", c="U", d="R", e="I", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 295:
            self.hintff(a="T", b="C", c="H", d="A", e="L", f="L", g="A", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 296:
            self.hintff(a="V", b="I", c="B", d="R", e="A", f="N", g="I", h="U", i="M", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 297:
            self.hintff(a="M", b="B", c="A", d="K", e="U", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 298:
            self.hintff(a="S", b="H", c="U", d="R", e="I", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 299:
            self.hintff(a="M", b="B", c="A", d="K", e="U", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 300:
            self.hintff(a="O", b="K", c="O", d="Y", e="E", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 301:
            self.hintff(a="N", b="A", c="K", d="I", e="A", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 302:
            self.hintff(a="J", b="A", c="B", d="A", e="R", f="I", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 303:
            self.hintff(a="N", b="J", c="O", d="B", e="U", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 304:
            self.hintff(a="K", b="I", c="L", d="L", e="M", f="O", g="N", h="G", i="E", j="R", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 0, 0, 0, 0, 0])
        elif self.level == 305:
            self.hintff(a="P", b="E", c="G", d="G", e="Y", f="C", g="A", h="R", i="T", j="E", k="R", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 8 ,10, 11, 0, 0, 0, 0])
        elif self.level == 306:
            self.hintff(a="S", b="A", c="M", d="W", e="I", f="L", g="S", h="O", i="N", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 0, 0, 0, 0])

        elif self.level == 307:
            self.hintff(a="B", b="R", c="U", d="C", e="E", f="B", g="A", h="N", i="N", j="E", k="R", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 0, 0, 0, 0])
        elif self.level == 308:
            self.hintff(a="B", b="R", c="U", d="C", e="E", f="B", g="A", h="N", i="N", j="E", k="R", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 0, 0, 0, 0])
        elif self.level == 309:
            self.hintff(a="T", b="O", c="N", d="Y", e="S", f="T", g="A", h="R", i="K", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,0, 0, 0, 0, 0, 0])
        elif self.level == 310:
            self.hintff(a="T", b="O", c="K", d="Y", e="O", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 311:
            self.hintff(a="F", b="R", c="I", d="G", e="G", f="A", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 312:
            self.hintff(a="M", b="J", c="O", d="L", e="N", f="I", g="R", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 313:
            self.hintff(a="H", b="O", c="W", d="A", e="R", f="D", g="S", h="T", i="A", j="R", k="K", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 0, 0, 0, 0])
        elif self.level == 314:
            self.hintff(a="1", b="9", c="7", d="0", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 315:
            self.hintff(a="A", b="S", c="G", d="A", e="R", f="D", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 316:
            self.hintff(a="2", b="0", c="1", d="2", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 317:
            self.hintff(a="2", b="0", c="1", d="2", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 318:
            self.hintff(a="N", b="E", c="W", d="Y", e="O", f="R", g="K", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 319:
            self.hintff(a="M", b="O", c="R", d="A", e="G", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 320:
            self.hintff(a="2", b="0", c="1", d="2", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 321:
            self.hintff(a="V", b="O", c="R", d="M", e="I", f="R", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 322:
            self.hintff(a="N", b="A", c="T", d="A", e="S", f="H", g="A", h="R", i="O", j="M", k="A", l="N", m="O",
                        n="F", o="F", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15])
        elif self.level == 323:
            self.hintff(a="L", b="O", c="K", d="I", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 324:
            self.hintff(a="R", b="E", c="S", d="C", e="U", f="E", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 325:
            self.hintff(a="Q", b="U", c="A", d="N", e="T", f="U", g="M", h="G", i="P", j="S", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 0, 0, 0, 0, 0])
        elif self.level == 326:
            self.hintff(a="C", b="A", c="P", d="T", e="A", f="I", g="N", h="M", i="A", j="R", k="V", l="E", m="L",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 0, 0])
        elif self.level == 327:
            self.hintff(a="C", b="A", c="P", d="T", e="A", f="I", g="N", h="M", i="A", j="R", k="V", l="E", m="L",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 0, 0])
        elif self.level == 328:
            self.hintff(a="N", b="E", c="B", d="U", e="L", f="A", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 329:
            self.hintff(a="C", b="A", c="S", d="S", e="I", f="E", g="L", h="A", i="N", j="G", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 0, 0, 0, 0, 0])
        elif self.level == 330:
            self.hintff(a="U", b="T", c="Y", d="S", e="S", f="E", g="S", h="K", i="L", j="A", k="U", l="E", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 9, 10 ,11, 12, 0, 0, 0, 0])
        elif self.level == 331:
            self.hintff(a="E", b="V", c="E", d="R", e="E", f="T", g="T", h="R", i="O", j="S", k="S", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 9, 10 ,11, 0, 0, 0, 0, 0])
        elif self.level == 332:
            self.hintff(a="K", b="I", c="L", d="L", e="M", f="O", g="N", h="G", i="E", j="R", k="", l="E", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 9, 10 ,0, 0, 0, 0, 0, 0])
        elif self.level == 333:
            self.hintff(a="H", b="E", c="A", d="R", e="T", f="S", g="H", h="A", i="P", j="E", k="D", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 9, 10 ,11, 0, 0, 0, 0, 0])
        elif self.level == 334:
            self.hintff(a="B", b="U", c="C", d="K", e="Y", f="B", g="A", h="R", i="N", j="E", k="S", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 9, 10 ,11, 0, 0, 0, 0, 0])
        elif self.level == 335:
            self.hintff(a="S", b="C", c="O", d="T", e="T", f="L", g="A", h="N", i="G", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 9, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 336:
            self.hintff(a="A", b="G", c="E", d="N", e="T", f="1", g="3", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 337:
            self.hintff(a="V", b="I", c="E", d="N", e="N", f="A", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 338:
            self.hintff(a="H", b="E", c="L", d="M", e="U", f="T", g="Z", h="E", i="M", j="O", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 9, 10 ,0, 0, 0, 0, 0, 0])
        elif self.level == 339:
            self.hintff(a="S", b="N", c="A", d="P", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 340:
            self.hintff(a="1", b="9", c="8", d="7", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0])
        elif self.level == 341:
            self.hintff(a="S", b="C", c="O", d="T", e="T", f="L", g="A", h="N", i="G", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 9, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 342:
            self.hintff(a="G", b="H", c="O", d="S", e="T", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 343:
            self.hintff(a="S", b="O", c="N", d="N", e="Y", f="B", g="U", h="R", i="C", j="H", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 9, 10, 0, 0, 0, 0, 0, 0])
        elif self.level == 344:
            self.hintff(a="B", b="I", c="L", d="L", e="F", f="O", g="S", h="T", i="E", j="R", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 9,10, 0, 0, 0, 0, 0, 0])
        elif self.level == 345:
            self.hintff(a="A", b="V", c="A", d="S", e="T", f="A", g="R", h="R", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 346:
            self.hintff(a="E", b="L", c="I", d="H", e="A", f="S", g="S", h="T", i="A", j="R", k="R", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 0, 0, 0, 0, 0])
        elif self.level == 347:
            self.hintff(a="H", b="O", c="P", d="E", e="V", f="A", g="N", h="D", i="Y", j="N", k="E", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 0, 0, 0, 0, 0])
        elif self.level == 348:
            self.hintff(a="T", b="H", c="A", d="N", e="O", f="S", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 349:

            self.hintff(a="T", b="H", c="A", d="N", e="O", f="S", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 350:
            self.hintff(a="C", b="A", c="P", d="T", e="A", f="I", g="N", h="M", i="A", j="R", k="V", l="E", m="L",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 0])
        elif self.level == 351:
            self.hintff(a="H", b="A", c="L", d="A", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 352:
            self.hintff(a="C", b="A", c="P", d="T", e="A", f="I", g="N", h="M", i="A", j="R", k="V", l="E", m="L",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 0])
        elif self.level == 353:
            self.hintff(a="Y", b="O", c="N", d="R", e="O", f="G", g="G", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 354:
            self.hintff(a="S", b="O", c="H", d="L", e="A", f="R", g="R", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 355:
            self.hintff(a="T", b="O", c="R", d="F", e="A", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 356:
            self.hintff(a="T", b="A", c="L", d="O", e="S", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 357:
            self.hintff(a="E", b="A", c="R", d="T", e="H", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 358:
            self.hintff(a="E", b="A", c="R", d="T", e="H", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 359:
            self.hintff(a="M", b="A", c="R", d="I", e="A", f="R", g="A", h="M", i="B", j="E", k="A", l="U", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 360:
            self.hintff(a="G", b="O", c="O", d="S", e="E", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 361:
            self.hintff(a="B", b="R", c="I", d="E", e="L", f="A", g="R", h="S", i="O", j="N", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 362:
            self.hintff(a="N", b="I", c="C", d="K", e="F", f="U", g="R", h="Y", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 363:
            self.hintff(a="W", b="E", c="N", d="D", e="Y", f="L", g="A", h="W", i="S", j="O", k="N", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 364:
            self.hintff(a="W", b="E", c="N", d="D", e="Y", f="L", g="A", h="W", i="S", j="O", k="N", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 365:
            self.hintff(a="T", b="E", c="S", d="S", e="E", f="R", g="A", h="C", i="T", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 366:
            self.hintff(a="M", b="O", c="J", d="A", e="V", f="E", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 367:
            self.hintff(a="M", b="O", c="J", d="A", e="V", f="E", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 368:
            self.hintff(a="C", b="A", c="R", d="O", e="L", f="D", g="A", h="N", i="V", j="E", k="R", l="S", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 369:
            self.hintff(a="C", b="A", c="R", d="O", e="L", f="D", g="A", h="N", i="V", j="E", k="R", l="S", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 370:
            self.hintff(a="C", b="A", c="R", d="O", e="L", f="D", g="A", h="N", i="V", j="E", k="R", l="S", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 371:
            self.hintff(a="M", b="I", c="S", d="T", e="E", f="R", g="I", h="O", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 372:
            self.hintff(a="M", b="I", c="S", d="T", e="E", f="R", g="I", h="O", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 373:
            self.hintff(a="C", b="A", c="R", d="O", e="L", f="D", g="A", h="N", i="V", j="E", k="R", l="S", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 374:
            self.hintff(a="C", b="A", c="R", d="O", e="L", f="D", g="A", h="N", i="V", j="E", k="R", l="S", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 375:
            self.hintff(a="S", b="H", c="I", d="E", e="L", f="D", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 376:
            self.hintff(a="C", b="A", c="R", d="O", e="L", f="D", g="A", h="N", i="V", j="E", k="R", l="S", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 377:
            self.hintff(a="Z", b="E", c="N", d="D", e="A", f="Y", g="A", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 378:
            self.hintff(a="T", b="O", c="M", d="H", e="O", f="L", g="L", h="A", i="N", j="D", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 379:
            self.hintff(a="V", b="E", c="R", d="S", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 380:
            self.hintff(a="R", b="A", c="T", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 400:
            self.hintff(a="N", b="E", c="W", d="J", e="E", f="R", g="S", h="E", i="Y", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 401:
            self.hintff(a="A", b="G", c="N", d="E", e="S", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 402:
            self.hintff(a="A", b="G", c="N", d="E", e="S", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 403:
            self.hintff(a="A", b="R", c="T", d="H", e="U", f="R", g="H", h="A", i="R", j="T", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 404:
            self.hintff(a="B", b="I", c="L", d="L", e="Y", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 405:
            self.hintff(a="T", b="O", c="M", d="M", e="Y", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 406:
            self.hintff(a="D", b="A", c="R", d="K", e="H", f="O", g="L", h="D", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 407:
            self.hintff(a="S", b="P", c="A", d="R", e="K", f="Y", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 408:
            self.hintff(a="H", b="E", c="X", d="A", e="G", f="O", g="N", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 409:
            self.hintff(a="J", b="I", c="M", d="M", e="Y", f="W", g="O", h="0", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 410:
            self.hintff(a="J", b="I", c="M", d="M", e="Y", f="W", g="O", h="O", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 411:
            self.hintff(a="G", b="E", c="R", d="A", e="L", f="D", g="I", h="N", i="E", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 412:
            self.hintff(a="S", b="W", c="O", d="R", e="D", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 413:
            self.hintff(a="W", b="E", c="S", d="T", e="V", f="I", g="E", h="W", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 414:
            self.hintff(a="D", b="A", c="R", d="C", e="Y", f="L", g="E", h="W", i="I", j="S", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 415:
            self.hintff(a="T", b="Y", c="L", d="E", e="R", f="H", g="A", h="Y", i="W", j="A", k="R", l="D", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 416:
            self.hintff(a="T", b="Y", c="L", d="E", e="R", f="H", g="A", h="Y", i="W", j="A", k="R", l="D", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 417:
            self.hintff(a="R", b="U", c="S", d="S", e="I", f="A", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 418:
            self.hintff(a="Y", b="E", c="L", d="E", e="N", f="A", g="B", h="E", i="L", j="O", k="V", l="A", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 419:
            self.hintff(a="Y", b="E", c="L", d="E", e="N", f="A", g="B", h="E", i="L", j="O", k="V", l="A", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 420:
            self.hintff(a="Y", b="E", c="L", d="E", e="N", f="A", g="B", h="E", i="L", j="O", k="V", l="A", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 421:
            self.hintff(a="A", b="L", c="E", d="X", e="E", f="L", g="S", h="H", i="O", j="S", k="T", l="A", m="K",
                        n="O", o="V", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        elif self.level == 422:
            self.hintff(a="A", b="N", c="T", d="O", e="N", f="I", g="A", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 423:
            self.hintff(a="A", b="N", c="T", d="O", e="N", f="I", g="A", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 424:
            self.hintff(a="R", b="U", c="S", d="S", e="I", f="A", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 425:
            self.hintff(a="S", b="I", c="B", d="E", e="R", f="I", g="A", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 426:
            self.hintff(a="W", b="E", c="N", d="W", e="U", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 427:
            self.hintff(a="S", b="H", c="A", d="N", e="G", f="C", g="H", h="I", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 428:
            self.hintff(a="X", b="I", c="A", d="L", e="I", f="N", g="G", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 429:
            self.hintff(a="X", b="I", c="A", d="L", e="I", f="N", g="G", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 430:
            self.hintff(a="T", b="A", c="L", d="O", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 431:
            self.hintff(a="M", b="A", c="N", d="D", e="A", f="R", g="I", h="N", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 432:
            self.hintff(a="K", b="A", c="T", d="Y", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 433:
            self.hintff(a="R", b="A", c="Z", d="O", e="R", f="F", g="I", h="S", i="T", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 434:
            self.hintff(a="A", b="B", c="O", d="M", e="I", f="N", g="A", h="T", i="I", j="O", k="N", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 435:
            self.hintff(a="X", b="I", c="A", d="L", e="I", f="N", g="G", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 436:
            self.hintff(a="G", b="O", c="R", d="R", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 437:
            self.hintff(a="R", b="A", c="P", d="U", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 438:
            self.hintff(a="R", b="A", c="P", d="U", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 439:
            self.hintff(a="G", b="O", c="R", d="R", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 440:
            self.hintff(a="G", b="O", c="R", d="R", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 441:
            self.hintff(a="T", b="H", c="O", d="R", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 442:
            self.hintff(a="L", b="O", c="V", d="E", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 443:
            self.hintff(a="A", b="X", c="L", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 444:
            self.hintff(a="Z", b="E", c="U", d="S", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 445:
            self.hintff(a="Z", b="E", c="U", d="S", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 446:
            self.hintff(a="Z", b="E", c="U", d="S", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 447:
            self.hintff(a="N", b="E", c="C", d="R", e="O", f="S", g="W", h="O", i="R", j="D", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 448:
            self.hintff(a="K", b="N", c="U", d="L", e="L", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 449:
            self.hintff(a="S", b="T", c="R", d="O", e="M", f="B", g="R", h="E", i="A", j="K", k="E", l="R", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 450:
            self.hintff(a="S", b="H", c="A", d="D", e="O", f="W", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 451:
            self.hintff(a="V", b="I", c="S", d="H", e="A", f="N", g="T", h="I", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 452:
            self.hintff(a="S", b="P", c="I", d="D", e="E", f="R", g="M", h="A", i="N", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 453:
            self.hintff(a="M", b="Y", c="S", d="T", e="E", f="R", g="I", h="O", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 454:
            self.hintff(a="1", b="7", c="", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 455:
            self.hintff(a="M", b="I", c="C", d="H", e="E", f="L", g="L", h="E", i="J", j="O", k="N", l="E", m="S",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 0])
        elif self.level == 456:
            self.hintff(a="M", b="A", c="T", d="T", e="M", f="U", g="R", h="D", i="O", j="C", k="K", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 457:
            self.hintff(a="M", b="A", c="Y", d="P", e="A", f="R", g="K", h="E", i="R", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 458:
            self.hintff(a="H", b="A", c="P", d="P", e="Y", f="H", g="O", h="G", i="A", j="N", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 459:
            self.hintff(a="D", b="O", c="C", d="T", e="O", f="R", g="O", h="C", i="T", j="O", k="P", l="U", m="S",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 13, 0, 0])
        elif self.level == 460:
            self.hintff(a="E", b="L", c="E", d="C", e="T", f="R", g="O", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 461:
            self.hintff(a="L", b="I", c="Z", d="A", e="R", f="D", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 462:
            self.hintff(a="G", b="R", c="E", d="E", e="N", f="G", g="O", h="B", i="L", j="I", k="N", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 463:
            self.hintff(a="S", b="A", c="N", d="D", e="M", f="A", g="N", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 464:
            self.hintff(a="T", b="O", c="M", d="H", e="O", f="L", g="L", h="A", i="N", j="D", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 465:
            self.hintff(a="A", b="N", c="D", d="R", e="E", f="W", g="G", h="A", i="R", j="F", k="I", l="E", m="L",
                        n="D", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0])
        elif self.level == 466:
            self.hintff(a="D", b="O", c="C", d="T", e="O", f="R", g="S", h="T", i="R", j="A", k="N", l="G", m="E",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 0])
        elif self.level == 467:
            self.hintff(a="M", b="I", c="R", d="R", e="O", f="R", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 468:
            self.hintff(a="M", b="A", c="Y", d="P", e="A", f="R", g="K", h="E", i="R", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 469:
            self.hintff(a="S", b="P", c="I", d="D", e="E", f="R", g="M", h="A", i="N", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 470:
            self.hintff(a="D", b="O", c="M", d="O", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 471:
            self.hintff(a="C", b="E", c="L", d="E", e="S", f="T", g="I", h="A", i="L", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 472:
            self.hintff(a="C", b="E", c="L", d="E", e="S", f="T", g="I", h="A", i="L", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 473:
            self.hintff(a="C", b="E", c="L", d="E", e="S", f="T", g="I", h="A", i="L", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 474:
            self.hintff(a="A", b="J", c="A", d="K", e="", f="", g="", h="", i="L", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 475:
            self.hintff(a="5", b="0", c="0", d="0", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 476:
            self.hintff(a="K", b="R", c="O", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 477:
            self.hintff(a="T", b="H", c="E", d="N", e="A", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 478:
            self.hintff(a="S", b="E", c="R", d="S", e="I", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 479:
            self.hintff(a="S", b="E", c="R", d="S", e="I", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 480:
            self.hintff(a="D", b="A", c="N", d="E", e="W", f="H", g="I", h="T", i="M", j="A", k="N", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 481:
            self.hintff(a="K", b="I", c="N", d="G", e="O", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 482:
            self.hintff(a="K", b="A", c="R", d="U", e="N", f="P", g="A", h="T", i="E", j="L", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 483:
            self.hintff(a="D", b="E", c="V", d="I", e="A", f="N", g="T", h="S", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 484:
            self.hintff(a="L", b="O", c="N", d="D", e="A", f="N", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 485:
            self.hintff(a="P", b="H", c="A", d="S", e="T", f="O", g="S", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 486:
            self.hintff(a="A", b="R", c="I", d="S", e="H", f="E", g="M", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 487:
            self.hintff(a="M", b="A", c="K", d="K", e="A", f="R", g="I", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 488:
            self.hintff(a="D", b="R", c="U", d="L", e="G", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 489:
            self.hintff(a="B", b="U", c="C", d="K", e="Y", f="B", g="A", h="R", i="N", j="E", k="S", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 490:
            self.hintff(a="J", b="O", c="H", d="N", e="W", f="A", g="L", h="K", i="E", j="R", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 491:
            self.hintff(a="H", b="E", c="L", d="M", e="U", f="T", g="Z", h="E", i="M", j="O", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 492:
            self.hintff(a="S", b="H", c="A", d="R", e="O", f="N", g="C", h="A", i="R", j="T", k="E", l="R", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 493:
            self.hintff(a="S", b="H", c="A", d="R", e="O", f="N", g="C", h="A", i="R", j="T", k="E", l="R", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 494:
            self.hintff(a="H", b="E", c="L", d="M", e="U", f="T", g="Z", h="E", i="M", j="O", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 495:
            self.hintff(a="S", b="A", c="M", d="W", e="I", f="L", g="S", h="O", i="N", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 496:
            self.hintff(a="S", b="A", c="R", d="A", e="H", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 497:
            self.hintff(a="S", b="A", c="M", d="W", e="I", f="L", g="S", h="O", i="N", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 498:
            self.hintff(a="J", b="O", c="H", d="N", e="W", f="A", g="L", h="K", i="E", j="R", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 499:
            self.hintff(a="N", b="I", c="C", d="O", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 500:
            self.hintff(a="F", b="L", c="A", d="G", e="S", f="M", g="A", h="S", i="H", j="E", k="R", l="S", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 501:
            self.hintff(a="B", b="A", c="T", d="T", e="L", f="E", g="S", h="T", i="A", j="R", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 502:
            self.hintff(a="F", b="L", c="A", d="G", e="S", f="M", g="A", h="S", i="H", j="E", k="R", l="S", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 503:
            self.hintff(a="S", b="H", c="U", d="R", e="I", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 504:
            self.hintff(a="N", b="A", c="K", d="I", e="A", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 505:
            self.hintff(a="S", b="H", c="U", d="R", e="I", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 506:
            self.hintff(a="O", b="K", c="O", d="Y", e="E", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 507:
            self.hintff(a="K", b="I", c="L", d="L", e="M", f="O", g="N", h="G", i="E", j="R", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 508:
            self.hintff(a="C", b="H", c="R", d="I", e="S", f="T", g="I", h="N", i="E", j="P", k="A", l="L", m="M",
                        n="E", o="R", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        elif self.level == 509:
            self.hintff(a="G", b="A", c="R", d="G", e="A", f="N", g="T", h="O", i="S", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 510:
            self.hintff(a="A", b="M", c="E", d="R", e="I", f="C", g="A", h="C", i="H", j="A", k="V", l="E", m="Z",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 0])
        elif self.level == 511:
            self.hintff(a="C", b="H", c="I", d="T", e="O", f="N", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 512:
            self.hintff(a="R", b="E", c="E", d="D", e="R", f="I", g="C", h="H", i="A", j="R", k="D", l="S", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 513:
            self.hintff(a="C", b="H", c="A", d="R", e="L", f="E", g="S", h="X", i="A", j="V", k="I", l="E", m="R",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 0])
        elif self.level == 514:
            self.hintff(a="W", b="A", c="N", d="D", e="A", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 515:
            self.hintff(a="W", b="A", c="N", d="D", e="A", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 516:
            self.hintff(a="M", b="O", c="R", d="D", e="O", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 517:
            self.hintff(a="D", b="O", c="C", d="T", e="O", f="R", g="S", h="T", i="R", j="A", k="N", l="G", m="E",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 0])
        elif self.level == 518:
            self.hintff(a="W", b="A", c="N", d="D", e="A", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 519:
            self.hintff(a="C", b="H", c="R", d="I", e="S", f="T", g="I", h="N", i="E", j="P", k="A", l="L", m="M",
                        n="E", o="R", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        elif self.level == 520:
            self.hintff(a="P", b="E", c="G", d="G", e="Y", f="C", g="A", h="R", i="T", j="E", k="R", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 521:
            self.hintff(a="8", b="3", c="8", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 522:
            self.hintff(a="D", b="A", c="R", d="K", e="H", f="O", g="L", h="D", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 523:
            self.hintff(a="N", b="A", c="M", d="O", e="R", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 524:
            self.hintff(a="N", b="A", c="M", d="O", e="R", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 525:
            self.hintff(a="N", b="A", c="M", d="O", e="R", f="A", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 526:
            self.hintff(a="H", b="A", c="I", d="T", e="I", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 527:
            self.hintff(a="T", b="A", c="L", d="O", e="C", f="A", g="N", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 528:
            self.hintff(a="T", b="A", c="L", d="O", e="K", f="I", g="T", h="E", i="S", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 529:
            self.hintff(a="A", b="T", c="L", d="A", e="N", f="T", g="I", h="C", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 530:
            self.hintff(a="T", b="O", c="U", d="S", e="S", f="A", g="I", h="N", i="T", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 531:
            self.hintff(a="T", b="V", c="A", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 532:
            self.hintff(a="2", b="0", c="1", d="2", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 533:
            self.hintff(a="G", b="O", c="B", d="I", e="R", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 534:
            self.hintff(a="M", b="O", c="B", d="I", e="U", f="S", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 535:
            self.hintff(a="S", b="Y", c="L", d="V", e="I", f="E", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 536:
            self.hintff(a="S", b="Y", c="L", d="V", e="I", f="E", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 537:
            self.hintff(a="T", b="E", c="M", d="P", e="A", f="D", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 538:
            self.hintff(a="R", b="O", c="V", d="O", e="N", f="N", g="A", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 539:
            self.hintff(a="V", b="O", c="I", d="D", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 540:
            self.hintff(a="R", b="O", c="V", d="O", e="N", f="N", g="A", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 541:
            self.hintff(a="M", b="O", c="B", d="I", e="U", f="S", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 542:
            self.hintff(a="S", b="I", c="F", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 543:
            self.hintff(a="A", b="L", c="I", d="O", e="T", f="H", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 544:
            self.hintff(a="M", b="A", c="R", d="C", e="S", f="P", g="E", h="C", i="T", j="O", k="R", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 545:
            self.hintff(a="W", b="E" ,c="N", d="D", e="Y", f="S", g="P", h="E", i="C", j="T", k="O", l="R", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 546:
            self.hintff(a="R", b="A", c="N", d="D", e="A", f="L", g="L", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 547:
            self.hintff(a="A", b="R", c="T", d="H", e="U", f="R", g="H", h="A", i="R", j="R", k="O", l="W", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 548:
            self.hintff(a="A", b="R", c="T", d="H", e="U", f="R", g="H", h="A", i="R", j="R", k="O", l="W", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 549:
            self.hintff(a="L", b="A", c="Y", d="L", e="A", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 550:
            self.hintff(a="J", b="A", c="C", d="K", e="L", f="O", g="C", h="K", i="E", j="L", k="Y", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 551:
            self.hintff(a="L", b="A", c="Y", d="L", e="A", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 552:
            self.hintff(a="3", b="2", c="", d="", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 553:
            self.hintff(a="S", b="T", c="E", d="V", e="E", f="N", g="G", h="R", i="A", j="N", k="T", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 554:
            self.hintff(a="T", b="A", c="W", d="E", e="R", f="E", g="T", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 555:
            self.hintff(a="A", b="M", c="M", d="I", e="T", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 556:
            self.hintff(a="K", b="H", c="O", d="N", e="S", f="H", g="U", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 557:
            self.hintff(a="P", b="E", c="G", d="G", e="Y", f="C", g="A", h="R", i="T", j="E", k="R", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 558:
            self.hintff(a="H", b="Y", c="D", d="R", e="A", f="S", g="T", h="O", i="M", j="P", k="E", l="R", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 559:
            self.hintff(a="W", b="A", c="T", d="C", e="H", f="E", g="R", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 560:
            self.hintff(a="U", b="L", c="T", d="R", e="O", f="N", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 561:
            self.hintff(a="K", b="I", c="L", d="L", e="M", f="O", g="N", h="G", i="E", j="R", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 562:
            self.hintff(a="C", b="H", c="R", d="I", e="S", f="T", g="I", h="N", i="E", j="P", k="A", l="L", m="M",
                        n="E", o="R", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        elif self.level == 563:
            self.hintff(a="T", b="C", c="H", d="A", e="L", f="L", g="A", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 564:
            self.hintff(a="L", b="O", c="K", d="I", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 565:
            self.hintff(a="U", b="K", c="R", d="A", e="I", f="N", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 566:
            self.hintff(a="H", b="A", c="N", d="K", e="P", f="Y", g="M", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 567:
            self.hintff(a="U", b="A", c="T", d="U", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 568:
            self.hintff(a="J", b="A", c="C", d="K", e="R", f="U", g="S", h="S", i="E", j="L", k="L", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 569:
            self.hintff(a="J", b="A", c="C", d="K", e="R", f="U", g="S", h="S", i="E", j="L", k="L", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 570:
            self.hintff(a="V", b="E", c="R", d="U", e="S", f="S", g="A", h="", i="", j="", k="L", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 571:
            self.hintff(a="E", b="L", c="S", d="A", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 572:
            self.hintff(a="M", b="A", c="N", d="T", e="I", f="S", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 573:
            self.hintff(a="K", b="A", c="M", d="A", e="L", f="A", g="K", h="H", i="A", j="N", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 574:
            self.hintff(a="A", b="A", c="M", d="I", e="R", f="K", g="H", h="A", i="N", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 575:
            self.hintff(a="B", b="R", c="U", d="N", e="O", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 576:
            self.hintff(a="K", b="A", c="R", d="E", e="E", f="M", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 577:
            self.hintff(a="K", b="A", c="M", d="A", e="L", f="A", g="K", h="H", i="A", j="N", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 578:
            self.hintff(a="K", b="R", c="E", d="E", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 579:
            self.hintff(a="N", b="O", c="O", d="R", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 580:
            self.hintff(a="S", b="A", c="N", d="A", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 581:
            self.hintff(a="H", b="A", c="S", d="A", e="N", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 582:
            self.hintff(a="A", b="I", c="S", d="H", e="A", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 583:
            self.hintff(a="A", b="I", c="S", d="H", e="A", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 584:
            self.hintff(a="N", b="A", c="K", d="I", e="A", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 585:
            self.hintff(a="T", b="O", c="D", d="D", e="P", f="H", g="E", h="L", i="P", j="S", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 586:
            self.hintff(a="S", b="K", c="A", d="A", e="R", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 587:
            self.hintff(a="D", b="A", c="R", d="E", e="D", f="E", g="V", h="I", i="L", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 588:
            self.hintff(a="L", b="U", c="K", d="E", e="J", f="A", g="C", h="O", i="B", j="S", k="O", l="N", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 589:
            self.hintff(a="W", b="O", c="N", d="G", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 590:
            self.hintff(a="A", b="B", c="O", d="M", e="I", f="N", g="A", h="T", i="I", j="O", k="N", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])
        elif self.level == 591:
            self.hintff(a="J", b="A", c="N", d="N", e="I", f="F", g="E", h="R", i="W", j="A", k="L", l="T", m="E",
                        n="R", o="S", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 13, 14, 15])
        elif self.level == 592:
            self.hintff(a="K", b="A", c="T", d="E", e="B", f="I", g="S", h="H", i="O", j="P", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0])
        elif self.level == 593:
            self.hintff(a="S", b="W", c="O", d="R", e="D", f="S", g="M", h="A", i="N", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 594:
            self.hintff(a="L", b="U", c="C", d="K", e="Y", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 595:
            self.hintff(a="E", b="C", c="H", d="O", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 596:
            self.hintff(a="K", b="I", c="N", d="G", e="P", f="I", g="N", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 597:
            self.hintff(a="L", b="U", c="K", d="E", e="J", f="A", g="C", h="O", i="B", j="S", k="O", l="N", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0, 0])
        elif self.level == 598:
            self.hintff(a="M", b="A", c="Y", d="A", e="L", f="O", g="P", h="E", i="Z", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0])
        elif self.level == 599:
            self.hintff(a="E", b="C", c="H", d="O", e="", f="", g="", h="", i="", j="", k="", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif self.level == 600:
            self.hintff(a="B", b="R", c="U", d="C", e="E", f="B", g="A", h="N", i="N", j="E", k="R", l="", m="",
                        n="", o="", lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0])




















































































class coin_move:
    def __init__(self):
        pass
    def sasi(self,lst8 = [],lst10 = [],lst7 = [],lst6 = [],lst4 = [],lst5 = [],lst12 = [],lst9 = [],lst11 = [],lst3 = [],lst2 = [],lst15 = [],lst14 = []):

        self.count += 1
        if self.level in (lst10):
            self.coin(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10, l=None, m=None, k=None, n=None, o=None)

        elif self.level in (lst7):
            self.coin(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=None, i=None, j=None, k=None, l=None, m=None, n=None, o=None)

        elif self.level in (lst6):
            self.coin(a=1, b=2, c=3, d=4, e=5, f=6, g=None, h=None, i=None, j=None, k=None, l=None, m=None, n=None,
                      o=None)
        elif self.level in (lst8):
            self.coin(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=None, j=None, k=None, l=None, m=None, n=None, o=None)
        elif self.level in (lst4):
            self.coin(a=1, b=2, c=3, d=4, e=None, f=None, g=None, h=None, i=None, j=None, k=None, l=None, m=None, n=None, o=None)
        elif self.level in (lst5):
            self.coin(a=1, b=2, c=3, d=4, e=5, f=None, g=None, h=None, i=None, j=None, k=None, l=None, m=None, n=None, o=None)
        elif self.level in (lst12):
            self.coin(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10, k=11, l=12, m=None,  n=None, o=None)
        elif self.level in (lst9):
            self.coin(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=None, l=None, m=None, k=None, n=None, o=None)
        elif self.level in (lst11):
            self.coin(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10, k=11, l=None, m=None, n=None, o=None)
        elif self.level  in (lst3):
            self.coin(a=1, b=2, c=3, d=None, e=None, f=None, g=None, h=None, i=None, j=None, k=None, l=None, m=None, n=None, o=None)
        elif self.level in (lst2):
            self.coin(a=1, b=2, c=None, d=None, e=None, f=None, g=None, h=None, i=None, j=None, k=None, l=None, m=None,n=None, o=None)
        elif self.level in (lst15):
            self.coin(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10, k=11, l=12, m=13,  n=14, o=15)
        elif self.level in (lst14):
            self.coin(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10, k=11, l=12, m=13,  n=14, o=None)
        else:
            print("c")
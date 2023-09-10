from kivy.storage.jsonstore import JsonStore


class coininc():
    def __init__(self):
        pass
    def win_coin(self):
        print(int(self.ids.coins.text))
        self.coin_js = JsonStore("coins_win.json")
        self.all_coins = int(self.ids.coins.text)
        self.all_coins += 10
        self.coin_js.put("coin_base",coins = self.all_coins)
        self.get_coin = self.coin_js.get("coin_base")["coins"]
        self.ids.coins.text = str(self.get_coin)
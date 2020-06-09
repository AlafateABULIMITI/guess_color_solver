import random


class Strategy:
    def __init__(self, color_pool, color_num):
        super().__init__()
        self.color_pool = color_pool
        self.color_num = color_num

    def random_stra(self):
        return random.sample(self.color_pool, self.color_num)

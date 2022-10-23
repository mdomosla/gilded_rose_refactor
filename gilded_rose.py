# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_sell_in(self, item):
        item.sell_in -= 1

    def update_quality(self, item):
        if item.sell_in < 0:
            item.quality -= 2
        else:
            item.quality -= 1

    def adjust_quality(self, item):
        if "Sulfuras" not in item.name:
            if item.quality > 50:
                item.quality = 50
        if item.quality < 0:
            item.quality = 0

    def update_sulfuras_item(self, item):
        item.quality = 80

    def update_brie_item(self, item):
        self.update_sell_in(item)
        item.quality += 1
        self.adjust_quality(item)

    def update_backstage_pass(self, item):
        self.update_sell_in(item)
        if item.sell_in in range(6, 11):
            item.quality += 2
        elif item.sell_in in range(0, 6):
            item.quality += 3
        elif item.sell_in == -1:
            item.quality = 0
        else:
            item.quality += 1
        self.adjust_quality(item)

    def update_conjured(self, item):
        self.update_sell_in(item)
        item.quality -= 2
        self.adjust_quality(item)

    def update_items(self):
        for item in self.items:
            item_name = item.name
            item_actions = {
                "Sulfuras": self.update_sulfuras_item,
                "Aged Brie": self.update_brie_item,
                "Backstage pass": self.update_backstage_pass,
                "Conjured": self.update_conjured
            }
            item_found_in_actions = False
            for key in item_actions.keys():
                if key in item_name:
                    item_found_in_actions = True
                    key_to_run = key
            if item_found_in_actions:
                item_actions[key_to_run](item)
            else:
                self.update_sell_in(item)
                self.update_quality(item)
                self.adjust_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

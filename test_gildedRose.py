import pytest
from grappa import should

from gilded_rose import Item, GildedRose


class TestGildedRose:

    @pytest.mark.parametrize("item_name, item_sell_in, item_quality, exp_sell_in, exp_quality", [("foo", 0, 0, -1, 0),
                                                                                                 ("foo", 0, 2, -1, 0),
                                                                                                 ("foo", 0, 4, -1, 2),
                                                                                                 ("foo", 1, 2, 0, 1),
                                                                                                 ("foo", 10, 30, 9, 29),
                                                                                                 ("foo", 10, 55, 9, 50)
                                                                                                 ])
    def test_foo_item(self, item_name, item_sell_in, item_quality, exp_sell_in, exp_quality):
        items = [Item(item_name, item_sell_in, item_quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items()
        items[0].name | should.be.equal.to(item_name)
        items[0].sell_in | should.be.equal.to(exp_sell_in)
        items[0].quality | should.be.equal.to(exp_quality)

    @pytest.mark.parametrize("item_name, item_sell_in, item_quality, exp_sell_in, exp_quality",
                             [("Aged Brie", 0, 0, -1, 1),
                              ("Aged Brie", 0, 2, -1, 3),
                              ("Aged Brie", 0, 49, -1, 50),
                              ("Aged Brie", -1, 55, -2, 50),
                              ("Aged Brie", 10, 30, 9, 31),
                              ("Aged Brie", 10, 80, 9, 50)
                              ])
    def test_brie(self, item_name, item_sell_in, item_quality, exp_sell_in, exp_quality):
        items = [Item(item_name, item_sell_in, item_quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items()
        items[0].name | should.be.equal.to(item_name)
        items[0].sell_in | should.be.equal.to(exp_sell_in)
        items[0].quality | should.be.equal.to(exp_quality)

    @pytest.mark.parametrize("item_name, item_sell_in, item_quality, exp_sell_in, exp_quality",
                             [("Sulfuras", 0, 0, 0, 80),
                              ("Sulfuras", 0, 2, 0, 80),
                              ("Sulfuras", 0, 4, 0, 80),
                              ("Sulfuras", 1, 2, 1, 80),
                              ("Sulfuras", 10, 30, 10, 80),
                              ("Sulfuras", 10, 80, 10, 80)
                              ])
    def test_sulfuras(self, item_name, item_sell_in, item_quality, exp_sell_in, exp_quality):
        items = [Item(item_name, item_sell_in, item_quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items()
        items[0].name | should.be.equal.to(item_name)
        items[0].sell_in | should.be.equal.to(exp_sell_in)
        items[0].quality | should.be.equal.to(exp_quality)

    @pytest.mark.parametrize("item_name, item_sell_in, item_quality, exp_sell_in, exp_quality",
                             [("Backstage pass", 0, 0, -1, 0),
                              ("Backstage pass", 0, 10, -1, 0),
                              ("Backstage pass", 1, 4, 0, 7),
                              ("Backstage pass", 1, -1, 0, 2),
                              ("Backstage pass", 5, 44, 4, 47),
                              ("Backstage pass", 10, 10, 9, 12),
                              ("Backstage pass", 10, 49, 9, 50),
                              ("Backstage pass", 6, 10, 5, 13),
                              ("Backstage pass", 11, 10, 10, 12),
                              ("Backstage pass", 12, 10, 11, 11),
                              ("Backstage pass", 7, 10, 6, 12),
                              ("Backstage pass", 1, 50, 0, 50),
                              ("Backstage pass", 0, 50, -1, 0),
                              ("Backstage pass", 7, 50, 6, 50)
                              ])
    def test_backstage(self, item_name, item_sell_in, item_quality, exp_sell_in, exp_quality):
        items = [Item(item_name, item_sell_in, item_quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items()
        items[0].name | should.be.equal.to(item_name)
        items[0].sell_in | should.be.equal.to(exp_sell_in)
        items[0].quality | should.be.equal.to(exp_quality)

    @pytest.mark.parametrize("item_name, item_sell_in, item_quality, exp_sell_in, exp_quality",
                             [("Conjured", 0, 0, -1, 0),
                              ("Conjured", 0, 10, -1, 8),
                              ("Conjured", 1, 4, 0, 2),
                              ("Conjured", 10, 50, 9, 48),
                              ("Conjured", 10, 55, 9, 50),
                              ("Conjured", 10, 51, 9, 49),
                              ("Conjured", 10, 1, 9, 0),
                              ])
    def test_conjured(self, item_name, item_sell_in, item_quality, exp_sell_in, exp_quality):
        items = [Item(item_name, item_sell_in, item_quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items()
        items[0].name | should.be.equal.to(item_name)
        items[0].sell_in | should.be.equal.to(exp_sell_in)
        items[0].quality | should.be.equal.to(exp_quality)

    @pytest.mark.parametrize("item_name, item_sell_in, item_quality, exp_sell_in, exp_quality",
                             [("+5 Dexterity Vest", 10, 20, 9, 19),
                              ("Aged Brie", 2, 0, 1, 1),
                              ("Elixir of the Mongoose", 5, 7, 4, 6),
                              ("Sulfuras, Hand of Ragnaros", 0, 80, 0, 80),
                              ("Sulfuras, Hand of Ragnaros", -1, 80, -1, 80),
                              ("Backstage passes to a TAFKAL80ETC concert", 15, 20, 14, 21),
                              ("Backstage passes to a TAFKAL80ETC concert", 10, 49, 9, 50),
                              ("Backstage passes to a TAFKAL80ETC concert", 5, 49, 4, 50),
                              ("Conjured Mana Cake", 3, 6, 2, 4)
                              ])
    def test_fixture(self, item_name, item_sell_in, item_quality, exp_sell_in, exp_quality):
        items = [Item(item_name, item_sell_in, item_quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items()
        items[0].name | should.be.equal.to(item_name)
        items[0].sell_in | should.be.equal.to(exp_sell_in)
        items[0].quality | should.be.equal.to(exp_quality)
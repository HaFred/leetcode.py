# class CategoryTree:
#
#     def __init__(self):
#         pass
#
#     def add_category(self, category, parent):
#         pass
#
#     def get_children(self, parent):
#         return []


class CategoryTree:
    def __init__(self):
        self.categories = {}  # hashmap

    def add_category(self, category, parent):
        self.categories[category] = parent
        if (parent not in self.categories.keys() and parent is not None) or category in self.categories.values():
            raise KeyError

    def get_children(self, category):
        return [child for child, parent in self.categories.items() if parent == category]  # list comprehension


if __name__ == "__main__":
    c = CategoryTree()
    c.add_category('A', None)
    c.add_category('B', 'A')
    c.add_category('C', 'A')
    print(','.join(c.get_children('A') or []))

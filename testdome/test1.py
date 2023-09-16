from enum import Enum


class Side(Enum):
    none = 0
    left = 1
    right = 2


class ChainLink:

    def __init__(self):
        self._left = None
        self._right = None

    def append(self, link):
        if self._right is not None: raise Exception('Link already connected!')
        self._right = link
        link._left = self

    # def longer_side(self, num_left=0, num_right=0):
    #     if self._left is not None:
    #         self.left_nodes = num_left
    #         self.left_nodes += 1
    #         self._left.longer_side(self.left_nodes, self.right_nodes)
    #     if self._right is not None:
    #         self.right_nodes = num_right
    #         self.right_nodes += 1
    #         self._right.longer_side(self.left_nodes, self.right_nodes)
    #     if self.left_nodes > self.right_nodes:
    #         return Side.left
    #     elif self.left_nodes < self.right_nodes:
    #         return Side.right
    #     else:
    #         return Side.none

    def longer_side(self):
        left_count = self.count_links(self._left, 'left')
        right_count = self.count_links(self._right, 'right')

        if left_count > right_count:
            return Side.left
        elif right_count > left_count:
            return Side.right
        else:
            return Side.equal

    @staticmethod
    def count_links(node, direction=None):
        count = 0
        while node:
            count += 1
            if direction == 'left':
                node = node._left
            elif direction == 'right':
                node = node._right
            else:
                raise Exception('Direction not specified!')
        return count


if __name__ == "__main__":
    left = ChainLink()
    middle = ChainLink()
    right = ChainLink()
    left.append(middle)
    middle.append(right)
    print(left.longer_side() == Side.right)

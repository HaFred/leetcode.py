# class MovingTotal:
#     def __init__(self):
#         self.numbers = []
#
#     def append(self, new_numbers):
#         self.numbers.extend(new_numbers)
#
#     def contains(self, target):
#         return any(target == sum(self.numbers[i:i+3]) for i in range(len(self.numbers) - 2))

class MovingTotal:
    def __init__(self):
        self.numbers = []
        self.sums = set()

    def append(self, new_numbers):
        for num in new_numbers:
            if len(self.numbers) >= 3:
                # self.sums.remove(sum(self.numbers[:3]))
                self.sums.add(sum(self.numbers))
                self.numbers.pop(0)
            self.numbers.append(num)

    def contains(self, target):
        return target in self.sums


if __name__ == "__main__":
    movingtotal = MovingTotal()

    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))

    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
    expected = [True,
                True,
                False,
                False,
                True,
                True,
                True,
                False]

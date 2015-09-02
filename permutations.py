
class PermutationBuilder():

    def __buildPermutations(self, level, things, permutation, result):
        result1 = []
        if level < len(things):
            thing = things[level]
            for i in range(0, len(thing)):
                item = thing[i]
                p = list(permutation)
                p.append(item)
                if (level == len(things) - 1):
                    result.append(p)
                else:
                    self.__buildPermutations(level + 1, things, p, result)


    def getPermutations(self, items):
        result = []
        self.__buildPermutations(0, items, [], result)
        return result

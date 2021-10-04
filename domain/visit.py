from datatype.enums import DartMultiplier


class Dart:
    def __init__(self, multiplier, segment):
        self.multiplier = multiplier  # see data type . enums . DartType ;o p t i o n a l l y c r e a t e t h i s a s a p r o p e r t y and v a l i d a t e
        self.segment = segment  # 1 t o 2 0 , 0 f o r mi s s / double−b u l l /s i n g l e −b u l l


    def get_score(self):
        return self.multiplier * self.segment

    def to_string(self):
        segment = None
        if self.segment is 25:
            segment = "BULL"

        if self.segment is 0:
            return "MISS"

        return DartMultiplier(self.multiplier).name + "−" + str(self.segment) if segment is None else segment


class Visit:
    def __init__(self):
        self.darts = []  # Limi ted t o 3 Dart el em e n t s f o r most games

    def __init__(self, darts):
        self.darts = []  # Limi ted t o 3 Dart el em e n t s f o r most games
        self.add_darts(darts)

    def add_dart(self, dart):
        self.darts.append(Dart(dart[0], dart[1]))

    def add_darts(self, darts):
        for dart in darts:
            self.add_dart(dart)

    def remove_trailing_darts(self, index):
        del self.darts[index:]

    # For many d a r t games , the t o t a l s c o r e from 3 d a r t s w i l l be r el e v a n t ,though t h e r e i s an argument f o r pl a ci n g t h i s
    # i n each s p e c i f i c type o f d a r t game where i t i s most r e l e v a n t

    def get_total(self):
        total = 0
        for dart in self.darts:
            total += dart.get_score()
        return total

    def to_string(self):
        output = ""
        for dart in self.darts:
            output += dart.to_string() + " "
        return output

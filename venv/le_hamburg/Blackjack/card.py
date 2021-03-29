class Card():
    def __init__(self, value:int):
        self.name = self.setName(value)
        self.value = self.setValue(self.name)

    def setName(self, x:int):
        
        switcher = {
            1: 'ace',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'jack',
            12: 'king',
            13: 'queen'
        }

        return switcher[x]

    def setValue(self, s:str):
        
        switcher = {
            'ace': 1,
            'aceEl': 11,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9, 
            'ten': 10,
            'jack': 10,
            'king': 10,
            'queen': 10,
        }

        return switcher[s]
    

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return str(self)
class PlayerCharacter:
    membership = True #Class Object Attribute
    def __init__(self,name='anonymous',age=0):
        if(age > 18):
            self.name = name #attributes
            self.age = age
    
    def run(self):
        print('run')
        return 'done'
    
    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(num1, num2):
        return num1 + num2
    
player1 = PlayerCharacter(name = "Cindy",age = 15)
print(player1.name,player1.age)
player2 = PlayerCharacter(name = "Tom",age = 20)
print(player2.name,player2.age)
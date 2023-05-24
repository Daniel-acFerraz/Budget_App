class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.total = 0

    #def __repr__(self):
    #    return '{self.__class__.__name__}({self.name}, {self.ledger}) {self.total}'.format(self=self)

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        moneyLeft = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}"+ "\n"

        return title+items+f"Total: {self.total}"

    def deposit(self, amount, description = ""):
        self.total += amount
        obj = {"amount": amount, "description": description}
        self.ledger.append(obj)


    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            obj = {"amount": -amount, "description": description}
            self.total -= amount
            self.ledger.append(obj)
            return True
        
        else: return False       

    def get_balance(self):
        return self.total
    
    def transfer(self, amount, otherCategory=""):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + otherCategory.name)
            otherCategory.deposit(amount, "Transfer from " + self.name)
            return True
        
        else: return False

    def check_funds(self, amount):
         if amount > self.total: return False
         else: return True


def create_spend_chart(categories):
    catExpenses = dict()
    totalExpenses = 0

    for category in categories:
        catExpenses[category] = 0
        for transition in category.ledger:
            if transition['amount'] < 0:
                totalExpenses -= transition['amount']
                totalExpenses = round(totalExpenses, 2)
                catExpenses[category] = round(catExpenses.get(category, 0) - transition['amount'], 2)
    
    chartLen = (len(categories)*3)+4
    h = 100
    chart = "Percentage spent by category\n"
    while h >= 0:
        chart += f"{h:>3}|"
        graphicMark = ""
        graphic = ""
        for category in categories:
            categoryPercentage = (catExpenses[category]/totalExpenses)*100

            if categoryPercentage > h-5:
                graphicMark = "o"
            else: graphicMark = " "
            graphic += f" {graphicMark} "
            if category == categories[-1]:
                graphic += "\n"
        chart += graphic
        h -= 10        
    whiteSpaces = "    "
    underBar = f"{whiteSpaces:-<{chartLen}}-"
    chart = chart + underBar + "\n"

    catLengths = list()
    for category in categories:
        catLengths.append(len(category.name))
    maxLen = max(catLengths)
    i = 0
    catList = list()
    while i < maxLen:
        for category in categories:
            if i < len(category.name):
                catList.append(category.name[i])
            else:
                catList.append(" ")
        i += 1
    j = 0
    jump = len(categories)
    catLine = "    "
    while j < len(catList):
        for category in categories:
            catLine += f" {catList[j]} "
            j += 1
            if j % jump == 0:
                catLine += "\n    "

    chart += catLine
    return chart


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print()
print(clothing)
print()
print(auto)
print()
print(create_spend_chart([food, clothing, auto]))
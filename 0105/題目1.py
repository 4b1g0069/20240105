class Person:
    # 創建Person類別的建構子
    # 設置三個屬性name, age, occupation
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    # 副函式定義，名稱為display 能顯示出他們的姓名/年齡/職業。   
    def display(self):
        print(f"姓名: {self.name} 年齡: {self.age} 職業: {self.occupation}.")
     
    # 副函式定義，名稱為change_occupation 能更改目前的職業
    def change_occupation(self, new_occupation):
        self.occupation = new_occupation
        print(f"{self.name}的新職業{self.occupation}.")

    # 副函式定義，名稱為Birthday，他們增長一歲
    def Birthday(self):
        self.age += 1
        print(f"{self.name}的生日到了，他的目前年紀:{self.age}")

# 創建三個Person物件，分別是張三/李四/王五和輸入他們年齡與職業
person1 = Person("張三", 25, "司機")
person2 = Person("李四", 30, "老師")
person3 = Person("王五", 20, "學生")

# 呼叫副函式
person1.display()                  # 顯示張三的姓名/年齡/職業
person1.change_occupation("保全")  # 張三更改職業
person1.Birthday()                 # 張三過生日
print("\n")
person2.display()                  # 顯示李四的姓名/年齡/職業
person2.change_occupation("律師")  # 李四更改職業
person2.Birthday()                 #李四過生日
print("\n")
person3.display()                  # 顯示"王五的姓名/年齡/職業 
person3.change_occupation("超商店員")  # 王五更改職業
person3.Birthday()                 #王五過生日

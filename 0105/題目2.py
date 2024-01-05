class Luggage:
   # 創建Luggage類別的建構子
   # 設置五屬性id, weight, departure, destination, name
    def __init__(self, id, weight, departure, destination, name):
        self.id = id
        self.weight = weight
        self.departure = departure
        self.destination = destination
        self.name = name
        
   # 副函式定義，名稱為display 能顯示出他們所有資訊 
    def dispaly(self):
        print(f"行李ID:{self.id}行李重量:{self.weight}行李出發地:{self.departure}行李目的地:{self.destination}行李所屬旅客姓名:{self.name}")
   
   # 副函式定義，名稱為change_id 能更改目前的id
    def change_id(self, new_id): 
        self.id = new_id
        print(f"新id為{self.id}.")

    # 副函式定義，名稱為change_weight 能更改目前的重量
    def change_weight(self, new_weight): 
        self.weight = new_weight
        print(f"新重量為{self.weight}.")

    # 副函式定義，名稱為change_departure能更改目前的出發地
    def change_departure(self, new_departure): 
        self.departure = new_departure
        print(f"新出發地為{self.departure}.")

   # 副函式定義，名稱為change_destination能更改目前的目的地
    def change_destination(self, new_destination): 
        self.destination = new_destination
        print(f"新目的地為{self.destination}.")

   # 副函式定義，名稱為change_name 能更改目前的旅客姓名      
    def change_name(self, new_name): 
        self.name = new_name
        print(f"新旅客姓名為{self.name}.")

# 創建三個Luggage物件，和輸入他們的資訊
luggage1 = Luggage("0001", 2.5, "台北", "大阪","張三")
luggage2 = Luggage("0002", 2.8, "高雄", "羽田","李四")
luggage3 = Luggage("0003", 1.8, "台南", "仁川","王五")

luggage1.dispaly()          # 顯示luggage1的所有資訊 
luggage1.change_id("2138")  # 改變luggage1的id 
luggage1.change_weight(2.7) # 改變luggage1的重量
luggage1.change_departure("高雄")   # 改變luggage1的出發地
luggage1.change_destination("中部") # 改變luggage1的目的地
luggage1.change_name("王XX")    #改變lluggage1目前的旅客姓名 

luggage2.dispaly()          # 顯示luggage2的所有資訊 
luggage2.change_id("1549")   # 顯示luggage2的所有資訊 
luggage2.change_weight(2.2) # 改變luggage2的重量
luggage2.change_departure("台北") # 改變luggage2的出發地
luggage2.change_destination("關西") # 改變luggage2的目的地
luggage2.change_name("陳XX") #改變lluggage2目前的旅客姓名 

luggage3.dispaly()           # 顯示luggage3的所有資訊 
luggage3.change_id("1255")  # 改變luggage3的id
luggage3.change_weight(2.5  )# 改變luggage3的重量
luggage3.change_departure("花連")   # 改變luggage3的出發地
luggage3.change_destination("金浦") # 改變luggage3的目的地
luggage2.change_name("陳XX")        #改變lluggage3目前的旅客姓名 
luggage3.change_name("林xx")        #改變lluggage3目前的旅客姓名 


class BoardingPass:
   # 創建BoardingPass類別的建構子
   # 設置七屬性id, name, id, time, gate_number, seat, pieces_of_luggage, luggage_id
    def __init__(self, name, id, time, gate_number, seat, pieces_of_luggage, luggage_id):
        self.name = name
        self.id = id
        self.time = time    
        self.gate_number = gate_number
        self.seat = seat    
        self.pieces_of_luggage = pieces_of_luggage
        self.luggage_id = luggage_id

    # 副函式定義，名稱為display 能顯示出他們所有資訊     
    def dispaly(self):
        print(f"旅客姓名:{self.name}登機證編號:{self.id}登機時間:{self.time}登機門編號:{self.gate_number}座位位置:{self.seat}行李件數:{self.pieces_of_luggage}行李ID:{self.luggage_id}")

    # 副函式定義，名稱為change_name 能更改目前的旅客姓名      
    def change_name(self, new_name): 
        self.name = new_name
        print(f"旅客新姓名為{self.name}.")

   # 副函式定義，名稱為change_id 能更改目前的登機證編號         
    def change_id(self, new_id): 
        self.id = new_id
        print(f"新登機證編號為{self.id}.")

  # 副函式定義，名稱為change_time 能更改目前的登機時間     
    def change_time(self, new_time): 
        self.time = new_time
        print(f"新登機時間為{self.time}.")

   # 副函式定義，名稱為change_destination 能更改目前的登機門編號      
    def change_destination(self, new_gate_number): 
        self.gate_number = new_gate_number
        print(f"登機門編號{self.gate_number}.")

   # 副函式定義，名稱為change_seat 能更改目前的座位位置:      
    def change_seat(self, new_seat): 
        self.seat = new_seat
        print(f"新座位位置為{self.seat}.")

   # 副函式定義，名稱為change_pieces_of_luggage( 能更改目前的行李件數      
    def change_pieces_of_luggage(self, new_pieces_of_luggage): 
        self.pieces_of_luggage = new_pieces_of_luggage
        print(f"新行李件數為{self.pieces_of_luggage}.")

   # 副函式定義，名稱為change_name 能更改目前的行李ID      
    def change_new_luggage_id(self, new_luggage_id): 
        self.luggage_id = new_luggage_id
        print(f"新行李ID為{new_luggage_id}.")

# 創建三個BoardingPass物件，和輸入他們的資訊
boardingpass1 = BoardingPass("Bob", "S1250","3p.m.", "12345B", "C1", 1, "234567C")
boardingpass2 = BoardingPass("Andy", "S2200", "5a.m.", "23456B","D4", 2,"567890C" )

boardingpass1.dispaly()                         # 顯示boardingpass1的所有資訊 
boardingpass1.change_name("Bobby")              # 改變boardingpass1的旅客姓名
boardingpass1.change_id("S2000")                # 改變boardingpass1的登機證編號 
boardingpass1.change_time("6p.m")               # 改變boardingpass1的登機時間
boardingpass1.change_destination("54321B")      # 改變boardingpass1的登機門編號
boardingpass1.change_seat("C2")                 # 改變boardingpass1的座位位置
boardingpass1.change_pieces_of_luggage(2)       # 改變boardingpass1的行李件數
boardingpass1.change_new_luggage_id("765432C")  # 改變boardingpass1的行李ID 

boardingpass2.dispaly()                          # 顯示boardingpass2的所有資訊 
boardingpass2.change_name("Anndry")              #改變boardingpass2的旅客姓名
boardingpass2.change_id("S1800")                 #改變boardingpass2的登機證編號 
boardingpass2.change_time("4a.m")                # 改變boardingpass2的登機時間
boardingpass2.change_destination("65432B")       # 改變boardingpass2的登機門編號
boardingpass2.change_seat("D1")                 # 改變boardingpass2的座位位置
boardingpass2.change_pieces_of_luggage(3)       # 改變boardingpass2的行李件數
boardingpass2.change_new_luggage_id("098765C")  # 改變boardingpass2的行李ID 


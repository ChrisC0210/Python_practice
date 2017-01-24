class Parent():
    #Parent類別
    #定義初始接收資料
    def __init__(self, last_name, eye_color):
        print ("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print ("Last name: " + self.last_name)
        print ("Eye color: " + self.eye_color)

class Child(Parent):
    #Child類別，繼承class Parent()
    #定義初始接收資料
    def __init__(self, last_name, eye_color, toys):
        print ("Child Constructor Called")
        #取得父類別的last_name和eye_color做為初始資料
        #遺傳，或是說繼承
        super().__init__(last_name, eye_color)
        self.toys = toys
    
    # method overriding
    #複寫掉父類別的show_info方法
    def show_info(self):
        print ("Last name: " + self.last_name)
        print ("Eye color: " + self.eye_color)
        print ("Number of toys: " + str(self.toys))
    
def main():
    david_lee = Parent("Lee", "blue")#設定父親資料
    print (david_lee.last_name)#印出父親得到的姓
    david_lee.show_info()#執行Parent的show_info()方法
    print("----------------------------")

    andy_lee = Child("Lee", "blue", 3)#兒子的資料
    print (andy_lee.last_name)#因為class Child()繼承了class Parent的方法所以可以直接印出
    print (andy_lee.toys)#印出得到的參數
    andy_lee.show_info()#執行Child的show_info()方法

if __name__ == '__main__':
    main()
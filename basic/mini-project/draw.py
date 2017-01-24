import turtle

def draw():
    window = turtle.Screen()
    window.bgcolor("red")#背景紅色

    brad = turtle.Turtle()
    brad.shape("turtle")#用烏龜畫圖
    brad.color("yellow")#顏色_黃色
    brad.speed(2)#速度
    brad.forward(50)#前進(50)
    brad.right(90)#右轉(90度)
    brad.forward(200)#前進(200)
    brad.left(90)#左轉(90度)
    brad.forward(100)#前進(100)

    brad = turtle.Turtle()
    brad.shape("classic")#用標準畫圖
    brad.color("green")#顏色_綠色
    brad.backward(150)#後退(150)
    brad.right(60)#右轉(60度)
    brad.forward(150)#前進(1200)
    brad.right(60)#右轉(60度)
    brad.backward(150)#前進(150)
    brad.left(60)#右轉(60度)

    angie = turtle.Turtle()
    angie.shape("arrow")#箭頭畫圖
    angie.color("blue")#藍色
    angie.circle(100)#畫圓(大小)

    window.exitonclick()#被點擊就關閉

def main():
    draw()

if __name__ == '__main__':
    main()
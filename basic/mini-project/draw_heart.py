from turtle import *
#轉向()
def curvemove():
    #向右轉走1，執行200次(200度)
    for i in range(200):
        right(1)
        forward(1)
color('red','pink')        
begin_fill()#開始填滿
#左下
left(140)#左邊140度
forward(111.65)#前進(111.65)
#左上
curvemove()#轉向畫半圓()

left(120)#左轉120度
#右上
curvemove()#轉向畫半圓()
#右下
forward(111.65)#前進(111.65)

end_fill()#填滿完畢
done()#完成之後不跳掉
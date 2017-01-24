import time
from datetime import datetime
import webbrowser
#指定判斷次數，用1表示一次倒數
total_breaks = 1
break_count = 0
#開始時印出開始時間
print ("This program started on " + str(datetime.now()))
#開始倒數，條件為：在break_count<total_breaks前執行
while(break_count < total_breaks):
	#暫停(秒數)
    time.sleep(10)
    #開啟指定網頁
    webbrowser.open('https://www.youtube.com/watch?v=u57d4_b_YgI')
    #設定下一迴圈條件，否則會無限迴圈
    break_count += 1
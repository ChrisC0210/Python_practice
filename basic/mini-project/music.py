import webbrowser

class Music():
    """
    This class provides a way to store music information 
    """
    VALID_RATINGS = ["A", "B", "C"]
    #儲存輸入變數
    def __init__(self, music_name, music_url):
        self.music_name = music_name
        self.music_url = music_url
    #play_music()：開一個新視窗，網址是輸入的網址
    def play_music(self):
        webbrowser.open(self.music_url)

def main():
    #呼叫class Music()傳入兩個參數
    better_together = Music("better together", "https://www.youtube.com/watch?v=u57d4_b_YgI")
    better_together.play_music()#使用play_music()的方法
    print (Music.VALID_RATINGS)#印出class Music()的變數 VALID_RATINGS
    print (Music.__doc__)#會把指定的區域中開頭的三引號註解區塊印出

if __name__ == '__main__':
    main()
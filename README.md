# sele_fb
### Now
#### main_test.py 
以最上層貼文作留言爬取，結果目錄在\output的text_split.json & text_splitted.json，前者為尚未留言處理，後者為將留言部分作名字替換。

#### emotion_get.py
作心情爬取，需提供心情頁面網址、資料夾名稱、檔案名稱，執行時一序執行angry_get.py & love_get.py，個別將除怒、愛心的心情物件刪除再作展開、爬取，並以共同儲存於單一json檔。

儲存目錄：\output\CrossAnalyze\資料夾名稱\檔案名稱.json



### Question
1. 針對單一貼文的展開留言無法執行(留言數龐大,目前以迴圈作控制)
2. 留言的查看更多沒辦法順利點擊(OK)
3. 尚未處理圖片留言(OK)
4. 因3. 現階段未對留言者與留言內容作分開存放(圖片留言會被視為None)(OK)
5. 因3. 產出的留言為抓取整個留言區塊的文字部分(包含 留言者名稱 + 留言內容 + (...查看更多))(完成處理)
6. 有出現過 [WinError 10061] 無法連線，因為目標電腦拒絕連線。ERROR

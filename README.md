# InCore 使用說明
## 啟動方式
1. 在Incore的根目錄，使用python 3.6，啟動src中的apps.py檔案
2. 指令 ```python3.6 ./src/apps.py```
## 資料庫位置和刪除方式
* 資料庫有分成兩個部分，一個是SQLdata，另一個是file system
  * SQL是指標資料，指向file system的資料，方便查找
  * ```InCore/models```會儲存訓練模型
  * ```InCore/db```會儲存訓練用資料
  * file system 是用來儲存實際的資料，會儲存在```InCore/db 和 InCore/models  ```中，這些要進行手動刪除。
  * **記得對SQLdata中的InCore和inanalysis資料刪除後，file system的資料一定要清理，否則這些資料會變成dead weight，而且日後不好分辨**
* 演算法儲存的位置在 ```/src/service/analyticService/core/analyticCore/*```的資料夾中，可以刪除的部分資料需要py和json檔案一並刪除，系統檔案型態必須要留下來，**千萬不要刪掉開頭是in開頭的py檔案和json，那些是是內建的演算法**。

## 重要參數
* 在 ```InCore/serverStatus.cfg ```

| 名稱      | 目的      | 功能     |
| -------- | -------- | -------- |
|analyticModuleUploadDeadline|上傳演算法期限|超過這個日期，所有人就無法上傳演算法|
## 上傳網址生成
* 在incore的目錄中，建立成一個名為allowSubmit.csv的檔案，之後以這樣的形式格式生成。
* 這個CSV不需要開頭，直接打內容。
| 學員學號      | ID       | 
| -------- | -------- | 
|學員名稱|非重複的id，建議使用學生學號+unixtime的hash值|

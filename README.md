# Selenium 動態爬蟲作業：MangaZ

## 一、作業說明

這次作業主要是練習使用 Python 的 Selenium 套件來操作 Chrome 瀏覽器，並從 MangaZ 網站取得圖片。

練習的內容包括開啟網頁、尋找和點擊按鈕、切換瀏覽器分頁、等待網頁載入，以及使用迴圈將圖片截圖儲存下來。

原本老師提供的是填空練習，完成並確認可以執行後，我再把程式整理成不同的 `def` 函式，讓每個部分負責不同的工作。

另外也加入了自動建立資料夾、避免重複儲存相同圖片，以及限制翻頁次數的功能，避免程式一直重複執行。

## 二、專案資料夾

```text
selenium-mangaz-assignment/
├── project_mangaz/
│   ├── __init__.py
│   ├── browser.py
│   └── scraper.py
├── downloaded_manga/       # 存放下載的圖片
├── assignment01_scraper.py  # 主程式
├── requirements.txt         # 需要安裝的套件
├── .gitignore               # 不上傳的檔案
└── README.md                # 作業說明
```

其中 `downloaded_manga` 會在執行程式時自動建立，裡面存放擷取下來的漫畫圖片。這些圖片只保留在自己的電腦，不會上傳到 GitHub。

## 三、安裝與執行方式

需要先安裝 Python（建議 3.10 以上）和 Google Chrome。

在 VS Code 開啟專案資料夾後，可以在終端機輸入以下指令：

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python assignment01_scraper.py
```

如果 PowerShell 無法啟動虛擬環境，也可以直接使用：

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe assignment01_scraper.py
```

程式執行後會自動開啟 Chrome，進入指定的漫畫網頁，並依照設定的流程截圖及翻頁。

執行完成後，可以到 `downloaded_manga` 資料夾查看圖片。

如果之後網站的按鈕或網頁結構改變，可能需要重新修改程式裡尋找元素的方式。

## 四、程式功能介紹

這次把程式分成幾個函式，方便自己閱讀和修改。

- `create_driver()`：設定並開啟 Chrome 瀏覽器。
- `enter_reader()`：進入漫畫網頁，點擊閱讀按鈕並切換分頁。
- `capture_visible_images()`：找出目前顯示的圖片，截圖並儲存，避免重複存入相同圖片。
- `go_to_next_page()`：尋找下一頁按鈕並點擊。
- `scrape_pages()`：使用迴圈重複截圖和翻頁，直到符合停止條件。
- `main()`：把前面的功能串起來，並在結束時關閉瀏覽器。

## 五、執行結果

這次實際執行後，成功開啟 MangaZ 網站，並將圖片儲存到指定資料夾。

**執行結果：**
- 成功儲存 31 張不同的圖片。
- 圖片依序命名為 `manga_page_0000.png` 到 `manga_page_0030.png`。
- 圖片統一存放在 `downloaded_manga` 資料夾。
- 程式最後因為等待下一頁按鈕逾時而停止，並正常關閉瀏覽器。

## 六、這次學到的東西

這次練習讓我比較了解 Selenium 是怎麼操作網頁的。

以前比較常直接看到程式執行的結果，這次透過老師提供的填空練習，開始認識 `find_element()`、`find_elements()`、`click()`、`WebDriverWait()` 等指令的用途。

另外也練習到 `while True` 迴圈、`try...except` 錯誤處理，以及使用 `def` 把比較長的程式拆成不同功能。

目前程式還有可以改進的地方，例如翻頁後使用 `time.sleep(2)` 等待圖片載入，雖然這次執行成功，但如果網路比較慢，兩秒可能不夠。

之後如果有機會，可以再練習判斷圖片是否真的載入完成，而不是只依靠固定等待時間。

這次也練習了如何整理 Python 專案資料夾，並透過 GitHub 保存程式碼。

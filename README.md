# Selenium 動態爬蟲作業：MangaZ

## 專案說明
使用 Python 與 Selenium 練習 Chrome 瀏覽器自動化、CSS Selector、部分連結文字定位、視窗切換、顯式等待、元素截圖、迴圈與例外處理。程式已整理為 `def` 函式，並加入圖片去重與安全翻頁上限。

僅對有權擷取與保存的內容執行；遵守目標網站使用條款。漫畫圖片不會提交至 GitHub。

## 結構
```text
selenium-mangaz-assignment/
├── project_mangaz/
│   ├── __init__.py
│   ├── browser.py
│   └── scraper.py
├── downloaded_manga/       # 執行後自動建立；不提交 Git
├── assignment01_scraper.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 安裝與執行
需要 Python 3.10+ 與 Google Chrome。在專案根目錄執行：

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python assignment01_scraper.py
```

如果 PowerShell 不允許啟用虛擬環境，可直接使用 `.venv\Scripts\python.exe -m pip install -r requirements.txt` 與 `.venv\Scripts\python.exe assignment01_scraper.py`。

Selenium Manager 通常會自動管理相容的 ChromeDriver。若網站結構、文字或按鈕有變動，需更新 `project_mangaz/scraper.py` 的定位器。固定 2 秒等待並不保證所有圖片都已載入；必要時可改用圖片狀態等待。

## 函式分工
- `create_driver()`：Chrome 設定與啟動。
- `enter_reader()`：開啟目標頁面、點擊閱讀、切換視窗。
- `capture_visible_images()`：儲存可見圖片元素的 PNG 截圖，依內容雜湊去重。
- `go_to_next_page()`：等待並點擊下一頁。
- `scrape_pages()`：整合循環、終止條件與安全上限。
- `main()`：建立資料夾、執行流程、確保關閉瀏覽器。

## 成果與提交
執行後圖片會儲存在本機 `downloaded_manga/`。以圖片瀏覽器或投影片播放圖片，使用 OBS 錄製成果影片。依老師要求另外提交影片與 GitHub Repo 連結。GitHub 只提交原始碼與說明，不提交下載圖片。

## 注意
這是課堂練習；已完成程式碼整理與語法檢查，但仍需在實際瀏覽器環境中驗證。若讀取器在原分頁導覽、載入過慢或有額外驗證，可能需調整等待條件。設定的 Chrome 121 User-Agent 可能與實際瀏覽器版本不同。

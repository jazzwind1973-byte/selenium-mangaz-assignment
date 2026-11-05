"""Entry point for the Selenium dynamic-page assignment.

Run only with content you are permitted to capture and retain.
"""
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from project_mangaz.browser import create_driver
from project_mangaz.scraper import enter_reader, scrape_pages


def main():
    output_dir = Path(__file__).resolve().parent / "downloaded_manga"
    output_dir.mkdir(parents=True, exist_ok=True)
    driver = None
    try:
        driver = create_driver()
        enter_reader(driver, WebDriverWait(driver, 10))
        total = scrape_pages(driver, output_dir)
        print(f"完成，共儲存 {total} 張不同的圖片；位置：{output_dir}")
    finally:
        if driver is not None:
            driver.quit()
            print("瀏覽器已關閉。")


if __name__ == "__main__":
    main()

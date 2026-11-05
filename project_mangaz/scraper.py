"""Navigation and element-screenshot logic for an authorized reading session."""
import hashlib
import time
from pathlib import Path

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


BOOK_URL = "https://www.mangaz.com/book/detail/157901"
IMAGE_SELECTOR = "div.page_image img.image"
NEXT_SELECTOR = "div.flip.flip-left"


def enter_reader(driver, wait):
    driver.get(BOOK_URL)
    print("Page Title:", driver.title)
    old_handles = set(driver.window_handles)
    start_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.open-viewer.book-begin.ga")
    ))
    start_button.click()
    try:
        wait.until(lambda d: len(set(d.window_handles) - old_handles) > 0)
        new_handle = next(iter(set(driver.window_handles) - old_handles))
        driver.switch_to.window(new_handle)
    except TimeoutException:
        # Some sites navigate in the same tab.
        print("未偵測到新視窗，繼續使用目前視窗。")
    read_now = wait.until(EC.element_to_be_clickable(
        (By.PARTIAL_LINK_TEXT, "すぐに読む")
    ))
    read_now.click()


def capture_visible_images(driver, output_dir, count, seen_hashes):
    """Save screenshots of visible image elements, skipping identical bytes."""
    for element in driver.find_elements(By.CSS_SELECTOR, IMAGE_SELECTOR):
        if not element.is_displayed():
            continue
        image_bytes = element.screenshot_as_png
        digest = hashlib.sha256(image_bytes).hexdigest()
        if digest in seen_hashes:
            continue
        target = output_dir / f"manga_page_{count:04d}.png"
        target.write_bytes(image_bytes)
        seen_hashes.add(digest)
        count += 1
        print(f"成功擷取頁面並儲存為: {target}")
    return count


def go_to_next_page(driver, wait, delay=2):
    try:
        next_page = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, NEXT_SELECTOR)
        ))
        next_page.click()
        print("已點擊下一頁，等待畫面載入...")
        time.sleep(delay)
        return True
    except TimeoutException:
        print("等待下一頁按鈕逾時，停止翻頁。")
        return False


def scrape_pages(driver, output_dir, max_turns=200):
    wait = WebDriverWait(driver, 10)
    count = 0
    seen_hashes = set()
    unchanged_turns = 0
    for turn in range(max_turns):
        before = count
        count = capture_visible_images(driver, output_dir, count, seen_hashes)
        if count == before:
            unchanged_turns += 1
        else:
            unchanged_turns = 0
        if unchanged_turns >= 3:
            print("連續三次未取得新圖片，停止以避免無窮迴圈。")
            break
        if not go_to_next_page(driver, wait):
            break
    else:
        print(f"已達安全翻頁上限 {max_turns} 次。")
    return count

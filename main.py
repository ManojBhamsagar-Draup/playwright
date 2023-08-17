from undetected_playwright import stealth_sync
from playwright.sync_api import sync_playwright, BrowserContext


headless = False


def run(context: BrowserContext):
    page = context.new_page()
    page.goto("https://nl.indeed.com/jobs?q=Industrieel+ingenieur&fromage=35&limit=50&start=0&sort=date&filter=0")

    _suffix = "-headless" if headless else "-headful"
    page.screenshot(path=f"result/sannysoft{_suffix}.png", full_page=True)
    result = page.content()
    print(result)


def bytedance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        stealth_sync(context)
        run(context)


if __name__ == '__main__':
    try:
        print("bytedance")
        bytedance()
    except Exception as e:
        print(e)
        print("bytedance failed")

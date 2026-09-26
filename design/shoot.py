import os
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
URL = "file://" + os.path.join(HERE, "screens.html")
OUT = os.path.join(HERE, "screens")
os.makedirs(OUT, exist_ok=True)

names = {
    "s0f": "00a-existing-fitness-home.png",
    "s0m": "00b-faye-tab-landing.png",
    "s1": "01-therapist-discovery.png",
    "s2": "02-booking-confirmation.png",
    "s3": "03-mood-dashboard.png",
    "s4": "04-content-resources.png",
}

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium/chrome-linux/chrome" if os.path.exists("/opt/pw-browsers/chromium/chrome-linux/chrome") else None)
    page = browser.new_page(viewport={"width": 1800, "height": 1000}, device_scale_factor=2)
    page.goto(URL)
    page.wait_for_timeout(300)
    for sel, fname in names.items():
        el = page.locator(f"#{sel}")
        el.screenshot(path=os.path.join(OUT, fname))
        print("saved", fname)
    # also a combined overview shot
    page.screenshot(path=os.path.join(OUT, "00-overview.png"), full_page=True)
    browser.close()
print("done")

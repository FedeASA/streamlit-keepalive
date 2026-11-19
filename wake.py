"""Visita las apps de Streamlit y, si están dormidas, aprieta el botón para despertarlas."""
import re
import sys
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

URLS = [
    "https://formulariorma.streamlit.app/",
    "https://rma-altavista.streamlit.app/",
]

WAKE_BTN = re.compile(r"get this app back up", re.I)


def wake(page, url: str) -> bool:
    print(f"-> {url}")
    page.goto(url, wait_until="domcontentloaded", timeout=90_000)
    page.wait_for_timeout(8_000)

    btn = page.get_by_role("button", name=WAKE_BTN)
    if btn.count() > 0:
        print("   Dormida. Despertando...")
        btn.first.click()
        try:
            btn.first.wait_for(state="detached", timeout=180_000)
        except PWTimeout:
            print("   ERROR: no se despertó en 3 minutos")
            return False
        page.wait_for_timeout(15_000)  # dejar que la app termine de arrancar
        print("   Despierta.")
    else:
        # Mantener la sesión abierta un rato para que cuente como tráfico real
        page.wait_for_timeout(15_000)
        print("   Ya estaba activa.")
    return True


def main() -> int:
    ok = True
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for url in URLS:
            try:
                ok &= wake(page, url)
            except Exception as e:
                print(f"   ERROR: {e}")
                ok = False
        browser.close()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

from playwright.sync_api import sync_playwright

# Verwende Playwright, um den Browser zu starten und die Seite zu laden
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    # Die Login-URL und die URL für die Zielseite
    login_url = 'https://melete.webuntis.com/WebUntis/index.do#/basic/login'
    target_url = 'https://melete.webuntis.com/timetable-contact-hours'

    # Anmeldung durchführen
    page.goto(login_url)
    page.fill('input[name="username"]', '200135@studierende.htl-donaustadt.at')
    page.fill('input[name="password"]', 'I am the one 1')
    page.click('button[type="submit"]')  # Je nach Button-Selector anpassen

    # Zugriff auf die Zielseite nach der Anmeldung
    page.goto(target_url)
    print(f"Aktuelle URL: {page.url}")

    # Warten auf JavaScript, das die Inhalte lädt
    page.wait_for_load_state('networkidle')

    # Drucke den gesamten HTML-Inhalt (erst 2000 Zeichen für eine schnelle Vorschau)
    html_content = page.content()
    print(html_content[:2000])

    # Schließe den Browser
    browser.close()
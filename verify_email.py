
import asyncio
import os
from playwright.async_api import async_playwright

async def verify_template(page, filename):
    print(f"Verifying {filename}...")
    await page.goto(f'file:///app/{filename}')

    # Capture header/content
    await page.screenshot(path=f'/home/jules/verification/{filename.replace(".", "_")}_top.png')

    # Test hover on CTA button
    cta = page.locator('.cta-button')
    if await cta.count() > 0:
        await cta.hover()
        await asyncio.sleep(0.5) # Wait for transition
        await page.screenshot(path=f'/home/jules/verification/{filename.replace(".", "_")}_cta_hover.png')

    # Scroll to bottom and capture footer
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    await asyncio.sleep(0.5)
    await page.screenshot(path=f'/home/jules/verification/{filename.replace(".", "_")}_footer.png')

async def main():
    if not os.path.exists('/home/jules/verification'):
        os.makedirs('/home/jules/verification')

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 800, 'height': 800})

        await verify_template(page, 'email_template.html')
        await verify_template(page, 'correo2.html')

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

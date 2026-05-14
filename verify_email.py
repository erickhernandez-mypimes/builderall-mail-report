
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f'file:///app/email_template.html')
        # Wait for fonts to load
        await page.wait_for_load_state('networkidle')
        await page.screenshot(path='/home/jules/verification/email_template_full.png', full_page=True)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

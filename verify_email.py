
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f'file:///app/email_template.html')
        await page.screenshot(path='/home/jules/verification/email_template.png')

        await page.goto(f'file:///app/correo2.html')
        await page.screenshot(path='/home/jules/verification/correo2.png')

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

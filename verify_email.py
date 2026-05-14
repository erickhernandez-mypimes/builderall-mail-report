
import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    # Ensure the verification directory exists
    os.makedirs('/home/jules/verification', exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Process email_template.html
        await page.goto(f'file:///app/email_template.html')
        await page.screenshot(path='/home/jules/verification/email_template.png')

        # Process correo2.html
        await page.goto(f'file:///app/correo2.html')
        await page.screenshot(path='/home/jules/verification/correo2.png')

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

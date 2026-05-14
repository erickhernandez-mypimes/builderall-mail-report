
import asyncio
import os
from playwright.async_api import async_playwright

async def verify_template(page, filename):
    filepath = f'file://{os.getcwd()}/{filename}'
    await page.goto(filepath)
    # Scroll to bottom to ensure footer is loaded/visible if needed (though full_page should handle it)
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    screenshot_path = f'/home/jules/verification/{filename.replace(".html", ".png")}'
    await page.screenshot(path=screenshot_path, full_page=True)
    print(f'Screenshot saved for {filename} at {screenshot_path}')

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        templates = ['email_template.html', 'correo2.html']
        for template in templates:
            await verify_template(page, template)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

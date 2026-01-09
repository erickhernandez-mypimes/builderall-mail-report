
import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        email_templates = [
            "email_sequence_1.html",
            "email_sequence_2.html",
            "email_sequence_3.html",
            "email_sequence_4.html",
            "email_sequence_5.html"
        ]

        output_dir = "/home/jules/verification"
        os.makedirs(output_dir, exist_ok=True)

        for template_file in email_templates:
            await page.goto(f'file:///app/{template_file}')
            screenshot_path = os.path.join(output_dir, template_file.replace(".html", ".png"))
            await page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

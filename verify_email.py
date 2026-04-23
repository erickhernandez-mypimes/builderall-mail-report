
import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Verify email_template.html
        await page.goto('file:///app/email_template.html')
        await expect(page.locator('a[href*="instagram"]')).to_have_attribute('title', 'Instagram')
        await expect(page.locator('a[href*="facebook"]')).to_have_attribute('title', 'Facebook')
        await expect(page.locator('a[href*="linkedin"]')).to_have_attribute('title', 'LinkedIn')
        print("email_template.html verified successfully.")

        # Verify correo2.html
        await page.goto('file:///app/correo2.html')
        await expect(page.locator('a[href*="instagram"]')).to_have_attribute('title', 'Instagram')
        await expect(page.locator('a[href*="facebook"]')).to_have_attribute('title', 'Facebook')
        await expect(page.locator('a[href*="linkedin"]')).to_have_attribute('title', 'LinkedIn')
        print("correo2.html verified successfully.")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

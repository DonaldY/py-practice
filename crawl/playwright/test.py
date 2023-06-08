import asyncio
from playwright.async_api import async_playwright
import time
###异步尝试获取海关数据
async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium]:
            browser = await browser_type.connect_over_cdp("http://localhost:9222")
            page = await browser.new_page()
            await page.goto('http://credit.customs.gov.cn/ccppwebserver/pages/ccpp/html/declCompany.html')
            time.sleep(5)
            await page.wait_for_load_state("load")
            # # 4
            # await page.wait_for_load_state("load")
            await page.click('#apanageName')
            time.sleep(5)
            await page.wait_for_load_state("load")
            await page.type('#apanageName1.form-control.autocompleter-node','44')
            time.sleep(10)
            await page.wait_for_load_state("load")
            await page.click('.autocompleter-item-selected')
            time.sleep(5)
            await page.wait_for_load_state("load")
            await page.click('a.layui-layer-btn0')
            time.sleep(5)
            await page.wait_for_load_state("load")
            await page.click('input.serch_ico')
            time.sleep(10)
            # await page.screenshot(path=f'screenshot-{browser_type.name}.png')
            # print(await page.title())
            await browser.close()

asyncio.run(main());
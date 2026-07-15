const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('http://localhost:8080/index.html?obs=true&test=true');
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'obs_test.png' });

  await page.goto('http://localhost:8080/index.html?obs=true');
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'obs_notest.png' });
  await browser.close();
})();

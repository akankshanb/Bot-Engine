'use strict';

const puppeteer = require('puppeteer');

const htmlContent = `
  <!doctype html>
  <html>
    <head><meta charset='UTF-8'><title>Test</title></head>
    <body>Test</body>
  </html>
`;

puppeteer.launch({ headless: false }).then(async (browser) => {
  const page = await browser.newPage();
  await page.setContent(htmlContent);
  setTimeout(async () => {
    console.log(await page.content());
  }, 3000);
});

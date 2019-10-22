const puppeteer = require('puppeteer');
const { expect }  = require('chai');

const loginEmail = process.env.MATTERMOST_EMAIL;
const loginPassword = process.env.MATTERMOST_PWD;

async function login(browser, url) {
  const page = await browser.newPage();

  await page.goto(url, {waitUntil: 'networkidle0'});

  // Login
  await page.type('input[id=loginId]', loginEmail);
  await page.type('input[id=loginPassword]', loginPassword);
  await page.click('button[id=loginButton]');

  // Wait for redirect
  await page.waitForNavigation();
  return page;
}


describe('Testing PlotBot usecases', function () {

    let browser;
    let page;
    let mattermost_url;

    this.timeout(5000000);

    beforeEach(async () => {
        browser = await puppeteer.launch({headless:true});
        mattermost_url = "http://ec2-18-217-150-234.us-east-2.compute.amazonaws.com:8065/plotbotteam/channels/off-topic";
        page = await login( browser, `${mattermost_url}/login` );
    });

    //afterEach(async () => {
      //  await browser.close();
    //});

    it('It should greet back', async () => {
        var list = [,]

        await page.waitForSelector('#post_textbox');
        await page.focus('#post_textbox')
        await page.keyboard.type( "@plotbot hi" );
        await page.keyboard.press('Enter');
        let promise = new Promise((res, rej) => {
          setTimeout(() => res("Waiting for the Response!"), 5000)
        });
        let waiting = await promise;
        await page.waitForSelector('.post__body');
        const output = await page.evaluate(() => Array.from(
          document.getElementsByClassName('post__body'), e => e.innerText));
        var result = output[output.length-1];
        expect(result).to.match(/^Hi/);

        await browser.close();
    });

    it('Happy flow when users asks for sample scatter plot', async () => {
        await page.waitForSelector('#post_textbox');
        await page.focus('#post_textbox')
        await page.keyboard.type( "sample scatterplot" );
        await page.keyboard.press('Enter');
        let promise = new Promise((res, rej) => {
          setTimeout(() => res("Waiting for the Response!"), 5000)
        });
        let waiting = await promise;
        await page.waitForSelector('.post__body');
        const output = await page.evaluate(() => Array.from(
          document.getElementsByClassName('post__body'), e => e.innerText));
        var result = output[output.length-1];
        expect(result).to.match(/scatterplot_code\.png\n.*\nscatterplot_graph\.png/);

        await browser.close();
    });

    it('Alternate flow when user requests for sample countplot which is not understood by PlotBot', async () => {
        await page.waitForSelector('#post_textbox');
        await page.focus('#post_textbox')
        await page.keyboard.type( "sample countplot" );
        await page.keyboard.press('Enter');
        let promise = new Promise((res, rej) => {
          setTimeout(() => res("Waiting for the Response!"), 5000)
        });
        let waiting = await promise;
        await page.waitForSelector('.post__body');
        const output = await page.evaluate(() => Array.from(
          document.getElementsByClassName('post__body'), e => e.innerText));
        var result = output[output.length-1];
        expect(result).to.match(/not available/);

        await browser.close();
    });

    it('happy flow when user asks to plot a graph by giving dataset', async () => {
        await page.waitForSelector('#post_textbox');
        await page.focus('#post_textbox')
        await page.keyboard.type( "plot scatterplot" );

        const example = await page.$('#fileUploadButton');
        const attach = await page.evaluateHandle(el => el.nextElementSibling, example);
        await attach.uploadFile('test/dataset.csv')
        let promise1 = new Promise((res, rej) => {
          setTimeout(() => res("Waiting for the Response!"), 5000)
        });
        let waiting1 = await promise1;

        await page.keyboard.press('Enter');
        let promise = new Promise((res, rej) => {
          setTimeout(() => res("Waiting for the Response!"), 5000)
        });
        let waiting = await promise;

        await page.waitForSelector('.post__body');
        const output = await page.evaluate(() => Array.from(
          document.getElementsByClassName('post__body'), e => e.innerText));
        var result = output[output.length-1];
        expect(result).to.match(/\.png/);

        await browser.close();
    });

    it('Alternate flow when user requests to plot countplot which is not understood by PlotBot', async () => {
      await page.waitForSelector('#post_textbox');
      await page.focus('#post_textbox')
      await page.keyboard.type( "plot countplot" );

      const example = await page.$('#fileUploadButton');
      const attach = await page.evaluateHandle(el => el.nextElementSibling, example);
      await attach.uploadFile('test/dataset.csv')
      let promise1 = new Promise((res, rej) => {
        setTimeout(() => res("Waiting for the Response!"), 5000)
      });
      let waiting1 = await promise1;

      await page.keyboard.press('Enter');
      let promise = new Promise((res, rej) => {
        setTimeout(() => res("Waiting for the Response!"), 5000)
      });
      let waiting = await promise;

      await page.waitForSelector('.post__body');
      const output = await page.evaluate(() => Array.from(
        document.getElementsByClassName('post__body'), e => e.innerText));
      var result = output[output.length-1];
      expect(result).to.match(/Please provide the correct/);
      await browser.close();
    });
/*
    it('Happy flow when user requests for all his plotted graphs', async () => {
        await page.waitForSelector('#post_textbox');
        await page.focus('#post_textbox')
        await page.keyboard.type( "retrieve plots" );
        await page.keyboard.press('Enter');
        let promise = new Promise((res, rej) => {
          setTimeout(() => res("Waiting for the Response!"), 10000)
        });
        let waiting = await promise;
        await page.waitForSelector('.post__body');
        const output = await page.evaluate(() => Array.from(
          document.getElementsByClassName('post__body'), e => e.innerText));
        var result = output[output.length-1];
        expect(result).to.match(/scatter.png/);

        await browser.close();
    });
*/
});

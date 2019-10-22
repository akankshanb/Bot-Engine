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
        mattermost_url = "http://ec2-18-217-150-234.us-east-2.compute.amazonaws.com:8065/plotbotteam/channels/mounika_trials";
        page = await login( browser, `${mattermost_url}/login` );
        //await page.goto(`${mattermost_url}`, {waitUntil: 'networkidle0'});
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
        await page.waitForSelector('.post__body');

        //await page.waitForSelector('h2 a');
        const output = await page.evaluate(() => Array.from(
          document.getElementsByClassName('post__body'), e => e.innerText));
        console.log(output[output.length-1]);
        var result = output[output.length-1];
        //console.log(expect(result).to.match(/^Hi*|^Sorry*/|));
        expect(result).to.match(/^Sorry*|^Hi*/);

        await browser.close();
    });

});

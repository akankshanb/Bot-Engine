const puppeteer = require('puppeteer')

const loginEmail = process.env.MATTERMOST_EMAIL;
const loginPassword = process.env.MATTERMOST_PWD;
const mattermostUrl = 'http://ec2-18-217-150-234.us-east-2.compute.amazonaws.com:8065/plotbotteam/channels/mounika_trials'

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

async function postMessage(page, msg)
{
  // Waiting for page to load
  await page.waitForSelector('#post_textbox');

  // Focus on post textbox and press enter.
  await page.focus('#post_textbox')
  await page.keyboard.type( msg );
  await page.keyboard.press('Enter');
  await page.waitForSelector('.post__body');

  const tweets = await page.evaluate(() => Array.from(document.getElementsByClassName('post__body'), e => e.innerText));

var len = tweets.length
console.log(tweets[len-1]);
console.log("***************************");

tweets.forEach(tweet => {
  console.log(tweet);
  console.log("-----------------")
});
}


(async () => {

  const browser = await puppeteer.launch({headless: false, args: ["--no-sandbox", "--disable-web-security"]});
  let page = await login( browser, `${mattermostUrl}/login` );
  await postMessage(page, "@plotbot hi" );

  // const html = await page.content(); // serialized HTML of page DOM.
  // browser.close();
})()

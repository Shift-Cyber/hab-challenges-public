const fs = require('fs');
const puppeteer = require('puppeteer');

const targetDomain = 'http://192.168.1.65';
var targetURL = '';

// load the url
fs.readFile('target_url.txt', 'utf8', function(err, data) {
  targetURL = data;
});

async function visitWithCookie() {  
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.setCookie({
    'name': 'flag',
    'value': 'flag{mirroring_to_the_max}',
    'url': targetDomain
  });

  // visit the page
  if (targetURL !== '') {
    console.log(targetURL);
    await page.goto(targetURL); // Replace with your URL

    // clear the file
    fs.writeFile('target_url.txt', '', function(err) {});
  }

  await browser.close();
}

visitWithCookie();

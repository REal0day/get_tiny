# get_tiny

I wrote a quick program that would randomly go through tinyurl.com and reverse the url shortening process. This will generate an extension from 1-6 alphanumeric characters and send a GET request to that url. If it successfully is redirected, it will download the file.html, and save the original tinyurl in the tinyurl.log file. All failed requests will get sent to failed.log
I could go deeper into this project, but what I realized was that links with fewer characters were generated earlier, so most links are from 2005 - 2009. The later, the older the links usually are.

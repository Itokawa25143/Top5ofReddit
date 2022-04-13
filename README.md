# Top5ofReddit

Flask API that displays today's five most popular posts in submitted subreddits.

Data is scraped from Reddit and is stored in static files (today-subreddit.csv).


## Prerequisites

You have to change __CLIENT_ID__, __SECRET_KEY__ and __USER_AGENT__ credentials in myapp.py

- To get __CLIENT_ID__, __SECRET_KEY__ and __USER_AGENT__ credentials you have to have Reddit account. 

  - Go to: https://www.reddit.com/prefs/apps

  - Scroll down and choose __"create another app"__

  - Fill the form

  - Create

  - You can see your new application in the list where you can click the __edit__ button.

  - Now you can read your __Client ID__ and __Client Secret__.

    >  <img width="223" alt="image" src="https://user-images.githubusercontent.com/27806574/163260721-56442022-38ac-4853-b4e5-8e24f677930a.png">
 
 
Clone the repo: 

```
git clone https://github.com/Itokawa25143/Top5ofReddit.git
cd Top5ofReddit 
```
To start using the Top5ofReddit API, you will need to install the following dependencies on your system: 
```
apt install python3-pip
pip install Flask
pip install pandas
pip install praw
```
Verify the installation: 
```
python3 -m flask --version
```
> <img width="110" alt="image" src="https://user-images.githubusercontent.com/27806574/163237084-863738cf-a4a4-4a01-a345-f04e1de496f8.png"> 
 

## Start app:
```
python3 myapp.py
```

Open http://localhost:5000/

Insert subreddit's name

> <img width="212" alt="image" src="https://user-images.githubusercontent.com/27806574/163234029-78ca111a-b849-4402-9e32-196f1270a244.png">


Submit:

> <img width="752" alt="image" src="https://user-images.githubusercontent.com/27806574/163234083-547ccfe3-cc90-42cc-b900-1bdc9776c169.png">


Also a file named date-subreddit'sname.csv is created in folder called __static/__:

> <img width="329" alt="image" src="https://user-images.githubusercontent.com/27806574/163235501-cd4b4c8e-5113-45e1-b39c-e0aa5c66e095.png">





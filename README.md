# Top5ofReddit
Flask API to get the top 5 posts from subreddit with user input

## Usage

Clone the repo: 

```
git clone https://github.com/Itokawa25143/Top5ofReddit.git

cd Top5ofReddit 
```

## Prerequisites

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


## Usage
API to get the top 5 posts from subreddits.

Start app:
```
python3 myapp.py
```

Open http://localhost:5000/

Insert subreddit's name

> <img width="212" alt="image" src="https://user-images.githubusercontent.com/27806574/163234029-78ca111a-b849-4402-9e32-196f1270a244.png">


Submit:

> <img width="752" alt="image" src="https://user-images.githubusercontent.com/27806574/163234083-547ccfe3-cc90-42cc-b900-1bdc9776c169.png">


Also a file named date-subreddit'sname.csv is created:

> <img width="329" alt="image" src="https://user-images.githubusercontent.com/27806574/163235501-cd4b4c8e-5113-45e1-b39c-e0aa5c66e095.png">





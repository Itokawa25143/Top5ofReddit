import flask
import requests
import csv
import praw
import pandas as pd
from os import path
from datetime import date
from flask import Flask, json, render_template, send_file, request, url_for, Response

app = Flask(__name__)

@app.route("/")
def ask():
  input = render_template('form.html')
  return input

@app.route("/data", methods = ['POST', 'GET'])
def data():
  if request.method == 'GET':
    return f"The URL /data is accessed directly. Try going to '/sub'."

  if request.method == 'POST':
    getinput = request.form['subreddit']
    input = getinput.lower()
    today = date.today().strftime('%Y-%m-%d')
    filename = today + "-" + input + ".csv"
    fileloc = "static/" + filename
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    if path.exists(fileloc):
      data = pd.read_csv(fileloc)
      pd.set_option('display.max_columns', None)
      return render_template('table.html', tables=[data.to_html()], titles=[''], message=input)

    else:
      reddit_read_only = praw.Reddit(
             client_id ='CLIENT_ID',
         client_secret ='CLIENT_SECRET',
            user_agent = 'TOP 5 of subreddits by /u/PurpleExplorer_I')

      subreddit  = reddit_read_only.subreddit(input)
      posts      = subreddit.top(limit=5)
      fileloc    = "static/" + filename
      posts_dict = {"Title": [],
                    "Score": [],
                    "Total comments": [],
                    "URL": []
                    }
      for post in posts:
        posts_dict["Title"].append(post.title)
        posts_dict["Score"].append(post.score)
        posts_dict["Total comments"].append(post.num_comments)
        posts_dict["URL"].append(post.url)
        top_posts = pd.DataFrame(posts_dict)
        top_posts
        top_posts.to_csv(fileloc, index=False)
      data = pd.read_csv(fileloc)
      return render_template('table.html', tables=[data.to_html()], titles=[''], message=input)

app.run(host='localhost', port=5000, debug=True)

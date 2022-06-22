# Twitter Sentiment Analysis on FlaskApp :notebook:
In this project I created a twitter sentiment analysis on flask app (web base).

# Directory Tree :cactus:
```bash
.
├── images
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   └── 5.png
├── main.py
├── README.md
├── static
│   ├── logo.png
│   └── style.css
└── templates
    ├── index.html
    └── sentiment.html

3 directories, 12 files
```

# Technology used in Project :hotsprings:
<img target="_blank" src="https://github.com/joshua/technology/blob/master/Flask.png" width="300">     <img target="_blank" src="https://github.com/joshua/technology/blob/master/pandas.png" width="300">    <img target="_blank" src="https://github.com/joshua/technology/blob/master/numpy.png" width="200">      <img target="_blank" src="https://github.com/joshua/technology/blob/master/tweepy.webp" width="200">     <img target="_blank" src="https://github.com/joshua/technology/blob/master/textblob.png" width="200">    <img target="_blank" src="https://github.com/joshua/technology/blob/master/wordcloud.png" width="300">

# Application :loudspeaker:
Ckeck out Twitter Sentiment Analysis on python **GUI** App :point_right: [click here](https://github.com/joshua/Twitter-Sentiment-Analysis-on-Python-GUI)

Ckeck out Twitter Sentiment Analysis on python **Jupyter Notebook** :point_right: [click here](https://github.com/nyadhi02)

Get a API key and put in the below code section
```python
def sentiment():
    userid = request.form.get('userid')
    hashtag = request.form.get('hashtag')

    if userid == "" and hashtag == "":
        error = "Please Enter any one value"
        return render_template('index.html', error=error)
    
    if not userid == "" and not hashtag == "":
        error = "Both entry not allowed"
        return render_template('index.html', error=error)
        
    if userid ==@"userName" and not hashtag ==#"hashtag"
        error = "follow instructions"
        return render_template('index.html', error=error)
    #=====================Insert Twitter API Here==========================
    consumerKey = ""
    consumerSecret = ""
    accessToken = ""
    accessTokenSecret = ""
    #=====================Insert Twitter API End===========================
    
    authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)
    authenticate.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(authenticate, wait_on_rate_limit = True)
   ```


## Bug / Feature Request :man_technologist:
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/joshua/Twitter-Sentiment-Analysis-on-Flask-App/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/joshua/Twitter-Sentiment-Analysis-on-Flask-App/issues/new). Please include sample queries and their corresponding results.

## Connect with me! 
Known on internet as **Nyadhi Joshua**

[![][I_LinkedIn]][LinkedIn]  [![][I_Github]][Github] [![][I_Twitter]][Twitter] [![][I_Telegram]][Telegram] [![][I_Instagram]][Instagram] 

## Email Me :e-mail:

[![][I_Email]][E-mail]

[LinkedIn]: https://www.linkedin.com/feed
[Github]: https://github.com/nyadhi02
[Twitter]: https://twitter.com/@alex80534146
[Telegram]: https://t.me/yogeshnile
[Instagram]:https://www.instagram.com/direct/new
[E-mail]: nyadhi.omondi@s.karu.ac.ke


[I_LinkedIn]: https://img.icons8.com/bubbles/100/000000/linkedin.png
[I_Github]: https://img.icons8.com/bubbles/100/000000/github.png
[I_Twitter]: https://img.icons8.com/bubbles/100/000000/twitter.png
[I_Telegram]: https://img.icons8.com/bubbles/100/000000/telegram-app.png
[I_Instagram]: https://img.icons8.com/bubbles/100/000000/instagram-new.png
[I_Email]: https://img.icons8.com/bubbles/100/000000/secured-letter.png

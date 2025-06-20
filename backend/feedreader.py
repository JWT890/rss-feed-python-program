import feedparser
import sys
import flask
from flask import Flask, render_template_string
from flask_cors import CORS

app = Flask(__name__)

RSS_FEEDS = {
    'Risky Business': "http://risky.biz/feeds/risky-business-news/",
    'ESPN': "https://www.espn.com/espn/rss/news",
    'HNRSS': "https://hnrss.org/frontpage",
    'SANS Daily': "https://isc.sans.edu/dailypodcast.xml",
    'SANS Education': "https://isc.sans.edu/rssfeed.xml",
    'Microsoft Blog': "https://msrc.microsoft.com/blog/categories/security-research-defense/feed",
    'Darknet Diaries': "https://www.darknet.org.uk/feed/",
    'Krebs on Security': "https://krebsonsecurity.com/feed/",
    'Security Magazine': "https://www.securitymagazine.com/rss/15",
    'CISA News': "https://www.cisa.gov/news.xml",
    'CISA Blog': "https://www.cisa.gov/blog.xml",
    'CISA Cyber Advisory': "https://www.cisa.gov/cybersecurity-advisories/all.xml",
    'NY Times': "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "NPR News": "https://feeds.npr.org/1001/rss.xml",
    'NPR Technology': "https://feeds.npr.org/1019/rss.xml",
    "Simplecast": "https://feeds.simplecast.com/54nAGcIl",
    "The Record": "https://therecord.media/tag/rss",
    "Ars Technica": "https://feeds.arstechnica.com/arstechnica/index",
    "TedTalks": "http://feeds.feedburner.com/TEDTalks_video",
    "r/technology": "https://www.reddit.com/r/technology/.rss",
    "BBC News": "http://feeds.bbci.co.uk/news/world/rss.xml",
    "New Heights": "https://rss.art19.com/new-heights",
    "Politico": "https://www.politico.com/rss/politicopicks.xml",
    "Politico": "https://rss.politico.com/morningcybersecurity.xml"
}
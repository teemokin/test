from flask import Flask, jsonify, render_template
import cloudscraper
# from bs4 import BeautifulSoup
# from requests_doh import DNSOverHTTPSSession
# session = DNSOverHTTPSSession(provider='cloudflare')


app = Flask(__name__)

@app.route("/")
def index():
    data = "Server is on"
    return respond_with(data)
    # return render_template('index.html', "PPONg")

@app.route("/wiki")
def tvwiki():


    url = "https://tvwiki.top"
    scraper = cloudscraper.create_scraper()
    headers = {
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Accept-Language': "ko,en;q=0.9,en-US;q=0.8,ru;q=0.7,vi;q=0.6,ja;q=0.5,zh-TW;q=0.4,zh-CN;q=0.3,zh;q=0.2",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    }

    r = scraper.get(url, headers=headers)
    status = r.status_code
    return respond_with(f"Wiki CloudFlare : {status}")

def respond_with(data):
    resp = jsonify(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = '*'
    return resp

if __name__ == '__main__':
    app.run()


from web_page_downloader import PageDownloader

converter = PageDownloader()

converter.save_html_from_url("https://www.google.com/", "google.html")

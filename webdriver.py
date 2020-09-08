from selenium import webdriver



class Driver:

    def __init__(self):
        self.instance = webdriver.Chrome("/usr/local/bin/chromedriver")

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")

    def get_url(self):
        return self.instance.current_url

    def implicitly_wait(self, seconds):
        self.instance.implicitly_wait(seconds)

    def maximize_window(self):
        return self.instance.maximize_window()



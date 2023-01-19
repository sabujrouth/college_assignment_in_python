print("Sabuj Routh")
class BrowserHistory:
    def __init__(self):
        self.history = []
        self.current = -1
        
    def navigate(self, url):
        self.history = self.history[:self.current+1]
        self.history.append(url)
        self.current += 1
        
    def forward(self):
        if self.current < len(self.history)-1:
            self.current += 1
            return self.history[self.current]
        return None
    
    def back(self):
        if self.current > 0:
            self.current -= 1
            return self.history[self.current]
        return None

# Example usage
browser = BrowserHistory()
browser.navigate("www.google.com")
browser.navigate("www.facebook.com")
print(browser.back()) # www.google.com
print(browser.forward()) # www.facebook.com

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    contents = []
    tag_open = False;
    vocab = '\n\r !"\'()+,-./0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz«»ÀÈÉßàèéìòùü'

    def handle_starttag(self, tag, attrs):
        self.tag_open = True

    def handle_endtag(self, tag):
        self.tag_open = False

    def handle_data(self, data):
        if self.tag_open: 
            if all(x in self.vocab for x in data):
                self.contents.append(data)

    def clean(self): # per liberare memoria ram
        self.contents = []



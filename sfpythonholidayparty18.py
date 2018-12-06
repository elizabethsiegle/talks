from bs4 import BeautifulSoup
import requests, string, random
from flask import Flask, request 
def scrape_and_clean(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    
    #get quotes from page
    div_quotes = soup.find_all("div", attrs={"class":"quoteText"})
    quotes = ''
    for q in div_quotes:
        author = ""
        # If no author, then skip
        try:
            author = q.find("a").get_text() + "\n"
        except:
            continue
        quote = ""
        # turn multiline quotes/poems into a single string
        for i in range(len(q.contents)):
            #find returns
            line = q.contents[i].encode("ascii", errors="ignore").decode("utf-8")
            print("line ", line)
            if (line[0] == "<"): # is tag, ignore characters that aren't part of quote 
                break
            else:
                quote += line

        quote = q.contents[0].encode("ascii", errors="ignore").decode("utf-8")
        quote = "\"" + quote.strip() + "\" "
        quotes += quote + '\n\n' + '-' + author + "#"
    quotes_to_return = filter(lambda x: x in string.printable, quotes) #clean
    return quotes_to_return


print(scrape_and_clean("http://www.goodreads.com/quotes/search?utf8=%E2%9C%93&q=harrypotter"))
print("hurr")
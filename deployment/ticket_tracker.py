import urllib.request
import html.parser
import json
import os
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

# Login
inputs = []
page = urllib.request.urlopen('http://msedev.byu.edu/bugs/scp/')
soup = BeautifulSoup(page, 'html.parser')
print(soup)
for node in soup.select('input'):
    inputs.append(''.join(node.find_all(text=True)))
print(inputs)

# Lists
ticket_numbers = []

# URLS
mylink_url = 'http://msedev.byu.edu/bugs/scp/tickets.php?advsid=5761e81620469a77100ee29be5558928'
webteam_url = 'http://msedev.byu.edu/bugs/scp/tickets.php?advsid=7a471ffd18ef8a3cffed365e1d34a444'

def get_ticket_info(url):
    # Just get the ticket table
    # ticket_table = SoupStrainer('form table')
    # Get page and run it through the parser
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    print(soup)
    # Ticket Numbers
    for node in soup.select('.emailTicket'):
        ticket_numbers.append(''.join(node.find_all(text=True)))
    print(ticket_numbers)


# mylink_tickets = get_ticket_info(mylink_url)
# webteam_tickets = get_ticket_info(webteam_url)

# 5761e81620469a77100ee29be5558928
# 5761e81620469a77100ee29be5558928

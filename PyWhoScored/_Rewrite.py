# -*- coding: utf-8 -*-
"""
Rewrite.py
"""

from PyWhoScored import Browser
import csv
import sys
reload(sys)
sys.setdefaultencoding('UTF8')

#--------------------
# REWRITE MODULE 
# Change URL DATA in csv files
#--------------------
# Rewrite tournament links
def _write_tournament_url(handler):
    Browser.open_browser(handler,"https://www.whoscored.com")
    
    _tList = []
    #Select list of tournaments
    html = handler.find_elements_by_css_selector("ul#popular-tournaments-list>li")
    for idx,ht in enumerate(html):
        _tList.append([idx,ht.text,ht.find_element_by_tag_name("a").get_attribute("href")])
    
    # Save into file
    with open('PyWhoScored/url-data/tournaments.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(_tList)

# Rewrite minor tournaments
def _write_alltournament_url(handler):
    fileloc = "PyWhoScored/url-data/tournaments.csv"
    rdata = []
    with open(fileloc, 'rb') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
         for row in spamreader:
             rdata.append(row)
    
    saveData = []
    for idx,trn in enumerate(rdata):
        print idx        
        Browser.open_browser(handler,trn[2])
        
        sNation = trn[0]
        #Find all tournament, including minor
        html = handler.find_elements_by_css_selector("select#tournaments>option")
        for ind,ht in enumerate(html):
            sData = ht.text
            sURL = "https://www.whoscored.com" + ht.get_attribute("value")
            saveData.append([sNation,ind,sData,sURL])
        
    # Save into file
    with open('PyWhoScored/url-data/alltournaments.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(saveData)

# Rewrite season links for each tournaments
def _write_seasons_url(handler):
    fileloc = "PyWhoScored/url-data/alltournaments.csv"
    rdata = []
    with open(fileloc, 'rb') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
         for row in spamreader:
             rdata.append(row)
    
    saveData = []
    for idx,trn in enumerate(rdata):
        Browser.open_browser(handler,trn[3])
        
        print idx
        sNation = trn[0]
        sTournament = trn[1]
        #Find all seasons' link
        html = handler.find_elements_by_css_selector("select#seasons>option")
        for ht in html:
            sData = ht.text
            sURL = "https://www.whoscored.com" + ht.get_attribute("value")
            saveData.append([sNation,sTournament,sData,sURL])
    
    # Save into file
    with open('PyWhoScored/url-data/allseasons.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(saveData)
    
#----------------
#----------------
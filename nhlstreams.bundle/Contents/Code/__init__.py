import sys
import os
import utils
import ConfigParser
import urllib, json
import socket
from datetime import datetime
from game import Game
from urlparse import parse_qsl

TITLE    = 'NHL Streams'
PREFIX   = '/video/nhlstreams'

ART      = 'art-default.jpg'
ICON     = 'icon-default.png'

oc = ObjectContainer()

def Start():
  ObjectContainer.title1 = TITLE
  ObjectContainer.art = R(ART)

  DirectoryObject.thumb = R(ICON)
  DirectoryObject.art = R(ART)
  EpisodeObject.thumb = R(ICON)
  EpisodeObject.art = R(ART)
  VideoClipObject.thumb = R(ICON)
  VideoClipObject.art = R(ART)

iniFilePath = os.path.join('Contents','Resources', 'nhlstreams.ini')

config = ConfigParser.ConfigParser()
config.read(iniFilePath)

hostname = socket.gethostbyname("mf.svc.nhl.com")
server = config.get("NHLstreams","Host")

def games(date): return Game.fromDate(config,date)

def listgames(date):
  items = []
  dategames = games(date)
  for g in dategames: 
    label = "%s vs. %s [%s]" % (g.awayFull,g.homeFull,g.timeRemaining if g.timeRemaining != "N/A" else utils.asCurrentTz(date,g.time))    
    url = '{0}?action=feeds&game={1}&date={2}'.format(addonUrl,g.id,date)
    oc.add(
      VideoClipObject(title=label, url=url)
      )

listgames(utils.today().strftime("%Y-%m-%d"))
import os
import json
import urllib2
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

# Set current directory

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load graphic

img = Image.open("./logo.png")
draw = ImageDraw.Draw(img)

# get api data

try:
  f = urllib2.urlopen('http://192.168.1.99/admin/api.php')
  json_string = f.read()
  parsed_json = json.loads(json_string)
  adsblocked = parsed_json['ads_blocked_today']
  ratioblocked = parsed_json['ads_percentage_today']
  f.close()
except:
  queries = '?'
  adsblocked = '?'
  ratioblocked = 0.0

font = ImageFont.truetype(FredokaOne, 16)

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

draw.text((10,15), str(adsblocked) + " AD'S", inky_display.RED, font)
draw.text((10,35), str("%.1f" % round(ratioblocked,2)) + " AD%", inky_display.RED, font)

inky_display.set_image(img)

inky_display.show()

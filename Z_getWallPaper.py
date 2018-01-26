import requests
import time
import os  

os.chdir( "F:\\image\\wallpaper")  

url = r"http://area.sinaapp.com/bingImg/"
page = requests.get(url)
image_name = "BingWallpaper-"+time.strftime("%Y-%m-%d")+'.jpg'
with open(image_name,'wb') as f:
	f.write(page.content)


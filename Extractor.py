from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options as FirefoxOptions


import re
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import time
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import yt_dlp
from bs4 import BeautifulSoup

class Extractor(object):

    def __init__(self, url) -> None:
        self.video_url = url
        self.video_info = {}
        # load firefox profile with UBlock extension installed
        # source : https://www.lambdatest.com/blog/adding-firefox-extensions-with-selenium-in-python/
        self.configure_webdriver()
        
    def configure_webdriver(self):
        self.options = FirefoxOptions()
        #self.options.add_argument("--headless")
        self.options.add_argument("-profile")
        self.options.add_argument('./firefox_profile_ublock/')
        self.options.add_argument('-private')
        #options.add_argument("profile")
        #self.profile = webdriver.FirefoxProfile("firefox_profile_ublock")
        self.driver = webdriver.Firefox(options=self.options)
        
        self.driver.get(self.video_url)    

    def refuse_condition(self):
        """Sometimes a dialog window appears to 
        """
        dialog = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "dialog")))

        div_bottom_dialog = dialog.find_element(By.CSS_SELECTOR, ".eom-buttons")
        btns = div_bottom_dialog.find_elements(By.TAG_NAME, "ytd-button-renderer")

        btns[1].click()


    def get_svg(self):
        """graph"""
        #self.refuse_condition()

        #hoverable = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ytp-progress-bar-container")))
        #ActionChains(self.driver, 1000)\
        #    .move_to_element(hoverable)\
        #    .perform()
        
        
        heatmap_chapter = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "ytp-heat-map-chapter")))

        svg_html = heatmap_chapter.get_attribute('innerHTML')

        self.driver.close()
        
        return svg_html
    
    def download_video(self, resolution=360):
        print("launch video donwloading")
       
        ydl_opts = {
            'format': f"b[height={resolution}][ext=mp4]",
            'quiet': True,
            "nopart": True,
            'outtmpl': "./download/youtube_video.%(ext)s"
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                self.video_info = ydl.extract_info(self.video_url)
        except yt_dlp.utils.DownloadError:
            print('interrupt the download')
            return False
        return True
    
    def extract_points_from_svg(self, svg):
        print("launch extraction points svg")

        soup = BeautifulSoup(svg, "lxml")
        path = soup.find("path")
        d = path.get("d")
        print(d)
        coordinates = d.replace("M ", "").replace("C ", "").split(" ")
        points = []
        for c in coordinates[1:]: #ignore first
            tab = c.split(",")
            x_coordinate = float(tab[0])
            y_coordinate = float(tab[1]) 
            points.append((x_coordinate, y_coordinate))         

        x_coords, y_coords = zip(*points)
   
        y_coords = [90.0-y for y in y_coords] # inverse graph
        y_coords = [y if y >= 0.0 else 0.0 for y in y_coords] # correct graph
        print(y_coords)
        #y_coords = [(y - y_min) / (y_max - y_min) for y in y_coords] # normalize between 0 and 1 : Y
        #print(y_coords)
        #print(min(y_coords), max(y_coords))
        
        new_points = list(zip(x_coords, y_coords))

        print("Extraction de points:", len(new_points))

        return new_points

    def plot_svg(self, points, threshold=80.0):
        # Représentation graphique de la courbe
        x_coords, y_coords = zip(*points)
        plt.plot(x_coords, y_coords, marker="+")
        plt.axhline(y=threshold, color='r', linestyle='--')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Courbe SVG')

    def plot_peaks(self, peaks):
        for peak in peaks:
            plt.scatter(peak[0], peak[1], marker="o")
        
    def plot_save_show(self):
        plt.savefig("./peaks/plot_svg_peaks.jpg")    
        plt.show()
        

    def find_peaks(self, points, threshold=80.0):
        # Trouver les pics en comparant les hauteurs des points voisins
        peaks = []
        for i in range(1, len(points)-1):
            prev_y = points[i-1][1]
            curr_y = points[i][1]
            next_y = points[i+1][1]
            if curr_y > prev_y and curr_y > next_y and curr_y >= threshold:
                peaks.append(points[i])
        return peaks
    
    def peaks_to_time(self, x):
        # 1000 -> time_duration (seconds)
        # x    ->    ?
        # (x * time_duration) / 1000 = time_peak

        return (x * self.video_info["duration"]) / 1000
    
    def extract_part(self, start_time, end_time, name):
        ffmpeg_extract_subclip("./download/youtube_video.mp4", start_time, end_time, targetname="peaks/"+name+".mp4")
from Extractor import Extractor

if __name__ == "__main__":
    yt_video_url = "https://www.youtube.com/watch?v=DayTsZvKmd8"

    duration_peak = 10 # in seconds / odd numbers

    extractor = Extractor(yt_video_url)

    svg_code = extractor.get_svg()

    points = extractor.extract_points_from_svg(svg_code)
    
    peaks = extractor.find_peaks(points)

    extractor.plot_svg(points)
    extractor.plot_peaks(peaks)
    extractor.plot_save_show()
  
    video_downloaded = extractor.download_video()

    if video_downloaded:
        for i, (x,y) in enumerate(peaks):
            x_in_sec = extractor.peaks_to_time(x)
            m, s = divmod(x_in_sec, 60)

            extractor.extract_part(x_in_sec - (duration_peak/2), x_in_sec + (duration_peak/2), str(i)+"_peak_at["+str(int(m))+"_"+str(int(s))+"]")
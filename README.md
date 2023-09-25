# ytb-most-replayed

On May 18, 2022, YouTube began rolling out a new feature that highlights the "most replayed" parts of a video. YouTube writes that the feature allows users to see a graphic that highlights the "most frequently replayed parts of the video."

<p align="center">
  <img src="https://github.com/Dorian25/ytb-most-replayed/assets/32178615/6f8e14fa-95e5-4b58-a3a6-df7fa96af62c">
</p>


## Features

- **Conversion SVG to graph** :framed_picture: :arrow_right: :chart_with_upwards_trend:
> Simply extract the heatmap of the video progress bar SVG Path into numerical points coordinates (x,y)
- :mountain: **Detection peaks**
> 
- :gear: **Parameters**
  - **y-threshold** (default: 80)
  - **video resolution** (default: 360p)
  - **clip duration** (default: 10sec) 

## Example

1. Choose a YouTube video (Dating: >5-7 days / views: >90k views)
> Date de publication : Jul 16, 2023
> 
> Nombre de vues : 748,709 views  
> 
> URL : [https://www.youtube.com/watch?v=1WEAJ-DFkHE](https://www.youtube.com/watch?v=DayTsZvKmd8)
<p align="center">
  <img src="https://img.youtube.com/vi/DayTsZvKmd8/maxresdefault.jpg">
</p>

2. The program will move the mouse over the progress bar of the video `ytp-progress-bar-container` to display the heatmap

> SVG Image
<p align="center">
<img src="https://github.com/Dorian25/ytb-most-replayed/assets/32178615/d599ca0e-771b-47b4-b0ba-fed2edc21aba">
</p>

> SVG Code HTML
```html
<svg class="ytp-heat-map-svg" height="100%" preserveAspectRatio="none" version="1.1" viewBox="0 0 1000 100" width="100%" style="height: 40px;"><defs><clipPath id="3"><path class="ytp-heat-map-path" d="M 0.0,100.0 C 1.0,93.3 2.0,72.7 5.0,66.7 C 8.0,60.8 11.0,65.6 15.0,70.3 C 19.0,74.9 21.0,87.3 25.0,90.0 C 29.0,92.7 31.0,83.6 35.0,83.6 C 39.0,83.6 41.0,90.2 45.0,90.0 C 49.0,89.8 51.0,85.2 55.0,82.5 C 59.0,79.9 61.0,75.3 65.0,76.8 C 69.0,78.3 71.0,87.4 75.0,90.0 C 79.0,92.6 81.0,90.0 85.0,90.0 C 89.0,90.0 91.0,90.0 95.0,90.0 C 99.0,90.0 101.0,94.5 105.0,90.0 C 109.0,85.5 111.0,69.1 115.0,67.6 C 119.0,66.1 121.0,78.0 125.0,82.5 C 129.0,86.9 131.0,88.5 135.0,90.0 C 139.0,91.5 141.0,91.4 145.0,90.0 C 149.0,88.6 151.0,83.1 155.0,83.1 C 159.0,83.1 161.0,88.6 165.0,90.0 C 169.0,91.4 171.0,90.0 175.0,90.0 C 179.0,90.0 181.0,90.0 185.0,90.0 C 189.0,90.0 191.0,90.0 195.0,90.0 C 199.0,90.0 201.0,91.5 205.0,90.0 C 209.0,88.5 211.0,82.6 215.0,82.6 C 219.0,82.6 221.0,88.5 225.0,90.0 C 229.0,91.5 231.0,90.6 235.0,90.0 C 239.0,89.4 241.0,90.5 245.0,87.2 C 249.0,83.9 251.0,79.0 255.0,73.4 C 259.0,67.9 261.0,56.3 265.0,59.6 C 269.0,62.9 271.0,84.4 275.0,90.0 C 279.0,95.6 281.0,87.6 285.0,87.5 C 289.0,87.4 291.0,95.5 295.0,89.3 C 299.0,83.2 301.0,63.4 305.0,56.7 C 309.0,50.0 311.0,49.2 315.0,55.9 C 319.0,62.5 321.0,86.9 325.0,90.0 C 329.0,93.1 331.0,74.7 335.0,71.2 C 339.0,67.6 341.0,69.5 345.0,72.1 C 349.0,74.8 351.0,80.9 355.0,84.5 C 359.0,88.0 361.0,88.9 365.0,89.8 C 369.0,90.7 371.0,91.2 375.0,89.1 C 379.0,87.0 381.0,82.2 385.0,79.4 C 389.0,76.6 391.0,74.7 395.0,75.1 C 399.0,75.5 401.0,88.6 405.0,81.4 C 409.0,74.1 411.0,55.0 415.0,38.8 C 419.0,22.5 421.0,-5.0 425.0,0.0 C 429.0,5.0 431.0,46.0 435.0,64.0 C 439.0,81.9 441.0,84.6 445.0,89.8 C 449.0,95.0 451.0,90.0 455.0,90.0 C 459.0,90.0 461.0,90.0 465.0,90.0 C 469.0,90.0 471.0,90.0 475.0,90.0 C 479.0,90.0 481.0,93.3 485.0,90.0 C 489.0,86.7 491.0,75.6 495.0,73.6 C 499.0,71.5 501.0,76.3 505.0,79.6 C 509.0,82.9 511.0,88.3 515.0,90.0 C 519.0,91.7 521.0,88.0 525.0,88.0 C 529.0,88.0 531.0,89.6 535.0,90.0 C 539.0,90.4 541.0,90.0 545.0,90.0 C 549.0,90.0 551.0,90.0 555.0,90.0 C 559.0,90.0 561.0,90.0 565.0,90.0 C 569.0,90.0 571.0,90.2 575.0,90.0 C 579.0,89.8 581.0,89.9 585.0,89.1 C 589.0,88.4 591.0,86.2 595.0,86.4 C 599.0,86.5 601.0,92.5 605.0,90.0 C 609.0,87.5 611.0,74.0 615.0,74.0 C 619.0,74.0 621.0,88.0 625.0,90.0 C 629.0,92.0 631.0,83.8 635.0,83.8 C 639.0,83.8 641.0,88.8 645.0,90.0 C 649.0,91.2 651.0,90.0 655.0,90.0 C 659.0,90.0 661.0,90.0 665.0,90.0 C 669.0,90.0 671.0,90.0 675.0,90.0 C 679.0,90.0 681.0,90.0 685.0,90.0 C 689.0,90.0 691.0,91.2 695.0,90.0 C 699.0,88.8 701.0,84.0 705.0,84.0 C 709.0,84.0 711.0,90.3 715.0,90.0 C 719.0,89.7 721.0,82.6 725.0,82.4 C 729.0,82.1 731.0,87.2 735.0,88.7 C 739.0,90.3 741.0,90.4 745.0,90.0 C 749.0,89.6 751.0,90.0 755.0,86.8 C 759.0,83.6 761.0,74.1 765.0,74.2 C 769.0,74.2 771.0,84.5 775.0,87.0 C 779.0,89.4 781.0,91.5 785.0,86.5 C 789.0,81.6 791.0,64.2 795.0,62.1 C 799.0,60.0 801.0,74.1 805.0,76.2 C 809.0,78.3 811.0,72.5 815.0,72.5 C 819.0,72.6 821.0,76.7 825.0,76.5 C 829.0,76.3 831.0,79.3 835.0,71.5 C 839.0,63.7 841.0,41.0 845.0,37.5 C 849.0,34.1 851.0,48.4 855.0,54.5 C 859.0,60.6 861.0,63.7 865.0,68.2 C 869.0,72.6 871.0,86.1 875.0,76.7 C 879.0,67.2 881.0,33.9 885.0,21.1 C 889.0,8.2 891.0,6.4 895.0,12.5 C 899.0,18.6 901.0,44.3 905.0,51.6 C 909.0,58.9 911.0,46.6 915.0,48.9 C 919.0,51.3 921.0,55.2 925.0,63.3 C 929.0,71.4 931.0,84.4 935.0,89.3 C 939.0,94.3 941.0,88.8 945.0,87.8 C 949.0,86.8 951.0,86.9 955.0,84.4 C 959.0,81.8 961.0,75.9 965.0,75.2 C 969.0,74.4 971.0,81.1 975.0,80.6 C 979.0,80.0 981.0,87.8 985.0,72.4 C 989.0,56.9 992.0,17.2 995.0,3.4 C 998.0,-10.4 999.0,-16.0 1000.0,3.4 C 1001.0,22.7 1000.0,80.7 1000.0,100.0" fill="white"></path></clipPath></defs><rect class="ytp-heat-map-graph" clip-path="url(#3)" fill="white" fill-opacity="0.2" height="100%" width="100%" x="0" y="0"></rect><rect class="ytp-heat-map-hover" clip-path="url(#3)" fill="white" height="100%" x="0" y="0"></rect><rect class="ytp-heat-map-play" clip-path="url(#3)" height="100%" x="0" y="0"></rect></svg>
```

3. From the SVG html code, the program extracts a list of coordinates (x,y) of points (about 1000 points) from the `d` attribute of the `<path>` tag
```python
>> [(1.0,87.5), (2.0,41.9), (5.0,37.5),... , (1001.0,87.4), (1000.0,96.8), (1000.0,100.0)]
```
<p align="center">
<img src="https://github.com/Dorian25/ytb-most-replayed/assets/32178615/daae76b6-b93a-40ef-9a2b-00bd3e5fe5dc">
</p>

4. The program reverses the scale of the graph by applying a simple subtraction to the y-intercept of the points
```python
>> [(1.0,2.5), (2.0,48.1), (5.0,52.4),... , (1001.0,2.89999999943), (1000.0,0.0), (1000.0,0.0)]
```
<p align="center">
<img src="https://github.com/Dorian25/ytb-most-replayed/assets/32178615/ec2019b2-19c3-4513-86af-a263f5c8d13d">
</p>

5. Then extract the coordinates of peaks with an ordinate > threshold (80 by default)
![plot_svg_peaks](https://github.com/Dorian25/ytb-most-replayed/assets/32178615/300cfa23-9e94-4c85-a6f0-7e61a4f51ebb)

6. To extract the "most replayed" moments, simply convert the coordinates into a time scale based on the total duration of the video. Then use the [moviepy](https://github.com/Zulko/moviepy) library to slice the entire video into portions of the desired length (by default 10 seconds).

Peak 1 at 13:15

https://github.com/Dorian25/ytb-most-replayed/assets/32178615/521d12b7-4f61-4914-8e3d-14f42710b691

Peak 2 at 28:04

https://github.com/Dorian25/ytb-most-replayed/assets/32178615/6b8a1d7d-aabc-4187-ba65-9ad9e2eaedea

Peak 3 at 31:14

https://github.com/Dorian25/ytb-most-replayed/assets/32178615/b0f8e7b8-a5e2-4b69-951b-66302107fd32









## How to run

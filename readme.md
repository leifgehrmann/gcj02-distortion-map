# GCJ-02 Distortion Map

I saw this [YouTube video] a while ago about China's obfuscated geodetic datum
called [GCJ-02]. But I was still curious what the distortion actually
looks like overall. I could only find [one result on the web], but was not
satisfied.

After discovering someone has made a nice python library for this called
[eviltransform], I quickly put together this script that will render the
displacement across China. The output of `distortion-map.py` is displayed
below.

![Map of China showing the GCJ-02 geodetic datum displacement](output.svg)

The direction of the arrows indicates the direction that the coordinate moves
when going from the [WGS-84] datum to the [GCJ-02] datum.

## Accuracy

Then I wondered how accurate this eviltransform library really is...

So I sampled some coordinates from Google Maps, which has map data using the
GCJ-02 datum, then located the "true" WGS-84 coordinates in
OpenStreetMap. These coordinates are in `empirical-data.csv`.

The script `empirical-data-vs-eviltransform.py` calculates the distance between
my sampled coordinates and eviltransform's coordinates. The results of
that script is displayed below.

```
leifgehrmann$ python empirical-data-vs-eviltransform.py 
Hefei:         2.1384628229593066 metres
Beijing:       1.7838294527020613 metres
Chongqing:     5.152717270471657 metres
Fuzhou:        0.9073348188453385 metres
Guangzhou:     2.937543074685877 metres
Lanzhou:       4.159880618652668 metres
Nanning:       8.015424820851045 metres
Guiyang:       2.667177044530215 metres
Zhengzhou:     4.802243020827364 metres
Wuhan:         6.02647477043642 metres
Shijiazhuang:  7.45528579111226 metres
Haikou:        4.066640772025619 metres
Harbin:        3.3008716093576784 metres
Changsha:      3.4208004718862783 metres
Changchun:     4.800336046545485 metres
Nanjing:       7.8535249322043885 metres
Nanchang:      4.488149443711448 metres
Shenyang:      4.740405971499917 metres
Hohhot:        2.5164124023982546 metres
Yinchuan:      2.920999302563985 metres
Xining:        6.154309560799352 metres
Chengdu:       7.605916911879766 metres
Jinan:         3.588598463196563 metres
Shanghai:      3.3167445838853786 metres
Xi'an:         1.973707095998891 metres
Taiyuan:       7.022766145577794 metres
Tianjin:       4.585507830027573 metres
Ürümqi:        3.573897436004349 metres
Lhasa:         7.8217763706152255 metres
Kunming:       3.7487647847649 metres
Hangzhou:      7.45360368958556 metres
Ngari:         11.539209405253525 metres
Kashgar:       6.566364759361955 metres
Altay:         2.759570437909781 metres
```

Since OpenStreetMap data and satellite imagery
usually has an error of ~15m, this means eviltransform is pretty reliable!

## Installation

```
# To install geos on the mac...
brew install geos

# Create a virtual environment
python3 -m venv venv

# Active the environment
source venv/bin/activate

# Install the dependencies
pip install -r requirements.txt

# Install the non-pip-able dependencies (This takes a while)
pip install https://github.com/matplotlib/basemap/archive/master.zip
```

## To run

```
python distortion-map.py

python empirical-data-vs-eviltransform.py
```

[YouTube video]: https://www.youtube.com/watch?v=L9Di-UVC-_4
[one result on the web]: https://www.gearthblog.com/blog/archives/2015/08/look-chinese-map-offsets.html
[eviltransform]: https://github.com/googollee/eviltransform
[WGS-84]: https://en.wikipedia.org/wiki/WGS-84
[GCJ-02]: https://en.wikipedia.org/wiki/Restrictions_on_geographic_data_in_China#GCJ-02

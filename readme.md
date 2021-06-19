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
City         My Sample         EvilTransform        Difference
Hefei        564.64 metres     566.31 metres         2.14 metres
Beijing      556.01 metres     555.90 metres         1.78 metres
Chongqing    475.64 metres     479.27 metres         5.15 metres
Fuzhou       591.79 metres     590.93 metres         0.91 metres
Guangzhou    623.50 metres     621.16 metres         2.94 metres
Lanzhou      220.37 metres     219.71 metres         4.16 metres
Nanning      503.55 metres     511.23 metres         8.02 metres
Guiyang      537.07 metres     539.67 metres         2.67 metres
Zhengzhou    581.16 metres     577.00 metres         4.80 metres
Wuhan        591.41 metres     586.37 metres         6.03 metres
Shijiazhuang 539.78 metres     532.51 metres         7.46 metres
Haikou       505.55 metres     509.61 metres         4.07 metres
Harbin       505.84 metres     509.06 metres         3.30 metres
Changsha     658.00 metres     659.92 metres         3.42 metres
Changchun    591.16 metres     586.82 metres         4.80 metres
Nanjing      534.96 metres     541.89 metres         7.85 metres
Nanchang     602.44 metres     606.67 metres         4.49 metres
Shenyang     576.46 metres     577.89 metres         4.74 metres
Hohhot       591.86 metres     589.36 metres         2.52 metres
Yinchuan     390.29 metres     387.54 metres         2.92 metres
Xining       180.53 metres     174.94 metres         6.15 metres
Chengdu      354.21 metres     359.84 metres         7.61 metres
Jinan        531.84 metres     528.25 metres         3.59 metres
Shanghai     473.37 metres     472.91 metres         3.32 metres
Xi'an        465.20 metres     463.65 metres         1.97 metres
Taiyuan      551.91 metres     555.13 metres         7.02 metres
Tianjin      562.76 metres     562.08 metres         4.59 metres
Ürümqi       264.13 metres     264.43 metres         3.57 metres
Lhasa        337.64 metres     335.95 metres         7.82 metres
Kunming      357.32 metres     359.96 metres         3.75 metres
Hangzhou     525.59 metres     522.34 metres         7.45 metres
Ngari        347.17 metres     345.03 metres        11.54 metres
Kashgar      267.57 metres     261.01 metres         6.57 metres
Altay        294.14 metres     292.83 metres         2.76 metres
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

# GCJ-02 Distortion Map

I saw this video a while ago: https://www.youtube.com/watch?v=L9Di-UVC-_4  

But I was curious what the distortion actually looks like as a whole. Google
was not giving me any good results.

After discovering someone has made a nice python library for this called
[eviltransform], I quickly put together this script that will render the
displacement across China.

The output of `distortion-map.py` is displayed below.

![Map of china showing the displacement caused by the GCJ-02 geodetic datum](output.svg)

The direction of the arrows indicates the direction that the coordinate moves
when going from the [WGS-84] datum to the [GCJ-02] datum. 

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
```

[eviltransform]: https://github.com/googollee/eviltransform
[WGS-84]: https://en.wikipedia.org/wiki/WGS-84
[GCJ-02]: https://en.wikipedia.org/wiki/Restrictions_on_geographic_data_in_China#GCJ-02

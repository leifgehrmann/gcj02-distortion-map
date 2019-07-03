from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import eviltransform
import math


basemap = Basemap(
    llcrnrlon=76,
    llcrnrlat=15,
    urcrnrlon=145,
    urcrnrlat=50,
    resolution='i',
    projection='tmerc',
    lon_0=102,
    lat_0=36)

x = []
y = []
dx = []
dy = []
s = []

fig = plt.subplots(nrows=1, figsize=(7.5, 5.25))

for utm_x in range(0, 8000000, 100000):
    for utm_y in range(0, 5000000, 100000):

        wgs_longitude, wgs_latitude = basemap(utm_x, utm_y, inverse=True)

        wgs_x, wgs_y = basemap(wgs_longitude, wgs_latitude)
        gcj_latitude, gcj_longitude = eviltransform.wgs2gcj(
            wgs_latitude,
            wgs_longitude
        )
        gxj_x, gxj_y = basemap(gcj_longitude, gcj_latitude)

        x.append(wgs_x)
        y.append(wgs_y)
        dx.append(wgs_x-gxj_x)
        dy.append(wgs_y-gxj_y)
        s.append(math.hypot(wgs_x-gxj_x, wgs_y-gxj_y))

basemap.drawmapboundary(fill_color='#000000')
basemap.fillcontinents(color='#444444', lake_color='None')
basemap.drawcountries(linewidth=1, zorder=11)

quiver_ref = basemap.quiver(
    x,
    y,
    dx,
    dy,
    s,
    zorder=10,
    scale=4500,
    scale_units='inches',
    headwidth=3,
    headlength=3,
    headaxislength=3,
    cmap='jet',
    pivot='mid'
)
color_bar = plt.colorbar(quiver_ref, pad=0.01)
color_bar.set_label('Metres', labelpad=5)

plt.title('GCJ-02 Map Displacement', fontsize=12)

plt.tight_layout()
plt.savefig('output.svg', pad_inches=0, dpi=144)

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

""" Read files """
overall_4_pop = pd.read_excel('/Users/Light/PythonData/overall_opioid_trend.xlsx', sheet_name=0)
city_shp = gpd.read_file('/Users/Light/PythonData/GeoCityData/COUNTY_MOI_1080617.shp')
# take a look the map we are going to use
city_shp.plot()

""" Merge """
overall_4_pop_geo = pd.merge(left = city_shp, right = overall_4_Px, on='COUNTYID')

""" Plot """
# define discrete cmap
def discrete_cmap(N, base_cmap=None):
    base = plt.cm.get_cmap(base_cmap)
    color_list = base(np.linspace(0, 1, N))
    cmap_name = base.name + str(N)
    return base.from_list(cmap_name, color_list, N)

# define upper bound & low bound
vmin = 0
vmax = 100

# divide the canvas into 2
fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1, figsize=(20, 16))

# map1
# latitude and longitude of Taiwan
ax1.set_ylim([21.5, 26.5])
ax1.set_xlim([117.5, 123.5])
ax1 = overall_4_pop_geo.plot(ax=ax1, linewidth=0.8, edgecolor='0',column=2012,cmap = discrete_cmap(5, 'OrRd'),vmin=0, vmax=vmax)
# linewidth : thickness of the silhouette 
# column : the data which you want to put into your map
# discrete_cmap(number of levels, color of cmap)
ax1.set_title('4 common opioids prescription per 1000 Medical Care-seeking population in Taiwan, 2012',fontweight=12,fontsize=14)
ax1.set_axis_off()
scatter1 = ax1.collections[0]
# this is about the colorbar on the right side.
plt.colorbar(scatter1,ax = ax1,ticks=[0,20,40,60,80,100],label='Number of Medical Care-seeking population per 1000',extend='max')

# this is about the labels on each city
overall_4_pop_geo['coords'] = overall_4_pop_geo['geometry'].apply(lambda x: x.representative_point().coords[:])
overall_4_pop_geo['coords'] = [coords[0] for coords in overall_4_pop_geo['coords']]
for idx, row in overall_4_pop_geo.iterrows():
    ax1.annotate(s=row[2012], xy=row['coords'],horizontalalignment='center',fontweight=12,fontsize=12)


# map2
ax2.set_ylim([21.5, 26.5])
ax2.set_xlim([117.5, 123.5])
ax2 = overall_4_pop_geo.plot(ax=ax2, linewidth=0.8, edgecolor='0',column=2016,cmap = discrete_cmap(5, 'OrRd'),vmin=0, vmax=vmax)
ax2.set_title('4 common opioids prescription per 1000 Medical Care-seeking population in Taiwan, 2016',fontweight=12,fontsize=14)
ax2.set_axis_off()
scatter2 = ax2.collections[0]
plt.colorbar(scatter2,ax = ax2,ticks=[0,20,40,60,80,100],label='Number of Medical Care-seeking population per 1000',extend='max')
overall_4_pop_geo['coords'] = overall_4_pop_geo['geometry'].apply(lambda x: x.representative_point().coords[:])
overall_4_pop_geo['coords'] = [coords[0] for coords in overall_4_pop_geo['coords']]
for idx, row in overall_4_pop_geo.iterrows():
    ax2.annotate(s=row[2016], xy=row['coords'],horizontalalignment='center',fontweight=12,fontsize=12)

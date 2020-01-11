

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

""" Read """

Codeine = pd.read_excel('/Users/Light/PythonData/opioid_trend.xlsx', sheet_name=0)
Morphine = pd.read_excel('/Users/Light/PythonData/opioid_trend.xlsx', sheet_name=1)
Fentanyl = pd.read_excel('/Users/Light/PythonData/opioid_trend.xlsx', sheet_name=2)
Pethidine = pd.read_excel('/Users/Light/PythonData/opioid_trend.xlsx', sheet_name=3)

overall_4_Px = pd.read_excel('/Users/Light/PythonData/overall_opioid_trend.xlsx', sheet_name=0)
overall_4_MME = pd.read_excel('/Users/Light/PythonData/overall_opioid_trend.xlsx', sheet_name=1)
overall_7_Px = pd.read_excel('/Users/Light/PythonData/overall_opioid_trend.xlsx', sheet_name=2)
overall_7_MME = pd.read_excel('/Users/Light/PythonData/overall_opioid_trend.xlsx', sheet_name=3)
overall_4_pop = pd.read_excel('/Users/Light/PythonData/overall_opioid_trend.xlsx', sheet_name=4)
overall_7_pop = pd.read_excel('/Users/Light/PythonData/overall_opioid_trend.xlsx', sheet_name=5)



pethidine = pd.read_excel('/Users/Light/Downloads/geo/pethidine.xlsx')
pethidine.head()

morphine = pd.read_excel('/Users/shawnslab/Desktop/geo/morphine.xlsx')
morphine.head()

fentanyl = pd.read_excel('/Users/shawnslab/Desktop/geo/fentanyl.xlsx')
fentanyl.head()

codeine = pd.read_excel('/Users/shawnslab/Desktop/geo/codeine.xlsx')
codeine.head()

ERLA = pd.read_excel('/Users/shawnslab/Desktop/geo/ERLA.xlsx')
ERLA.head()

MME = pd.read_excel('/Users/shawnslab/Desktop/geo/MME.xlsx')
MME.head()

level = pd.read_excel('/Users/shawnslab/Desktop/geo/level.xlsx')
level.head()

drugday = pd.read_excel('/Users/shawnslab/Desktop/geo/drugday.xlsx')
drugday.head()

short = pd.read_excel('/Users/shawnslab/Desktop/geo/short.xlsx')
short.head()

long = pd.read_excel('/Users/shawnslab/Desktop/geo/long.xlsx')
long.head()

city_shp = gpd.read_file('/Users/Light/PythonData/GeoCityData/COUNTY_MOI_1080617.shp')
city_shp.plot()

Town_shp = gpd.read_file('/Users/Light/PythonData/GeoTownData/TOWN_MOI_1071226.shp')
Town_shp.plot()

town_mediclass = pd.read_excel('/Users/Light/PythonData/town_mediclass.xlsx')
long.head()

""" Merge """

Codeine_geo = pd.merge(left = city_shp, right = Codeine, on='COUNTYID')
Morphine_geo = pd.merge(left = city_shp, right = Morphine, on='COUNTYID')
Fentanyl_geo = pd.merge(left = city_shp, right = Fentanyl, on='COUNTYID')
Pethidine_geo = pd.merge(left = city_shp, right = Pethidine, on='COUNTYID')

overall_4_Px_geo = pd.merge(left = city_shp, right = overall_4_Px, on='COUNTYID')
overall_4_MME_geo = pd.merge(left = city_shp, right = overall_4_MME, on='COUNTYID')
overall_7_Px_geo = pd.merge(left = city_shp, right = overall_7_Px, on='COUNTYID')
overall_7_MME_geo = pd.merge(left = city_shp, right = overall_7_MME, on='COUNTYID')
overall_4_pop_geo = pd.merge(left = city_shp, right = overall_7_pop, on='COUNTYID')
overall_7_pop_geo = pd.merge(left = city_shp, right = overall_7_pop, on='COUNTYID')



mediclass = pd.merge(left = Town_shp, right = town_mediclass, on='TOWNID')

short = pd.merge(left = city_shp, right = short, on='COUNTYID')
long = pd.merge(left = city_shp, right = long, on='COUNTYID')
drugday = pd.merge(left = city_shp, right = drugday, on='COUNTYID')
ERLA = pd.merge(left = city_shp, right = ERLA, on='COUNTYID')
MME = pd.merge(left = city_shp, right = MME, on='COUNTYID')
level = pd.merge(left = city_shp, right = level, on='COUNTYID')





np.percentile(overall_4_pop[2012], [20, 40, 60, 80, 100])
np.percentile(overall_7_pop[2012], [20, 40, 60, 80, 100])



""" Plot """

def discrete_cmap(N, base_cmap=None):

    base = plt.cm.get_cmap(base_cmap)
    color_list = base(np.linspace(0, 1, N))
    cmap_name = base.name + str(N)
    return base.from_list(cmap_name, color_list, N)

vmin = 0
vmax = 160
norm = plt.Normalize(vmin=0, vmax=vmax)
fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1, figsize=(20, 16))
ax1.set_ylim([21.5, 26.5])
ax1.set_xlim([117.5, 123.5])
ax1 = overall_7_MME_geo.plot(ax=ax1, linewidth=0.8, edgecolor='0',column=2012,cmap = discrete_cmap(5, 'OrRd'),vmin=0, vmax=vmax)
ax1.set_title('7 overall opioids Used in Taiwan, 2012',fontweight=12,fontsize=14)
ax1.set_axis_off()
scatter1 = ax1.collections[0]
plt.colorbar(scatter1,ax = ax1,ticks=[0,32,64,96,128,160],label='Morphine Milligram Equivalents per Day',extend='max')
ax2.set_ylim([21.5, 26.5])
ax2.set_xlim([117.5, 123.5])
ax2 = overall_7_MME_geo.plot(ax=ax2, linewidth=0.8, edgecolor='0',column=2016,cmap = discrete_cmap(5, 'OrRd'),vmin=0, vmax=vmax)
ax2.set_title('7 overall opioids Used in Taiwan, 2016',fontweight=12,fontsize=14)
ax2.set_axis_off()
scatter2 = ax2.collections[0]
plt.colorbar(scatter2,ax = ax2,ticks=[0,32,64,96,128,160],label='Morphine Milligram Equivalents per Day',extend='max')

vmin = 0
vmax = 100
norm = plt.Normalize(vmin=0, vmax=vmax)
fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1, figsize=(20, 16))
ax1.set_ylim([21.5, 26.5])
ax1.set_xlim([117.5, 123.5])
ax1 = overall_4_pop_geo.plot(ax=ax1, linewidth=0.8, edgecolor='0',column=2012,cmap = discrete_cmap(5, 'OrRd'),vmin=0, vmax=vmax)
ax1.set_title('4 common opioids prescription per 1000 Medical Care-seeking population in Taiwan, 2012',fontweight=12,fontsize=14)
ax1.set_axis_off()
scatter1 = ax1.collections[0]
plt.colorbar(scatter1,ax = ax1,ticks=[0,20,40,60,80,100],label='Number of Medical Care-seeking population per 1000',extend='max')
ax2.set_ylim([21.5, 26.5])
ax2.set_xlim([117.5, 123.5])
ax2 = overall_4_pop_geo.plot(ax=ax2, linewidth=0.8, edgecolor='0',column=2016,cmap = discrete_cmap(5, 'OrRd'),vmin=0, vmax=vmax)
ax2.set_title('4 common opioids prescription per 1000 Medical Care-seeking population in Taiwan, 2016',fontweight=12,fontsize=14)
ax2.set_axis_off()
scatter2 = ax2.collections[0]
plt.colorbar(scatter2,ax = ax2,ticks=[0,20,40,60,80,100],label='Number of Medical Care-seeking population per 1000',extend='max')






vmin = 0
vmax = 20
norm = plt.Normalize(vmin=0, vmax=vmax)
f,ax= plt.subplots(figsize=(10, 8))
ax.set_ylim([21.5, 26.5])
ax.set_xlim([117.5, 123.5])
Pethidine_geo.plot(ax=ax, linewidth=0.8, edgecolor='0',column=2012,cmap = discrete_cmap(5, 'OrRd_r'),vmin=0, vmax=vmax)
ax.set_title('title test',fontweight=12,fontsize=14)
ax.set_axis_off()
scatter = ax.collections[0]
plt.colorbar(scatter,ticks=[0,4,8,12,16,20],label='Morphine Milligram Equivalents per Day',extend='max')



cax = fig.add_axes([10, 0.1, 0.03, 0.8])
sm = plt.cm.ScalarMappable(cmap='YlOrRd', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbr = fig.colorbar(sm, cax=cax)
cbr.ax.tick_params(labelsize=200) 
plt.tight_layout()
plt.show()

plt.colorbar(scatter, ax=ax, extend='min')




"""
Test Area1
"""
f,ax1= plt.subplots(1)
ax1.set_ylim([21.5, 26.5])
ax1.set_xlim([117.5, 123.5])
test.plot(ax=ax1,linewidth=5, edgecolor='0.5' ,vmin=0, vmax=100, legend=True)
plt.show()
"""
"""

"""
Test Area2
"""
f, ax = plt.subplots(1)
shp.plot(ax=ax, linewidth=5, edgecolor='0.5')
plt.axis('equal')
plt.show()
"""
"""




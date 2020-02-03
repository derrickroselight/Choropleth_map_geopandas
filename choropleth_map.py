

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

""" Read files """

overall_4_Px = pd.read_excel('/Users/Light/PythonData/overall_opioid_trend.xlsx', sheet_name=0)
city_shp = gpd.read_file('/Users/Light/PythonData/GeoCityData/COUNTY_MOI_1080617.shp')
city_shp.plot()


""" Merge """

Codeine_geo = pd.merge(left = city_shp, right = Codeine, on='COUNTYID')
Morphine_geo = pd.merge(left = city_shp, right = Morphine, on='COUNTYID')
Fentanyl_geo = pd.merge(left = city_shp, right = Fentanyl, on='COUNTYID')
Pethidine_geo = pd.merge(left = city_shp, right = Pethidine, on='COUNTYID')

overall_4_Px_geo = pd.merge(left = city_shp, right = overall_4_Px, on='COUNTYID')



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




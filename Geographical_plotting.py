#!/usr/bin/env python
# coding: utf-8

# In[21]:


import plotly.plotly as pl
import plotly.graph_objs as gobj 
import pandas as pd


# In[22]:


from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot


# In[155]:


init_notebook_mode(connected=True)


# scope ( enumerated : "world" | "usa" | "europe" | "asia" | "africa" | "north america" | "south america" ) 

# locationmode ( enumerated : "ISO-3" | "USA-states" | "country names" ) 
# default: "ISO-3" 

# colorscales:
#             ['Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 'RdBu',
#             'Reds', 'Blues', 'Picnic', 'Rainbow', 'Portland', 'Jet',
#             'Hot', 'Blackbody', 'Earth', 'Electric', 'Viridis', 'Cividis']

# bgcolor
#                 Sets the color of padded area.
#             bordercolor
#                 Sets the axis line color.
#             borderwidth
#                 Sets the width (in px) or the border enclosing
#                 this color bar.
#             dtick
#                 Sets the step in-between ticks on this axis.
#                 Use with `tick0`. Must be a positive number, or
#                 special strings available to "log" and "date"
#                 axes. If the axis `type` is "log", then ticks
#                 are set every 10^(n*dtick) where n is the tick
#                 number. For example, to set a tick mark at 1,
#                 10, 100, 1000, ... set dtick to 1. To set tick
#                 marks at 1, 100, 10000, ... set dtick to 2. To
#                 set tick marks at 1, 5, 25, 125, 625, 3125, ...
#                 set dtick to log_10(5), or 0.69897000433. "log"
#                 has several special values; "L<f>", where `f`
#                 is a positive number, gives ticks linearly
#                 spaced in value (but not position). For example
#                 `tick0` = 0.1, `dtick` = "L0.5" will put ticks
#                 at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
#                 plus small digits between, use "D1" (all
#                 digits) or "D2" (only 2 and 5). `tick0` is
#                 ignored for "D1" and "D2". If the axis `type`
#                 is "date", then you must convert the time to
#                 milliseconds. For example, to set the interval
#                 between ticks to one day, set `dtick` to
#                 86400000.0. "date" also has special values
#                 "M<n>" gives ticks spaced by a number of
#                 months. `n` must be a positive integer. To set
#                 ticks on the 15th of every third month, set
#                 `tick0` to "2000-01-15" and `dtick` to "M3". To
#                 set ticks every 4 years, set `dtick` to "M48"
#             exponentformat
#                 Determines a formatting rule for the tick
#                 exponents. For example, consider the number
#                 1,000,000,000. If "none", it appears as
#                 1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
#                 "power", 1x10^9 (with 9 in a super script). If
#                 "SI", 1G. If "B", 1B.
#             len
#                 Sets the length of the color bar This measure
#                 excludes the padding of both ends. That is, the
#                 color bar length is this length minus the
#                 padding on both ends.
#             lenmode
#                 Determines whether this color bar's length
#                 (i.e. the measure in the color variation
#                 direction) is set in units of plot "fraction"
#                 or in *pixels. Use `len` to set the value.
#             nticks
#                 Specifies the maximum number of ticks for the
#                 particular axis. The actual number of ticks
#                 will be chosen automatically to be less than or
#                 equal to `nticks`. Has an effect only if
#                 `tickmode` is set to "auto".
#             outlinecolor
#                 Sets the axis line color.
#             outlinewidth
#                 Sets the width (in px) of the axis line.
#             separatethousands
#                 If "true", even 4-digit integers are separated
#             showexponent
#                 If "all", all exponents are shown besides their
#                 significands. If "first", only the exponent of
#                 the first tick is shown. If "last", only the
#                 exponent of the last tick is shown. If "none",
#                 no exponents appear.
#             showticklabels
#                 Determines whether or not the tick labels are
#                 drawn.
#             showtickprefix
#                 If "all", all tick labels are displayed with a
#                 prefix. If "first", only the first tick is
#                 displayed with a prefix. If "last", only the
#                 last tick is displayed with a suffix. If
#                 "none", tick prefixes are hidden.
#             showticksuffix
#                 Same as `showtickprefix` but for tick suffixes.
#             thickness
#                 Sets the thickness of the color bar This
#                 measure excludes the size of the padding, ticks
#                 and labels.
#             thicknessmode
#                 Determines whether this color bar's thickness
#                 (i.e. the measure in the constant color
#                 direction) is set in units of plot "fraction"
#                 or in "pixels". Use `thickness` to set the
#                 value.
#             tick0
#                 Sets the placement of the first tick on this
#                 axis. Use with `dtick`. If the axis `type` is
#                 "log", then you must take the log of your
#                 starting tick (e.g. to set the starting tick to
#                 100, set the `tick0` to 2) except when
#                 `dtick`=*L<f>* (see `dtick` for more info). If
#                 the axis `type` is "date", it should be a date
#                 string, like date data. If the axis `type` is
#                 "category", it should be a number, using the
#                 scale where each category is assigned a serial
#                 number from zero in the order it appears.
#             tickangle
#                 Sets the angle of the tick labels with respect
#                 to the horizontal. For example, a `tickangle`
#                 of -90 draws the tick labels vertically.
#             tickcolor
#                 Sets the tick color.
#             tickfont
#                 Sets the color bar's tick label font
#             tickformat
#                 Sets the tick label formatting rule using d3
#                 formatting mini-languages which are very
#                 similar to those in Python. For numbers, see: h
#                 ttps://github.com/d3/d3-format/blob/master/READ
#                 ME.md#locale_format And for dates see:
#                 https://github.com/d3/d3-time-
#                 format/blob/master/README.md#locale_format We
#                 add one item to d3's date formatter: "%{n}f"
#                 for fractional seconds with n digits. For
#                 example, *2016-10-13 09:15:23.456* with
#                 tickformat "%H~%M~%S.%2f" would display
#                 "09~15~23.46"
#             tickformatstops
#                 plotly.graph_objs.choropleth.colorbar.Tickforma
#                 tstop instance or dict with compatible
#                 properties
#             tickformatstopdefaults
#                 When used in a template (as layout.template.dat
#                 a.choropleth.colorbar.tickformatstopdefaults),
#                 sets the default property values to use for
#                 elements of choropleth.colorbar.tickformatstops
#             ticklen
#                 Sets the tick length (in px).
#             tickmode
#                 Sets the tick mode for this axis. If "auto",
#                 the number of ticks is set via `nticks`. If
#                 "linear", the placement of the ticks is
#                 determined by a starting position `tick0` and a
#                 tick step `dtick` ("linear" is the default
#                 value if `tick0` and `dtick` are provided). If
#                 "array", the placement of the ticks is set via
#                 `tickvals` and the tick text is `ticktext`.
#                 ("array" is the default value if `tickvals` is
#                 provided).
#             tickprefix
#                 Sets a tick label prefix.
#             ticks
#                 Determines whether ticks are drawn or not. If
#                 "", this axis' ticks are not drawn. If
#                 "outside" ("inside"), this axis' are drawn
#                 outside (inside) the axis lines.
#             ticksuffix
#                 Sets a tick label suffix.
#             ticktext
#                 Sets the text displayed at the ticks position
#                 via `tickvals`. Only has an effect if
#                 `tickmode` is set to "array". Used with
#                 `tickvals`.
#             ticktextsrc
#                 Sets the source reference on plot.ly for
#                 ticktext .
#             tickvals
#                 Sets the values at which ticks on this axis
#                 appear. Only has an effect if `tickmode` is set
#                 to "array". Used with `ticktext`.
#             tickvalssrc
#                 Sets the source reference on plot.ly for
#                 tickvals .
#             tickwidth
#                 Sets the tick width (in px).
#             title
#                 plotly.graph_objs.choropleth.colorbar.Title
#                 instance or dict with compatible properties
#             titlefont
#                 Deprecated: Please use
#                 choropleth.colorbar.title.font instead. Sets
#                 this color bar's title font. Note that the
#                 title's font used to be set by the now
#                 deprecated `titlefont` attribute.
#             titleside
#                 Deprecated: Please use
#                 choropleth.colorbar.title.side instead.
#                 Determines the location of color bar's title
#                 with respect to the color bar. Note that the
#                 title's location used to be set by the now
#                 deprecated `titleside` attribute.
#             x
#                 Sets the x position of the color bar (in plot
#                 fraction).
#             xanchor
#                 Sets this color bar's horizontal position
#                 anchor. This anchor binds the `x` position to
#                 the "left", "center" or "right" of the color
#                 bar.
#             xpad
#                 Sets the amount of padding (in px) along the x
#                 direction.
#             y
#                 Sets the y position of the color bar (in plot
#                 fraction).
#             yanchor
#                 Sets this color bar's vertical position anchor
#                 This anchor binds the `y` position to the
#                 "top", "middle" or "bottom" of the color bar.
#             ypad
#                 Sets the amount of padding (in px) along the y
#                 direction.
# 

# ## India's Neighbours

# In[449]:


data = dict(type = 'choropleth',
            locations = ['India','Nepal','China','Pakistan','Bangladesh','Bhutan','Myanmar','Sri Lanka'],
            locationmode = 'country names',
            colorscale= 'Portland',
            text= ['IND','NEP','CHI','PAK','BAN','BHU', 'MYN','SLK'],
            z=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0],
            colorbar = {'title':'Country Colours', 'len':200,'lenmode':'pixels' })


# In[450]:


layout = dict(geo = {'scope':'asia'})


# In[451]:


col_map = gobj.Figure(data = [data],layout = layout)


# In[452]:


iplot(col_map)


# ## India's Neighbours' Population 2018

# In[456]:


pop = pd.read_csv('popula.csv')


# In[457]:


pop.columns


# In[299]:


cols = ['Country Name','2018']


# In[300]:


countries  = ['India','Pakistan','China','Bangladesh','Nepal','Bhutan','Myanmar','Sri Lanka']


# In[479]:


new_pop = pop[cols][pop['Country Name'].isin(countries)]


# In[481]:


new_pop


# In[567]:


data2 = dict(type = 'choropleth',
            locations = new_pop['Country Name'],
            locationmode = 'country names',
            autocolorscale = False,
            colorscale = 'RdBu',
            text= new_pop['Country Name'],
            z=new_pop['2018'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 1)),
            colorbar = {'title':'Colour Range','len':0.25,'lenmode':'fraction'})


# In[568]:


layout2 = dict(geo = dict(scope='asia'))
                         #showlakes = True,
                         #lakecolor = 'rgb(85,173,240)'))
                         #colorscale = { 'sequential':'Blues'}) #geo = {'scope':'world'}


# In[569]:


asiamap = gobj.Figure(data = [data2],layout = layout2)


# In[570]:


iplot(asiamap)


# ## World Population 2018

# In[575]:


pop = pd.read_csv('popula.csv')


# In[576]:


cols = ['Country Name','2018']


# In[577]:


new = pop[cols]


# In[578]:


data3 = dict(type = 'choropleth',
            locations = new['Country Name'],
            locationmode = 'country names',
            autocolorscale = False,
            colorscale = 'Rainbow',
            text= new['Country Name'],
            z=new['2018'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 1)),
            colorbar = {'title':'Colour Range','len':0.25,'lenmode':'fraction'})


# In[579]:


layout3 = dict(geo = dict(scope='world'))
                       


# In[580]:


worldmap = gobj.Figure(data = [data3],layout = layout3)


# In[582]:


iplot(worldmap)


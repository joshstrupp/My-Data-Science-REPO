# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:27:48 2015

@author: joshstrupp
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nfl2000 = pd.read_csv('nfl2000stats.csv', sep=',') #13-3
nfl2001 = pd.read_csv('nfl2001stats.csv', sep=',') #7-9
nfl2002 = pd.read_csv('nfl2002stats.csv', sep=',') #11-5
nfl2003 = pd.read_csv('nfl2003stats.csv', sep=',') #12-4
nfl2004 = pd.read_csv('nfl2004stats.csv', sep=',') #5-11
nfl2005 = pd.read_csv('nfl2005stats.csv', sep=',') #4-12
nfl2006 = pd.read_csv('nfl2006stats.csv', sep=',') #8-8
nfl2007 = pd.read_csv('nfl2007stats.csv', sep=',') #10-6
nfl2008 = pd.read_csv('nfl2008stats.csv', sep=',') #13-3
nfl2009 = pd.read_csv('nfl2009stats.csv', sep=',') #8-8
nfl2010 = pd.read_csv('nfl2010stats.csv', sep=',') #6-10
nfl2011 = pd.read_csv('nfl2011stats.csv', sep=',') #9-7
nfl2012 = pd.read_csv('nfl2012stats.csv', sep=',') #6-10
nfl2013 = pd.read_csv('nfl2013stats.csv', sep=',') #7-9

nfl2000['WinLoss'] = ('ScoreOff' > 'ScoreDef') #Trying to create column for win/loss

nfl2000.columns


#LIST W-L for Titans each year

#13-3
nfl2000.ScoreOff.mean() #20.57
nfl2000.groupby('TeamName').ScoreOff.mean() #20.3
nfl2000.groupby('TeamName').ScoreDef.mean() #13.43

#7-9
nfl2001.ScoreOff.mean() #20.21
nfl2001.groupby('TeamName').ScoreOff.mean() #21 
nfl2001.groupby('TeamName').ScoreDef.mean() #24.25

#11-5
nfl2002.ScoreOff.mean() #21.67
nfl2002.groupby('TeamName').ScoreOff.mean() #22.93
nfl2002.groupby('TeamName').ScoreDef.mean() #20.25

#12-4
nfl2003.ScoreOff.mean() #20.83
nfl2003.groupby('TeamName').ScoreOff.mean() #27.18
nfl2003.groupby('TeamName').ScoreDef.mean() #20.25

#5-11
nfl2004.ScoreOff.mean() #21.48
nfl2004.groupby('TeamName').ScoreOff.mean() #21.5
nfl2004.groupby('TeamName').ScoreDef.mean() #27.43

#4-12
nfl2005.ScoreOff.mean() #20.61
nfl2005.groupby('TeamName').ScoreOff.mean() #18.68
nfl2005.groupby('TeamName').ScoreDef.mean() #26.31

#8-8
nfl2006.ScoreOff.mean() #20.66
nfl2006.groupby('TeamName').ScoreOff.mean() #20.25
nfl2006.groupby('TeamName').ScoreDef.mean() #25

#10-6
nfl2007.ScoreOff.mean() #21.69
nfl2007.groupby('TeamName').ScoreOff.mean() #18.81
nfl2007.groupby('TeamName').ScoreDef.mean() #18.56

#13-3
nfl2008.ScoreOff.mean() #22.03
nfl2008.groupby('TeamName').ScoreOff.mean() #23.44
nfl2008.groupby('TeamName').ScoreDef.mean() #14.62

#8-8
nfl2009.ScoreOff.mean() #21.47
nfl2009.groupby('TeamName').ScoreOff.mean() #22.13
nfl2009.groupby('TeamName').ScoreDef.mean() #25.125

#6-10
nfl2010.ScoreOff.mean() #22.04
nfl2010.groupby('TeamName').ScoreOff.mean() #22.25
nfl2010.groupby('TeamName').ScoreDef.mean() #21.19

#9-7
nfl2011.ScoreOff.mean() #22.18
nfl2011.groupby('TeamName').ScoreOff.mean() #20.31
nfl2011.groupby('TeamName').ScoreDef.mean() #19.81

#6-10
nfl2012.ScoreOff.mean() #22.75
nfl2012.groupby('TeamName').ScoreOff.mean() #20.625
nfl2012.groupby('TeamName').ScoreDef.mean() #29.44

#7-9
nfl2013.ScoreOff.mean() #23.41
nfl2013.groupby('TeamName').ScoreOff.mean() #22.62
nfl2013.groupby('TeamName').ScoreDef.mean() #23.81

#is there a way to merge into one massive df?
nfl = pd.merge(nfl2000, nfl2001, how='outer', on=None, left_on=None, right_on=None,
      left_index=True, right_index=True, sort=True,
      suffixes=('_x', '_y'), copy=True)




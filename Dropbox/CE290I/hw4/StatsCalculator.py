
# coding: utf-8

# In[12]:

import numpy as np
from scipy import stats
data=np.genfromtxt('TestData.csv', delimiter=',', skiprows=1)
DropBox,Box,GoogleDrive,MicrosoftOneDrive,Local=data[:,0],data[:,1],data[:,2],data[:,3],data[:,4]


# In[23]:

#Comparing DropBox to Local, unequal variances
DropBoxToLocal=stats.ttest_ind(DropBox,Local,axis=0,equal_var=False)
print DropBoxToLocal


# In[17]:

#Comparing Box to Local, unequal variances
BoxToLocal=stats.ttest_ind(Box,Local,axis=0,equal_var=False)
print BoxToLocal


# In[18]:

#Comparing GoogleDrive to Local, unequal variances
GoogleDriveToLocal=stats.ttest_ind(GoogleDrive,Local,axis=0,equal_var=False)
print GoogleDriveToLocal


# In[19]:

#Comparing MicrosoftOneDrive to Local, unequal variances
MicrosoftOneDriveToLocal=stats.ttest_ind(MicrosoftOneDrive,Local,axis=0,equal_var=False)
print MicrosoftOneDriveToLocal


# In[21]:

#Comparing Local to Local, unequal variances, just a test :)
LocalToLocal=stats.ttest_ind(Local,Local,axis=0,equal_var=False)
print LocalToLocal


# In[ ]:




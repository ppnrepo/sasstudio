# Youtube: https://www.youtube.com/watch?v=nx7-LDxHkxA

# Import the SWAT package into the Python session
import swat

# Import pandas to gain access the any pandas functions
import pandas as pd

# Import matplotlib to gain access its plotting capabilities
import matplotlib.pyplot as plt

# Set enviroment variables 
os.environ['CAS_CLIENT_SSL_CA_LIST'] = r"d:\temp\trustedcerts.pem"

# Run a connection statement
# Use Python enviroment variables to prevent plain text passawords within the code.
conn = swat.CAS('https://sasserver.demo.sas.com/cas-shared-default-http/', port=8777, username="sasdemo", password="password")

# Read connection´s status
conn.serverstatus()

# Load data into a local CASLIB - Read raw data
castbl = conn.upload_file(data='home/sas/studentperformance.csv', casout=dict(name='StudentsPerformance', caslib='casuser', replace=True))

# View the first 10 rows of the data
castbl.head(10)

# Creating histograms of the data
plt.show()

# Manipulate Data - Addressing Incorrect Data
# Identify the student with a reading score of greater than 100
# This must be a mistake
caslib[castbl['reading score']>100].head()

# Replace reading score value of 120 with the value of missing.
castbl['reading score'].replace(120, pd.np.nan, inplace=True)
CASColumn('STUDENTPERFORMANCE', caslib='CASUSER(alexandre.alves@gmail.com)')['reading score']

# Explore data
castbl.info()

# If you have missing value, one way is use statistic formula to impute - fillna method - (replace on this case) any missing data
# For exemple - median()
castbl,fillna(castbl.median(), inplace=true)

# check if it´s ok
castbl.info()

# Promoting the Data - Making the data available to all active CAS Sessions (not for only one user)
# 2 options to do that: 
#   - Continue to code in Python
#   - SAS Viya products: SAS Visual Analytics, SAS Model Manager and SAS Visual DM and ML
conn.promote(name=castbl, targetlib='public', target='STUDENTMODIFIED')

# Connect to new CAS Table => STUDENTMODIFIED
casstumod = conn.CASTable('STUDENTMODIFIED', caslib='public')

# Information about new table STUDENTMODIFIED
casstumod.info()

# Box Plots - Python Box Plots
casstumod.boxplot(column='math score', by='parental level of education', patch_artist=True, capprops=dict(linewidth=2), whiskerprops=dict(linewidth=2), medianprops=dict(linewidth=2)figsize=(15,9))
plt.title('Math Score By Parental level of Education')
plt.show()
# Alternatively that boxplot can be done at SAS Visual Analytics

# Scatter Graphs
casstumod.plot(x='writinh score', y='reading score', kind='scatter', color='purple',figsize=(15,9))
plt.title('Reading Scores vs Writing Scores')
plt.show()
# Alternatively that boxplot can be done at SAS Visual Analytics













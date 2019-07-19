# ==============================================================================================================================================================
#
# PLUTUS - Share Code Machine Learning Codebase
#
# Application that find key attributes for predicting share prices into the future
#
# ==============================================================================================================================================================

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import pathlib                      # for handling local dorectories
import time                         # for reporting how much time the functions take to finish
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from application_log                import log_application_header, log_application_footer
from data_OHLC                      import load_ohlc_data_file, save_ohlc_share_df, create_share_dict
from features_volume                import add_volumn_features
from features_price                 import add_price_features
from features_dates                 import add_date_features

pd.set_option('display.max_columns', 500)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Application CEO
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
application_start_time = time.time()  
log_application_header()

share_dict          = load_ohlc_data_file()                                             # load the OHLC share data from Disk
# share_dict          = add_date_features( share_dict )                                   # date related features and indicators
# share_dict          = add_volumn_features( share_dict )                                 # volume Indicators
# share_dict          = add_price_features( share_dict )                                  # Attach Price  Features to the dataset


# -------------------------------------------------------------------------------------- Save the OHLC Share Dataframe to Disk
# save_ohlc_share_df( share_df )

log_application_footer(application_start_time)


# for share_code, share_data in share_dict.items():
#     print ( share_code )
#     print ( '' )
#     print ( share_data.head(5) )

# for share_data in share_dict.values():
#     # print ( share_code )
#     print ( '' )
#     print ( share_data.tail(5) )




# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# PROCESS issues
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# How to proceed
# 1)  load all data and add all features - or 
# 2)  load the latest data and add the missing features to it

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# CODE issues
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# x future and past vol and price can be achieved by deleting or adding rows at the beginning or end of the current dataframe - sort of shift the column up or down and then merge back by date
# x adding past volume is very slow and not flexible - lets see what we can do with this
# x add file state save after modifications
# x add better iteration - loop through lists
# x add better screen logging
# x try splitting loaded share data into a dictionary
# x get rid of pychach using git ignore
# x update counter in dictionary iteration

# change python version for code base - ask liam how to change which version of python is running on this project
# maybe add in some price and vol features - ie moved <1% 2-5% etc and then do some basic ML to see if anything of significance pops up
# add the daily dowload merging code into this application so it can be re-run or appended to somehow?
# redo create_share_dict - remove index check as this seems to be a python 2.7 issue
# add dataframe to dictionary needs to be faster - takes 631 seconds which is 70% of the run time




# ============================================================================================================================================


# PLUTUS SHARE DATA ANAYSER AND MACHINE LEARNING CODE BASE -   - commenced @ 2019-07-17 21:03:38


# ============================================================================================================================================
# --------------------------------------------------------------------------------------------------------------------------------------------
# Load OHLC Share data
# process                                                               progress       share codes    rows      columns   load time           
# --------------------------------------------------------------------------------------------------------------------------------------------
# loading OHLC                                                          Completed      5258           6790426   8         seconds = 012.239
# first date        in share file =  1997-01-02 00:00:00
# last  date        in share file =  2018-09-28 00:00:00
# subset share codes to dictionary                                      
# Completed      5258           6790426   8.0       seconds = 631.199
# add sequential counter to OHLC share data                             Completed      5258           6790426   11.0      seconds = 043.354
# --------------------------------------------------------------------------------------------------------------------------------------------
#                                                                       COMPLETED      total time =   686.83 seconds   011.447 minutes
# --------------------------------------------------------------------------------------------------------------------------------------------
# Add Date Related Features
# process                                                               progress       share codes    rows      columns   load time           
# --------------------------------------------------------------------------------------------------------------------------------------------
# adding weekday and month number                                       Completed      5258           6790426   13.0      seconds = 008.468
# adding day name                                                       Completed      5258           6790426   20.0      seconds = 032.534
# adding month name                                                     Completed      5258           6790426   32.0      seconds = 049.375
# --------------------------------------------------------------------------------------------------------------------------------------------
#                                                                       COMPLETED      total time =   90.377 seconds   001.506 minutes
# --------------------------------------------------------------------------------------------------------------------------------------------
# Add Volume Features to OHLC Share data
# process                                                               progress       share codes    rows      columns   load time           
# --------------------------------------------------------------------------------------------------------------------------------------------
# adding average volume to OHLC df                                      Completed      5258           6790426   33.0      seconds = 003.634
# adding past & future volume                                           Completed      5258           6790426   45.0      seconds = 089.323
# --------------------------------------------------------------------------------------------------------------------------------------------
#                                                                       COMPLETED      total time =   92.957 seconds   001.549 minutes
# --------------------------------------------------------------------------------------------------------------------------------------------
# Add Share Price Features to OHLC Share data
# process                                                               progress       share codes    rows      columns   load time           
# --------------------------------------------------------------------------------------------------------------------------------------------
# adding past & future price                                            Completed      5258           6790426   57.0      seconds = 091.814
# --------------------------------------------------------------------------------------------------------------------------------------------
#                                                                       COMPLETED      total time =   91.814 seconds   001.053 minutes
# ============================================================================================================================================
# FINISHED PROCESSING @ 2019-07-17 21:19:40 - total load time = 962.06 seconds  -  16.03 minutes
# ============================================================================================================================================
# (base) Robs-Personal-MacBook-Pro:plutus_share_ml robhay$ 
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
share_dict          = add_date_features( share_dict )                                   # date related features and indicators
share_dict          = add_volumn_features( share_dict )                                 # volume Indicators
share_dict          = add_price_features( share_dict )                                  # Attach Price  Features to the dataset


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
# coding issues
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# How to proceed
# 1)  load all data and add all features - or 
# 2)  load the latest data and add the missing features to it

# <1> requires fast code - which is a requirement anyway
# <2> requires some checking that we dont already have the data and then some cleaver merging/appending code at the end

# future and past vol and price can be achieved by deleting or adding rows at the beginning or end of the current dataframe - sort of shift the column up or down and then merge back by date
# adding past volume is very slow and not flexible - lets see what we can do with this

# add file state save after modifications
# Ensure the columns are in the order you want
# add better iteration - loop through lists
# add better screen logging
# try splitting loaded share data into a dictionary

# maybe add in some price and vol features - ie moved <1% 2-5% etc and then do some basic ML to see if anything of significance pops up
# get rid of pychach using git ignore
# update counter in dictionary iteration
# add the daily dowload merging code into this application so it can be re-run or appended to somehow?
# ask liam how to change which version of python is running on this project
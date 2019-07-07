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
# from application_log                import print_seperator

from data_OHLC                      import ohlc_loader, load_OHLC_share_df, add_sequential_counter
from features_volume                import add_volumn_features
from features_price                 import price_values
from features_dates                 import add_date_features
from application_log                import log_application_header, log_application_footer


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Application CEO
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
application_start_time = time.time()  
log_application_header()

share_df            = ohlc_loader()                                             # load the OHLC share data from Disk
# list_of_share_codes = list_of_share_codes( share_df )
# ----------------------------------------------- volume Indicators
# share_df            = add_volumn_features( share_df )                           # volume Indicators

# share_df = price_values( share_df )                                     # Attach Price  Features to the dataset
#########################
# maybe add in some price and vol features - ie moved <1% 2-5% etc and then do some basic ML to see if anything of significance pops up

share_df            = add_date_features( share_df )                             # date related features and indicators

# print ( share_df.tail(7) )


# ----------------------------------------------- Save the OHLC Share Dataframe to Disk
# app.save_OHLC_share_df( share_df )

log_application_footer(application_start_time)








# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# coding issues
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# Do we 
# 1)  load all data and add all features - or 
# 2)  load the latest data and add the missing features to it

# 1) requires fast code - which is a requirement anyway
# 2) requires some checking that we dont already have the data and then some cleaver merging/appending code at the end


# future and past vol and price can be achieved by deleting or adding rows at the beginning or end of the current dataframe - sort of shift the column up or down and then merge back by date


# adding past volumn is very slow and not flixible - lets see what we can do with this
# add file state save after modifications
# Ensure the columns are in the order you want




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
# import numpy as np
# import pathlib                      # for handling local directories
import time                         # for reporting how much time the functions take to finish
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from application_log                import log_application_header, log_application_footer
from common                         import convert_dict_into_single_df, sort_df_into_alphabetical_order
from data_OHLC                      import load_ohlc_data_file, save_ohlc_share_df
from features_volume                import add_volume_features
from features_price                 import add_price_features
from features_dates                 import add_date_features
from features                       import add_primary_analysis_features
from ml                             import machine_learning_manager

pd.set_option('display.max_columns', 500)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Application CEO
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
application_start_time = time.time()  
log_application_header()


share_df            = load_ohlc_data_file()                                             # load the OHLC share data from Disk
# share_df            = add_date_features( share_df )                                     # date related features and indicators

share_dict          = add_volume_features( share_df )                                   # volume Indicators
share_dict          = add_price_features( share_dict )                                  # Attach Price  Features to the dataset

share_df            = convert_dict_into_single_df( share_dict )                         # ready for saving the result

share_df            = add_primary_analysis_features( share_df )                         # add in primary Y features

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Machine Learning Code
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# value_to_predict    = 'y_close_up_in_01_days'
# machine_learning_manager ( share_df, value_to_predict )

# -------------------------------------------------------------------------------------- Save the OHLC Share Dataframe to Disk
# save_ohlc_share_df( share_df )
# -------------------------------------------------------------------------------------- Close Application
log_application_footer( application_start_time )


share_df = sort_df_into_alphabetical_order( share_df )

# print ( list(share_df) )
print ( share_df.head(10))
# print ( share_df[[ 'close', 'volume', 'volume_average_per_minute', 'volume_ma_03_per_minute', 'volume_ma_08_per_minute', 'volume_ma_21_per_minute', 'Y_close_up_in_01_days']] )







# for share_code, share_data in share_dict.items():
#     print ( share_code )
#     print ( '' )
#     print ( share_data.head(5) )

# for share_data in share_dict.values():
#     # print ( share_code.upper() )
#     print ( '' )
#     print ( share_data.tail(5) )



# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# Speed Tracking
# date          seconds            minutes                      notes
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# 17 July 19    962.06 seconds  -  16.03 minutes                first go at the initials data analysis - focus on dict next as really slow
# 19 july 19    190.29 seconds  -  3.17 minutes                 pretty big improvement - 3 mins is ok
# 22 July 19    171.35 seconds  -  2.86 minutes                 minor improvements 



# --------------------------------------------------------------------------------------------------------------------------------------------
# Add Volume Features to OHLC Share data
# process                                                               progress       share codes    rows      columns   load time           
# --------------------------------------------------------------------------------------------------------------------------------------------
# adding average volume to OHLC df                                      Completed      5258           6790426   33        seconds = 000.309
# subset share codes into a dictionary                                  Completed      5258           6790426   33.0      seconds = 010.256
# adding past & future volume                                           Completed      5258           6790426   45.0      seconds = 070.195
# --------------------------------------------------------------------------------------------------------------------------------------------
#                                                                       COMPLETED      total time =   80.76 seconds    001.346 minutes
# --------------------------------------------------------------------------------------------------------------------------------------------
# Add Share Price Features to OHLC Share data
# process                                                               progress       share codes    rows      columns   load time           
# --------------------------------------------------------------------------------------------------------------------------------------------
# adding past & future price                                            Completed      5258           6790426   57.0      seconds = 075.222
# --------------------------------------------------------------------------------------------------------------------------------------------
#                                                                       COMPLETED      total time =   75.222 seconds   001.254 minutes
# ============================================================================================================================================
# FINISHED PROCESSING @ 2019-07-22 19:03:09 - total processing time = 171.35 seconds  -  2.86 minutes
# ============================================================================================================================================


# ============================================================================================================================================
# --------------------------------------------------------------------------------------------------------------------------------------------
# Load OHLC Share data
# process                                                               progress       share codes    rows      columns   load time           
# --------------------------------------------------------------------------------------------------------------------------------------------
# loading OHLC                                                          Completed      5258           6790426   8         seconds = 006.087
# first date        in share file =  1997-01-02 00:00:00
# last  date        in share file =  2018-09-28 00:00:00
# add sequential counter to OHLC share data                             Completed      5258           6790426   11        seconds = 002.174
# --------------------------------------------------------------------------------------------------------------------------------------------
#                                                                       COMPLETED      total time =   08.303 seconds   000.138 minutes
# --------------------------------------------------------------------------------------------------------------------------------------------
# Add Date Related Features
# process                                                               progress       share codes    rows      columns   load time           
# --------------------------------------------------------------------------------------------------------------------------------------------
# adding week day number                                                Completed      5258           6790426   12        seconds = 000.584
# adding month number                                                   Completed      5258           6790426   13        seconds = 000.506
# adding day name for mon                                               Completed      5258           6790426   14        seconds = 000.319
# adding day name for tue                                               Completed      5258           6790426   15        seconds = 000.631
# adding day name for wed                                               Completed      5258           6790426   16        seconds = 000.941
# adding day name for thur                                              Completed      5258           6790426   17        seconds = 001.253
# adding day name for fri                                               Completed      5258           6790426   18        seconds = 001.571
# adding day name for sat                                               Completed      5258           6790426   19        seconds = 001.889
# adding day name for sun                                               Completed      5258           6790426   20        seconds = 002.209
# adding month name for jan                                             Completed      5258           6790426   21        seconds = 000.313
# adding month name for feb                                             Completed      5258           6790426   22        seconds = 000.635
# adding month name for mar                                             Completed      5258           6790426   23        seconds = 000.945
# adding month name for apr                                             Completed      5258           6790426   24        seconds = 001.257
# adding month name for may                                             Completed      5258           6790426   25        seconds = 001.563
# adding month name for jun                                             Completed      5258           6790426   26        seconds = 001.875
# adding month name for jul                                             Completed      5258           6790426   27        seconds = 002.189
# adding month name for aug                                             Completed      5258           6790426   28        seconds = 002.501
# adding month name for sep                                             Completed      5258           6790426   29        seconds = 002.825
# adding month name for oct                                             Completed      5258           6790426   30        seconds = 003.015
# adding month name for nov                                             Completed      5258           6790426   31        seconds = 003.474
# adding month name for dec                                             Completed      5258           6790426   32        seconds = 003.783
# --------------------------------------------------------------------------------------------------------------------------------------------
#                                                                       COMPLETED      total time =   07.081 seconds   000.118 minutes
# --------------------------------------------------------------------------------------------------------------------------------------------
# Convert Dataframe into a Dictionary of Shares
# process                                                               progress       share codes    rows      columns   load time           
# --------------------------------------------------------------------------------------------------------------------------------------------
# subset share codes to dictionary                                      Completed      5258           6790426   32.0      seconds = 008.319
# --------------------------------------------------------------------------------------------------------------------------------------------
#                                                                       COMPLETED      total time =   08.32 seconds    000.139 minutes
# --------------------------------------------------------------------------------------------------------------------------------------------
# Add Volume Features to OHLC Share data
# process                                                               progress       share codes    rows      columns   load time           
# --------------------------------------------------------------------------------------------------------------------------------------------
# adding average volume to OHLC df                                      Completed      5258           6790426   33.0      seconds = 003.238
# adding past & future volume                                           Completed      5258           6790426   45.0      seconds = 074.199
# --------------------------------------------------------------------------------------------------------------------------------------------
#                                                                       COMPLETED      total time =   77.437 seconds   001.291 minutes
# --------------------------------------------------------------------------------------------------------------------------------------------
# Add Share Price Features to OHLC Share data
# process                                                               progress       share codes    rows      columns   load time           
# --------------------------------------------------------------------------------------------------------------------------------------------
# adding past & future price                                            Completed      5258           6790426   57.0      seconds = 089.015
# --------------------------------------------------------------------------------------------------------------------------------------------
#                                                                       COMPLETED      total time =   89.15 seconds    001.486 minutes
# ============================================================================================================================================
# FINISHED PROCESSING @ 2019-07-19 21:11:02 - total processing time = 190.29 seconds  -  3.17 minutes
# ============================================================================================================================================





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


# With new dictionary process

# --------------------------------------------------------------------------------------------------------------------------------------------
# Add Share Price Features to OHLC Share data
# process                                                               progress       share codes    rows      columns   load time           
# --------------------------------------------------------------------------------------------------------------------------------------------
# adding past & future price                                            Completed      5258           6790426   57.0      seconds = 079.759
# --------------------------------------------------------------------------------------------------------------------------------------------
#                                                                       COMPLETED      total time =   79.759 seconds   001.329 minutes
# ============================================================================================================================================
# FINISHED PROCESSING @ 2019-07-19 20:39:51 - total processing time = 273.67 seconds  -  4.56 minutes
# ============================================================================================================================================

# and a little more sensible order of functions


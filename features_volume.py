
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# import pandas as pd
# import numpy as np
import time                             # for reporting how much time the functions take to finish
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from common                         import create_share_dict, past_and_future_periods, moving_average_periods
from common                         import col_name_volume_moving_average, col_name_volume_past, col_name_volume_future
from application_log                import log_core_process_header, log_core_process_footer
from application_log                import log_process_commencing,  log_df_process_completed, log_dict_process_completed

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Module Values
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
volume_column_name                      = 'volume'
average_volume_per_minute_column_name   = 'volume_average_per_minute'
minutes_per_day                         = 360                                 # Opening time = 10am and closing time = 4pm. Total minutes = 6 * 60 = 360 minutes


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Worker Functions
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def avg_vol_per_minute( share_df ):
    if volume_column_name in share_df.columns:
        function_start_time = time.time()
        log_process_commencing( str( 'adding average volume to OHLC df' )  )

        share_df[average_volume_per_minute_column_name]    = share_df[ volume_column_name ] / minutes_per_day               

        log_df_process_completed( share_df, function_start_time )       
        return ( share_df )
    else: log_df_process_completed( share_df, time.time(), error_message='volume col missing from shares_df' ); return( share_df )

def time_shifted_average_volume( share_data ):
    for period_no in past_and_future_periods:
        new_past_vol_col    = col_name_volume_past  ( period_no )
        new_future_vol_col  = col_name_volume_future( period_no )

        share_data[ new_past_vol_col ]       = share_data[ average_volume_per_minute_column_name ].shift( period_no )
        share_data[ new_future_vol_col ]     = share_data[ average_volume_per_minute_column_name ].shift( period_no * -1 )

        share_data[ new_past_vol_col ].fillna  ( share_data[ average_volume_per_minute_column_name ], inplace=True)
        share_data[ new_future_vol_col ].fillna( share_data[ average_volume_per_minute_column_name ], inplace=True)

    return ( share_data )

def volume_moving_average( share_data ):  
    for period_no in moving_average_periods:
        new_moving_average_col, new_moving_average_per_minute_col  = col_name_volume_moving_average( period_no )

        share_data[ new_moving_average_col ]            = share_data.volume.rolling(period_no).mean() 
        share_data[ new_moving_average_per_minute_col ] = share_data[ new_moving_average_col ] / minutes_per_day   

        share_data[ new_moving_average_col            ].fillna  ( share_data[ volume_column_name ],                    inplace=True)
        share_data[ new_moving_average_per_minute_col ].fillna  ( share_data[ average_volume_per_minute_column_name ], inplace=True)
    return ( share_data )



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Manager Function
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def add_volumn_features( share_df ):
    core_process_name           = 'Add Volume Features to OHLC Share data'
    core_process_start_time     = time.time()
    log_core_process_header     (  core_process_name )
   

    share_df            = avg_vol_per_minute( share_df )        # Average Volume
    
    share_dict          = create_share_dict( share_df )         # convert df to dictionary for faster time shifting

   #------------------------------------------------------------- time shifted Volume
    function_start_time = time.time()
    log_process_commencing( str( 'adding past & future volume' ) )
    for share_code, share_data in share_dict.items():
        share_dict[share_code] = time_shifted_average_volume( share_data )
    log_dict_process_completed( share_dict, function_start_time )
    #------------------------------------------------------------- moving average on volume
    function_start_time = time.time()
    log_process_commencing( str( 'add moving average to volume' ) )
    for share_code, share_data in share_dict.items():
        share_dict[share_code] = volume_moving_average( share_data )
    log_dict_process_completed( share_dict, function_start_time )


    log_core_process_footer( core_process_name, core_process_start_time )
    return ( share_dict )   





# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# import pandas as pd
# import numpy as np
import time                             # for reporting how much time the functions take to finish
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from common                         import format_period, create_share_dict
from application_log                import log_core_process_header, log_core_process_footer
from application_log                import log_process_commencing,  log_df_process_completed, log_dict_process_completed


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Worker Functions
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def add_average_volume( share_df ):
    if 'volume' in share_df.columns:
        function_start_time = time.time()
        log_process_commencing( str( 'adding average volume to OHLC df' )  )

        share_df['volume_average_per_minute']    = share_df['volume'] / 360                 # Opening time = 10am and closing time = 4pm. Total minutes = 6 * 60 = 360 minutes

        log_df_process_completed( share_df, function_start_time )       
        return ( share_df )
    else: log_df_process_completed( share_df, time.time(), error_message='volume col missing from shares_df' ); return( share_df )


def time_shifted_average_volume( share_data ):
    required_periods = [ 1, 2, 3, 4, 5, 10 ]

    for period_no in required_periods:
        formatted_period_no = format_period( period_no )

        new_past_vol_col    = str( 'past_vol_' +  formatted_period_no )
        new_future_vol_col  = str( 'future_vol_' +  formatted_period_no )

        share_data[ new_past_vol_col ]       = share_data['volume_average_per_minute'].shift( period_no )
        share_data[ new_future_vol_col ]     = share_data['volume_average_per_minute'].shift( period_no * -1 )

        share_data[ new_past_vol_col ].fillna  ( share_data['volume_average_per_minute'], inplace=True)
        share_data[ new_future_vol_col ].fillna( share_data['volume_average_per_minute'], inplace=True)

    return ( share_data )

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Manager Function
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def add_volumn_features( share_df ):
    core_process_name           = 'Add Volume Features to OHLC Share data'
    core_process_start_time     = time.time()
    log_core_process_header     (  core_process_name )
   

    share_df            = add_average_volume( share_df )        # Average Volume
    
    share_dict          = create_share_dict( share_df )         # convert df to dictionary for faster time shifting

   #------------------------------------------------------------- time shifted Volume
    function_start_time = time.time()
    log_process_commencing( str( 'adding past & future volume' ) )
    
    for share_code, share_data in share_dict.items():
        share_dict[share_code] = time_shifted_average_volume( share_data )
    
    log_dict_process_completed( share_dict, function_start_time )

    log_core_process_footer( core_process_name, core_process_start_time )
    return ( share_dict )   




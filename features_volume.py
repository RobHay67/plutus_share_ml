
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# import pandas as pd
# import numpy as np
import time                             # for reporting how much time the functions take to finish
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from common                         import check_dataframe_if_these_cols_exist, lookup_share_value, format_period
# from application_log                import print_seperator, log_process_commencing, log_process_completed
from application_log                import log_core_process_header, log_core_process_footer
from application_log                import log_process_commencing,  log_process_completed
# import app

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Helper Functions
# --------------------------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Worker Functions
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def add_average_volume( share_data ):
    required_columns_list = [ 'volume' ]
    if check_dataframe_if_these_cols_exist( share_data, required_columns_list, 'share dataframe' ) != 'FAILED':
        new_features_being_added = [ 'volume_average' ]     
        if new_features_being_added[0] in share_data.columns: 
            share_data.drop( new_features_being_added, axis=1, inplace=True) 
        share_data['volume_average_per_minute']    = share_data['volume'] / 360                 # Opening time = 10am and closing time = 4pm. Total minutes = 6 * 60 = 360 minutes
    return ( share_data )

def time_shifted_average_volume( share_data ):
    required_periods = [ 1, 2, 3, 4, 5, 10 ]

    for period_no in required_periods:
        
        formatted_period_no = format_period( period_no )

        new_past_vol_col    = str( 'past_vol_' +  formatted_period_no )
        new_future_vol_col  = str( 'future_vol_' +  formatted_period_no )

        share_data[ new_past_vol_col ]       = share_data['volume_average_per_minute'].shift( period_no )
        share_data[ new_future_vol_col ]     = share_data['volume_average_per_minute'].shift( period_no * -1 )

        share_data[ new_past_vol_col ].fillna( share_data['volume_average_per_minute'], inplace=True)

    return ( share_data )

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Manager Function
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def add_volumn_features( share_dict ):
    core_process_name           = 'Add Volume Features to OHLC Share data'
    core_process_start_time     = time.time()
    log_core_process_header     (  core_process_name )

    for share_code, share_data in share_dict.items():
        
        function_start_time = time.time()
        log_process_commencing( str( 'adding average volume to OHLC df' )  )
        share_dict[share_code] = add_average_volume               ( share_data )   
        log_process_completed( share_data, function_start_time )

        function_start_time = time.time()
        log_process_commencing( str( 'adding past & future volume' ) )
        share_dict[share_code] = time_shifted_average_volume      ( share_data )
        log_process_completed( share_data, function_start_time )

    log_core_process_footer( core_process_name, core_process_start_time )
    return ( share_dict )   





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
def add_average_volume( share_df ):
    function_start_time = time.time()
    log_process_commencing( str( 'adding average volume to OHLC df' )  )

    required_columns_list = [ 'volume' ]

    if check_dataframe_if_these_cols_exist( share_df, required_columns_list, 'share dataframe' ) != 'FAILED':
        new_features_being_added = [ 'volume_average' ]     

        if new_features_being_added[0] in share_df.columns: 
            share_df.drop( new_features_being_added, axis=1, inplace=True) 
        
        share_df['volume_average_per_minute']    = share_df['volume'] / 360                 # Opening time = 10am and closing time = 4pm. Total minutes = 6 * 60 = 360 minutes

    log_process_completed( share_df, function_start_time )
    return ( share_df )

def time_shifted_average_volume( share_df ):
    required_periods = [ 1, 2, 3, 4, 5, 10 ]

    for period_no in required_periods:
        function_start_time = time.time()
        formatted_period_no = format_period( period_no )

        new_past_vol_col    = str( 'past_vol_' +  formatted_period_no )
        new_future_vol_col  = str( 'future_vol_' +  formatted_period_no )

        log_process_commencing( str( 'adding - past   volume - ' + formatted_period_no + ' day' ) )
        share_df[ new_past_vol_col ]    = share_df.apply(lambda row: lookup_share_value(row, share_df, ( period_no * -1 ), 'volume_average_per_minute'), axis=1 )
        log_process_completed( share_df, function_start_time )

        function_start_time = time.time()
        log_process_commencing( str( 'adding - future volume - ' + formatted_period_no + ' day' ) )
        share_df[ new_future_vol_col ]  = share_df.apply(lambda row: lookup_share_value(row, share_df, period_no, 'volume_average_per_minute'), axis=1 )
        log_process_completed( share_df, function_start_time )
    
    return ( share_df )

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Manager Function
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def add_volumn_features( share_df ):
    core_process_name           = 'Add Volume Features to OHLC Share data'
    core_process_start_time     = time.time()
    log_core_process_header     (  core_process_name )

    share_df = add_average_volume( share_df )

    share_df = time_shifted_average_volume( share_df )

    log_core_process_footer( core_process_name, core_process_start_time )
    return ( share_df )   




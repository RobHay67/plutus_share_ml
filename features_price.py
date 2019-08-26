# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# import pandas as pd
import time                             # for reporting how much time the functions take to finish
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from application_log                import log_core_process_header, log_core_process_footer
from application_log                import log_process_commencing,  log_dict_process_completed
from common                         import past_and_future_periods, moving_average_periods, closing_price_column_name
from common                         import column_name_close_past, column_name_close_future, column_name_close_moving_average

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Worker Functions
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def time_shifted_close( share_data ):   
    for period_no in past_and_future_periods:       
        new_past_close_column    = column_name_close_past  ( period_no )
        new_future_close_column  = column_name_close_future( period_no )

        share_data[ new_past_close_column ]       = share_data[ closing_price_column_name ].shift( period_no )
        share_data[ new_future_close_column ]     = share_data[ closing_price_column_name ].shift( period_no * -1 )

        share_data[ new_past_close_column   ].fillna  ( share_data[ closing_price_column_name ], inplace=True)
        share_data[ new_future_close_column ].fillna( share_data[ closing_price_column_name ], inplace=True)
    return ( share_data )

def close_moving_average( share_data ):   
    for period_no in moving_average_periods:
        new_moving_average_col = column_name_close_moving_average( period_no )

        share_data[ new_moving_average_col ] = share_data.close.rolling(period_no).mean() 

        share_data[ new_moving_average_col ].fillna  ( share_data[ closing_price_column_name ], inplace=True)
    return ( share_data )

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Manager Function
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def add_price_features( share_dict ):
    core_process_name           = 'Add Share Price Features to OHLC Share data'
    core_process_start_time     = time.time()
    log_core_process_header     (  core_process_name )

    #------------------------------------------------------------- close historical and future price
    function_start_time = time.time()
    log_process_commencing( str( 'add past & future price' ) )
    for share_code, share_data in share_dict.items():
        share_dict[share_code] = time_shifted_close ( share_data )
    log_dict_process_completed( share_dict, function_start_time )
    #------------------------------------------------------------- moving average for close
    function_start_time = time.time()
    log_process_commencing( str( 'add moving average to close value' ) )
    for share_code, share_data in share_dict.items():
        share_dict[share_code] = close_moving_average     ( share_data )
    log_dict_process_completed( share_dict, function_start_time )
    

    log_core_process_footer( core_process_name, core_process_start_time )
    return ( share_dict )   
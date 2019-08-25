# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# import pandas as pd
import time                             # for reporting how much time the functions take to finish
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from common                         import format_period, past_and_future_periods, moving_average_periods
from application_log                import log_core_process_header, log_core_process_footer
from application_log                import log_process_commencing,  log_dict_process_completed



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Worker Functions
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def time_shifted_close_price( share_data ):
    # past_and_future_periods = [ 1, 2, 3, 4, 5, 10 ]
    
    for period_no in past_and_future_periods:       
        formatted_period_no = format_period( period_no )

        new_past_vol_col    = str( 'past_close_' +  formatted_period_no )
        new_future_vol_col  = str( 'future_close_' +  formatted_period_no )

        share_data[ new_past_vol_col ]       = share_data['close'].shift( period_no )
        share_data[ new_future_vol_col ]     = share_data['close'].shift( period_no * -1 )

        share_data[ new_past_vol_col ].fillna  ( share_data['close'], inplace=True)
        share_data[ new_future_vol_col ].fillna( share_data['close'], inplace=True)
    return ( share_data )

def close_moving_average( share_data ):
    moving_average_periods = [ 8, 21 ]
    
    for period_no in moving_average_periods:
        formatted_period_no = format_period( period_no )

        new_moving_average_col    = str( 'close_ma_' +  formatted_period_no )

        share_data[ new_moving_average_col ] = share_data.close.rolling(period_no).mean() 

        share_data[ new_moving_average_col ].fillna  ( share_data['close'], inplace=True)
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
        share_dict[share_code] = time_shifted_close_price ( share_data )
    log_dict_process_completed( share_dict, function_start_time )
    #------------------------------------------------------------- moving average for close
    function_start_time = time.time()
    log_process_commencing( str( 'add moving average to close value' ) )
    for share_code, share_data in share_dict.items():
        share_dict[share_code] = close_moving_average     ( share_data )
    log_dict_process_completed( share_dict, function_start_time )
    

    log_core_process_footer( core_process_name, core_process_start_time )
    return ( share_dict )   
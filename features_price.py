# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# import pandas as pd
import time                             # for reporting how much time the functions take to finish
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from common                         import lookup_share_value, format_period
from application_log                import log_core_process_header, log_core_process_footer
from application_log                import log_process_commencing,  log_process_completed



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Worker Functions
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def time_shifted_price_values( share_df ):
    required_periods = [ 1, 2, 3, 4, 5, 10 ]
    
    for period_no in required_periods:
        function_start_time = time.time()
        formatted_period_no = format_period( period_no )

        new_past_vol_col    = str( 'past_close_' +  formatted_period_no )
        new_future_vol_col  = str( 'future_close_' +  formatted_period_no )

        log_process_commencing( str( 'adding closing price - past   - ' + formatted_period_no + ' day' ) )
        share_df[ new_past_vol_col ]    = share_df.apply(lambda row: lookup_share_value(row, share_df, ( period_no * -1 ), 'close'), axis=1 )
        log_process_completed( share_df, function_start_time )

        function_start_time = time.time()
        log_process_commencing( str( 'adding closing price - future - ' + formatted_period_no + ' day' ) )
        share_df[ new_future_vol_col ]  = share_df.apply(lambda row: lookup_share_value(row, share_df, period_no,          'close'), axis=1 )
        log_process_completed( share_df, function_start_time )
    
    return ( share_df )


    # share_df['past_close_01'] = share_df.apply(lambda row: lookup_share_value(row, share_df, -1, 'close'), axis=1 )
    # print ( 'added - past price - 1 day' ) 
    # share_df['past_close_02'] = share_df.apply(lambda row: lookup_share_value(row, share_df, -2, 'close'), axis=1 )
    # print ( 'added - past price - 2 days' ) 
    # share_df['past_close_03'] = share_df.apply(lambda row: lookup_share_value(row, share_df, -3, 'close'), axis=1 )
    # print ( 'added - past price - 3 days' ) 
    # share_df['past_close_04'] = share_df.apply(lambda row: lookup_share_value(row, share_df, -4, 'close'), axis=1 )
    # print ( 'added - past price - 4 days' ) 
    # share_df['past_close_05'] = share_df.apply(lambda row: lookup_share_value(row, share_df, -5, 'close'), axis=1 )
    # print ( 'added - past price - 5 days' ) 
    # share_df['past_close_10'] = share_df.apply(lambda row: lookup_share_value(row, share_df, -10, 'close'), axis=1 )
    # print ( 'added - past price - 10 days' ) 


    # share_df['futr_close_01'] = share_df.apply(lambda row: lookup_share_value(row, share_df, 1, 'close'), axis=1 )
    # print ( 'added - future price - 1 day' ) 
    # share_df['futr_close_02'] = share_df.apply(lambda row: lookup_share_value(row, share_df, 2, 'close'), axis=1 )
    # print ( 'added - future price - 2 days' ) 
    # share_df['futr_close_03'] = share_df.apply(lambda row: lookup_share_value(row, share_df, 3, 'close'), axis=1 )
    # print ( 'added - future price - 3 days' ) 
    # share_df['futr_close_04'] = share_df.apply(lambda row: lookup_share_value(row, share_df, 4, 'close'), axis=1 )
    # print ( 'added - future price - 4 days' ) 
    # share_df['futr_close_05'] = share_df.apply(lambda row: lookup_share_value(row, share_df, 5, 'close'), axis=1 )
    # print ( 'added - future price - 5 days' ) 
    # share_df['futr_close_10'] = share_df.apply(lambda row: lookup_share_value(row, share_df, 10, 'close'), axis=1 )
    # print ( 'added - future price - 10 days' ) 

    # print ( 'Completed - adding Past and Future Share Prices' )
    
    # return ( share_df )


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Manager Function
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def add_price_features( share_df ):
    core_process_name           = 'Add Share Price Features to OHLC Share data'
    core_process_start_time     = time.time()
    log_core_process_header     (  core_process_name )

    share_df = time_shifted_price_values( share_df )

    log_core_process_footer( core_process_name, core_process_start_time )
    return ( share_df )   
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import numpy as np
import time                         # for reporting how much time the functions take to finish
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from application_log                import log_core_process_header, log_core_process_footer
from application_log                import log_process_commencing,  log_df_process_completed
from common                         import close_column_name, past_and_future_periods, determine_column_name_close_future, determine_column_name_close_higher
from common                         import volume_average_per_minute_column_name, moving_average_periods, determine_column_name_volume_ma_higher, determine_column_name_volume_moving_average




# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Volume Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def volume_above_ma_per_minute( share_df ):
    function_start_time = time.time()
    log_process_commencing( str( 'determine if volume is above moving averages' )  )

    for period_no in moving_average_periods: 
        new_moving_average_col, new_moving_average_per_minute_col  = determine_column_name_volume_moving_average( period_no )
        # print ( new_moving_average_per_minute_col )
        volume_ma_higher_column_name = determine_column_name_volume_ma_higher( period_no )
        share_df[ volume_ma_higher_column_name ] = np.where( share_df[ volume_average_per_minute_column_name ] > share_df[ new_moving_average_per_minute_col ], 1, 0)   

    log_df_process_completed( share_df, function_start_time )       
    return ( share_df )

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Future Closing Price Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def close_higher_in_future( share_df ):
    function_start_time = time.time()
    log_process_commencing( str( 'determine if price is higher tomorrow' )  )

    for period_no in past_and_future_periods:       
        close_future_column     = determine_column_name_close_future( period_no )
        close_higher_column     = determine_column_name_close_higher( period_no )
        # close_higher_analysis   = 'y_' + close_higher_column
        share_df[ close_higher_column ] = np.where( share_df[ close_future_column ] > share_df[ close_column_name ], 1, 0)   
        # share_df[ close_higher_analysis ] = share_df[ close_higher_column ]

    log_df_process_completed( share_df, function_start_time )       
    return ( share_df )


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Results Analysis Manager
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def add_results_analysis_features( share_df ):
    core_process_name           = 'Add Analysis Features'
    core_process_start_time     = time.time()
    log_core_process_header     (  core_process_name )

    
    share_df            = close_higher_in_future( share_df )
    share_df            = volume_above_ma_per_minute( share_df )

    log_core_process_footer( core_process_name, core_process_start_time )
    return ( share_df )   


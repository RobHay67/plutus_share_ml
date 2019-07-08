# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import numpy as np
import time                         # for reporting how much time the functions take to finish
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from application_log                import log_core_process_header, log_core_process_footer
from application_log                import log_process_commencing,  log_process_completed

def add_week_day_and_month_no( share_df ):
    function_start_time = time.time()
    log_process_commencing( str( 'adding weekday and month number' )  )

    if 'trading_date' in share_df.columns:
        share_df['weekday_no'] = share_df['trading_date'].dt.dayofweek
        share_df['month_no'] = share_df['trading_date'].dt.month

        log_process_completed( share_df, function_start_time )

        return ( share_df )

    else: log_process_completed( share_df, time.time(), error_message='trading_date col missing from shares_df' ); return( share_df )

def add_day_of_the_week_features( share_df ):
    trading_day_dict = {
                        0 : 'mon',
                        1 : 'tue',
                        2 : 'wed',
                        3 : 'thur',
                        4 : 'fri',
                        5 : 'sat',
                        6 : 'sun',
                        } 

    for day_no, day_name in trading_day_dict.items():
        function_start_time = time.time()
        log_process_commencing( str( 'adding day name for ' + day_name )  )

        new_col_name = str( 'feat_date_is_' + day_name)
        if new_col_name in share_df.columns: share_df.drop( new_col_name, axis=1, inplace=True) 

        share_df[new_col_name]  = np.where( share_df.weekday_no == day_no, 1, 0)

        log_process_completed( share_df, function_start_time )

    # del share_df['weekday']
    return ( share_df )
    
def add_month_of_the_year_features( share_df ):
    month_no_dict =     {
                        1  : 'jan',
                        2  : 'feb',
                        3  : 'mar',
                        4  : 'apr',
                        5  : 'may',
                        6  : 'jun',
                        7  : 'jul',
                        8  : 'aug',
                        9  : 'sep',
                        10 : 'oct',
                        11 : 'nov',
                        12 : 'dec',
                        }

    for month_no, month_name in month_no_dict.items():
        function_start_time = time.time()
        log_process_commencing( str( 'adding month name for ' + month_name )  )

        new_col_name = str( 'feat_date_is_' + month_name )
        if new_col_name in share_df.columns: share_df.drop( new_col_name, axis=1, inplace=True) 
        
        share_df[ new_col_name ]  = np.where( share_df.month_no ==  month_no, 1, 0)

        log_process_completed( share_df, function_start_time ) 

    # del share_df['month']
    return ( share_df )
  
def add_date_features( share_df ):
    core_process_name           = 'Add Date Related Features'
    core_process_start_time     = time.time()
    log_core_process_header     (  core_process_name )

    share_df = add_week_day_and_month_no( share_df )

    share_df = add_day_of_the_week_features( share_df )
    share_df = add_month_of_the_year_features( share_df )

    print ( len(share_df.columns) )

    log_core_process_footer( core_process_name, core_process_start_time )
    return ( share_df )  









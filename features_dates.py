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

def add_week_day_and_month_no( share_data ):
    if 'trading_date' in share_data.columns:
        share_data['weekday_no'] = share_data['trading_date'].dt.dayofweek
        share_data['month_no'] = share_data['trading_date'].dt.month   
        return ( share_data )
    else: log_process_completed( share_data, time.time(), error_message='trading_date col missing from shares_df' ); return( share_data )

def add_day_of_the_week_features( share_data ):
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
        new_col_name = str( 'feat_date_is_' + day_name)
        if new_col_name in share_data.columns: share_data.drop( new_col_name, axis=1, inplace=True) 
        share_data[new_col_name]  = np.where( share_data.weekday_no == day_no, 1, 0)
    # del share_data['weekday']
    return ( share_data )
    
def add_month_of_the_year_features( share_data ):
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
        new_col_name = str( 'feat_date_is_' + month_name )
        if new_col_name in share_data.columns: share_data.drop( new_col_name, axis=1, inplace=True) 
        share_data[ new_col_name ]  = np.where( share_data.month_no ==  month_no, 1, 0)
    # del share_data['month']
    return ( share_data )
  
def add_date_features( share_dict ):
    core_process_name           = 'Add Date Related Features'
    core_process_start_time     = time.time()
    log_core_process_header     (  core_process_name )

    function_start_time = time.time()
    log_process_commencing( str( 'adding weekday and month number' )  )
    for share_code, share_data in share_dict.items():
        share_dict[share_code] = add_week_day_and_month_no      ( share_data )
    log_process_completed( share_data, function_start_time )

    function_start_time = time.time()
    log_process_commencing( str( 'adding day name' )  )
    for share_code, share_data in share_dict.items():
        share_dict[share_code] = add_day_of_the_week_features   ( share_data )
    log_process_completed( share_data, function_start_time )

    function_start_time = time.time()
    log_process_commencing( str( 'adding month name' )  )
    for share_code, share_data in share_dict.items():
        share_dict[share_code] = add_month_of_the_year_features ( share_data )
    log_process_completed( share_data, function_start_time ) 
        
        
    # share_data = add_day_of_the_week_features( share_data )
    # share_data = add_month_of_the_year_features( share_data )

    # print ( len(share_data.columns) )

    log_core_process_footer( core_process_name, core_process_start_time )
    return ( share_dict )  



# --------------------------------------------------------------------------------------------------------------------------------------------
# Add Date Related Features
# process                                                               progress       share codes    rows      columns   load time           
# --------------------------------------------------------------------------------------------------------------------------------------------
# adding weekday and month number                                       Completed      2              6209      12        seconds = 000.004
# adding day name for mon                                               Completed      2              6209      13        seconds = 000.003
# adding day name for tue                                               Completed      2              6209      14        seconds = 000.003
# adding day name for wed                                               Completed      2              6209      15        seconds = 000.002
# adding day name for thur                                              Completed      2              6209      16        seconds = 000.002
# adding day name for fri                                               Completed      2              6209      17        seconds = 000.002
# adding day name for sat                                               Completed      2              6209      18        seconds = 000.002
# adding day name for sun                                               Completed      2              6209      19        seconds = 000.004
# adding month name for jan                                             Completed      2              6209      20        seconds = 000.004





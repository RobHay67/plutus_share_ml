# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import time                             # for reporting how much time the functions take to finish

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from application_log                  import log_core_process_header, log_core_process_footer
from application_log                  import log_process_commencing, log_dict_process_completed, log_df_process_completed



past_and_future_periods = [ 1, 2, 3, 4, 5, 10 ]
moving_average_periods  = [ 8, 21 ]



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Common Functions
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def format_period( period_no ):
    str_period_no = str( period_no )
    if len( str_period_no ) == 1:
        formatted_period = str( '0' + str_period_no )
    else:
        formatted_period = str( period_no )
    return ( formatted_period )

def format_currency_total( value ):
    formated_currency_value = str( '$ {:,}'.format(round( value, 2)) )
    return ( formated_currency_value )

def col_name_volume_past( period_no ):
    formatted_period_no = format_period( period_no )
    new_past_vol_col    = str( 'volume_' +  formatted_period_no + '_days_ago' )
    return( new_past_vol_col )

def col_name_volume_future( period_no ):
    formatted_period_no = format_period( period_no )
    new_future_vol_col  = str( 'volume_' +  formatted_period_no + '_days_in_future')
    return( new_future_vol_col )


def col_name_moving_average( period_no ):
    formatted_period_no = format_period( period_no )
    mov_avg = str( 'volume_ma_' +  formatted_period_no )
    ma_per_minute = mov_avg + '_per_minute'
    return( mov_avg, ma_per_minute )




# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Manager - Convert Dataframe to a Dictionary by share_code
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def create_share_dict( share_df ):
    function_start_time = time.time()
    log_process_commencing( str( 'seperate share codes into a dictionary')  )   

    share_dict = dict( tuple( share_df.groupby( 'share_code' ) ) )
   
    log_dict_process_completed( share_dict, function_start_time )
    return ( share_dict )

def convert_dict_into_single_df( share_dict ):
    core_process_name           = 'Create Single Dataframe (extract dictionary)'
    core_process_start_time     = time.time()
    log_core_process_header     (  core_process_name )

    function_start_time = time.time()
    log_process_commencing( str( 'combine share codes into single dataframe')  )   

    share_df = pd.concat(share_dict.values(), ignore_index=True)

    log_df_process_completed( share_df, function_start_time )

    log_core_process_footer( core_process_name, core_process_start_time )
    return ( share_df )




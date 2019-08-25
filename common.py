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
    past_volume_column    = str( 'volume_' +  formatted_period_no + '_days_ago' )
    return( past_volume_column )

def col_name_volume_future( period_no ):
    formatted_period_no = format_period( period_no )
    future_volume_column  = str( 'volume_' +  formatted_period_no + '_days_in_future')
    return( future_volume_column )


def col_name_volume_moving_average( period_no ):
    formatted_period_no = format_period( period_no )
    volume_moving_average_column     = str( 'volume_ma_' +  formatted_period_no )
    moving_average_per_minute_column = volume_moving_average_column + '_per_minute'
    return( volume_moving_average_column, moving_average_per_minute_column )

def col_name_close_moving_average( period_no ):
    formatted_period_no = format_period( period_no )
    close_moving_average_column = str( 'close_ma_' +  formatted_period_no )
    return( close_moving_average_column )

def col_name_close_past( period_no ):
    formatted_period_no = format_period( period_no )
    past_volumn_column    = str( 'close_' +  formatted_period_no + '_days_ago' )
    return( past_volumn_column )

def col_name_close_future( period_no ):
    formatted_period_no = format_period( period_no )
    future_volumn_column  = str( 'close_' +  formatted_period_no + '_days_in_future')
    return( future_volumn_column )

def col_name_price_higher( period_no ):
    formatted_period_no = format_period( period_no )
    future_close_higher_column = str( 'Y_close_' + formatted_period_no + '_days')
    return( future_close_higher_column )


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




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
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Module Values
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
past_and_future_periods                 = [ 1, 2, 3, 4, 5, 10 ]
moving_average_periods                  = [ 1, 2, 3, 5, 8, 13, 21, 34 ]
closing_price_column_name               = 'close'
volume_column_name                      = 'volume'
average_volume_per_minute_column_name   = 'volume_average_per_minute'
minutes_per_day                         = 360                                 # Opening time = 10am and closing time = 4pm. Total minutes = 6 * 60 = 360 minutes

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

def sort_df_into_alphabetical_order( share_df ):
    column_list = list(share_df.columns.values)      # Order columns alpabethically for easy comparison of missing columns
    column_list.sort()
    share_df = share_df[column_list]  
    return( share_df )       

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Column Naming Functions
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def column_name_volume_past( period_no ):
    formatted_period_no = format_period( period_no )
    column_name         = str( 'volume_-_' +  formatted_period_no + '_day' )
    return( column_name )

def column_name_volume_future( period_no ):
    formatted_period_no = format_period( period_no )
    column_name         = str( 'volume_+_' +  formatted_period_no + '_day')
    return( column_name )


def column_name_volume_moving_average( period_no ):
    formatted_period_no = format_period( period_no )
    column_name         = str( 'volume_ma_' +  formatted_period_no )
    column_name_per_min = column_name + '_per_min'
    return( column_name, column_name_per_min )

def column_name_volume_ma_higher( period_no ):
    formatted_period_no = format_period( period_no )
    column_name         = str( 'volume_ma_up_' + formatted_period_no + '_per_min')
    return( column_name )





def column_name_close_past( period_no ):
    formatted_period_no = format_period( period_no )
    column_name         = str( 'close_-_' +  formatted_period_no + '_day' )
    return( column_name )

def column_name_close_future( period_no ):
    formatted_period_no = format_period( period_no )
    column_name         = str( 'close_+_' +  formatted_period_no + '_day')
    return( column_name )

def column_name_close_moving_average( period_no ):
    formatted_period_no = format_period( period_no )
    column_name         = str( 'close_ma_' +  formatted_period_no )
    return( column_name )

def column_name_price_higher( period_no ):
    formatted_period_no = format_period( period_no )
    column_name         = str( 'y_close_up_in_' + formatted_period_no + '_days')
    return( column_name )


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




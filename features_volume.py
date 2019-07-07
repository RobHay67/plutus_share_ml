
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# import pandas as pd
# import numpy as np
import time                             # for reporting how much time the functions take to finish
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from common                     import check_dataframe_if_these_cols_exist, lookup_share_value
from application_log            import print_seperator, log_process_commencing, log_process_completed
# import app

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Helper Functions
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def format_period( period_no ):
    str_period_no = str( period_no )
    if len( str_period_no ) == 1:
        formatted_period = str( '0' + str_period_no )
    else:
        formatted_period = str( period_no )
    return ( formatted_period )



def add_average_volume( share_df ):
    required_columns_list = [ 'volume' ]

    if check_dataframe_if_these_cols_exist( share_df, required_columns_list, 'share dataframe' ) != 'FAILED':
        new_features_being_added = [ 'volume_average' ]     

        if new_features_being_added[0] in share_df.columns: 
            share_df.drop( new_features_being_added, axis=1, inplace=True) 

        # Opening time = 10am and closing time = 4pm. Total minutes = 6 * 60 = 360 minutes
        share_df['volume_average_per_minute']    = share_df['volume'] / 360

        print ( 'Completed - adding average volume to share dataframe')
        return ( share_df )

def volume_values( share_df ):
    # app.print_seperator('key')
    print ( 'Commenced - adding Past and Future Volume Changes' )
    # app.print_seperator('single')

    required_periods = [ 1, 2, 3, 4, 5, 10 ]

    for period_no in required_periods:
        function_start_time = time.time()
        formatted_period_no = format_period( period_no )

        new_past_vol_col    = str( 'past_vol_' +  formatted_period_no )
        new_future_vol_col  = str( 'future_vol_' +  formatted_period_no )

        sub_process = str( 'added - past volume - ' + formatted_period_no + ' day' ) 
        log_process_commencing( sub_process )
        share_df[ new_past_vol_col ]    = share_df.apply(lambda row: lookup_share_value(row, share_df, ( period_no * -1 ), 'volume_average_per_minute'), axis=1 )
        log_process_completed( len(share_df), len(share_df.columns), function_start_time )

        sub_process = str( 'added - future volume - ' + formatted_period_no + ' day' ) 
        share_df[ new_future_vol_col ]  = share_df.apply(lambda row: lookup_share_value(row, share_df, period_no, 'volume_average_per_minute'), axis=1 )
        



    # share_df['past_vol_01'] = share_df.apply(lambda row: lookup_share_value(row, share_df, -1, 'volume_average_per_minute'), axis=1 )
    # print ( 'added - past volume - 1 day' ) 
    # share_df['past_vol_02'] = share_df.apply(lambda row: lookup_share_value(row, share_df, -2, 'volume_average_per_minute'), axis=1 )
    # print ( 'added - past volume - 2 day' ) 
    # share_df['past_vol_03'] = share_df.apply(lambda row: lookup_share_value(row, share_df, -3, 'volume_average_per_minute'), axis=1 )
    # print ( 'added - past volume - 3 day' ) 
    # share_df['past_vol_04'] = share_df.apply(lambda row: lookup_share_value(row, share_df, -4, 'volume_average_per_minute'), axis=1 )
    # print ( 'added - past volume - 4 day' ) 
    # share_df['past_vol_05'] = share_df.apply(lambda row: lookup_share_value(row, share_df, -5, 'volume_average_per_minute'), axis=1 )
    # print ( 'added - past volume - 5 day' ) 
    # share_df['past_vol_10'] = share_df.apply(lambda row: lookup_share_value(row, share_df, -10, 'volume_average_per_minute'), axis=1 )
    # print ( 'added - past volume - 10 day' ) 

    # share_df['futr_vol_01'] = share_df.apply(lambda row: lookup_share_value(row, share_df, 1, 'volume_average_per_minute'), axis=1 )
    # print ( 'added - future volume - 1 day' ) 
    # share_df['futr_vol_02'] = share_df.apply(lambda row: lookup_share_value(row, share_df, 2, 'volume_average_per_minute'), axis=1 )
    # print ( 'added - future volume - 2 day' ) 
    # share_df['futr_vol_03'] = share_df.apply(lambda row: lookup_share_value(row, share_df, 3, 'volume_average_per_minute'), axis=1 )
    # print ( 'added - future volume - 3 day' ) 
    # share_df['futr_vol_04'] = share_df.apply(lambda row: lookup_share_value(row, share_df, 4, 'volume_average_per_minute'), axis=1 )
    # print ( 'added - future volume - 4 day' ) 
    # share_df['futr_vol_05'] = share_df.apply(lambda row: lookup_share_value(row, share_df, 5, 'volume_average_per_minute'), axis=1 )
    # print ( 'added - future volume - 5 day' ) 
    # share_df['futr_vol_10'] = share_df.apply(lambda row: lookup_share_value(row, share_df, 10, 'volume_average_per_minute'), axis=1 )
    # print ( 'added - future volume - 10 day' ) 


    print ( 'Completed - adding Past and Future Volume Changes' )
    print_seperator('single')
    
    return ( share_df )





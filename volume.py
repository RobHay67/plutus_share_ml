import pandas as pd
import numpy as np

import app



def add_average_volume( share_df ):
    required_columns_list = [ 'volume' ]

    if app.check_dataframe_if_these_cols_exist( share_df, required_columns_list, 'share dataframe' ) != 'FAILED':
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

    share_df['past_vol_01'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, -1, 'volume_average_per_minute'), axis=1 )
    print ( 'added - past volume - 1 day' ) 
    share_df['past_vol_02'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, -2, 'volume_average_per_minute'), axis=1 )
    print ( 'added - past volume - 2 day' ) 
    share_df['past_vol_03'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, -3, 'volume_average_per_minute'), axis=1 )
    print ( 'added - past volume - 3 day' ) 
    share_df['past_vol_04'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, -4, 'volume_average_per_minute'), axis=1 )
    print ( 'added - past volume - 4 day' ) 
    share_df['past_vol_05'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, -5, 'volume_average_per_minute'), axis=1 )
    print ( 'added - past volume - 5 day' ) 
    share_df['past_vol_10'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, -10, 'volume_average_per_minute'), axis=1 )
    print ( 'added - past volume - 10 day' ) 

    share_df['futr_vol_01'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, 1, 'volume_average_per_minute'), axis=1 )
    print ( 'added - future volume - 1 day' ) 
    share_df['futr_vol_02'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, 2, 'volume_average_per_minute'), axis=1 )
    print ( 'added - future volume - 2 day' ) 
    share_df['futr_vol_03'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, 3, 'volume_average_per_minute'), axis=1 )
    print ( 'added - future volume - 3 day' ) 
    share_df['futr_vol_04'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, 4, 'volume_average_per_minute'), axis=1 )
    print ( 'added - future volume - 4 day' ) 
    share_df['futr_vol_05'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, 5, 'volume_average_per_minute'), axis=1 )
    print ( 'added - future volume - 5 day' ) 
    share_df['futr_vol_10'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, 10, 'volume_average_per_minute'), axis=1 )
    print ( 'added - future volume - 10 day' ) 


    print ( 'Completed - adding Past and Future Volume Changes' )
    app.print_seperator('single')
    
    return ( share_df )





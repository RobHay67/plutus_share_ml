import pandas as pd
import numpy as np

import app



def price_values( share_df ):
    # app.print_seperator('key')
    print ( 'Commenced - adding Past and Future Share Prices' )
    # app.print_seperator('single')


    share_df['past_close_01'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, -1, 'close'), axis=1 )
    print ( 'added - past price - 1 day' ) 
    share_df['past_close_02'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, -2, 'close'), axis=1 )
    print ( 'added - past price - 2 days' ) 
    share_df['past_close_03'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, -3, 'close'), axis=1 )
    print ( 'added - past price - 3 days' ) 
    share_df['past_close_04'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, -4, 'close'), axis=1 )
    print ( 'added - past price - 4 days' ) 
    share_df['past_close_05'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, -5, 'close'), axis=1 )
    print ( 'added - past price - 5 days' ) 
    share_df['past_close_10'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, -10, 'close'), axis=1 )
    print ( 'added - past price - 10 days' ) 


    share_df['futr_close_01'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, 1, 'close'), axis=1 )
    print ( 'added - future price - 1 day' ) 
    share_df['futr_close_02'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, 2, 'close'), axis=1 )
    print ( 'added - future price - 2 days' ) 
    share_df['futr_close_03'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, 3, 'close'), axis=1 )
    print ( 'added - future price - 3 days' ) 
    share_df['futr_close_04'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, 4, 'close'), axis=1 )
    print ( 'added - future price - 4 days' ) 
    share_df['futr_close_05'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, 5, 'close'), axis=1 )
    print ( 'added - future price - 5 days' ) 
    share_df['futr_close_10'] = share_df.apply(lambda row: app.lookup_share_value(row, share_df, 10, 'close'), axis=1 )
    print ( 'added - future price - 10 days' ) 

    # app.print_seperator('single')
    print ( 'Completed - adding Past and Future Share Prices' )
    # app.print_seperator('key')
    
    return ( share_df )



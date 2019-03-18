import pandas as pd
import numpy as np

import app

def lookup_share_price ( row, share_df, no_of_days, search_direction ):
    share_code      = row.name[0]
    current_period  = row.name[1]
    minimum_period  = row['counter_min']
    maximum_period  = row['counter_max']

    if search_direction == 'past':
        period_to_find = current_period - no_of_days
        if period_to_find < minimum_period: period_to_find = minimum_period
        if period_to_find > maximum_period: period_to_find = maximum_period
        return ( share_df.loc[ ( share_code, period_to_find ), ['close'] ] )
    elif search_direction == 'futr':
        period_to_find = current_period + no_of_days
        if period_to_find < minimum_period: period_to_find = minimum_period
        if period_to_find > maximum_period: period_to_find = maximum_period
        return ( share_df.loc[ ( share_code, period_to_find ), ['close'] ] )
    else:
        return ( 0 )



def past_share_prices( share_df ):
    app.print_seperator('key')
    print ( 'Commenced - adding Past and Future Share Prices' )
    share_df['past_01'] = share_df.apply(lambda row: lookup_share_price(row, share_df, 1, 'past'), axis=1 )
    print ( 'added - past price - 1 day' ) 
    share_df['past_02'] = share_df.apply(lambda row: lookup_share_price(row, share_df, 2, 'past'), axis=1 )
    print ( 'added - past price - 2 days' ) 
    share_df['past_03'] = share_df.apply(lambda row: lookup_share_price(row, share_df, 3, 'past'), axis=1 )
    print ( 'added - past price - 3 days' ) 
    share_df['past_04'] = share_df.apply(lambda row: lookup_share_price(row, share_df, 4, 'past'), axis=1 )
    print ( 'added - past price - 4 days' ) 
    share_df['past_05'] = share_df.apply(lambda row: lookup_share_price(row, share_df, 5, 'past'), axis=1 )
    print ( 'added - past price - 5 days' ) 
    share_df['past_10'] = share_df.apply(lambda row: lookup_share_price(row, share_df, 10, 'past'), axis=1 )
    print ( 'added - past price - 10 days' ) 
    share_df['futr_01'] = share_df.apply(lambda row: lookup_share_price(row, share_df, 1, 'futr'), axis=1 )
    print ( 'added - future price - 1 day' ) 
    share_df['futr_02'] = share_df.apply(lambda row: lookup_share_price(row, share_df, 2, 'futr'), axis=1 )
    print ( 'added - future price - 2 days' ) 
    share_df['futr_03'] = share_df.apply(lambda row: lookup_share_price(row, share_df, 3, 'futr'), axis=1 )
    print ( 'added - future price - 3 days' ) 
    share_df['futr_04'] = share_df.apply(lambda row: lookup_share_price(row, share_df, 4, 'futr'), axis=1 )
    print ( 'added - future price - 4 days' ) 
    share_df['futr_05'] = share_df.apply(lambda row: lookup_share_price(row, share_df, 5, 'futr'), axis=1 )
    print ( 'added - future price - 5 days' ) 
    share_df['futr_10'] = share_df.apply(lambda row: lookup_share_price(row, share_df, 10, 'futr'), axis=1 )
    print ( 'added - future price - 10 days' ) 
    print ( 'Completed - loading OHLC Share data' )
    app.print_seperator('key')
    
    return ( share_df )



import pandas as pd
import numpy as np
import pathlib



ohlc_share_df_folder = pathlib.Path.home().joinpath('shares', 'ohlc', )
ohlc_share_df_filename = pathlib.Path.joinpath(ohlc_share_df_folder, 'ohlc_shares.csv' )

share_df_dict = { 'share_code':'object',
                    'date':'object', 
                    'open':'float64',
                    'high':'float64', 
                    'low':'float64', 
                    'close':'float64', 
                    'volume':'float64'              }


def print_seperator( seperator_type ):
    if seperator_type=='key':
        print ( '=' * 120 )
    elif seperator_type == 'single':
        print ( '-' * 120 )
    else:
        print ( '*' * 120 )


def list_of_share_codes(share_df):
    return ( share_df.share_code.unique().tolist() )


def load_OHLC_share_df():
    print_seperator('key')   
    print ( 'commencing loading of OHLC Share data' )
    print_seperator('single')
    share_df = pd.read_csv( ohlc_share_df_filename, dtype=share_df_dict, parse_dates=['trading_date'] )
    # Ensure the columns are in the order you want

    print ( 'first date        in the share file = ', share_df.trading_date.min() )
    print ( 'last  date        in the share file = ', share_df.trading_date.max() )
    print ( 'total records     in share file     = ', len(share_df) )
    print ( 'total no of codes in share file     = ', len( list_of_share_codes( share_df) ) )
    print_seperator('single')
    print ( 'Completed - loading OHLC Share data' )
    print_seperator('key')
    return ( share_df )   

def save_OHLC_share_df( share_df) :
    print_seperator('key')   
    print ( 'commencing save of OHLC Share data' )
    share_df.reset_index(inplace=True)
    share_df.to_csv(ohlc_share_df_filename, index=False)
    print ( 'Completed - saving OHLC Share data' )
    print_seperator('key')   



# Functions



def check_dataframe_if_these_cols_exist(dataframe, column_list, dataframe_name):
    for column in column_list:
        if column not in dataframe.columns:
            print ( 'FAILED <', column, '> missing from', dataframe_name )
            return ( 'FAILED' )
        # else:
        #     print ( 'found ', column)

def add_sequential_counter( share_df ):
    required_columns_list = [   'share_code', 'trading_date' ]

    if check_dataframe_if_these_cols_exist( share_df, required_columns_list, 'share dataframe' ) != 'FAILED':
        new_features_being_added = [ 'counter', 'counter_min','counter_max' ]     

        if new_features_being_added[0] in share_df.columns: 
            share_df.drop( new_features_being_added, axis=1, inplace=True) 

        share_df.sort_values(['trading_date', 'share_code'], ascending=True, inplace=True)
        share_df['counter']    = share_df.groupby(['share_code']).cumcount()+1
        share_df['counter_min'] = share_df.groupby('share_code')['counter'].transform('min')
        share_df['counter_max'] = share_df.groupby('share_code')['counter'].transform('max')
        # share_df['index_counter'] = share_df['counter']
        share_df = share_df.set_index(['share_code','counter'])
        print ( 'Completed - adding counter to share dataframe')
        return ( share_df )
    else:
        return ( share_df )



def lookup_share_value ( row, share_df, no_of_days, value_column ):
    share_code      = row.name[0]
    current_period  = row.name[1]
    minimum_period  = row['counter_min']
    maximum_period  = row['counter_max']
    current_value   = row[value_column]


    period_to_find = current_period + no_of_days

    if period_to_find < minimum_period: period_to_find = minimum_period
    if period_to_find > maximum_period: period_to_find = maximum_period

    lookup_value      = share_df.loc[ ( share_code, period_to_find ), [ value_column ] ]
    
    if no_of_days < 0:
        percentage_change =  ( current_value - lookup_value ) / lookup_value
    else :
        percentage_change =  ( lookup_value - current_value ) / current_value

    return ( percentage_change )



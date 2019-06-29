# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
# import numpy as np
import pathlib                      # for handling local dorectories

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from application_log                import print_seperator
from common                         import check_dataframe_if_these_cols_exist, lookup_share_value



ohlc_share_df_folder    = pathlib.Path.home().joinpath('shares', 'ohlc', )
ohlc_share_df_filename  = pathlib.Path.joinpath(ohlc_share_df_folder, 'ohlc_shares.csv' )

share_df_dict =     {
                    'share_code'    :'object',
                    'date'          :'object', 
                    'open'          :'float64',
                    'high'          :'float64', 
                    'low'           :'float64', 
                    'close'         :'float64', 
                    'volume'        :'float64'              
                    }


def load_OHLC_share_df():
    print_seperator('key')   
    print ( 'commencing loading of OHLC Share data' )
    print_seperator('single')

    share_df = pd.read_csv( ohlc_share_df_filename, dtype=share_df_dict, parse_dates=['trading_date'] )
    
    # Ensure the columns are in the order you want

    print ( 'first date        in share file = ', share_df.trading_date.min() )
    print ( 'last  date        in share file = ', share_df.trading_date.max() )
    print ( 'total records     in share file = ', len(share_df) )
    print ( 'total no of codes in share file = ', len( list_of_share_codes( share_df) ) )
    
    print_seperator( 'single' )
    print ( 'Completed - loading OHLC Share data' )
    print_seperator( 'key' )
    
    return ( share_df )   




def save_OHLC_share_df( share_df) :
    print_seperator( 'key' )   
    print ( 'commencing save of OHLC Share data' )

    share_df.reset_index(inplace=True)
    share_df.to_csv(ohlc_share_df_filename, index=False)

    print ( 'Completed - saving OHLC Share data' )
    print_seperator( 'key' )   



def list_of_share_codes(share_df):
    return ( share_df.share_code.unique().tolist() )

def add_sequential_counter( share_df ):
    required_columns_list = [  'share_code', 'trading_date' ]

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
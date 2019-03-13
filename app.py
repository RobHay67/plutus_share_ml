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


def load_OHLC_share_df():
    print_seperator('key')   
    print ( 'commencing loading of OHLC Share data' )
    share_df = pd.read_csv( ohlc_share_df_filename, dtype=share_df_dict, parse_dates=['trading_date'] )

    print ( 'first date in the share file = ', share_df.trading_date.min() )
    print ( 'last  date in the share file = ', share_df.trading_date.max() )
    print ( 'total records  in share file = ', len(share_df) )
    print ( 'Completed - loading OHLC Share data' )
    print_seperator('key')
    return ( share_df )   
    # share_df.trading_date.max()
    # len(share_df)

def save_OHLC_share_df( share_df) :
    print_seperator('key')   
    print ( 'commencing save of OHLC Share data' )
    share_df.to_csv(ohlc_share_df_filename, index=False)
    print ( 'Completed - saving OHLC Share data' )
    print_seperator('key')   

def list_of_share_codes(share_df):
    return ( share_df.share_code.tolist() )


# Functions

def add_sequential_counter( share_df ):
    share_df.sort_values(['trading_date', 'share_code'], ascending=True, inplace=True)
    share_df['counter'] = share_df.groupby(['share_code']).cumcount()+1
    print ( 'Completed - adding counter to share daatframe')
    return ( share_df )



def check_dataframe_if_these_cols_exist(dataframe, column_list, dataframe_name):
    for column in column_list:
        if column not in dataframe.columns:
            print ( 'FAILED <', column, '> missing from', dataframe_name )
            return ( 'FAILED' )
        # else:
        #     print ( 'found ', column)




def add_day_of_the_week_features( share_df ):
    required_columns_list = [   'trading_date' ]

    if check_dataframe_if_these_cols_exist( share_df, required_columns_list, 'share dataframe' ) != 'FAILED':
        new_features_being_added = ['feat_date_is_mon',
                                    'feat_date_is_tue',
                                    'feat_date_is_wed',
                                    'feat_date_is_thur',
                                    'feat_date_is_fri',
                                    'feat_date_is_sat',
                                    'feat_date_is_sun'  ]     

        if new_features_being_added[0] in share_df.columns: 
            share_df.drop( new_features_being_added, axis=1, inplace=True) 

        share_df['weekday'] = share_df['trading_date'].dt.dayofweek

        share_df['feat_date_is_mon']  = np.where( share_df.weekday == 0, 1, 0)
        share_df['feat_date_is_tue']  = np.where( share_df.weekday == 1, 1, 0)
        share_df['feat_date_is_wed']  = np.where( share_df.weekday == 2, 1, 0)
        share_df['feat_date_is_thur'] = np.where( share_df.weekday == 3, 1, 0)
        share_df['feat_date_is_fri']  = np.where( share_df.weekday == 4, 1, 0)
        share_df['feat_date_is_sat']  = np.where( share_df.weekday == 5, 1, 0)
        share_df['feat_date_is_sun']  = np.where( share_df.weekday == 6, 1, 0)

        del share_df['weekday']

        print ( 'Completed - adding day of the week features')
        return ( share_df )
    else:
        return ( share_df )












# def price_categorisation():
#     print ('this')
#     # do some cool stuff here


# def volume_categorisation():
#     # do some cool stuff here








    

    
    
# def share_code_list(share_df):
#     return ( share_df.share_code.tolist() )
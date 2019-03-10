# Functions


def check_dataframe_if_these_cols_exist():
    # receive a dataframe
    # receive a col list
    # return the dataframe or an error which the sender will need to evaluate


def price_categorisation():
    # do some cool stuff here


def volume_categorisation():
    # do some cool stuff here







def save_df():
    print ( 'commencing save of primary dataframe' )
    share_df.to_csv('shares/share_df.csv', index=False)
    print ( 'finished saving primary dataframe' )
    
def load_df():
    print ( 'commencing loading of primary dataframe' )
    total_share_df_filename = pathlib.Path.home().joinpath('git_repo', 'Plutus_share_analyser', 'shares', 'share_df.csv' )
    share_df = pd.read_csv( total_share_df_filename, dtype=share_data_dict, parse_dates=['trading_date'] )
    print ( 'first date in the share file = ', share_df.trading_date.min() )
    print ( 'last  date in the share file = ', share_df.trading_date.max() )
    print ( 'total records  in share file = ', len(share_df) )
    print ( '=' * 100)
    print ( 'finished loading primary dataframes' )
    return ( share_df )   
    # share_df.trading_date.max()
    # len(share_df)
    
    
def share_code_list(share_df):
    return ( share_df.share_code.tolist() )
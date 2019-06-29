# import pandas as pd
import numpy as np
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from common                     import check_dataframe_if_these_cols_exist



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


def add_month_of_the_year_features( share_df ):
    required_columns_list = [   'trading_date' ]

    if check_dataframe_if_these_cols_exist( share_df, required_columns_list, 'share dataframe' ) != 'FAILED':
        new_features_being_added = ['feat_date_is_jan',
                                    'feat_date_is_feb',
                                    'feat_date_is_mar',
                                    'feat_date_is_apr',
                                    'feat_date_is_may',
                                    'feat_date_is_jun',
                                    'feat_date_is_jul',
                                    'feat_date_is_aug',
                                    'feat_date_is_sep',
                                    'feat_date_is_oct',
                                    'feat_date_is_nov',
                                    'feat_date_is_dec'  ]     

        if new_features_being_added[0] in share_df.columns: 
            share_df.drop( new_features_being_added, axis=1, inplace=True) 

        share_df['month'] = share_df['trading_date'].dt.month

        share_df['feat_date_is_jan']  = np.where( share_df.month ==  1, 1, 0)
        share_df['feat_date_is_feb']  = np.where( share_df.month ==  2, 1, 0)
        share_df['feat_date_is_mar']  = np.where( share_df.month ==  3, 1, 0)
        share_df['feat_date_is_apr']  = np.where( share_df.month ==  4, 1, 0)
        share_df['feat_date_is_may']  = np.where( share_df.month ==  5, 1, 0)
        share_df['feat_date_is_jun']  = np.where( share_df.month ==  6, 1, 0)
        share_df['feat_date_is_jul']  = np.where( share_df.month ==  7, 1, 0)
        share_df['feat_date_is_aug']  = np.where( share_df.month ==  8, 1, 0)
        share_df['feat_date_is_sep']  = np.where( share_df.month ==  9, 1, 0)
        share_df['feat_date_is_oct']  = np.where( share_df.month == 10, 1, 0)
        share_df['feat_date_is_nov']  = np.where( share_df.month == 11, 1, 0)
        share_df['feat_date_is_dec']  = np.where( share_df.month == 12, 1, 0)
   

        del share_df['month']

        print ( 'Completed - adding month of the year features')
        return ( share_df )
    else:
        return ( share_df )









# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd



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

def check_dataframe_if_these_cols_exist(dataframe, column_list, dataframe_name):
    for column in column_list:
        if column not in dataframe.columns:
            print ( 'FAILED <', column, '> missing from', dataframe_name )
            return ( 'FAILED' )
        # else:
        #     print ( 'found ', column)





# def lookup_share_value ( row, share_df, no_of_days, value_column ):
#     share_code      = row.name[0]
#     current_period  = row.name[1]
#     minimum_period  = row['counter_min']
#     maximum_period  = row['counter_max']
#     current_value   = row[value_column]


#     period_to_find = current_period + no_of_days

#     if period_to_find < minimum_period: period_to_find = minimum_period
#     if period_to_find > maximum_period: period_to_find = maximum_period

#     lookup_value      = share_df.loc[ ( share_code, period_to_find ), [ value_column ] ]
    
#     if no_of_days < 0:
#         percentage_change =  ( current_value - lookup_value ) / lookup_value
#     else :
#         percentage_change =  ( lookup_value - current_value ) / current_value

#     return ( percentage_change )
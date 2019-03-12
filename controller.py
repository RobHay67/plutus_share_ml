import pandas as pd

import app



# ----------------------------------------------- load the OHLC share data from Disk
share_df = app.load_OHLC_share_df()

# list_of_share_codes = app.list_of_share_codes( share_df )




share_df = app.add_day_of_the_week_features( share_df )




# ----------------------------------------------- Save the OHLC Share Dataframe to Disk
# app.save_OHLC_share_df( share_df )


# print ( share_df.feat_date_is_mon.value_counts() )
print ( share_df.sample(4) )

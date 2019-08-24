# This is going to be python code

# general process - load up the OHLC dataset and add features to IT

# Definition of features.........

# todo ==================================================================================================
# ENHANCEMENTS
#  Calculation Methodology
    # its going to take a long time to work out the chages for all the historical data
    # we need a method to only work on certain periods or where we have added  new price value of feature
# DONE Consider changing the way the previous price is looked up - might be able to do it by shifting a col of the dataframe - could be quicker

# DONE ==================================================================================================
#  Period Identifyer
    # DONE - period_no          - Need to generate a sequential period number
    # We may need a date filler routine as well? not sure about This - maybe we could just find missing dates and make sure this makes sense

# todo ==================================================================================================
# Basic Share Master Data and Info - need to source this from somewhere
    # todo  - Industry
    # todo  - Dividend_Cum_Date
    # todo  - Dividend_annoncement_Date
    # todo  - Dividend_amount
    # todo  - Dividend_yield
    # todo  - Franking Credits amount and is it even offered

# WIP ==================================================================================================
# Date Related features
    # DONE  - _is_mon               - day of the week
    # DONE  - _is_jan               - which month
    # todo  - _is_pub_holiday       - Public holidays
    #       - _pub_hol_yesterday    - was a public holiday yesterday
    #       - _pub_hol_tomorrow     - public holiday scheduled for tomorrow



# WIP ==================================================================================================
#  Price Direction Indicators
    # todo PREFIX = feature_price_
    # DONE - _up_for_n_days     - Price going up (and then how many days - ie last2, 3, 4, 5 days etc)
    # DONE - _down_for_n_days   - price going down
    # DONE - _same_for_n_days   - Price has not changed
    # todo - _up_gap            - gap between prior close and current open  (extend this for n days (up to 10))
    # todo - _down_gap          - gap between prior close and current open  (extend this for n days (up to 10))
    #                           - Use % size of the gap for relativity
    # DONE Differential from yesterday (historical)
    # DONE Differential from 2 days ago (historical)
    # DONE Price in 1 to 10 days time
    # DONE price in 30 days time 
    # DONE perhaps these should be represented as a percentage and then categorised accordingly

# WIP ==================================================================================================
# Volume Indicators
    # DONE Averge Vol today
    # DONE Averge Vol yesterday
    # DONE Avg Vol for last 2 days, last 5 days, last 10 days etc
    # DONE Vol into the future by an appropriate amount 1 day, 2 days, 5, 10 ,30 days
    # Is the above just the moving average - 
    # < check how the MACD works to smooth out the averages > migth be over sampling here?

# todo ==================================================================================================
# EXTERNAL INFORMATION
    # Interest Rates
    # Bond Rates
    # Gold Price
    # Key Commodity Prices
    #     Gold
    #     Coppers
    #     rare earths
    #     Iron...
    #     Average Labour Rates
    # Company tax rates (average)
    # Job Advertisments (ANZ)
    # Unemployment Rate
    # GDP









# This is going to be python code

# general process - load up the OHLC dataset and add features to IT

# Definition of features.........

# ==================================================================================================
# Period Identifyer
    # todo - period_no          - Need to generate a sequential period number
    # We may need a date filler routine as well? not sure about This - maybe we could just find missing dates and make sure this makes sense

# ==================================================================================================
# Basic Share Master Data and Info - need to source this from somewhere
    # Industry
    # Dividend_Cum_Date
    # Dividend_annoncement_Date
    # Dividend_amount
    # Dividend_yield
    # Franking Credits amount and is it even offered

# ==================================================================================================
# Date Related features
# PREFIX = feature_date_
    # DONE  - _is_mon               - day of the week
    # todo  - _is_jan               - which month
    # todo  - _is_pub_holiday       - Public holidays
    #       - _pub_hol_yesterday    - was a public holiday yesterday
    #       - _pub_hol_tomorrow     - public holiday scheduled for tomorrow



# ==================================================================================================
# Price Direction Indicators
# PREFIX = feature_price_
    # todo - _up_for_n_days     - Price going up (and then how many days - ie last2, 3, 4, 5 days etc)
    # todo - _down_for_n_days   - price going down
    # todo - _same_for_n_days   - Price has not changed
    # todo - _up_gap            - gap between prior close and current open  (extend this for n days (up to 10))
    # todo - _down_gap          - gap between prior close and current open  (extend this for n days (up to 10))
    #                           - Use % size of the gap for relativity
    # Differential from yesterday (historical)
    # Differential from 2 days ago (historical)
    # Price in 1 to 10 days time
    # price in 30 days time 
    # perhaps these should be represented as a percentage and then categorised accordingly

# ==================================================================================================
# Volume Indicators
    # Averge Vol today
    # Averge Vol yesterday
    # Avg Vol for last 2 days, last 5 days, last 10 days etc
    # Vol into the future by an appropriate amount 1 day, 2 days, 5, 10 ,30 days
    # Is the above just the moving average - 
    # < check how the MACD works to smooth out the averages > migth be over sampling here?

# ==================================================================================================
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









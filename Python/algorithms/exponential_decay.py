```
Complete the exponential_decay function.

It calculates the final value of a quantity after a certain time has passed, 
given its initial value and decay rate. 
Be sure that you round the result to the nearest whole number. 
You can't have a fraction of a follower!
```

def decayed_followers(intl_followers, percent_lost_daily, days):
    return round(intl_followers * percent_lost_daily ** days - 1)

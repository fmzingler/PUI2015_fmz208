##This work was developed by Jingqin Gao and Fernando Zingler

The data waas provided by citibike website (https://www.citibikenyc.com/system-data), and both months of April and August were selected for analysis.

#IDEA

Standard subscribers are likely to be commuter on the morning peak.
Non-Subscribers (Customers) are less likely than subscribers to choose biking for commuting

#NULL HYPOTHESIS
For commercial hour, the ratio of average hourly trips by subscribers during peak hours to that of subscribers during off-peaak hours is same or lower than the same for non-subscribers (customers).
Peak Hours: 8AM-10AM AND 5PM-8PM
Off-Peak Hours: 6AM-8AM and 10AM-5PM
Commercial Hours: 6AM-8PM

#ALTERNATIVE HYPOTHESIS
For commercial hour, the ratio of average hourly trips by subscribers during peak hours to that of subscribers during off-peaak hours is significaantly higher than the same for non-subscribers..
significant level 0.05

#CONTRIBUIIONS
The hypothesis (null and alternative) were created by both authors together. Jingqin developed the base code. Fernando reviewed the logic and formulation of the code.
Jingquin tested the code for April 2015 and Fernando for August 2015. 


#ANALYSIS AND RESULTS
August data is larger then April, but the distribuition for the trips dusring the day are very similar, including same peak hours in the morning/afternoon.

For both months evaluated, the Null Hypothesis could be rejected. In April, the z score resulted in 79.22, which is very large. In this case, a probabiility of p=0.9998 was used, which resulted in  a value smaller than thee level of significance established. In August, the z value was even bigger (127.70), providing the same result as April: The Null Hyothesis could be rejected. 

The test selected can be considered appropriated because the samples are random and independent.



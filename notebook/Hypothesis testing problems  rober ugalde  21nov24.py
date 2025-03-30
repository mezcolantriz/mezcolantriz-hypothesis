# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:28:02 2024
Hypothesis testing problems







@author: rober ugalde
"""

from scipy.stats import ttest_ind

# Data for the two diets
diet_1 = [2.0, 2.5, 3.0, 2.8, 2.3, 2.7, 2.5]
diet_2 = [3.0, 3.2, 3.1, 2.9, 2.8, 3.0, 3.2]

# Perform an independent t-test
t_stat, p_value = ttest_ind(diet_1, diet_2)

# Print the results
print("T-Statistic:", round(t_stat, 4))
print("P-Value:", round(p_value, 4))

# Conclusion based on p-value
alpha = 0.05
if p_value < alpha:
    print("Conclusion: Reject the null hypothesis. There is a significant difference in average weight loss between the two diets.")
else:
    print("Conclusion: Fail to reject the null hypothesis. There is no significant difference in average weight loss between the two diets.")


comment - Analyze the conclusions. :
    
    The data provides strong evidence that the weight loss 
    outcomes differ between the two diets, with Diet 2 appearing 
    to be more effective. Further investigation or experimentation 
    might focus on why Diet 2 performs better.
    
    
"""
ANOVA
ANOVA (Analysis of Variance) is a statistical technique used to compare the measures of two or more groups. The idea behind ANOVA is to decompose the total variability in the data into two components: between-group variability and within-group variability:

Between-group variability: This variability refers to the differences between the group means. If this variability is considerably larger than the within-group variability, it could be an indication that at least one of the group means is different.
Within-group variability: This variability refers to the dispersion of the data within each group. If all groups have similar variability, then any noticeable difference in group means could be considered significant.
Hypotheses in ANOVA typically include:

Null hypothesis (₀
): The means of all groups are equal.
Alternative hypothesis (₁
): At least one of the group means is different.
If the ANOVA test result is significant (e.g., a p-value less than a threshold such as 0.05), this suggests that at least one group mean is different.

Exercise 2
A farmer decides to test three different types of fertilizers to determine if one is superior in terms of corn production. The farmer plants corn on 15 identical plots and uses all three fertilizers (5 plots for each type). At the end of the season, he measures the corn yield (in kg) of each plot, with the following result:

Fertilizer 1	Fertilizer 2	Fertilizer 3
20	22	24
21	21	23
20	23	22
19	22	23
20	21	24
With this data, he seeks to answer the following question: Is there a significant difference in average corn yield between the three types of fertilizers?

To help you, follow the points below:

State the hypothesis: null and alternative hypothesis.
Perform the ANOVA test.

    
   """ 
    
  from scipy.stats import f_oneway

# Corn yield data for the three fertilizers
fertilizer_1 = [20, 21, 20, 19, 20]
fertilizer_2 = [22, 21, 23, 22, 21]
fertilizer_3 = [24, 23, 22, 23, 24]

# Perform one-way ANOVA
f_stat, p_value = f_oneway(fertilizer_1, fertilizer_2, fertilizer_3)

# Print the results
print("F-Statistic:", round(f_stat, 4))
print("P-Value:", round(p_value, 4))

# Conclusion based on p-value
alpha = 0.05
if p_value < alpha:
    print("Conclusion: Reject the null hypothesis. There is a significant difference in average corn yield between the three fertilizers.")
else:
    print("Conclusion: Fail to reject the null hypothesis. There is no significant difference in average corn yield between the three fertilizers.")

    
    result : F-Statistic: 20.3158
    P-Value: 0.0001
    Conclusion: Reject the null hypothesis. There is a significant difference in average corn yield between the three fertilizers.
 
    
    """
Analyze the conclusions.
If one fertilizer is better than another, how can we know it?
"""
   
    If the p-value is greater than 0.05:
Fail to reject the null hypothesis (𝐻0H 0 ).
This indicates there is no significant difference between the average corn yields of the three fertilizers.


If the p-value is less than or equal to 0.05:
Reject the null hypothesis (𝐻0H 0).
This suggests that at least one fertilizer produces 
a significantly different average yield.




    
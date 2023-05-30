"""Operations on multiple dataframes
Description
Given three data frames containing the number of gold, silver, and bronze Olympic medals 
won by some countries, determine the total number of medals won by each country. 

Note: All three data frames don’t have all the same countries. So, ensure you use 
the ‘fill_value’ argument (set it to zero), to avoid getting NaN values. Also, ensure you sort 
the final data frame, according to the total medal count in descending order. 
Make sure that the results are in integers."""

import numpy as np 
import pandas as pd

# Defining the three dataframes indicating the gold, silver, and bronze medal counts
# of different countries
gold = pd.DataFrame({'Country': ['USA', 'France', 'Russia'],
                         'Medals': [15, 13, 9]}
                    )
silver = pd.DataFrame({'Country': ['USA', 'Germany', 'Russia'],
                        'Medals': [29, 20, 16]}
                    )
bronze = pd.DataFrame({'Country': ['France', 'USA', 'UK'],
                        'Medals': [40, 28, 27]}
                    )

final_df = pd.concat([gold, silver, bronze], axis=0)
count_df = final_df.groupby( by = "Country").sum().sort_values("Medals", ascending = False)

print(count_df)
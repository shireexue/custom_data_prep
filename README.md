# Welcome to Custom_Data_Prep
> This is a library to help data scientist to efficiently prepare datasets for analysis and modeling


```python
%load_ext autoreload
%autoreload 2
```

    The autoreload extension is already loaded. To reload it, use:
      %reload_ext autoreload


```python
import pandas as pd
from custom_data_prep.core import cat_treat
import numpy as np
```

## Install

`pip install custom_data_prep`

## How to use

```python
# Import data 
data = {'Name':['Tom', 'nick', 'krish', 'jack','Amy','Lily','Carol'],
        'Age':['33','22','41','12','34','21','60'],
        'Country':['US','AU','UK','CN','US','JP','NZ'],
        'target':[1,0,0,1,0,1,1]
       }

df=pd.DataFrame(data)
```

Result before collapsing - 'Country' feature has 6 levels

```python
# Import class and apply function

o =cat_treat(df,['Country'])
df_new,catclasses=o.reduce_cardinality(keep_level=3)

```

Result after collapsing - Now 'Country' has been reduced to 3 levels only 

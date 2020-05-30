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
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
      <th>Country</th>
      <th>target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom</td>
      <td>33</td>
      <td>US</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>nick</td>
      <td>22</td>
      <td>AU</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>krish</td>
      <td>41</td>
      <td>UK</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>jack</td>
      <td>12</td>
      <td>CN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>34</td>
      <td>US</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Lily</td>
      <td>21</td>
      <td>JP</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Carol</td>
      <td>60</td>
      <td>NZ</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



```python
# Import class and apply function

o =cat_treat(df,['Country'])
df_new,catclasses=o.reduce_cardinality(keep_level=3)

```

Result after collapsing - Now 'Country' has been reduced to 3 levels only 

```python
df_new
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
      <th>Country</th>
      <th>target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom</td>
      <td>33</td>
      <td>US</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>nick</td>
      <td>22</td>
      <td>OTHER</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>krish</td>
      <td>41</td>
      <td>OTHER</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>jack</td>
      <td>12</td>
      <td>CN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>34</td>
      <td>US</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Lily</td>
      <td>21</td>
      <td>OTHER</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Carol</td>
      <td>60</td>
      <td>OTHER</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



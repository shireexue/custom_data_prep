# Welcome to Custom_Data_Prep
> This is a library built with NBDEV to help data scientist to efficiently prepare datasets for analysis and modeling


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
print(df)
```

        Name Age Country  target
    0    Tom  33      US       1
    1   nick  22      AU       0
    2  krish  41      UK       0
    3   jack  12      CN       1
    4    Amy  34      US       0
    5   Lily  21      JP       1
    6  Carol  60      NZ       1


```python
# Import class and apply function

o =cat_treat(df,['Country'])
df_new,catclasses=o.reduce_cardinality(keep_level=3)

```

Result after collapsing - Now 'Country' has been reduced to 3 levels only 

```python
print(df_new)
```

        Name Age Country  target
    0    Tom  33      US       1
    1   nick  22   OTHER       0
    2  krish  41   OTHER       0
    3   jack  12      CN       1
    4    Amy  34      US       0
    5   Lily  21   OTHER       1
    6  Carol  60   OTHER       1


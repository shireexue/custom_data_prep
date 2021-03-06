# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['collapse_level', 'cat_treat']

# Cell
import numpy as np

def collapse_level(df,categorical_vars,keep_level=20):
    """Collapse levels for categorical variables with high cardinality.

    This operation identifies categorical variables with high cardinality and combine into levels that have
    both high target rates and frequency. The number of levels to keep is defined by user.

    Parameters
    ----------
    df : pandas dataframe, required
        Dataframe to process

    categorical_vars : list, required
        A list of categorical variables that will go through the treatment process

    keep_level : int, required
        Used to select high cardinality variables which exceed the specified level and collapse existing
        levels to this range.

    """

    numclasses={}
    catclasses={}
    for c in categorical_vars:
        uni_cnt=(len(np.unique(df[[c]])))
        numclasses[c]=uni_cnt
        if uni_cnt>keep_level:
            df_group=df.groupby(c).agg(pred_rate=('target','mean'),cnt=('Name','count')).reset_index()\
                       .sort_values(['cnt','pred_rate'],ascending=False)[:keep_level-1]
            keep_list=df_group.iloc[:,0].tolist()
            df[c]=np.where(~df[c].isin(keep_list),'OTHER',df[c])
            catclasses[c]=df.loc[:,c].unique().tolist()

    return df,catclasses

# Cell
class cat_treat:

    def __init__(self, df, categorical_vars):

        #attributes
        self.df=df
        self.categorical_vars=categorical_vars

    def reduce_cardinality(self,keep_level=20):
        """Collapse levels for categorical variables with high cardinality.

        This operation identifies categorical variables with high cardinality and combine into levels that have
        both high target rates and frequency. The number of levels to keep is defined by user.

        Parameters
        -----------
        df : pandas dataframe, required
            Dataframe to process

        categorical_vars : list, required
            A list of categorical variables that will go through the treatment process

        keep_level : int, required
            Used to select high cardinality variables which exceed the specified level and collapse existing
            levels to this range.

        """
        return collapse_level(self.df,self.categorical_vars,keep_level)
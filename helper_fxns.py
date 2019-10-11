# yapf: disable
import re

def get_public_school_dis(df, col):
    '''Filters for only public school district aka ISD or CISD
    Args:
        df: the DataFrame that contains col
        col: the header name of the column to perform the filter on
    Returns:
        ret_df: the filtered DataFrame
    '''
    is_public_school_dis = df[col].str.match('.*ISD')
    ret_df = df[is_public_school_dis]
    return(ret_df)

def remove_cisd_isd_from_col(df, col):
    '''Removes CISD or ISD from strings in a column
    Args:
        df: the DataFrame that contains col
        col: the header name of the column to perform the removal on
    Returns:
        df: the DataFrame with the altered strings
    '''
    is_isd_cisd = re.compile(r'\s(CISD|ISD|CONSOLIDATED ISD|CONSOLIDATED CISD|Consolidated Independent School District, TX|Independent School District, TX)')
    df[col] =df[col].replace(to_replace=is_isd_cisd, value='') 
    return (df)
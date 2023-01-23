import pandas as pd
import numpy as np

def date_to_int(df, column):

    """Convierte una columna de fechas al número de días desde una fecha mínima

        Args:
            df(DataFrame): Dataframe en el que se convertirá la columna
            column(str): nombre de la columna

        Returns:
            new_df(DataFrame): DataFrame con la nueva columna incluida
    """

    new_df = df

    min_date = '1970-01-01 00:00:00' #minima fecha que se puede convertir a Timestamp
    new_df.loc[new_df[column] < min_date, column] = min_date
    
    new_col = column + "_INT"
    
    new_df[new_col] = pd.to_datetime(new_df[column]).values.astype(np.int64) // (144 * 1e10)
    
    return new_df


def sep_groups(df, column):

    """ Separa los grupos concatenados como string de la columna en variables dummy
        
        Args:
            df(DataFrame): Dataframe donde se procesará la columna
            column(str): nombre de la columna
        Returns:
            new_df(DataFrame): DataFrame que incluye las variables dummy de cada columna
    """
    
    new_df = df
    groups_df = new_df[column].str.split('|', expand = True)

    groups_list = []
    for i in range(groups_df.shape[1]):
        groups_list.extend(groups_df[i].unique())

    groups_list = list(set(groups_list))
    groups_list.remove('None')

    groups_df = pd.get_dummies(groups_df)
    colnames_groups = groups_df.columns

    for group in groups_list:
        new_df[group] = np.zeros(df.shape[0])
        
        for col in colnames_groups:
            if col.endswith(group):
                new_df[group] = new_df[group] + groups_df[col]

    return new_df
    
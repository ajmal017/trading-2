def create_rollings(work_df, column, agg_func, windows, min_period=None):
    """
    work_df: un DataFrame
    column: str, columna a la cual se quiere applicar los rollings
    agg_func: str, funcion de agregacion de los rollings
    windows: iter, iterable con los numeros de ventanas para hacer los rollings
    min_periods: int, periodos minimos para agregar el rolling
    Return:
    DataFrame  con los las columnas hechas rolling
    """

    rolling_df = pd.concat(map(lambda win: pd.DataFrame(work_df[column].rolling(window=win,
                                 min_periods=min_period).agg(agg_func).shift(1)).rename(columns=dict(zip(agg_func, 
                                                [f'Rolling_{agg}_{column}_{win}' for agg in agg_func]))), 
                                                        windows), 
                                                            axis=1)
    return rolling_df
    
def create_shifts(work_df, column, shifts):
    """
    work_df: un DataFrame
    column: str, columna a la cual se quiere applicar los shift
    shifts: iterable con los numeros de shifts a aplicar

    """
    shift_df = pd.concat(map(lambda sh: work_df[column].shift(sh), shifts), axis=1)
    shift_df.columns = [f"{column}_shift_{sh}" for sh in shifts]
    return shift_df
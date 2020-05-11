def CAPM(ri, rf, rm):
    """E (ri)= rf + β [E (rm) – rf]

    E (ri): Tasa de rentabilidad esperada de un activo concreto, por ejemplo, de una acción del Ibex 35.
    rf: Rentabilidad del activo sin riesgo. Realmente, todos los activos financieros conllevan riesgo. 
            Por lo que buscamos activos de menor riesgo, que en escenarios de normalidad son los activos de deuda pública. (CETES)
    Beta de un activo financiero: Medida de la sensibilidad del activo respecto a su Benchmark.
            La interpretación de este parámetro nos permite conocer la variación relativa de la rentabilidad 
            del activo respecto al mercado en que cotiza. Por ejemplo, si una acción del IBEX 35 tiene una Beta de 1,1, 
            quiere decir que cuando el IBEX suba un 10% la acción subirá un 11%.
    E(rm): Tasa de rentabilidad esperada del mercado en que cotiza el activo. Por ejemplo, del IBEX 35 (IPC).
    
    Descomponiendo la fórmula, podemos diferenciar dos factores:

        rm – rf: Riesgo asociado al mercado en que cotiza el activo.
        ri – rf: Riesgo asociado al activo en concreto."""
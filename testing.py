import Laboratorio;
import pytest;

def test_convertirBinario_1():
    assert Laboratorio.convertirBinario(2345) == 100100101001

def test_convertirBinario_2():
    assert Laboratorio.convertirBinario(0) == 0

def test_convertirBinario_3():
    assert Laboratorio.convertirBinario(3) == 11

def test_digitosOrdenados_1():
    assert Laboratorio.digitosOrdenados(2345678) == True

def test_digitosOrdenados_2():
    assert Laboratorio.digitosOrdenados(92345678) == False

#####################################################################################################

def test_extremosLista_1():
    assert Laboratorio.extremosLista([18,5,8,45,96, 60]) == [5,96]

def test_extremosLista_2():
    assert Laboratorio.extremosLista([96, 96,96]) == [96]

def test_extremosLista_3():
    assert isinstance(Laboratorio.extremosLista([]), str) == isinstance("Error: La lista debe contener al menos 2 elementos", str)

def test_extremosLista_4():
    assert isinstance(Laboratorio.extremosLista([2,5,7,"ABC"]), str) == isinstance("Error: La lista debe contener elementos tipo entero", str)
    
#####################################################################################################

def test_eliminarElementosLista_1():
    assert Laboratorio.eliminarElementosLista([254, 25, 8], [25]) == [254, 8]

def test_eliminarElementosLista_2():
    assert Laboratorio.eliminarElementosLista([54, 25, 8], [25, 54]) == [8]

def test_eliminarElementosLista_3():
    assert Laboratorio.eliminarElementosLista([54, 25, 8], [21, 24]) == [54,25,8]

def test_eliminarElementosLista_4():
    assert isinstance(Laboratorio.eliminarElementosLista([], [2,4]), str) == isinstance("Error: La primera lista debe contener al menos 1 elemento", str) 

def test_eliminarElementosLista_5():
    assert isinstance(Laboratorio.eliminarElementosLista([23,78,9], []), str) == isinstance("Error: La segunda lista debe contener al menos 1 elemento", str) 

def test_eliminarElementosLista_6():
    assert isinstance(Laboratorio.extremosLista([2,5,7,"ABC"], [2,8]), str) == isinstance("Error: La primera lista debe elementos tipo entero", str) 

def test_eliminarElementosLista_7():
    assert isinstance(Laboratorio.extremosLista([2,5,7], [2,"8"]), str) == isinstance("Error: La segunda lista debe elementos tipo entero", str) 

#####################################################################################################

def test_cortarNumero_1():
    assert Laboratorio.cortarNumero(1335, 1, 2) == 33

def test_cortarNumero_2():
    assert isinstance(str(Laboratorio.cortarNumero(1335, 8, 2)), str) == isinstance('Error: Indices fuera del rango del número', str)  

###########################################################################    

def test_corrimientoAEntero_1():
    assert Laboratorio.corrimientoAEntero(133.5) == 1335
    
def test_corrimientoAEntero_2():
    assert Laboratorio.corrimientoAEntero(-133.5) == -1335  

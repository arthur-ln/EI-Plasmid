from RotTable import RotTable

def test_write():
    R1 = RotTable()
    R2 = RotTable()
    Matrice1 = R1.getRotTable()
    R2.generate()
    R2.writeRotTable(Matrice1)
    Matrice2 = R2.getRotTable()
    #vérification que la fonction write fonctionne correctement
    assert(Matrice1==Matrice2)



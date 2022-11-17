#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Pezzo import Pezzo

class Re(Pezzo):
    """
    implementa il Re
    """

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Torre')
        self.graphic_rep = '\u2654' if self.colore == 'W' else '\u265a'

    def verifica_mossa(self, destinazione):
        """
        verifica se il Re può essere mosso alla destinazione

        Parameters
        ----------
        destinazione : coppia di coordinate (list)
            posizione di destinazione della mossa

        Returns
        -------
        bool
        indica se la mossa è legale o no

        """
        if super().verifica_mossa(destinazione):  # le condizioni generiche sono verificate
            if self.posizione[0] == destinazione[0]:  # la mossa è lungo la stessa riga
                if destinazione[1]-1 > (self.posizione[1]-1)+1 or destinazione[1]-1 < (self.posizione[1]-1)-1:
                    print(f"La mossa non è legale, il Re non può spostarsi di due caselle a destra/sinistra.")
                    return False
                if destinazione[1]-1 == (self.posizione[1]-1)+1 or destinazione[1]-1 == (self.posizione[1]-1)-1:
                    riga = destinazione[1]
                return True

            elif self.posizione[1] == destinazione[1]:  # la mossa è lungo la stessa colonna
                if ord(destinazione[0])-1 > (ord(self.posizione[0])-1)+1 or ord(destinazione[0])-1 < (ord(self.posizione[0])-1)-1: #Se voglio spostarmi di due in avanti o indietro
                    print(f"La mossa non è legale, il Re non può spostarsi di due caselle avanti/indietro.")
                    return False
                if ord(destinazione[0])-1 == (ord(self.posizione[0])-1)+1 or ord(destinazione[0])-1 == (ord(self.posizione[0])-1)-1: #se la destinazione è sulla riga precedente o successica della stessa colonna
                    col = ord(destinazione[0])
                return True

            elif destinazione[1] < self.posizione[1] and destinazione[0] < self.posizione[0]: #la mossa è in diagonale verso l'alto a sinistra
                if ord(destinazione[0])-1 == (ord(self.posizione[0])-1)-1 and destinazione[1]-1 == (self.posizione[1]-1)-1:
                    riga = destinazione[1]
                    col = ord(destinazione[0])
                else:
                    print(f"La mossa non è legale, il Re non può fare questo spostamento")
                    return False
                return True

            elif  destinazione[1] > self.posizione[1] and destinazione[0] < self.posizione[0]:# la mossa è in diagonale verso l'alto a destra
                if ord(destinazione[0])-1 == (ord(self.posizione[0])-1)-1 and destinazione[1]-1 == (self.posizione[1]-1)+1:
                    riga = destinazione[1]
                    col = ord(destinazione[0])
                else:
                    print(f"La mossa non è legale, il Re non può fare questo spostamento")
                    return False
                return True

            elif destinazione[1] < self.posizione[1] and destinazione[0] > self.posizione[0]: # la mossa è in diagonale verso il basso a sinistra
                if ord(destinazione[0])-1 == (ord(self.posizione[0])-1)+1 and destinazione[1]-1 == (self.posizione[1]-1)-1:
                    riga = destinazione[1]
                    col = ord(destinazione[0])
                else:
                    print(f"La mossa non è legale, il Re non può fare questo spostamento")
                    return False
                return True

            elif destinazione[1] > self.posizione[1] and destinazione[0] > self.posizione[0]: #la mossa è in diagonale verso il basso a destra
                if ord(destinazione[0])-1 == (ord(self.posizione[0])-1)+1 and destinazione[1]-1 == (self.posizione[1]-1)+1:
                    riga = destinazione[1]
                    col = ord(destinazione[0])
                else:
                    print(f"La mossa non è legale, il Re non può fare questo spostamento")
                    return False
                return True

            else:
                print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Re')
                return False
        else:
            print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Re')
            return False

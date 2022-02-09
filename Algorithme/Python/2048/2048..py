# coding: utf-8

from tkinter import *
from tkinter import messagebox
import random

class DefaultBoardX4:
    """
    Classe par défaut du tableau 2048, permet d'initialiser l'interface,
    les couleurs (ici de base), l'appararition des tuiles,
    et tout se qui permet de faire fonctionner le jeu
    """
    bg_color={#couleur de fond des blocks
        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#edc850',
        '16': '#edc53f',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#f2b179',
        '1024': '#f59563',
        '2048': '#edc22e',
    }

    color={#couleur des nombres
        '2': '#776e65',
        '4': '#f9f6f2',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#776e65',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }


    def __init__(self):
        """
        Permet de créer la fenêtre de jeu, nombre de case du tableau,
        couleur de fond, titre + police...
        """
        self.window=Tk()
        self.window.title('2048')
        self.window.iconbitmap('.\\Sans titre - 3.ico')
        self.gameArea=Frame(self.window,bg= 'azure3')
        self.board=[]
        self.gridCell=[[0]*4 for i in range(4)]
        self.compress=False
        self.merge=False
        self.moved=False
        self.score=0

        for i in range(4):
            rows=[]
            for j in range(4):
                l=Label(self.gameArea,text='',bg='azure4',
                font=('arial',22,'bold'),width=4,height=2)
                l.grid(row=i,column=j,padx=7,pady=7)

                rows.append(l);
            self.board.append(rows)
        self.gameArea.grid()

    def reverse(self):
        """
        Inverse les positions x et y (notamment utilisé quand les touches
        down et right sont pressé)
        """
        for ind in range(4):
            i=0
            j=3
            while(i<j):
                self.gridCell[ind][i],self.gridCell[ind][j]=self.gridCell[ind][j],self.gridCell[ind][i]
                i+=1
                j-=1

    def transpose(self):
        """
        Utilise la fonction zip pour stocker le tableau sous forme de liste
        """

        self.gridCell=[list(t)for t in zip(*self.gridCell)]

    def compressGrid(self):
        """
        Permet la fusion de deux tuiles
        """

        self.compress=False
        temp=[[0] *4 for i in range(4)]
        for i in range(4):
            cnt=0
            for j in range(4):
                if self.gridCell[i][j]!=0:
                    temp[i][cnt]=self.gridCell[i][j]
                    if cnt!=j:
                        self.compress=True
                    cnt+=1
        self.gridCell=temp

    def mergeGrid(self):
        """
        Fonction qui gère la fusion des tuiles avec la même valeur
        """
        self.merge=False
        for i in range(4):
            for j in range(4 - 1):
                if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                    self.gridCell[i][j] *= 2
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge = True

    def random_cell(self):
        """
        Permet de déposer une tuile 2 ou 4 aléatoirement en début partie
        """
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]= 2 if random.random()<=.80 else 4

    def random_cell2(self):
        """
        Pareil mais uniquement avec des tuiles 2
        """
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]= 2

    def can_merge(self):
        """
        Permet de savoir si la fusion de deux tuiles est possible (renvoie un
        booléen
        """
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j] == self.gridCell[i][j+1]:
                    return True

        for i in range(3):
            for j in range(4):
                if self.gridCell[i+1][j] == self.gridCell[i][j]:
                    return True
        return False

    def paintGrid(self):
        """
        Fonction qui permet de donner les couleurs correspondant à sa couleur
        sur color et bgcolor
        """
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j]==0:
                    self.board[i][j].config(text='',bg='azure4')
                else:
                    self.board[i][j].config(text=str(self.gridCell[i][j]),
                    bg=self.bg_color.get(str(self.gridCell[i][j])),
                    fg=self.color.get(str(self.gridCell[i][j])))

class LightBoardX4:
    """
    2048 en tableau x4, avec des couleurs clair
    """
    bg_color={#couleur de fond des blocks
        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#f2b279',
        '16': '#f59563',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#edc850',
        '1024': '#edc53f',
        '2048': '#edc22e',
    }

    color={#couleur des nombres
        '2': '#776e65',
        '4': '#776e65',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#f9f6f2',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }

    def __init__(self):
        self.window=Tk()
        self.window.title('2048')
        self.window.iconbitmap('.\\Sans titre - 3.ico')
        self.gameArea=Frame(self.window,bg= '#bbada0')
        self.board=[]
        self.gridCell=[[0]*4 for i in range(4)]
        self.compress=False
        self.merge=False
        self.moved=False
        self.score=0

        for i in range(4):
            rows=[]
            for j in range(4):
                l=Label(self.gameArea,text='',bg='azure4',
                font=('arial',22,'bold'),width=4,height=2)
                l.grid(row=i,column=j,padx=7,pady=7)

                rows.append(l);
            self.board.append(rows)
        self.gameArea.grid()

    def reverse(self):
        for ind in range(4):
            i=0
            j=3
            while(i<j):
                self.gridCell[ind][i],self.gridCell[ind][j]=self.gridCell[ind][j],self.gridCell[ind][i]
                i+=1
                j-=1

    def transpose(self):
        self.gridCell=[list(t)for t in zip(*self.gridCell)]

    def compressGrid(self):
        self.compress=False
        temp=[[0] *4 for i in range(4)]
        for i in range(4):
            cnt=0
            for j in range(4):
                if self.gridCell[i][j]!=0:
                    temp[i][cnt]=self.gridCell[i][j]
                    if cnt!=j:
                        self.compress=True
                    cnt+=1
        self.gridCell=temp

    def mergeGrid(self):
        self.merge=False
        for i in range(4):
            for j in range(4 - 1):
                if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                    self.gridCell[i][j] *= 2
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge = True

    def random_cell(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]= 2 if random.random()<=.80 else 4

    def random_cell2(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]= 2

    def can_merge(self):
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j] == self.gridCell[i][j+1]:
                    return True

        for i in range(3):
            for j in range(4):
                if self.gridCell[i+1][j] == self.gridCell[i][j]:
                    return True
        return False

    def paintGrid(self):
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j]==0:
                    self.board[i][j].config(text='',bg='#cdc1b4')
                else:
                    self.board[i][j].config(text=str(self.gridCell[i][j]),
                    bg=self.bg_color.get(str(self.gridCell[i][j])),
                    fg=self.color.get(str(self.gridCell[i][j])))

class DarkBoardX4:
    """
    2048 en tableau x4, avec des couleurs sombre
    """
    bg_color={#couleur de fond des blocks
        '2': '#392a1a',
        '4': '#473717',
        '8': '#7f410c',
        '16': '#8e3609',
        '32': '#902208',
        '64': '#a62508',
        '128': '#826611',
        '256': '#8d6f10',
        '512': '#977710',
        '1024': '#a2800f',
        '2048': '#ac890f',
    }

    color={#couleur des nombres
        '2': '#776e65',
        '4': '#776e65',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#f9f6f2',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }

    def __init__(self):
        self.window=Tk()
        self.window.title('2048')
        self.window.iconbitmap('.\\Sans titre - 3.ico')
        self.gameArea=Frame(self.window,bg= '#574a3e')
        self.board=[]
        self.gridCell=[[0]*4 for i in range(4)]
        self.compress=False
        self.merge=False
        self.moved=False
        self.score=0

        for i in range(4):
            rows=[]
            for j in range(4):
                l=Label(self.gameArea,text='',bg='azure4',
                font=('arial',22,'bold'),width=4,height=2)
                l.grid(row=i,column=j,padx=7,pady=7)

                rows.append(l);
            self.board.append(rows)
        self.gameArea.grid()

    def reverse(self):
        for ind in range(4):
            i=0
            j=3
            while(i<j):
                self.gridCell[ind][i],self.gridCell[ind][j]=self.gridCell[ind][j],self.gridCell[ind][i]
                i+=1
                j-=1

    def transpose(self):
        self.gridCell=[list(t)for t in zip(*self.gridCell)]

    def compressGrid(self):
        self.compress=False
        temp=[[0] *4 for i in range(4)]
        for i in range(4):
            cnt=0
            for j in range(4):
                if self.gridCell[i][j]!=0:
                    temp[i][cnt]=self.gridCell[i][j]
                    if cnt!=j:
                        self.compress=True
                    cnt+=1
        self.gridCell=temp

    def mergeGrid(self):
        self.merge=False
        for i in range(4):
            for j in range(4 - 1):
                if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                    self.gridCell[i][j] *= 2
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge = True

    def random_cell(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]= 2 if random.random()<=.80 else 4

    def random_cell2(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]= 2

    def can_merge(self):
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j] == self.gridCell[i][j+1]:
                    return True

        for i in range(3):
            for j in range(4):
                if self.gridCell[i+1][j] == self.gridCell[i][j]:
                    return True
        return False

    def paintGrid(self):
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j]==0:
                    self.board[i][j].config(text='',bg='#4d3f31')
                else:
                    self.board[i][j].config(text=str(self.gridCell[i][j]),
                    bg=self.bg_color.get(str(self.gridCell[i][j])),
                    fg=self.color.get(str(self.gridCell[i][j])))

class DefaultBoardX8:
    """
    2048 en tableau x8 (remplace toute les occurence de 4 (pour un tableau en x4)
    par 8 (pour un tableau en x8))
    """
    bg_color={
        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#edc850',
        '16': '#edc53f',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#f2b179',
        '1024': '#f59563',
        '2048': '#edc22e',
    }

    color={
        '2': '#776e65',
        '4': '#f9f6f2',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#776e65',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }

    def __init__(self):
        """
        changement : défini le tableau en x8
        """
        self.window=Tk()
        self.window.title('2048')
        self.window.iconbitmap('.\\Sans titre - 3.ico')
        self.gameArea=Frame(self.window,bg= 'azure3')
        self.board=[]
        self.gridCell=[[0]*8 for i in range(8)]
        self.compress=False
        self.merge=False
        self.moved=False
        self.score=0

        for i in range(8):
            rows=[]
            for j in range(8):
                l=Label(self.gameArea,text='',bg='azure4',
                font=('arial',22,'bold'),width=4,height=2)
                l.grid(row=i,column=j,padx=7,pady=7)

                rows.append(l);
            self.board.append(rows)
        self.gameArea.grid()

    def reverse(self):
        for ind in range(8):
            i=0
            j=7
            while(i<j):
                self.gridCell[ind][i],self.gridCell[ind][j]=self.gridCell[ind][j],self.gridCell[ind][i]
                i+=1
                j-=1

    def transpose(self):
        self.gridCell=[list(t)for t in zip(*self.gridCell)]

    def compressGrid(self):
        self.compress=False
        temp=[[0] *8 for i in range(8)]
        for i in range(8):
            cnt=0
            for j in range(8):
                if self.gridCell[i][j]!=0:
                    temp[i][cnt]=self.gridCell[i][j]
                    if cnt!=j:
                        self.compress=True
                    cnt+=1
        self.gridCell=temp

    def mergeGrid(self):
        self.merge=False
        for i in range(8):
            for j in range(8 - 1):
                if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                    self.gridCell[i][j] *= 2
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge = True

    def random_cell(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]= 2 if random.random()<=.80 else 4

    def random_cell2(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]= 2

    def can_merge(self):
        for i in range(8):
            for j in range(7):
                if self.gridCell[i][j] == self.gridCell[i][j+1]:
                    return True

        for i in range(7):
            for j in range(8):
                if self.gridCell[i+1][j] == self.gridCell[i][j]:
                    return True
        return False

    def paintGrid(self):
        for i in range(8):
            for j in range(8):
                if self.gridCell[i][j]==0:
                    self.board[i][j].config(text='',bg='azure4')
                else:
                    self.board[i][j].config(text=str(self.gridCell[i][j]),
                    bg=self.bg_color.get(str(self.gridCell[i][j])),
                    fg=self.color.get(str(self.gridCell[i][j])))

class LightBoardX8:
    """
    2048 en tableau x8, avec des couleurs clair
    """
    bg_color={#couleur de fond des blocks
        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#f2b279',
        '16': '#f59563',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#edc850',
        '1024': '#edc53f',
        '2048': '#edc22e',
    }

    color={#couleur des nombres
        '2': '#776e65',
        '4': '#776e65',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#f9f6f2',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }

    def __init__(self):
        self.window=Tk()
        self.window.title('2048')
        self.window.iconbitmap('.\\Sans titre - 3.ico')
        self.gameArea=Frame(self.window,bg= '#bbada0')
        self.board=[]
        self.gridCell=[[0]*8 for i in range(8)]
        self.compress=False
        self.merge=False
        self.moved=False
        self.score=0

        for i in range(8):
            rows=[]
            for j in range(8):
                l=Label(self.gameArea,text='',bg='azure4',
                font=('arial',22,'bold'),width=4,height=2)
                l.grid(row=i,column=j,padx=7,pady=7)

                rows.append(l);
            self.board.append(rows)
        self.gameArea.grid()

    def reverse(self):
        for ind in range(8):
            i=0
            j=7
            while(i<j):
                self.gridCell[ind][i],self.gridCell[ind][j]=self.gridCell[ind][j],self.gridCell[ind][i]
                i+=1
                j-=1

    def transpose(self):
        self.gridCell=[list(t)for t in zip(*self.gridCell)]

    def compressGrid(self):
        self.compress=False
        temp=[[0] *8 for i in range(8)]
        for i in range(8):
            cnt=0
            for j in range(8):
                if self.gridCell[i][j]!=0:
                    temp[i][cnt]=self.gridCell[i][j]
                    if cnt!=j:
                        self.compress=True
                    cnt+=1
        self.gridCell=temp

    def mergeGrid(self):
        self.merge=False
        for i in range(8):
            for j in range(8 - 1):
                if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                    self.gridCell[i][j] *= 2
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge = True

    def random_cell(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]= 2 if random.random()<=.80 else 4

    def random_cell2(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]= 2

    def can_merge(self):
        for i in range(8):
            for j in range(7):
                if self.gridCell[i][j] == self.gridCell[i][j+1]:
                    return True

        for i in range(7):
            for j in range(8):
                if self.gridCell[i+1][j] == self.gridCell[i][j]:
                    return True
        return False

    def paintGrid(self):
        for i in range(8):
            for j in range(8):
                if self.gridCell[i][j]==0:
                    self.board[i][j].config(text='',bg='#cdc1b4')
                else:
                    self.board[i][j].config(text=str(self.gridCell[i][j]),
                    bg=self.bg_color.get(str(self.gridCell[i][j])),
                    fg=self.color.get(str(self.gridCell[i][j])))

class DarkBoardX8:
    """
    2048 en tableau x4, avec des couleurs clair
    """
    bg_color={#couleur de fond des blocks
        '2': '#392a1a',
        '4': '#473717',
        '8': '#7f410c',
        '16': '#8e3609',
        '32': '#902208',
        '64': '#a62508',
        '128': '#826611',
        '256': '#8d6f10',
        '512': '#977710',
        '1024': '#a2800f',
        '2048': '#ac890f',
    }

    color={#couleur des nombres
        '2': '#776e65',
        '4': '#776e65',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#f9f6f2',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }

    def __init__(self):
        self.window=Tk()
        self.window.title('2048')
        self.window.iconbitmap('.\\Sans titre - 3.ico')
        self.gameArea=Frame(self.window,bg= '#574a3e')
        self.board=[]
        self.gridCell=[[0]*8 for i in range(8)]
        self.compress=False
        self.merge=False
        self.moved=False
        self.score=0

        for i in range(8):
            rows=[]
            for j in range(8):
                l=Label(self.gameArea,text='',bg='azure4',
                font=('arial',22,'bold'),width=4,height=2)
                l.grid(row=i,column=j,padx=7,pady=7)

                rows.append(l);
            self.board.append(rows)
        self.gameArea.grid()

    def reverse(self):
        for ind in range(8):
            i=0
            j=7
            while(i<j):
                self.gridCell[ind][i],self.gridCell[ind][j]=self.gridCell[ind][j],self.gridCell[ind][i]
                i+=1
                j-=1

    def transpose(self):
        self.gridCell=[list(t)for t in zip(*self.gridCell)]

    def compressGrid(self):
        self.compress=False
        temp=[[0] *8 for i in range(8)]
        for i in range(8):
            cnt=0
            for j in range(8):
                if self.gridCell[i][j]!=0:
                    temp[i][cnt]=self.gridCell[i][j]
                    if cnt!=j:
                        self.compress=True
                    cnt+=1
        self.gridCell=temp

    def mergeGrid(self):
        self.merge=False
        for i in range(8):
            for j in range(8 - 1):
                if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                    self.gridCell[i][j] *= 2
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge = True

    def random_cell(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]= 2 if random.random()<=.80 else 4

    def random_cell2(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]= 2

    def can_merge(self):
        for i in range(8):
            for j in range(7):
                if self.gridCell[i][j] == self.gridCell[i][j+1]:
                    return True

        for i in range(7):
            for j in range(8):
                if self.gridCell[i+1][j] == self.gridCell[i][j]:
                    return True
        return False

    def paintGrid(self):
        for i in range(8):
            for j in range(8):
                if self.gridCell[i][j]==0:
                    self.board[i][j].config(text='',bg='#4d3f31')
                else:
                    self.board[i][j].config(text=str(self.gridCell[i][j]),
                    bg=self.bg_color.get(str(self.gridCell[i][j])),
                    fg=self.color.get(str(self.gridCell[i][j])))

class DefaultGameX4:
    """
    Classe qui permet d'éditer les touches
    et ajouter les tuiles en utilisant une de jeu en tableau x4
    """

    def __init__(self,gamepanel):
        """
        Permet d'initialiser la fenêtre
        """
        self.gamepanel=gamepanel
        self.end=False
        self.won=False

    def start(self):
        """
        Permet de rentrer des tuiles et commencer le jeu
        """
        self.gamepanel.random_cell()
        self.gamepanel.random_cell2()

        self.gamepanel.paintGrid()
        self.gamepanel.window.bind('<Key>', self.link_keys)
        self.gamepanel.window.mainloop()

    def link_keys(self,event):
        """
        Permet d'utiliser les touches du clavier
        """
        if self.end or self.won:
            return

        self.gamepanel.compress = False
        self.gamepanel.merge = False
        self.gamepanel.moved = False

        presed_key=event.keysym

        if presed_key=='Up':#keybind flèche du haut ⬆️
            self.gamepanel.transpose()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.transpose()

        elif presed_key=='Down':#keybind flèche du bas ⬇️
            self.gamepanel.transpose()
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()
            self.gamepanel.transpose()

        elif presed_key=='Left':#keybind flèche de gauche ⬅️
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()

        elif presed_key=='Right':#keybind flèche de droite ➡️
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()

        self.gamepanel.paintGrid()
        print(self.gamepanel.score)

        flag=0
        for i in range(4):
            for j in range(4):
                if(self.gamepanel.gridCell[i][j]==2048):
                    flag=1
                    break

        if(flag==1): #Chercher 2048
            self.won=True
            messagebox.showinfo('2048', message='You Won!!!🎉')
            print("Won")
            return

        for i in range(4):
            for j in range(4):
                if self.gamepanel.gridCell[i][j]==0:
                    flag=1
                    break

        if not (flag or self.gamepanel.can_merge()):
            self.end=True
            messagebox.showinfo('2048','Game Over!!!')
            print("Over")

        if self.gamepanel.moved:
            self.gamepanel.random_cell()

        self.gamepanel.paintGrid()

class DefaultGameX8:
    """
    Classe qui permet d'éditer les touches
    et ajouter les tuiles en utilisant une de jeu en tableau x8
    """
    def __init__(self,gamepanel):
        self.gamepanel=gamepanel
        self.end=False
        self.won=False

    def start(self):
        self.gamepanel.random_cell()
        self.gamepanel.random_cell2()

        self.gamepanel.paintGrid()
        self.gamepanel.window.bind('<Key>', self.link_keys)
        self.gamepanel.window.mainloop()

    def link_keys(self,event):
        if self.end or self.won:
            return

        self.gamepanel.compress = False
        self.gamepanel.merge = False
        self.gamepanel.moved = False

        presed_key=event.keysym

        if presed_key=='Up':#keybind flèche du haut ⬆️
            self.gamepanel.transpose()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.transpose()

        elif presed_key=='Down':#keybind flèche du bas ⬇️
            self.gamepanel.transpose()
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()
            self.gamepanel.transpose()

        elif presed_key=='Left':#keybind flèche de gauche ⬅️
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()

        elif presed_key=='Right':#keybind flèche de droite ➡️
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()

        self.gamepanel.paintGrid()
        print(self.gamepanel.score)

        flag=0
        for i in range(8):
            for j in range(8):
                if(self.gamepanel.gridCell[i][j]==2048):
                    flag=1
                    break

        if(flag==1): #Chercher 2048
            self.won=True
            messagebox.showinfo('2048', message='You Wonnn!!')
            print("won")
            return

        for i in range(8):
            for j in range(8):
                if self.gamepanel.gridCell[i][j]==0:
                    flag=1
                    break

        if not (flag or self.gamepanel.can_merge()):
            self.end=True
            messagebox.showinfo('2048','Game Over!!!')
            print("Over")

        if self.gamepanel.moved:
            self.gamepanel.random_cell()

        self.gamepanel.paintGrid()

class fin :
    """
    permet de créer une fenêtre qui compare le score des deux joueurs, et affiche le gagnant
    """
    def __init__(self, gamepanel, gamepanel2):
        self.window=Tk()
        self.window.iconbitmap('.\\Sans titre - 3.ico')
        self.window.title('Fin')
        self.gameArea=Frame(self.window,bg= 'azure3')
        self.board=[]
        self.compress=False
        self.merge=False
        self.moved=False
        if gamepanel.score > gamepanel2.score :
            label = Label(self.window, text= "J1 a gagné", font=('arial', 22, 'bold'), pady = 30)
            label.pack()
        elif gamepanel.score < gamepanel2.score :
            label = Label(self.window, text= "J2 a gagné", font=('arial', 22, 'bold'), pady = 30)
            label.pack()
        else :
            label = Label(self.window, text= "Egalité :(", font=('arial', 22, 'bold'), pady = 30)
            label.pack()
        self.window.mainloop()









class Interface1:
    """
    Interface pour choisir son mode de jeu : simple x4/x8, multi x4/x8 et un bouton vers l'interface 2
    """
    def __init__(self):

        def lunchdefaultx4():
            """
            Si l'utilisateur appuie sur le bouton 2048 x4, le jeu choisi se lance
            """
            gamepanel = DefaultBoardX4()
            game2048 = DefaultGameX4(gamepanel)
            game2048.start()

        def lunchdefaultx8():
            """
            Si l'utilisateur appuie sur le bouton 2048 x8, le jeu choisi se lance
            """
            gamepanel = DefaultBoardX8()
            game2048 = DefaultGameX8(gamepanel)
            game2048.start()

        def lunchdefaultmultiplayerx4():
            """
            Si l'utilisateur appuie sur le bouton 2048 x4 multiplayers, le jeu choisi se lance
            """
            gamepanel = DefaultBoardX4()
            game2048 = DefaultGameX4(gamepanel)
            game2048.start()

            gamepanel2 = DefaultBoardX4()
            game2048 = DefaultGameX4(gamepanel2)
            game2048.start()

            fin(gamepanel, gamepanel2)

        def lunchdefaultmultiplayerx8():
            """
            Si l'utilisateur appuie sur le bouton 2048 x8 multiplayers, le jeu choisi se lance
            """
            gamepanel = DefaultBoardX8()
            game2048 = DefaultGameX8(gamepanel)
            game2048.start()

            gamepanel2 = DefaultBoardX8()
            game2048= DefaultGameX8(gamepanel2)
            game2048.start()

            fin(gamepanel, gamepanel2)

        def interface2():
            """
            accès à la deuxième interface
            """
            Interface2()
        """
        Parti de code permettant de créer la fenêtre de choix et les boutons
        """
        tkWindow = Tk()
        tkWindow.geometry('400x350')
        tkWindow.iconbitmap('.\\Sans titre - 3.ico')
        tkWindow.title('Make your choice')

        label = Label(tkWindow,text='Que voulez vous faire ?',
            font=('arial',22,'bold'), pady=30)
        label.pack()

        button = Button(tkWindow,
	        text = '2048 - x4',
	        command=lunchdefaultx4,
            font=('arial',10,'bold'))
        button.pack()

        button = Button(tkWindow,
	        text = '2048 - x8',
	        command = lunchdefaultx8,
            font=('arial',10,'bold'))
        button.pack()

        label = Label(tkWindow,text='',
            font=('arial',0,'bold'))
        label.pack()

        button = Button(tkWindow,
	        text = 'Multiplayer 2048 - x4',
	        command = lunchdefaultmultiplayerx4,
            font=('arial',10,'bold'))
        button.pack()

        button = Button(tkWindow,
	        text = 'Multiplayer 2048 - x8',
	        command = lunchdefaultmultiplayerx8,
            font=('arial',10,'bold'))
        button.pack()

        label = Label(tkWindow,text='',
            font=('arial',0,'bold'))
        label.pack()

        button = Button(tkWindow,
	        text = '2048 - Colors',
	        command = interface2,
            font=('arial',10,'bold'))
        button.pack()

        tkWindow.mainloop()




class Interface2:

    def __init__(self):

        def close():
            tkWindow = Tk.quit

        def lunchlightx4():
            """
            Si l'utilisateur appuie sur le bouton 2048 x4 light, le jeu choisi se lance
            """
            gamepanel = LightBoardX4()
            game2048 = DefaultGameX4(gamepanel)
            game2048.start()

        def lunchdarkx4():
            """
            Si l'utilisateur appuie sur le bouton 2048 x4 dark, le jeu choisi se lance
            """
            gamepanel = DarkBoardX4()
            game2048 = DefaultGameX4(gamepanel)
            game2048.start()

        def lunchlightx8():
            """
            Si l'utilisateur appuie sur le bouton 2048 x8 light, le jeu choisi se lance
            """
            gamepanel = LightBoardX8()
            game2048 = DefaultGameX8(gamepanel)
            game2048.start()

        def lunchdarkx8():
            """
            Si l'utilisateur appuie sur le bouton 2048 x8 dark, le jeu choisi se lance
            """
            gamepanel = DarkBoardX8()
            game2048 = DefaultGameX8(gamepanel)
            game2048.start()

        def lunchlightmultiplayerx4():
            """
            Si l'utilisateur appuie sur le bouton 2048 x4 light multiplayers, le jeu choisi se lance
            """
            gamepanel = LightBoardX4()
            game2048 = DefaultGameX4(gamepanel)
            game2048.start()

            gamepanel2 = LightBoardX4()
            game2048 = DefaultGameX4(gamepanel2)
            game2048.start()

            fin(gamepanel,gamepanel2)

        def lunchdarkmultiplayerx4():
            """
            Si l'utilisateur appuie sur le bouton 2048 x4 dark multiplayers, le jeu choisi se lance
            """
            gamepanel = DarkBoardX4()
            game2048 = DefaultGameX4(gamepanel)
            game2048.start()

            gamepanel2 = DarkBoardX4()
            game2048 = DefaultGameX4(gamepanel2)
            game2048.start()

            fin(gamepanel,gamepanel2)

        def lunchlightmultiplayerx8():
            """
            Si l'utilisateur appuie sur le bouton 2048 x8 light multiplayers, le jeu choisi se lance
            """
            gamepanel = LightBoardX8()
            game2048 = DefaultGameX8(gamepanel)
            game2048.start()

            gamepanel2 = LightBoardX8()
            game2048 = DefaultGameX8(gamepanel2)
            game2048.start()

            fin(gamepanel,gamepanel2)

        def lunchdarkmultiplayerx8():
            """
            Si l'utilisateur appuie sur le bouton 2048 x8 dark muliplayers, le jeu choisi se lance
            """
            gamepanel = DarkBoardX8()
            game2048 = DefaultGameX8(gamepanel)
            game2048.start()

            gamepanel2 = DarkBoardX8()
            game2048 = DefaultGameX8(gamepanel2)
            game2048.start()

            fin(gamepanel,gamepanel2)
        """
        Parti de code permettant de créer la fenêtre de choix et les boutons
        """
        tkWindow = Tk()
        tkWindow.geometry('400x850')
        tkWindow.iconbitmap('.\\Sans titre - 3.ico')
        tkWindow.title('Make your choice')

        label = Label(tkWindow,text='Quel couleur voulez vous ?',
            font=('arial',22,'bold'), pady=30)
        label.pack()

        label = Label(tkWindow,text='2048 - x4',
            font=('arial',22,'bold'), pady=30)
        label.pack()

        button = Button(tkWindow,
	        text = 'Light theme',
	        command = lunchlightx4,
            font=('arial',10,'bold'))
        button.pack()

        button = Button(tkWindow,
	        text = 'Dark theme',
	        command = lunchdarkx4,
            font=('arial',10,'bold'))
        button.pack()

        label = Label(tkWindow,text='2048 - x8',
            font=('arial',22,'bold'), pady=30)
        label.pack()

        button = Button(tkWindow,
	        text = 'Light theme',
	        command = lunchlightx8,
            font=('arial',10,'bold'))
        button.pack()

        button = Button(tkWindow,
	        text = 'Dark theme',
	        command = lunchdarkx8,
            font=('arial',10,'bold'))
        button.pack()

        label = Label(tkWindow,text='Multuiplayer 2048 - x4',
            font=('arial',22,'bold'), pady=30)
        label.pack()

        button = Button(tkWindow,
	        text = 'Light theme',
	        command = lunchlightmultiplayerx4,
            font=('arial',10,'bold'))
        button.pack()

        button = Button(tkWindow,
	        text = 'Dark theme',
	        command = lunchdarkmultiplayerx4,
            font=('arial',10,'bold'))
        button.pack()

        label = Label(tkWindow,text='Multiplayer 2048 - x8',
            font=('arial',22,'bold'), pady=30)
        label.pack()

        button = Button(tkWindow,
	        text = 'Light theme',
	        command = lunchlightmultiplayerx8,
            font=('arial',10,'bold'))
        button.pack()

        button = Button(tkWindow,
	        text = 'Dark theme',
	        command = lunchdarkmultiplayerx8,
            font=('arial',10,'bold'))
        button.pack()

        label = Label(tkWindow,text='',
            font=('arial',22,'bold'), pady=5)
        label.pack()

        tkWindow.mainloop()


Interface1()#lance l'interface de sélection pour le jeu
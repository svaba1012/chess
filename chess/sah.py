import numpy as np
import pygame as pg
import time
import button as bt

pg.init() 
white = (255, 255, 255) 
X = 1350
Y = 700
startOfTableX = 375
startOfTableY = 75
ivicaPolja = 75
brojPolja = 8
undoX = startOfTableX + 12 * ivicaPolja
undoY = startOfTableY + 7 * ivicaPolja
image = pg.image.load(r'.\Sl\crnopolje.png')
image1 = pg.image.load(r'.\Sl\belopolje.png')

crnilovacnabelom = pg.image.load(r'.\Sl\crnilovacnabelom.png')
crnilovacnabelom = pg.transform.rotozoom(crnilovacnabelom, 0, 75 / 128)
crnilovacnacrnom = pg.image.load(r'.\Sl\crnilovacnacrnom.png')
crnilovacnacrnom = pg.transform.rotozoom(crnilovacnacrnom, 0, 75 / 128)
belilovacnabelom = pg.image.load(r'.\Sl\belilovacnabelom.png')
belilovacnabelom = pg.transform.rotozoom(belilovacnabelom, 0, 75 / 128)
belilovacnacrnom = pg.image.load(r'.\Sl\belilovacnacrnom.png')
belilovacnacrnom = pg.transform.rotozoom(belilovacnacrnom, 0, 75 / 128)

crnitopnabelom = pg.image.load(r'.\Sl\crnitopnabelom.png')
crnitopnabelom = pg.transform.rotozoom(crnitopnabelom, 0, 75 / 128)
crnitopnacrnom = pg.image.load(r'.\Sl\crnitopnacrnom.png')
crnitopnacrnom = pg.transform.rotozoom(crnitopnacrnom, 0, 75 / 128)
belitopnabelom = pg.image.load(r'.\Sl\belitopnabelom.png')
belitopnabelom = pg.transform.rotozoom(belitopnabelom, 0, 75 / 128)
belitopnacrnom = pg.image.load(r'.\Sl\belitopnacrnom.png')
belitopnacrnom = pg.transform.rotozoom(belitopnacrnom, 0, 75 / 128)

crnakraljicanabelom = pg.image.load(r'.\Sl\crnakraljicanabelom.png')
crnakraljicanabelom = pg.transform.rotozoom(crnakraljicanabelom, 0, 75 / 128)
crnakraljicanacrnom = pg.image.load(r'.\Sl\crnakraljicanacrnom.png')
crnakraljicanacrnom = pg.transform.rotozoom(crnakraljicanacrnom, 0, 75 / 128)
belakraljicanabelom = pg.image.load(r'.\Sl\belakraljicanabelom.png')
belakraljicanabelom = pg.transform.rotozoom(belakraljicanabelom, 0, 75 / 128)
belakraljicanacrnom = pg.image.load(r'.\Sl\belakraljicanacrnom.png')
belakraljicanacrnom = pg.transform.rotozoom(belakraljicanacrnom, 0, 75 / 128)

crnipijunnabelom = pg.image.load(r'.\Sl\crnipijunnabelom.png')
crnipijunnabelom = pg.transform.rotozoom(crnipijunnabelom, 0, 75 / 128)
crnipijunnacrnom = pg.image.load(r'.\Sl\crnipijunnacrnom.png')
crnipijunnacrnom = pg.transform.rotozoom(crnipijunnacrnom, 0, 75 / 128)
belipijunnabelom = pg.image.load(r'.\Sl\belipijunnabelom.png')
belipijunnabelom = pg.transform.rotozoom(belipijunnabelom, 0, 75 / 128)
belipijunnacrnom = pg.image.load(r'.\Sl\belipijunnacrnom.png')
belipijunnacrnom = pg.transform.rotozoom(belipijunnacrnom, 0, 75 / 128)

crnikonjnabelom = pg.image.load(r'.\Sl\crnikonjnabelom.png')
crnikonjnabelom = pg.transform.rotozoom(crnikonjnabelom, 0, 75 / 128)
crnikonjnacrnom = pg.image.load(r'.\Sl\crnikonjnacrnom.png')
crnikonjnacrnom = pg.transform.rotozoom(crnikonjnacrnom, 0, 75 / 128)
belikonjnabelom = pg.image.load(r'.\Sl\belikonjnabelom.png')
belikonjnabelom = pg.transform.rotozoom(belikonjnabelom, 0, 75 / 128)
belikonjnacrnom = pg.image.load(r'.\Sl\belikonjnacrnom.png')
belikonjnacrnom = pg.transform.rotozoom(belikonjnacrnom, 0, 75 / 128)

crnikraljnabelom = pg.image.load(r'.\Sl\crnikraljnabelom.png')
crnikraljnabelom = pg.transform.rotozoom(crnikraljnabelom, 0, 75 / 128)
crnikraljnacrnom = pg.image.load(r'.\Sl\crnikraljnacrnom.png')
crnikraljnacrnom = pg.transform.rotozoom(crnikraljnacrnom, 0, 75 / 128)
belikraljnabelom = pg.image.load(r'.\Sl\belikraljnabelom.png')
belikraljnabelom = pg.transform.rotozoom(belikraljnabelom, 0, 75 / 128)
belikraljnacrnom = pg.image.load(r'.\Sl\belikraljnacrnom.png')
belikraljnacrnom = pg.transform.rotozoom(belikraljnacrnom, 0, 75 / 128)

image = pg.transform.rotozoom(image, 0, 75 / 128)
image1 = pg.transform.rotozoom(image1, 0, 75 / 128)
display_surface = pg.display.set_mode((0, 0), pg.FULLSCREEN) 
pg.display.set_caption('Sah')
tabla = np.zeros((brojPolja, brojPolja), dtype = dict)
color = -1

for j in range(brojPolja):
    color *= -1
    for i in range(brojPolja):
        polje = {"x" : i, "y" : j, "boja" : color, "figura" : None}
        color *= -1
        tabla[j][i] = polje

class figura:
    def __init__(self, boja, poz):
        self.boja = boja
        self.poz = poz
        self.pomerena = False
        self.ziva = True
        self.stvarnoZiva = True
        poz['figura'] = self
    def getColor(self):
        return self.boja
    def kill(self):
        self.ziva = False
    def stvarnoKill(self):
        self.stvarnoZiva = False
    def isRealAlive(self):
        return self.stvarnoZiva
    def isAlive(self):
        return self.ziva
    def revive(self):
        self.ziva = True
    def getPoz(self):
        return self.poz
    def doMove(self, tabla1, potez):
        a = self.poz["x"]
        b = self.poz["y"]
        tabla1[b][a]["figura"] = None
        a = potez[0]
        b = potez[1]
        self.poz = tabla1[b][a]
        killedFig = tabla[b][a]["figura"]
        if killedFig != None:
            killedFig.kill()
        tabla1[b][a]["figura"] = self
        return killedFig
    def undoMove(self, tabla1, staraPozicija, killedFig):
        a = self.poz["x"]
        b = self.poz["y"]
        tabla1[b][a]["figura"] = killedFig
        if killedFig != None:
            killedFig.revive()
        a = staraPozicija[0]
        b = staraPozicija[1]
        self.poz = tabla1[b][a]
        tabla1[b][a]["figura"] = self
    def move(self, tabla1, razX, razY, moguciPotezi):
        for potez in moguciPotezi:
            if razX == potez[0] and razY == potez[1]:
                self.doMove(tabla1, potez)
                self.pomerena = True
                return [True, None]
        return [False, None]
    def crtaj(self, pic1, pic2, pic3, pic4):
        pozX, pozY = indexToPos(self.poz["x"], self.poz["y"])
        if self.boja == 1:
            if self.poz["boja"] == 1:
                display_surface.blit(pic1, (pozX, pozY))
            else:
                display_surface.blit(pic2, (pozX, pozY))
        else:
            if self.poz["boja"] == 1:
                display_surface.blit(pic3, (pozX, pozY))
            else:
                display_surface.blit(pic4, (pozX, pozY))
    
         
def topIliLovacMove(isBishop, curX, curY, boja, tabla1, napadnutaPolja, king, skupFigura, figura):
    validMoves = []
    attackingSquares = []
    pravci = np.full(4, True, dtype = bool)
    kx = -1
    ky = -1
    for j in range(4):
        for i in range(1, 8):
            if pravci[j]:
                if isBishop:
                    newX = curX + kx * i
                    newY = curY + ky * i
                else:
                    newX = curX + ky * (j % 2) * i
                    newY = curY + ky * ((j + 1) % 2) * i
                if newX >= 0 and newY >= 0 and newX < brojPolja and newY < brojPolja:
                    polj = tabla1[newY][newX]
                    fig = polj["figura"]
                    if fig == None or fig.getColor() != boja:
                        '''
                        eatenFig = figura.doMove(tabla1, [newX, newY])
                        napadnutaPolja = allValidMoves(skupFigura, king)
                        if not king.isCheck(napadnutaPolja):
                            validMoves.append([newX, newY])
                        figura.undoMove(tabla1, [curX, curY], eatenFig)
                        '''
                        attackingSquares.append([newX, newY])
                        validMoves.append([newX, newY])
                        if fig != None:
                            pravci[j] = False
                    else:
                        pravci[j] = False
                else:
                    pravci[j] = False
        ky *= (-1 * kx)
        kx *= -1  
    return validMoves, attackingSquares
    
class lovac(figura):
    def potMove(self, tabla1, napadnutaPolja, king, skupFigura):
        curX = self.poz["x"]
        curY = self.poz["y"]
        color = self.boja
        return topIliLovacMove(True, curX, curY, color, tabla1, napadnutaPolja, king, skupFigura, self)


class top(figura):
    def potMove(self, tabla1, napadnutaPolja, king, skupFigura):
        curX = self.poz["x"]
        curY = self.poz["y"]
        color = self.boja
        return topIliLovacMove(False, curX, curY, color, tabla1, napadnutaPolja, king, skupFigura, self)
        
class kraljica(figura):
    def potMove(self, tabla1, napadnutaPolja, king, skupFigura):
        curX = self.poz["x"]
        curY = self.poz["y"]
        color = self.boja
        validMoves1, attackingSquares1 = topIliLovacMove(True, curX, curY, color, tabla1, napadnutaPolja, king, skupFigura, self)
        validMoves2, attackingSquares2  = topIliLovacMove(False, curX, curY, color, tabla1, napadnutaPolja, king, skupFigura, self)
        if validMoves2 != None:
            validMoves1.extend(validMoves2)
        if attackingSquares2 != None:
            attackingSquares1.extend(attackingSquares2)
        return validMoves1, attackingSquares1

class pijun(figura):
    def potMove(self, tabla1, napadnutaPolja, king, skupFigura):
        validMoves = []
        attackingSquares = []
        curX = self.poz["x"] 
        curY = self.poz["y"]
        boja = self.boja
        j = -1
        r = 3
        if boja == -1:
            j = 1
        if self.pomerena:
            r = 2
        newX = curX
        newY = curY
        for i in range(1, r):
            newY += j
            if i == 1:
                for brojac in range(2):
                    newX = curX + j
                    j *= -1
                    if newX >= 0 and newY >= 0 and newX < 8 and newY < 8:
                        polj = tabla1[newY][newX]
                        attackingSquares.append([newX, newY])
                        if polj["figura"] != None and polj["figura"].getColor() != boja:
                            '''
                            eatenFig = self.doMove(tabla1, [newX, newY])
                            napadnutaPolja = allValidMoves(skupFigura, king)
                            if not king.isCheck(napadnutaPolja):
                                validMoves.append([newX, newY])
                            self.undoMove(tabla1, [curX, curY], eatenFig)
                            '''
                            validMoves.append([newX, newY])
            if newY >= 0 and newY < 8:
                polj = tabla1[newY][curX]
                if polj["figura"] != None:
                    break
                
                self.doMove(tabla1, [curX, newY])
                napadnutaPolja = allValidMoves(skupFigura, king)
                if not king.isCheck(napadnutaPolja):
                    validMoves.append([curX, newY])
                self.undoMove(tabla1, [curX, curY], None)
                
                #validMoves.append([curX, newY])
        return validMoves, attackingSquares
    def move(self, tabla1, razX, razY, m):
        isItMoved, unapredi = super().move(tabla1, razX, razY, m)
        if (self.boja == 1 and self.poz["y"] == 0) or (self.boja == -1 and self.poz["y"] == 7):
            unapredi = self
        return [isItMoved, unapredi]
    
    
class konj(figura):
    def potMove(self, tabla1, napadnutaPolja, king, skupFigura):
        i = 1
        j = 2
        validMoves = []
        attackingSquares = []
        curX = self.poz["x"] 
        curY = self.poz["y"]
        boja = self.boja
        for brojac in range(2):
            for brojac1 in range(2):
                for brojac2 in range(2):
                    newX = curX + i
                    newY = curY + j
                    i *= -1
                    if newX >= 0 and newY >= 0 and newX < 8 and newY < 8:
                        polj = tabla1[newY][newX]
                        if polj["figura"] == None or polj["figura"].getColor() != boja:
                            '''
                            eatenFig = self.doMove(tabla1, [newX, newY])
                            napadnutaPolja = allValidMoves(skupFigura, king)
                            if not king.isCheck(napadnutaPolja):
                                validMoves.append([newX, newY])
                            self.undoMove(tabla1, [curX, curY], eatenFig)
                            '''
                            attackingSquares.append([newX, newY])
                            validMoves.append([newX, newY])
                j *= -1
            i, j = j, i
        return validMoves, attackingSquares

class kralj(figura):
    def potMove(self, tabla1, napadnutaPolja, king, skupFigura):
        validMoves = []
        attackingSquares = []
        curX = self.poz["x"] 
        curY = self.poz["y"]
        curPoz = [curX, curY]
        boja = self.boja
        for j in range(-1, 2):
            for i in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                newX = curX + i
                newY = curY + j
                if newX >= 0 and newY >= 0 and newX < 8 and newY < 8:
                    polj = tabla1[newY][newX]
                    if polj["figura"] == None or polj["figura"].getColor() != boja:
                        newPoz = [newX, newY]
                        if newPoz not in napadnutaPolja:
                            '''
                            eatenFig = self.doMove(tabla1, newPoz)
                            napadnutaPolja = allValidMoves(skupFigura, king)
                            if not king.isCheck(napadnutaPolja):
                                validMoves.append([newX, newY])
                            self.undoMove(tabla1, curPoz, eatenFig)
                            '''
                            attackingSquares.append([newX, newY])
                            validMoves.append([newX, newY])
        return validMoves, attackingSquares
    def isCheck(self, napPolja):
        polj = [self.poz["x"], self.poz["y"]]
        if polj in napPolja:
            return True
        return False

def allValidMoves(skupFigura, king):
    allMoves = []
    for fig in skupFigura:
        if fig.isAlive():
            vMoves = fig.potMove(tabla, [], king, [])[1]
            allMoves.extend(vMoves)
    return allMoves

    
def indexToPos(x, y):
    x = x * ivicaPolja + startOfTableX
    y = y * ivicaPolja + startOfTableY
    return x, y

def mouseClicked(first):
    mP = pg.mouse.get_pressed()[0]
    if mP and first:
        first = False
        return True, first
    elif not mP:
        first = True
        return False, first
    else:
        return False, False

def up(fig, num):
    boja = fig.getColor()
    poz = fig.getPoz()
    if num == 0:
        fig = konj(boja, poz)
    elif num == 1:
        fig = lovac(boja, poz)
    elif num == 2:
        fig = top(boja, poz)
    elif num == 3:
        fig = kraljica(boja, poz)
    return fig


def izaberiPolje(tabla1, kvadrat, potezi, izabranaFigura, turn, upgrade, bMoves, wMoves, bfigure, wfigure):  
    mousePoz = pg.mouse.get_pos()
    x = (mousePoz[0] - startOfTableX) // ivicaPolja
    y = (mousePoz[1] - startOfTableY) // ivicaPolja
    if x >= 0 and y >= 0 and x < brojPolja and y < brojPolja and upgrade == None:
        polj = tabla1[y][x]
        if izabranaFigura != None:
            if turn == -1:
                isItMoved, upgrade = izabranaFigura.move(tabla1, x, y, izabranaFigura.potMove(tabla, wMoves, kralj1, wfigure)[0])
            else:
                isItMoved, upgrade = izabranaFigura.move(tabla1, x, y, izabranaFigura.potMove(tabla, bMoves, kralj2, bfigure)[0])
            if(isItMoved):
                kvadrat, potezi= None, None
                turn *= -1
            izabranaFigura = None
        X, Y = indexToPos(x, y)
        kvadrat = (X, Y, ivicaPolja, ivicaPolja)
        izabranaFigura = polj["figura"]
        if izabranaFigura != None and izabranaFigura.getColor() == turn:
            if turn == -1:
                potezi = izabranaFigura.potMove(tabla, wMoves, kralj1, wfigure)[0]
            else:
                potezi = izabranaFigura.potMove(tabla, bMoves, kralj2, bfigure)[0]
            for potez in potezi:
                potez[0], potez[1] = indexToPos(potez[0], potez[1])
                potez.append(ivicaPolja)
                potez.append(ivicaPolja)
        else:
            potezi = None
            kvadrat = None
            izabranaFigura = None
    elif upgrade != None:
        y = mousePoz[1] - (startOfTableY + 3 * ivicaPolja)
        x = mousePoz[0] - startOfTableX
        if y > 0 and x > 0 and y < ivicaPolja * 2 and x < ivicaPolja * 8:
            upgrade = up(upgrade, x // (ivicaPolja * 2))
    else:
        kvadrat = None
        potezi = None
        izabranaFigura = None
    return [kvadrat, potezi, izabranaFigura, turn, upgrade]

def upFig(skupFigura, fig):
    skupFigura.append(fig)
    return skupFigura

def noValidMoves(skupFigura, king, napPolja, napFigure):
    for fig in skupFigura:
        if len(fig.potMove(tabla, napPolja, king, napFigure)[0]) > 0:
            return False
    return True

    
        
        
def crtajTablu(tabla1, upgrade):
    for j in range(brojPolja):
        for i in range(brojPolja):
            polj = tabla1[j][i]
            if polj['figura'] == None:
                if polj["boja"] == -1:
                    display_surface.blit(image, (indexToPos(polj["x"], polj["y"])))
                else:
                    display_surface.blit(image1, (indexToPos(polj["x"], polj["y"])))
            if type(polj["figura"]) == lovac:
                polj['figura'].crtaj(belilovacnabelom, belilovacnacrnom, crnilovacnabelom, crnilovacnacrnom)
            elif type(polj["figura"]) == top:
                polj['figura'].crtaj(belitopnabelom, belitopnacrnom, crnitopnabelom, crnitopnacrnom)
            elif type(polj['figura']) == kraljica:
                polj['figura'].crtaj(belakraljicanabelom, belakraljicanacrnom, crnakraljicanabelom, crnakraljicanacrnom)
            elif type(polj['figura']) == pijun:
                polj['figura'].crtaj(belipijunnabelom, belipijunnacrnom, crnipijunnabelom, crnipijunnacrnom)
            elif type(polj['figura']) == konj:
                polj['figura'].crtaj(belikonjnabelom, belikonjnacrnom, crnikonjnabelom, crnikonjnacrnom)
            elif type(polj['figura']) == kralj:
                polj['figura'].crtaj(belikraljnabelom, belikraljnacrnom, crnikraljnabelom, crnikraljnacrnom)
            if upgrade != None:
                pg.draw.rect(display_surface, (0, 255, 0), (startOfTableX - ivicaPolja, startOfTableY + 150, 750, 300), 0)
                if upgrade.getColor() == 1:
                    belikonjnacrnom1 = pg.transform.rotozoom(belikonjnacrnom, 0, 2)
                    belilovacnacrnom1 = pg.transform.rotozoom(belilovacnacrnom, 0, 2)
                    belitopnacrnom1 = pg.transform.rotozoom(belitopnacrnom, 0, 2)
                    belakraljicanacrnom1 = pg.transform.rotozoom(belakraljicanacrnom, 0, 2)
                else:
                    belikonjnacrnom1 = pg.transform.rotozoom(crnikonjnabelom, 0, 2)
                    belilovacnacrnom1 = pg.transform.rotozoom(crnilovacnabelom, 0, 2)
                    belitopnacrnom1 = pg.transform.rotozoom(crnitopnabelom, 0, 2)
                    belakraljicanacrnom1 = pg.transform.rotozoom(crnakraljicanabelom, 0, 2)
                yIzbor = startOfTableY + 3 * ivicaPolja
                display_surface.blit(belikonjnacrnom1, (startOfTableX, yIzbor))
                display_surface.blit(belilovacnacrnom1, (startOfTableX + ivicaPolja * 2, yIzbor))
                display_surface.blit(belitopnacrnom1, (startOfTableX + ivicaPolja * 4, yIzbor))
                display_surface.blit(belakraljicanacrnom1, (startOfTableX + ivicaPolja * 6, yIzbor))
                pg.draw.rect(display_surface, (100,0,255), (startOfTableX, yIzbor, ivicaPolja * 2, ivicaPolja * 2), 10)
                pg.draw.rect(display_surface, (100,0,255), (startOfTableX + ivicaPolja * 2, yIzbor, ivicaPolja * 2, ivicaPolja * 2), 10)
                pg.draw.rect(display_surface, (100,0,255), (startOfTableX + ivicaPolja * 4, yIzbor, ivicaPolja * 2, ivicaPolja * 2), 10)
                pg.draw.rect(display_surface, (100,0,255), (startOfTableX + ivicaPolja * 6, yIzbor, ivicaPolja * 2, ivicaPolja * 2), 10)
                display_surface.blit(text, textRect)
    pg.draw.rect(display_surface, (255, 0, 0), (undoX, undoY, ivicaPolja, ivicaPolja), 0)

def playerVsPl():
    return True

def mainMenu():
    naslov = bt.button(X / 2 - 150, 50, 300, 50, (0,0,0), "SRB SAH", 20, (255,255,255))
    p1VsP2 = bt.button(X / 2 - 150, Y / 2, 300, 50, (255,255,255), "P1 VS P2", 20, (0,0,0))
    p1VsCom = bt.button(X / 2 - 150, Y / 2 - 75, 300, 50, (255,255,255), "P1 VS COM", 20, (0,0,0))
    izlaz = bt.button(X / 2 - 150, Y / 2 + 75, 300, 50, (255,255,255), "QUIT", 20, (0,0,0))
    igraj = None
    kraj = None
    while True:
        display_surface.fill((0,0,0))
        naslov.crtaj(display_surface)
        p1VsP2.crtaj(display_surface)
        p1VsCom.crtaj(display_surface)
        izlaz.crtaj(display_surface)
        igraj = p1VsP2.buttonFunc(playerVsPl)
        kraj = izlaz.buttonFunc(playerVsPl)
        if igraj != None:
            break
        if kraj != None:
            pg.quit() 
            quit()
        for event in pg.event.get() : 
            if event.type == pg.QUIT : 
                pg.quit() 
                quit() 
            pg.display.update()
        
def gamePlVsPl():
    beleFigure = []
    crneFigure = []
    pijuni = np.zeros(16, dtype = pijun)
    for i in range(16):
        if i < 8:
            pijuni[i] = pijun(-1, tabla[1][i])
            crneFigure.append(pijuni[i])
        else:
            pijuni[i] = pijun(1, tabla[6][i - 8])
            beleFigure.append(pijuni[i])
    lovac2 = lovac(-1, tabla[0][2])    
    lovac1 = lovac(-1, tabla[0][5])
    lovac3 = lovac(1, tabla[7][2])
    lovac4 = lovac(1, tabla[7][5])
    top2 = top(-1, tabla[0][0])
    top1 = top(-1, tabla[0][7])
    top3 = top(1, tabla[7][0])  
    top4 = top(1, tabla[7][7])
    konj2 = konj(-1, tabla[0][1])    
    konj1 = konj(-1, tabla[0][6])
    konj3 = konj(1, tabla[7][1])
    konj4 = konj(1, tabla[7][6])
    kraljica1 = kraljica(-1, tabla[0][3])
    kraljica2 = kraljica(1, tabla[7][3])

    beleFigure.append(lovac4)
    beleFigure.append(lovac3)
    beleFigure.append(top3)
    beleFigure.append(top4)
    beleFigure.append(konj3)
    beleFigure.append(konj4)
    beleFigure.append(kraljica2)
    beleFigure.append(kralj2)

    crneFigure.append(lovac1)
    crneFigure.append(lovac2)
    crneFigure.append(top1)
    crneFigure.append(top2)
    crneFigure.append(konj1)
    crneFigure.append(konj2)
    crneFigure.append(kralj1)
    crneFigure.append(kraljica1)
     
    kvadrat = None
    potezi = None
    font = pg.font.Font('freesansbold.ttf', 32)
    text = font.render('Unapredite pijuna u jednu od figura', True, (0,0,255), (0,255,0))
    textSahMatB = font.render('Sah mat! Crni je pobedio! Klikni za izlaz.', True, (0,0,255), (0,255,0))
    textSahMatW = font.render('Sah mat! Beli je pobedio! Klikni za izlaz.', True, (0,0,255), (0,255,0))
    textRect = text.get_rect()
    textRect.center = (startOfTableX + 4 * ivicaPolja, startOfTableY + 2.5 * ivicaPolja)
    textRect2 = textSahMatB.get_rect()
    textRect2.center = (startOfTableX + 4 * ivicaPolja, startOfTableY + 4 * ivicaPolja)
    matW = False
    matB = False
    izabranaFigura = None
    nextTurn = 1
    upgrade = None
    prvi = True
    crniMoves = allValidMoves(crneFigure, kralj1)
    beliMoves = allValidMoves(beleFigure, kralj2)
    while True : 
        display_surface.fill(white)  
        crtajTablu(tabla, upgrade)
        mClicked, prvi = mouseClicked(prvi)
        turnCopy = nextTurn
        if mClicked and not matW and not matB:
                kvadrat, potezi, izabranaFigura, nextTurn, upgrade = izaberiPolje(tabla, kvadrat, potezi, izabranaFigura, nextTurn, upgrade, crniMoves, beliMoves, crneFigure, beleFigure)
                if upgrade != None and type(upgrade) != pijun and upgrade.getColor() == -1: 
                    crneFigure = upFig(crneFigure, upgrade)
                    upgrade = None
                elif upgrade != None and type(upgrade) != pijun and upgrade.getColor() == 1:
                    beleFigure = upFig(beleFigure, upgrade)
                    upgrade = None
                if turnCopy != nextTurn:
                    crniMoves = allValidMoves(crneFigure, kralj1)
                    beliMoves = allValidMoves(beleFigure, kralj2)
        elif matW:
            display_surface.blit(textSahMatW, textRect2)
            if mClicked:
                pg.quit() 
                quit()
        elif matB:
            display_surface.blit(textSahMatB, textRect2)
            if mClicked:
                pg.quit() 
                quit()
        if noValidMoves(crneFigure, kralj1, beliMoves, beleFigure):
            matW = True
        if noValidMoves(beleFigure, kralj2, crniMoves, crneFigure):
            matB = True
        if potezi != None:
            for potez in potezi:
                pg.draw.rect(display_surface, (0, 0, 255), potez, 5)
        if kvadrat != None:
            pg.draw.rect(display_surface, (255,0,0), kvadrat, 5)
        for event in pg.event.get() : 
            if event.type == pg.QUIT : 
                pg.quit() 
                quit() 
            pg.display.update()

mainMenu()
kralj1 = kralj(-1, tabla[0][4])
kralj2 = kralj(1, tabla[7][4])
gamePlVsPl()
    
   
    




from jedi.api.refactoring import inline

print("hello")
##
a = 2
##
from matplotlib import pyplot as plt, pyplot

x = [3, 4, 14, 67]

y = [3, 4, 44, 85]

plt.plot(x, y, color='k', linestyle='--', marker='o', label='hey')
plt.title('<3')
plt.xlabel('test en x')
plt.ylabel('test en y')
plt.legend('courbe')
plt.show()

##
# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Importation du paquet wxPython
import wx


# Création d'un nouveau cadre, dérivé du wxPython 'Frame'.
class TestFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, -1, title, pos=(-1, -1), size=(200, 100))

        # À l'intérieur du cadre, créer un panneau..
        panel = wx.Panel(self, -1)

        # Créer un texte dans le panneau
        texte = wx.StaticText(panel, -1, "Bonjour tout le monde!", wx.Point(10, 5), wx.Size(-1, -1))

        # Créer un bouton dans le panneau
        bouton = wx.Button(panel, -1, "Cliquez-moi!", wx.Point(10, 35), wx.Size(-1, -1))
        # lier le bouton à une fonction:
        self.Bind(wx.EVT_BUTTON, self.creerDiag, bouton)

    # fonction qui affiche une boîte de dialogue
    def creerDiag(self, event):
        dlg = wx.MessageDialog(self, "Merci de m'avoir cliqué, ça fait du bien.",
                               "Merci!", wx.ICON_EXCLAMATION | wx.YES_NO | wx.CANCEL)
        dlg.ShowModal()
        dlg.Destroy()


# Chaque application wxWidgets doit avoir une classe dérivée de wx.App
class TestApp(wx.App):
    def OnInit(self):
        frame = TestFrame(None, -1, "Test")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True


if __name__ == '__main__':
    app = TestApp(0)  # créer une nouvelle instance de l'application
    app.MainLoop()  # lancer l'application
##
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

##
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace((np.pi/2), 3*(np.pi/2), 60)

x = np.cos(theta)
y = np.sin(theta)

xl = np.array([0, 0])
yl = np.array([-1, 1])

plt.plot(x, y, xl, yl)
plt.axis("equal")
plt.xlim(-3,3)

plt.show()

##

import numpy as np
import matplotlib.pyplot as plt


figure = plt.figure(figsize = (5, 5))
# suppression des marges
plt.gcf().subplots_adjust(0, 0, 1, 1)
axes = figure.add_subplot(111)
# pas de cadre
axes.set_frame_on(False)
# pas de graduations d'axes
axes.xaxis.set_visible(False)
axes.yaxis.set_visible(False)
axes.add_artist(plt.Arc((2.5, 2.5), 3, 2, 20, 0, 120))

axes.show()

##
import matplotlib.pyplot as plt

xy = (2.0, 3.0)
width = 4.0
height = 5.0
angle = (0.0)
theta1 = 0.0
theta2 = 360.0
arc = plt.patches.Arc(xy, width, height, angle, theta1, theta2)
# plt.plot(arc)
plt.show()

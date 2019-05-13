from routeCalculator import pathSegment
from tkinter import * # Tkinter in python 2
import os

class GUI:
    def __init__(self,master,mapfilename,mapcoords,graph,latList,lonList):
        
        ''' INPUT: mapfilename - name of map image (in "img" folder) (.gif)
                   coords - list of latitudes and longitudes limiting the map image
                            with the following format: [left,right,bottom,top], with
                            the first two longitudes, and the last two latitudes
        '''
        self.graph,self.latList,self.lonList = graph,latList,lonList 
        
        self.risk = 0; self.comf = 0; self.path = []
        self.lat = 0; self.lon = 0; self.alpha = 0
        self.master = master
        self.master.title("Interactive Map")
        self.master.geometry("673x671")
        self.mapWidth = 673; self.mapHeight = 611
        self.left = mapcoords[0]; self.right = mapcoords[1]
        self.bottom = mapcoords[2]; self.top = mapcoords[3]
        
        self.mapname = mapfilename
        self.canvas = Canvas(master,width=self.mapWidth, height=self.mapHeight, \
        highlightbackground = 'green', highlightcolor="green",borderwidth = 10)
        self.canvas.bind("<Button-1>", self.saveCoords)
        self.canvas.bind("<Button-3>", self.printcoords)
        self.canvas.pack(side = TOP)
        gif1 = PhotoImage(file = os.path.dirname(os.getcwd()) + self.mapname)
        self.canvas.create_image(0, 0, image = gif1, anchor = NW)
       
        self.T = Text(master, height=2, width=30)
        self.T.pack(side = LEFT)
        self.b = Button(master, text="Save", command=self.savePopup, width=10)
        self.b.pack(side = LEFT)
        self.T2 = Text(master, height=2, width=30)
        self.T2.pack(side = RIGHT)
        self.b = Button(master, text="Reset", command=self.resetAll, width=10)
        self.b.pack(side = RIGHT)
        
        self.master.bind("a", self.modifAlpha)
        
        mainloop()
        
    def updateOutput1(self):
        self.T.delete(1.0, END)
        self.T.insert(INSERT, "Coords: " + str(self.coord) + '\nDiscomfort: ' + \
        str(round(self.comf,2)) + ',\tRisk: ' + str(round(self.risk,2)))
        mainloop()
    
    def updateOutput2(self):
        self.T2.delete(1.0, END)
        self.T2.insert(INSERT, "Coords: " + str(self.coord) + '\n' + 'alpha: ' + str(self.alpha))
        mainloop()  

    def saveCoords(self,event):
        [lon, lat] = [event.x,event.y]
        self.canvas.create_oval(lon-1.5, lat-1.5, lon+1.5,\
        lat+1.5, outline="red", fill=None, width=5)
        if self.lat != 0:
            start = self.coordConvertOut([self.lat,self.lon]);
            end = self.coordConvertOut([lat,lon])
            best, total, comf, risk = pathSegment(self.graph,self.latList,\
                                                self.lonList,start,end,self.alpha)
            self.comf += comf; self.risk += risk
            if len(self.path) == 0: self.path = self.path + best
            else: self.path = self.path + best[1:]
            node0 = best[0]
            for node in best[1:]:
                [lat0,lon0] = self.coordConvertIn([node0.lat,node0.lon])
                [lat1,lon1] = self.coordConvertIn([node.lat,node.lon])
                node0 = node
                self.canvas.create_line(lon0,lat0,lon1,lat1,fill="red",width=2)
        
        [self.lon,self.lat] = [event.x,event.y]
        self.coord = self.coordConvertOut([lat,lon])
        self.coord[0] = round(self.coord[0],4); self.coord[1] = round(self.coord[1],4)
        self.updateOutput1()
                  
    def printcoords(self,event):
        self.coord = self.coordConvertOut([event.y,event.x])
        self.coord[0] = round(self.coord[0],4); self.coord[1] = round(self.coord[1],4)
        self.updateOutput2()
        
    def coordConvertIn(self,coords):
        x = (coords[1]-self.left)*self.mapWidth/(self.right-self.left)
        y = self.mapHeight-(coords[0]-self.bottom)*self.mapHeight/(self.top-self.bottom)
        return [y,x]
        
    def coordConvertOut(self,coords):
        x = self.left+(self.right-self.left)*coords[1]/self.mapWidth
        y = self.bottom+(self.top-self.bottom)*(self.mapHeight-coords[0])/self.mapHeight
        return [y,x]
    
    def savePopup(self):
        self.toplevel = Toplevel(self.master)
        self.e2 = Entry(self.toplevel, width=30)
        self.e2.pack()
        self.e2.focus_set()
        self.e2.insert(END, 'userRoute' + str(round(self.risk,3)))
        self.eb2 = Button(self.toplevel, text="Save", width=15,command=self.saveRoute)
        self.eb2.pack()
        mainloop()
        
    def saveRoute(self):
        filename = self.e2.get()
        path = os.path.dirname(os.getcwd()) + '/userRoutes/'
        f = open(path + filename + '.txt','w')
        f.write('discomfort: ' + str(self.comf) + '\trisk: ' + str(self.risk) +'\n')
        for node in self.path:
            f.write(str(node) + '\t' + str(node.lat) + '\t' + str(node.lon) + '\n')
        f.close()
        self.toplevel.destroy()
    
    def setAlpha(self): # discomfort only - 0 <= alpha <= 1 - risk only
        self.alpha = float(self.e.get())
        self.toplevel.destroy()
    
    def modifAlpha(self,event):
        self.toplevel = Toplevel(self.master)
        self.e = Entry(self.toplevel)
        self.e.pack()
        self.e.focus_set()
        self.eb = Button(self.toplevel, text="set alpha", width=15,command=self.setAlpha)
        self.eb.pack()
        mainloop()
        
    def resetAll(self):
        self.risk = 0; self.comf = 0; self.path = []
        self.lat = 0; self.lon = 0; self.alpha = 0
        self.T.delete(1.0, END)
        self.T2.delete(1.0, END)
        self.canvas.delete("all")
        gif1 = PhotoImage(file = os.path.dirname(os.getcwd()) + self.mapname)
        self.canvas.create_image(0, 0, image = gif1, anchor = NW)
        mainloop()
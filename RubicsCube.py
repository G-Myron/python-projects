import random as rand
import tkinter as tk

root=tk.Tk()
root.title("Cube")
##root.geometry=('80x60+50+50')
##root.maxsize(800, 600)
##root.resizable(False, False)
F=tk.Frame(root,bg="#a0a0a8")
F.grid()

N=3#int(input("Give size: "))
SIZE=100/N
N-=1

"""Sides=["Up","Down","Right","Left","Back","Front"]"""

##print("Give the Cube's Colours:")
##for i in range(6):
##        Colour_names.append(input("{}: ".format(Sides[i])))
Colour_names=["grey","black","yellow","red","orange","blue","green"]
#Colour_names=["black","white","yellow","red","purple","blue","green"]


##def change(obj1, obj2):
##	obj1.x,obj1.y,obj1.z,obj2.x,obj2.y,obj2.z = obj2.x,obj2.y,obj2.z,obj1.x,obj1.y,obj1.z
##	obj1.pos,obj2.pos = obj2.pos,obj1.pos
##	c.print_cube()


class cube_part:
    "colours=[up,down,right,left,back,front]"
    def __init__(self, x_y_z, colours=[0,0,0,0,0,0]):
        self.pos=x_y_z
        self.x,self.y,self.z = self.pos
        self.cols=colours
        self.find_solved()
        
    def find_solved(self):
        self.solved=[1,1,1]
        if 1 in self.cols: self.solved[2]=N
        if 2 in self.cols: self.solved[2]=0
        if 3 in self.cols: self.solved[0]=N
        if 4 in self.cols: self.solved[0]=0
        if 5 in self.cols: self.solved[1]=N
        if 6 in self.cols: self.solved[1]=0
        
    def is_solved(self):
        if self.pos==self.solved:
            for i in self.cols:
                if i!=0 and self.cols[i-1]==i:
                    return True
        return False
    def rotate_colours(self, axis=0, direction=0):
        if axis==0:
            if direction==0:
##                self.cols=[self.cols[4],self.cols[5],self.cols[2],self.cols[3],self.cols[1],self.cols[0]]
                self.cols[0], self.cols[1], self.cols[4], self.cols[5] =\
                self.cols[4], self.cols[5], self.cols[1], self.cols[0]
            else:
                self.cols[0], self.cols[1], self.cols[4], self.cols[5] =\
                self.cols[5], self.cols[4], self.cols[0], self.cols[1]
        if axis==1:
            if direction==0:
                self.cols[0], self.cols[1], self.cols[2], self.cols[3] =\
                self.cols[2], self.cols[3], self.cols[1], self.cols[0]
            else:
                self.cols[0], self.cols[1], self.cols[2], self.cols[3] =\
                self.cols[3], self.cols[2], self.cols[0], self.cols[1]
        if axis==2:
            if direction==0:
                self.cols[2], self.cols[3], self.cols[4], self.cols[5] =\
                self.cols[5], self.cols[4], self.cols[2], self.cols[3]
            else:
                self.cols[2], self.cols[3], self.cols[4], self.cols[5] =\
                self.cols[4], self.cols[5], self.cols[3], self.cols[2]


class Cube:
    def __init__(self):
        self.objects=[]
        self.create_cube()
        
    def create_cube(self):
        for x in range(0,N+1):
            for y in range(0,N+1):
                for z in range(0,N+1):
##                    if x in [0,N] or y in [0,N] or z in [0,N]:
                    if x*y*z==0 or x*y*z//N:
                        colours=[0,0,0,0,0,0]
                        if z in [0,N]:
                            colours[1-z//N]=2-z//N
                        if x in [0,N]:
                            colours[3-x//N]=4-x//N
                        if y in [0,N]:
                            colours[5-y//N]=6-y//N
                        
##                        if z==N:
##                            colours[0]=1
##                        if z==0:
##                            colours[1]=2
##                        if x==N:
##                            colours[2]=3
##                        if x==0:
##                            colours[3]=4
##                        if y==N:
##                            colours[4]=5
##                        if y==0:
##                            colours[5]=6
                        obj=cube_part(x_y_z=[x,y,z], colours=colours)
                        self.objects.append(obj)
        self.print_cube()

    def initialize(self):
        for obj in self.objects:
            for i in range(6):
                if obj.cols[i]!=0:
                    test=1
                    while test>0:
                        test=0
                        got=input("{} side in {}:".format(Sides[i],obj.pos))
                        try:
                            got=int(got)
                            if got<1 or got>6:
                                print("Not valid colour...")
                                test=1
                            else: obj.cols[i]=got
                        except Exception:
                            try:obj.cols[i]=Colour_names.index(got)
                            except Exception:
                                print("Not valid colour...")
                                test=1
            obj.find_solved()
            print(obj.cols,obj.solved,obj.pos)
        self.print_cube()
    
    def rotate(self, axis=0, count=0, direction=0, printit=True):
        """axis = rotation axis (0 for x, 1 for y, 2 for z) \ncount = row, column or layer (0,1,...,N) \ndirection = which way? (0 , 1)"""
##        axes=["x","y","z"]
##        layers=["1st","2nd","3rd"]
##        direc=["+","-"]
##        print("Στροφή ως προς τον {} άξονα στο {} επίπεδο με φορά {}.".format(axes[axis],layers[count],direc[direction]))
        for obj in self.objects:
            if obj.pos[axis]==count:
                obj.rotate_colours(axis=axis,direction=direction)
                if axis==0:
                    if direction==0: obj.y, obj.z = N-obj.z, obj.y
                    else: obj.z, obj.y = N-obj.y, obj.z
                if axis==1:
                    if direction==0: obj.x, obj.z = N-obj.z, obj.x
                    else: obj.z, obj.x = N-obj.x, obj.z
                if axis==2:
                    if direction==0: obj.x, obj.y = N-obj.y, obj.x
                    else: obj.y, obj.x = N-obj.x, obj.y
                obj.pos=[obj.x,obj.y,obj.z]
        if printit: self.print_cube()
        
    def rotate_cube(self, axis=0, direction=0, printit=True):
        for n in range(N+1):
            self.rotate(axis, n, direction, False)
##            for obj in self.objects:
##                if axis==0:
##                    if direction!=0: obj.solved[1], obj.solved[2] = N-obj.solved[2], obj.solved[1]
##                    else: obj.solved[2], obj.solved[1] = N-obj.solved[1], obj.solved[2]
##                if axis==1:
##                    if direction!=0: obj.solved[0], obj.solved[2] = N-obj.solved[2], obj.solved[0]
##                    else: obj.solved[2], obj.solved[0] = N-obj.solved[0], obj.solved[2]
##                if axis==2:
##                    if direction!=0: obj.solved[0], obj.solved[1] = N-obj.solved[1], obj.solved[0]
##                    else: obj.solved[1], obj.solved[0] = N-obj.solved[0], obj.solved[1]
        if printit: self.print_cube()
    
    def randomize(self, times=100, printit=True):
        for t in range(times):
                self.rotate(rand.randint(0,2),rand.randint(0,N),rand.randint(0,1),False)
        if printit: self.print_cube()
    
    def sequence(self,movesset, inverse=False, symmetry=-1, side=0, printit=True):
        "side = [-1, 0,1,2] = [None, x,y,z]"
        moves = movesset.copy()
        
        if inverse:
            moves.reverse()
            for i in range(len(moves)):
                moves[i]=[moves[i][0],moves[i][1],1-moves[i][2]]
        
        if symmetry>-1:
            for i in range(len(moves)):
                if moves[i][0]==symmetry:
                    moves[i]=[moves[i][0],N-moves[i][1],moves[i][2]]
                else:
                    moves[i]=[moves[i][0],moves[i][1],1-moves[i][2]]
            
        for i in range(side):
            self.rotate_cube(2,0,False)
        
        for i in range(len(moves)):
            self.rotate(moves[i][0],moves[i][1],moves[i][2],False)
        
        for i in range(side):
            self.rotate_cube(2,1,False)
        
        if printit: self.print_cube()
        
    def set_in_corner(self, obj):
        if obj.pos==obj.solved and obj.cols.index(1)==0: return
        
        x,y,z=obj.solved[0],obj.solved[1],obj.solved[2]
        x0,y0,z0=obj.x,obj.y,obj.z
        
        if obj.z == z:
            self.rotate(0,x0,y0//N,False)
            self.rotate(2,obj.z,1-y0//N,False)
            self.rotate(0,x0,1-y0//N,False)
        
        if obj.z != z:
            while obj.x!=x or obj.y!=y:
                self.rotate(2,0,0,False)
            if obj.cols.index(1)==1:
                self.rotate(0,x,y//N,False)
                self.rotate(2,0,0,False)
                self.rotate(2,0,0,False)
                self.rotate(0,x,1-y//N,False)
            while obj.x!=x or obj.y!=y:
                self.rotate(2,0,0,False)
            
            while obj.pos!=[0,0,0]:
                self.rotate_cube(2,printit=False)
            
            if obj.cols.index(1)==5:
                self.rotate(2,0,0,False)
                self.rotate(0,0,0,False)
                self.rotate(2,0,1,False)
                self.rotate(0,0,1,False)
            
            elif obj.cols.index(1)==3:
                self.rotate(2,0,1,False)
                self.rotate(1,0,0,False)
                self.rotate(2,0,0,False)
                self.rotate(1,0,1,False)
            
            while obj.pos!=obj.solved:
                self.rotate_cube(2,printit=False)
            
##            if obj.cols.index(1) in [2,3]:
##                if x==y:
##                    self.rotate(2,0,1,False)
##                    self.rotate(1,y,y//N,False)
##                    self.rotate(2,0,0,False)
##                    self.rotate(1,y,1-y//N,False)
##                else:
##                    self.rotate(2,0,0,False)
##                    self.rotate(1,y,1-y//N,False)
##                    self.rotate(2,0,1,False)
##                    self.rotate(1,y,y//N,False)
##            
##            elif obj.cols.index(1) in [4,5]:
##                if x==y:
##                    self.rotate(2,0,0,False)
##                    self.rotate(0,x,x//N,False)
##                    self.rotate(2,0,1,False)
##                    self.rotate(0,x,1-x//N,False)
##                else:
##                    self.rotate(2,0,1,False)
##                    self.rotate(0,x,1-x//N,False)
##                    self.rotate(2,0,0,False)
##                    self.rotate(0,x,x//N,False)
            
        
    def set_in_side(self, obj):
        if obj.pos==obj.solved and obj.cols.index(1)==0: return
        x,y,z=obj.solved[0],obj.solved[1],obj.solved[2]
        x0,y0,z0=obj.x,obj.y,obj.z
        
        if obj.z == z:
            self.rotate(0,x0,y0//N,False)
            self.rotate(2,obj.z,1-y0//N,False)
            self.rotate(0,x0,1-y0//N,False)
        
        if obj.z == 0:
            
            while obj.x!=x or obj.y!=y:
                self.rotate(2,0,0,False)
            
            if obj.cols.index(1)==1:
                if x in [0,N]: #y==1
                    self.rotate(1,y,x//N,False)
                    self.rotate(2,0,0,False)
                    self.rotate(2,0,0,False)
                    self.rotate(1,y,1-x//N,False)
                elif y in [0,N]: #x==1
                    self.rotate(0,x,y//N,False)
                    self.rotate(2,0,0,False)
                    self.rotate(2,0,0,False)
                    self.rotate(0,x,1-y//N,False)
            
            else:
                if x in [0,N]:
                    self.rotate(2,0,0,False)
                    self.rotate(1,y,x//N,False)
                    self.rotate(2,0,1,False)
                    self.rotate(1,y,1-x//N,False)
                elif y in [0,N]:
                    self.rotate(2,0,0,False)
                    self.rotate(0,x,y//N,False)
                    self.rotate(2,0,1,False)
                    self.rotate(0,x,1-y//N,False)
            
        else:
            for i in obj.cols:
                if i>1:break
            while obj.cols[i-1]!=i:
                self.rotate(2,obj.z,0,False)
            x0,y0=obj.x,obj.y
            self.rotate(2,obj.z,0,False)
            self.rotate(2,obj.z,0,False)
            if x in [0,N]:
                self.rotate(0,x,y0//N,False)
                self.rotate(2,obj.z,0,False)
                self.rotate(2,obj.z,0,False)
                self.rotate(0,x,1-y0//N,False)
            elif y in [0,N]:
                self.rotate(1,y,x0//N,False)
                self.rotate(2,obj.z,0,False)
                self.rotate(2,obj.z,0,False)
                self.rotate(1,y,1-x0//N,False)
            
    
    def solve_top(self, printit=True):
        for obj in self.objects:
            if obj.solved[2]==N:
                # Για το κεντρικό (Για 3x3, 5x5 κλπ.) #
                if obj.cols.count(0)==5 and obj.cols.index(1)!=0:
                    if obj.cols.index(1)==1: self.sequence(movesset_centers,printit=False)
                    ind=obj.cols.index(1)
                    if ind==2:self.sequence(movesset_centers,0,0,printit=False)
                    if ind==3:self.sequence(movesset_centers,0,-1,printit=False)
                    if ind==4:self.sequence(movesset_centers,1,1,printit=False)
                    if ind==5:self.sequence(movesset_centers,1,0,printit=False)
                
                # Για τα γωνιακά #
                elif obj.cols.count(0)==3:
                    self.set_in_corner(obj)
                
                # Για τα πλευρικά # Δουλεύει μόνο για 3x3
                elif obj.cols.count(0)==4:
                    self.set_in_side(obj)
        
        if printit:self.print_cube()
    
    def solve_middle(self, printit=True):
        for obj in self.objects:
            if obj.z==1 and obj.cols.count(0)==5:
                if obj.pos!=obj.solved:#Μπορεί να κολλήσει αν δεν είναι στη σειρά τα κέντρα με z=1
                    self.rotate(2,1,0,False)
        
        for obj in self.objects:
            if obj.solved[2]==1 and obj.cols.count(0)==4 and not obj.is_solved():
                if obj.z==1:
                    if obj.pos[:2]==[0,0]: side=0
                    if obj.pos[:2]==[0,2]: side=1
                    if obj.pos[:2]==[2,2]: side=2
                    if obj.pos[:2]==[2,0]: side=3
                    self.sequence(movesset_1,0,-1,side,False)
                
                if obj.z==0:
                    for i in obj.cols[2:]:
                        if i!=0:break
                    while obj.cols[obj.cols[1]-1]!=i:
                        self.rotate(2,0,0,False)
                    
                    side=obj.y+2*(obj.x//N)
                    self.rotate(2,0,0,False)
                    self.rotate(2,0,0,False)
                    
                    self.sequence(movesset_1,1,0,side,False)
                    if not obj.is_solved():
                        self.sequence(movesset_1,0,0,side,False)
                        self.sequence(movesset_1,1,-1,side,False)
            
        if printit:self.print_cube()
    
    def correct_bcorners(self, corners):
        not_list=[]
        test=0
        while test<2:
            test=0
            for obj in corners:
                if obj.pos==obj.solved:
                    if obj in not_list: not_list.remove(obj)
                    test+=1
                elif obj not in not_list: not_list.append(obj)
            if test<2:
                self.rotate(2,0,0,False)
            
        if test==2:
            obj1,obj2 = not_list[0],not_list[1]
            if obj1.x != obj2.x and obj1.y != obj2.y:
                test=0
                self.sequence(movesset_4, printit=False)
        
            if obj1.x == obj2.x:
                self.sequence(movesset_4,0,(obj1.x//N)-1, printit=False)
            else:#obj1.y == obj2.y
                self.sequence(movesset_4,0,-(obj1.y//N),1, printit=False)
                
            if test==0:
                self.sequence(movesset_4,1, printit=False)
        
    def solve_bcorners(self, corners):
        not_list=[0,0,0,0]
        while len(not_list)>2:
            not_list=[]
            for obj in corners:
                if obj.is_solved():
                    if obj in not_list: not_list.remove(obj)
                elif obj not in not_list: not_list.append(obj)
            if len(not_list)>2:
                self.sequence(movesset_2_2, printit=False)
        
        if len(not_list)==3:
            print("Problem... not_list has 3")
            for obj in corners:
                if obj not in not_list:
                    times=0
                    while obj1.pos != [N,N,0]:
                        times+=1
                        self.rotate(2, printit=False)
                    self.sequence(movesset_6)
                    for i in range(times):
                        self.rotate(2,0,1, printit=False)
                    self.solve_bcorners(corners)
        
        if len(not_list)==2:##May have problems
            obj1,obj2 = not_list[0],not_list[1]
            if obj1.x!=obj2.x and obj1.y!=obj2.y:
                self.sequence(movesset_2,0,0, printit=False)
                self.sequence(movesset_2, printit=False)
                self.solve_bcorners(corners)
                
            if obj1.x==obj2.x:
                x=obj1.x
                while obj1.cols[1]!=2:
                    self.sequence(movesset_2,x,0, printit=False)
                    self.sequence(movesset_2,x, printit=False)
            if obj1.y==obj2.y:
                self.rotate(2,printit=False)
                x=obj1.x
                while obj1.cols[1]!=2:
                    self.sequence(movesset_2,x,0, printit=False)
                    self.sequence(movesset_2,x, printit=False)
                self.rotate(2,0,1,printit=False)
            
        if len(not_list)==1:
            print("...Solve_bcorners")
        
    def solve_bsides(self,sides):
        if not sides: return
        
        wrong_cols=[0,0,0,0]
        while len(wrong_cols)==4:
            wrong_cols=[]
            for obj in sides:
                if obj.cols[1]!=2:wrong_cols.append(obj)
            if len(wrong_cols) == 4:
                self.sequence(movesset_3,printit=False)
        
        if len(wrong_cols) in [1,3]:
            print("Problem... WOW!")
            return
        
        if len(wrong_cols)==2:
            obj1,obj2 = wrong_cols[0],wrong_cols[1]
            
            if obj1.x==obj2.x:
                self.sequence(movesset_5,printit=False)
            if obj1.y==obj2.y:
                self.sequence(movesset_5,0,-1,1,printit=False)

            times=0
            while obj1.y != N:
                times+=1
                self.rotate(2, printit=False)
            if obj2.x==0:
                self.sequence(movesset_3,1, printit=False)
            elif obj2.x==N:
                self.sequence(movesset_3,0, printit=False)
            for i in range(times):
                self.rotate(2,0,1, printit=False)
            
        solved=[]
        while solved==[]:
            for obj in sides:
                if obj.is_solved():
                    solved.append(obj)
            if solved==[]:
                self.sequence(movesset_5,printit=False)
        
        if len(solved)!=4: obj=solved[0]
        else: return
        
        for obj1 in sides:
            if obj1 != obj:break
        
        while obj1.pos!=obj1.solved:
            times=0
            while obj.y != N:
                times+=1
                self.rotate(2, printit=False)
            self.sequence(movesset_5,printit=False)
            for i in range(times):
                self.rotate(2,0,1, printit=False)
        
    def solve_bottom(self,printit=True):
        corners,sides=[],[]
        for obj in self.objects:
            if obj.solved[2]==0:
                if obj.cols.count(0)==3: corners.append(obj)
                if obj.cols.count(0)==4: sides.append(obj)
        
        self.correct_bcorners(corners)
        self.solve_bcorners(corners)
        self.solve_bsides(sides)
    
    def print_cube(self):
        for obj in self.objects:
            #print("Position:",obj.pos,"\tColours:",obj.cols)
            
            if obj.z==N:
                F_=tk.Frame(F,bg=Colour_names[obj.cols[0]])
                F_.grid(ipadx=SIZE,ipady=SIZE,row=(N+1)-1- obj.y,column=(N+1)+ obj.x)
            if obj.z==0:
                F_=tk.Frame(F,bg=Colour_names[obj.cols[1]])
                F_.grid(ipadx=SIZE,ipady=SIZE,row=2*(N+1)+ obj.y,column=(N+1)+ obj.x)
            if obj.x==N:
                F_=tk.Frame(F,bg=Colour_names[obj.cols[2]])
                F_.grid(ipadx=SIZE,ipady=SIZE,row=2*(N+1)-1- obj.z,column=2*(N+1)+ obj.y)
            if obj.x==0:
                F_=tk.Frame(F,bg=Colour_names[obj.cols[3]])
                F_.grid(ipadx=SIZE,ipady=SIZE,row=2*(N+1)-1- obj.z,column=(N+1)-1- obj.y)
            if obj.y==N:
                F_=tk.Frame(F,bg=Colour_names[obj.cols[4]])
                F_.grid(ipadx=SIZE,ipady=SIZE,row=2*(N+1)-1- obj.z,column=4*(N+1)- obj.x)
            if obj.y==0:
                F_=tk.Frame(F,bg=Colour_names[obj.cols[5]])
                F_.grid(ipadx=SIZE,ipady=SIZE,row=2*(N+1)-1- obj.z,column=(N+1)+ obj.x)
        
    def solve(self, printit=True):  #Για 2x2 και 3x3
        self.solve_top(False)
        self.solve_middle(False)
        self.solve_bottom(False)
        if printit:self.print_cube()


movesset_centers=[[0,int(N/2),0],[2,int(N/2),0],[0,int(N/2),1],[2,int(N/2),1]] #Μόνο για περιττές διαστάσεις. πχ 3x3

movesset_1=[[0,0,0],[2,0,1],[0,0,1],[2,0,1],[1,0,0],[2,0,0],[1,0,1]]
movesset_2=[[0,0,0],[2,0,0],[0,0,1],[2,0,0],[0,0,0],[2,0,1],[2,0,1],[0,0,1]]
movesset_2_2=[[0,0,0],[2,0,0],[0,0,1],[2,0,0],[0,0,0],[2,0,1],[0,0,1],[2,0,0],[0,0,0],[2,0,1],[2,0,1],[0,0,1]]
movesset_3=[[0,1,0],[2,0,0],[0,1,1],[2,0,1],[2,0,1],[0,1,0],[2,0,0],[0,1,1]]

movesset_4=[[0,0,0],[2,0,0],[0,0,1],[2,0,1],[0,0,0],[2,0,0],[0,0,1],[1,0,0],[2,0,1],[1,0,1],[2,0,0],[2,0,0],[0,0,0],[2,0,1],[0,0,1]] #If 6 times, only sides change
movesset_5=[[0,1,0],[2,0,0],[2,0,0],[0,1,1],[2,0,0],[0,1,0],[2,0,0],[2,0,0],[0,1,1],[2,0,0],[0,1,0],[2,0,0],[2,0,0],[0,1,1]] #down sides
movesset_6=[[0,0,0],[2,0,0],[0,0,1],[2,0,1],[0,0,0],[2,0,0],[0,0,1],[1,0,0],[2,0,1],[1,0,1],[2,0,0],[2,0,0],[0,0,0],[2,0,1],[0,0,1]]
movesset_7=[[0,0,0],[2,0,0],[0,0,1],[0,2,0],[2,0,1],[0,2,1],[2,0,1],[0,2,0],[2,0,0],[2,0,0],[0,2,1],[1,0,0],[2,0,0],[1,0,1]]
movesset_8=[[1,0,1],[0,0,0],[2,0,1],[0,0,1],[1,0,0],[0,2,0],[2,0,0],[0,2,1]]
movesset_9=[[0,1,0],[2,0,1],[0,1,1],[1,1,0],[2,0,0],[1,1,1],[2,0,0],[2,0,0],[1,1,0],[2,0,0],[1,1,1],[0,1,0],[2,0,0],[0,1,1]]

movesset__=[[0,0,0],[2,0,0],[0,0,1],[2,0,1],[0,0,0],[2,0,0],[0,0,1],[1,0,0],[2,0,1],[1,0,1],[2,0,0],[2,0,0],[0,0,0],[2,0,1],[0,0,1]]
movesset__1=[[0,0,0],[2,0,0],[0,0,1],[2,0,1],[0,0,0],[2,0,0],[0,0,1],[1,0,0],[2,0,1],[1,0,1],[2,0,1],[0,0,0],[2,0,1],[2,0,1],[0,0,1]]

movesset_new=[[0,1,0],[2,0,1],[0,2,0],[2,0,0],[0,1,1],[2,0,1],[0,2,1],[2,0,0]]




c=Cube()

def test(times=1):
    for i in range(times):
        c.randomize(printit=False)
        c.solve(False)
        for obj in c.objects:
            if not obj.is_solved():
                c.print_cube()
                return False
    return True

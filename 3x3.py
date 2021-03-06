class square:
    def __init__(self, a, b, c, d, e, f, g, h,i):
        self.list_all = [a, b, c, d, e, f, g ,h, i]
        # for nb in self.list_all:
        tent = False
        if len(self.list_all) != 9:
            print("Length of the list is wrong")
            tent = True
        while tent:
            break
##        for nb in self.list_all:
##            if any([nb not in range(0, 10), str(nb).isalpha()]):
##                print("one or more elements are incorrects" + str(self.list_all))
##                break
# TODO : corrigez les fautes d'orthographe
# TODO : changer les liste en generator
# TODO : mettre à jour tous les 4 en 9, et les 2 en 3
class grid:
    def __init__(self, sq1, sq2, sq3, sq4,sq5, sq6, sq7, sq8, sq9):
        self.double_looper=0
        self.counter=0

        self.list_init = [sq1.list_all,
                          sq2.list_all,
                          sq3.list_all,
                          sq4.list_all,
                          sq5.list_all,
                          sq6.list_all,
                          sq7.list_all,
                          sq8.list_all,
                          sq9.list_all]

        self.MyGrid = {}
        for x in range(0, 9):
            """going throught the squares"""
            for y in range(0, 9):
                """going throught each element of the square"""
                aa = eval(f"{y}//3") + eval(f"({x}//3)*3")
                ab = eval(f"{y}%3") + eval(f"({x}%3)*3")
                ref = str(aa) + "-" + str(ab)
                self.MyGrid[ref] = self.list_init[x][y]

        sorted_keys=[*self.MyGrid.keys()]
        sorted_keys.sort()
        NewGrid={}
        for i in sorted_keys:
            NewGrid[i]=self.MyGrid[i]

        self.MyGrid=NewGrid
        print(f"The initial grid was : {self.MyGrid}")
        
        self.list_lines = [[*"l" * 9], [*"l" * 9], [*"l" * 9],
                           [*"l" * 9],[*"l" * 9], [*"l" * 9],
                           [*"l" * 9], [*"l" * 9], [*"l" * 9]]
        
        self.list_cols = [[*"c" * 9], [*"c" * 9], [*"c" * 9],
                          [*"c" * 9],[*"c" * 9], [*"c" * 9],
                          [*"c" * 9],[*"c" * 9], [*"c" * 9]]
        
        self.list_sqs = [[*"s" * 9], [*"s" * 9], [*"s" * 9],
                         [*"s" * 9], [*"s" * 9], [*"s" * 9],
                         [*"s" * 9], [*"s" * 9], [*"s" * 9]]

        self.list_unks = []
        self.creations()

    def creations(self):
        #Dynamic creation based on self.MyGrid
        """creation of lines"""
        for i in self.MyGrid:
            ii = i.split("-")
            self.list_lines[int(ii[0])][int(ii[1])] = self.MyGrid[i]
 
        """creation of columns"""
        for ex, et, ey in self.MyGrid:
            self.list_cols[int(ey)][int(ex)] = self.MyGrid[ex + et + ey]
 
        """creation of squares"""
        for ex, et, ey in self.MyGrid:
            sqi = ((int(ex) // 3) * 3) + (int(ey) // 3)
            sqii = ((int(ex) % 3) * 3) + (int(ey) % 3)
            self.list_sqs[sqi][sqii] = self.MyGrid[ex + et + ey]
 

        """creation of list of keys with unknown values"""
        list_keys = [*self.MyGrid.keys()]
        list_values = [*self.MyGrid.values()]
        for n, i in enumerate(list_values):
            if i == 0:
                self.list_unks.append(list_keys[n])

    def update_lists(self):
        """we reset self.list_unks because it uses the append function"""
        self.list_unks = []
        self.creations()

    def fill_easy(self):
        # print("List of unks :")
        # print(self.list_unks)
        if self.double_looper>=2:
            print('WE STOP. Cannot find solution')
            print('the intermediate grid :')
            print(self.MyGrid)
            print('the potentials:')
            print(self.dict_unks)
            self.force_fill()
            return
        
        self.filled_counter = 0
        self.answered=[]
        for i in self.list_unks:
            # print(f"Now we check : {i}")
            # print(nb_unk_line,nb_unk_col,nb_unk_sq)

            xy = i.split("-")
            mycell = self.MyGrid[i]
            myline = self.list_lines[int(xy[0])]
            mycol = self.list_cols[int(xy[1])]
            mysq = eval("self.list_sqs[" + str(eval(f"(({xy[0]}//3)*3)+({xy[1]}//3)")) + "]")

            nb_unk_line = myline.count(0)
            nb_unk_col = mycol.count(0)
            nb_unk_sq = mysq.count(0)

            if nb_unk_line == 1:
                answer = 10 - sum(myline)
                self.MyGrid[i] = answer
                self.answered.append(i)
                self.filled_counter += 1
                print(f"filled line {i}" + "=" + f"{answer}")
            if nb_unk_col == 1:
                answer = 10 - sum(mycol)
                self.MyGrid[i] = answer
                self.answered.append(i)
                self.filled_counter += 1
                print(f"filled col {i}" + "=" + f"{answer}")
            if nb_unk_sq == 1:
                #print(f"my sq : {mysq}")
                answer = 10 - sum(mysq)
                self.MyGrid[i] = answer
                #print(f"number of unk : {nb_unk_sq}")
                self.answered.append(i)
                self.filled_counter += 1
                print(f"filled sq {i}" + "=" + f"{answer}")

        for answered in self.answered:
            if answered in self.list_unks:
                self.list_unks.remove(answered)

        # print("Grid filled in function : ")
        # print(self.MyGrid)
        self.update_lists()

        if len(self.list_unks) == 0:
            print("The Grid has been completed")
            print(self.MyGrid)
        elif self.filled_counter == 0 :
            # launch fill_hard
            print("No cell were filled.")
            if self.double_looper<=1:
                self.double_looper+=1
            pass
            self.fill_complexe()
        else:
            print(f"{self.filled_counter} cell filled. Here we go again.")
            # print("Grid filled in function : ")
            # print(self.MyGrid)
            if self.double_looper>0:
                self.double_looper-=1
            self.answered=[]
            self.fill_easy()


    def fill_complexe(self):
        print("Let's check the complex ones.")

        #create a dict of potential values for unks

        self.dict_unks={}
        for unk in self.list_unks:
            self.dict_unks[unk]=[]

#        print(self.dict_unks)

        for i in self.list_unks:
            xy = i.split("-")
            mycell = self.MyGrid[i]
            myline = self.list_lines[int(xy[0])]
            mycol = self.list_cols[int(xy[1])]
            mysq = eval("self.list_sqs[" + str(eval(f"(({xy[0]}//3)*3)+({xy[1]}//3)")) + "]")

            sudoku_num=[*range(1,10)]

            # print("My line")
            # print(myline)

            for num in sudoku_num:
                if num not in myline:
                    if num not in self.dict_unks[i]:
                        self.dict_unks[i].append(num)
                        #print(f"We add {num} to {i} as a possibility")
            for num in sudoku_num:
                if num not in mycol:
                    if num not in self.dict_unks[i]:
                        self.dict_unks[i].append(num)
                        #print(f"We add {num} to {i} as a possibility")
            for num in sudoku_num:
                if num not in myline:
                    if num not in self.dict_unks[i]:
                        self.dict_unks[i].append(num)
                        #print(f"We add {num} to {i} as a possibility")
        print('potentials before checking :')
        print(self.dict_unks)
        #we check if any of the possibilities already exists in other line or col or square range
        for i in self.dict_unks:
            xy = i.split("-")
            mycell = self.MyGrid[i]
            myline = self.list_lines[int(xy[0])]
            mycol = self.list_cols[int(xy[1])]
            mysq = eval("self.list_sqs[" + str(eval(f"(({xy[0]}//3)*3)+({xy[1]}//3)")) + "]")

            for ii in self.dict_unks[i]:
                if ii in myline:
                    #print("found one!")
                    try:
                        self.dict_unks[i].remove(ii)
                    except:
                        continue
                        #print("Already removed")
                if ii in mycol:
                    #print("found one!")
                    try:
                        self.dict_unks[i].remove(ii)
                    except:
                        continue
                        #print("Already removed")
                if ii in mysq:
                    #print("found one!")
                    try:
                        self.dict_unks[i].remove(ii)
                    except:
                        continue
                        #print("Already removed")

 #       print(f"Potentials are : {self.dict_unks}")

        #Now we fill the cells that has only 1 potential
        for k,v in self.dict_unks.items():
            if len(v)==1:
                self.MyGrid[k]=v[0]

        self.update_lists()

        if len(self.list_unks) == 0:
            print("The Grid has been completed")
            print(self.MyGrid)
        else:
            #and run again fill_easy because new cells has been filled
            self.fill_easy()

    def validation(self,grid,num,key):
        
        x,e,y=key
        sqi = ((int(x) // 3) * 3) + (int(y) // 3)
        sqii = ((int(x) % 3) * 3) + (int(y) % 3)
        mysq = eval("self.list_sqs[" + str(eval(f"(({int(x)}//3)*3)+({int(y)}//3)")) + "]")
        
        checking=[num not in self.list_lines[int(x)],
                num not in self.list_cols[int(y)],
                num not in mysq]
        return all(checking)
        
    def force_fill(self):
        self.update_lists()
        
        if len(self.list_unks)==0 :
            print('finished')
            print(f"FINAL : {self.MyGrid}")
            return True
        
        
        for key in self.list_unks:
            #print(key)
            x,e,y=key
            sqi = ((int(x) // 3) * 3) + (int(y) // 3)
            sqii = ((int(x) % 3) * 3) + (int(y) % 3)
            print(f'Potentials for {key} are {self.dict_unks[key]}')
            for potential in self.dict_unks[key]:
                print(f'lets try {key} : {potential}')
            
                if self.validation(self.MyGrid,potential,key):
                    self.MyGrid[key]=potential
                    self.list_lines[int(x)][int(y)]=potential
                    self.list_cols[int(y)][int(x)]=potential
                    self.list_sqs[sqi][sqii]=potential
                    self.counter+=1
                    print('yes')
                    
                    if self.force_fill():
                        return True

                    self.MyGrid[key]=0
                    self.list_lines[int(x)][int(y)]=0
                    self.list_cols[int(y)][int(x)]=0
                    self.list_sqs[sqi][sqii]=0
                    print(f'NO for {key} : {potential}')
                print(f'the end of test for {key} : {potential}')
            print(f'the end for potentials : {key}')
            return False
        print('The grid')
        print(self.MyGrid)
        return False
            

                    
                

            




sq1 = square(0,0,0,0,8,0,6,0,2)
sq2 = square(0,0,0,2,0,7,0,4,0)
sq3 = square(2,0,0,0,9,0,5,0,0)
sq4 = square(1,7,0,5,0,0,0,0,9)
sq5 = square(0,6,0,9,0,1,0,2,0)
sq6 = square(0,5,0,3,0,0,0,4,0)
sq7 = square(0,0,5,0,9,0,0,0,6)
sq8 = square(0,0,2,4,3,0,0,0,0)
sq9 = square(6,0,3,0,7,0,0,2,0)
g = grid(sq1, sq2, sq3, sq4, sq5, sq6, sq7, sq8, sq9)
g.fill_easy()


max_rows = 8
max_cols = 4
matrix = [[1] * max_cols for _ in range(max_rows)]
matrix[2][2] = 0
matrix[3][0] = 0
matrix[3][1] = 0
matrix[4][2] = 0
matrix[6][1] = 0
matrix[7][1] = 0
matrix[1][1] = 0


for r in matrix:
    print(r)


def move_robot(matrix,max_lin,max_col):
    caminho=[(0,0)]
    lin,col=0,0
    
    while True:

        while  lin <=max_lin-1 and col <=max_col-1  and  (matrix[lin+1][col] !=0 or matrix[lin][col+1] !=0):
            
           
            if matrix[lin+1][col] != 0:
                lin+=1
            else: 
                col+=1

            pos=(lin,col)
            caminho.append(pos)
        
        x,y=lin,col
        
        while lin==max_lin and matrix[lin][y]==1 and y<max_col:
            y+=1
            caminho.append((lin,y))

        while col==max_col and matrix[y][col]==1 and x<max_lin:
            x+=1
            caminho.append((x,col))

        
        if caminho[-1] == (max_lin,max_col):
            break

        else:
            temp=caminho[-1]
            matrix[temp[0]][temp[1]]=0
            caminho_inv=caminho[::-1]
            p=False
            for k in range(len(caminho_inv)-1):
                var_act=caminho_inv[k]
                var_ant=caminho_inv[k+1]
                p=True
                diff_lin,diff_col=var_act[0]-var_ant[0], var_act[1]-var_ant[1]
                
                if diff_lin==1 and  0<= var_ant[1]+1 <= max_col  and matrix[var_ant[0]][var_ant[1] + 1] != 0:
                    pos_ini_x,pos_ini_y=var_ant[0],var_ant[1]
                    a=k
                    break
                elif diff_col==1 and  0<= var_ant[0]+1 <= max_lin and  matrix[var_ant[0]+1][var_ant[1]] != 0:
                    pos_ini_x,pos_ini_y=var_ant[0],var_ant[1]
                    a=k
                    break
                else:
                    matrix[var_act[0]][var_act[1]]=0
            
            if p==False:
                return 'não há caminhos possíveis'
            else:
                caminho=caminho[:-a-1]
                lin,col=pos_ini_x,pos_ini_y
            
            
        

    return caminho 



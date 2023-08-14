class TicTacToe:
    def __init__(self):
        self.board=["|-|","-","|-|","|-|","-","|-|","|-|","-","|-|"]
        self.board_memory = [0,0,0,0,0,0,0,0,0]
        self.board_occupied = [False,False,False,False,False,False,False,False,False]

    def print_board(self):
        # count=0
        print(self.board[0], self.board[1],self.board[2], sep=' ')
        print(self.board[3], self.board[4],self.board[5], sep=' ')
        print(self.board[6], self.board[7],self.board[8], sep=' ')


    def reset(self):
        self.board=["|-|","-","|-|","|-|","-","|-|","|-|","-","|-|"]
        self.board_memory = [0,0,0,0,0,0,0,0,0]
        self.board_occupied = [False,False,False,False,False,False,False,False,False]

    def check_for_condition_horizontal(self,board):
        test_arr=[]
        # print(len(board))

        def helper_(i,board):
            # print(board)
            test_arr=[]
            test_arr.append(board[i])
            test_arr.append(board[i+1])
            test_arr.append(board[i+2])
            
            if test_arr[0]==test_arr[1] and test_arr[1]==test_arr[2] and test_arr[0]==test_arr[2] and 0 not in test_arr:
                # print("asfdafd")
                # print(test_arr)
                test_arr= set(test_arr)
                if len(test_arr)==1:
                    if list(test_arr)[0]==1:
                        print(f"Winner X")
                    else:
                        print(f"Winner O")
                    print("Game Over")
                    return True


        ret=helper_(0,board)
        if ret:
            return ret
        
        ret=helper_(3,board)
        if ret:
            return ret
        
        ret=helper_(6,board)
        if ret:
            return ret
    def check_for_condition_vertical(self,board):
        # test_arr=[]
        # print(len(board))
        def helper_(i,board):
            test_arr=[]
            test_arr.append(board[i])
            test_arr.append(board[i+3])
            test_arr.append(board[i+6])
        
            if test_arr[0]==test_arr[1] and test_arr[1]==test_arr[2] and test_arr[0]==test_arr[2] and 0 not in test_arr:
                # count=0
                test_arr= set(test_arr)
                if len(test_arr)==1:
                    if list(test_arr)[0]==1:
                        print(f"Winner X")
                    else:
                        print(f"Winner O")
                    print("Game Over")
                    return True

        ret=helper_(0,board)
        if ret:
            return ret
         
        ret = helper_(1,board)
        if ret:
            return ret
                
        ret=helper_(2,board)
        if ret:
            return ret
 
    def check_for_condition_diagonal(self,board):

        if board[0]==board[4] and board[4]==board[8] and board[0]==board[8] and board[0] != 0 and board[4] != 0 and board[8] != 0:
            if board[0]==1:
                print(f"Winner X")
            else:
                print(f"Winner O")
            return True
        if board[2]==board[4] and board[4]==board[6] and board[2]==board[6] and board[2] != 0 and board[4]!=0 and board[6]!=0:
            if board[0]==1:
                print(f"Winner X")
            else:
                print(f"Winner O")
            return True
        

    def check_for_win(self):
        check_for_win_board = self.board_memory

        ret=self.check_for_condition_horizontal(check_for_win_board)
        if ret:
            return ret
        ret=self.check_for_condition_vertical(check_for_win_board)
        if ret:
            return ret
        ret=self.check_for_condition_diagonal(check_for_win_board)
        if ret:
            return ret
        



    def update(self,postion,player_number):
        # print("player 1 is X")
        # print("player 2 is O")
        if player_number==1:
            self.board[postion-1] = "|X|"
            self.board_memory[postion-1]=1
            self.board_occupied[postion-1]=True
        else:
            self.board[postion-1] = "|O|"
            self.board_memory[postion-1] = 2
            self.board_occupied[postion-1]=True

        
        # print(self.board)
        ret=self.check_for_win()
        if ret:
            return ret

    def start(self):


        print("Welcome to the TIC TAC TOE game")
        print("player 1 is X")
        print("player 2 is O")
        player=True
        while True:
         
            if player:
                player_number=1
            else:
                player_number=2
            
            self.print_board()
            start=input(f"Choose a postion on the board (1-9)  now it is player {player_number}'s turn!!!")

            try:
                if int(start)>0 and int(start)<=9:
                    position=int(start)

                    # print("sdfdsfs ")
                    if self.board_memory[position-1]:
                        print("Cannot reoccupy position!!!")
                        continue
                    if self.update(position,player_number):
                        response=input("Do you want to play another round? Y/N : (Enter only Y/N!)")
                        try:
                            if not str(response)=="Y" or not str(response)=="N":
                                pass
                            if response=="Y":
                                self.reset()
                            elif response=="N":
                                break
                        except:
                            print("Goodbye!")
                            # break
                            

                     
                        
                        
           
                else:
                    print("Enter a valid number between 1-9!")            
            except:
                print("Enter a valid number between 1-9!")

            player=not player

    




if __name__=="__main__":
   t = TicTacToe()
   t.start()
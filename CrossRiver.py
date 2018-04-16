edgeFlag1=True #河岸标识符现在在A岸
edgeFlag2=False#河岸标识符 与上面一样 用这两个就可以表示船
sheep1=[1,1,1]#河岸A的羊
sheep2=[]#河岸B的狼
wolf1=[1,1,1]#河岸A的狼
wolf2=[]#河岸B的狼
GameFlag=True#游戏开始标志
edge1="A"#用来识别A岸
edge2="B"#用来识别B岸
step=0
winner_list=[]
winner={}


def oprate(SheepA, SheepB, WolfA, WolfB,EdgeFlag1,EdgeFlag2):#键入操作进行游戏

    global edgeFlag1,edgeFlag2,step
    for i in range(2):
        op=input("请输入你的操作：")
        push(op,SheepA,SheepB,WolfA,WolfB)#对当前操作进行操作
    # judge(EdgeFlag1,SheepA,SheepB,WolfA,WolfB)#判断对岸状态
    # EdgeFlag1=False  #判断完置反 表示船走了
    # EdgeFlag2=True
    edgeFlag1 = not EdgeFlag1
    edgeFlag2 = not EdgeFlag2
    step += 1
    return

def push (Op,SheepA,SheepB,WolfA,WolfB):
    if Op =="S": #输入S进行操作
        SheepA.pop() #当前河岸S-1
        SheepB.append(1)#对岸+1
        return
    elif Op=="W":
        WolfA.pop()
        WolfB.append(1)
        return
    elif Op=="N":#可以不上元素返回
        return

def judge(SheepA,WolfA,SheepB,WolfB):
    global GameFlag
    if (len(SheepA)<len(WolfA) or len(SheepB)<len(WolfB)) and len(SheepA)!=0 and len(SheepB)!=0 :
        print("你输了")
        GameFlag=False
    elif len(SheepA)==0 and len(WolfA)==0:
        print("你赢了")
        fo = open("winners.txt", "a", encoding="UTF-8")
        winner["姓名："]=input("请输入你的姓名：")
        winner["步数"]=step
        fo.write(winner)
        fo.close()
        fo = open("winners.txt","r+",encoding="UTF-8")
        winner_list=fo.readlines()
        winner_list.sort(key="步数")
        for onewinner in winner_list:
            fo.write(onewinner)
        fo.close()
        GameFlag=False
    else:
        print("请继续")
        return
# def iscontinue(edge,list):
#     if edege
#     if list.length==0:
#         print("此岸已没有可操作的了")
#     else:
#         return
def show(EdgeFlag1,EdgeFlag2,Edge1,Edge2,Sheep1,Sheep2,Wolf1,Wolf2):
    print("当前状态是：")
    for wolf in wolf1:
        print("""                            *    *                 
                             *  *                  
                              **                   
                             *  **                 
                            *    **                
                 ***********      **               
             ****************                      
            ******************                     
          *   * *           *  *                   
        *      *  *           *   *                
                *   *          *    *              
                 *   *          *     *            
        """)



    for sheep in sheep1:
        print("""                                      *  *         
                ************          ****         
             *******************    **  ***        
           **********************  **     ***      
          *************************                
           **********************                  
             ******************                          
            *  * *********** * *                   
           *    *           *   *                  
        """)
    print("河岸%s有%d只羊%d只狼" % (Edge1, len(Sheep1), len(Wolf1)))
    print("______________________________________________________")
    for wolf in wolf2:
        print("""                            *    *                 
                                *  *                  
                                 **                   
                                *  **                 
                               *    **                
                    ***********      **               
                ****************                      
               ******************                     
             *   * *           *  *                   
           *      *  *           *   *                
                   *   *          *    *              
                    *   *          *     *            
           """)
    for sheep in sheep2:
        print("""                                      *  *         
                ************          ****         
             *******************    **  ***        
           **********************  **     ***      
          *************************                
           **********************                  
             ******************                          
            *  * *********** * *                   
           *    *           *   *                  
        """)
    print("河岸%s有%d只羊%d只狼" % (Edge2, len(Sheep2), len(Wolf2)))

    if(EdgeFlag1==True):
        print("""现在船在   A岸""")
    elif (EdgeFlag2==True):
        print("""现在船在   B岸""")
def main():
    print("""欢迎进入狼羊过河游戏
        游戏规则：现在在河岸A有3只羊和3只狼要都过河，但是河岸边只有一艘小船，小船自多只能承载两个单位，且必须至少有一个单位在船上时小船才会开动。
                 当船两岸任意一岸的羊的数量小于狼的数量时，羊就会被吃掉游戏失败。怎样做才能让所有的羊和狼都过河呢？
        操作提示：
                S：让此岸的羊上船
                W：让此岸的狼上船
                N：不上船""")
    fo = open("winners.txt", "ab+")
    fo.close()
    show(edgeFlag1, edgeFlag2, edge1, edge2, sheep1, sheep2, wolf1, wolf2)
    while GameFlag == True:
        print("步数：%d"%step)
        if edgeFlag1==True:
            oprate(sheep1, sheep2, wolf1, wolf2,edgeFlag1,edgeFlag2)
            judge(sheep1,wolf1,sheep2,wolf2)
        elif edgeFlag2==True:
            oprate(sheep2, sheep1, wolf2, wolf1,edgeFlag1,edgeFlag2)
            judge(sheep1,wolf1,sheep2,wolf2)
        show(edgeFlag1,edgeFlag2,edge1, edge2, sheep1, sheep2, wolf1, wolf2)
main()
print(edgeFlag1)





#! /usr/bin/env python3 
#  coding = utf-8       
from math  import sin, cos, radians as rads ####################
from numpy import array, dot, argmax, around                   #
################################################################
def rmx(h):                      # rotation matrix, h iz in degs
    h = rads(h)                             # convert to radians
    return array([[ cos(h), sin(h)],                       # ye!
                  [-sin(h), cos(h)]])                    # bye:)
# c o o r z   t r a n s f o r m a t i o n s ####################
def prim(h, coorz):                       # napu cToKa napu npuM
    m = rmx(h)                                                 #
    return around(dot(m, coorz), decimals=4)                   #
################################################################
def scope(ls): return min(ls), max(ls)                       #:)
class Segment: #                                            boom
    ############################################################
    def __init__(self, x1, y1, x2, y2):
        self.coorz = ((x1, y1), #  A                   y|
                      (x2, y1), #  B   D--------C       |
                      (x2, y2), #  C   |        |       |
                      (x1, y2)) #  D   A--------B       o------x
    ############################################################
    def __str__(self): return f"{self.coorz}"
    ############################################################
    def __repr__(self): return self.__str__()
    ############################################################
    #               .
    #       y`      .        C.` x`    in thiz case the scope of
    #      `.       .      B.` `.      the x` projection will be
    #        `.     .    D.` `.  `.    (A, C)
    #          `.   .  A.` `d  `.  `c
    #            `. . .` `.      `.
    #              `.`     `a      `b 
    def proj(self, h): #                       scope projections
        coorz1 = array([prim(h, coorz) for coorz in self.coorz])
        return [scope(coorz1[:, j]) for j in (0, 1)]
################################################################
# Entry: h        - rotation angle
#        segments - list of segments
# Exit : Okay ve vant 2 get list of scope projections for both
#        x` and y` directions thatz.
def getProjScope(h, segments):
    ls = array([seg.proj(h) for seg in segments])
    return ls[:, 0], ls[:, 1] # ye-e! 
################################################## .global stuff
džERO = 0 # what is this?
debug = False                                            # foolz
def insert(val, ls): # Okay insert val in ls like in insert sort
    if val in ls: return #                      no need for that
    j = len(ls) # ------------------------------ insert position
    while True:                   # keep it simple
        if j == džERO: break      # ve ar don!
        if val > ls[j - 1]: break # yeep!
        j -= 1                    # wtf?
    ls.insert(j, val)             #                      finally
################################################################
def getendp(proj):        # get endpoints from a projection list
    endp = []                                  #
    for interval in proj:                      #
        for val in interval: insert(val, endp) #
    return endp                                #             o o
################################################################
def is_subset(a, b, interval):     # ck if [a, b] is in interval
    if a >= interval[0] and b <= interval[1]: return True
    return False
################################################################
# The first element of ls is the current maxcntr followed by a
# list of endp indices. If cntr is less then maxcntr do nothing
# if is greather than replace maxcntr otherwice append ze index.
def push_max(cntr, j, ls):           # 
    maxval = ls[0]                   #
    if cntr < maxval: return         # 
    if cntr > maxval: ls[:] = [cntr] # 
    ls.append(j)                     # 
################################################################
def intasect(proj): #  习 近 平 ： 志 在 全 胜 的 战"疫"纲 领 ！
# 李 克 强 主 持 召 开 应 对 疫 情 工 作 领 导 小 组 会 议
# 我 国 医 用 N  9  5  口 罩 日 产 能 突 破 1  0  0  万 只
# 坚 决 夺 取 疫 情 防 控 和 经 济 社 会 发 展 双 胜 利
# 用 好 “  互 联 网 +  ”  ， 发 挥 战 疫 春 耕 的 硬 核 力 量
# 面 对 疫 情 ， 这 位 优 秀 的 摩 洛 哥 女 孩 决 定 留 在 武 汉
# 武 汉 2  5  日 餐 饮 外 卖 订 单 数 量 达 1  3  万 单
# “  抗 疫 一 线 就 是 我 们 的 课 堂 ”                  
################################################################
    endp = getendp(proj)
    ls = [-1]
    for j in range(len(endp) - 1):
        cntr = 0
        a, b = endp[j], endp[j + 1]
        for interval in proj:
            if is_subset(a, b, interval): cntr += 1
        push_max(cntr, j, ls)
    return ls, endp
################################################################
# group intasect data:
class Cntr: #                                            C unte
    ######################################################o####
    def __init__(self, coor, proj):                       #
        self.coor = coor              
        j = {'x': 0, 'y': 1}[coor]
        ls, endp = intasect(proj[j])
        self.n = ls[0] # that is the counte                    r
        self.endp = [(endp[j], endp[j+1]) for j in ls[1:]]     #
    ############################################################
    def total(self): return sum([i[1]-i[0] for i in self.endp])
    ############################################################
    def __gt__(self, other):         # >
        if self.n != other.n: return self.n > other.n
        return self.total() > other.total()        
################################################################
def str8(h, segments):                #
    proj = getProjScope(h, segments)  #
    ############################################################
    xcntr = Cntr('x', proj)           #
    ycntr = Cntr('y', proj)           #
    ############################################################
    return sorted((xcntr, ycntr))[-1] #
################################################################
#                      5. . . . . . . . .  cerMeHT noeTuka
#                       . . . . . . . . .
#            -         4. . . . . . . . .  koGTo 7ecHo ce
#             '         . . . . . . . . .  ra3upa
#              `,      3. . . . . . . . .  r7ega caMo
#                -      . . . . . . . .,-` a7 gKa3upa.,?!  
#                 '    2. . . . . . ,-` .
#                  `,   . . . . .,-`. . .
#                    - 1. . . ,-` . . . .
#                     ' . .,-`. . . . C O O R
#                      `,-` . . . . . . .
#                       0   1   2   3   4
def dOthEMAth():
    if debug: import pdb; pdb.set_trace()
##### initialize
    segments = (Segment(1, 1, 2, 3),
                Segment(3, 3, 4, 5))
##### find maximum solution
    cntr = [str8(h, segments) for h in range(90)]
    max_h = int(argmax(cntr))
    max_cntr = cntr[max_h]
##### dump solution
    print("angle    :", max_h)
    print("coor     :", max_cntr.coor)
    print("endpoints:", max_cntr.endp)
################################################################
if __name__ == "__main__": dOthEMAth()
########################################################### log:

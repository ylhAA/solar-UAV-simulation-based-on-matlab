import vsp_2
import numpy as np
from datetime import datetime

# 参考示例 NACA 3412(怎么颠倒还没有尝试出来) 和 NASA SC-0412
stage = 7
root_up = [0.20027, 0.06942, 0.26365, 0.01476, 0.27234, 0.14104, 0.17256, 0.20330]
root_low = [-0.20027, -0.08095, -0.21768, -0.12756, -0.14138, -0.24818, 0.04641, 0.16772]
tip_up = [0.15727, 0.33244, 0.11350, 0.26489, 0.29933, 0.14698, 0.27400, 0.25044]
tip_low = [-0.15727, -0.04782, -0.19466, 0.10213, -0.22039, 0.03441, -0.06494, -0.06763]


# #############################################################
# #################### 焦点计算cal_xcg #########################
# #############################################################
# 这个焦点计算不好用 感觉精度差而且计算时间长
def cal_xcg(up_root, low_root, up_tip, low_tip, stag):
    # 参数设置
    flag = 0  # 控制变量
    max_iterations = 10  # 最大迭代步数
    var_ctrl = 1e-4  # 理想状态下才能让函数到0 实际上并不行 防止越界发散
    var_value_ctrl = 1e-4  # 大约是0.01的精度
    epsilon = 0.001  # 更新步长
    # 建立几何
    vsp_2.create_Geom(up_root, low_root, up_tip, low_tip, stag)
    # 设置初始参数
    value = 1  # 两个var_value的差值
    Xcg = 0  # 中间变量
    Xcg_0 = 0  # 初始迭代位置
    Xcg_1 = 0.1  # 双初值法
    iterations = 0  # 初始迭代步数
    # 开始迭代
    cmy_0 = vsp_2.vsp_aero_sweep(Xcg_0)
    var_value_0 = var_cal(cmy_0) - var_ctrl
    cmy_1 = vsp_2.vsp_aero_sweep(Xcg_1)
    var_value_1 = var_cal(cmy_1) - var_ctrl
    iteration_gap = np.fabs(Xcg_1 - Xcg_0)
    while value > var_value_ctrl and iteration_gap > epsilon and iterations < max_iterations:
        # 把0的参数代替为1
        Xcg = Xcg_1 - var_value_1 / ((var_value_1 - var_value_0) / (Xcg_1 - Xcg_0))
        Xcg_0 = Xcg_1
        cmy_0 = cmy_1
        if Xcg > 1 or Xcg < 0:
            flag = 2
            break
        var_value_0 = var_value_1
        # 更新参数1的值
        cmy_1 = vsp_2.vsp_aero_sweep(Xcg)
        var_value_1 = var_cal(cmy_1) - var_ctrl
        Xcg_1 = Xcg
        # 计算新的均方差差值 迭代步长
        value = np.fabs(var_value_1 - var_value_0)
        iteration_gap = np.fabs(Xcg_1 - Xcg_0)
        iterations += 1
    if iterations == max_iterations:
        flag = 1
    # 输出迭代情况
    if flag == 0:
        print("正常收敛\n迭代次数:", iterations)
    elif flag == 1:
        print("ERROR\n超过迭代最大次数")
    elif flag == 2:
        print("ERROR\n超过合理迭代范围")
    else:
        pass
    print(iteration_gap, value)
    return Xcg


# #############################################################
# #################### 俯仰力矩分析var_cal ######################
# #############################################################
def var_cal(cmy_array):
    var_value = 0
    avr_value = 0
    for i in range(len(cmy_array)):
        avr_value = avr_value + cmy_array[i]
    avr_value = avr_value / (len(cmy_array))
    for i in range(len(cmy_array)):
        var_value = var_value + np.power((cmy_array[i] - avr_value), 2)
    var_value = var_value / len(cmy_array)
    print(avr_value)
    return var_value


# #############################################################
# ################### 配平攻角计算alpha_cal #####################
# #############################################################
# 输入气动焦点位置 寻找配平攻角
# 受到了求解器的影响，迭代是发散的，可能跟模型有关
def alpha_cal(up_root, low_root, up_tip, low_tip, stag, xcg):
    # 参数设置
    flag = 0  # 控制变量
    value_ctrl = 5e-3
    max_iterations = 10  # 最大迭代步数
    epsilon = 0.05  # 更新步长
    supervise_file = ("D:\\aircraft design competition\\24solar\\design_model\\whole_wing_optimization\\vsp"
                      "\\supervise.txt")

    # 建立几何
    vsp_2.create_Geom(up_root, low_root, up_tip, low_tip, stag)
    # 设置初始参数
    AOA = 0
    alpha_0 = -4  # 初始迭代位置
    alpha_1 = 4  # 双初值法
    iterations = 0  # 初始迭代步数

    # 开始迭代
    current_time = datetime.now()
    with open(supervise_file, 'a') as file:
        file.write(f"解算开始时间: {current_time}\n")
    [_, Cmy_0, _] = vsp_2.vsp_aero(xcg, alpha_0)
    [_, Cmy_1, _] = vsp_2.vsp_aero(xcg, alpha_1)
    cmy_0 = Cmy_0[0]
    cmy_1 = Cmy_1[0]  # 变成处理单个数字
    iteration_gap = np.fabs(alpha_1 - alpha_0)
    value = np.fabs(cmy_0 - cmy_1)  # 两个Cmy_value的差值
    while value > value_ctrl and iteration_gap > epsilon and iterations < max_iterations:
        # 更新下一个点的位置
        alpha = alpha_1 - cmy_1 / ((cmy_1 - cmy_0) / (alpha_1 - alpha_0))
        with open(supervise_file, 'a') as file:
            file.write(f"iterations: {iterations}\n")
            file.write(f"alpha: {alpha}\n")
            file.write(f"alpha_0: {alpha_0}\n")
            file.write(f"alpha_1: {alpha_1}\n")
            file.write(f"cmY_0: {cmy_0}\n")
            file.write(f"cmY_1: {cmy_1}\n")
            # 更新参数0的值
        alpha_0 = alpha_1
        cmy_0 = cmy_1
        if alpha > 10 or alpha < -3:
            flag = 2
            break
        # 更新参数1的值
        Cmy_1 = vsp_2.vsp_aero(xcg, alpha)
        cmy_1 = Cmy_1[0]
        alpha_1 = alpha
        # 计算新的均方差差值 迭代步长
        value = np.fabs(cmy_1 - cmy_0)
        iteration_gap = np.fabs(alpha_1 - alpha_0)
        iterations += 1
    file.close()
    if iterations == max_iterations:
        flag = 1
        # 输出迭代情况
    if flag == 0:
        AOA = alpha_1
        print("正常收敛\n迭代次数:", iterations)
    elif flag == 1:
        print("ERROR\n超过迭代最大次数")
    elif flag == 2:
        print("ERROR\n超过合理迭代范围")
    else:
        pass
    print(iteration_gap, value)
    return AOA
    # 前后插值控制 步长控制 最大步数控制


# #############################################################
# #################### 简单的demo与测试 #########################
# #############################################################

# # var_cal测试
# value = var_cal([1, 2, 3])
# print(value)

# #单点demo
# vsp_2.create_Geom(root_up, root_low, tip_up, tip_low, stage)
# [cl, CMy, cdi] = vsp_2.vsp_aero(0.2, 1)
# print(cl)
# print(CMy)
# print(cdi)

# # 多点计算demo
# vsp_2.create_Geom(root_up, root_low, tip_up, tip_low, stage)
# CMy_array = np.empty((10, 5))
# for i in range(10):
#     CMy = vsp_2.vsp_aero_sweep(0.275 + i * 0.05)
#     CMy_array[i, :] = CMy
# print(CMy_array)

# 焦点计算测试
# xcg = cal_xcg(root_up, root_low, tip_up, tip_low, stage)
# print(xcg)

# 配平攻角测试
# Alpha = alpha_cal(root_up, root_low, tip_up, tip_low, stage, 0.28)
# print(Alpha)

import openvsp as vsp
import paths
import numpy as np


# #############################################################
# ##################### 初始化OpenVSP模型########################
# #############################################################
def create_Geom_0(root_up, root_low, tip_up, tip_low, stage):  # input A1[],A2[]
    vsp.VSPCheckSetup()
    vsp.VSPRenew()

    # 添加一个主翼
    main_wing = vsp.AddGeom("WING")
    vsp.InsertXSec(main_wing, 1, vsp.XS_GENERAL_FUSE)

    # 更改主翼参数
    vsp.SetParmVal(main_wing, "SectTess_U", "XSec_1", 4)  # 内段弦长方向划分
    vsp.SetParmVal(main_wing, "Tess_W", "Shape", 30)  # 用来调整展长方向划分
    vsp.SetParmVal(main_wing, "Root_Chord", "XSec_1", 0.31800)
    vsp.SetParmVal(main_wing, "Tip_Chord", "XSec_1", 0.30000)
    vsp.SetParmVal(main_wing, "Span", "XSec_1", 0.05000)
    vsp.SetParmVal(main_wing, "Area", "XSec_1", 0.01545)
    vsp.SetParmVal(main_wing, "Sweep", "XSec_1", 20)

    vsp.Update()

    vsp.SetParmVal(main_wing, "SectTess_U", "XSec_2", 25)  # 外段弦长方向划分 注意一定要跟 xsec_2自己放在一起不然小心报错
    vsp.SetParmVal(main_wing, "Root_Chord", "XSec_2", 0.30000)
    vsp.SetParmVal(main_wing, "Tip_Chord", "XSec_2", 0.30000)
    vsp.SetParmVal(main_wing, "Span", "XSec_2", 1.22000)
    vsp.SetParmVal(main_wing, "Area", "XSec_2", 0.36600)
    vsp.SetParmVal(main_wing, "Sweep", "XSec_2", 20)

    vsp.Update()

    surf0 = vsp.GetXSecSurf(main_wing, 0)
    vsp.ChangeXSecShape(surf0, 0, vsp.XS_CST_AIRFOIL)
    xsec_0 = vsp.GetXSec(surf0, 0)
    vsp.Update()
    vsp.SetUpperCST(xsec_0, stage, root_up)
    vsp.SetLowerCST(xsec_0, stage, root_low)  # 根部CST翼型

    vsp.ChangeXSecShape(surf0, 1, vsp.XS_CST_AIRFOIL)
    xsec_1 = vsp.GetXSec(surf0, 1)
    vsp.Update()
    vsp.SetUpperCST(xsec_1, stage, root_up)
    vsp.SetLowerCST(xsec_1, stage, root_low)  # 与根部相同CST翼型

    vsp.ChangeXSecShape(surf0, 2, vsp.XS_CST_AIRFOIL)
    xsec_2 = vsp.GetXSec(surf0, 2)
    vsp.Update()
    vsp.SetUpperCST(xsec_2, stage, tip_up)
    vsp.SetLowerCST(xsec_2, stage, tip_low)  # 稍部CST翼型
    vsp.Update()

    # 添加翼梢小翼
    wing_let_1 = vsp.AddGeom("WING")
    # 更改翼梢小翼参数
    vsp.SetParmVal(wing_let_1, "Root_Chord", "XSec_1", 0.36000)
    vsp.SetParmVal(wing_let_1, "Tip_Chord", "XSec_1", 0.24500)
    vsp.SetParmVal(wing_let_1, "Span", "XSec_1", 0.11500)
    vsp.SetParmVal(wing_let_1, "Sweep", "XSec_1", 45)
    vsp.SetParmVal(wing_let_1, "X_Rel_Location", "XForm", 0.562)
    vsp.SetParmVal(wing_let_1, "Y_Rel_Location", "XForm", 1.275)
    vsp.SetParmVal(wing_let_1, "X_Rel_Rotation", "XForm", 90)
    vsp.Update()

    # 设置截面为椭圆形 如果缺省就是 NACA0010
    surf1 = vsp.GetXSecSurf(wing_let_1, 0)
    vsp.ChangeXSecShape(surf1, 0, vsp.XS_ELLIPSE)
    vsp.ChangeXSecShape(surf1, 1, vsp.XS_ELLIPSE)
    vsp.Update()

    wing_let_2 = vsp.AddGeom("WING")
    # 更改翼梢小翼参数
    vsp.SetParmVal(wing_let_2, "Root_Chord", "XSec_1", 0.36000)
    vsp.SetParmVal(wing_let_2, "Tip_Chord", "XSec_1", 0.24500)
    vsp.SetParmVal(wing_let_2, "Span", "XSec_1", 0.11500)
    vsp.SetParmVal(wing_let_2, "Sweep", "XSec_1", 45)
    vsp.SetParmVal(wing_let_2, "X_Rel_Location", "XForm", 0.562)
    vsp.SetParmVal(wing_let_2, "Y_Rel_Location", "XForm", 1.275)
    vsp.SetParmVal(wing_let_2, "X_Rel_Rotation", "XForm", -90)
    vsp.Update()

    # 设置截面为椭圆形 如果缺省就是 NACA0010
    surf2 = vsp.GetXSecSurf(wing_let_2, 0)
    vsp.ChangeXSecShape(surf2, 0, vsp.XS_ELLIPSE)
    vsp.ChangeXSecShape(surf2, 1, vsp.XS_ELLIPSE)
    vsp.Update()
    # 保存文件
    file_name = paths.vsp_file
    vsp.WriteVSPFile(file_name, vsp.SET_ALL)

    print("Geom Generate COMPLETE")


def create_Geom_1(root_up, root_low, tip_up, tip_low, stage):
    vsp.VSPCheckSetup()
    vsp.VSPRenew()

    # 添加一个主翼
    main_wing = vsp.AddGeom("WING")
    vsp.InsertXSec(main_wing, 1, vsp.XS_GENERAL_FUSE)

    # 更改主翼参数
    vsp.SetParmVal(main_wing, "SectTess_U", "XSec_1", 4)  # 内段弦长方向划分
    vsp.SetParmVal(main_wing, "Tess_W", "Shape", 30)  # 用来调整展长方向划分
    vsp.SetParmVal(main_wing, "Root_Chord", "XSec_1", 0.31800)
    vsp.SetParmVal(main_wing, "Tip_Chord", "XSec_1", 0.30000)
    vsp.SetParmVal(main_wing, "Span", "XSec_1", 0.05000)
    vsp.SetParmVal(main_wing, "Area", "XSec_1", 0.01545)
    vsp.SetParmVal(main_wing, "Sweep", "XSec_1", 20)

    vsp.Update()

    vsp.SetParmVal(main_wing, "SectTess_U", "XSec_2", 25)  # 外段弦长方向划分 注意一定要跟 xsec_2自己放在一起不然小心报错
    vsp.SetParmVal(main_wing, "Root_Chord", "XSec_2", 0.30000)
    vsp.SetParmVal(main_wing, "Tip_Chord", "XSec_2", 0.30000)
    vsp.SetParmVal(main_wing, "Span", "XSec_2", 1.22000)
    vsp.SetParmVal(main_wing, "Area", "XSec_2", 0.36600)
    vsp.SetParmVal(main_wing, "Sweep", "XSec_2", 20)

    vsp.Update()

    surf0 = vsp.GetXSecSurf(main_wing, 0)
    vsp.ChangeXSecShape(surf0, 0, vsp.XS_CST_AIRFOIL)
    xsec_0 = vsp.GetXSec(surf0, 0)
    vsp.Update()
    vsp.SetUpperCST(xsec_0, stage, root_up)
    vsp.SetLowerCST(xsec_0, stage, root_low)  # 根部CST翼型

    vsp.ChangeXSecShape(surf0, 1, vsp.XS_CST_AIRFOIL)
    xsec_1 = vsp.GetXSec(surf0, 1)
    vsp.Update()
    vsp.SetUpperCST(xsec_1, stage, root_up)
    vsp.SetLowerCST(xsec_1, stage, root_low)  # 与根部相同CST翼型

    vsp.ChangeXSecShape(surf0, 2, vsp.XS_CST_AIRFOIL)
    xsec_2 = vsp.GetXSec(surf0, 2)
    vsp.Update()
    vsp.SetUpperCST(xsec_2, stage, tip_up)
    vsp.SetLowerCST(xsec_2, stage, tip_low)  # 稍部CST翼型
    vsp.Update()

    # 保存文件
    file_name = paths.vsp_file
    vsp.WriteVSPFile(file_name, vsp.SET_ALL)

    print("Geom Generate COMPLETE")


# 读取dat文件来生成几何模型 放弃vsp内部的gemo
# 输入两个
def create_Geom_2(tip_airfoil_path, root_airfoil_path):
    # 读取文件的设置
    # 初始检查与更新
    vsp.VSPCheckSetup()
    vsp.VSPRenew()

    # 添加一个主翼
    main_wing = vsp.AddGeom("WING")
    vsp.InsertXSec(main_wing, 1, vsp.XS_GENERAL_FUSE)

    # 更改主翼参数
    vsp.SetParmVal(main_wing, "SectTess_U", "XSec_1", 4)  # 内段弦长方向划分
    vsp.SetParmVal(main_wing, "Tess_W", "Shape", 30)  # 用来调整展长方向划分
    vsp.SetParmVal(main_wing, "Root_Chord", "XSec_1", 0.31800)
    vsp.SetParmVal(main_wing, "Tip_Chord", "XSec_1", 0.30000)
    vsp.SetParmVal(main_wing, "Span", "XSec_1", 0.05000)
    vsp.SetParmVal(main_wing, "Area", "XSec_1", 0.01545)
    vsp.SetParmVal(main_wing, "Sweep", "XSec_1", 20)

    vsp.Update()

    vsp.SetParmVal(main_wing, "SectTess_U", "XSec_2", 25)  # 外段弦长方向划分 注意一定要跟 xsec_2自己放在一起不然小心报错
    vsp.SetParmVal(main_wing, "Root_Chord", "XSec_2", 0.30000)
    vsp.SetParmVal(main_wing, "Tip_Chord", "XSec_2", 0.30000)
    vsp.SetParmVal(main_wing, "Span", "XSec_2", 1.22000)
    vsp.SetParmVal(main_wing, "Area", "XSec_2", 0.36600)
    vsp.SetParmVal(main_wing, "Sweep", "XSec_2", 20)

    vsp.Update()
    # 更改为dat文件读取
    surf0 = vsp.GetXSecSurf(main_wing, 0)
    vsp.ChangeXSecShape(surf0, 0, vsp.XS_FILE_AIRFOIL)
    xsec_0 = vsp.GetXSec(surf0, 0)
    vsp.ReadFileAirfoil(xsec_0, root_airfoil_path)
    vsp.Update()
    # 根部翼型

    vsp.ChangeXSecShape(surf0, 1, vsp.XS_FILE_AIRFOIL)
    xsec_1 = vsp.GetXSec(surf0, 1)
    vsp.ReadFileAirfoil(xsec_1, root_airfoil_path)
    vsp.Update()
    # 与根部相同的翼型

    vsp.ChangeXSecShape(surf0, 2, vsp.XS_FILE_AIRFOIL)
    xsec_2 = vsp.GetXSec(surf0, 2)
    vsp.ReadFileAirfoil(xsec_2, tip_airfoil_path)
    vsp.Update()
    # 稍部CST翼型

    # 保存文件
    file_name = paths.vsp_file
    vsp.WriteVSPFile(file_name, vsp.SET_ALL)

    print("Geom Generate COMPLETE")


def create_Geom_3(tip_airfoil_path, mid_airfoil_path, root_airfoil_path):
    # 读取文件的设置
    # 初始检查与更新
    vsp.VSPCheckSetup()
    vsp.VSPRenew()

    # 添加一个主翼
    main_wing = vsp.AddGeom("WING")
    vsp.InsertXSec(main_wing, 1, vsp.XS_GENERAL_FUSE)
    vsp.InsertXSec(main_wing, 2, vsp.XS_GENERAL_FUSE)
    # 更改主翼参数
    vsp.SetParmVal(main_wing, "SectTess_U", "XSec_1", 4)  # 内段弦长方向划分
    vsp.SetParmVal(main_wing, "Tess_W", "Shape", 30)  # 用来调整展长方向划分
    vsp.SetParmVal(main_wing, "Root_Chord", "XSec_1", 0.31800)
    vsp.SetParmVal(main_wing, "Tip_Chord", "XSec_1", 0.30000)
    vsp.SetParmVal(main_wing, "Span", "XSec_1", 0.05000)
    vsp.SetParmVal(main_wing, "Area", "XSec_1", 0.01545)
    vsp.SetParmVal(main_wing, "Sweep", "XSec_1", 10)

    vsp.Update()

    vsp.SetParmVal(main_wing, "SectTess_U", "XSec_2", 13)  # 外段弦长方向划分 注意一定要跟 xsec_2自己放在一起不然小心报错
    vsp.SetParmVal(main_wing, "Root_Chord", "XSec_2", 0.30000)
    vsp.SetParmVal(main_wing, "Tip_Chord", "XSec_2", 0.30000)
    vsp.SetParmVal(main_wing, "Span", "XSec_2", 0.625000)
    vsp.SetParmVal(main_wing, "Area", "XSec_2", 0.183)
    vsp.SetParmVal(main_wing, "Sweep", "XSec_2", 10)

    vsp.Update()

    vsp.SetParmVal(main_wing, "SectTess_U", "XSec_3", 13)  # 外段弦长方向划分 注意一定要跟 xsec_2自己放在一起不然小心报错
    vsp.SetParmVal(main_wing, "Root_Chord", "XSec_3", 0.30000)
    vsp.SetParmVal(main_wing, "Tip_Chord", "XSec_3", 0.30000)
    vsp.SetParmVal(main_wing, "Span", "XSec_3", 0.625000)
    vsp.SetParmVal(main_wing, "Area", "XSec_3", 0.183)
    vsp.SetParmVal(main_wing, "Sweep", "XSec_3", 10)

    vsp.Update()
    # 更改为dat文件读取
    surf0 = vsp.GetXSecSurf(main_wing, 0)
    vsp.ChangeXSecShape(surf0, 0, vsp.XS_FILE_AIRFOIL)
    xsec_0 = vsp.GetXSec(surf0, 0)
    vsp.ReadFileAirfoil(xsec_0, root_airfoil_path)
    vsp.Update()
    # 根部翼型

    vsp.ChangeXSecShape(surf0, 1, vsp.XS_FILE_AIRFOIL)
    xsec_1 = vsp.GetXSec(surf0, 1)
    vsp.ReadFileAirfoil(xsec_1, root_airfoil_path)
    vsp.Update()
    # 与根部相同的翼型

    vsp.ChangeXSecShape(surf0, 2, vsp.XS_FILE_AIRFOIL)
    xsec_2 = vsp.GetXSec(surf0, 2)
    vsp.ReadFileAirfoil(xsec_2, mid_airfoil_path)
    vsp.Update()
    # 中部CST翼型

    vsp.ChangeXSecShape(surf0, 3, vsp.XS_FILE_AIRFOIL)
    xsec_3 = vsp.GetXSec(surf0, 3)
    vsp.ReadFileAirfoil(xsec_3, tip_airfoil_path)
    vsp.Update()
    # 稍部CST翼型

    # 保存文件
    file_name = paths.vsp_file
    vsp.WriteVSPFile(file_name, vsp.SET_ALL)

    print("Geom Generate COMPLETE")


# 有后掠角的几何生成文件注意是角度
def create_Geom_4(tip_airfoil_path, mid_airfoil_path, root_airfoil_path, angle=10):
    # 读取文件的设置
    angled = angle * np.pi / 180
    chord = 0.277
    blank = 0.05
    # 初始检查与更新
    vsp.VSPCheckSetup()
    vsp.VSPRenew()

    # 添加一个主翼
    main_wing = vsp.AddGeom("WING")
    vsp.InsertXSec(main_wing, 1, vsp.XS_GENERAL_FUSE)
    vsp.InsertXSec(main_wing, 2, vsp.XS_GENERAL_FUSE)
    # 更改主翼参数
    vsp.SetParmVal(main_wing, "SectTess_U", "XSec_1", 4)  # 内段弦长方向划分
    vsp.SetParmVal(main_wing, "Tess_W", "Shape", 30)  # 用来调整展长方向划分
    vsp.SetParmVal(main_wing, "Root_Chord", "XSec_1", chord / np.cos(angled) + blank * np.sin(angled))
    vsp.SetParmVal(main_wing, "Tip_Chord", "XSec_1", chord / np.cos(angled))
    vsp.SetParmVal(main_wing, "Span", "XSec_1", blank)
    vsp.SetParmVal(main_wing, "Area", "XSec_1", (2 * (chord / np.cos(angled)) + blank * np.sin(angled)) * blank / 2)
    vsp.SetParmVal(main_wing, "Sweep", "XSec_1", angle)

    vsp.Update()

    vsp.SetParmVal(main_wing, "SectTess_U", "XSec_2", 13)  # 外段弦长方向划分 注意一定要跟 xsec_2自己放在一起不然小心报错
    vsp.SetParmVal(main_wing, "Root_Chord", "XSec_2", chord / np.cos(angled))
    vsp.SetParmVal(main_wing, "Tip_Chord", "XSec_2", chord / np.cos(angled))
    vsp.SetParmVal(main_wing, "Span", "XSec_2", (1.25 + np.tan(angled) * chord) * np.cos(angled) / 2)
    vsp.SetParmVal(main_wing, "Area", "XSec_2",
                   chord / np.cos(angled) * (1.25 + np.tan(angled) * chord) * np.cos(angled) / 2)
    vsp.SetParmVal(main_wing, "Sweep", "XSec_2", angle)

    vsp.Update()

    vsp.SetParmVal(main_wing, "SectTess_U", "XSec_3", 13)  # 外段弦长方向划分 注意一定要跟 xsec_2自己放在一起不然小心报错
    vsp.SetParmVal(main_wing, "Root_Chord", "XSec_3", chord / np.cos(angled))
    vsp.SetParmVal(main_wing, "Tip_Chord", "XSec_3", chord / np.cos(angled))
    vsp.SetParmVal(main_wing, "Span", "XSec_3", (1.25 + np.tan(angled) * chord) * np.cos(angled) / 2)
    vsp.SetParmVal(main_wing, "Area", "XSec_3",
                   chord / np.cos(angled) * (1.25 + np.tan(angled) * chord) * np.cos(angled) / 2)
    vsp.SetParmVal(main_wing, "Sweep", "XSec_3", angle)

    vsp.Update()
    # 更改为dat文件读取
    surf0 = vsp.GetXSecSurf(main_wing, 0)
    vsp.ChangeXSecShape(surf0, 0, vsp.XS_FILE_AIRFOIL)
    xsec_0 = vsp.GetXSec(surf0, 0)
    vsp.ReadFileAirfoil(xsec_0, root_airfoil_path)
    vsp.Update()
    # 根部翼型

    vsp.ChangeXSecShape(surf0, 1, vsp.XS_FILE_AIRFOIL)
    xsec_1 = vsp.GetXSec(surf0, 1)
    vsp.ReadFileAirfoil(xsec_1, root_airfoil_path)
    vsp.Update()
    # 与根部相同的翼型

    vsp.ChangeXSecShape(surf0, 2, vsp.XS_FILE_AIRFOIL)
    xsec_2 = vsp.GetXSec(surf0, 2)
    vsp.ReadFileAirfoil(xsec_2, mid_airfoil_path)
    vsp.Update()
    # 中部CST翼型

    vsp.ChangeXSecShape(surf0, 3, vsp.XS_FILE_AIRFOIL)
    xsec_3 = vsp.GetXSec(surf0, 3)
    vsp.ReadFileAirfoil(xsec_3, tip_airfoil_path)
    vsp.Update()
    # 稍部CST翼型

    # 保存文件
    file_name = paths.vsp_file
    vsp.WriteVSPFile(file_name, vsp.SET_ALL)

    print("Geom Generate COMPLETE")


# #############################################################
# ####################vsp-aero单点计算##########################
# #############################################################

def vsp_aero(x_cg, aoa):  # 重心位置 迎角
    # 检查和清除否则模型会叠加干扰后续模型的建立
    vsp.VSPCheckSetup()
    vsp.VSPRenew()
    # result_file = "D:\\aircraft design competition\\24solar\\design_model\\whole_wing_optimization\\vsp"
    # "\\result.csv"
    # 几何文件写入
    filename_vsp_aero_ana = paths.vsp_file
    # 这里是为了调用几何
    vsp.ReadVSPFile(filename_vsp_aero_ana)

    # 分析文件命名
    comp_geom = "VSPAEROComputeGeometry"
    print(comp_geom)

    # 设置defaults
    vsp.SetAnalysisInputDefaults(comp_geom)
    analysis_name_results = vsp.ExecAnalysis(comp_geom)  # 返回的是一个ID
    print("The Geom Result:\n", analysis_name_results)
    # 把所有的分析模式全部输出来
    for analysis in vsp.ListAnalysis():
        print(analysis)

    # 分析方法
    analysis_name = "VSPAEROSweep"  # 找到一个适合的求解器 不要用single point
    vsp.SetIntAnalysisInput(comp_geom, "AnalysisMethod", (1, vsp.VORTEX_LATTICE))
    # 打印该求解器所有可以更改的参数
    # print("VSPAEROSweep 所有可选参数\n")
    # vsp.PrintAnalysisInputs(analysis_name)

    # 设置参考翼面

    # 手动设置 来自GUI总体参数确定后的 From Model
    S_ref = [0.763]
    vsp.SetDoubleAnalysisInput(analysis_name, "Sref", S_ref, 0)
    b_ref = [2.540]
    vsp.SetDoubleAnalysisInput(analysis_name, "bref", b_ref, 0)
    c_ref = [0.304]
    vsp.SetDoubleAnalysisInput(analysis_name, "cref", c_ref, 0)

    # 自动计算设置 (暂时不成功)
    # ref_flag = [0]
    # vsp.SetIntAnalysisInput(analysis_name, "RefFlag", ref_flag, 0)
    vsp.Update()

    # 设置来流参数
    mach_speed = [0.02053]  # 7.00m/s altitude 0m
    vsp.SetDoubleAnalysisInput(analysis_name, "MachStart", mach_speed, 0)
    machNpts = [1]
    vsp.SetIntAnalysisInput(analysis_name, "MachNpts", machNpts, 0)
    alpha = [aoa]
    vsp.SetDoubleAnalysisInput(analysis_name, "AlphaStart", alpha, 0)
    alphaNpts = [1]
    vsp.SetIntAnalysisInput(analysis_name, "AlphaNpts", alphaNpts, 0)
    vsp.Update()
    rho = [1.225]  # 近地面大气密度参数
    vsp.SetDoubleAnalysisInput(analysis_name, "Rho", rho, 0)
    Re = [143651]  # 近地面 7m/s 参考长度为弦长 0.30m
    vsp.SetDoubleAnalysisInput(analysis_name, "ReCref", Re, 0)

    # 设置重心
    xcg = [x_cg]
    vsp.SetDoubleAnalysisInput(analysis_name, "Xcg", xcg, 0)

    # 高级设置
    N_cpu = [8]  # 调用CPU数目
    vsp.SetIntAnalysisInput(analysis_name, "NCPU", N_cpu, 0)
    Iter = [10]  # 迭代步数
    vsp.SetIntAnalysisInput(analysis_name, "WakeNumIter", Iter, 0)
    vsp.Update()
    print("analysis parameter modified\n COMPLETED\n")
    # print("VSPAEROSweep 参数输入结果\n")
    # vsp.PrintAnalysisInputs(analysis_name)

    # #############################################################
    # 进行中间的保存尝试 观察vsp3是否正常
    # file_name = "D:\\aircraft design competition\\24solar\\design_model\\whole_wing_optimization\\vsp\\test2.vsp3"
    # vsp.WriteVSPFile(file_name, vsp.SET_ALL)
    # #############################################################

    # 开始计算
    # #############################################################
    print("\tExecution...")
    _ = vsp.ExecAnalysis(analysis_name)
    print("COMPLETE")
    # #############################################################

    # 后处理
    # #############################################################
    # 返回一个列表里面是所有可用结果的名称
    _ = vsp.GetAllResultsNames()
    # 查找point的ID并赋值给point_id
    point_id = vsp.FindResultsID("point")
    # 一样的也是一个查找
    polar_id = vsp.FindResultsID("VSPAERO_Polar")

    # 用来了解可用的结果集合和数据的名称（全部打印出来）
    # for result in results:
    #     data_names = vsp.GetAllDataNames(vsp.FindResultsID(result))
    #     for data_name in data_names:
    #         print(f"{result} > {data_name}")

    # 用来统计CL的数据量并打印第一个
    print("num of data in 'VSPAERO_Polar > CL': ", vsp.GetNumData(polar_id, "CL"))
    cl = vsp.GetDoubleResults(polar_id, "CL", 0)
    print(f"CL = {cl}\n")
    print("num of data in 'VSPAERO_Polar > CDi': ", vsp.GetNumData(polar_id, "CDi"))
    cdi = vsp.GetDoubleResults(polar_id, "CDi", 0)
    print(f"CDi = {cdi}\n")
    # 这里的polar_id 赋值的是"VSPAERO_Polar" 也就是结果组的一个值 引用了结果组"VSPAERO_Polar"的L_D的部分
    print("num of data in 'VSPAERO_Polar > L_D': ", vsp.GetNumData(polar_id, "L_D"))
    l_d = vsp.GetDoubleResults(polar_id, "L_D", 0)
    print(f"L/D = {l_d}\n")
    print("num of data in 'area': ", vsp.GetNumData(point_id, "area"))
    area = vsp.GetDoubleResults(point_id, "area", 0)
    print(f"area = {area}\n")
    print("num of data in 'VSPAERO_Polar > CMy'", vsp.GetNumData(polar_id, "CMy"))
    CMy = vsp.GetDoubleResults(polar_id, "CMy", 0)
    print(f"CMy = {CMy}\n")
    CDtot = vsp.GetDoubleResults(polar_id, "CDtot", 0)
    # 暂时想到给出这些数据 描述表面平坦度等其他约束条件的参数可能要想别的办法

    # # 这里储存一下结果文件，路径改一下就好了 应该多次迭代会覆盖的
    # vsp.WriteResultsCSVFile(test,
    #                         result_file)
    return cl, CMy, cdi, CDtot


def vsp_aero_0(x_cg, aoa, sref=0.781, bref=2.6, cref=0.303):  # 重心位置 迎角
    # 检查和清除否则模型会叠加干扰后续模型的建立
    vsp.VSPCheckSetup()
    vsp.VSPRenew()
    # result_file = "D:\\aircraft design competition\\24solar\\design_model\\whole_wing_optimization\\vsp"
    # "\\result.csv"
    # 几何文件写入
    filename_vsp_aero_ana = paths.vsp_file
    # 这里是为了调用几何
    vsp.ReadVSPFile(filename_vsp_aero_ana)

    # 分析文件命名
    comp_geom = "VSPAEROComputeGeometry"
    print(comp_geom)

    # 设置defaults
    vsp.SetAnalysisInputDefaults(comp_geom)
    analysis_name_results = vsp.ExecAnalysis(comp_geom)  # 返回的是一个ID
    print("The Geom Result:\n", analysis_name_results)
    # 把所有的分析模式全部输出来
    for analysis in vsp.ListAnalysis():
        print(analysis)

    # 分析方法
    analysis_name = "VSPAEROSweep"  # 找到一个适合的求解器 不要用single point
    vsp.SetIntAnalysisInput(comp_geom, "AnalysisMethod", (1, vsp.VORTEX_LATTICE))
    # 打印该求解器所有可以更改的参数
    # print("VSPAEROSweep 所有可选参数\n")
    # vsp.PrintAnalysisInputs(analysis_name)

    # 设置参考翼面

    # 手动设置 来自GUI总体参数确定后的 From Model
    S_ref = [sref]
    vsp.SetDoubleAnalysisInput(analysis_name, "Sref", S_ref, 0)
    b_ref = [bref]
    vsp.SetDoubleAnalysisInput(analysis_name, "bref", b_ref, 0)
    c_ref = [cref]
    vsp.SetDoubleAnalysisInput(analysis_name, "cref", c_ref, 0)
    # 自动计算设置 (暂时不成功)
    # ref_flag = [0]
    # vsp.SetIntAnalysisInput(analysis_name, "RefFlag", ref_flag, 0)
    vsp.Update()

    # 设置来流参数
    mach_speed = [0.02053]  # 7.00m/s altitude 0m
    vsp.SetDoubleAnalysisInput(analysis_name, "MachStart", mach_speed, 0)
    machNpts = [1]
    vsp.SetIntAnalysisInput(analysis_name, "MachNpts", machNpts, 0)
    alpha = [aoa]
    vsp.SetDoubleAnalysisInput(analysis_name, "AlphaStart", alpha, 0)
    alphaNpts = [1]
    vsp.SetIntAnalysisInput(analysis_name, "AlphaNpts", alphaNpts, 0)
    vsp.Update()
    rho = [1.225]  # 近地面大气密度参数
    vsp.SetDoubleAnalysisInput(analysis_name, "Rho", rho, 0)
    Re = [143651]  # 近地面 7m/s 参考长度为弦长 0.30m
    vsp.SetDoubleAnalysisInput(analysis_name, "ReCref", Re, 0)

    # 设置重心
    xcg = [x_cg]
    vsp.SetDoubleAnalysisInput(analysis_name, "Xcg", xcg, 0)

    # 高级设置
    N_cpu = [8]  # 调用CPU数目
    vsp.SetIntAnalysisInput(analysis_name, "NCPU", N_cpu, 0)
    Iter = [10]  # 迭代步数
    vsp.SetIntAnalysisInput(analysis_name, "WakeNumIter", Iter, 0)
    vsp.Update()
    print("analysis parameter modified\n COMPLETED\n")
    # print("VSPAEROSweep 参数输入结果\n")
    # vsp.PrintAnalysisInputs(analysis_name)

    # #############################################################
    # 进行中间的保存尝试 观察vsp3是否正常
    # file_name = "D:\\aircraft design competition\\24solar\\design_model\\whole_wing_optimization\\vsp\\test2.vsp3"
    # vsp.WriteVSPFile(file_name, vsp.SET_ALL)
    # #############################################################

    # 开始计算
    # #############################################################
    print("\tExecution...")
    _ = vsp.ExecAnalysis(analysis_name)
    print("COMPLETE")
    # #############################################################

    # 后处理
    # #############################################################
    # 返回一个列表里面是所有可用结果的名称
    _ = vsp.GetAllResultsNames()
    # 查找point的ID并赋值给point_id
    point_id = vsp.FindResultsID("point")
    # 一样的也是一个查找
    polar_id = vsp.FindResultsID("VSPAERO_Polar")

    # 用来了解可用的结果集合和数据的名称（全部打印出来）
    # for result in results:
    #     data_names = vsp.GetAllDataNames(vsp.FindResultsID(result))
    #     for data_name in data_names:
    #         print(f"{result} > {data_name}")

    # 用来统计CL的数据量并打印第一个
    print("num of data in 'VSPAERO_Polar > CL': ", vsp.GetNumData(polar_id, "CL"))
    cl = vsp.GetDoubleResults(polar_id, "CL", 0)
    print(f"CL = {cl}\n")
    print("num of data in 'VSPAERO_Polar > CDi': ", vsp.GetNumData(polar_id, "CDi"))
    cdi = vsp.GetDoubleResults(polar_id, "CDi", 0)
    print(f"CDi = {cdi}\n")
    # 这里的polar_id 赋值的是"VSPAERO_Polar" 也就是结果组的一个值 引用了结果组"VSPAERO_Polar"的L_D的部分
    print("num of data in 'VSPAERO_Polar > L_D': ", vsp.GetNumData(polar_id, "L_D"))
    l_d = vsp.GetDoubleResults(polar_id, "L_D", 0)
    print(f"L/D = {l_d}\n")
    print("num of data in 'area': ", vsp.GetNumData(point_id, "area"))
    area = vsp.GetDoubleResults(point_id, "area", 0)
    print(f"area = {area}\n")
    print("num of data in 'VSPAERO_Polar > CMy'", vsp.GetNumData(polar_id, "CMy"))
    CMy = vsp.GetDoubleResults(polar_id, "CMy", 0)
    print(f"CMy = {CMy}\n")
    CDtot = vsp.GetDoubleResults(polar_id, "CDtot", 0)
    # 暂时想到给出这些数据 描述表面平坦度等其他约束条件的参数可能要想别的办法

    # # 这里储存一下结果文件，路径改一下就好了 应该多次迭代会覆盖的
    # vsp.WriteResultsCSVFile(test,
    #                         result_file)
    return cl, CMy, cdi, CDtot


# #############################################################
# ####################vsp-aero多点配平##########################
# #############################################################
def vsp_aero_sweep(x_cg):
    # 检查和清除否则模型会叠加干扰后续模型的建立
    vsp.VSPCheckSetup()
    vsp.VSPRenew()

    # 几何文件写入
    filename_vsp_aero_ana = paths.vsp_file
    # 这里是为了调用几何
    vsp.ReadVSPFile(filename_vsp_aero_ana)

    # 分析文件命名
    comp_geom = "VSPAEROComputeGeometry"
    print(comp_geom)

    # 设置defaults
    vsp.SetAnalysisInputDefaults(comp_geom)
    vsp.ExecAnalysis(comp_geom)
    # analysis_name_results = vsp.ExecAnalysis(comp_geom)  # 返回的是一个ID
    # print("The Geom Result:\n", analysis_name_results)
    # 把所有的分析模式全部输出来
    # for analysis in vsp.ListAnalysis():
    #     print(analysis)

    # 分析方法
    analysis_name = "VSPAEROSweep"  # 找到一个适合的求解器 不要用single point
    vsp.SetIntAnalysisInput(comp_geom, "AnalysisMethod", (1, vsp.VORTEX_LATTICE))
    # 打印该求解器所有可以更改的参数
    # print("VSPAEROSweep 所有可选参数\n")
    # vsp.PrintAnalysisInputs(analysis_name)

    # 设置参考翼面

    # 手动设置 来自GUI总体参数确定后的 From Model
    S_ref = [0.763]
    vsp.SetDoubleAnalysisInput(analysis_name, "Sref", S_ref, 0)
    b_ref = [2.540]
    vsp.SetDoubleAnalysisInput(analysis_name, "bref", b_ref, 0)
    c_ref = [0.304]
    vsp.SetDoubleAnalysisInput(analysis_name, "cref", c_ref, 0)

    # 自动计算设置 (暂时不成功)
    # ref_flag = [0]
    # vsp.SetIntAnalysisInput(analysis_name, "RefFlag", ref_flag, 0)
    vsp.Update()

    # 设置来流参数
    mach_speed = [0.02053]  # 7.00m/s altitude 0m
    vsp.SetDoubleAnalysisInput(analysis_name, "MachStart", mach_speed, 0)
    machNpts = [1]
    vsp.SetIntAnalysisInput(analysis_name, "MachNpts", machNpts, 0)
    alpha_start = [1]
    vsp.SetDoubleAnalysisInput(analysis_name, "AlphaStart", alpha_start, 0)
    alpha_end = [5]
    vsp.SetDoubleAnalysisInput(analysis_name, "AlphaEnd", alpha_end, 0)
    alphaNpts = [5]
    vsp.SetIntAnalysisInput(analysis_name, "AlphaNpts", alphaNpts, 0)
    vsp.Update()
    rho = [1.225]  # 近地面大气密度参数
    vsp.SetDoubleAnalysisInput(analysis_name, "Rho", rho, 0)
    Re = [143651]  # 近地面 7m/s 参考长度为弦长 0.30m
    vsp.SetDoubleAnalysisInput(analysis_name, "ReCref", Re, 0)

    # 设置重心
    xcg = [x_cg]
    vsp.SetDoubleAnalysisInput(analysis_name, "Xcg", xcg, 0)

    # 高级设置
    N_cpu = [8]  # 调用CPU数目
    vsp.SetIntAnalysisInput(analysis_name, "NCPU", N_cpu, 0)
    Iter = [10]  # 迭代步数
    vsp.SetIntAnalysisInput(analysis_name, "WakeNumIter", Iter, 0)
    vsp.Update()
    print("analysis parameter modified\n COMPLETED\n")
    # print("VSPAEROSweep 参数输入结果\n")
    # vsp.PrintAnalysisInputs(analysis_name)

    # #############################################################
    # # 进行中间的保存尝试 观察vsp3是否正常
    # file_name = "D:\\aircraft design competition\\24solar\\design_model\\whole_wing_optimization\\vsp\\test2.vsp3"
    # vsp.WriteVSPFile(file_name, vsp.SET_ALL)
    # ##############################################################
    # 开始计算

    # #############################################################
    print("\tExecution...")
    vsp.ExecAnalysis(analysis_name)
    print("COMPLETE")
    # #############################################################

    # 后处理
    # #############################################################
    # # 返回一个列表里面是所有可用结果的名称
    # results = vsp.GetAllResultsNames()
    # # 查找point的ID并赋值给point_id
    # point_id = vsp.FindResultsID("point")
    # # 一样的也是一个查找
    polar_id = vsp.FindResultsID("VSPAERO_Polar")
    print("num of data in 'VSPAERO_Polar > CMy'", vsp.GetNumData(polar_id, "CMy"))
    CMy = vsp.GetDoubleResults(polar_id, "CMy", 0)
    print(f"CMy = {CMy}\n")
    return CMy


def vsp_aero_sweep_0(start, end):
    x_cg = 0
    # 检查和清除否则模型会叠加干扰后续模型的建立
    vsp.VSPCheckSetup()
    vsp.VSPRenew()

    # 几何文件写入
    filename_vsp_aero_ana = paths.vsp_file
    # 这里是为了调用几何
    vsp.ReadVSPFile(filename_vsp_aero_ana)

    # 分析文件命名
    comp_geom = "VSPAEROComputeGeometry"
    # print(comp_geom)

    # 设置defaults
    vsp.SetAnalysisInputDefaults(comp_geom)
    vsp.ExecAnalysis(comp_geom)

    # 分析方法
    analysis_name = "VSPAEROSweep"  # 找到一个适合的求解器 不要用single point
    vsp.SetIntAnalysisInput(comp_geom, "AnalysisMethod", (1, vsp.VORTEX_LATTICE))

    # 手动设置 来自GUI总体参数确定后的 From Model
    S_ref = [0.763]
    vsp.SetDoubleAnalysisInput(analysis_name, "Sref", S_ref, 0)
    b_ref = [2.540]
    vsp.SetDoubleAnalysisInput(analysis_name, "bref", b_ref, 0)
    c_ref = [0.304]
    vsp.SetDoubleAnalysisInput(analysis_name, "cref", c_ref, 0)
    # 自动计算设置 (暂时不成功)
    # ref_flag = [0]
    # vsp.SetIntAnalysisInput(analysis_name, "RefFlag", ref_flag, 0)
    vsp.Update()
    vsp.Update()

    # 设置来流参数
    mach_speed = [0.02053]  # 7.00m/s altitude 0m
    vsp.SetDoubleAnalysisInput(analysis_name, "MachStart", mach_speed, 0)
    machNpts = [1]
    vsp.SetIntAnalysisInput(analysis_name, "MachNpts", machNpts, 0)
    alpha_start = [start]
    vsp.SetDoubleAnalysisInput(analysis_name, "AlphaStart", alpha_start, 0)
    alpha_end = [end]
    vsp.SetDoubleAnalysisInput(analysis_name, "AlphaEnd", alpha_end, 0)
    alphaNpts = [5]
    vsp.SetIntAnalysisInput(analysis_name, "AlphaNpts", alphaNpts, 0)
    vsp.Update()
    rho = [1.225]  # 近地面大气密度参数
    vsp.SetDoubleAnalysisInput(analysis_name, "Rho", rho, 0)
    Re = [143651]  # 近地面 7m/s 参考长度为弦长 0.30m
    vsp.SetDoubleAnalysisInput(analysis_name, "ReCref", Re, 0)

    # 设置重心
    xcg = [x_cg]
    vsp.SetDoubleAnalysisInput(analysis_name, "Xcg", xcg, 0)

    # 高级设置
    N_cpu = [8]  # 调用CPU数目
    vsp.SetIntAnalysisInput(analysis_name, "NCPU", N_cpu, 0)
    Iter = [10]  # 迭代步数
    vsp.SetIntAnalysisInput(analysis_name, "WakeNumIter", Iter, 0)
    vsp.Update()
    print("analysis parameter modified\n COMPLETED\n")
    # print("VSPAEROSweep 参数输入结果\n")
    # vsp.PrintAnalysisInputs(analysis_name)

    # #############################################################
    # # 进行中间的保存尝试 观察vsp3是否正常
    # file_name = "D:\\aircraft design competition\\24solar\\design_model\\whole_wing_optimization\\vsp\\test2.vsp3"
    # vsp.WriteVSPFile(file_name, vsp.SET_ALL)
    # ##############################################################
    # 开始计算

    # #############################################################
    print("\tExecution...")
    vsp.ExecAnalysis(analysis_name)
    print("COMPLETE")
    # #############################################################

    # 后处理
    # #############################################################
    # # 返回一个列表里面是所有可用结果的名称
    # results = vsp.GetAllResultsNames()
    # # 查找point的ID并赋值给point_id
    # point_id = vsp.FindResultsID("point")
    # # 一样的也是一个查找
    polar_id = vsp.FindResultsID("VSPAERO_Polar")
    print("num of data in 'VSPAERO_Polar > CMy'", vsp.GetNumData(polar_id, "CMy"))
    CMy = vsp.GetDoubleResults(polar_id, "CMy", 0)
    print(f"CMy = {CMy}\n")
    print("num of data in 'VSPAERO_Polar > CL': ", vsp.GetNumData(polar_id, "CL"))
    cl = vsp.GetDoubleResults(polar_id, "CL", 0)
    print(f"CL = {cl}\n")
    return CMy, cl


def vsp_aero_sweep_1(start, end, num, sref=0.781, bref=2.600, cref=0.303, xcg=0.25859):
    # 检查和清除否则模型会叠加干扰后续模型的建立
    vsp.VSPCheckSetup()
    vsp.VSPRenew()

    # 几何文件写入
    filename_vsp_aero_ana = paths.vsp_file
    # 这里是为了调用几何
    vsp.ReadVSPFile(filename_vsp_aero_ana)

    # 分析文件命名
    comp_geom = "VSPAEROComputeGeometry"
    # print(comp_geom)

    # 设置defaults
    vsp.SetAnalysisInputDefaults(comp_geom)
    vsp.ExecAnalysis(comp_geom)

    # 分析方法
    analysis_name = "VSPAEROSweep"  # 找到一个适合的求解器 不要用single point
    vsp.SetIntAnalysisInput(comp_geom, "AnalysisMethod", (1, vsp.VORTEX_LATTICE))

    # 手动设置 来自GUI总体参数确定后的 From Model
    S_ref = [sref]
    vsp.SetDoubleAnalysisInput(analysis_name, "Sref", S_ref, 0)
    b_ref = [bref]
    vsp.SetDoubleAnalysisInput(analysis_name, "bref", b_ref, 0)
    c_ref = [cref]
    vsp.SetDoubleAnalysisInput(analysis_name, "cref", c_ref, 0)
    # 自动计算设置 (暂时不成功)
    # ref_flag = [0]
    # vsp.SetIntAnalysisInput(analysis_name, "RefFlag", ref_flag, 0)
    vsp.Update()
    vsp.Update()

    # 设置来流参数
    mach_speed = [0.02053]  # 7.00m/s altitude 0m
    vsp.SetDoubleAnalysisInput(analysis_name, "MachStart", mach_speed, 0)
    machNpts = [1]
    vsp.SetIntAnalysisInput(analysis_name, "MachNpts", machNpts, 0)
    alpha_start = [start]
    vsp.SetDoubleAnalysisInput(analysis_name, "AlphaStart", alpha_start, 0)
    alpha_end = [end]
    vsp.SetDoubleAnalysisInput(analysis_name, "AlphaEnd", alpha_end, 0)
    alphaNpts = [num]
    vsp.SetIntAnalysisInput(analysis_name, "AlphaNpts", alphaNpts, 0)
    vsp.Update()
    rho = [1.225]  # 近地面大气密度参数
    vsp.SetDoubleAnalysisInput(analysis_name, "Rho", rho, 0)
    Re = [143651]  # 近地面 7m/s 参考长度为弦长 0.30m
    vsp.SetDoubleAnalysisInput(analysis_name, "ReCref", Re, 0)

    # 设置重心
    xcg = [xcg]
    vsp.SetDoubleAnalysisInput(analysis_name, "Xcg", xcg, 0)

    # 高级设置
    N_cpu = [8]  # 调用CPU数目
    vsp.SetIntAnalysisInput(analysis_name, "NCPU", N_cpu, 0)
    Iter = [10]  # 迭代步数
    vsp.SetIntAnalysisInput(analysis_name, "WakeNumIter", Iter, 0)
    vsp.Update()
    print("analysis parameter modified\n COMPLETED\n")
    # print("VSPAEROSweep 参数输入结果\n")
    # vsp.PrintAnalysisInputs(analysis_name)

    # #############################################################
    # # 进行中间的保存尝试 观察vsp3是否正常
    # file_name = "D:\\aircraft design competition\\24solar\\design_model\\whole_wing_optimization\\vsp\\test2.vsp3"
    # vsp.WriteVSPFile(file_name, vsp.SET_ALL)
    # ##############################################################
    # 开始计算

    # #############################################################
    print("\tExecution...")
    vsp.ExecAnalysis(analysis_name)
    print("COMPLETE")
    # #############################################################

    # 后处理
    # #############################################################
    # # 返回一个列表里面是所有可用结果的名称
    # results = vsp.GetAllResultsNames()
    # # 查找point的ID并赋值给point_id
    # point_id = vsp.FindResultsID("point")
    # # 一样的也是一个查找
    polar_id = vsp.FindResultsID("VSPAERO_Polar")
    print("num of data in 'VSPAERO_Polar > CMy'", vsp.GetNumData(polar_id, "CMy"))
    CMy = vsp.GetDoubleResults(polar_id, "CMy", 0)
    print(f"CMy = {CMy}\n")
    print("num of data in 'VSPAERO_Polar > CL': ", vsp.GetNumData(polar_id, "CL"))
    cl = vsp.GetDoubleResults(polar_id, "CL", 0)
    print(f"CL = {cl}\n")
    cdi = vsp.GetDoubleResults(polar_id, "CDi", 0)
    print(f"cdi = {cdi}\n")
    return CMy, cl


# #############################################################
# #################### 简单的demo与测试 #########################
# #############################################################
# vsp_aero_sweep_0(-4, 4)
# vsp_aero(0.25, 5)
# 用来测试几何体是否成功生成
# create_Geom_3(paths.tip_file, paths.mid_file, paths.root_file)
# vsp_aero_sweep_1(-5, 5, 2)
# create_Geom_4(paths.tip_file, paths.mid_file, paths.root_file, angle=30)

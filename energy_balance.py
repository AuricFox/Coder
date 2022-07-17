class Flow: #Calculates mole fractions of liquid and vapor
    def __init__(
            self, A1=0, B1=0, C1=0, A2=0, B2=0, C2=0,
            Z_A=0, Z_B=0,
            temp_i=20, temp_f=20, pressure_i=760, pressure_f=760
            ):
        #---Antinoe Coeffiecents---
        self.A1 = A1
        self.B1 = B1
        self.C1 = C1
        self.A2 = A2
        self.B2 = B2
        self.C2 = C2
        #---Inlet flow composition---
        self.Z_A = Z_A
        self.Z_B = Z_B
        #---Temperature (C)---
        self.t_i = temp_i
        self.t_f = temp_f
        #---Pressure (mmHg)---
        self.p_i = pressure_i
        self.p_f = pressure_f
        #---Partial pressures---
        self.P_SA = 10**(self.A1 - self.B1 / (self.t_f + self.C1))
        self. P_SB = 10**(self.A2 - self.B2 / (self.t_f + self.C2))
        #---Liquid mole fractions---
        self.XA = (self.p_f - self.P_SB) / (self.P_SA - self.P_SB)
        self.XB = (self.p_f - self.P_SA) / (self.P_SB - self.P_SA)
        #---Vapor mole fractions---
        self.YA = (self.P_SA / self.p_f) * self.XA
        self.YB = (self.P_SB / self.p_f) * self.XB
        #---Liquid flow stream---
        self.L_flow = ((self.Z_B - self.YB * (self.Z_A / self.YA)) / 
                       (self.XB - self.YB * (self.XA / self.YA)))
        #---Vapor flow stream---
        self.V_flow = ((self.Z_B - self.XB * (self.Z_A / self.XA)) / 
                       (self.YB - self.XB * (self.YA / self.XA)))
        
    def P_SA(self): #Returns partial pressure of sol A
        return self.P_SA
    def P_SB(self): #Returns partial pressure of sol B
        return self.P_SB
    #===Setter Functions=======================================================
    def SetXA(self, XA): #Returns liquid fraction of sol A
        self.XA = XA
    def SetXB(self, XB): #Returns liquid fraction of sol B
        self.XB = XB
    
    def setYA(self, YA): #Returns vapor fraction of solution A
        self.YA = YA
    def SetYB(self, YB): #Returns vapor fraction of solution B
        self.YB = YB
    
    def SetL_flow(self, L_flow): #Returns outlet fraction of liquid
        self.L_flow = L_flow
    def SetV_flow(self, V_flow): #Returns outlet fraction of vapor
        self.V_flow = V_flow
    #===Getter Functions=======================================================
    def XA(self): #Returns liquid fraction of sol A
        return self.XA
    def XB(self): #Returns liquid fraction of sol B
        return self.XB
    
    def YA(self): #Returns vapor fraction of solution A
        return self.YA
    def YB(self): #Returns vapor fraction of solution B
        return self.YB
    
    def L_flow(self): #Returns outlet fraction of liquid
        return self.L_flow
    def V_flow(self): #Returns outlet fraction of vapor
        return self.V_flow
    
    def __str__(self):
        return (
                "Liquid A: " + str(self.XA) +
                "\nLiquid B: " + str(self.XB) +
                "\nVapor A: " + str(self.YA) +
                "\nVapor B: " + str(self.YB) +
                "\nLiquid Fraction: " + str(self.L_flow) +
                "\nVapor Fraction: " + str(self.V_flow)
                )
class Energy(Flow): #Calculates energy input
    def __init__(
            self, A1=0, B1=0, C1=0, A2=0, B2=0, C2=0, Z_A=1, Z_B=0,
            temp_i=20, temp_f=20, pressure_i=760, pressure_f=760,
            Cp_LA=0, Cp_VA=0, Cp_LB=0, Cp_VB=0,
            H_VA=0, H_VB=0, Tnbp_A=100, Tnbp_B=100
            ):
        Flow.__init__(
            self, A1, B1, C1, A2, B2, C2,
            Z_A, Z_B,
            temp_i, temp_f, pressure_i, pressure_f
            )
        #---Heat capacity (J/mol*C)---
        self.Cp_LA = Cp_LA
        self.Cp_VA = Cp_VA
        self.Cp_LB = Cp_LB
        self.Cp_VB = Cp_VB
        #---Enthalpy of Reaction (J/mol)---
        self.H_VA = H_VA
        self.H_VB = H_VB
        #---Normal boiling point (C)---
        self.Tnbp_A = Tnbp_A
        self.Tnbp_B = Tnbp_B
        #---Enthalpy of liquids---
        self.dH_LA = self.Cp_LA * (self.t_f - self.t_i)
        self.dH_LB = self.Cp_LB * (self.t_f - self.t_i)
        #---Enthalpy of vapors---
        self.dH_VA = (self.Cp_LA * (self.Tnbp_A - self.t_i) + self.H_VA + 
                      self.Cp_VA * (self.t_f - self.Tnbp_A))
        self.dH_VB = (self.Cp_LB * (self.Tnbp_B - self.t_i) + self.H_VB + 
                      self.Cp_VB * (self.t_f - self.Tnbp_B))
        #---Heat added---
        self.Q = (self.V_flow * (self.YA * self.dH_VA + self.YB * self.dH_VB) + 
            self.L_flow * (self.XA * self.dH_LA + self.XB * self.dH_LB))
    
    def EnthalpyLiquidA(self): #Returns difference in enthalpy of liq A
        return self.dH_LA #Value is small
    def EnthalpyLiquidB(self): #Returns difference in enthalpy of lid B
        return self.dH_LB #Value is small
    
    def EnthalpyVaporA(self): #Returns difference in enthalpy of vap A
        return self.dH_VA
    def EnthalpyVaporB(self): #Returns difference in enthalpy of vap B
        return self.dH_VB
    
    def HeatAdded(self): #Returns heat difference
        return self.Q
    def __str__(self):
        return (
                "Liquid A: " + str(self.XA) +
                "\nLiquid B: " + str(self.XB) +
                "\nVapor A: " + str(self.YA) +
                "\nVapor B: " + str(self.YB)  +
                "\nLiquid Fraction: " + str(self.L_flow) +
                "\nVapor Fraction: " + str(self.V_flow) +
                "\nEnthalpy of Liqiud A: " + str(self.dH_LA) +
                "\nEnthalpy of Liquid B: " + str(self.dH_LB) +
                "\nEnthalpy of Vapor A: " + str(self.dH_VA) +
                "\nEnthalpy of Vapor B: " + str(self.dH_VB) +
                "\nHeat: " + str(self.Q)
                )
        
        
if __name__ == "__main__":
    response = str(input("Testing program (Y/N)? "))
    if (response == "Y") or (response == "y"):
        A1 = 6.87601
        B1 = 1171.17
        C1 = 224.41
        A2 = 6.89677
        B2 = 1264.90
        C2 = 216.54
        Z_A = .75
        Z_B = .25
        t_i = 25
        t_f = 75
        p_i = 760
        p_f = 760
        Cp_LA = 189.1
        Cp_VA = 143.1 
        Cp_LB = 212
        Cp_VB = 165.9
        H_VA = 28900
        H_VB = 31800
        Tnbp_A = 68.74
        Tnbp_B = 98.9
        
#        s1 = MoleFractions(A1,B1,C1,A2,B2,C2,Z_A,Z_B,t_i,t_f)
#        print(s1)
#        print(MoleFractions.SolutionA_Pressure(s1))
#        print(MoleFractions.SolutionB_Pressure(s1))
        
        s1 = Flow(
                A1, B1, C1, A2, B2, C2, Z_A, Z_B, t_i, t_f, p_i, p_f,
                #Cp_LA, Cp_VA, Cp_LB, Cp_VB, H_VA, H_VB, Tnbp_A, Tnbp_B
                )
        print(s1)
    elif (response == "N") or (response == "n"):
        A1 = float(input("Antinoe A coeffiecent for component A? "))
        B1 = float(input("Antinoe B coeffiecent for component A? "))
        C1 = float(input("Antinoe C coeffiecent for component A? "))
        A2 = float(input("Antinoe A coeffiecent for component B? "))
        B2 = float(input("Antinoe B coeffiecent for component B? "))
        C2 = float(input("Antinoe C coeffiecent for component B? "))
        Z_A = float(input("Mole fraction of component A at inlet? "))
        Z_B = float(input("Mole fraction of component B at inlet? "))
        t_i = float(input("Initial temperature(C)? "))
        t_f = float(input("Final temperature(C)? "))
        p_i = float(input("Initial Pressure(mmHg)? "))
        p_f = float(input("Final Pressure(mmHg)? "))
        Cp_LA = float(input("Liquid heat capacity of component A(J/mol*C)? "))
        Cp_VA = float(input("Vapor heat capacity of component A(J/mol*C)? "))
        Cp_LB = float(input("Liquid heat capacity of component B(J/mol*C)? "))
        Cp_VB = float(input("Vapor heat capacity of component B(J/mol*C)? "))
        H_VA = float(input("Enthalpy of formation of vapor component A(J/mol)? "))
        H_VB = float(input("Enthalpy of formation of vapor component B(J/mol)? "))
        Tnbp_A = float(input("Normal boiling point of component A(C)? "))
        Tnbp_B = float(input("Normal boiling point of component B(C)? "))
        s2 = Energy(
                A1, B1, C1, A2, B2, C2, Z_A, Z_B, t_i, t_f, p_i, p_f,
                Cp_LA, Cp_VA, Cp_LB, Cp_VB, H_VA, H_VB, Tnbp_A, Tnbp_B
                )
        print(s2)
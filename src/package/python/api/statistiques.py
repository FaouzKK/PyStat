from fpdf import FPDF

class Statistique:

    def __init__(self,statistique:list[dict]) -> None:
        self.satistique = statistique
    



    def get_somme_effectif(self) -> int:
        global somme_effectif
        somme_effectif = 0

        for eff in self.satistique :
            data : int = eff["ni"]
            somme_effectif += data

        return somme_effectif
    
    def get_moyenne(self) -> int:
        return self.get_xini() / self.get_somme_effectif() # type: ignore



    def get_mode(self) -> list[int]:
        global big_eff 
        big_eff = 0 
        for eff in self.satistique :
            data : int = eff["ni"]
            if data > big_eff :
                big_eff = data

        global mode
        mode = []
        for thisdata in self.satistique :
            if  thisdata["ni"] == big_eff :
                value:int = int(thisdata["xi"])
                mode.append(value) # type: ignore

        return mode
    
          
    def get_xini(self, xi:int|None = None) ->int|str :
        global value 
        if xi == None :
            value = 0
            for eff in self.satistique :
                value += eff["xi"] * eff["ni"]

            return value

        else :
            value = None
            for eff in self.satistique :
                if eff["xi"] == xi :
                    value = eff["ni"] * eff["xi"]

            if value == None :
                return "xi not found"

            return value
        
    
    def get_variance(self) -> int:
        x_barre_carrer = self.get_moyenne() ** 2
        
        global x_carrer_barre

        xi_carrer_ni = 0

        for data in self.satistique :
            xi_carrer_ni += (data["xi"] ** 2 )* data["ni"]

        x_carrer_barre = xi_carrer_ni / self.get_somme_effectif()

        return x_carrer_barre - x_barre_carrer # type: ignore
    
    def get_ecart_type(self) -> int:
        return self.get_variance() ** 0.5
    
    
    def get_pdf(self, filename="statistique.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 12)
        
        # Add table header
        pdf.cell(40, 10, "xi", 1)
        pdf.cell(40, 10, "ni", 1)
        pdf.ln()
        
        # Add table data
        for data in self.satistique:
            pdf.cell(40, 10, str(data["xi"]), 1)
            pdf.cell(40, 10, str(data["ni"]), 1)
            pdf.ln()
        
        # Add calculations
        pdf.ln(10)
        pdf.cell(40, 10, f"Somme des effectifs: {self.get_somme_effectif()}")
        pdf.ln()
        pdf.cell(40, 10, f"Moyenne: {self.get_moyenne()}")
        pdf.ln()
        pdf.cell(40, 10, f"Mode: {', '.join(map(str, self.get_mode()))}")
        pdf.ln()
        pdf.cell(40, 10, f"Variance: {self.get_variance()}")
        pdf.ln()
        pdf.cell(40, 10, f"Ecart type: {self.get_ecart_type()}")
        
        pdf.output(filename)
    



class Statistique_double:
    def __init__(self,stat_xy: list[dict[str,int]]) -> None:
        self.stat_xy = stat_xy
        self.stat_x : list[dict] = []
        self.stat_y : list[dict] = []

        for stat in stat_xy :
            xi :dict = {
                "xi" : stat["xi"],
                "ni" : 1
            }
            yi : dict = {
                "xi" : stat["yi"],
                "ni" : 1
            }
            self.stat_x.append(xi)
            self.stat_y.append(yi)

    
    def get_stat_x(self) :
        return Statistique(self.stat_x)
    
    def get_stat_y(self) :
        return Statistique(self.stat_y)
    
    def get_sum_n(self) :
        return len(self.stat_x)
    

    def get_xiyi(self,i : int|None = None) :
        if i == None :
            global value
            value = 0
            for stat in self.stat_xy :
                value += (stat["xi"] * stat["yi"])
            return value
        
        else :
            try :
                i = i-1
                return self.stat_xy[i]["xi"] + self.stat_xy[i]["yi"]
            except :
                raise ValueError("L'indice entre n'est pas inclus dans le tableau fournis")



    def get_cov_xy(self) :
        return  ((self.get_xiyi() / self.get_sum_n() ) - (self.get_stat_x().get_moyenne() * self.get_stat_y().get_moyenne()))
    
    
    def get_a(self) :
        return (self.get_cov_xy() /self.get_stat_x().get_variance())
    
    def get_b(self) :
        return self.get_stat_y().get_moyenne() - (self.get_a() * self.get_stat_x().get_moyenne())

    
    def get_coefficient_corellation(self) :
        return self.get_cov_xy() / (self.get_stat_x().get_ecart_type() * self.get_stat_y().get_ecart_type())
    
    def get_pdf(self, filename="statistique_double.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 12)
        
        # Add table header
        pdf.cell(40, 10, "xi", 1)
        pdf.cell(40, 10, "yi", 1)
        pdf.ln()
        
        # Add table data
        for data in self.stat_xy:
            pdf.cell(40, 10, str(data["xi"]), 1)
            pdf.cell(40, 10, str(data["yi"]), 1)
            pdf.ln()
        
        # Add calculations
        pdf.ln(10)
        pdf.cell(40, 10, f"Somme des n: {self.get_sum_n()}")
        pdf.ln()
        pdf.cell(40, 10, f"Covariance XY: {self.get_cov_xy()}")
        pdf.ln()
        pdf.cell(40, 10, f"a: {self.get_a()}")
        pdf.ln()
        pdf.cell(40, 10, f"b: {self.get_b()}")
        pdf.ln()
        pdf.cell(40, 10, f"Coefficient de corrélation: {self.get_coefficient_corellation()}")
        
        pdf.output(filename)



if __name__ == "__main__" :
    data = [
        {
            "xi" : 5,
            "yi" : 25
        },
        {
            "xi" : 6,
            "yi" : 30
        },
        {
            "xi" : 9,
            "yi" : 35
        },
        {
            "xi" : 12,
            "yi" : 45
        },
        {
            "xi" : 18,
            "yi" : 65
        }
    ]

    new_stat = Statistique_double(data)

    print(new_stat.get_coefficient_corellation())


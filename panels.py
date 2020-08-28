# Solar Panel Class
class SolarPanel:

    def __init__(self, name, price=0, pmax=0, vmp=0, imp=0, voc=0, isc=0, efficiency=0, op_temp=0, p_coeff=0, v_coeff=0,
                 i_coeff=0, ff=0, n_s=0, n_p=0, notc=0):
        self.notc = notc
        self.n_p = n_p
        self.n_s = n_s
        self.imp = imp
        self.i_coeff = i_coeff
        self.v_coeff = v_coeff
        self.p_coeff = p_coeff
        self.name = name
        self.price = price
        self.pmax = pmax
        self.vmp = vmp
        self.voc = voc
        self.isc = isc
        self.efficiency = efficiency
        self.op_temp = op_temp
        self.ff = self.generate_ff()

    def generate_ff(self) -> float:
        return self.pmax / (self.voc * self.isc)

    def get_coeffs(self) -> tuple:
        return self.p_coeff, self.v_coeff, self.i_coeff


# Solar Profile class, could be joined with the panel class
class SolarProfile:

    def __init__(self, panel: SolarPanel):
        self.panel = panel

    def p_pv(self, v, i) -> float:
        return self.panel.n_s * self.panel.n_p * v * i * self.panel.ff

    def i_sc(self, t_c, g) -> float:
        return (self.panel.isc + (self.panel.i_coeff * (t_c - 25))) * (g / 1000)

    def v_oc(self, t_c) -> float:
        return self.panel.voc - (self.panel.v_coeff * t_c)

    def temperature_c(self, t_a, g) -> float:
        return t_a + (((self.panel.notc - 20) / 1000) * g)

    def get_power(self, t_a, g) -> float:
        t_c = self.temperature_c(t_a, g)
        v_oc = self.v_oc(t_c)
        i_sc = self.i_sc(t_c, g)
        p_pv = self.p_pv(v_oc, i_sc)
        return p_pv

    def get_voltage(self, t_a, g) -> float:
        t_c = self.temperature_c(t_a, g)
        v_oc = self.v_oc(t_c)
        return v_oc

    def get_current(self, t_a, g) -> float:
        t_c = self.temperature_c(t_a, g)
        i_sc = self.i_sc(t_c, g)
        return i_sc

import numpy as np;
from scipy import io as spio;
from scipy import special as special;
from scipy import linalg;
from scipy import optimize;
import matplotlib.pyplot as plt;

print("\n\r");
print("====================================");
print("数值积分：scipy.integrate");
print("====================================");
#最通用的积分程序是scipy.integrate.quad()
from scipy.integrate import quad;
res, err = quad(np.sin, 0, np.pi/2);
print(np.allclose(res, 1));

print(np.allclose(err, 1 - res));

def calc_derivative(ypos, time, counter_arr):
    counter_arr += 1;
    return -2 * ypos;
#弹道将被计算
from scipy.integrate import odeint;
time_vec = np.linspace(0, 4, 40);
counter = np.zeros((1,), dtype=np.uint16);
yvec, info = odeint(calc_derivative, 1, time_vec, args=(counter,), full_output=True);
print("counter====>", counter);
print(info['nfe'][:10]);

mass = 0.5;
kspring = 4;
cviscous = 0.4;
eps = cviscous / (2 * mass * np.sqrt(kspring/mass));
print(eps<1);

nu_coef = cviscous / mass;
om_coef = kspring / mass;
print("nu_coef===>", nu_coef);
print("om_coef===>", om_coef);


#因此函数将计算速度和加速度通过
def calc_deri(yvec, time, nuc, omc):
    return (yvec[1], -nuc * yvec[1] - omc*yvec[0]);
time_vec = np.linspace(0, 10, 100);
yarr = odeint(calc_deri, (1, 0), time_vec, args=(nu_coef, om_coef))
print("time_vec===>", time_vec);
print("yarr===>", yarr);










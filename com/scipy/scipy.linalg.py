import numpy as np;
from scipy import io as spio;
from scipy import special as special;
from scipy import linalg;

print("\n\r");
print("====================================");
print("线性代数运算：scipy.linalg");
print("====================================");

print("=== scipy.linalg.det()函数计算方阵的行列式 ===");
arr = np.array([
    [1, 2],
    [3, 4]
]);
det = linalg.det(arr);
print(det);
#print(linalg.det(np.noes(3, 4)));

print("=== scipy.linalg.inv()计算方阵的逆");
iarr = linalg.inv(arr);
print(iarr);

print("=== 奇异值分解 ===");
arr = np.arange(9).reshape((3, 3)) + np.diag([1, 0, 1])
print(arr);
uarr, spec, vharr = linalg.svd(arr);
print(spec);
print(uarr);
print(vharr);


sarr = np.diag(spec)
svd_mat = uarr.dot(sarr).dot(vharr);
print(svd_mat);
sdata = np.allclose(svd_mat, arr)
print(sdata);
















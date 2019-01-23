import numpy as np;
from scipy import io as spio;
from scipy import special as special;
from scipy import linalg;
from scipy import optimize;
import matplotlib.pyplot as plt;
from scipy import signal;
from scipy import ndimage;
from scipy import misc;

print("\n\r");
print("====================================");
print("图像处理：scipy.ndimage");
print("====================================");

print("=== 图像的几何变换 ===");
#改变方向，分辨率等
from scipy import misc;
#lena = misc.lena()
lena = misc.ascent();
shifted_lena = ndimage.shift(lena, (50, 50))
shifted_lena2 = ndimage.shift(lena, (50, 50), mode='nearest')
rotated_lena = ndimage.rotate(lena, 30)
cropped_lena = lena[50:-50, 50:-50];
zoomed_lena = ndimage.zoom(lena, 2);
print(zoomed_lena.shape);

print(plt.subplot(321));

#pl.imshow(lena, cmap=cm.gray);
print(plt.subplot(322));
#plt.show();


print("=== 图像滤镜 === ");

noisy_lena = np.copy(lena).astype(np.float)
noisy_lena += lena.std()*0.5*np.random.standard_normal(lena.shape)
blurred_lena = ndimage.gaussian_filter(noisy_lena, sigma=3)
median_lena = ndimage.median_filter(blurred_lena, size=5)
from scipy import signal
wiener_lena = signal.wiener(blurred_lena, (5,5));
print("wiener_lena====>", wiener_lena);
#许多其它scipy.ndimage.filters和scipy.signal中的滤镜可以被应用到图像中


print("=== 数学形态学 ===");
el = ndimage.generate_binary_structure(2, 1);
print("el===>", el);
print(el.astype(np.int));

#腐蚀
a = np.zeros((7,7), dtype=int);
a[1:6, 2:5] = 1;
print("a====>", a);

b = ndimage.binary_erosion(a).astype(a.dtype);
print("b====>", b);

## 腐蚀移除对象使结构更小
c = ndimage.binary_erosion(a, structure=np.ones((5,5))).astype(a.dtype);
print("c====>", c);

#膨胀
a = np.zeros((5, 5));
a[2, 2] = 1;
print("a=====>", a);
c =  ndimage.binary_dilation(a).astype(a.dtype);
print("c=====>", c);

#开操作(opening)
a = np.zeros((5,5), dtype=np.int)
a[1:4, 1:4] = 1; a[4, 4] = 1;
print("a=====>", a);

# 开操作可以移除小的对象
c =ndimage.binary_opening(a, structure=np.ones((3,3))).astype(np.int);
print("c=====>", c);

# 开操作也能平滑边角
d = ndimage.binary_opening(a).astype(np.int);
print("d=====>", d);
#闭操作(closing): ndimage.binary_closing



a = np.zeros((50, 50))
a[10:-10, 10:-10] = 1;
print("a======>", a);
a += 0.25*np.random.standard_normal(a.shape);
print("a======>", a);
mask = a>=0.5
print("mask=====>", mask);
opened_mask = ndimage.binary_opening(mask);
print("opened_mask=====>", opened_mask);
closed_mask = ndimage.binary_closing(opened_mask)
print("closed_mask=====>", closed_mask);

a = np.zeros((7,7), dtype=np.int);
a[1:6, 1:6] = 3
a[4,4] = 2; a[2,3] = 1
print("a=====>", a);

c = ndimage.grey_erosion(a, size=(3,3));
print("c=====>", c);


print("==== 图像测量 ====");
x, y = np.indices((300, 300))
sig = np.sin(2*np.pi*x/50.)*np.sin(2*np.pi*y/50.)*(1+x*y/50.**2)**2
mask = sig > 1

#现在我们查找图像中对象的各种信息：
labels, nb = ndimage.label(mask);
print("labels====>", labels);
print("nb====>", nb);


areas = ndimage.sum(mask, labels, range(1, labels.max()+1))
print("areas====>", areas);

maxima = ndimage.maximum(sig, labels, range(1, labels.max()+1))
print("maxima====>", maxima);

ndimage.find_objects(labels==4)
# Out[187]: [(slice(30L, 48L, None), slice(30L, 48L, None))]

sl = ndimage.find_objects(labels==4)
print("sl====>", sl);
import pylab as pl
pl.imshow(sig[sl[0]])
pl.show();
# Out[190]: <matplotlib.image.AxesImage at 0xb2fdcd0>



#地址: https://www.jianshu.com/p/1a3db06e786d





# 裂纹检测
## 简介
毫无疑问，每年都有数以亿记的资金花在各式建筑体的维护和修缮工程中。如果裂纹能尽早被发现，这个花费将被极大的缩减。不同程度的裂纹，修缮开支是不一样的。早发现早修缮无疑是明智之举。同样，如果能尽早发现道路的裂纹，也将大大减少事故的发生。首先我们得拍下混凝土或道路的表面图，检测将基于这些图片展开。检测的正确率取决于图片质量和实际拍摄。
我们的最终目的是，开发一个能自动检测裂纹的系统。这之前，我们需要检测裂纹的位置。

## 方法
裂纹检测方法可以分为以下四步:
1. 图像抓取
2. 图像处理
3. 图像分割
4. 特征提取

## 图像抓取
通常，抓取到的图像像素越高越好。以下是两个可以用来检测的示例.
<img src="https://cirraybucket.oss-cn-shanghai.aliyuncs.com/yijian/openapi/Cracked_01.jpg" width="30%">
<img src="https://cirraybucket.oss-cn-shanghai.aliyuncs.com/yijian/openapi/Cracked_07.jpg" width="30%">

## 图像处理
图像处理过程也分3步进行
1. 灰度缩放和平均 (Gray scaling and averaging)
首先，对图像进行模糊处理，使之在接下来的步骤中更易处理。
<img src="https://cirraybucket.oss-cn-shanghai.aliyuncs.com/yijian/openapi/blur1.jpg" width="30%">
<img src="https://cirraybucket.oss-cn-shanghai.aliyuncs.com/yijian/openapi/blur7.jpg" width="30%">

2. 对数变换 (Logarithmic transformation)
对数变换是指把图像里的像素值替换为对数值。这步用来做图像增强。
<img src="https://cirraybucket.oss-cn-shanghai.aliyuncs.com/yijian/openapi/img_log-1.jpg" width="30%">
<img src="https://cirraybucket.oss-cn-shanghai.aliyuncs.com/yijian/openapi/img_log-7.jpg" width="30%">

3. 图像平滑:双边滤波 (Image smoothing: bilateral filter)
双边滤波和高斯滤波的内容可以参考OpenCV内容
<img src="https://cirraybucket.oss-cn-shanghai.aliyuncs.com/yijian/openapi/bilateral-1.jpg" width="30%">
<img src="https://cirraybucket.oss-cn-shanghai.aliyuncs.com/yijian/openapi/bilateral-7.jpg" width="30%">

## 图像分割
图像分割也分2步进行
1. 边缘检测 (Canny edge detection)
<img src="https://cirraybucket.oss-cn-shanghai.aliyuncs.com/yijian/openapi/edges-1.jpg" width="30%">
<img src="https://cirraybucket.oss-cn-shanghai.aliyuncs.com/yijian/openapi/edges-7.jpg" width="30%">
2. 形态转换 (Morphological transformation)
<img src="https://cirraybucket.oss-cn-shanghai.aliyuncs.com/yijian/openapi/closing-1.jpg" width="30%">
<img src="https://cirraybucket.oss-cn-shanghai.aliyuncs.com/yijian/openapi/closing-7.jpg" width="30%">

## 特征提取
特征提取算法有SIFT,SURF,ORB等好几种，SIFT和SURF收费而ORB免费。ORB = Oriented FAST and Rotated BRIEF. 它计算速度快，匹配精准的特点。用ORB方法后，我们得到图像如下
<img src="https://cirraybucket.oss-cn-shanghai.aliyuncs.com/yijian/openapi/CrackDetected-1.jpg" width="30%">
<img src="https://cirraybucket.oss-cn-shanghai.aliyuncs.com/yijian/openapi/CrackDetected-7.jpg" width="30%">

## 结果讨论
我们尝试了近20张有裂纹+无裂纹图片，裂纹在我们的结果图里很准确的显示。所以我们断言，只要图片清晰，该检测方法能达到80-90%的准确率。
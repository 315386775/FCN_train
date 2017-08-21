function cmap = labelcolormap(N)

if nargin==0
    N=256
end
cmap = zeros(N,3);
for i=1:N
    id = i-1; r=0;g=0;b=0;
    for j=0:7
        r = bitor(r, bitshift(bitget(id,1),7 - j));
        g = bitor(g, bitshift(bitget(id,2),7 - j));
        b = bitor(b, bitshift(bitget(id,3),7 - j));
        id = bitshift(id,-3);
    end
    cmap(i,1)=r; cmap(i,2)=g; cmap(i,3)=b;
end
cmap = cmap / 255;

background 0 0 0 ±³¾° 
aeroplane 128 0 0 ·É»ú 
bicycle 0 128 0 
bird 128 128 0 
boat 0 0 128 
bottle 128 0 128 Æ¿×Ó 
bus 0 128 128 ´ó°Í 
car 128 128 128 
cat 64 0 0 Ã¨ 
chair 192 0 0 
cow 64 128 0 
diningtable 192 128 0 ²Í×À 
dog 64 0 128 
horse 192 0 128 
motorbike 64 128 128 
person 192 128 128 
pottedplant 0 64 0 ÅèÔÔ 
sheep 128 64 0 
sofa 0 192 0 
train 128 192 0 
tvmonitor 0 64 128 ÏÔÊ¾Æ÷
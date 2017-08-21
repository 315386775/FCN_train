dirs=dir('F:/xxx/*.png');
for n=1:numel(dirs)
     strname=strcat('F:/xxx/',dirs(n).name);
     img=imread(strname);
     [x,map]=rgb2ind(img,256);
     newname=strcat('F:/xxx/',dirs(n).name);
     imwrite(x,map,newname,'png');
end
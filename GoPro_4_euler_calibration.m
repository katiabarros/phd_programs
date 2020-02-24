%---------------------------THIS PROGRAM IS NOT WORKING AS IT SHOULD BE!!!!!!!!!!!!!!!!!!-----------------------
%program writen by Kátia Mendes to calculate the attitude of the GoPros 
% it takes the data from the geometric calibration, the GoPros and the moon position 
% to try to extract the attitude of the cameras. Might contain errors. 

clear all
close all
clc

%center pixels through calibration
cx=2106.74;			%this comes from step 2, the geometric calibration
cy=1512.82;

%fov for gopro 5
diagfov=149.2;			% this is from GoPro manual
vfov=94.4;
hfov=122.6;

%calculating patterns of gopro
vaa1=atand((0-cy)/(4000-cx));
vaa1=vaa1+360;
d1=sqrt(cy^2+(4000-cx)^2);
a=(diagfov/2)/d1;


%data from the moon: x, y, azimuth and elevation
test=load('pixels_hero5_1010.txt');
test1=load('moon_hero5_1010.txt');

%reading each column
x0=test(:,1);
y0=test(:,2);
azimuth=test1(:,4);
elevation=test1(:,5);

%calculating vza and vaa of the images
dx=x0-cx;
dy=y0-cy;
d=sqrt(dx.^2+dy.^2);
vza=d*a;
vaa=atand(dy./dx);

for i=1:size(vaa)
  if vaa(i)<=0 
    vaa(i) = vaa(i) + 360;
  end
end

%data from the images: vza, vaa
%data from the moon: elevation, azimuth

%all the way around for calculate the pixels of the calculated
e0=tand (azimuth);
e1=((90-elevation)./a);

dxm=sqrt((e1.^2)./(1+e0.^2));
dym=dxm.*e0;

xm=dxm+cx;
ym=dym+cy;

%distance of the moon to the center of the pixels
b=sqrt(dxm.^2+dym.^2);


%-----------------------start calculating pitch, roll and yaw
for i= -90:1:90
    for j= -90:1:90
        for k= -180:1:180
        
roll=i; % 30.55;  
pitch=j; %35.1; 
yaw=k; %-51.45 ;

%convert to radians
iroll = roll*pi/180.;
ipitch = pitch*pi/180.;
iyaw = yaw*pi/180.;
isza = vza*pi/180.;
isaa = vaa*pi/180.;

%calculate cartesian coordinates from sza and saa
x=sin(isza).*cos(isaa);
y=sin(isza).*sin(isaa);
z=cos(isza);


%rotate cartesian coordinates with three rotation matrizes (pos. math.) for yaw, pitch and roll

xx= x*(cos(ipitch)*cos(iyaw)) + y*(cos(ipitch)*sin(iyaw)) + ...
    z*(-sin(ipitch));

yy= x*(sin(iroll)*sin(ipitch)*cos(iyaw)-cos(iroll)*sin(iyaw)) + ...
    y*(sin(iroll)*sin(ipitch)*sin(iyaw)+cos(iroll)*cos(iyaw)) + ...
    z*(sin(iroll)*cos(ipitch));

zz= x*(cos(iroll)*sin(ipitch)*cos(iyaw)+sin(iroll)*sin(iyaw)) + ...
    y*(cos(iroll)*sin(ipitch)*sin(iyaw)-sin(iroll)*cos(iyaw)) + ...
    z*(cos(iroll)*cos(ipitch));


%return back to spherical coordinates

vza_new=acos(zz./(sqrt(xx.^2+yy.^2+zz.^2)));
vaa_new=atan(yy./xx);

vza_new=vza_new/pi*180.;
vaa_new=vaa_new/pi*180.;

 if (vaa_new<=0) 
    vaa_new=vaa_new+360;
 end
   

%return back to pixels to calculate the values
e3=tand (vaa_new);
e4=((vza_new)./a);

dxmn=sqrt((e4.^2)./(1+e3.^2));
dymn=dxmn.*e3;

xmn=dxmn+cx;
ymn=dymn+cy;

%distance of the new moon to the center of the pixels
%dn=sqrt(dxmn.^2+dymn.^2);

%xm=round(xm);
%xmn=round(xmn);
%ym=round(ym);
%ymn=round(ymn);

%if ((xm.-xmn)<10 && (xm.-xmn)>-10 && (ym.-ymn)<10 && (ym.-ymn)>-10)
%tolerance of distance from points between calculated and from pictures
tol=100;
one = ones(size(xmn));
if ((xm <= xmn+tol*one)&(xm >= xmn-tol*one)&(ym <= ymn+tol*one)&(ym >= ymn-tol*one))
  [i,j,k,mean(xm-xmn),mean(ym-ymn)]
   

    
     figure
    plot(x0,y0,'.','LineWidth',2)
    hold on 
  %  plot(cx,cy,'.')
    plot(xm,ym,'r-','LineWidth',2)
   % hold on
    plot(xmn,ymn,'go')
    xlim ([0 3680])
  %  ylim ([0 2760])
    set (gca,'ydir','reverse')
    legend ('Image','Moon','New')
end

        end
    end
end


  %  figure
  %  plot(xm,ym,'.')
  %  hold on
  %  plot(xmn,ymn,'.')
 

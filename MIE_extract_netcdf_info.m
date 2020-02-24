clear all
close all
clc

%ncfile = 'watercloud_670.mie.cdf' ; % nc file name
%ncfile = 'Y:/LEIPSIC/bin/inputs/Clouds_for_LEIPSIC/new_cloud.cdf';
ncfile ='Z:/home_rad/Katia/MCarats/Teste/evi/wc.10000.mie.cdf';

% To get information about the nc file
%ncinfo(ncfile)

% to display nc file
%ncdisp(ncfile)

% to read a vriable 'var' exisiting in nc file
wl =ncread(ncfile, 'wavelen')
reff = ncread(ncfile,'reff')      
ntheta = ncread(ncfile,'ntheta') ;      %number of scattering angles
theta = ncread(ncfile,'theta') ;
phase = ncread(ncfile,'phase') ;
nmom = ncread(ncfile,'nmom') ;     %'number of Legendre polynomials'
pmom  = ncread(ncfile,'pmom') ;     %'Legendre polynomials'
ext  = ncread(ncfile,'ext') ;       %'extinction coefficient'
ssa  = ncread(ncfile,'ssa') ;      %'single scattering albedo'
refre = ncread(ncfile,'refre') ;    %'refractive index (real)'
refim = ncread(ncfile,'refim') ;    %'refractive index (imaginary)'
rho = ncread(ncfile,'rho') ;        %density of medium
gg=ncread(ncfile,'gg') ;            %asymetry factor

 zero=zeros(90,1);
 theta=theta*pi/180;

teste=[theta(:,1) phase(:,1) phase(:,2) zero phase(:,2) phase(:,1) zero zero zero phase(:,3)];
teste1=flip(teste);

x1=theta(:,1,1)*180/3.14;
x5=theta(:,1,5)*180/3.14;
x10=theta(:,1,10)*180/3.14;
x15=theta(:,1,15)*180/3.14;
x20=theta(:,1,20)*180/3.14;
x25=theta(:,1,25)*180/3.14;

plot(x1,phase(:,1))
hold on
plot(x5,phase(:,5))
plot(x10,phase(:,10))
plot(x15,phase(:,15))
plot(x20,phase(:,20))
plot(x25,phase(:,25))

legend('Reff=1um','Reff=5um','Reff=10um','Reff=15um','Reff=20um','Reff=25um')
xlim ([0 180])

#Code by GVV Sharma
#July  8, 2020
#released under GNU GPL
#Generates data for a triangle problem
#Data is saved in a file called triangle.dat

clear;
close;
clc;

%Generate line points
function x_AB =   line_gen(A,B)
  len =10;
  lam_1 = linspace(0,1,len);
  for i=1:len,
    temp1 = A + lam_1(i)*(B-A);
    x_AB(:,i)= temp1;
end
endfunction
	
%begin function
function m =  dir_vec(A,B)
  m = B-A;
endfunction 

a = 4;
b = 3;
c = sqrt(a**2+b**2);

%Triangle vertices
A = [0;b];
B = [a;0] ;
C = [0;0] ;
%

%Mid point of A,B
M=[a/2;b/2];

% Point D
D=[a;b];

%Generating the lines
x_AB = line_gen(A,B);
x_BC = line_gen(B,C);
x_CA = line_gen(C,A);
x_CM = line_gen(C,M);
x_MD = line_gen(M,D);
x_DB = line_gen(D,B);

x_AB
save ("-ascii", "triangle.dat","x_AB","x_BC","x_CA","x_CM","x_MD","x_DB");




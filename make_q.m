q = 0;
for i = 1:101
    q = q + K*R_area(i)*(T_D200W(2,i)-40)/l;
end
q
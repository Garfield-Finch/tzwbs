for i = 1:1:20
data= B090512020(1000*(i-1)+1:1000*i,:)';
figure(i);
plot(data);
end

data2= B090512020(1000*(5-1)+1:1000*5,:)';
figure(5);
plot(data2);
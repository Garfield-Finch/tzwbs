%get the average data, real
data= BT17111239db(1:5000,:)';
for i = 2:1:200
    data= data+ BT17111239db(5000*(i-1)+1:5000*i,:)';
end
real=data/200;
figure(20000);
plot(real); 
%%%%

%noise of sample k
k=1;
data= BT17111239db(1+5000*(k-1):5000*k,:)';
noise = data-real;
%%%%

%get the averaged noise segment
all_shifted_noise = zeros(1,1330);
for i=1:1:200
    data= BT17111239db(5000*(i-1)+1:5000*i,:)';
    noise = data-real;
    min = 10000;
    index = 0;
    for j=5000:-1:3000
        if noise(j)<min
            min = noise(j);
            index = j;
        end
    end
    shifted_noise = noise(index-1330+1:index);
    all_shifted_noise = all_shifted_noise+shifted_noise;
end
average_shifted_noise = all_shifted_noise/200;
% plot(average_shifted_noise);

for u=51:1:60;
    data= BT17111239db(1+5000*(u-1):5000*u,:)';
    min = 10000;
    index2 = 0;
    for j=5000:-1:3000
        if data(j)<min
            min = data(j);
            index2 = j;
        end
    end
    figure(u);
    plot(data);
    
    j=1331;
    for i=index2:-1:1
        j=mod(j-2,1330)+1;
        data(i)=data(i)-average_shifted_noise(j);
    end
    figure(u+5000); 
    plot(data);
end


conn = database('srtp', 'root', 'yxc'); % 连接数据库
for i = 1:80
    sqlquery = sprintf('select images_location from pictures where id = %d', i);
    results = fetch(conn, sqlquery);    % 读取图片相对存储地址
    results = results.images_location{1};
    results = fullfile('D:\Pycharm2022\srtp', results);
    image = imread(results);            % 打开图片
    img_gaussian = imnoise(image, 'gaussian' , 0, 0.02);    % 添加高斯噪声（均值为0，方差为0.02）
    img_poisson = imnoise(image, 'poisson');    % 添加泊松噪声
    img_salt = imnoise(image, 'salt & pepper', 0.02);   % 添加椒盐噪声（均值为0.02）
    image = medfilt2(img_salt, 3);
    subplot(2, 2, 1);
    imshow(image);
    subplot(2, 2, 2);
    imshow(img_gaussian);
    subplot(2, 2, 3);
    imshow(img_poisson);
    subplot(2, 2, 4);
    imshow(img_salt);
end
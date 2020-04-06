insert into students values
(0,'小明',18,180.00,2,1,0),
(0,'小月月',18,180.00,2,2,1),
(0,'彭于晏',29,185.00,1,1,0),
(0,'刘德华',59,175.00,1,2,1),
(0,'黄蓉',38,160.00,2,1,0),
(0,'凤姐',28,150.00,4,2,1),
(0,'王祖贤',18,172.00,2,1,1),
(0,'周杰伦',36,null,1,1,0),
(0,'程坤',27,181.0,1,2,0),
(0,'刘亦菲',25,166.00,2,2,0),
(0,'金星',33,162.00,3,3,1),
(0,'静香',12,180.00,2,4,0),
(0,'郭靖',12,170.00,1,4,0),
(0,'周杰',34,176.0,2,5,0);

area (id,parent_id,name,short_name,longitude,latitude,level,sort,status)
create table area(
    id int primary key,
    parent_id int,
    name varchar(30),
    short_name varchar(30),
    longitude decimal(9,6),
    latitude decimal(8,6),
    level tinyint,
    sort tinyint,
    status tinyint
);


create table goods(
    id int unsigned primary key auto_increment not null,
    name varchar(150) not null,
    cate_name varchar(40) not null,
    band_name varchar(40) not null,
    price decimal(10,3) not null default 0,
    is_show bit not null default 1,
    is_saleoff bit not null default 0
);



insert into goods values(0, 'r510vc 156英寸笔记本', '笔记本', '华硕', '3399', default, default);
insert into goods values(0, 'y400n 14.0英寸笔记本电脑','笔记本','联想','4999', default, default);
insert into goods values(0, 'g150th 15.6英寸游戏本', '游戏本', '雷神', '8499', default,default);
insert into goods values(0, 'x550cc 15.6英寸笔记本', '笔记本', '华硕', '2799', default, default);
insert into goods values(0, 'x240超极本', '超级本', '联想', '4880', default, default);
insert into goods values(0, 'u330p 13.3英寸超极本', '超级本', '联想', '4299', default, default);
insert into goods values(0, 'svp13226scb触控超极本', '超级本', '索尼','7999' ,default, default);
insert into goods values(0, 'ipad mini 7.9英寸平板电脑', '平板电脑', '苹果', '1998', default, default);
insert Into goods values(0, 'ipad air 9.7英寸平板电脑', '平板电脑', '苹果', '3388', default, default);
insert into goods values(0, 'ipad min1 配备retina 显示屏', '平板电脑', '苹果', '2788', default, default);
insert into goods values(0, 'ideacentre c340 20英寸一体电脑', '台式机', '联想', '3499', default, default);
insert into goods values(0, 'vostro 3800-r1206 台式电脑', '台式机', '戴尔', '2899', default, default);
insert into goods values(0, 'imac me086ch/a 21.5英寸- -体电脑', '台式机', '苹果', '9188', default, default);
insert into goods values(0, 'at7-7414lp台式电脑Linux', '台式机', '宏基', '3699', default, default);
insert into goods values(0, 'z220sff f4f06pa工作站', '服务器/工作站', '惠普', '4288', default, default);
insert into goods values(0, 'poweredge 11服务器', '服务器/工作站', '戴尔', '5388', default, default);
insert into goods values(0, 'mac pro专业级台式电脑', '服务器/工作站', '苹果', '28888', default, default);
insert into goods values(0, 'hmz-t3w头戴显示设备', '笔记本配件', '索尼', '6999', default, default);
insert into goods values(0, '商务双肩背包', '笔记本配件', '索尼', '99', default, default);
insert into goods values(0, 'x3250 m4机架式服务器', '服务器/工作站', 'ibm', '6888', default, default);



 select * from goods
     inner join(
        select cate_name,
        max(price) as max_price,
        min(price) as min_price,
        avg(price) as avg_price,
        count(*) from goods group by cate_name
     ) as goods_new_info on goods.cate_name=goods_new_info.cate_name and goods.price=goods_new_info.max_price;



    create table if not exists goods_cates(
        id int unsigned primary key auto_increment,
        name varchar(40) not null
    );


    insert into goods (name, cate_id, brand_name,price)
    values('LaserJet Pro P1606dn 黑白打印机', 12, 4, '1849');
    


    create view v_goods_info as select g.*, c.name as cate_name, b.name as brand_name from goods as g left join goods_cates as c on g.cate_id=c.id left join goods_brands as b on g.brand_id=b.id;
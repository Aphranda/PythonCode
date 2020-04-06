-- 数据库操作

    -- 链接数据库
    mysql -u root -p
    mysql -u root -p password

    -- 退出数据库
    exit/quit/ctrl + d

    --sql语句结尾都有分号;结尾
    --显示数据库版本
    select version()

    -- 查看所有数据库
    show databases;

    --显示当前数据库时间
    select now()

    --创建数据库
    --create database 数据库名 charset=utf8;
    create database python01;
    create database `python-01`;
    create database python02 charset=utf8;

    --查看创建数据库的语句
    --show create database 数据库名;
    show create database python01;

    --查看当前使用的数据库
    select database();

    --使用数据库
    --use 数据库名;
    use python01;

    --删除数据库
    --drop database 数据库名;
    drop database python01;
    drop database `python-04`

--数据表操作

    --查看当前数据库所有的表
    show tables;

    --创建数据表
    --auto_incremenr 表示自动增长
    --not null 表示不能为空
    --primary key 表示主键
    --default 表示默认值
    --create table 数据表名字 (字段 类型 约束[, 字段 类型 约束]);
    --创建classses表(id name)
    create table xxxxxx(id int, names varchar(30));
    create table yyyyyy(id int primary key not null auto_increment, names varchar(30));
    create table yyyyyy(
        id int primary key not null auto_increment, 
        names varchar(30)
    );

    --查询表属性结构
    desc 数据表名;

    --创建student表(id names hight gender cls_id)
    create table student(
        id int unsigned not null auto_increment primary key,
        names varchar(30) default "",
        age tinyint unsigned default 0,
        hight decimal(5,2),
        gender enum("男", "女","中性","保密") default "保密",
        cls_id int unsigned default 0,
        is_delete bit default 0
    );
    --创建班级表
    create table classes(
        id int unsigned auto_increment primary key not null,
        name varchar(30) not null
    );
    --在表里插入数据
    insert into student values(0, "大D", 18, 188.88, "男" , 0);

    --查询表里面的数据
    select*from student;

    --修改表结构

    --添加字段
    --alter table 表名 add 列名 类型;
    alter table student add birthday datetime;

    --添加外键
    alter tables goods add foreign key (cate_id) references goods_cates(id);

    --修改字段
    --不重命名 alter table 表名 modify 列名 类型及约束;
    alter table student modify birthday date;

    --重命名 alter table 表名 change 原名 新名 类型及约束;
    alter table student change birthday birth date default "1997-01-01";

    --删除字段
    --alter table 表名 drop 列名;
    alter table student drop hight;

    --删除表
    --drop table 表名;
    drop table xxxxxx;

    --查看创造的表
    --show create table 表名;
    show create table student;


--增删改查(curd)
    --增加
        --全列插入
        --insert [into] 表名 values(......)
        --主键字段可以用 0 null default 来占位
        --向classes表中插入一个班级
        insert into classes values (0, "菜鸟班")


        +--------+----------------------------+------+-----+------------+----------------+
        | Field  | Type                       | Null | Key | Default    | Extra          |
        +--------+----------------------------+------+-----+------------+----------------+
        | id     | int(10) unsigned           | NO   | PRI | NULL       | auto_increment |
        | names  | varchar(30)                | YES  |     | NULL       |                |
        | age    | tinyint(3) unsigned        | YES  |     | NULL       |                |
        | gender | enum('男','女','保密')      | YES  |     | 保密       |                |
        | cls_id | int(10) unsigned           | YES  |     | NULL       |                |
        | birth  | date                       | YES  |     | 1997-01-01 |                |
        +--------+----------------------------+------+-----+------------+----------------+
        --向studen表插入一个学生信息
        insert into student values(0, "阿七", 20, "男", "1", "2000-01-01");
        --枚举中的下表从1开始，向后对应
        insert into student values(0, "十三", 20, "2", "1", "2000-01-01");

        --部分插入
        --insert into 表名(列1,.....) values(值,......)
        insert into student (names, gender) values ("十七", "2");

        --多行插入
        insert into student (names, gender) values ("小飞", "1"), ("大保", "1");
        --全部多行
        insert into student values(0, "大飞", 30, "男", "1", "2000-01-01"), (0, "保安", 20, "男", "1", "2000-01-01");
        insert into classes values(0, "python_01期"),(0, "python_02期");


    --删除
        --物理删除
        --delete from 表名 where 条件;
        delete from student where id<8;

        --逻辑删除
        --用一个字段表示 这条信息不可用
        --给student增加一个is_delete字段bit类型
        alter table student add is_delete bit default 0;
        update student set is_delete where id=6;
        select*from student where is_delete=0;
    
    --修改
        --update 表名 set 列1=值1, 列2=值2......where 条件;
        update student set age=20 where id=5;
        update student set age=21,cls_id=1 where id=5;

    --查询
        --查询所有列
        --select*from 表名;
        select*from student;

        --条件查询
        --select*from 表名 where 表名;
        select*from student where gender="男";

        --查询指定列
        --select 列1,列2,..... from 表名;
        select names, gender from student;

        --可以用as为列或者表的指定别名
        --select 字段[as 别名] , 字段[as 别名] from 数据表 where ......;
        select names as 姓名, gender as 性别 from student;

        --字段顺序
        select id as 序号, gender as 性别, names as 姓名 from student;

        --依据表的属性查询
        select s.names, s.gender from student as s;

        --去重查询
        --distinct字段
        select distinct gender from students;


--条件查询
    --比较运算符
        --select ..... from 表名 where ......
        -- > 大于
        --查询大于18岁的信息
        select * from students where age>18;

        -- < 小于
        --查询小于18岁的信息
        select * from students where age<18;
        select id,name,gender from students where age<18;

        -- <= 小于等于
        --查询小于等于18岁的信息
        select * from students where age<=18;

        -- >= 大于等于
        --查询大于等于18岁的信息
        select * from students where age>=18;

        -- =  等于
        --查询等于18岁的信息
        select * from students where age=18;

        -- != 不等于
        --查询不等于18岁的信息
        select * from students where age!=18;


    --逻辑运算符
        -- and
        --18到28之间所有学生信息
        select * from students where age>18 and age<28;

        --18岁以上的女性
        select * from students where age>18 and gender="女";

        --or
        --18岁以上或者身高超过180（包含）以上
        select * from students where age>18 or hight>=180;

        --not
        --不在18以上的女性
        select * from students where not age>18 and gender="女";
        --除18岁以上女性之外的所有
        select * from students where not (age>18 and gender=2);

    
--模糊查询
    --like
        -- % 替换1个或者多个
        -- _ 替换1个

        --查询姓名中以"小"开头的名字
        select name from students where name like "小%";

        --查询姓名中包含“小”
        select name from students where name like "%小%";

        --查询有2个字的名字
        select name from students where name like "__";

        --查询至少有2个字的名字
        select name from students where name like "__%";

        --查询有3个字的名字
        select name from students where name like "___";

    --rlike(正则)
        --查询以周开始的姓名
        select name from students where name rlike "^周";

        --查询以 周开始、伦结尾的姓名
        select name from students where name rlike "^周.*伦$";


--范围查询
    -- in (1, 3, 8)表示在一个非连续的范围内
        --查询 年龄为18 34的姓名
        select name,age from students where age in (12, 18, 34);


    --not in 不在非连续范围内
        --查询 年龄不在为18 34的姓名
        select name,age from students where age not in (12, 18, 34);


    --between ... and 表示在一个连续的范围之内
        --查询 年龄在18到34之间
        select name, age from students where age between 18 and 34;
    
    --not between ... and 表示不在在一个连续的范围之内的其他
        --查询 年龄在18到34之外
        select name, age from students where age not between 18 and 34;
        select name, age from students where not age between 18 and 34;

--空判断
    --判空is null
        --查询信息为空
        select name, hight from students where hight is null;

    --判断非空
        --查询信息非空
        select name, hight from students where hight is not null;



--排序
    --order by字段
        --asc从小到大排序，升序
        --desc从大到小排序，降序

        --查询年龄在18到34的男性，按照年龄从小到大排序
        select * from students where (age between 18 and 34) and gender=1 order by age;
        select * from students where (age between 18 and 34) and gender=1 order by age asc;
        --从大到小
        select * from students where (age between 18 and 34) and gender=1 order by age desc;

        --查询年龄在18到34岁的女性，身高从高到矮排序
        select * from students where (age between 18 and 34) and gender=2 order by hight desc;

    --order by 多个字段 (优先级从前往后降低)
        --查询年龄在18到34岁的女性，身高从高到矮排序
        --身高相同，按年龄，年龄相同按id
        select * from students where (age between 18 and 34) and gender=2 order by hight desc,age asc,id desc;

        --按年龄从小到大，身高从高到矮排序
        select * from students order by age asc, hight desc;


--聚合函数
    --总数
    --count
        --查询男性有多少人，女性有多少人
        select count(*) from students where gender=1;
        select count(*) as "男性人数" from students where gender=1;
        select count(*) as "女性人数" from students where gender=2;

    --最大值
    --max
        --查询最大年龄
        select max(age) from students;

        --查询女性最高身高
        select max(hight) from students where gender=2;

    --最小值
    --min

    --求和
    --sum
        --计算所有人的年龄总和
        select sum(age) from students;

    --平均值
    --avg
        --计算平均年龄
        select avg(age) from students;

    --四舍五入 round(123.23, 1)保留一位小数
        --计算平均年龄，保留两位小数
        select round(avg(age), 2) from students;

        --计算男性平均身高，保留两位小数
        select round(avg(hight), 2) from students where gender=1;



--分组
    --group by
        --按照性别分组查询所有性别
        select gender from students group by gender;

        --计算每个分组中的人数
        select gender,count(*) from students group by gender;
        select gender,max(age) from students group by gender;

        --计算男性人数
        select gender,count(*) from students where gender=1 group by gender;


    --group_concat(......)
        --查询组内属性集合
        --查询同性别人数
        select gender,group_concat(name," ",age," ",id) from students group by gender;

        --查询男性具体信息
        select gender,group_concat(name," ",age," ",id) from students where gender=1 group by gender;

    --having 分组后判断-达到要求的分组  从查询结果中做后续判断
        --查询年龄超过30岁的性别，以及姓名 having avg(age)>30
        select gender, group_concat(name), avg(age) from students group by gender having avg(age)>30;

        --查询分组后组员大于2
        select gender, group_concat(name) from students group by gender having count(*)>2;


--分页
    --limit start , count
        --从那个数开始，查询个数

        --限制查询出来的个数
        select * from students where gender=1 limit 5;

        --查询前5个
        select * from students limit 0,5;

        --查询6-10
        select * from students limit 5,5;

        --每页显示2个，第1个页面
        select * from students limit 0,2;

        --每页显示2个，第2个页面
        select * from students limit 2,2;

        --每页显示2个，第3个页面
        select * from students limit 4,2;

        --每页显示2个，第4个页面
        select * from students limit 6,2;

        select * from students limit (N-1)*n,n; 第N页 每页显示n个

        select * from students where gender=2 order by hight desc limit 0, 2;


--连接查询
    -- inner join ... on
        --查询能够对应班级的学生以及班级信息

        --内连接查询 取A与B的交际 on 
        --select ... from 表A inner join 表B;
        select * from students inner join classes;

        --查询所有能够对应班级的学生及班级信息
        select * from students inner join classes on students.cls_id = classes.id;

        --按照要求显示班级，姓名
        select students.name, classes.name from students inner join classes on students.cls_id = classes.id;
        --简写
        select s.name, c.name from students as s inner join classes as c on s.cls_id = c.id;

        --在以上查询中，将班级信息放在第一列
        select c.name, s.* from students as s inner join classes as c on s.cls_id = c.id;

        --查询所有能够对应班级的学生及班级信息, 并按班级排序
        select c.name, s.* from students as s inner join classes as c on s.cls_id = c.id order by c.name;

        --查询所有能够对应班级的学生及班级信息, 并按班级排序, 同一个班级安装序号排列
        select c.name, s.* from students as s inner join classes as c on s.cls_id = c.id order by c.name, s.id;

    --外连接
        --左连接 left join 左边为基准，能找到就显示，找不到就显示null
        --查询每位同学对应的班级信息
        select * from students as s left join classes as c on s.cls_id=c.id;

        --右链接 right join
        --查询没有对应班级的学生
        select * from students as s left join classes as c on s.cls_id=c.id having c.id is null;
        select * from students as s left join classes as c on s.cls_id=c.id where c.id is null;
        


--自关联
    --查询所有省份

    --查询山东省有哪些城市
    select * from area as province inner join area as city on city.parent_id = province.id having province.name = "山东省";

    --父子联合查询
    select province.name, city.name from area as province inner join area as city on city.parent_id = province.id having province.name = "父级目录";

--子查询
    --标量子查询
    --查询高出平均升高的信息

    --查询最高的男生信息
    select * from students where hight = 188;
    select * from students where hight = (select max(hight) from students);

    --查询河北省下属市
    select * from area where parent_id=(select id from area where name="河北省");


--实践

    --创建商品总表goods
    create table goods(
        id int unsigned primary key auto_increment not null,
        name varchar(150) not null,
        cate_name varchar(40) not null,
        brand_name varchar(40) not null,
        price decimal(10,3) not null default 0,
        is_show bit not null default 1,
        is_saleoff bit not null default 0
    );

    --将查询结果作为一张表，进行联合查询。
    select * from goods
    inner join(
        select cate_name,
        max(price) as max_price,
        min(price) as min_price,
        avg(price) as avg_price,
        count(*) from goods group by cate_name
    ) as goods_new_info on goods.cate_name=goods_new_info.cate_name and goods.price=goods_new_info.max_price;


    --将cate_name分表，进行数据插入
    --创建goods_cates分表
    create table if not exists goods_cates(
        id int unsigned primary key auto_increment,
        name varchar(40) not null
    );

    --把goods表里的cate_name到数据，插入到goods_cate的name中
    insert into goods_cates(name) select cate_name from goods group by cate_name;

    --同步数据，使用关联查询用g.cate_name=c.name进行定位，然后将goods_cate中的id传入goods中的cate_name里
    update goods as g inner join goods_cates as c on g.cate_name=c.name set g.cate_name=c.id;
    update goods as g inner join goods_brands as b on g.brand_name = b.name set g.brand_name=b.id;


    --将父子连接的字段和类型进行修改
    alter table goods change cate_name cate_id int unsigned not null;
    alter table goods change brand_name brand_id int unsigned not null;
    --多个一起修改
    alter table goods 
    change cate_name cate_id int unsigned not null,
    change brand_name brand_id int unsigned not null;

    --将cate_id变成外键
    alter table goods add foreign key (cate_id) references goods_cates(id);
    alter table goods add foreign key (brand_id) references goods_brands(id);

    --创建产品品牌表 goods_brands
    create table if not exists goods_brands(
        id int unsigned primary key auto_increment,
        name varchar(40) not null
    ) select brand_name as name from goods group by brand_name;

    --取消外键约束
    --获取外键名称
    --show create table goods
    --删除外键
    alter tabel goods drop foreign key 外键名称

    --创建订单表
    create table orders(
        id int unsigned primary key auto_increment,
        order_data_time datetime,
        customer_id int unsigned
    );

    --创建客户表
    create table customers(
        id int unsigned primary key auto_increment,
        name varchar(30) not null,
        address varchar(30) not null,
        tel int unsigned not null,
        password int unsigned not null,
    );

    --创建订单详情表
    create table order_detail(
        id int unsigned primary key auto_increment,
        customer_id int unsigned not null,
        goods_id int unsigned not null,
        quailty int unsigned
    );

    --添加索引
    create index text_index on test(title(10));

    --查询索引
    select * from text_index where title = "ha-90000";

    --创建账户并授予所有权限
    --创建新用户
    create user 'userName'@'%' identified ...，创建新用户，此时使用create user
    create user 'dl'@'%' identified '123456';
    
    --提供权限
    grant all privileges on jing_dong.* to 'dl'@'localhost' with grant option;
    

    --查看用户有哪些权限
    show grants for 'dl'@'localhost';


    














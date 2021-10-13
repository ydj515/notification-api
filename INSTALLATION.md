## installation

### 필요 모듈
```bash
pip install fastapi
pip install unicorn
pip install pymysql
pip install sqlalchemy
pip install alembic
```

### mysql install
- docker install
- travis 사용을 위해 user를 travis로 설정
```
docker pull mysql
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root --name mysql mysql
docker ps -a
winpty docker run -it ubuntu bash
mysql -u root -p
CREATE USER 'travis'@'%' IDENTIFIED BY 'ehdwls515';
GRANT ALL PRIVILEGES ON *.* TO 'travis'@'%';
```

- create table
```sql
-- auto-generated definition
create table users
(
    id              int auto_increment primary key,
    status          enum ('active', 'deleted', 'blocked') default 'active'          not null,
    email           varchar(255)                                                    null,
    pw              varchar(2000)                                                   null,
    name            varchar(255)                                                    null,
    phone_number    varchar(20)                                                     null,
    profile_img     varchar(1000)                                                   null,
    sns_type        enum ('FB', 'G', 'K', 'Email')                                  null,
    marketing_agree tinyint(1)                            default 0                 null,
    updated_at      datetime                              default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    created_at      datetime                              default CURRENT_TIMESTAMP not null
);
```
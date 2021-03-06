## installation

### 필요 모듈
```bash
pip install fastapi
pip install unicorn
pip install pymysql
pip install sqlalchemy
pip install alembic
pip install bcrypt
pip install jwt
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

```sql
create table api_keys
(
    id             int auto_increment
        primary key,
    access_key     varchar(64)                                                     not null,
    secret_key     varchar(64)                                                     not null,
    user_memo      varchar(50)                                                     null,
    status         enum ('active', 'stopped', 'deleted') default 'active'          not null,
    is_whitelisted tinyint(1)                            default 0                 null,
    user_id        int                                                             not null,
    updated_at     datetime                              default CURRENT_TIMESTAMP null,
    created_at     datetime                              default CURRENT_TIMESTAMP null
);

create index api_keys_access_key_index
    on api_keys (access_key);
```

```sql
create table api_whitelists
(
    id         int auto_increment
        primary key,
    ip_addr    varchar(64)                        not null,
    api_key_id int                                not null,
    updated_at datetime default CURRENT_TIMESTAMP not null,
    created_at datetime default CURRENT_TIMESTAMP not null,
    constraint api_whitelists_api_keys_id_fk
        foreign key (api_key_id) references api_keys (id)
            on delete cascade
);
```
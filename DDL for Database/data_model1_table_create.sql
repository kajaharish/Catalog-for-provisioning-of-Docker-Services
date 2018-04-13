CREATE TABLE minor_db.user (
    username varchar(35) NOT NULL,
    fname varchar(35) NOT NULL,
    lname varchar(35) NOT NULL,
    password varchar(35) NOT NULL,
    address varchar(255) NOT NULL,
    question varchar(100) NOT NULL,
    answer varchar(35) NOT NULL,
    email varchar(255) NOT NULL,
    PRIMARY KEY (username)
);



CREATE TABLE minor_db.container (
    container_name varchar(35) NOT NULL,
    username varchar(35) NOT NULL,
    container_id varchar(70) NOT NULL UNIQUE,
    container_ip varchar(15) NOT NULL,
    start_time varchar(30) NOT NULL,
    end_time varchar(30) NOT NULL,
    web_server boolean NOT NULL,
    db_server boolean NOT NULL,
    php boolean NOT NULL,
    python boolean NOT NULL,
    total_uptime varchar(30) NOT NULL,
    PRIMARY KEY (container_name),
    FOREIGN KEY (username) REFERENCES user(username)
);


CREATE INDEX ON minor_db.container
    (username);


CREATE TABLE minor_db.nfs_server (
    container_id varchar(20) NOT NULL,
    used_space varchar(15) NOT NULL,
    total_space varchar(15) NOT NULL,
    mount_point varchar(4096) NOT NULL,
    lv_name varchar(255) NOT NULL,
    PRIMARY KEY (container_id),
    FOREIGN KEY (container_id) REFERENCES container(container_id)
);


CREATE TABLE minor_db.payment (
    payment_id varchar(15) NOT NULL,
    username varchar(35) NOT NULL,
    container_id varchar(20) NOT NULL,
    total_uptime varchar(10) NOT NULL,
    confirmation boolean NOT NULL,
    payment_date date NOT NULL,
    payment_time time NOT NULL,
    amount int NOT NULL,
    PRIMARY KEY (payment_id),
    FOREIGN KEY (container_id) REFERENCES container(container_id)
);


CREATE INDEX ON minor_db.payment
    (username);
CREATE INDEX ON minor_db.payment
    (container_id);


CREATE TABLE minor_db.database (
    db_name varchar(128) NOT NULL,
    username varchar(35) NOT NULL,
    db_password varchar(35) NOT NULL,
    PRIMARY KEY (db_name),
    FOREIGN KEY (username) REFERENCES user(username)
);

CREATE INDEX ON minor_db.database
    (username);


CREATE TABLE minor_db.session (
    session_id varchar(35) NOT NULL,
    username varchar(35) NOT NULL,
    PRIMARY KEY (session_id),
    FOREIGN KEY (username) REFERENCES user(username)
);

CREATE INDEX ON minor_db.session
    (username);

CREATE TABLE IF NOT EXISTS scans (
    scan_id int NOT NULL AUTO_INCREMENT,
    start_time timestamp,
    runtime decimal,
    command varchar(255),
    uphosts int,
    downhosts int,
    PRIMARY KEY (scan_id)
);

CREATE TABLE IF NOT EXISTS hosts (
    host_id int NOT NULL AUTO_INCREMENT,
    scan_id int NOT NULL,
    ipv4_address varchar(255),
    hostname varchar(255),
    status varchar(255),
    reason varchar(255),
    PRIMARY KEY (host_id),
    FOREIGN KEY (scan_id) REFERENCES scans(scan_id)
);
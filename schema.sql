CREATE TABLE IF NOT EXISTS scans (
    scan_id int NOT NULL AUTO_INCREMENT,
    start_time timestamp,
    runtime decimal,
    command varchar(255),
    PRIMARY KEY (scan_id)
);
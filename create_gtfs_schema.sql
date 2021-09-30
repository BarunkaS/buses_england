-- in testing, relations not defined, datatype to be changed later
CREATE TABLE IF NOT EXISTS L1_agency (
	agency_id VARCHAR NOT NULL,
	agency_name VARCHAR NOT NULL,
	agency_url VARCHAR,
	agency_timezone VARCHAR,
	agency_lang VARCHAR,
	agency_phone VARCHAR,
	agency_noc VARCHAR
);

CREATE TABLE IF NOT EXISTS L1_calendar_dates (
	service_id DECIMAL NOT NULL,
	date DECIMAL NOT NULL,
	exception_type DECIMAL
);

CREATE TABLE IF NOT EXISTS L1_calendar (
	service_id DECIMAL NOT NULL,
	monday BOOLEAN NOT NULL,
	tuesday BOOLEAN NOT NULL,
	wednesday BOOLEAN NOT NULL,
	thursday BOOLEAN NOT NULL,
	friday BOOLEAN NOT NULL,
	saturday BOOLEAN NOT NULL,
	sunday BOOLEAN NOT NULL,
	start_date DECIMAL NOT NULL,
	end_date DECIMAL NOT NULL
);

CREATE TABLE IF NOT EXISTS L1_feed_info (
	feed_publisher_name VARCHAR NOT NULL,
	feed_publisher_url VARCHAR NOT NULL,
	feed_lang VARCHAR,
	feed_version BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS L1_routes (
	route_id VARCHAR NOT NULL,
	agency_id VARCHAR NOT NULL,
	route_short_name VARCHAR,
	route_long_name VARCHAR,
	route_type DECIMAL
);

CREATE TABLE IF NOT EXISTS L1_shapes (
	shape_id VARCHAR NOT NULL,
	shape_pt_lat DECIMAL,
	shape_pt_lon DECIMAL,
	shape_pt_sequence INT,
	shape_dist_traveled VARCHAR
);

CREATE TABLE IF NOT EXISTS L1_stop_times (
	trip_id VARCHAR NOT NULL,
	arrival_time VARCHAR ,
	departure_time VARCHAR,
	stop_id VARCHAR,
	stop_sequence INT,
	stop_headsign VARCHAR,
	pickup_type INT,
	drop_off_type INT,
	shape_dist_traveled VARCHAR,
	timepoint INT
);

CREATE TABLE IF NOT EXISTS L1_stops (
	stop_id VARCHAR NOT NULL,
	stop_code VARCHAR,
	stop_name VARCHAR NOT NULL,
	stop_lat DECIMAL NOT NULL,
	stop_lon DECIMAL NOT NULL,
	wheelchair_boarding BOOLEAN,
	location_type VARCHAR,
	parent_station VARCHAR,
	platform_code VARCHAR
);

CREATE TABLE IF NOT EXISTS L1_trips (
	route_id VARCHAR NOT NULL,
	service_id DECIMAL NOT NULL,
	trip_id VARCHAR NOT NULL,
	trip_headsign VARCHAR,
	block_id VARCHAR,
	shape_id VARCHAR,
	wheelchair_accessible BOOLEAN
);


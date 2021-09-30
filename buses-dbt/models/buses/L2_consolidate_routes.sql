SELECT 
     a.agency_name,
     r.route_short_name,
     t.route_id,
     t.service_id, --connects to calendars
    st.arrival_time,
    st.departure_time,
    st.stop_sequence,
    round(st.shape_dist_traveled::DECIMAL,2) as dist_travelled,
    st.timepoint,
    s.stop_name,
    s.stop_lat,
    s.stop_lon
FROM l1_agency a
left join l1_routes r on r.agency_id = a.agency_id
inner join subset_locations sl on sl.line_ref = r.route_short_name
left join l1_trips t on t.route_id = r.route_id
left join l1_stop_times st on st.trip_id = t.trip_id
left join l1_stops s on st.stop_id = s.stop_id
where a.agency_id = 'OP794'
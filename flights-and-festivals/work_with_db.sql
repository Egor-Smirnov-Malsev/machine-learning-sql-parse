SELECT
    week_number,
    ticket_amount,
    festival_week,
    festival_name
FROM (
    SELECT
        EXTRACT (WEEK FROM arrival_time) AS week_number,
        COUNT(ticket_no) AS ticket_amount
    FROM 
        flights
    INNER JOIN ticket_flights ON ticket_flights.flight_id = flights.flight_id
    WHERE
        arrival_time between '23-07-2018' and '01-10-2018' AND arrival_airport IN (
            SELECT
                airport_code
            FROM
                airports
            WHERE
                city = 'Москва'
        )
    GROUP BY
        week_number
) AS sq
LEFT JOIN (
    SELECT
        festival_name,
        EXTRACT (WEEK FROM festival_date) AS festival_week
    FROM festivals
    WHERE
        festival_date > '23-07-2018' AND festival_date < '30-09-2018' AND festival_city = 'Москва'
    ) AS sq1 ON festival_week = week_number

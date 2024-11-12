#Blacklist para ver si se da el acceso o no 
CREATE TABLE Blacklist (
    username VARCHAR(25) PRIMARY KEY, reason TEXT
)

CREATE FUNCTION log_event(p_username VARCHAR,p_event TEXT )
    RETURNS void as $$
BEGIN
    RAISE notice "User: ,Event: ",p_username, p_event;
END;
$$ LANGUAGE plpgsql;
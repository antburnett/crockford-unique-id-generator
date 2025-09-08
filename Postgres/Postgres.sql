CREATE OR REPLACE FUNCTION generate_crockford_id(size INT DEFAULT 12) 
RETURNS TEXT AS $$
DECLARE
    -- Crockford Base32: excludes I, L, O, U for readability
    alphabet TEXT := '123456789ABCDEFGHJKMNPQRSTVWXYZ';
    result TEXT := '';
    i INT;
BEGIN
    FOR i IN 1..size LOOP
        result := result || substr(alphabet, floor(random() * 32 + 1)::INT, 1);
    END LOOP;
    RETURN result;
END;
$$ LANGUAGE plpgsql;

-- Add to your road segments table
ALTER TABLE road_segments 
ADD COLUMN id TEXT DEFAULT generate_crockford_id() UNIQUE;

-- Or for new tables
CREATE TABLE road_segments (
    id TEXT DEFAULT generate_crockford_id() PRIMARY KEY,
    -- your other columns
);
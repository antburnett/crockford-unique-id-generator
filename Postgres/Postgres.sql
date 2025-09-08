CREATE OR REPLACE FUNCTION fn_generate_crockford_id(size INT DEFAULT 12) 
RETURNS TEXT AS $$
DECLARE
    -- Crockford Base32: excludes I, L, O, U, 0 for readability
    -- 4 chars = 31^4 = 923,521 combinations
    -- 12 chars = 31^12 = 8.14 x 10^17 combinations  
    -- 32 chars = 31^32 = 4.61 x 10^47 combinations
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
ADD COLUMN id TEXT DEFAULT fn_generate_crockford_id() UNIQUE;

-- Or for new tables
CREATE TABLE road_segments (
    id TEXT DEFAULT fn_generate_crockford_id() PRIMARY KEY,
    -- your other columns
);
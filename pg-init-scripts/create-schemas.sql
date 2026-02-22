DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_namespace WHERE nspname = 'social_backend') THEN
        CREATE SCHEMA social_backend;
    END IF;

--     IF NOT EXISTS (SELECT 1 FROM pg_namespace WHERE nspname = 'payments_backend') THEN
--         CREATE SCHEMA payments_backend;
--     END IF;
END $$;

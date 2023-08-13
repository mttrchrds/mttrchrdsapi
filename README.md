# mttrchrdsapi
API for mttrchrds.com

- When creating from fresh DB, add an env variable to Render calle "CREATE_SUPERUSER" with value of "True". As free tier Render Web Service blocks access to shell. Remove this afterwards so it doesn't do it on each deploy.
- Likewise, DATABASE_URL env variable is populated with "Internal Database URL" field in PostgreSQL DB settings
- Connecting to Render DB in PgAdmin. Copy "External Database URL" in Render settings. It will be formatted postgres://<username>:<render_id>@<host_name>/<database_name>. Use path parts for connection details (password is stored in Postgres settings in Render)


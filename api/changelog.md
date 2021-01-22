# 1.3.2

- Improve the time complexity of `edupage` function.
- Rewrite core `edupage` parser, to be more readable.
- Remade the whole test suite, to use threading and handle more edge cases.
- Merge `./config.toml` and `./pytest.ini` into `./pyproject.toml`.
- Changed the value of `STATISTICS_DEFAULT_DATE_SPAN` in `./pyproject.toml` from 7, to 31.

# 1.3.1

- Extracted core function of `./api/vlo/_tta.py` to `./api/vlo/edupage.py` for further usage/optimalizations.

# 1.3.0

- Added the `/api/nxt` endpoint for getting the next lesson for selected class.
- Fixed `/stats` frontend issue and limited the number of requests showing per page.
- Implemented timed lru cache, because previous one wasnt working properly.
- Lenghted the timeouts on VLO api endpoints

# 1.2

- Added the `/api/tim` endpoint.
- Added the `/api/dbu` endpoint for fetching latest data from the edupage database.
- Added the `"subject_short"` field to the `lesson` object.
- Made the event detector in the `/api/tta` endpoint more forgiving and accurate.
- Added `/stats` endpoint for monitoring usage without.

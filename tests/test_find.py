from unittest.mock import patch

import pytest

from themoviedb import routes, schemas


@pytest.mark.asyncio
async def test_find_by_imdb(get_data, assert_data):
    data = get_data("find/find")
    imdb_id = "test"

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        results = await routes.Find().by_imdb(imdb_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{imdb_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "external_source": "imdb_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)


@pytest.mark.asyncio
async def test_find_by_tvdb(get_data, assert_data):
    data = get_data("find/find")
    tvdb_id = "test"

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        results = await routes.Find().by_tvdb(tvdb_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{tvdb_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "external_source": "tvdb_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)


@pytest.mark.asyncio
async def test_find_by_freebase_mid(get_data, assert_data):
    data = get_data("find/find")
    freebase_mid = "test"

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        results = await routes.Find().by_freebase_mid(freebase_mid)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{freebase_mid}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "external_source": "freebase_mid",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)


@pytest.mark.asyncio
async def test_find_by_freebase(get_data, assert_data):
    data = get_data("find/find")
    freebase_id = "test"

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        results = await routes.Find().by_freebase(freebase_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{freebase_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "external_source": "freebase_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)


@pytest.mark.asyncio
async def test_find_by_tvrage(get_data, assert_data):
    data = get_data("find/find")
    tvrage_id = "test"

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        results = await routes.Find().by_tvrage(tvrage_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{tvrage_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "external_source": "tvrage_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)


@pytest.mark.asyncio
async def test_find_by_facebook(get_data, assert_data):
    data = get_data("find/find")
    facebook_id = "test"

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        results = await routes.Find().by_facebook(facebook_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{facebook_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "external_source": "facebook_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)


@pytest.mark.asyncio
async def test_find_by_instagram(get_data, assert_data):
    data = get_data("find/find")
    instagram_id = "test"

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        results = await routes.Find().by_instagram(instagram_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{instagram_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "external_source": "instagram_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)


@pytest.mark.asyncio
async def test_find_by_twitter(get_data, assert_data):
    data = get_data("find/find")
    twitter_id = "test"

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        results = await routes.Find().by_twitter(twitter_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{twitter_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "external_source": "twitter_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)

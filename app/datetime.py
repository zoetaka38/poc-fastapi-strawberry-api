from datetime import datetime

from dateutil import tz  # type: ignore


def _now(timezone: str = "") -> datetime:
    """現在時刻を取得する
    pbx api の内部ではすべてUTCを原則とする
    ユーザ入出力を伴う場合のみユーザのTimeZone Awareで扱うが、
    pbx api ではユーザ入出力を直接的に扱うことはないため、基本的には常に utcnow を使う
    :param timezone: IANA Timezone ("Asia/Tokyo" など)
    """
    if not timezone:
        return datetime.now(tz=tz.tzutc())
    else:
        return datetime.now(tz=tz.gettz(timezone))


def utcnow() -> datetime:
    """UTCで現在時刻を取得する"""
    return datetime.now(tz=tz.tzutc())


def now_iso8601(timezone: str = "") -> str:
    """ISO 8601形式で現在時刻を取得する
    :param timezone: IANA Timezone ("Asia/Tokyo" など)
    """
    return _now(timezone).isoformat()


def utcnow_iso8601() -> str:
    """ISO 8601形式でUTCで現在時刻を取得する"""
    return utcnow().isoformat()

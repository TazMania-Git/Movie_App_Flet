# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = Welcomefromdict(json.loads(json_string))

from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, TypeVar, Callable, Type, cast
from enum import Enum
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Dates:
    maximum: datetime
    minimum: datetime

    @staticmethod
    def from_dict(obj: Any) -> 'Dates':
        assert isinstance(obj, dict)
        maximum = from_datetime(obj.get("maximum"))
        minimum = from_datetime(obj.get("minimum"))
        return Dates(maximum, minimum)

    def to_dict(self) -> dict:
        result: dict = {}
        result["maximum"] = self.maximum.isoformat()
        result["minimum"] = self.minimum.isoformat()
        return result


class OriginalLanguage(Enum):
    en = "en"


@dataclass
class Result:
    adult: bool
    backdroppath: str
    genreids: List[int]
    id: int
    originallanguage: OriginalLanguage
    originaltitle: str
    overview: str
    popularity: float
    posterpath: str
    releasedate: datetime
    title: str
    video: bool
    voteaverage: float
    votecount: int

    @staticmethod
    def from_dict(obj: Any) -> 'Result':
        assert isinstance(obj, dict)
        adult = from_bool(obj.get("adult"))
        backdroppath = from_str(obj.get("backdrop_path"))
        genreids = from_list(from_int, obj.get("genre_ids"))
        id = from_int(obj.get("id"))
        originallanguage = OriginalLanguage(obj.get("original_language"))
        originaltitle = from_str(obj.get("original_title"))
        overview = from_str(obj.get("overview"))
        popularity = from_float(obj.get("popularity"))
        posterpath = from_str(obj.get("poster_path"))
        releasedate = from_datetime(obj.get("release_date"))
        title = from_str(obj.get("title"))
        video = from_bool(obj.get("video"))
        voteaverage = from_float(obj.get("vote_average"))
        votecount = from_int(obj.get("vote_count"))
        return Result(adult, backdroppath, genreids, id, originallanguage, originaltitle, overview, popularity, posterpath, releasedate, title, video, voteaverage, votecount)

    def to_dict(self) -> dict:
        result: dict = {}
        result["adult"] = from_bool(self.adult)
        result["backdrop_path"] = from_str(self.backdroppath)
        result["genre_ids"] = from_list(from_int, self.genreids)
        result["id"] = from_int(self.id)
        result["original_language"] = to_enum(OriginalLanguage, self.originallanguage)
        result["original_title"] = from_str(self.originaltitle)
        result["overview"] = from_str(self.overview)
        result["popularity"] = to_float(self.popularity)
        result["poster_path"] = from_str(self.posterpath)
        result["release_date"] = self.releasedate.isoformat()
        result["title"] = from_str(self.title)
        result["video"] = from_bool(self.video)
        result["vote_average"] = to_float(self.voteaverage)
        result["vote_count"] = from_int(self.votecount)
        return result


@dataclass
class Welcome:
    dates: Dates
    page: int
    results: List[Result]
    totalpages: int
    totalresults: int

    @staticmethod
    def from_dict(obj: Any) -> 'Welcome':
        assert isinstance(obj, dict)
        dates = Dates.from_dict(obj.get("dates"))
        page = from_int(obj.get("page"))
        results = from_list(Result.from_dict, obj.get("results"))
        totalpages = from_int(obj.get("total_pages"))
        totalresults = from_int(obj.get("total_results"))
        return Welcome(dates, page, results, totalpages, totalresults)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dates"] = to_class(Dates, self.dates)
        result["page"] = from_int(self.page)
        result["results"] = from_list(lambda x: to_class(Result, x), self.results)
        result["total_pages"] = from_int(self.totalpages)
        result["total_results"] = from_int(self.totalresults)
        return result


def Welcomefromdict(s: Any) -> Welcome:
    return Welcome.from_dict(s)


def Welcometodict(x: Welcome) -> Any:
    return to_class(Welcome, x)

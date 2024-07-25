import discogs_client
from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class DiscogsSettings(BaseSettings):
    user_token: str = Field(...)
    consumer: str = Field(...)
    consumer_secret: str = Field(...)
    model_config = SettingsConfigDict(case_sensitive=False, env_file=".env", env_prefix="DISCOGS_", extra="ignore")


settings = DiscogsSettings()

DISCOGS_REQUEST_TOKEN_URL = "https://api.discogs.com/oauth/request_token"
DISCOGS_AUTHORIZE_URL = "https://www.discogs.com/oauth/authorize"
DISCOGS_ACCESS_TOKEN_URL = "https://api.discogs.com/oauth/access_token"

# TODO setup oauth
# d = discogs_client.Client("deepcuts/1.0", consumer_key=settings.consumer, consumer_secret=settings.consumer_secret)
# print(d.get_authorize_url())


def search_for_release(d: discogs_client.Client, query: str):
    results = d.search(query, type="release,master")
    return results.page(1).keys()


if __name__ == "__main__":
    print("Hi")
    d = discogs_client.Client("my_user_agent/1.0", user_token=settings.user_token)
    results = d.search("DAMN.", artist="Kendrick", type="release,master")
    print(results.page(1)[0])
    # release = d.release(1)

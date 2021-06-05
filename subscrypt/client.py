from urllib.parse import urljoin

import requests


class Subscrypt:
    def __init__(
            self,
            base_url: str = 'http://206.189.154.160:3000/'
    ):
        self.base_url = base_url

    def _get(self, path, **params):
        return requests.get(
            url=urljoin(self.base_url, path),
            params=params,
        ).json()

    def check_subscription(self, user_address: str, provider_address: str, plan_index: int):
        return self._get(
            '/subsCrypt/checkSubscription/',
            user=user_address,
            providerAddress=provider_address,
            planIndex=plan_index,
        )
        
    def check_subscription_with_username(self, username: str, provider_address: str, plan_index: int):
        return self._get(
            f'/subsCrypt/checkSubscription/{username}/',
            providerAddress=provider_address,
            planIndex=plan_index,
        )
        
    def get_username(self, sender: str):
        return self._get(
            f'/subsCrypt/getUsername/{sender}/',
        )
        
    def retrieve_whole_data_with_username(self, username: str, password: str):
        return self._get(
            '/subsCrypt/retrieveDataWithUsername/',
            username=username,
            phrase=password,
        )
        
    def retrieve_data_with_username(self, user_address: str, provider_address: str, password: str):
        return self._get(
            f'/subsCrypt/retrieveDataWithUsername/{provider_address}/',
            username=user_address,
            phrase=password,
        )
        
    def retrieve_data_with_wallet(self, sender: str, provider_address: str):
        # TODO (there is no api doc in swagger)
        raise NotImplemented

    def retrieve_whole_data_with_wallet(self, sender: str):
        # TODO (there is no api doc in swagger)
        raise NotImplemented

    def is_username_available(self, username: str):
        return self._get(
            f'/subsCrypt/isUsernameAvailable/{username}',
        )
        
    def check_auth(self, user_address: str, provider_address: str, password: str):
        return self._get(
            '/subsCrypt/checkAuth/',
            userAddress=user_address,
            providerAddress=provider_address,
            phrase=password,
        )
        
    def check_auth_with_username(self, username: str, provider_address: str, password: str):
        return self._get(
            f'/subsCrypt/checkAuth/{username}/',
            providerAddress=provider_address,
            phrase=password,
        )
        
    def user_check_auth(self, user_address: str, password: str):
        return self._get(
            '/subsCrypt/userCheckAuth/',
            userAddress=user_address,
            phrase=password,
        )
        
    def user_check_auth_with_username(self, username: str, password: str):
        return self._get(
            f'/subsCrypt/userCheckAuth/{username}/',
            phrase=password,
        )
        
    def get_plan_data(self, provider_address: str, plan_index: int):
        return self._get(
            f'/subsCrypt/getPlanData/{provider_address}/{plan_index}/',
        )
        
    def provider_check_auth(self, provider_address: str, password: str):
        return self._get(
            '/subsCrypt/providerCheckAuth/',
            providerAddress=provider_address,
            phrase=password,
        )
        
    def provider_check_auth_with_username(self, provider_username: str, password: str):
        return self._get(
            f'/subsCrypt/providerCheckAuth/{provider_username}/',
            phrase=password,
        )
        
    def get_plan_characteristics(self, provider_address: str, plan_index: int):
        return self._get(
            f'/subsCrypt/getPlanCharacteristics/{provider_address}/{plan_index}/',
        )
        
    def get_sha2(self, string: str):
        # TODO (there is no api doc in swagger)
        raise NotImplemented

    def is_connected(self):
        return self._get(
            '/subsCrypt/isConnected/'
        )

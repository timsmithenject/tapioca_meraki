# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)


from .resource_mapping import RESOURCE_MAPPING


class MerakiClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://api.meraki.com/api/v1/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(MerakiClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        # Use API token directly in the headers for authentication
        params['headers'] = {
            'Authorization': f'Bearer {api_params.get("access_token")}',
            'Content-Type': 'application/json'
        }

        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


Meraki = generate_wrapper_from_adapter(MerakiClientAdapter)

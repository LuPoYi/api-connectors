# coding: utf-8

"""
    Bybit API

    ## REST API for the Bybit Exchange. Base URI: [https://api-testnet.bybit.com]    # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@bybit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class WalletApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def wallet_get_records(self, **kwargs):  # noqa: E501
        """Get wallet fund records  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_get_records(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date: Start point for result
        :param str end_date: End point for result
        :param str currency: Currency type
        :param str wallet_fund_type: wallet fund type
        :param str page: Page. Default getting first page data
        :param str limit: Limit for data size per page, max size is 50. Default as showing 20 pieces of data per page
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.wallet_get_records_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.wallet_get_records_with_http_info(**kwargs)  # noqa: E501
            return data

    def wallet_get_records_with_http_info(self, **kwargs):  # noqa: E501
        """Get wallet fund records  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_get_records_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date: Start point for result
        :param str end_date: End point for result
        :param str currency: Currency type
        :param str wallet_fund_type: wallet fund type
        :param str page: Page. Default getting first page data
        :param str limit: Limit for data size per page, max size is 50. Default as showing 20 pieces of data per page
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'currency', 'wallet_fund_type', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method wallet_get_records" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'currency' in params:
            query_params.append(('currency', params['currency']))  # noqa: E501
        if 'wallet_fund_type' in params:
            query_params.append(('wallet_fund_type', params['wallet_fund_type']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'apiSignature', 'timestamp']  # noqa: E501

        return self.api_client.call_api(
            '/open-api/wallet/fund/records', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def wallet_get_risk_limit(self, **kwargs):  # noqa: E501
        """Get risk limit.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_get_risk_limit(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.wallet_get_risk_limit_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.wallet_get_risk_limit_with_http_info(**kwargs)  # noqa: E501
            return data

    def wallet_get_risk_limit_with_http_info(self, **kwargs):  # noqa: E501
        """Get risk limit.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_get_risk_limit_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method wallet_get_risk_limit" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'apiSignature', 'timestamp']  # noqa: E501

        return self.api_client.call_api(
            '/open-api/wallet/risk-limit/list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def wallet_set_risk_limit(self, symbol, risk_id, **kwargs):  # noqa: E501
        """Set risk limit  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_set_risk_limit(symbol, risk_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: Contract type. (required)
        :param float risk_id: Risk ID. Can be found with the Get risk limit list endpoint. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.wallet_set_risk_limit_with_http_info(symbol, risk_id, **kwargs)  # noqa: E501
        else:
            (data) = self.wallet_set_risk_limit_with_http_info(symbol, risk_id, **kwargs)  # noqa: E501
            return data

    def wallet_set_risk_limit_with_http_info(self, symbol, risk_id, **kwargs):  # noqa: E501
        """Set risk limit  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_set_risk_limit_with_http_info(symbol, risk_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: Contract type. (required)
        :param float risk_id: Risk ID. Can be found with the Get risk limit list endpoint. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol', 'risk_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method wallet_set_risk_limit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `wallet_set_risk_limit`")  # noqa: E501
        # verify the required parameter 'risk_id' is set
        if ('risk_id' not in params or
                params['risk_id'] is None):
            raise ValueError("Missing the required parameter `risk_id` when calling `wallet_set_risk_limit`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'symbol' in params:
            form_params.append(('symbol', params['symbol']))  # noqa: E501
        if 'risk_id' in params:
            form_params.append(('risk_id', params['risk_id']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'apiSignature', 'timestamp']  # noqa: E501

        return self.api_client.call_api(
            '/open-api/wallet/risk-limit', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def wallet_withdraw(self, **kwargs):  # noqa: E501
        """Get wallet fund records  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_withdraw(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date: Start point for result
        :param str end_date: End point for result
        :param str coin: Currency
        :param str status: Withdraw status
        :param str page: Page. Default getting first page data
        :param str limit: Limit for data size per page, max size is 50. Default as showing 20 pieces of data per page
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.wallet_withdraw_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.wallet_withdraw_with_http_info(**kwargs)  # noqa: E501
            return data

    def wallet_withdraw_with_http_info(self, **kwargs):  # noqa: E501
        """Get wallet fund records  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wallet_withdraw_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date: Start point for result
        :param str end_date: End point for result
        :param str coin: Currency
        :param str status: Withdraw status
        :param str page: Page. Default getting first page data
        :param str limit: Limit for data size per page, max size is 50. Default as showing 20 pieces of data per page
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'coin', 'status', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method wallet_withdraw" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'coin' in params:
            query_params.append(('coin', params['coin']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'apiSignature', 'timestamp']  # noqa: E501

        return self.api_client.call_api(
            '/open-api/wallet/withdraw/list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

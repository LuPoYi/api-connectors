# coding: utf-8

"""
    Bybit API

    ## REST API for the Bybit Exchange. Base URI: [https://api-testnet.bybit.com]    # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@bybit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OrderRes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'order_id': 'str',
        'user_id': 'float',
        'symbol': 'str',
        'side': 'str',
        'order_type': 'str',
        'price': 'float',
        'qty': 'str',
        'time_in_force': 'str',
        'order_status': 'str',
        'last_exec_time': 'float',
        'last_exec_price': 'float',
        'leaves_qty': 'float',
        'cum_exec_qty': 'float',
        'cum_exec_value': 'float',
        'cum_exec_fee': 'float',
        'reject_reason': 'str',
        'order_link_id': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'order_id': 'order_id',
        'user_id': 'user_id',
        'symbol': 'symbol',
        'side': 'side',
        'order_type': 'order_type',
        'price': 'price',
        'qty': 'qty',
        'time_in_force': 'time_in_force',
        'order_status': 'order_status',
        'last_exec_time': 'last_exec_time',
        'last_exec_price': 'last_exec_price',
        'leaves_qty': 'leaves_qty',
        'cum_exec_qty': 'cum_exec_qty',
        'cum_exec_value': 'cum_exec_value',
        'cum_exec_fee': 'cum_exec_fee',
        'reject_reason': 'reject_reason',
        'order_link_id': 'order_link_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, order_id=None, user_id=None, symbol=None, side=None, order_type=None, price=None, qty=None, time_in_force=None, order_status=None, last_exec_time=None, last_exec_price=None, leaves_qty=None, cum_exec_qty=None, cum_exec_value=None, cum_exec_fee=None, reject_reason=None, order_link_id=None, created_at=None, updated_at=None):  # noqa: E501
        """OrderRes - a model defined in Swagger"""  # noqa: E501

        self._order_id = None
        self._user_id = None
        self._symbol = None
        self._side = None
        self._order_type = None
        self._price = None
        self._qty = None
        self._time_in_force = None
        self._order_status = None
        self._last_exec_time = None
        self._last_exec_price = None
        self._leaves_qty = None
        self._cum_exec_qty = None
        self._cum_exec_value = None
        self._cum_exec_fee = None
        self._reject_reason = None
        self._order_link_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if user_id is not None:
            self.user_id = user_id
        if symbol is not None:
            self.symbol = symbol
        if side is not None:
            self.side = side
        if order_type is not None:
            self.order_type = order_type
        if price is not None:
            self.price = price
        if qty is not None:
            self.qty = qty
        if time_in_force is not None:
            self.time_in_force = time_in_force
        if order_status is not None:
            self.order_status = order_status
        if last_exec_time is not None:
            self.last_exec_time = last_exec_time
        if last_exec_price is not None:
            self.last_exec_price = last_exec_price
        if leaves_qty is not None:
            self.leaves_qty = leaves_qty
        if cum_exec_qty is not None:
            self.cum_exec_qty = cum_exec_qty
        if cum_exec_value is not None:
            self.cum_exec_value = cum_exec_value
        if cum_exec_fee is not None:
            self.cum_exec_fee = cum_exec_fee
        if reject_reason is not None:
            self.reject_reason = reject_reason
        if order_link_id is not None:
            self.order_link_id = order_link_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def order_id(self):
        """Gets the order_id of this OrderRes.  # noqa: E501


        :return: The order_id of this OrderRes.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderRes.


        :param order_id: The order_id of this OrderRes.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def user_id(self):
        """Gets the user_id of this OrderRes.  # noqa: E501


        :return: The user_id of this OrderRes.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this OrderRes.


        :param user_id: The user_id of this OrderRes.  # noqa: E501
        :type: float
        """

        self._user_id = user_id

    @property
    def symbol(self):
        """Gets the symbol of this OrderRes.  # noqa: E501


        :return: The symbol of this OrderRes.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this OrderRes.


        :param symbol: The symbol of this OrderRes.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def side(self):
        """Gets the side of this OrderRes.  # noqa: E501


        :return: The side of this OrderRes.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this OrderRes.


        :param side: The side of this OrderRes.  # noqa: E501
        :type: str
        """

        self._side = side

    @property
    def order_type(self):
        """Gets the order_type of this OrderRes.  # noqa: E501


        :return: The order_type of this OrderRes.  # noqa: E501
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this OrderRes.


        :param order_type: The order_type of this OrderRes.  # noqa: E501
        :type: str
        """

        self._order_type = order_type

    @property
    def price(self):
        """Gets the price of this OrderRes.  # noqa: E501


        :return: The price of this OrderRes.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderRes.


        :param price: The price of this OrderRes.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def qty(self):
        """Gets the qty of this OrderRes.  # noqa: E501


        :return: The qty of this OrderRes.  # noqa: E501
        :rtype: str
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this OrderRes.


        :param qty: The qty of this OrderRes.  # noqa: E501
        :type: str
        """

        self._qty = qty

    @property
    def time_in_force(self):
        """Gets the time_in_force of this OrderRes.  # noqa: E501


        :return: The time_in_force of this OrderRes.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this OrderRes.


        :param time_in_force: The time_in_force of this OrderRes.  # noqa: E501
        :type: str
        """

        self._time_in_force = time_in_force

    @property
    def order_status(self):
        """Gets the order_status of this OrderRes.  # noqa: E501


        :return: The order_status of this OrderRes.  # noqa: E501
        :rtype: str
        """
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        """Sets the order_status of this OrderRes.


        :param order_status: The order_status of this OrderRes.  # noqa: E501
        :type: str
        """

        self._order_status = order_status

    @property
    def last_exec_time(self):
        """Gets the last_exec_time of this OrderRes.  # noqa: E501


        :return: The last_exec_time of this OrderRes.  # noqa: E501
        :rtype: float
        """
        return self._last_exec_time

    @last_exec_time.setter
    def last_exec_time(self, last_exec_time):
        """Sets the last_exec_time of this OrderRes.


        :param last_exec_time: The last_exec_time of this OrderRes.  # noqa: E501
        :type: float
        """

        self._last_exec_time = last_exec_time

    @property
    def last_exec_price(self):
        """Gets the last_exec_price of this OrderRes.  # noqa: E501


        :return: The last_exec_price of this OrderRes.  # noqa: E501
        :rtype: float
        """
        return self._last_exec_price

    @last_exec_price.setter
    def last_exec_price(self, last_exec_price):
        """Sets the last_exec_price of this OrderRes.


        :param last_exec_price: The last_exec_price of this OrderRes.  # noqa: E501
        :type: float
        """

        self._last_exec_price = last_exec_price

    @property
    def leaves_qty(self):
        """Gets the leaves_qty of this OrderRes.  # noqa: E501


        :return: The leaves_qty of this OrderRes.  # noqa: E501
        :rtype: float
        """
        return self._leaves_qty

    @leaves_qty.setter
    def leaves_qty(self, leaves_qty):
        """Sets the leaves_qty of this OrderRes.


        :param leaves_qty: The leaves_qty of this OrderRes.  # noqa: E501
        :type: float
        """

        self._leaves_qty = leaves_qty

    @property
    def cum_exec_qty(self):
        """Gets the cum_exec_qty of this OrderRes.  # noqa: E501


        :return: The cum_exec_qty of this OrderRes.  # noqa: E501
        :rtype: float
        """
        return self._cum_exec_qty

    @cum_exec_qty.setter
    def cum_exec_qty(self, cum_exec_qty):
        """Sets the cum_exec_qty of this OrderRes.


        :param cum_exec_qty: The cum_exec_qty of this OrderRes.  # noqa: E501
        :type: float
        """

        self._cum_exec_qty = cum_exec_qty

    @property
    def cum_exec_value(self):
        """Gets the cum_exec_value of this OrderRes.  # noqa: E501


        :return: The cum_exec_value of this OrderRes.  # noqa: E501
        :rtype: float
        """
        return self._cum_exec_value

    @cum_exec_value.setter
    def cum_exec_value(self, cum_exec_value):
        """Sets the cum_exec_value of this OrderRes.


        :param cum_exec_value: The cum_exec_value of this OrderRes.  # noqa: E501
        :type: float
        """

        self._cum_exec_value = cum_exec_value

    @property
    def cum_exec_fee(self):
        """Gets the cum_exec_fee of this OrderRes.  # noqa: E501


        :return: The cum_exec_fee of this OrderRes.  # noqa: E501
        :rtype: float
        """
        return self._cum_exec_fee

    @cum_exec_fee.setter
    def cum_exec_fee(self, cum_exec_fee):
        """Sets the cum_exec_fee of this OrderRes.


        :param cum_exec_fee: The cum_exec_fee of this OrderRes.  # noqa: E501
        :type: float
        """

        self._cum_exec_fee = cum_exec_fee

    @property
    def reject_reason(self):
        """Gets the reject_reason of this OrderRes.  # noqa: E501


        :return: The reject_reason of this OrderRes.  # noqa: E501
        :rtype: str
        """
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, reject_reason):
        """Sets the reject_reason of this OrderRes.


        :param reject_reason: The reject_reason of this OrderRes.  # noqa: E501
        :type: str
        """

        self._reject_reason = reject_reason

    @property
    def order_link_id(self):
        """Gets the order_link_id of this OrderRes.  # noqa: E501


        :return: The order_link_id of this OrderRes.  # noqa: E501
        :rtype: str
        """
        return self._order_link_id

    @order_link_id.setter
    def order_link_id(self, order_link_id):
        """Sets the order_link_id of this OrderRes.


        :param order_link_id: The order_link_id of this OrderRes.  # noqa: E501
        :type: str
        """

        self._order_link_id = order_link_id

    @property
    def created_at(self):
        """Gets the created_at of this OrderRes.  # noqa: E501


        :return: The created_at of this OrderRes.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OrderRes.


        :param created_at: The created_at of this OrderRes.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this OrderRes.  # noqa: E501


        :return: The updated_at of this OrderRes.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this OrderRes.


        :param updated_at: The updated_at of this OrderRes.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OrderRes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrderRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

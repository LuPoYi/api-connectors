/**
 * Bybit API
 * ## REST API for the Bybit Exchange. Base URI: [https://api-testnet.bybit.com]  
 *
 * OpenAPI spec version: 1.0.0
 * Contact: support@bybit.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.8
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.BybitApi) {
      root.BybitApi = {};
    }
    root.BybitApi.SymbolInfo = factory(root.BybitApi.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The SymbolInfo model module.
   * @module model/SymbolInfo
   * @version 1.0.0
   */

  /**
   * Constructs a new <code>SymbolInfo</code>.
   * @alias module:model/SymbolInfo
   * @class
   */
  var exports = function() {
    var _this = this;







  };

  /**
   * Constructs a <code>SymbolInfo</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/SymbolInfo} obj Optional instance to populate.
   * @return {module:model/SymbolInfo} The populated <code>SymbolInfo</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('name')) {
        obj['name'] = ApiClient.convertToType(data['name'], 'String');
      }
      if (data.hasOwnProperty('base_currency')) {
        obj['base_currency'] = ApiClient.convertToType(data['base_currency'], 'String');
      }
      if (data.hasOwnProperty('quote_currency')) {
        obj['quote_currency'] = ApiClient.convertToType(data['quote_currency'], 'String');
      }
      if (data.hasOwnProperty('price_scale')) {
        obj['price_scale'] = ApiClient.convertToType(data['price_scale'], 'Number');
      }
      if (data.hasOwnProperty('price_filter')) {
        obj['price_filter'] = ApiClient.convertToType(data['price_filter'], Object);
      }
      if (data.hasOwnProperty('lot_size_filter')) {
        obj['lot_size_filter'] = ApiClient.convertToType(data['lot_size_filter'], Object);
      }
    }
    return obj;
  }

  /**
   * @member {String} name
   */
  exports.prototype['name'] = undefined;
  /**
   * @member {String} base_currency
   */
  exports.prototype['base_currency'] = undefined;
  /**
   * @member {String} quote_currency
   */
  exports.prototype['quote_currency'] = undefined;
  /**
   * @member {Number} price_scale
   */
  exports.prototype['price_scale'] = undefined;
  /**
   * @member {Object} price_filter
   */
  exports.prototype['price_filter'] = undefined;
  /**
   * @member {Object} lot_size_filter
   */
  exports.prototype['lot_size_filter'] = undefined;



  return exports;
}));



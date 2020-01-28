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
    root.BybitApi.FundingRate = factory(root.BybitApi.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The FundingRate model module.
   * @module model/FundingRate
   * @version 1.0.0
   */

  /**
   * Constructs a new <code>FundingRate</code>.
   * Get the last funding Rate
   * @alias module:model/FundingRate
   * @class
   */
  var exports = function() {
    var _this = this;




  };

  /**
   * Constructs a <code>FundingRate</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/FundingRate} obj Optional instance to populate.
   * @return {module:model/FundingRate} The populated <code>FundingRate</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('symbol')) {
        obj['symbol'] = ApiClient.convertToType(data['symbol'], 'String');
      }
      if (data.hasOwnProperty('funding_rate')) {
        obj['funding_rate'] = ApiClient.convertToType(data['funding_rate'], 'String');
      }
      if (data.hasOwnProperty('funding_rate_timestamp')) {
        obj['funding_rate_timestamp'] = ApiClient.convertToType(data['funding_rate_timestamp'], 'Number');
      }
    }
    return obj;
  }

  /**
   * @member {String} symbol
   */
  exports.prototype['symbol'] = undefined;
  /**
   * @member {String} funding_rate
   */
  exports.prototype['funding_rate'] = undefined;
  /**
   * @member {Number} funding_rate_timestamp
   */
  exports.prototype['funding_rate_timestamp'] = undefined;



  return exports;
}));



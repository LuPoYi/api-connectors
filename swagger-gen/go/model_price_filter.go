/*
 * Bybit API
 *
 * ## REST API for the Bybit Exchange. Base URI: [https://api-testnet.bybit.com]  
 *
 * API version: 1.0.0
 * Contact: support@bybit.com
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package swagger

type PriceFilter struct {
	MinPrice string `json:"min_price,omitempty"`
	MaxPrice string `json:"max_price,omitempty"`
	TickSize string `json:"tick_size,omitempty"`
}

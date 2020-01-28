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

type SymbolInfo struct {
	Name string `json:"name,omitempty"`
	BaseCurrency string `json:"base_currency,omitempty"`
	QuoteCurrency string `json:"quote_currency,omitempty"`
	PriceScale float32 `json:"price_scale,omitempty"`
	PriceFilter *interface{} `json:"price_filter,omitempty"`
	LotSizeFilter *interface{} `json:"lot_size_filter,omitempty"`
}

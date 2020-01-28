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

// Get the last funding fee
type FundingPredicted struct {
	PredictedFundingRate float64 `json:"predicted_funding_rate,omitempty"`
	PredictedFundingFee float64 `json:"predicted_funding_fee,omitempty"`
}

/**
 * Bybit API
 * ## REST API for the Bybit Exchange. Base URI: [https://api-testnet.bybit.com]  
 *
 * OpenAPI spec version: 1.0.0
 * Contact: support@bybit.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import io.swagger.annotations.*;
import com.google.gson.annotations.SerializedName;

@ApiModel(description = "")
public class LeverageResult {
  
  @SerializedName("BTCUSD")
  private Object BTCUSD = null;
  @SerializedName("EOSUSD")
  private Object EOSUSD = null;
  @SerializedName("ETHUSD")
  private Object ETHUSD = null;
  @SerializedName("XRPUSD")
  private Object XRPUSD = null;

  /**
   **/
  @ApiModelProperty(value = "")
  public Object getBTCUSD() {
    return BTCUSD;
  }
  public void setBTCUSD(Object BTCUSD) {
    this.BTCUSD = BTCUSD;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public Object getEOSUSD() {
    return EOSUSD;
  }
  public void setEOSUSD(Object EOSUSD) {
    this.EOSUSD = EOSUSD;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public Object getETHUSD() {
    return ETHUSD;
  }
  public void setETHUSD(Object ETHUSD) {
    this.ETHUSD = ETHUSD;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public Object getXRPUSD() {
    return XRPUSD;
  }
  public void setXRPUSD(Object XRPUSD) {
    this.XRPUSD = XRPUSD;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LeverageResult leverageResult = (LeverageResult) o;
    return (this.BTCUSD == null ? leverageResult.BTCUSD == null : this.BTCUSD.equals(leverageResult.BTCUSD)) &&
        (this.EOSUSD == null ? leverageResult.EOSUSD == null : this.EOSUSD.equals(leverageResult.EOSUSD)) &&
        (this.ETHUSD == null ? leverageResult.ETHUSD == null : this.ETHUSD.equals(leverageResult.ETHUSD)) &&
        (this.XRPUSD == null ? leverageResult.XRPUSD == null : this.XRPUSD.equals(leverageResult.XRPUSD));
  }

  @Override
  public int hashCode() {
    int result = 17;
    result = 31 * result + (this.BTCUSD == null ? 0: this.BTCUSD.hashCode());
    result = 31 * result + (this.EOSUSD == null ? 0: this.EOSUSD.hashCode());
    result = 31 * result + (this.ETHUSD == null ? 0: this.ETHUSD.hashCode());
    result = 31 * result + (this.XRPUSD == null ? 0: this.XRPUSD.hashCode());
    return result;
  }

  @Override
  public String toString()  {
    StringBuilder sb = new StringBuilder();
    sb.append("class LeverageResult {\n");
    
    sb.append("  BTCUSD: ").append(BTCUSD).append("\n");
    sb.append("  EOSUSD: ").append(EOSUSD).append("\n");
    sb.append("  ETHUSD: ").append(ETHUSD).append("\n");
    sb.append("  XRPUSD: ").append(XRPUSD).append("\n");
    sb.append("}\n");
    return sb.toString();
  }
}

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

import io.swagger.client.model.WithdrawRecords;
import java.math.BigDecimal;
import java.util.*;
import io.swagger.annotations.*;
import com.google.gson.annotations.SerializedName;

/**
 * Get account withdraw records response
 **/
@ApiModel(description = "Get account withdraw records response")
public class WithdrawResBase {
  
  @SerializedName("ret_code")
  private BigDecimal retCode = null;
  @SerializedName("ret_msg")
  private String retMsg = null;
  @SerializedName("ext_code")
  private String extCode = null;
  @SerializedName("ext_info")
  private String extInfo = null;
  @SerializedName("result")
  private List<WithdrawRecords> result = null;
  @SerializedName("time_now")
  private String timeNow = null;

  /**
   **/
  @ApiModelProperty(value = "")
  public BigDecimal getRetCode() {
    return retCode;
  }
  public void setRetCode(BigDecimal retCode) {
    this.retCode = retCode;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getRetMsg() {
    return retMsg;
  }
  public void setRetMsg(String retMsg) {
    this.retMsg = retMsg;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getExtCode() {
    return extCode;
  }
  public void setExtCode(String extCode) {
    this.extCode = extCode;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getExtInfo() {
    return extInfo;
  }
  public void setExtInfo(String extInfo) {
    this.extInfo = extInfo;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public List<WithdrawRecords> getResult() {
    return result;
  }
  public void setResult(List<WithdrawRecords> result) {
    this.result = result;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getTimeNow() {
    return timeNow;
  }
  public void setTimeNow(String timeNow) {
    this.timeNow = timeNow;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    WithdrawResBase withdrawResBase = (WithdrawResBase) o;
    return (this.retCode == null ? withdrawResBase.retCode == null : this.retCode.equals(withdrawResBase.retCode)) &&
        (this.retMsg == null ? withdrawResBase.retMsg == null : this.retMsg.equals(withdrawResBase.retMsg)) &&
        (this.extCode == null ? withdrawResBase.extCode == null : this.extCode.equals(withdrawResBase.extCode)) &&
        (this.extInfo == null ? withdrawResBase.extInfo == null : this.extInfo.equals(withdrawResBase.extInfo)) &&
        (this.result == null ? withdrawResBase.result == null : this.result.equals(withdrawResBase.result)) &&
        (this.timeNow == null ? withdrawResBase.timeNow == null : this.timeNow.equals(withdrawResBase.timeNow));
  }

  @Override
  public int hashCode() {
    int result = 17;
    result = 31 * result + (this.retCode == null ? 0: this.retCode.hashCode());
    result = 31 * result + (this.retMsg == null ? 0: this.retMsg.hashCode());
    result = 31 * result + (this.extCode == null ? 0: this.extCode.hashCode());
    result = 31 * result + (this.extInfo == null ? 0: this.extInfo.hashCode());
    result = 31 * result + (this.result == null ? 0: this.result.hashCode());
    result = 31 * result + (this.timeNow == null ? 0: this.timeNow.hashCode());
    return result;
  }

  @Override
  public String toString()  {
    StringBuilder sb = new StringBuilder();
    sb.append("class WithdrawResBase {\n");
    
    sb.append("  retCode: ").append(retCode).append("\n");
    sb.append("  retMsg: ").append(retMsg).append("\n");
    sb.append("  extCode: ").append(extCode).append("\n");
    sb.append("  extInfo: ").append(extInfo).append("\n");
    sb.append("  result: ").append(result).append("\n");
    sb.append("  timeNow: ").append(timeNow).append("\n");
    sb.append("}\n");
    return sb.toString();
  }
}

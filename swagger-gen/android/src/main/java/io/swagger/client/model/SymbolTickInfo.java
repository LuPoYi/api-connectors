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

import java.math.BigDecimal;
import io.swagger.annotations.*;
import com.google.gson.annotations.SerializedName;

/**
 * Get the orderbook response
 **/
@ApiModel(description = "Get the orderbook response")
public class SymbolTickInfo {
  
  @SerializedName("symbol")
  private String symbol = null;
  @SerializedName("bid_price")
  private String bidPrice = null;
  @SerializedName("ask_price")
  private String askPrice = null;
  @SerializedName("last_price")
  private String lastPrice = null;
  @SerializedName("last_tick_direction")
  private String lastTickDirection = null;
  @SerializedName("prev_price_24h")
  private String prevPrice24h = null;
  @SerializedName("price_24h_pcnt")
  private String price24hPcnt = null;
  @SerializedName("high_price_24h")
  private String highPrice24h = null;
  @SerializedName("low_price_24h")
  private String lowPrice24h = null;
  @SerializedName("prev_price_1h")
  private String prevPrice1h = null;
  @SerializedName("price_1h_pcnt")
  private String price1hPcnt = null;
  @SerializedName("mark_price")
  private String markPrice = null;
  @SerializedName("index_price")
  private String indexPrice = null;
  @SerializedName("open_interest")
  private BigDecimal openInterest = null;
  @SerializedName("open_value")
  private String openValue = null;
  @SerializedName("total_turnover")
  private String totalTurnover = null;
  @SerializedName("turnover_24h")
  private String turnover24h = null;
  @SerializedName("total_volume")
  private BigDecimal totalVolume = null;
  @SerializedName("volume_24h")
  private BigDecimal volume24h = null;
  @SerializedName("funding_rate")
  private String fundingRate = null;
  @SerializedName("predicted_funding_rate")
  private String predictedFundingRate = null;
  @SerializedName("next_funding_time")
  private String nextFundingTime = null;
  @SerializedName("countdown_hour")
  private BigDecimal countdownHour = null;

  /**
   **/
  @ApiModelProperty(value = "")
  public String getSymbol() {
    return symbol;
  }
  public void setSymbol(String symbol) {
    this.symbol = symbol;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getBidPrice() {
    return bidPrice;
  }
  public void setBidPrice(String bidPrice) {
    this.bidPrice = bidPrice;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getAskPrice() {
    return askPrice;
  }
  public void setAskPrice(String askPrice) {
    this.askPrice = askPrice;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getLastPrice() {
    return lastPrice;
  }
  public void setLastPrice(String lastPrice) {
    this.lastPrice = lastPrice;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getLastTickDirection() {
    return lastTickDirection;
  }
  public void setLastTickDirection(String lastTickDirection) {
    this.lastTickDirection = lastTickDirection;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getPrevPrice24h() {
    return prevPrice24h;
  }
  public void setPrevPrice24h(String prevPrice24h) {
    this.prevPrice24h = prevPrice24h;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getPrice24hPcnt() {
    return price24hPcnt;
  }
  public void setPrice24hPcnt(String price24hPcnt) {
    this.price24hPcnt = price24hPcnt;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getHighPrice24h() {
    return highPrice24h;
  }
  public void setHighPrice24h(String highPrice24h) {
    this.highPrice24h = highPrice24h;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getLowPrice24h() {
    return lowPrice24h;
  }
  public void setLowPrice24h(String lowPrice24h) {
    this.lowPrice24h = lowPrice24h;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getPrevPrice1h() {
    return prevPrice1h;
  }
  public void setPrevPrice1h(String prevPrice1h) {
    this.prevPrice1h = prevPrice1h;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getPrice1hPcnt() {
    return price1hPcnt;
  }
  public void setPrice1hPcnt(String price1hPcnt) {
    this.price1hPcnt = price1hPcnt;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getMarkPrice() {
    return markPrice;
  }
  public void setMarkPrice(String markPrice) {
    this.markPrice = markPrice;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getIndexPrice() {
    return indexPrice;
  }
  public void setIndexPrice(String indexPrice) {
    this.indexPrice = indexPrice;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public BigDecimal getOpenInterest() {
    return openInterest;
  }
  public void setOpenInterest(BigDecimal openInterest) {
    this.openInterest = openInterest;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getOpenValue() {
    return openValue;
  }
  public void setOpenValue(String openValue) {
    this.openValue = openValue;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getTotalTurnover() {
    return totalTurnover;
  }
  public void setTotalTurnover(String totalTurnover) {
    this.totalTurnover = totalTurnover;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getTurnover24h() {
    return turnover24h;
  }
  public void setTurnover24h(String turnover24h) {
    this.turnover24h = turnover24h;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public BigDecimal getTotalVolume() {
    return totalVolume;
  }
  public void setTotalVolume(BigDecimal totalVolume) {
    this.totalVolume = totalVolume;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public BigDecimal getVolume24h() {
    return volume24h;
  }
  public void setVolume24h(BigDecimal volume24h) {
    this.volume24h = volume24h;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getFundingRate() {
    return fundingRate;
  }
  public void setFundingRate(String fundingRate) {
    this.fundingRate = fundingRate;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getPredictedFundingRate() {
    return predictedFundingRate;
  }
  public void setPredictedFundingRate(String predictedFundingRate) {
    this.predictedFundingRate = predictedFundingRate;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getNextFundingTime() {
    return nextFundingTime;
  }
  public void setNextFundingTime(String nextFundingTime) {
    this.nextFundingTime = nextFundingTime;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public BigDecimal getCountdownHour() {
    return countdownHour;
  }
  public void setCountdownHour(BigDecimal countdownHour) {
    this.countdownHour = countdownHour;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SymbolTickInfo symbolTickInfo = (SymbolTickInfo) o;
    return (this.symbol == null ? symbolTickInfo.symbol == null : this.symbol.equals(symbolTickInfo.symbol)) &&
        (this.bidPrice == null ? symbolTickInfo.bidPrice == null : this.bidPrice.equals(symbolTickInfo.bidPrice)) &&
        (this.askPrice == null ? symbolTickInfo.askPrice == null : this.askPrice.equals(symbolTickInfo.askPrice)) &&
        (this.lastPrice == null ? symbolTickInfo.lastPrice == null : this.lastPrice.equals(symbolTickInfo.lastPrice)) &&
        (this.lastTickDirection == null ? symbolTickInfo.lastTickDirection == null : this.lastTickDirection.equals(symbolTickInfo.lastTickDirection)) &&
        (this.prevPrice24h == null ? symbolTickInfo.prevPrice24h == null : this.prevPrice24h.equals(symbolTickInfo.prevPrice24h)) &&
        (this.price24hPcnt == null ? symbolTickInfo.price24hPcnt == null : this.price24hPcnt.equals(symbolTickInfo.price24hPcnt)) &&
        (this.highPrice24h == null ? symbolTickInfo.highPrice24h == null : this.highPrice24h.equals(symbolTickInfo.highPrice24h)) &&
        (this.lowPrice24h == null ? symbolTickInfo.lowPrice24h == null : this.lowPrice24h.equals(symbolTickInfo.lowPrice24h)) &&
        (this.prevPrice1h == null ? symbolTickInfo.prevPrice1h == null : this.prevPrice1h.equals(symbolTickInfo.prevPrice1h)) &&
        (this.price1hPcnt == null ? symbolTickInfo.price1hPcnt == null : this.price1hPcnt.equals(symbolTickInfo.price1hPcnt)) &&
        (this.markPrice == null ? symbolTickInfo.markPrice == null : this.markPrice.equals(symbolTickInfo.markPrice)) &&
        (this.indexPrice == null ? symbolTickInfo.indexPrice == null : this.indexPrice.equals(symbolTickInfo.indexPrice)) &&
        (this.openInterest == null ? symbolTickInfo.openInterest == null : this.openInterest.equals(symbolTickInfo.openInterest)) &&
        (this.openValue == null ? symbolTickInfo.openValue == null : this.openValue.equals(symbolTickInfo.openValue)) &&
        (this.totalTurnover == null ? symbolTickInfo.totalTurnover == null : this.totalTurnover.equals(symbolTickInfo.totalTurnover)) &&
        (this.turnover24h == null ? symbolTickInfo.turnover24h == null : this.turnover24h.equals(symbolTickInfo.turnover24h)) &&
        (this.totalVolume == null ? symbolTickInfo.totalVolume == null : this.totalVolume.equals(symbolTickInfo.totalVolume)) &&
        (this.volume24h == null ? symbolTickInfo.volume24h == null : this.volume24h.equals(symbolTickInfo.volume24h)) &&
        (this.fundingRate == null ? symbolTickInfo.fundingRate == null : this.fundingRate.equals(symbolTickInfo.fundingRate)) &&
        (this.predictedFundingRate == null ? symbolTickInfo.predictedFundingRate == null : this.predictedFundingRate.equals(symbolTickInfo.predictedFundingRate)) &&
        (this.nextFundingTime == null ? symbolTickInfo.nextFundingTime == null : this.nextFundingTime.equals(symbolTickInfo.nextFundingTime)) &&
        (this.countdownHour == null ? symbolTickInfo.countdownHour == null : this.countdownHour.equals(symbolTickInfo.countdownHour));
  }

  @Override
  public int hashCode() {
    int result = 17;
    result = 31 * result + (this.symbol == null ? 0: this.symbol.hashCode());
    result = 31 * result + (this.bidPrice == null ? 0: this.bidPrice.hashCode());
    result = 31 * result + (this.askPrice == null ? 0: this.askPrice.hashCode());
    result = 31 * result + (this.lastPrice == null ? 0: this.lastPrice.hashCode());
    result = 31 * result + (this.lastTickDirection == null ? 0: this.lastTickDirection.hashCode());
    result = 31 * result + (this.prevPrice24h == null ? 0: this.prevPrice24h.hashCode());
    result = 31 * result + (this.price24hPcnt == null ? 0: this.price24hPcnt.hashCode());
    result = 31 * result + (this.highPrice24h == null ? 0: this.highPrice24h.hashCode());
    result = 31 * result + (this.lowPrice24h == null ? 0: this.lowPrice24h.hashCode());
    result = 31 * result + (this.prevPrice1h == null ? 0: this.prevPrice1h.hashCode());
    result = 31 * result + (this.price1hPcnt == null ? 0: this.price1hPcnt.hashCode());
    result = 31 * result + (this.markPrice == null ? 0: this.markPrice.hashCode());
    result = 31 * result + (this.indexPrice == null ? 0: this.indexPrice.hashCode());
    result = 31 * result + (this.openInterest == null ? 0: this.openInterest.hashCode());
    result = 31 * result + (this.openValue == null ? 0: this.openValue.hashCode());
    result = 31 * result + (this.totalTurnover == null ? 0: this.totalTurnover.hashCode());
    result = 31 * result + (this.turnover24h == null ? 0: this.turnover24h.hashCode());
    result = 31 * result + (this.totalVolume == null ? 0: this.totalVolume.hashCode());
    result = 31 * result + (this.volume24h == null ? 0: this.volume24h.hashCode());
    result = 31 * result + (this.fundingRate == null ? 0: this.fundingRate.hashCode());
    result = 31 * result + (this.predictedFundingRate == null ? 0: this.predictedFundingRate.hashCode());
    result = 31 * result + (this.nextFundingTime == null ? 0: this.nextFundingTime.hashCode());
    result = 31 * result + (this.countdownHour == null ? 0: this.countdownHour.hashCode());
    return result;
  }

  @Override
  public String toString()  {
    StringBuilder sb = new StringBuilder();
    sb.append("class SymbolTickInfo {\n");
    
    sb.append("  symbol: ").append(symbol).append("\n");
    sb.append("  bidPrice: ").append(bidPrice).append("\n");
    sb.append("  askPrice: ").append(askPrice).append("\n");
    sb.append("  lastPrice: ").append(lastPrice).append("\n");
    sb.append("  lastTickDirection: ").append(lastTickDirection).append("\n");
    sb.append("  prevPrice24h: ").append(prevPrice24h).append("\n");
    sb.append("  price24hPcnt: ").append(price24hPcnt).append("\n");
    sb.append("  highPrice24h: ").append(highPrice24h).append("\n");
    sb.append("  lowPrice24h: ").append(lowPrice24h).append("\n");
    sb.append("  prevPrice1h: ").append(prevPrice1h).append("\n");
    sb.append("  price1hPcnt: ").append(price1hPcnt).append("\n");
    sb.append("  markPrice: ").append(markPrice).append("\n");
    sb.append("  indexPrice: ").append(indexPrice).append("\n");
    sb.append("  openInterest: ").append(openInterest).append("\n");
    sb.append("  openValue: ").append(openValue).append("\n");
    sb.append("  totalTurnover: ").append(totalTurnover).append("\n");
    sb.append("  turnover24h: ").append(turnover24h).append("\n");
    sb.append("  totalVolume: ").append(totalVolume).append("\n");
    sb.append("  volume24h: ").append(volume24h).append("\n");
    sb.append("  fundingRate: ").append(fundingRate).append("\n");
    sb.append("  predictedFundingRate: ").append(predictedFundingRate).append("\n");
    sb.append("  nextFundingTime: ").append(nextFundingTime).append("\n");
    sb.append("  countdownHour: ").append(countdownHour).append("\n");
    sb.append("}\n");
    return sb.toString();
  }
}

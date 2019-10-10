/* 
 * Bybit API
 *
 * ## REST API for the Bybit Exchange. 
 *
 * OpenAPI spec version: 1.0.0
 * Contact: support@bybit.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// PositionInfo.
    /// </summary>
    [DataContract]
    public partial class PositionInfo :  IEquatable<PositionInfo>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="PositionInfo" /> class.
        /// </summary>
        /// <param name="id">id.</param>
        /// <param name="userId">userId.</param>
        /// <param name="riskId">riskId.</param>
        /// <param name="symbol">symbol.</param>
        /// <param name="side">side.</param>
        /// <param name="size">size.</param>
        /// <param name="positionValue">positionValue.</param>
        /// <param name="entryPrice">entryPrice.</param>
        /// <param name="leverage">leverage.</param>
        /// <param name="autoAddMargin">autoAddMargin.</param>
        /// <param name="positionMargin">positionMargin.</param>
        /// <param name="liqPrice">liqPrice.</param>
        /// <param name="bustPrice">bustPrice.</param>
        /// <param name="occClosingFee">occClosingFee.</param>
        /// <param name="occFundingFee">occFundingFee.</param>
        /// <param name="takeProfit">takeProfit.</param>
        /// <param name="stopLoss">stopLoss.</param>
        /// <param name="trailingStop">trailingStop.</param>
        /// <param name="positionStatus">positionStatus.</param>
        /// <param name="deleverageIndicator">deleverageIndicator.</param>
        /// <param name="ocCalcData">ocCalcData.</param>
        /// <param name="orderMargin">orderMargin.</param>
        /// <param name="walletBalance">walletBalance.</param>
        /// <param name="unrealisedPnl">unrealisedPnl.</param>
        /// <param name="realisedPnl">realisedPnl.</param>
        /// <param name="cumRealisedPnl">cumRealisedPnl.</param>
        /// <param name="cumCommission">cumCommission.</param>
        /// <param name="crossSeq">crossSeq.</param>
        /// <param name="positionSeq">positionSeq.</param>
        /// <param name="createdAt">createdAt.</param>
        /// <param name="updatedAt">updatedAt.</param>
        public PositionInfo(decimal? id = default(decimal?), decimal? userId = default(decimal?), decimal? riskId = default(decimal?), string symbol = default(string), string side = default(string), decimal? size = default(decimal?), decimal? positionValue = default(decimal?), decimal? entryPrice = default(decimal?), decimal? leverage = default(decimal?), decimal? autoAddMargin = default(decimal?), decimal? positionMargin = default(decimal?), decimal? liqPrice = default(decimal?), decimal? bustPrice = default(decimal?), decimal? occClosingFee = default(decimal?), decimal? occFundingFee = default(decimal?), decimal? takeProfit = default(decimal?), decimal? stopLoss = default(decimal?), decimal? trailingStop = default(decimal?), string positionStatus = default(string), string deleverageIndicator = default(string), string ocCalcData = default(string), decimal? orderMargin = default(decimal?), decimal? walletBalance = default(decimal?), decimal? unrealisedPnl = default(decimal?), decimal? realisedPnl = default(decimal?), decimal? cumRealisedPnl = default(decimal?), decimal? cumCommission = default(decimal?), decimal? crossSeq = default(decimal?), decimal? positionSeq = default(decimal?), string createdAt = default(string), string updatedAt = default(string))
        {
            this.Id = id;
            this.UserId = userId;
            this.RiskId = riskId;
            this.Symbol = symbol;
            this.Side = side;
            this.Size = size;
            this.PositionValue = positionValue;
            this.EntryPrice = entryPrice;
            this.Leverage = leverage;
            this.AutoAddMargin = autoAddMargin;
            this.PositionMargin = positionMargin;
            this.LiqPrice = liqPrice;
            this.BustPrice = bustPrice;
            this.OccClosingFee = occClosingFee;
            this.OccFundingFee = occFundingFee;
            this.TakeProfit = takeProfit;
            this.StopLoss = stopLoss;
            this.TrailingStop = trailingStop;
            this.PositionStatus = positionStatus;
            this.DeleverageIndicator = deleverageIndicator;
            this.OcCalcData = ocCalcData;
            this.OrderMargin = orderMargin;
            this.WalletBalance = walletBalance;
            this.UnrealisedPnl = unrealisedPnl;
            this.RealisedPnl = realisedPnl;
            this.CumRealisedPnl = cumRealisedPnl;
            this.CumCommission = cumCommission;
            this.CrossSeq = crossSeq;
            this.PositionSeq = positionSeq;
            this.CreatedAt = createdAt;
            this.UpdatedAt = updatedAt;
        }
        
        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public decimal? Id { get; set; }

        /// <summary>
        /// Gets or Sets UserId
        /// </summary>
        [DataMember(Name="user_id", EmitDefaultValue=false)]
        public decimal? UserId { get; set; }

        /// <summary>
        /// Gets or Sets RiskId
        /// </summary>
        [DataMember(Name="risk_id", EmitDefaultValue=false)]
        public decimal? RiskId { get; set; }

        /// <summary>
        /// Gets or Sets Symbol
        /// </summary>
        [DataMember(Name="symbol", EmitDefaultValue=false)]
        public string Symbol { get; set; }

        /// <summary>
        /// Gets or Sets Side
        /// </summary>
        [DataMember(Name="side", EmitDefaultValue=false)]
        public string Side { get; set; }

        /// <summary>
        /// Gets or Sets Size
        /// </summary>
        [DataMember(Name="size", EmitDefaultValue=false)]
        public decimal? Size { get; set; }

        /// <summary>
        /// Gets or Sets PositionValue
        /// </summary>
        [DataMember(Name="position_value", EmitDefaultValue=false)]
        public decimal? PositionValue { get; set; }

        /// <summary>
        /// Gets or Sets EntryPrice
        /// </summary>
        [DataMember(Name="entry_price", EmitDefaultValue=false)]
        public decimal? EntryPrice { get; set; }

        /// <summary>
        /// Gets or Sets Leverage
        /// </summary>
        [DataMember(Name="leverage", EmitDefaultValue=false)]
        public decimal? Leverage { get; set; }

        /// <summary>
        /// Gets or Sets AutoAddMargin
        /// </summary>
        [DataMember(Name="auto_add_margin", EmitDefaultValue=false)]
        public decimal? AutoAddMargin { get; set; }

        /// <summary>
        /// Gets or Sets PositionMargin
        /// </summary>
        [DataMember(Name="position_margin", EmitDefaultValue=false)]
        public decimal? PositionMargin { get; set; }

        /// <summary>
        /// Gets or Sets LiqPrice
        /// </summary>
        [DataMember(Name="liq_price", EmitDefaultValue=false)]
        public decimal? LiqPrice { get; set; }

        /// <summary>
        /// Gets or Sets BustPrice
        /// </summary>
        [DataMember(Name="bust_price", EmitDefaultValue=false)]
        public decimal? BustPrice { get; set; }

        /// <summary>
        /// Gets or Sets OccClosingFee
        /// </summary>
        [DataMember(Name="occ_closing_fee", EmitDefaultValue=false)]
        public decimal? OccClosingFee { get; set; }

        /// <summary>
        /// Gets or Sets OccFundingFee
        /// </summary>
        [DataMember(Name="occ_funding_fee", EmitDefaultValue=false)]
        public decimal? OccFundingFee { get; set; }

        /// <summary>
        /// Gets or Sets TakeProfit
        /// </summary>
        [DataMember(Name="take_profit", EmitDefaultValue=false)]
        public decimal? TakeProfit { get; set; }

        /// <summary>
        /// Gets or Sets StopLoss
        /// </summary>
        [DataMember(Name="stop_loss", EmitDefaultValue=false)]
        public decimal? StopLoss { get; set; }

        /// <summary>
        /// Gets or Sets TrailingStop
        /// </summary>
        [DataMember(Name="trailing_stop", EmitDefaultValue=false)]
        public decimal? TrailingStop { get; set; }

        /// <summary>
        /// Gets or Sets PositionStatus
        /// </summary>
        [DataMember(Name="position_status", EmitDefaultValue=false)]
        public string PositionStatus { get; set; }

        /// <summary>
        /// Gets or Sets DeleverageIndicator
        /// </summary>
        [DataMember(Name="deleverage_indicator", EmitDefaultValue=false)]
        public string DeleverageIndicator { get; set; }

        /// <summary>
        /// Gets or Sets OcCalcData
        /// </summary>
        [DataMember(Name="oc_calc_data", EmitDefaultValue=false)]
        public string OcCalcData { get; set; }

        /// <summary>
        /// Gets or Sets OrderMargin
        /// </summary>
        [DataMember(Name="order_margin", EmitDefaultValue=false)]
        public decimal? OrderMargin { get; set; }

        /// <summary>
        /// Gets or Sets WalletBalance
        /// </summary>
        [DataMember(Name="wallet_balance", EmitDefaultValue=false)]
        public decimal? WalletBalance { get; set; }

        /// <summary>
        /// Gets or Sets UnrealisedPnl
        /// </summary>
        [DataMember(Name="unrealised_pnl", EmitDefaultValue=false)]
        public decimal? UnrealisedPnl { get; set; }

        /// <summary>
        /// Gets or Sets RealisedPnl
        /// </summary>
        [DataMember(Name="realised_pnl", EmitDefaultValue=false)]
        public decimal? RealisedPnl { get; set; }

        /// <summary>
        /// Gets or Sets CumRealisedPnl
        /// </summary>
        [DataMember(Name="cum_realised_pnl", EmitDefaultValue=false)]
        public decimal? CumRealisedPnl { get; set; }

        /// <summary>
        /// Gets or Sets CumCommission
        /// </summary>
        [DataMember(Name="cum_commission", EmitDefaultValue=false)]
        public decimal? CumCommission { get; set; }

        /// <summary>
        /// Gets or Sets CrossSeq
        /// </summary>
        [DataMember(Name="cross_seq", EmitDefaultValue=false)]
        public decimal? CrossSeq { get; set; }

        /// <summary>
        /// Gets or Sets PositionSeq
        /// </summary>
        [DataMember(Name="position_seq", EmitDefaultValue=false)]
        public decimal? PositionSeq { get; set; }

        /// <summary>
        /// Gets or Sets CreatedAt
        /// </summary>
        [DataMember(Name="created_at", EmitDefaultValue=false)]
        public string CreatedAt { get; set; }

        /// <summary>
        /// Gets or Sets UpdatedAt
        /// </summary>
        [DataMember(Name="updated_at", EmitDefaultValue=false)]
        public string UpdatedAt { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class PositionInfo {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  UserId: ").Append(UserId).Append("\n");
            sb.Append("  RiskId: ").Append(RiskId).Append("\n");
            sb.Append("  Symbol: ").Append(Symbol).Append("\n");
            sb.Append("  Side: ").Append(Side).Append("\n");
            sb.Append("  Size: ").Append(Size).Append("\n");
            sb.Append("  PositionValue: ").Append(PositionValue).Append("\n");
            sb.Append("  EntryPrice: ").Append(EntryPrice).Append("\n");
            sb.Append("  Leverage: ").Append(Leverage).Append("\n");
            sb.Append("  AutoAddMargin: ").Append(AutoAddMargin).Append("\n");
            sb.Append("  PositionMargin: ").Append(PositionMargin).Append("\n");
            sb.Append("  LiqPrice: ").Append(LiqPrice).Append("\n");
            sb.Append("  BustPrice: ").Append(BustPrice).Append("\n");
            sb.Append("  OccClosingFee: ").Append(OccClosingFee).Append("\n");
            sb.Append("  OccFundingFee: ").Append(OccFundingFee).Append("\n");
            sb.Append("  TakeProfit: ").Append(TakeProfit).Append("\n");
            sb.Append("  StopLoss: ").Append(StopLoss).Append("\n");
            sb.Append("  TrailingStop: ").Append(TrailingStop).Append("\n");
            sb.Append("  PositionStatus: ").Append(PositionStatus).Append("\n");
            sb.Append("  DeleverageIndicator: ").Append(DeleverageIndicator).Append("\n");
            sb.Append("  OcCalcData: ").Append(OcCalcData).Append("\n");
            sb.Append("  OrderMargin: ").Append(OrderMargin).Append("\n");
            sb.Append("  WalletBalance: ").Append(WalletBalance).Append("\n");
            sb.Append("  UnrealisedPnl: ").Append(UnrealisedPnl).Append("\n");
            sb.Append("  RealisedPnl: ").Append(RealisedPnl).Append("\n");
            sb.Append("  CumRealisedPnl: ").Append(CumRealisedPnl).Append("\n");
            sb.Append("  CumCommission: ").Append(CumCommission).Append("\n");
            sb.Append("  CrossSeq: ").Append(CrossSeq).Append("\n");
            sb.Append("  PositionSeq: ").Append(PositionSeq).Append("\n");
            sb.Append("  CreatedAt: ").Append(CreatedAt).Append("\n");
            sb.Append("  UpdatedAt: ").Append(UpdatedAt).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as PositionInfo);
        }

        /// <summary>
        /// Returns true if PositionInfo instances are equal
        /// </summary>
        /// <param name="input">Instance of PositionInfo to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(PositionInfo input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
                ) && 
                (
                    this.UserId == input.UserId ||
                    (this.UserId != null &&
                    this.UserId.Equals(input.UserId))
                ) && 
                (
                    this.RiskId == input.RiskId ||
                    (this.RiskId != null &&
                    this.RiskId.Equals(input.RiskId))
                ) && 
                (
                    this.Symbol == input.Symbol ||
                    (this.Symbol != null &&
                    this.Symbol.Equals(input.Symbol))
                ) && 
                (
                    this.Side == input.Side ||
                    (this.Side != null &&
                    this.Side.Equals(input.Side))
                ) && 
                (
                    this.Size == input.Size ||
                    (this.Size != null &&
                    this.Size.Equals(input.Size))
                ) && 
                (
                    this.PositionValue == input.PositionValue ||
                    (this.PositionValue != null &&
                    this.PositionValue.Equals(input.PositionValue))
                ) && 
                (
                    this.EntryPrice == input.EntryPrice ||
                    (this.EntryPrice != null &&
                    this.EntryPrice.Equals(input.EntryPrice))
                ) && 
                (
                    this.Leverage == input.Leverage ||
                    (this.Leverage != null &&
                    this.Leverage.Equals(input.Leverage))
                ) && 
                (
                    this.AutoAddMargin == input.AutoAddMargin ||
                    (this.AutoAddMargin != null &&
                    this.AutoAddMargin.Equals(input.AutoAddMargin))
                ) && 
                (
                    this.PositionMargin == input.PositionMargin ||
                    (this.PositionMargin != null &&
                    this.PositionMargin.Equals(input.PositionMargin))
                ) && 
                (
                    this.LiqPrice == input.LiqPrice ||
                    (this.LiqPrice != null &&
                    this.LiqPrice.Equals(input.LiqPrice))
                ) && 
                (
                    this.BustPrice == input.BustPrice ||
                    (this.BustPrice != null &&
                    this.BustPrice.Equals(input.BustPrice))
                ) && 
                (
                    this.OccClosingFee == input.OccClosingFee ||
                    (this.OccClosingFee != null &&
                    this.OccClosingFee.Equals(input.OccClosingFee))
                ) && 
                (
                    this.OccFundingFee == input.OccFundingFee ||
                    (this.OccFundingFee != null &&
                    this.OccFundingFee.Equals(input.OccFundingFee))
                ) && 
                (
                    this.TakeProfit == input.TakeProfit ||
                    (this.TakeProfit != null &&
                    this.TakeProfit.Equals(input.TakeProfit))
                ) && 
                (
                    this.StopLoss == input.StopLoss ||
                    (this.StopLoss != null &&
                    this.StopLoss.Equals(input.StopLoss))
                ) && 
                (
                    this.TrailingStop == input.TrailingStop ||
                    (this.TrailingStop != null &&
                    this.TrailingStop.Equals(input.TrailingStop))
                ) && 
                (
                    this.PositionStatus == input.PositionStatus ||
                    (this.PositionStatus != null &&
                    this.PositionStatus.Equals(input.PositionStatus))
                ) && 
                (
                    this.DeleverageIndicator == input.DeleverageIndicator ||
                    (this.DeleverageIndicator != null &&
                    this.DeleverageIndicator.Equals(input.DeleverageIndicator))
                ) && 
                (
                    this.OcCalcData == input.OcCalcData ||
                    (this.OcCalcData != null &&
                    this.OcCalcData.Equals(input.OcCalcData))
                ) && 
                (
                    this.OrderMargin == input.OrderMargin ||
                    (this.OrderMargin != null &&
                    this.OrderMargin.Equals(input.OrderMargin))
                ) && 
                (
                    this.WalletBalance == input.WalletBalance ||
                    (this.WalletBalance != null &&
                    this.WalletBalance.Equals(input.WalletBalance))
                ) && 
                (
                    this.UnrealisedPnl == input.UnrealisedPnl ||
                    (this.UnrealisedPnl != null &&
                    this.UnrealisedPnl.Equals(input.UnrealisedPnl))
                ) && 
                (
                    this.RealisedPnl == input.RealisedPnl ||
                    (this.RealisedPnl != null &&
                    this.RealisedPnl.Equals(input.RealisedPnl))
                ) && 
                (
                    this.CumRealisedPnl == input.CumRealisedPnl ||
                    (this.CumRealisedPnl != null &&
                    this.CumRealisedPnl.Equals(input.CumRealisedPnl))
                ) && 
                (
                    this.CumCommission == input.CumCommission ||
                    (this.CumCommission != null &&
                    this.CumCommission.Equals(input.CumCommission))
                ) && 
                (
                    this.CrossSeq == input.CrossSeq ||
                    (this.CrossSeq != null &&
                    this.CrossSeq.Equals(input.CrossSeq))
                ) && 
                (
                    this.PositionSeq == input.PositionSeq ||
                    (this.PositionSeq != null &&
                    this.PositionSeq.Equals(input.PositionSeq))
                ) && 
                (
                    this.CreatedAt == input.CreatedAt ||
                    (this.CreatedAt != null &&
                    this.CreatedAt.Equals(input.CreatedAt))
                ) && 
                (
                    this.UpdatedAt == input.UpdatedAt ||
                    (this.UpdatedAt != null &&
                    this.UpdatedAt.Equals(input.UpdatedAt))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
                if (this.UserId != null)
                    hashCode = hashCode * 59 + this.UserId.GetHashCode();
                if (this.RiskId != null)
                    hashCode = hashCode * 59 + this.RiskId.GetHashCode();
                if (this.Symbol != null)
                    hashCode = hashCode * 59 + this.Symbol.GetHashCode();
                if (this.Side != null)
                    hashCode = hashCode * 59 + this.Side.GetHashCode();
                if (this.Size != null)
                    hashCode = hashCode * 59 + this.Size.GetHashCode();
                if (this.PositionValue != null)
                    hashCode = hashCode * 59 + this.PositionValue.GetHashCode();
                if (this.EntryPrice != null)
                    hashCode = hashCode * 59 + this.EntryPrice.GetHashCode();
                if (this.Leverage != null)
                    hashCode = hashCode * 59 + this.Leverage.GetHashCode();
                if (this.AutoAddMargin != null)
                    hashCode = hashCode * 59 + this.AutoAddMargin.GetHashCode();
                if (this.PositionMargin != null)
                    hashCode = hashCode * 59 + this.PositionMargin.GetHashCode();
                if (this.LiqPrice != null)
                    hashCode = hashCode * 59 + this.LiqPrice.GetHashCode();
                if (this.BustPrice != null)
                    hashCode = hashCode * 59 + this.BustPrice.GetHashCode();
                if (this.OccClosingFee != null)
                    hashCode = hashCode * 59 + this.OccClosingFee.GetHashCode();
                if (this.OccFundingFee != null)
                    hashCode = hashCode * 59 + this.OccFundingFee.GetHashCode();
                if (this.TakeProfit != null)
                    hashCode = hashCode * 59 + this.TakeProfit.GetHashCode();
                if (this.StopLoss != null)
                    hashCode = hashCode * 59 + this.StopLoss.GetHashCode();
                if (this.TrailingStop != null)
                    hashCode = hashCode * 59 + this.TrailingStop.GetHashCode();
                if (this.PositionStatus != null)
                    hashCode = hashCode * 59 + this.PositionStatus.GetHashCode();
                if (this.DeleverageIndicator != null)
                    hashCode = hashCode * 59 + this.DeleverageIndicator.GetHashCode();
                if (this.OcCalcData != null)
                    hashCode = hashCode * 59 + this.OcCalcData.GetHashCode();
                if (this.OrderMargin != null)
                    hashCode = hashCode * 59 + this.OrderMargin.GetHashCode();
                if (this.WalletBalance != null)
                    hashCode = hashCode * 59 + this.WalletBalance.GetHashCode();
                if (this.UnrealisedPnl != null)
                    hashCode = hashCode * 59 + this.UnrealisedPnl.GetHashCode();
                if (this.RealisedPnl != null)
                    hashCode = hashCode * 59 + this.RealisedPnl.GetHashCode();
                if (this.CumRealisedPnl != null)
                    hashCode = hashCode * 59 + this.CumRealisedPnl.GetHashCode();
                if (this.CumCommission != null)
                    hashCode = hashCode * 59 + this.CumCommission.GetHashCode();
                if (this.CrossSeq != null)
                    hashCode = hashCode * 59 + this.CrossSeq.GetHashCode();
                if (this.PositionSeq != null)
                    hashCode = hashCode * 59 + this.PositionSeq.GetHashCode();
                if (this.CreatedAt != null)
                    hashCode = hashCode * 59 + this.CreatedAt.GetHashCode();
                if (this.UpdatedAt != null)
                    hashCode = hashCode * 59 + this.UpdatedAt.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
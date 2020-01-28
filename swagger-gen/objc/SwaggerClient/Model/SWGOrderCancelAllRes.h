#import <Foundation/Foundation.h>
#import "SWGObject.h"

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





@protocol SWGOrderCancelAllRes
@end

@interface SWGOrderCancelAllRes : SWGObject


@property(nonatomic) NSString* clOrdID;

@property(nonatomic) NSNumber* userId;

@property(nonatomic) NSString* side;

@property(nonatomic) NSString* orderType;

@property(nonatomic) NSString* price;

@property(nonatomic) NSString* qty;

@property(nonatomic) NSString* timeInForce;

@property(nonatomic) NSString* createType;

@property(nonatomic) NSString* orderStatus;

@property(nonatomic) NSNumber* leavesQty;

@property(nonatomic) NSNumber* leavesValue;

@property(nonatomic) NSString* createdAt;

@property(nonatomic) NSString* updatedAt;

@property(nonatomic) NSString* crossStatus;

@property(nonatomic) NSNumber* crossSeq;

@end

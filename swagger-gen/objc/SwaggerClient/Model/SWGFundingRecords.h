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





@protocol SWGFundingRecords
@end

@interface SWGFundingRecords : SWGObject


@property(nonatomic) NSNumber* _id;

@property(nonatomic) NSNumber* userId;

@property(nonatomic) NSString* coin;

@property(nonatomic) NSNumber* walletId;

@property(nonatomic) NSString* type;

@property(nonatomic) NSString* amount;

@property(nonatomic) NSString* txId;

@property(nonatomic) NSString* address;

@property(nonatomic) NSString* walletBalance;

@property(nonatomic) NSString* execTime;

@property(nonatomic) NSNumber* crossSeq;

@end

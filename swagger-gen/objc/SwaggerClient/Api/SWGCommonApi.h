#import <Foundation/Foundation.h>
#import "SWGApi.h"

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



@interface SWGCommonApi: NSObject <SWGApi>

extern NSString* kSWGCommonApiErrorDomain;
extern NSInteger kSWGCommonApiMissingParamErrorCode;

-(instancetype) initWithApiClient:(SWGApiClient *)apiClient NS_DESIGNATED_INITIALIZER;

/// Get bybit server time.
/// 
///
/// 
///  code:200 message:"Request was successful"
///
/// @return NSObject*
-(NSURLSessionTask*) commonGetWithCompletionHandler: 
    (void (^)(NSObject* output, NSError* error)) handler;



@end

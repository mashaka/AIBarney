//
//  API.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import Foundation
import Alamofire
import SwiftyJSON

class API {
    
    static func getUserList(completion: @escaping (JSON) -> ()) {
        let usersUrl = URL(string: "http://ryadom.me/api/users/")!
        
        Alamofire.request(usersUrl,
                          method: .get,
                          parameters: nil,
                          headers: AuthHelper.authHeader()).validate().responseJSON { response in
                            switch response.result {
                            case .success(let json): completion(JSON(json))
                            case .failure(_): print(API.error(response: response))
                            }
        }
    }
    
    static func getHistory(chatId: String, completion: @escaping (JSON) -> ()) {
        let historyUrl = URL(string: String(format: "http://ryadom.me/api/chat/%@/messages/", chatId))!
        
        Alamofire.request(historyUrl,
                          method: .get,
                          parameters: nil,
                          headers: AuthHelper.authHeader()).validate().responseJSON { response in
                            switch response.result {
                            case .success(let json): completion(JSON(json))
                            case .failure(_): print(API.error(response: response))
                            }
        }
    }
    
    static func getTips(chatId: String, completion: @escaping (JSON) -> ()) {
        let tipsUrl = URL(string: String(format: "http://ryadom.me/api/chat/%@/tips/", chatId))!
        
        Alamofire.request(tipsUrl,
                          method: .get,
                          parameters: nil,
                          headers: AuthHelper.authHeader()).validate().responseJSON { response in
                            switch response.result {
                            case .success(let json): completion(JSON(json))
                            case .failure(_): print(API.error(response: response))
                            }
        }
    }
    
    static func sendMessage(chatId: String, message: Message, completion: @escaping (Bool) -> ()) {
        let sendMessageUrl = URL(string: String(format: "http://ryadom.me/api/chat/%@/messages/", chatId))!
        
        Alamofire.request(sendMessageUrl,
                          method: .post,
                          parameters: message.apiParams(),
                          headers: AuthHelper.authHeader()).validate().responseJSON { response in
                            switch response.result {
                            case .success(_): completion(true)
                            case .failure(_): completion(false); print(API.error(response: response))
                            }
        }
    }
    
    // Error parsing ----------------------
    
    static func error(response: DataResponse<Any>) -> String {
        if(response.response == nil) {
            print(response.debugDescription)
            return "Connection Was Lost"
        }
        
        let statusCode: Int = response.response!.statusCode
        
        if(statusCode == 500) {
            print(response.debugDescription)
            return "500"
        }
        
        if(statusCode == 404) {
            print(response.debugDescription)
            return "404"
        }
        
        let jsonString = String(data: response.data!, encoding: String.Encoding.utf8)!
        let parsedError = JSON(parseJSON: jsonString)
        return parsedError.debugDescription
    }
}

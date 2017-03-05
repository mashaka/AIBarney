//
//  AuthHelper.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit

struct AuthData {
    static var shared: AuthData = AuthData()
    
    var token: String? = UserDefaults.standard.value(forKey: "token") as? String {
        didSet {
            UserDefaults.standard.set(token, forKey: "token")
        }
    }
    
    var id: String? = UserDefaults.standard.value(forKey: "id") as? String {
        didSet {
            UserDefaults.standard.set(id, forKey: "id")
        }
    }
    
    mutating func setFromQuery(query: String) -> Bool {
        let params: [String] = query.components(separatedBy: "&")
        for param in params {
            let keyValue: [String] = param.components(separatedBy: "=")
            switch keyValue[0] {
            case "token": token = keyValue[1]
            case "id": id = keyValue[1]
            case "error": return false
            default: continue
            }
        }
        return true
    }
}

class AuthHelper {
    static let shared: AuthHelper = AuthHelper()
    
    static var isAuthorized: Bool {
        return AuthData.shared.token != nil
    }
    
    static func authHeader() -> [String: String] {
        return ["Authorization": "Token \(AuthData.shared.token!)"]
    }
    
    static func loginToFacebook() {
        let fbLoginURL: URL = URL(string: "http://ryadom.me/oauth/login/facebook/")!
        UIApplication.shared.open(fbLoginURL, options: [:], completionHandler: nil)
    }
}
